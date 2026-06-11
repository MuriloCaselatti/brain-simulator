"""Tests for SPEC-003 -- LearningEngine + PlasticityScheduler.

Covers the :class:`~core.interfaces.CognitiveModule` contract, STDP gating
via neuromodulation, and TD-Learning. The Bi & Poo 1998 STDP curve and the
LIF firing-rate range are validated separately in
``tests/scientific/test_lif_validation.py``.
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
from core.learning_engine import (  # noqa: E402
    TD_ALPHA,
    TD_GAMMA,
    LearningEngine,
    PlasticityScheduler,
)
from core.synapse import STDPSynapse  # noqa: E402


def make_inputs(spike_trains, neuromodulation=None, timestamp_ms=0.0):
    return ModuleInputs(
        spike_trains=np.asarray(spike_trains, dtype=float),
        attention_signal=1.0,
        neuromodulation=neuromodulation or NeuromodulationSignal(),
        timestamp_ms=timestamp_ms,
    )


# --- Construction / contract --------------------------------------------------------


def test_is_cognitive_module():
    engine = LearningEngine()
    assert isinstance(engine, CognitiveModule)
    assert engine.n_neurons == 0
    assert engine.alpha == TD_ALPHA
    assert engine.gamma == TD_GAMMA


def test_get_synaptic_targets_reflects_registered_projections():
    engine = LearningEngine()
    syn = STDPSynapse(n_pre=2, n_post=2, weight_init=0.5)
    engine.register_projection(syn, source_module="pre", target_module="post")

    targets = engine.get_synaptic_targets()
    assert len(targets) == 1
    assert isinstance(targets[0], SynapticTarget)
    assert targets[0].source_module == "pre"
    assert targets[0].target_module == "post"
    assert targets[0].weight_matrix is syn.weight_matrix


# --- update() / plasticity gating -----------------------------------------------------


def test_update_applies_stdp_when_acetylcholine_above_threshold():
    engine = LearningEngine()
    syn = STDPSynapse(n_pre=1, n_post=1, weight_init=0.5)
    engine.register_projection(syn, source_module="pre", target_module="post")
    w0 = syn.weight_matrix.copy()

    inputs = make_inputs([1.0, 1.0], neuromodulation=NeuromodulationSignal(acetylcholine=1.0))
    outputs = engine.update(dt=1.0, inputs=inputs)

    assert isinstance(outputs, ModuleOutputs)
    assert outputs.internal_state["plastic"] is True
    assert not np.array_equal(syn.weight_matrix, w0)


def test_update_skips_stdp_when_acetylcholine_below_threshold():
    engine = LearningEngine()
    syn = STDPSynapse(n_pre=1, n_post=1, weight_init=0.5)
    engine.register_projection(syn, source_module="pre", target_module="post")
    w0 = syn.weight_matrix.copy()

    inputs = make_inputs([1.0, 1.0], neuromodulation=NeuromodulationSignal(acetylcholine=0.0))
    outputs = engine.update(dt=1.0, inputs=inputs)

    assert outputs.internal_state["plastic"] is False
    assert np.array_equal(syn.weight_matrix, w0)


def test_scheduler_disable_overrides_acetylcholine():
    engine = LearningEngine()
    syn = STDPSynapse(n_pre=1, n_post=1, weight_init=0.5)
    engine.register_projection(syn, source_module="pre", target_module="post")
    engine.scheduler.disable()
    w0 = syn.weight_matrix.copy()

    inputs = make_inputs([1.0, 1.0], neuromodulation=NeuromodulationSignal(acetylcholine=1.0))
    engine.update(dt=1.0, inputs=inputs)

    assert np.array_equal(syn.weight_matrix, w0)


# --- get_state() ----------------------------------------------------------------------


def test_get_state_reports_mean_weight_and_active_synapses():
    engine = LearningEngine()
    syn = STDPSynapse(n_pre=2, n_post=2, weight_init=0.5)
    engine.register_projection(syn, source_module="pre", target_module="post")

    state = engine.get_state()
    assert isinstance(state, ModuleState)
    assert state.n_neurons == 0
    assert state.mean_weight == pytest.approx(0.5)
    assert state.active_synapses == 4


# --- TD-Learning -------------------------------------------------------------------------


def test_td_error_positive_when_reward_exceeds_expectation():
    engine = LearningEngine()
    engine.value_estimate = 0.0

    td_error = engine.compute_td_error(reward=1.0, value_next=0.0)

    assert td_error > 0
    assert engine.last_td_error == td_error


def test_td_error_negative_when_reward_below_expectation():
    engine = LearningEngine()
    engine.value_estimate = 1.0

    td_error = engine.compute_td_error(reward=0.0, value_next=0.0)

    assert td_error < 0


def test_apply_td_update_moves_value_toward_target():
    engine = LearningEngine()
    engine.value_estimate = 0.0
    engine.compute_td_error(reward=1.0, value_next=0.0)

    new_value = engine.apply_td_update()

    assert new_value == pytest.approx(TD_ALPHA * 1.0)


def test_apply_td_update_scaled_by_dopamine():
    engine = LearningEngine()
    engine.value_estimate = 0.0
    engine.apply_neuromodulation(NeuromodulationSignal(dopamine=2.0))
    engine.compute_td_error(reward=1.0, value_next=0.0)

    new_value = engine.apply_td_update()

    assert new_value == pytest.approx(TD_ALPHA * 2.0 * 1.0)


# --- reset() -------------------------------------------------------------------------------


def test_reset_restores_value_and_synapses():
    engine = LearningEngine()
    syn = STDPSynapse(n_pre=1, n_post=1, weight_init=0.5)
    engine.register_projection(syn, source_module="pre", target_module="post")
    w0 = syn.weight_matrix.copy()

    engine.compute_td_error(reward=1.0, value_next=0.0)
    engine.apply_td_update()
    engine.update(
        dt=1.0,
        inputs=make_inputs([1.0, 1.0], neuromodulation=NeuromodulationSignal(acetylcholine=1.0)),
    )

    engine.reset()

    assert engine.value_estimate == 0.0
    assert engine.last_td_error == 0.0
    assert np.array_equal(syn.weight_matrix, w0)


# --- PlasticityScheduler --------------------------------------------------------------------


def test_plasticity_scheduler_thresholds():
    scheduler = PlasticityScheduler(acetylcholine_threshold=0.5)

    assert scheduler.is_plastic(NeuromodulationSignal(acetylcholine=0.6)) is True
    assert scheduler.is_plastic(NeuromodulationSignal(acetylcholine=0.4)) is False


def test_plasticity_scheduler_learning_rate_scale_nonnegative():
    scheduler = PlasticityScheduler()
    assert scheduler.learning_rate_scale(NeuromodulationSignal(dopamine=-1.0)) == 0.0
    assert scheduler.learning_rate_scale(NeuromodulationSignal(dopamine=1.5)) == 1.5
