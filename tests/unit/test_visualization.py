"""Unit tests for the SPEC-009 visualization layer.

Covers the demo brain assembly (real engine, no cycles, 8 region states), frame
serialization (JSON-safe, correct encodings), and the SimulationRunner control
surface (play/pause/step/speed/isolate/reset) and its non-blocking renderer.

The browser-side Three.js code is not exercised here -- these tests validate the
Python contract the visualization streams over the WebSocket.
"""
from __future__ import annotations

import json
import time

import numpy as np
import pytest

from core.interfaces import CognitiveModule
from core.simulation_engine import SimulationEngine
from visualization.demo_brain import (
    EXECUTION_DEPENDENCIES,
    NEUROMODULATOR_ID,
    REGION_CONNECTIONS,
    REGION_LAYOUT,
    DemoRegion,
    build_demo_brain,
)
from visualization.server import (
    SimulationRunner,
    serialize_frame,
    serialize_layout,
)


# -- demo_brain ----------------------------------------------------------------

def test_demo_region_is_cognitive_module():
    region = DemoRegion("sensory", n_neurons=50, seed=0)
    assert isinstance(region, CognitiveModule)
    assert region.module_id == "sensory"
    assert region.n_neurons == 50
    assert region.get_synaptic_targets() == []


def test_demo_region_update_shapes_and_bounds():
    region = DemoRegion("sensory", n_neurons=64, intrinsic_hz=40.0, osc_freq_hz=1.0, seed=1)
    from core.interfaces import ModuleInputs, NeuromodulationSignal

    inputs = ModuleInputs(
        spike_trains=np.ones(64),
        attention_signal=1.0,
        neuromodulation=NeuromodulationSignal(),
        timestamp_ms=250.0,
    )
    out = region.update(1.0, inputs)
    assert out.spike_trains.shape == (64,)
    assert out.firing_rate.shape == (64,)
    assert set(np.unique(out.spike_trains)).issubset({0.0, 1.0})
    assert np.all(out.firing_rate >= 0.0)

    state = region.get_state()
    assert state.n_neurons == 64
    assert state.voltage.shape == (64,)
    assert state.timestamp_ms == 250.0


def test_build_demo_brain_has_eight_regions_and_no_cycle():
    engine = build_demo_brain(n_neurons=40)
    # All 8 anatomical regions plus the neuromodulator are registered.
    assert set(REGION_LAYOUT).issubset(set(engine._modules))
    assert NEUROMODULATOR_ID in engine._modules
    # execution_order computes without raising (no dependency cycle).
    order = engine.execution_order
    assert len(order) == len(REGION_LAYOUT) + 1
    # Every region precedes the modules that depend on it.
    for module_id, deps in EXECUTION_DEPENDENCIES.items():
        for dep in deps:
            assert order.index(dep) < order.index(module_id)


def test_demo_brain_step_produces_region_states():
    engine = build_demo_brain(n_neurons=40)
    snapshot = engine.step()
    for region_id in REGION_LAYOUT:
        assert region_id in snapshot.states
        assert snapshot.states[region_id].firing_rate.shape == (40,)


def test_demo_brain_activity_propagates_from_source():
    engine = build_demo_brain(n_neurons=120, seed=3)
    # Run long enough for the oscillatory sensory drive to fire and propagate.
    rates = {rid: 0.0 for rid in REGION_LAYOUT}
    for _ in range(400):
        snap = engine.step()
        for rid in REGION_LAYOUT:
            rates[rid] = max(rates[rid], float(snap.states[rid].firing_rate.mean()))
    # The driven sensory region and at least one downstream region were active.
    assert rates["sensory"] > 1.0
    assert rates["working_memory"] > 1.0


# -- serialization -------------------------------------------------------------

def test_serialize_layout_shape_is_json_safe():
    layout = serialize_layout()
    assert layout["type"] == "layout"
    assert len(layout["regions"]) == len(REGION_LAYOUT)
    assert len(layout["connections"]) == len(REGION_CONNECTIONS)
    # Must round-trip through JSON.
    json.dumps(layout)


def test_serialize_frame_is_json_safe_and_complete():
    engine = build_demo_brain(n_neurons=40)
    snapshot = engine.step()
    frame = serialize_frame(
        snapshot,
        dopamine=1.5,
        noradrenaline=1.0,
        acetylcholine=1.0,
        playing=True,
        speed=2.0,
        isolated={"pfc"},
    )
    assert frame["type"] == "frame"
    assert frame["dopamine"] == 1.5
    assert frame["playing"] is True
    assert len(frame["regions"]) == len(REGION_LAYOUT)
    by_id = {r["id"]: r for r in frame["regions"]}
    assert by_id["pfc"]["isolated"] is True
    for region in frame["regions"]:
        assert isinstance(region["firing_rate"], float)
        assert isinstance(region["spike"], bool)
    # Whole frame must be JSON-serializable (no numpy scalars leaking through).
    json.dumps(frame)


# -- SimulationRunner ----------------------------------------------------------

def test_runner_step_command_advances_one_tick():
    runner = SimulationRunner(build_demo_brain(n_neurons=30))
    assert runner.engine.current_time_ms == 0.0
    runner.handle_command({"cmd": "step"})
    # In step mode the loop drains one request; emulate the loop body directly.
    assert runner._step_requests == 1
    runner._step_requests -= 1
    runner._advance()
    assert runner.engine.current_time_ms == 1.0
    assert runner.latest_frame() is not None


def test_runner_play_pause_flags():
    runner = SimulationRunner(build_demo_brain(n_neurons=30))
    runner.handle_command({"cmd": "play"})
    assert runner.playing is True
    runner.handle_command({"cmd": "pause"})
    assert runner.playing is False


def test_runner_speed_is_clamped():
    runner = SimulationRunner(build_demo_brain(n_neurons=30))
    runner.handle_command({"cmd": "speed", "value": 1000})
    assert runner.speed == 50.0
    runner.handle_command({"cmd": "speed", "value": 0.0})
    assert runner.speed == 0.1
    runner.handle_command({"cmd": "speed", "value": "bad"})
    assert runner.speed == 0.1  # unchanged on invalid input


def test_runner_isolate_toggles():
    runner = SimulationRunner(build_demo_brain(n_neurons=30))
    runner.handle_command({"cmd": "isolate", "module": "pfc"})
    assert "pfc" in runner.isolated
    runner.handle_command({"cmd": "isolate", "module": "pfc"})
    assert "pfc" not in runner.isolated
    # Unknown module ignored.
    runner.handle_command({"cmd": "isolate", "module": "nonexistent"})
    assert runner.isolated == set()
    runner.handle_command({"cmd": "isolate", "module": "sensory"})
    runner.handle_command({"cmd": "clear_isolate"})
    assert runner.isolated == set()


def test_runner_reset_rewinds_clock():
    runner = SimulationRunner(build_demo_brain(n_neurons=30))
    runner._advance()
    runner._advance()
    assert runner.engine.current_time_ms == 2.0
    runner.handle_command({"cmd": "reset"})
    assert runner.engine.current_time_ms == 0.0
    assert runner.playing is False


def test_runner_renderer_never_blocks_clock():
    # The renderer callback is registered on a real engine; a slow/raising
    # callback must not break stepping. Here we assert the callback runs and
    # populates a frame, and that stepping continues to advance time.
    runner = SimulationRunner(build_demo_brain(n_neurons=30))
    for _ in range(5):
        runner._advance()
    assert runner.engine.current_time_ms == 5.0
    frame = runner.latest_frame()
    assert frame is not None
    assert frame["type"] == "frame"


def test_runner_thread_runs_when_playing():
    runner = SimulationRunner(build_demo_brain(n_neurons=30))
    runner.handle_command({"cmd": "speed", "value": 20})
    runner.handle_command({"cmd": "play"})
    runner.start()
    try:
        time.sleep(0.2)
        assert runner.engine.current_time_ms > 0.0
        assert runner.latest_frame() is not None
    finally:
        runner.stop()
