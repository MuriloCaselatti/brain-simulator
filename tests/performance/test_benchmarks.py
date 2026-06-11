"""SPEC-013 -- Performance benchmarks against the target-hardware budget.

The target machine (Acer Aspire 3, 12 GB RAM, integrated GPU, no CUDA) sets the
budget SPEC-013 codifies:

    simulate_100ms(n_neurons=2000) < 5.0   # seconds of wall time
    visualizer_fps()              >= 25
    memory_usage_mb()             < 4096

These benchmarks are wall-clock / memory sensitive, so they are marked
``performance`` and run on the real hardware rather than in a constrained CI
sandbox.

A note on ``simulate_100ms``: a SPEC-003 :class:`~core.neuron.LIFPopulation`
pays a large *fixed* cost per Brian2 ``net.run`` call (~70-100 ms of Python /
codegen overhead, independent of the simulated interval). "Simulating 100 ms"
therefore means advancing 100 ms of *biological* time in one ``update`` call --
the amortized path the scientific suites already use -- not 100 separate 1 ms
ticks (whose cost is dominated by that fixed overhead and is benchmarked
indirectly elsewhere).

``visualizer_fps`` cannot be measured headlessly (the WebGL frame rate lives in
the browser). We instead benchmark the *backend* frame-production rate -- how
many fully-stepped, serialized frames per second the engine can feed the
renderer -- which is the throughput the 30 fps WebSocket stream draws from. The
true on-device WebGL frame rate is verified manually on the target hardware.
"""
import os
import sys
import time

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.interfaces import ModuleInputs, NeuromodulationSignal  # noqa: E402
from core.neuron import LIFPopulation  # noqa: E402

pytestmark = pytest.mark.performance

# SPEC-013 budget.
SIMULATE_100MS_BUDGET_S = 5.0
MIN_VISUALIZER_FPS = 25
MAX_MEMORY_MB = 4096


def _idle_inputs() -> ModuleInputs:
    return ModuleInputs(
        spike_trains=np.zeros(0),
        attention_signal=0.5,
        neuromodulation=NeuromodulationSignal(),
        timestamp_ms=0.0,
    )


def simulate_100ms(n_neurons: int = 2000) -> float:
    """Advance ``n_neurons`` LIF neurons by 100 ms of simulated time; return
    the wall-clock seconds taken."""
    pop = LIFPopulation("benchmark", n_neurons=n_neurons)
    pop.set_input_current(20.0)  # physiological, suprathreshold drive
    # Warm up Brian2 codegen so the measurement reflects steady-state cost.
    pop.update(1.0, _idle_inputs())

    start = time.perf_counter()
    pop.update(100.0, _idle_inputs())
    return time.perf_counter() - start


def visualizer_fps(n_frames: int = 120) -> float:
    """Backend frame-production rate of the demo brain (steps/serializations
    per second), the throughput feeding the visualization stream."""
    from visualization.demo_brain import build_demo_brain
    from visualization.server import serialize_frame

    engine = build_demo_brain(n_neurons=200, seed=7)
    engine.step()  # warm up

    start = time.perf_counter()
    for _ in range(n_frames):
        snapshot = engine.step()
        serialize_frame(
            snapshot,
            dopamine=1.0,
            noradrenaline=1.0,
            acetylcholine=1.0,
            playing=True,
            speed=1.0,
            isolated=set(),
            td_error=0.0,
        )
    elapsed = time.perf_counter() - start
    return n_frames / elapsed


def memory_usage_mb() -> float:
    """Resident set size (MB) of the current process."""
    import psutil

    return psutil.Process().memory_info().rss / (1024.0 * 1024.0)


# --- Benchmarks ---------------------------------------------------------------


def test_simulate_100ms_2000_neurons_under_budget():
    elapsed = simulate_100ms(n_neurons=2000)
    assert elapsed < SIMULATE_100MS_BUDGET_S, (
        f"simulate_100ms(2000) took {elapsed:.2f}s "
        f"(budget {SIMULATE_100MS_BUDGET_S}s)"
    )


def test_visualizer_backend_sustains_min_fps():
    fps = visualizer_fps()
    assert fps >= MIN_VISUALIZER_FPS, (
        f"backend frame production {fps:.1f} fps < {MIN_VISUALIZER_FPS} fps target"
    )


def test_memory_usage_within_budget():
    # Build a representative workload before measuring: a full 2000-neuron LIF
    # population plus the 8-region demo brain.
    from visualization.demo_brain import build_demo_brain

    pop = LIFPopulation("mem_probe", n_neurons=2000)
    pop.set_input_current(20.0)
    pop.update(10.0, _idle_inputs())

    engine = build_demo_brain(n_neurons=200, seed=7)
    engine.run(100.0)

    usage = memory_usage_mb()
    assert usage < MAX_MEMORY_MB, f"RSS {usage:.0f} MB exceeds {MAX_MEMORY_MB} MB budget"
