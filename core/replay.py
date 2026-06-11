"""Brain Simulator -- Replay: deterministic re-execution + recorded playback.

Implements the SPEC-012 replay contract on top of :mod:`core.instrumentation`:

    * :func:`verify_replay` -- runs a seeded :class:`~core.simulation_engine.SimulationEngine`
      twice from the same seed and confirms every published
      :class:`~core.interfaces.ModuleState` is bit-identical across both runs
      (the SPEC-012 "replay reproduces identically" acceptance criterion).
    * :class:`ReplayRecorder` -- wraps an :class:`~core.instrumentation.InstrumentationLogger`
      to record a seeded run to JSONL/HDF5, stamping the seed as provenance.
    * :class:`ReplayPlayer` -- reads a recorded HDF5 file back as a sequence of
      per-tick frames, without re-running the simulation (e.g. for feeding a
      visualization in "replay mode").

Determinism depends on every stochastic module accepting an explicit ``seed``
/ ``rng`` and not touching the global NumPy RNG (see
:class:`~visualization.demo_brain.DemoRegion`,
:class:`~modules.reasoning.model_free.ModelFreeRL`, etc.). ``factory(seed)``
must construct a *fresh* engine -- and every stochastic module within it --
from ``seed`` so two calls with the same seed are independent and identical.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Iterator, List, Optional, Union

import h5py
import numpy as np

from core.brain_bus import BusSnapshot
from core.instrumentation import InstrumentationConfig, InstrumentationLogger
from core.simulation_engine import SimulationEngine

__all__ = [
    "EngineFactory",
    "ReplayMismatch",
    "ReplayRecorder",
    "ReplayPlayer",
    "run_seeded",
    "verify_replay",
]

# Builds a fresh, fully-wired engine from a seed (or None for a default seed).
EngineFactory = Callable[[Optional[int]], SimulationEngine]


def run_seeded(factory: EngineFactory, seed: Optional[int], n_steps: int) -> List[BusSnapshot]:
    """Build a fresh engine via ``factory(seed)`` and run it for ``n_steps`` ticks.

    Returns the list of :class:`~core.brain_bus.BusSnapshot` produced, one per tick.
    """
    engine = factory(seed)
    return [engine.step() for _ in range(n_steps)]


@dataclass(frozen=True)
class ReplayMismatch:
    """A single discrepancy found between two seeded runs by :func:`verify_replay`."""

    step: int
    module_id: str
    field: str


def verify_replay(factory: EngineFactory, seed: Optional[int], n_steps: int) -> List[ReplayMismatch]:
    """Run ``factory(seed)`` twice for ``n_steps`` ticks and diff the states.

    An empty result means every :class:`~core.interfaces.ModuleState` published
    on the BrainBus (``voltage``, ``firing_rate``, ``mean_weight``,
    ``active_synapses``) was bit-identical, tick-for-tick, across both runs --
    i.e. the simulation is deterministic for this ``seed`` (SPEC-012
    acceptance criterion).
    """
    run_a = run_seeded(factory, seed, n_steps)
    run_b = run_seeded(factory, seed, n_steps)

    mismatches: List[ReplayMismatch] = []
    for step, (snapshot_a, snapshot_b) in enumerate(zip(run_a, run_b)):
        for module_id, state_a in snapshot_a.states.items():
            state_b = snapshot_b.states.get(module_id)
            if state_b is None:
                mismatches.append(ReplayMismatch(step, module_id, "missing_state"))
                continue
            for field_name in ("voltage", "firing_rate"):
                if not np.array_equal(getattr(state_a, field_name), getattr(state_b, field_name)):
                    mismatches.append(ReplayMismatch(step, module_id, field_name))
            if state_a.mean_weight != state_b.mean_weight:
                mismatches.append(ReplayMismatch(step, module_id, "mean_weight"))
            if state_a.active_synapses != state_b.active_synapses:
                mismatches.append(ReplayMismatch(step, module_id, "active_synapses"))
    return mismatches


class ReplayRecorder:
    """Records a seeded simulation run to JSONL/HDF5 for later replay.

    Registers an :class:`~core.instrumentation.InstrumentationLogger` on
    ``engine`` as a StateRenderer and stamps the run's ``seed`` as HDF5
    provenance metadata (read back by :class:`ReplayPlayer`).

    Usage::

        engine = build_demo_brain(seed=42)
        with ReplayRecorder(engine, config, seed=42) as recorder:
            recorder.run(10_000)
    """

    def __init__(
        self,
        engine: SimulationEngine,
        config: InstrumentationConfig,
        seed: Optional[int] = None,
    ) -> None:
        self.engine = engine
        self.seed = seed
        self.logger = InstrumentationLogger(config)
        self.logger.set_seed(seed)
        engine.register_state_renderer(self.logger.record)

    def run(self, n_steps: int) -> None:
        """Advance :attr:`engine` by ``n_steps`` ticks, recording each one."""
        for _ in range(n_steps):
            self.engine.step()

    def close(self) -> None:
        self.logger.close()

    def __enter__(self) -> "ReplayRecorder":
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()


class ReplayPlayer:
    """Reads a :class:`~core.instrumentation.InstrumentationLogger` HDF5 file
    back as a sequence of per-tick frames, without re-running the simulation.
    """

    def __init__(self, hdf5_path: Union[str, Path]) -> None:
        self.hdf5_path = Path(hdf5_path)
        with h5py.File(self.hdf5_path, "r") as f:
            seed = int(f.attrs.get("seed", -1))
            self.seed: Optional[int] = None if seed == -1 else seed
            self.log_every_n_steps = int(f.attrs.get("log_every_n_steps", 1))
            self.module_ids: List[str] = list(f.keys())
            self.n_frames = (
                f[self.module_ids[0]]["timestamps"].shape[0] if self.module_ids else 0
            )

    def frames(self) -> Iterator[Dict[str, Dict[str, object]]]:
        """Yield one dict per recorded tick, keyed by ``module_id``.

        Each per-module entry contains ``timestamp_ms``, ``voltage``,
        ``firing_rate``, ``mean_weight``, ``active_synapses`` and (if
        recorded) ``spikes``.
        """
        with h5py.File(self.hdf5_path, "r") as f:
            for i in range(self.n_frames):
                frame: Dict[str, Dict[str, object]] = {}
                for module_id in self.module_ids:
                    group = f[module_id]
                    entry: Dict[str, object] = {
                        "timestamp_ms": float(group["timestamps"][i]),
                        "voltage": group["voltage"][i],
                        "firing_rate": group["firing_rate"][i],
                        "mean_weight": float(group["mean_weight"][i]),
                        "active_synapses": int(group["active_synapses"][i]),
                    }
                    if "spikes" in group:
                        entry["spikes"] = group["spikes"][i]
                    frame[module_id] = entry
                yield frame
