"""Tests for SPEC-006 -- Predictive Coding hierarchy.

PredictiveLayer + PredictiveCodingHierarchy implement a three-level
Rao & Ballard (1999) predictive-coding model exposed through the frozen
SPEC-001 :class:`~core.interfaces.CognitiveModule` contract.

The three suites map directly onto the SPEC-006 acceptance criteria:
    1. prediction error decreases with repeated training of the same stimulus;
    2. a top-down prediction modulates the lower-level representation;
    3. precision (attention) scales the weight of the prediction error.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.interfaces import (  # noqa: E402
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)
from modules.predictive_coding.hierarchy import PredictiveCodingHierarchy  # noqa: E402
from modules.predictive_coding.layer import PredictiveLayer  # noqa: E402


def _inputs(spike_trains, attention_signal=1.0, neuromodulation=None, timestamp_ms=0.0):
    return ModuleInputs(
        spike_trains=np.asarray(spike_trains, dtype=float),
        attention_signal=attention_signal,
        neuromodulation=neuromodulation or NeuromodulationSignal(),
        timestamp_ms=timestamp_ms,
    )


def _stimulus(size=64, seed=0):
    rng = np.random.default_rng(seed)
    return rng.random(size)


# --- CognitiveModule contract conformance -----------------------------------


def test_is_cognitive_module():
    h = PredictiveCodingHierarchy(rng=np.random.default_rng(0))
    assert isinstance(h, CognitiveModule)


def test_update_returns_module_outputs():
    h = PredictiveCodingHierarchy(rng=np.random.default_rng(0))
    out = h.update(1.0, _inputs(_stimulus()))
    assert isinstance(out, ModuleOutputs)
    assert out.spike_trains.shape == (h.n_neurons,)
    assert out.firing_rate.shape == (h.n_neurons,)
    assert set(out.spike_trains).issubset({0.0, 1.0})
    assert "prediction_error_per_level" in out.internal_state
    assert len(out.internal_state["prediction_error_per_level"]) == 3


def test_get_state_contract():
    h = PredictiveCodingHierarchy(rng=np.random.default_rng(0))
    h.update(1.0, _inputs(_stimulus()))
    state = h.get_state()
    assert isinstance(state, ModuleState)
    assert state.module_id == h.module_id
    assert state.n_neurons == h.n_neurons
    assert state.voltage.shape == (h.n_neurons,)
    assert state.firing_rate.shape == (h.n_neurons,)


def test_synaptic_targets_are_generative_weights():
    h = PredictiveCodingHierarchy(rng=np.random.default_rng(0))
    targets = h.get_synaptic_targets()
    assert len(targets) == 3
    for t, layer in zip(targets, h.layers):
        assert isinstance(t, SynapticTarget)
        assert t.weight_matrix.shape == (layer.n_below, layer.n_units)


def test_reset_clears_representation():
    h = PredictiveCodingHierarchy(rng=np.random.default_rng(0))
    for _ in range(5):
        h.update(1.0, _inputs(_stimulus()))
    h.reset()
    assert all(np.allclose(layer.r, 0.0) for layer in h.layers)


def test_requires_three_levels():
    with pytest.raises(ValueError):
        PredictiveCodingHierarchy(level_sizes=(32, 16))


# --- Criterion #1: error decreases with repeated training -------------------


def test_prediction_error_decreases_with_training():
    h = PredictiveCodingHierarchy(input_size=64, rng=np.random.default_rng(1))
    stim = _stimulus(64, seed=42)

    first = h.update(1.0, _inputs(stim)).internal_state["total_prediction_error"]
    for _ in range(150):
        out = h.update(1.0, _inputs(stim))
    last = out.internal_state["total_prediction_error"]

    assert last < first
    # The bottom level should explain most of the stimulus after training.
    assert last < 0.5 * first


def test_error_does_not_decrease_when_learning_frozen():
    h = PredictiveCodingHierarchy(input_size=64, rng=np.random.default_rng(2))
    stim = _stimulus(64, seed=7)
    h.set_learning_enabled(False)

    first = h.update(1.0, _inputs(stim)).internal_state["total_prediction_error"]
    for _ in range(150):
        out = h.update(1.0, _inputs(stim))
    last = out.internal_state["total_prediction_error"]

    # Without plasticity the generative weights cannot learn the stimulus, so
    # there is no sustained, large reduction in error.
    assert last > 0.5 * first


# --- Criterion #2: top-down prediction modulates the lower level ------------


def test_top_down_prior_modulates_lower_representation():
    seed = np.random.default_rng(3)
    stim = _stimulus(64, seed=99)

    baseline = PredictiveCodingHierarchy(
        input_size=64, rng=np.random.default_rng(3)
    )
    primed = PredictiveCodingHierarchy(input_size=64, rng=np.random.default_rng(3))
    primed.set_top_down_prior(np.ones(primed.level_sizes[2]) * 2.0)

    for _ in range(10):
        baseline.update(1.0, _inputs(stim))
        primed.update(1.0, _inputs(stim))

    r1_baseline = baseline.layers[0].r.copy()
    r1_primed = primed.layers[0].r.copy()

    # A top-level prior changes the lowest representation level.
    assert not np.allclose(r1_baseline, r1_primed, atol=1e-3)


def test_top_down_prediction_reaches_input_level():
    h = PredictiveCodingHierarchy(input_size=64, rng=np.random.default_rng(4))
    stim = _stimulus(64, seed=5)
    out = h.update(1.0, _inputs(stim))
    top_prediction = out.internal_state["top_prediction"]
    # The L1 -> input generative prediction has the input's shape and is used
    # to form the level-0 error.
    assert top_prediction.shape == (h.input_size,)


# --- Criterion #3: precision (attention) scales the error weight ------------


def test_attention_scales_weighted_error():
    h = PredictiveCodingHierarchy(input_size=64, rng=np.random.default_rng(5))
    stim = _stimulus(64, seed=11)

    low = h.update(1.0, _inputs(stim, attention_signal=0.0))
    pi_low = low.internal_state["precision"]

    h.reset()
    h = PredictiveCodingHierarchy(input_size=64, rng=np.random.default_rng(5))
    high = h.update(1.0, _inputs(stim, attention_signal=1.0))
    pi_high = high.internal_state["precision"]

    # Higher attention -> higher precision -> larger weight on the error.
    assert pi_high > pi_low
    assert high.internal_state["weighted_error_per_level"][0] > (
        low.internal_state["weighted_error_per_level"][0]
    )


def test_acetylcholine_gates_precision():
    h = PredictiveCodingHierarchy(input_size=64, rng=np.random.default_rng(6))
    stim = _stimulus(64, seed=13)

    base = h.update(1.0, _inputs(stim, attention_signal=0.5)).internal_state[
        "precision"
    ]

    h.apply_neuromodulation(NeuromodulationSignal(acetylcholine=0.0))
    gated = h.update(1.0, _inputs(stim, attention_signal=0.5)).internal_state[
        "precision"
    ]

    assert gated < base
    assert gated == pytest.approx(0.0)


# --- PredictiveLayer unit behaviour -----------------------------------------


def test_layer_prediction_and_error_shapes():
    layer = PredictiveLayer("L1", n_units=8, n_below=16, rng=np.random.default_rng(0))
    assert layer.predict().shape == (16,)
    err = layer.compute_error(np.ones(16))
    assert err.shape == (16,)


def test_layer_learning_reduces_error_for_fixed_representation():
    layer = PredictiveLayer(
        "L1", n_units=8, n_below=16, learning_rate=0.1, rng=np.random.default_rng(0)
    )
    layer.r = np.ones(8)
    target = np.random.default_rng(0).random(16)

    layer.compute_error(target)
    first = float(np.linalg.norm(layer.error))
    for _ in range(50):
        layer.compute_error(target)
        layer.learn(precision=1.0)
    layer.compute_error(target)
    last = float(np.linalg.norm(layer.error))

    assert last < first
