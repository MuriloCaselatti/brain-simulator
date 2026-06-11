"""Tests for SPEC-012 -- Instrumentation + Replay.

Exercises :mod:`core.instrumentation` (JSONL/HDF5 logging, sampled at every
``log_every_n_steps`` tick, queryable by module/timestep) and
:mod:`core.replay` (deterministic re-execution from a seed + recorded
playback) against a real :class:`~core.simulation_engine.SimulationEngine`
running the SPEC-009 demo brain.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.instrumentation import (  # noqa: E402
    InstrumentationConfig,
    InstrumentationLogger,
    iter_logs,
    list_modules,
    read_module_series,
)
from core.replay import ReplayPlayer, ReplayRecorder, run_seeded, verify_replay  # noqa: E402
from visualization.demo_brain import build_demo_brain  # noqa: E402


# -- InstrumentationLogger -------------------------------------------------------

def test_logger_samples_every_n_steps_and_writes_hdf5(tmp_path):
    engine = build_demo_brain(n_neurons=8, seed=1)
    config = InstrumentationConfig(output_dir=tmp_path, run_name="run1", log_every_n_steps=2)
    logger = InstrumentationLogger(config)
    engine.register_state_renderer(logger.record)

    for _ in range(10):
        engine.step()
    logger.close()

    # Ticks 0, 2, 4, 6, 8 are sampled (10 ticks, every 2nd starting at 0).
    assert logger.sampled_steps == 5

    modules = set(list_modules(logger.hdf5_path))
    assert modules == set(engine.execution_order)

    voltage = read_module_series(logger.hdf5_path, "sensory", "voltage")
    assert voltage.shape == (5, 8)
    assert voltage.dtype == np.float32

    spikes = read_module_series(logger.hdf5_path, "sensory", "spikes")
    assert spikes.shape == (5, 8)

    timestamps = read_module_series(logger.hdf5_path, "sensory", "timestamps")
    np.testing.assert_array_equal(timestamps, [0.0, 2.0, 4.0, 6.0, 8.0])


def test_logger_records_seed_as_hdf5_provenance(tmp_path):
    engine = build_demo_brain(n_neurons=4, seed=42)
    config = InstrumentationConfig(output_dir=tmp_path, run_name="run_seed", log_every_n_steps=1)
    logger = InstrumentationLogger(config)
    logger.set_seed(42)
    engine.register_state_renderer(logger.record)
    engine.step()
    logger.close()

    import h5py
    with h5py.File(logger.hdf5_path, "r") as f:
        assert int(f.attrs["seed"]) == 42


# -- iter_logs querying -----------------------------------------------------------

def test_iter_logs_filters_by_module_and_step_range(tmp_path):
    engine = build_demo_brain(n_neurons=4, seed=2)
    config = InstrumentationConfig(output_dir=tmp_path, run_name="run2", log_every_n_steps=1)
    logger = InstrumentationLogger(config)
    engine.register_state_renderer(logger.record)

    for _ in range(20):
        engine.step()
    logger.close()

    all_records = list(iter_logs(logger.jsonl_path))
    assert len(all_records) == 20 * len(engine.execution_order)

    sensory_only = list(iter_logs(logger.jsonl_path, module_id="sensory"))
    assert len(sensory_only) == 20
    assert all(r["module_id"] == "sensory" for r in sensory_only)

    windowed = list(iter_logs(logger.jsonl_path, module_id="sensory", start_step=5, end_step=9))
    assert [r["step"] for r in windowed] == [5, 6, 7, 8, 9]


# -- Replay determinism -------------------------------------------------------------

def test_verify_replay_is_deterministic_with_fixed_seed():
    factory = lambda seed: build_demo_brain(n_neurons=10, seed=seed)

    mismatches = verify_replay(factory, seed=123, n_steps=50)

    assert mismatches == []


def test_verify_replay_detects_divergence_across_seeds():
    # Different seeds must NOT produce identical voltage traces -- sanity
    # check that the comparison in verify_replay is actually sensitive to
    # the RNG stream, not vacuously true.
    factory = lambda seed: build_demo_brain(n_neurons=10, seed=seed)

    snapshots_a = run_seeded(factory, 123, 10)
    snapshots_b = run_seeded(factory, 456, 10)

    diverged = any(
        not np.array_equal(snap_a.states[module_id].voltage, snap_b.states[module_id].voltage)
        for snap_a, snap_b in zip(snapshots_a, snapshots_b)
        for module_id in snap_a.states
    )
    assert diverged


# -- ReplayRecorder / ReplayPlayer round trip ---------------------------------------

def test_replay_recorder_and_player_round_trip(tmp_path):
    engine = build_demo_brain(n_neurons=6, seed=7)
    config = InstrumentationConfig(output_dir=tmp_path, run_name="recorded", log_every_n_steps=1)

    with ReplayRecorder(engine, config, seed=7) as recorder:
        recorder.run(15)

    player = ReplayPlayer(config.output_dir / "recorded.h5")
    assert player.seed == 7
    assert player.n_frames == 15
    assert set(player.module_ids) == set(engine.execution_order)

    frames = list(player.frames())
    assert len(frames) == 15
    assert frames[0]["sensory"]["voltage"].shape == (6,)
    # Timestamps are recorded in tick order.
    timestamps = [frame["sensory"]["timestamp_ms"] for frame in frames]
    assert timestamps == sorted(timestamps)
