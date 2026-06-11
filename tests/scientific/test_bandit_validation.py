"""SPEC-007 -- Scientific validation: dual RL on a 2-armed bandit task.

This suite validates the parallel model-free / model-based reinforcement
learning systems (Daw, Niv & Dayan 2005) and their arbitration against the
SPEC-007 acceptance criteria:

    1. Model-free converges on a stationary 2-armed bandit in < 200 trials.
    2. Model-based outperforms model-free in a task with a contingency
       reversal (it adapts its world model faster than the model-free
       cached values can catch up).
    3. PFC inhibits the impulsive (model-free) response when its value
       exceeds the control threshold.
    4. Stress (noradrenaline) shifts the full pipeline's final decision from
       the model-based recommendation toward the model-free / impulsive one
       -- the "stress favours model-free" transition.

References:
    * Daw, Niv & Dayan (2005) -- uncertainty-based competition between
      prefrontal (model-based) and dorsolateral striatal (model-free)
      reinforcement-learning systems.
    * Schwabe & Wolf (2009) -- acute stress shifts behavioural control from
      goal-directed to habitual systems.
    * Arnsten (2009) -- stress signalling impairs prefrontal cortex function.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.interfaces import ModuleInputs, NeuromodulationSignal  # noqa: E402
from modules.reasoning.decision_gate import DecisionGate  # noqa: E402
from modules.reasoning.model_based import ModelBasedRL  # noqa: E402
from modules.reasoning.model_free import ModelFreeRL  # noqa: E402
from modules.reasoning.pfc import PFCExecutive  # noqa: E402


def _inputs(spike_trains, neuromodulation=None):
    return ModuleInputs(
        spike_trains=np.asarray(spike_trains, dtype=float),
        attention_signal=1.0,
        neuromodulation=neuromodulation or NeuromodulationSignal(),
        timestamp_ms=0.0,
    )


class TwoArmedBandit:
    """A stationary (or non-stationary, via :meth:`set_probabilities`)
    2-armed Bernoulli bandit."""

    def __init__(self, p_arm0: float, p_arm1: float, rng: np.random.Generator):
        self.probabilities = [p_arm0, p_arm1]
        self._rng = rng

    def set_probabilities(self, p_arm0: float, p_arm1: float) -> None:
        self.probabilities = [p_arm0, p_arm1]

    def step(self, action: int) -> float:
        return float(self._rng.random() < self.probabilities[action])

    def draw_both(self):
        """Pre-draw the outcome of *both* arms for this trial.

        Used to compare two agents under matched reward sequences.
        """
        return [float(self._rng.random() < p) for p in self.probabilities]


# --- Criterion #1: model-free converges in < 200 trials -----------------------------


def test_model_free_converges_on_two_armed_bandit():
    """A clearly-better arm (p=0.8) is preferred > 70% of the time within 200 trials."""
    bandit = TwoArmedBandit(0.8, 0.2, rng=np.random.default_rng(42))
    agent = ModelFreeRL(
        n_actions=2, learning_rate=0.05, temperature=0.2, rng=np.random.default_rng(1)
    )

    chosen_actions = []
    for _ in range(200):
        action, _ = agent.select_action()
        reward = bandit.step(action)
        agent.update_value(action, reward)
        chosen_actions.append(action)

    fraction_best_arm = np.mean([a == 0 for a in chosen_actions[-50:]])
    assert fraction_best_arm > 0.7
    # The learned value of the better arm should dominate.
    assert agent.q_values[0] > agent.q_values[1]


# --- Criterion #2: model-based beats model-free after a contingency reversal --------


def _run_reversal(seed: int, phase1_trials: int = 150, phase2_trials: int = 50):
    """Run matched model-free and model-based agents through a reversal.

    Both agents see the *same* per-trial reward draws for each arm (the
    bandit's outcomes are pre-drawn once per trial and indexed by each
    agent's own action), so the comparison isolates how quickly each
    learning system adapts after the reversal at ``phase1_trials``.

    Returns the mean reward each agent earned in the last 20 trials of
    phase 2 (post-reversal).
    """
    env_rng = np.random.default_rng(seed)
    mf = ModelFreeRL(
        n_actions=2, learning_rate=0.05, temperature=0.2,
        rng=np.random.default_rng(seed + 1000),
    )
    mb = ModelBasedRL(
        n_actions=2, model_learning_rate=0.3, n_simulations=20, temperature=0.2,
        rng=np.random.default_rng(seed + 2000),
    )

    bandit = TwoArmedBandit(0.8, 0.2, rng=env_rng)
    mf_rewards = []
    mb_rewards = []
    for trial in range(phase1_trials + phase2_trials):
        if trial == phase1_trials:
            bandit.set_probabilities(0.2, 0.8)  # contingency reversal

        outcomes = bandit.draw_both()

        a_mf, _ = mf.select_action()
        r_mf = outcomes[a_mf]
        mf.update_value(a_mf, r_mf)
        mf_rewards.append(r_mf)

        a_mb, _, _ = mb.select_action()
        r_mb = outcomes[a_mb]
        mb.update_model(a_mb, r_mb)
        mb_rewards.append(r_mb)

    return float(np.mean(mf_rewards[-20:])), float(np.mean(mb_rewards[-20:]))


def test_model_based_outperforms_model_free_after_reversal():
    mf_scores = []
    mb_scores = []
    for seed in range(30):
        mf_score, mb_score = _run_reversal(seed * 7)
        mf_scores.append(mf_score)
        mb_scores.append(mb_score)

    mf_avg = float(np.mean(mf_scores))
    mb_avg = float(np.mean(mb_scores))

    # Model-based's flexible world model re-adapts to the reversed
    # contingency faster than model-free's slowly-shifting cached values.
    assert mb_avg > mf_avg + 0.1


# --- Criterion #3: PFC inhibits impulsive response above the control threshold ------


def test_pfc_inhibits_impulsive_response_when_reward_exceeds_threshold():
    pfc = PFCExecutive(n_actions=2, control_threshold=0.5)

    # The model-free pathway strongly favours action 0 (a tempting outcome).
    mf_values = np.array([0.9, 0.1])
    out = pfc.update(1.0, _inputs(mf_values))

    assert out.internal_state["inhibit"] is True
    assert out.internal_state["inhibited_action"] == 0
    assert out.internal_state["gate"][0] == pytest.approx(0.0)

    # A modest preference, below the control threshold, is left unchecked.
    pfc.reset()
    out = pfc.update(1.0, _inputs(np.array([0.3, 0.1])))
    assert out.internal_state["inhibit"] is False


# --- Criterion #4: stress shifts the final decision toward model-free ----------------


def _pipeline_decision(noradrenaline: float):
    """Run one full SPEC-007 decision cycle at a given noradrenaline level.

    The model-free pathway has learned a strong preference for the
    "impulsive" action 0; the model-based pathway has learned that action 1
    is actually better. PFC may veto the impulsive action before the
    DecisionGate arbitrates between the two systems.
    """
    neuromod = NeuromodulationSignal(noradrenaline=noradrenaline)

    mf = ModelFreeRL(n_actions=2, temperature=0.2, rng=np.random.default_rng(0))
    mf.q_values = np.array([0.9, 0.1])

    mb = ModelBasedRL(n_actions=2, temperature=0.2, rng=np.random.default_rng(1))
    mb.reward_model = np.array([0.3, 0.7])

    pfc = PFCExecutive(n_actions=2, control_threshold=0.5, noradrenaline_sensitivity=1.0)
    gate = DecisionGate(n_actions=2, baseline_noradrenaline=1.0, stress_gain=2.0)

    mf_out = mf.update(1.0, _inputs(np.zeros(0), neuromod))
    mb_out = mb.update(1.0, _inputs(np.zeros(0), neuromod))

    pfc_out = pfc.update(1.0, _inputs(mf_out.internal_state["q_values"], neuromod))
    gate.set_inhibition_gate(pfc_out.internal_state["gate"])

    combined = np.concatenate(
        [mf_out.internal_state["action_probabilities"], mb_out.internal_state["action_probabilities"]]
    )
    gate_out = gate.update(1.0, _inputs(combined, neuromod))
    return gate_out.internal_state["action"], pfc_out.internal_state["inhibit"]


def test_stress_shifts_final_decision_from_model_based_to_model_free():
    # At baseline arousal, PFC inhibits the impulsive action 0 and the
    # DecisionGate (weighting both systems equally) follows model-based.
    calm_action, calm_inhibited = _pipeline_decision(noradrenaline=1.0)
    assert calm_inhibited is True
    assert calm_action == 1  # model-based's recommendation

    # Under acute stress, PFC's control is impaired (no inhibition) and the
    # arbitration weight shifts toward model-free -- the impulsive action
    # wins.
    stressed_action, stressed_inhibited = _pipeline_decision(noradrenaline=2.0)
    assert stressed_inhibited is False
    assert stressed_action == 0  # model-free's impulsive recommendation
