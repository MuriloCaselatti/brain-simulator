"""Brain Simulator -- Instrumentation: structured logs + HDF5 snapshots.

Implements SPEC-012 against the frozen SPEC-001/002 contracts. An
:class:`InstrumentationLogger` is a :class:`~core.brain_bus.BusSnapshot`
consumer -- register it via
:meth:`~core.simulation_engine.SimulationEngine.register_state_renderer` like
any other StateRenderer, so it never blocks the clock (exceptions it raises
are swallowed by the engine).

Two artifacts are written per run, both under ``InstrumentationConfig.output_dir``:

    * ``<run_name>.jsonl`` -- one JSON object per ``(step, module_id)`` sampled,
      with scalar summaries (mean voltage/firing rate, mean weight, active
      synapses, JSON-safe metadata). Queryable by ``module_id`` and timestep
      range via :func:`iter_logs`.
    * ``<run_name>.h5`` -- one HDF5 group per module, with resizable datasets
      per variable (``timestamps``, ``voltage``, ``firing_rate``, ``spikes``,
      ``mean_weight``, ``active_synapses``), one row per sampled step.

To avoid saturating disk on long runs, only every
``InstrumentationConfig.log_every_n_steps`` tick is sampled (ADR: SPEC-012).
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Union

import h5py
import numpy as np

from core.brain_bus import BusSnapshot

__all__ = [
    "InstrumentationConfig",
    "InstrumentationLogger",
    "iter_logs",
    "read_module_series",
    "list_modules",
]


@dataclass
class InstrumentationConfig:
    """Configuration for :class:`InstrumentationLogger`.

    Attributes:
        output_dir: Directory the JSONL/HDF5 artifacts are written to
            (created if missing).
        run_name: Basename for ``<run_name>.jsonl`` and ``<run_name>.h5``.
        log_every_n_steps: Sample one tick out of every ``N``. ``1`` records
            every tick (use only for short runs -- see module docstring).
        compression: ``h5py`` dataset compression filter, or ``None`` to
            disable compression.
        dtype: Floating point dtype used for HDF5 array datasets. ``float32``
            halves storage versus the ``float64`` arrays produced by NumPy.
    """

    output_dir: Union[str, Path] = "logs"
    run_name: str = "run"
    log_every_n_steps: int = 10
    compression: Optional[str] = "gzip"
    dtype: Any = np.float32

    def __post_init__(self) -> None:
        if self.log_every_n_steps < 1:
            raise ValueError("log_every_n_steps must be >= 1")


def _json_safe(value: Any) -> Any:
    """Recursively convert ``value`` into a JSON-serialisable structure."""
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.floating,)):
        return float(value)
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.bool_,)):
        return bool(value)
    if isinstance(value, dict):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(v) for v in value]
    return value


class InstrumentationLogger:
    """Records :class:`~core.brain_bus.BusSnapshot` ticks to JSONL + HDF5.

    Intended use::

        config = InstrumentationConfig(output_dir="logs", run_name="exp1")
        logger = InstrumentationLogger(config)
        engine.register_state_renderer(logger.record)
        engine.run(10_000)
        logger.close()

    Or as a context manager::

        with InstrumentationLogger(config) as logger:
            engine.register_state_renderer(logger.record)
            engine.run(10_000)
    """

    def __init__(self, config: InstrumentationConfig) -> None:
        self.config = config
        out_dir = Path(config.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        self.jsonl_path = out_dir / f"{config.run_name}.jsonl"
        self.hdf5_path = out_dir / f"{config.run_name}.h5"

        self._jsonl_file = open(self.jsonl_path, "w", encoding="utf-8")
        self._h5_file = h5py.File(self.hdf5_path, "w")
        self._h5_file.attrs["log_every_n_steps"] = config.log_every_n_steps

        self._tick_count = 0
        self._sampled_count = 0

    @property
    def sampled_steps(self) -> int:
        """Number of ticks that were actually sampled and written so far."""
        return self._sampled_count

    def set_seed(self, seed: Optional[int]) -> None:
        """Record the RNG seed used for this run as HDF5 provenance metadata."""
        self._h5_file.attrs["seed"] = -1 if seed is None else int(seed)

    def record(self, snapshot: BusSnapshot) -> None:
        """StateRenderer callback: sample and persist ``snapshot`` if due.

        Called once per tick by the :class:`~core.simulation_engine.SimulationEngine`.
        Only every :attr:`InstrumentationConfig.log_every_n_steps`-th tick is
        written to disk.
        """
        step = self._tick_count
        self._tick_count += 1
        if step % self.config.log_every_n_steps != 0:
            return

        spikes_by_module = {
            event.source_module: event.payload.spike_trains
            for event in snapshot.events
            if event.event_type == "module_output"
        }

        for module_id, state in snapshot.states.items():
            spikes = spikes_by_module.get(module_id)
            self._write_jsonl(step, state, spikes)
            self._write_hdf5(module_id, state, spikes)

        self._jsonl_file.flush()
        self._sampled_count += 1

    def _write_jsonl(self, step: int, state: Any, spikes: Optional[np.ndarray]) -> None:
        record: Dict[str, Any] = {
            "step": step,
            "timestamp_ms": state.timestamp_ms,
            "module_id": state.module_id,
            "n_neurons": state.n_neurons,
            "mean_voltage": float(np.mean(state.voltage)) if state.voltage.size else 0.0,
            "mean_firing_rate": (
                float(np.mean(state.firing_rate)) if state.firing_rate.size else 0.0
            ),
            "mean_weight": float(state.mean_weight),
            "active_synapses": int(state.active_synapses),
            "metadata": _json_safe(state.metadata),
        }
        if spikes is not None:
            record["n_spikes"] = int(np.sum(spikes))
        self._jsonl_file.write(json.dumps(record) + "\n")

    def _write_hdf5(self, module_id: str, state: Any, spikes: Optional[np.ndarray]) -> None:
        group = self._h5_file.require_group(module_id)
        dtype = self.config.dtype

        self._append(group, "timestamps", np.asarray([state.timestamp_ms], dtype=np.float64))
        self._append(group, "voltage", state.voltage[np.newaxis, :].astype(dtype))
        self._append(group, "firing_rate", state.firing_rate[np.newaxis, :].astype(dtype))
        self._append(
            group, "mean_weight", np.asarray([state.mean_weight], dtype=np.float64)
        )
        self._append(
            group, "active_synapses", np.asarray([state.active_synapses], dtype=np.int64)
        )
        if spikes is not None:
            self._append(group, "spikes", np.asarray(spikes)[np.newaxis, :].astype(dtype))

    def _append(self, group: h5py.Group, name: str, row: np.ndarray) -> None:
        if name not in group:
            group.create_dataset(
                name,
                data=row,
                maxshape=(None,) + row.shape[1:],
                chunks=True,
                compression=self.config.compression,
            )
        else:
            dataset = group[name]
            dataset.resize(dataset.shape[0] + row.shape[0], axis=0)
            dataset[-row.shape[0]:] = row

    def close(self) -> None:
        """Flush and close both the JSONL and HDF5 outputs."""
        self._jsonl_file.close()
        self._h5_file.close()

    def __enter__(self) -> "InstrumentationLogger":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()


def iter_logs(
    jsonl_path: Union[str, Path],
    module_id: Optional[str] = None,
    start_step: Optional[int] = None,
    end_step: Optional[int] = None,
) -> Iterator[Dict[str, Any]]:
    """Yield JSONL records, optionally filtered by ``module_id`` and step range.

    Args:
        jsonl_path: Path to a ``.jsonl`` file written by :class:`InstrumentationLogger`.
        module_id: If given, only records for this module are yielded.
        start_step: If given, only records with ``step >= start_step`` are yielded.
        end_step: If given, only records with ``step <= end_step`` are yielded.
    """
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if module_id is not None and record["module_id"] != module_id:
                continue
            if start_step is not None and record["step"] < start_step:
                continue
            if end_step is not None and record["step"] > end_step:
                continue
            yield record


def list_modules(hdf5_path: Union[str, Path]) -> List[str]:
    """Return the ``module_id``s recorded as top-level groups in ``hdf5_path``."""
    with h5py.File(hdf5_path, "r") as f:
        return list(f.keys())


def read_module_series(
    hdf5_path: Union[str, Path], module_id: str, variable: str
) -> np.ndarray:
    """Read the full time series for ``variable`` of ``module_id`` from HDF5.

    ``variable`` is one of ``"timestamps"``, ``"voltage"``, ``"firing_rate"``,
    ``"spikes"``, ``"mean_weight"``, ``"active_synapses"`` (whichever were
    written for that module).
    """
    with h5py.File(hdf5_path, "r") as f:
        return f[module_id][variable][...]
