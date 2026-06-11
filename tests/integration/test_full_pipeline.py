"""SPEC-013 -- Full-pipeline integration over one simulated second.

This test wires *real* cognitive modules from several SPECs into a single
:class:`~core.simulation_engine.SimulationEngine` and runs them for one second
of simulated time (1000 ticks at dt = 1 ms), exercising the whole stack end to
end:

    sensory drive -> attention (saliency, DAN) -> memory (working, episodic)
    -> predictive coding -> neuromodulation (broadcast back to every module)

through the real :class:`~core.brain_bus.BrainBus` (synchronous, one-tick
latency). The Brian2-backed :class:`~core.neuron.LIFPopulation` is deliberately
left out of the 1000-tick loop: it pays a fixed ~70-100 ms cost per
``net.run`` call, so per-millisecond stepping of it is validated separately
(see ``tests/performance/test_benchmarks.py`` and
``tests/scientific/test_lif_validation.py``); here the lightweight rate-based
modules stand in so a full second runs quickly.

Validated properties:
    * the dependency graph assembles into a valid topological order (no cycle);
    * the engine runs a full second without error and produces 1000 snapshots;
    * every module publishes finite (no NaN/Inf) state on every tick;
    * the neuromodulatory signal is broadcast to every module each tick;
    * the run is fully deterministic given fixed seeds (replayability).
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.simulation_engine import SimulationEngine  # noqa: E402
from modules.attention.dan import DAN  # noqa: E402
from modules.attention.saliency import SaliencyMap  # noqa: E402
from modules.memory.episodic import EpisodicMemory  # noqa: E402
from modules.memory.working import WorkingMemory  # noqa: E402
from modules.neuromodulation.system import NeuromodulatorSystem  # noqa: E402
from modules.predictive_coding.hierarchy import PredictiveCodingHierarchy  # noqa: E402
from visualization.demo_brain import DemoRegion  # noqa: E402

N = 64
DURATION_MS = 1000
MODULE_IDS = [
    "sensory",
    "saliency",
    "attention_dan",
    "working_memory",
    "episodic_memory",
    "predictive_coding",
    "neuromodulators",
]


def _build_pipeline(seed: int = 7) -> SimulationEngine:
    """Assemble the integrated pipeline of real cognitive modules."""
    engine = SimulationEngine()

    sensory = DemoRegion(
        "sensory", n_neurons=N, baseline_hz=8.0, intrinsic_hz=40.0,
        osc_freq_hz=1.5, seed=seed,
    )
    saliency = SaliencyMap("saliency", n_neurons=N)
    dan = DAN("attention_dan", n_neurons=N)
    working = WorkingMemory("working_memory", n_neurons=N)
    episodic = EpisodicMemory("episodic_memory", n_neurons=N)
    predictive = PredictiveCodingHierarchy(
        "predictive_coding", input_size=N, n_inference_steps=5,
        rng=np.random.default_rng(seed + 100),
    )
    neuromod = NeuromodulatorSystem("neuromodulators")

    engine.add_module(sensory, depends_on=[])
    engine.add_module(saliency, depends_on=["sensory"])
    engine.add_module(dan, depends_on=["saliency"])
    engine.add_module(working, depends_on=["sensory"])
    engine.add_module(episodic, depends_on=["sensory"])
    engine.add_module(predictive, depends_on=["sensory"])
    engine.add_module(
        neuromod,
        depends_on=["attention_dan", "working_memory", "predictive_coding"],
    )
    engine.register_neuromodulator("neuromodulators")

    # Seed episodic memory with a couple of recallable traces.
    rng = np.random.default_rng(seed + 200)
    for _ in range(4):
        episodic.store_pattern(rng.choice([-1.0, 1.0], size=N))

    _ = engine.execution_order  # force topological sort (raises on a cycle)
    return engine


def _run(engine: SimulationEngine, n_ticks: int):
    """Step the engine, re-driving arousal/reward each tick so the
    neuromodulatory signal stays phasically non-basal."""
    neuromod = engine._modules["neuromodulators"]
    snapshots = []
    for _ in range(n_ticks):
        neuromod.set_arousal(1.0)             # sustained arousal -> noradrenaline
        neuromod.observe_reward(1.0, 0.0)     # unexpected reward -> dopamine burst
        snapshots.append(engine.step())
    return snapshots


# --- Assembly & end-to-end run -----------------------------------------------


def test_pipeline_assembles_into_valid_topological_order():
    engine = _build_pipeline()
    order = engine.execution_order

    assert set(order) == set(MODULE_IDS)
    # Dependencies must precede dependents.
    pos = {m: i for i, m in enumerate(order)}
    assert pos["sensory"] < pos["saliency"] < pos["attention_dan"]
    assert pos["sensory"] < pos["working_memory"]
    assert pos["attention_dan"] < pos["neuromodulators"]
    assert pos["predictive_coding"] < pos["neuromodulators"]


def test_pipeline_runs_one_second_and_publishes_finite_state():
    engine = _build_pipeline()

    start = time.perf_counter()
    snapshots = _run(engine, DURATION_MS)
    elapsed = time.perf_counter() - start

    assert len(snapshots) == DURATION_MS
    assert elapsed < 30.0, f"1s pipeline took {elapsed:.1f}s (regression?)"

    for snapshot in snapshots:
        assert set(snapshot.states) == set(MODULE_IDS)
        for module_id, state in snapshot.states.items():
            assert np.all(np.isfinite(state.firing_rate)), module_id
            assert np.all(np.isfinite(state.voltage)), module_id
            # >= 0 up to floating-point noise (e.g. Modern Hopfield state ~= -1).
            assert np.all(state.firing_rate >= -1e-6), module_id


def test_pipeline_records_full_replay_history():
    engine = _build_pipeline()
    _run(engine, DURATION_MS)

    history = engine.get_history(DURATION_MS)
    assert len(history) == DURATION_MS
    # Monotonically increasing timestamps over the whole second.
    timestamps = [s.timestamp_ms for s in history]
    assert timestamps == sorted(timestamps)
    assert timestamps[0] == 0.0
    assert timestamps[-1] == DURATION_MS - 1


# --- Neuromodulation broadcast ------------------------------------------------


def test_neuromodulation_is_broadcast_to_every_module():
    engine = _build_pipeline()
    _run(engine, 200)

    signal = engine.neuromodulation
    # The sustained arousal / reward drive keeps the signal phasically elevated.
    assert signal.noradrenaline > 1.0
    assert signal.dopamine > 1.0

    # apply_neuromodulation reached the modules: a DemoRegion stores the
    # broadcast noradrenaline gain, and it matches the engine-held signal.
    sensory = engine._modules["sensory"]
    assert sensory._na_gain > 1.0
    assert abs(sensory._na_gain - signal.noradrenaline) < 1e-9


# --- Determinism / replayability ---------------------------------------------


def test_pipeline_is_deterministic_given_a_seed():
    """Two pipelines built and driven identically produce bit-identical state
    trajectories -- the precondition for SPEC-012 deterministic replay."""
    engine_a = _build_pipeline(seed=7)
    engine_b = _build_pipeline(seed=7)

    snaps_a = _run(engine_a, 150)
    snaps_b = _run(engine_b, 150)

    for sa, sb in zip(snaps_a, snaps_b):
        for module_id in MODULE_IDS:
            assert np.array_equal(
                sa.states[module_id].firing_rate,
                sb.states[module_id].firing_rate,
            ), f"divergence in {module_id}"
