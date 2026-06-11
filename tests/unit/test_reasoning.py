"""Tests for SPEC-007 -- Reasoning (dual RL + PFC + DecisionGate).

Covers the :class:`~core.interfaces.CognitiveModule` contract and the
arbitration / inhibition logic of:

* :class:`~modules.reasoning.model_free.ModelFreeRL`
* :class:`~modules.reasoning.model_based.ModelBasedRL`
* :class:`~modules.reasoning.pfc.PFCExecutive`
* :class:`~modules.reasoning.decision_gate.DecisionGate`

End-to-end RL acceptance criteria (bandit convergence, contingency reversal)
live in ``tests/scientific/test_bandit_validation.py``.
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
from modules.reasoning.decision_gate import DecisionGate  # noqa: E402
from modules.reasoning.model_based import ModelBasedRL  # noqa: E402
from modules.reasoning.model_free import ModelFreeRL, softmax  # noqa: E402
from modules.reasoning.pfc import PFCExecutive  # noqa: E402


def _inputs(spike_trains, attention_signal=1.0, neuromodulation=None, timestamp_ms=0.0):
    return ModuleInputs(
        spike_trains=np.asarray(spike_trains, dtype=float),
        attention_signal=attention_signal,
        neuromodulation=neuromodulation or NeuromodulationSignal(),
        timestamp_ms=timestamp_ms,
    )


# --- softmax helper -----------------------------------------------------------------


def test_softmax_sums_to_one_and_prefers_larger_value():
    probs = softmax(np.array([1.0, 0.0]), temperature=0.5)
    assert probs.sum() == pytest.approx(1.0)
    assert probs[0] > probs[1]


# --- ModelFreeRL: CognitiveModule contract -------------------------------------------


def test_model_free_is_cognitive_module():
    agent = ModelFreeRL(rng=np.random.default_rng(0))
    assert isinstance(agent, CognitiveModule)


def test_model_free_update_returns_module_outputs():
    agent = ModelFreeRL(n_actions=3, rng=np.random.default_rng(0))
    out = agent.update(1.0, _inputs(np.zeros(0)))
    assert isinstance(out, ModuleOutputs)
    assert out.spike_trains.shape == (3,)
    assert out.firing_rate.shape == (3,)
    assert out.spike_trains.sum() == 1.0  # one-hot action selection
    assert out.internal_state["action"] in (0, 1, 2)
    assert out.internal_state["q_values"].shape == (3,)


def test_model_free_get_state_contract():
    agent = ModelFreeRL(rng=np.random.default_rng(0))
    agent.update(1.0, _inputs(np.zeros(0)))
    state = agent.get_state()
    assert isinstance(state, ModuleState)
    assert state.module_id == agent.module_id
    assert state.n_neurons == agent.n_neurons


def test_model_free_synaptic_targets_expose_q_values():
    agent = ModelFreeRL(n_actions=2, rng=np.random.default_rng(0))
    targets = agent.get_synaptic_targets()
    assert len(targets) == 1
    assert isinstance(targets[0], SynapticTarget)
    assert targets[0].weight_matrix.shape == (1, 2)


def test_model_free_update_value_moves_q_toward_reward():
    agent = ModelFreeRL(n_actions=2, learning_rate=0.5, rng=np.random.default_rng(0))
    agent.update_value(action=0, reward=1.0)
    assert agent.q_values[0] == pytest.approx(0.5)
    assert agent.q_values[1] == pytest.approx(0.0)


def test_model_free_dopamine_scales_learning_rate():
    agent = ModelFreeRL(n_actions=2, learning_rate=0.5, rng=np.random.default_rng(0))
    agent.apply_neuromodulation(NeuromodulationSignal(dopamine=0.0))
    agent.update_value(action=0, reward=1.0)
    assert agent.q_values[0] == pytest.approx(0.0)


def test_model_free_reset_clears_q_values():
    agent = ModelFreeRL(n_actions=2, learning_rate=0.5, rng=np.random.default_rng(0))
    agent.update_value(action=0, reward=1.0)
    agent.reset()
    assert np.allclose(agent.q_values, 0.0)


# --- ModelBasedRL: CognitiveModule contract -------------------------------------------


def test_model_based_is_cognitive_module():
    agent = ModelBasedRL(rng=np.random.default_rng(0))
    assert isinstance(agent, CognitiveModule)


def test_model_based_update_returns_module_outputs():
    agent = ModelBasedRL(n_actions=3, rng=np.random.default_rng(0))
    out = agent.update(1.0, _inputs(np.zeros(0)))
    assert isinstance(out, ModuleOutputs)
    assert out.spike_trains.shape == (3,)
    assert out.firing_rate.shape == (3,)
    assert out.internal_state["action"] in (0, 1, 2)
    assert out.internal_state["reward_model"].shape == (3,)
    assert out.internal_state["deliberation_steps"] == agent.n_simulations


def test_model_based_update_model_moves_toward_reward():
    agent = ModelBasedRL(n_actions=2, model_learning_rate=0.5, rng=np.random.default_rng(0))
    agent.update_model(action=0, reward=1.0)
    assert agent.reward_model[0] == pytest.approx(0.75)  # 0.5 + 0.5*(1 - 0.5)


def test_model_based_deliberate_returns_reward_model():
    agent = ModelBasedRL(n_actions=2, rng=np.random.default_rng(0))
    agent.reward_model = np.array([0.9, 0.1])
    assert np.allclose(agent.deliberate(), [0.9, 0.1])


def test_model_based_synaptic_targets_expose_reward_model():
    agent = ModelBasedRL(n_actions=2, rng=np.random.default_rng(0))
    targets = agent.get_synaptic_targets()
    assert len(targets) == 1
    assert targets[0].weight_matrix.shape == (1, 2)


def test_model_based_reset_restores_prior():
    agent = ModelBasedRL(n_actions=2, rng=np.random.default_rng(0))
    agent.update_model(action=0, reward=1.0)
    agent.reset()
    assert np.allclose(agent.reward_model, 0.5)


# --- PFCExecutive ---------------------------------------------------------------------


def test_pfc_is_cognitive_module():
    pfc = PFCExecutive()
    assert isinstance(pfc, CognitiveModule)


def test_pfc_inhibits_high_value_impulsive_action():
    pfc = PFCExecutive(n_actions=2, control_threshold=0.5)
    out = pfc.update(1.0, _inputs([0.9, 0.1]))
    assert out.internal_state["inhibit"] is True
    assert out.internal_state["inhibited_action"] == 0
    assert out.spike_trains[0] == pytest.approx(0.0)
    assert out.spike_trains[1] == pytest.approx(1.0)


def test_pfc_does_not_inhibit_below_threshold():
    pfc = PFCExecutive(n_actions=2, control_threshold=0.5)
    out = pfc.update(1.0, _inputs([0.3, 0.1]))
    assert out.internal_state["inhibit"] is False
    assert out.internal_state["inhibited_action"] is None
    assert np.allclose(out.spike_trains, [1.0, 1.0])


def test_pfc_stress_raises_effective_threshold():
    pfc = PFCExecutive(n_actions=2, control_threshold=0.5, noradrenaline_sensitivity=1.0)
    base = pfc.effective_threshold()

    pfc.apply_neuromodulation(NeuromodulationSignal(noradrenaline=2.0))
    stressed = pfc.effective_threshold()

    assert stressed > base


def test_pfc_stress_can_disable_inhibition():
    pfc = PFCExecutive(n_actions=2, control_threshold=0.5, noradrenaline_sensitivity=1.0)
    stressed = NeuromodulationSignal(noradrenaline=2.0)
    out = pfc.update(1.0, _inputs([0.9, 0.1], neuromodulation=stressed))
    # threshold doubled to 1.0 -> 0.9 no longer exceeds it
    assert out.internal_state["inhibit"] is False


def test_pfc_synaptic_targets_empty():
    pfc = PFCExecutive()
    assert pfc.get_synaptic_targets() == []


def test_pfc_reset_clears_state():
    pfc = PFCExecutive(n_actions=2)
    pfc.apply_neuromodulation(NeuromodulationSignal(noradrenaline=2.0))
    pfc.update(1.0, _inputs([0.9, 0.1]))
    pfc.reset()
    assert pfc.effective_threshold() == pytest.approx(pfc.control_threshold)


# --- DecisionGate ---------------------------------------------------------------------


def test_decision_gate_is_cognitive_module():
    gate = DecisionGate()
    assert isinstance(gate, CognitiveModule)


def test_decision_gate_update_returns_module_outputs():
    gate = DecisionGate(n_actions=2)
    combined = np.array([0.9, 0.1, 0.2, 0.8])
    out = gate.update(1.0, _inputs(combined))
    assert isinstance(out, ModuleOutputs)
    assert out.spike_trains.shape == (2,)
    assert out.internal_state["action_probabilities"].sum() == pytest.approx(1.0)


def test_decision_gate_baseline_weights_systems_equally():
    gate = DecisionGate(n_actions=2, baseline_noradrenaline=1.0)
    w = gate.arbitration_weight(noradrenaline=1.0)
    assert w == pytest.approx(0.5)


def test_decision_gate_stress_shifts_weight_to_model_free():
    gate = DecisionGate(n_actions=2, baseline_noradrenaline=1.0, stress_gain=2.0)

    mf_probs = np.array([0.9, 0.1])
    mb_probs = np.array([0.2, 0.8])
    combined = np.concatenate([mf_probs, mb_probs])

    low_stress = gate.update(
        1.0, _inputs(combined, neuromodulation=NeuromodulationSignal(noradrenaline=0.5))
    )
    high_stress = gate.update(
        1.0, _inputs(combined, neuromodulation=NeuromodulationSignal(noradrenaline=2.0))
    )

    assert high_stress.internal_state["w_model_free"] > low_stress.internal_state["w_model_free"]
    assert (
        high_stress.internal_state["action_probabilities"][0]
        > low_stress.internal_state["action_probabilities"][0]
    )


def test_decision_gate_inhibition_gate_vetoes_action():
    gate = DecisionGate(n_actions=2)
    gate.set_inhibition_gate(np.array([0.0, 1.0]))

    mf_probs = np.array([0.9, 0.1])
    mb_probs = np.array([0.9, 0.1])
    combined = np.concatenate([mf_probs, mb_probs])

    out = gate.update(1.0, _inputs(combined))
    assert out.internal_state["action_probabilities"][0] == pytest.approx(0.0)
    assert out.internal_state["action_probabilities"][1] == pytest.approx(1.0)
    assert out.internal_state["action"] == 1


def test_decision_gate_synaptic_targets_empty():
    gate = DecisionGate()
    assert gate.get_synaptic_targets() == []


def test_decision_gate_reset_clears_inhibition_gate():
    gate = DecisionGate(n_actions=2)
    gate.set_inhibition_gate(np.array([0.0, 1.0]))
    gate.reset()
    assert np.allclose(gate._inhibition_gate, 1.0)
