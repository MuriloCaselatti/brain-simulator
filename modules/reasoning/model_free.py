"""Brain Simulator -- Model-Free Reinforcement Learning (SPEC-007).

Implements :class:`ModelFreeRL`, a habitual action-value learner modelling the
basal ganglia "habit" pathway (Daw, Niv & Dayan 2005). Action values
``q_values`` are updated by a Rescorla-Wagner / TD(0) delta rule with a small,
fixed :attr:`learning_rate`:

    Q[a] += learning_rate * (reward - Q[a])

Actions are sampled from a softmax over ``q_values`` (:attr:`temperature`
controls exploration).

Fast but inflexible
--------------------
Action *selection* is a single cached lookup -- no search, no model of the
environment -- so this system is **fast**. But because the learning rate is
small and fixed, ``q_values`` only track the *long-run average* outcome of
each action: after the environment's contingencies change (e.g. a bandit
reversal), the cached values are slow to catch up, making this system
**inflexible** relative to :class:`~modules.reasoning.model_based.ModelBasedRL`.

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

__all__ = ["ModelFreeRL", "softmax"]


def softmax(values: np.ndarray, temperature: float) -> np.ndarray:
    """Numerically-stable softmax of ``values`` at the given ``temperature``."""
    values = np.asarray(values, dtype=float)
    temperature = max(float(temperature), 1e-6)
    scaled = values / temperature
    scaled = scaled - scaled.max()
    exp = np.exp(scaled)
    total = exp.sum()
    if total <= 0.0:
        return np.full(values.shape, 1.0 / values.size)
    return exp / total


class ModelFreeRL(CognitiveModule):
    """Habitual, action-value-caching reinforcement learner.

    Args:
        module_id: Stable identifier for this module instance.
        n_actions: Number of discrete actions (e.g. bandit arms).
        learning_rate: Step size of the Rescorla-Wagner update. Small and
            fixed -- the source of this system's "inflexibility".
        temperature: Softmax temperature for action selection. Lower values
            make the policy more greedy with respect to ``q_values``.
        max_rate_hz: Firing rate mapped to action probability ``1.0``.
        rng: Optional NumPy generator for reproducible action sampling.
    """

    def __init__(
        self,
        module_id: str = "model_free",
        n_actions: int = 2,
        learning_rate: float = 0.05,
        temperature: float = 0.2,
        max_rate_hz: float = 50.0,
        rng: Optional[np.random.Generator] = None,
    ) -> None:
        if n_actions < 2:
            raise ValueError("n_actions must be >= 2")
        super().__init__(module_id, n_actions)

        self.n_actions = n_actions
        self.learning_rate = learning_rate
        self.temperature = temperature
        self.max_rate_hz = max_rate_hz
        self._rng = rng if rng is not None else np.random.default_rng()

        self.q_values = np.zeros(n_actions)
        self._last_action: Optional[int] = None
        self._last_probabilities = np.full(n_actions, 1.0 / n_actions)
        self._dopamine = 1.0
        self._timestamp_ms = 0.0

    # -- RL interface ----------------------------------------------------------

    def select_action(self) -> Tuple[int, np.ndarray]:
        """Sample an action from the softmax policy over ``q_values``."""
        probs = softmax(self.q_values, self.temperature)
        action = int(self._rng.choice(self.n_actions, p=probs))
        self._last_action = action
        self._last_probabilities = probs
        return action, probs

    def update_value(self, action: int, reward: float) -> float:
        """Apply the Rescorla-Wagner delta rule for ``action``.

        Returns the prediction error ``reward - Q[action]`` (before update).
        Dopamine (set via :meth:`apply_neuromodulation`) scales the effective
        learning rate, consistent with :class:`~core.learning_engine.PlasticityScheduler`.
        """
        lr = self.learning_rate * max(0.0, self._dopamine)
        prediction_error = reward - self.q_values[action]
        self.q_values[action] += lr * prediction_error
        return prediction_error

    # -- CognitiveModule contract ------------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        """Select an action for this timestep from the cached ``q_values``.

        Reward delivery and value updates happen out-of-band via
        :meth:`update_value` (the caller observes the environment's reward
        for the action returned in ``internal_state["action"]`` and feeds it
        back before the next :meth:`update`).
        """
        self._timestamp_ms = inputs.timestamp_ms
        action, probs = self.select_action()

        spikes = np.zeros(self.n_actions)
        spikes[action] = 1.0

        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=probs * self.max_rate_hz,
            internal_state={
                "action": action,
                "q_values": self.q_values.copy(),
                "action_probabilities": probs,
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
            mean_weight=float(self.q_values.mean()),
            active_synapses=int(np.count_nonzero(self.q_values)),
            timestamp_ms=self._timestamp_ms,
            metadata={
                "q_values": self.q_values.copy(),
                "last_action": self._last_action,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Dopamine scales the learning-rate of :meth:`update_value`."""
        self._dopamine = signal.dopamine

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        """Expose ``q_values`` as a 1xN matrix for observability.

        Not consumed by the STDP ``LearningEngine`` -- the Rescorla-Wagner
        update in :meth:`update_value` is this module's own plasticity rule
        (ADR-008 pattern).
        """
        return [
            SynapticTarget(
                source_module=self.module_id,
                target_module=self.module_id,
                weight_matrix=self.q_values.reshape(1, -1),
                synapse_type="excitatory",
            )
        ]

    def reset(self) -> None:
        self.q_values = np.zeros(self.n_actions)
        self._last_action = None
        self._last_probabilities = np.full(self.n_actions, 1.0 / self.n_actions)
        self._dopamine = 1.0
        self._timestamp_ms = 0.0
