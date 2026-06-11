"""Brain Simulator -- Decision Gate (SPEC-007).

Implements :class:`DecisionGate`, the final arbitration stage of the SPEC-007
reasoning system. It combines the action-probability vectors of the parallel
RL systems --

* :class:`~modules.reasoning.model_free.ModelFreeRL` ("emotion" / habit --
  fast, automatic, stimulus-bound), and
* :class:`~modules.reasoning.model_based.ModelBasedRL` ("reason" / planning --
  slow, deliberate, goal-directed)

-- into a single action, gated by the inhibitory signal from
:class:`~modules.reasoning.pfc.PFCExecutive`.

Stress/urgency arbitration (SPEC-007 stress -> model-free transition)
------------------------------------------------------------------------
The mixing weight between the two systems is a sigmoid of noradrenaline
(:meth:`arbitration_weight`), centred on :attr:`baseline_noradrenaline`:

    w_model_free = sigmoid(stress_gain * (noradrenaline - baseline_noradrenaline))
    action_probabilities = w_model_free * mf_probs + (1 - w_model_free) * mb_probs

At basal noradrenaline the two systems are weighted equally
(``w_model_free == 0.5``); under stress (noradrenaline above baseline) the
weight shifts toward the fast, habitual model-free system, reflecting the
classic finding that acute stress shifts behavioural control from
goal-directed to habitual systems (Schwabe & Wolf 2009).

Implements :class:`~core.interfaces.CognitiveModule` (SPEC-001, frozen).
"""
from __future__ import annotations

from typing import List, Optional

import numpy as np

from core.interfaces import (
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)
from modules.attention._utils import align_to

__all__ = ["DecisionGate"]


class DecisionGate(CognitiveModule):
    """Arbitrates between model-free and model-based action proposals.

    Args:
        module_id: Stable identifier for this module instance.
        n_actions: Number of discrete actions.
        baseline_noradrenaline: Noradrenaline level at which model-free and
            model-based systems are weighted equally (``w_model_free == 0.5``).
        stress_gain: Slope of the sigmoid mapping noradrenaline deviation from
            baseline to :meth:`arbitration_weight`.
        max_rate_hz: Firing rate mapped to action probability ``1.0``.
    """

    def __init__(
        self,
        module_id: str = "decision_gate",
        n_actions: int = 2,
        baseline_noradrenaline: float = 1.0,
        stress_gain: float = 2.0,
        max_rate_hz: float = 50.0,
    ) -> None:
        if n_actions < 2:
            raise ValueError("n_actions must be >= 2")
        super().__init__(module_id, n_actions)

        self.n_actions = n_actions
        self.baseline_noradrenaline = baseline_noradrenaline
        self.stress_gain = stress_gain
        self.max_rate_hz = max_rate_hz

        self._noradrenaline = baseline_noradrenaline
        self._inhibition_gate = np.ones(n_actions)
        self._last_action: Optional[int] = None
        self._last_probabilities = np.full(n_actions, 1.0 / n_actions)
        self._last_w_model_free = 0.5
        self._timestamp_ms = 0.0

    # -- PFC coupling --------------------------------------------------------------

    def set_inhibition_gate(self, gate: np.ndarray) -> None:
        """Apply an inhibitory gate from :class:`~modules.reasoning.pfc.PFCExecutive`.

        Entries of ``gate`` near ``0`` veto the corresponding action;
        :meth:`update` multiplies the arbitrated action probabilities by this
        gate before re-normalising.
        """
        self._inhibition_gate = align_to(gate, self.n_actions)

    def clear_inhibition_gate(self) -> None:
        """Remove any PFC veto (equivalent to an all-ones gate)."""
        self._inhibition_gate = np.ones(self.n_actions)

    # -- arbitration -----------------------------------------------------------------

    def arbitration_weight(self, noradrenaline: Optional[float] = None) -> float:
        """Return ``w_model_free`` -- the mixing weight on the model-free policy.

        Increases monotonically with ``noradrenaline`` (stress favours
        model-free). Defaults to the noradrenaline level set by the most
        recent :meth:`apply_neuromodulation`/:meth:`update` call.
        """
        nor = self._noradrenaline if noradrenaline is None else noradrenaline
        x = self.stress_gain * (nor - self.baseline_noradrenaline)
        return float(1.0 / (1.0 + np.exp(-x)))

    # -- CognitiveModule contract ------------------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        """Combine model-free and model-based proposals into a final action.

        ``inputs.spike_trains`` is expected to be the concatenation
        ``[model_free_action_probabilities, model_based_action_probabilities]``,
        each of length :attr:`n_actions`.
        """
        self._timestamp_ms = inputs.timestamp_ms
        self._noradrenaline = inputs.neuromodulation.noradrenaline

        combined = align_to(inputs.spike_trains, 2 * self.n_actions)
        mf_probs = combined[: self.n_actions]
        mb_probs = combined[self.n_actions :]

        w_mf = self.arbitration_weight()
        self._last_w_model_free = w_mf

        probs = w_mf * mf_probs + (1.0 - w_mf) * mb_probs
        probs = probs * self._inhibition_gate
        total = probs.sum()
        if total <= 0.0:
            probs = np.full(self.n_actions, 1.0 / self.n_actions)
        else:
            probs = probs / total

        action = int(np.argmax(probs))
        self._last_action = action
        self._last_probabilities = probs

        spikes = np.zeros(self.n_actions)
        spikes[action] = 1.0

        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=probs * self.max_rate_hz,
            internal_state={
                "action": action,
                "action_probabilities": probs,
                "w_model_free": w_mf,
                "w_model_based": 1.0 - w_mf,
                "inhibition_gate": self._inhibition_gate.copy(),
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
            mean_weight=float(self._last_w_model_free),
            active_synapses=int(np.count_nonzero(self._inhibition_gate)),
            timestamp_ms=self._timestamp_ms,
            metadata={
                "action": self._last_action,
                "w_model_free": self._last_w_model_free,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Noradrenaline shifts :meth:`arbitration_weight` toward model-free."""
        self._noradrenaline = signal.noradrenaline

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        """The DecisionGate owns no learned synapses -- it arbitrates."""
        return []

    def reset(self) -> None:
        self._noradrenaline = self.baseline_noradrenaline
        self._inhibition_gate = np.ones(self.n_actions)
        self._last_action = None
        self._last_probabilities = np.full(self.n_actions, 1.0 / self.n_actions)
        self._last_w_model_free = 0.5
        self._timestamp_ms = 0.0
