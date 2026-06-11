"""Tests for SPEC-003 -- LIFPopulation (Brian2-backed).

Covers the :class:`~core.interfaces.CognitiveModule` contract and basic
neuron dynamics. Scientific validation (firing rate ranges, all-or-none law)
lives in ``tests/scientific/test_lif_validation.py``.
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
)
from core.neuron import (  # noqa: E402
    MAX_NEURONS,
    MIN_NEURONS,
    V_REST,
    V_THRESH,
    LIFPopulation,
)


def make_inputs(n_pre: int = 0, attention_signal: float = 0.5) -> ModuleInputs:
    return ModuleInputs(
        spike_trains=np.zeros(n_pre),
        attention_signal=attention_signal,
        neuromodulation=NeuromodulationSignal(),
        timestamp_ms=0.0,
    )


# --- Construction ------------------------------------------------------------


def test_is_cognitive_module():
    pop = LIFPopulation("test_pop", n_neurons=MIN_NEURONS)
    assert isinstance(pop, CognitiveModule)
    assert pop.module_id == "test_pop"
    assert pop.n_neurons == MIN_NEURONS


@pytest.mark.parametrize("n_neurons", [MIN_NEURONS - 1, MAX_NEURONS + 1, 0])
def test_population_size_out_of_range_rejected(n_neurons):
    with pytest.raises(ValueError):
        LIFPopulation("bad", n_neurons=n_neurons)


# --- update() ------------------------------------------------------------------


def test_update_returns_correct_shapes_and_types():
    pop = LIFPopulation("pop", n_neurons=MIN_NEURONS)
    outputs = pop.update(dt=1.0, inputs=make_inputs())

    assert isinstance(outputs, ModuleOutputs)
    assert outputs.spike_trains.shape == (MIN_NEURONS,)
    assert outputs.firing_rate.shape == (MIN_NEURONS,)
    assert set(np.unique(outputs.spike_trains)).issubset({0.0, 1.0})
    assert np.all(outputs.firing_rate >= 0.0)


def test_resting_population_does_not_spike():
    pop = LIFPopulation("pop", n_neurons=MIN_NEURONS)
    outputs = pop.update(dt=5.0, inputs=make_inputs())
    assert np.all(outputs.spike_trains == 0.0)
    assert np.all(outputs.firing_rate == 0.0)


# --- get_state() ---------------------------------------------------------------


def test_get_state_returns_module_state():
    pop = LIFPopulation("pop", n_neurons=MIN_NEURONS)
    state = pop.get_state()

    assert isinstance(state, ModuleState)
    assert state.module_id == "pop"
    assert state.n_neurons == MIN_NEURONS
    assert state.voltage.shape == (MIN_NEURONS,)
    assert state.firing_rate.shape == (MIN_NEURONS,)
    # Resting potential before any current is injected.
    assert np.allclose(state.voltage, V_REST)


# --- apply_neuromodulation() ----------------------------------------------------


def test_noradrenaline_lowers_threshold():
    pop = LIFPopulation("pop", n_neurons=MIN_NEURONS)
    base_threshold = pop.get_state().metadata["v_thresh_mV"]

    pop.apply_neuromodulation(NeuromodulationSignal(noradrenaline=1.5))
    raised_threshold = pop.get_state().metadata["v_thresh_mV"]

    assert raised_threshold < base_threshold
    assert np.isclose(base_threshold, V_THRESH)


def test_acetylcholine_gain_is_clamped_nonnegative():
    pop = LIFPopulation("pop", n_neurons=MIN_NEURONS)
    pop.apply_neuromodulation(NeuromodulationSignal(acetylcholine=-1.0))
    assert pop._acetylcholine_gain == 0.0


# --- get_synaptic_targets() ------------------------------------------------------


def test_get_synaptic_targets_empty_by_default():
    pop = LIFPopulation("pop", n_neurons=MIN_NEURONS)
    assert pop.get_synaptic_targets() == []


# --- reset() -----------------------------------------------------------------------


def test_reset_restores_resting_potential_and_clears_history():
    pop = LIFPopulation("pop", n_neurons=MIN_NEURONS)
    pop.set_input_current(20.0)
    pop.update(dt=10.0, inputs=make_inputs())

    pop.reset()

    state = pop.get_state()
    assert np.allclose(state.voltage, V_REST)
    assert np.all(state.firing_rate == 0.0)
    assert np.all(pop._external_current == 0.0)


# --- set_input_current() ------------------------------------------------------------


def test_set_input_current_validates_shape():
    pop = LIFPopulation("pop", n_neurons=MIN_NEURONS)
    with pytest.raises(ValueError):
        pop.set_input_current(np.zeros(MIN_NEURONS - 1))


def test_set_input_current_scalar_broadcasts():
    pop = LIFPopulation("pop", n_neurons=MIN_NEURONS)
    pop.set_input_current(5.0)
    assert pop._external_current.shape == (MIN_NEURONS,)
    assert np.all(pop._external_current == 5.0)
