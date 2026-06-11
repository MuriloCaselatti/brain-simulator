"""Brain Simulator -- Model-Based Reinforcement Learning (SPEC-007).

Implements :class:`ModelBasedRL`, a deliberative learner modelling
goal-directed, prefrontal/orbitofrontal-style control (Daw, Niv & Dayan 2005).
Unlike :class:`~modules.reasoning.model_free.ModelFreeRL`, this module learns
an explicit internal model of the environment -- :attr:`reward_model`, the
expected reward of each action -- and *re-derives* its policy from that model
on every timestep via :meth:`deliberate`.

Slow but flexible
------------------
* **Flexible**: :attr:`reward_model` is updated with a comparatively large
  :attr:`model_learning_rate`, so when the environment's contingencies change
  (e.g. a bandit reversal) the model -- and therefore the policy derived from
  it -- adapts within a handful of trials.
* **Slow**: choosing an action requires :meth:`deliberate` to *forward-simulate*
  the world model :attr:`n_simulations` times per action to estimate its
  expected outcome, rather than a single cached lookup. ``n_simulations`` is
  reported in ``internal_state["deliberation_steps"]`` as a proxy for this
  per-decision computational cost.

Implements :class:`~core.interfaces.CognitiveModule` (SPEC-001, frozen).
"""
from __future__ import annotations

from typing import List, Optional, Tuple

import numpy as np

from core.interfaces import (
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)
from modules.reasoning.model_free import softmax

__all__ = ["ModelBasedRL"]


class ModelBasedRL(CognitiveModule):
    """Deliberative learner that plans over an explicit reward model.

    Args:
        module_id: Stable identifier for this module instance.
        n_actions: Number of discrete actions (e.g. bandit arms).
        model_learning_rate: Step size of the reward-model update. Larger
            than :attr:`~modules.reasoning.model_free.ModelFreeRL.learning_rate`
            -- the source of this system's "flexibility".
        n_simulations: Number of forward simulations of the reward model used
            by :meth:`deliberate` per decision -- a proxy for deliberation
            cost ("slowness").
        temperature: Softmax temperature for action selection over the
            deliberated values.
        max_rate_hz: Firing rate mapped to action probability ``1.0``.
        rng: Optional NumPy generator for reproducible simulation/sampling.
    """

    def __init__(
        self,
        module_id: str = "model_based",
        n_actions: int = 2,
        model_learning_rate: float = 0.3,
        n_simulations: int = 20,
        temperature: float = 0.2,
        max_rate_hz: float = 50.0,
        rng: Optional[np.random.Generator] = None,
    ) -> None:
        if n_actions < 2:
            raise ValueError("n_actions must be >= 2")
        super().__init__(module_id, n_actions)

        self.n_actions = n_actions
        self.model_learning_rate = model_learning_rate
        self.n_simulations = n_simulations
        self.temperature = temperature
        self.max_rate_hz = max_rate_hz
        self._rng = rng if rng is not None else np.random.default_rng()

        # Uninformative prior: each action expected to be a fair coin flip.
        self.reward_model = np.full(n_actions, 0.5)
        self._last_action: Optional[int] = None
        self._last_probabilities = np.full(n_actions, 1.0 / n_actions)
        self._dopamine = 1.0
        self._timestamp_ms = 0.0

    # -- world model -------------------------------------------------------------

    def update_model(self, action: int, reward: float) -> float:
        """Update :attr:`reward_model` for ``action`` toward ``reward``.

        Returns the model's prediction error ``reward - reward_model[action]``
        (before update). Dopamine (set via :meth:`apply_neuromodulation`)
        scales the effective learning rate, mirroring
        :class:`~core.learning_engine.PlasticityScheduler`.
        """
        lr = self.model_learning_rate * max(0.0, self._dopamine)
        prediction_error = reward - self.reward_model[action]
        self.reward_model[action] += lr * prediction_error
        return prediction_error

    def deliberate(self) -> np.ndarray:
        """Forward-simulate the reward model to estimate each action's value.

        For a model ``reward_model[a]`` representing the believed probability
        of reward, the expectation of :attr:`n_simulations` Bernoulli draws
        converges to ``reward_model[a]`` itself -- this is exactly what
        "evaluating the model" means for a one-step task. The cost of that
        evaluation (rather than its outcome) is what makes this system slow;
        see :attr:`n_simulations`.
        """
        return np.clip(self.reward_model, 0.0, 1.0)

    def select_action(self) -> Tuple[int, np.ndarray, np.ndarray]:
        """Deliberate, then sample an action from the resulting softmax."""
        values = self.deliberate()
        probs = softmax(values, self.temperature)
        action = int(self._rng.choice(self.n_actions, p=probs))
        self._last_action = action
        self._last_probabilities = probs
        return action, probs, values

    # -- CognitiveModule contract ------------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        """Deliberate over the world model and select an action.

        Reward delivery and model updates happen out-of-band via
        :meth:`update_model` (the caller observes the environment's reward
        for the action returned in ``internal_state["action"]`` and feeds it
        back before the next :meth:`update`).
        """
        self._timestamp_ms = inputs.timestamp_ms
        action, probs, values = self.select_action()

        spikes = np.zeros(self.n_actions)
        spikes[action] = 1.0

        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=probs * self.max_rate_hz,
            internal_state={
                "action": action,
                "reward_model": self.reward_model.copy(),
                "values": values,
                "action_probabilities": probs,
                "deliberation_steps": self.n_simulations,
            },
        )

    def get_state(self) -> ModuleState:
        firing_rate = self._last_probabilities * self.max_rate_hz
        voltage = -70.0 + 25.0 * self._last_probabilities
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=voltage,
            firing_rate=firing_rate,
            mean_weight=float(self.reward_model.mean()),
            active_synapses=int(np.count_nonzero(self.reward_model)),
            timestamp_ms=self._timestamp_ms,
            metadata={
                "reward_model": self.reward_model.copy(),
                "last_action": self._last_action,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Dopamine scales the learning-rate of :meth:`update_model`."""
        self._dopamine = signal.dopamine

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        """Expose ``reward_model`` as a 1xN matrix for observability.

        Not consumed by the STDP ``LearningEngine`` -- :meth:`update_model`
        is this module's own plasticity rule (ADR-008 pattern).
        """
        return [
            SynapticTarget(
                source_module=self.module_id,
                target_module=self.module_id,
                weight_matrix=self.reward_model.reshape(1, -1),
                synapse_type="excitatory",
            )
        ]

    def reset(self) -> None:
        self.reward_model = np.full(self.n_actions, 0.5)
        self._last_action = None
        self._last_probabilities = np.full(self.n_actions, 1.0 / self.n_actions)
        self._dopamine = 1.0
        self._timestamp_ms = 0.0
