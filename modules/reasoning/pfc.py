"""Brain Simulator -- PFC Executive Control (SPEC-007).

Implements :class:`PFCExecutive`, modelling the prefrontal cortex's
inhibitory-control role over the basal-ganglia "habit" pathway
(:class:`~modules.reasoning.model_free.ModelFreeRL`): a strongly tempting,
high-immediate-value action is *vetoed* before it reaches the
:class:`~modules.reasoning.decision_gate.DecisionGate`, giving the slower
:class:`~modules.reasoning.model_based.ModelBasedRL` system room to override
an impulsive choice (e.g. delay-of-gratification / go-no-go control,
Miller & Cohen 2001).

Inhibitory control rule
------------------------
On every timestep, :meth:`update` reads the action-value vector of the
impulsive (model-free) pathway and identifies its most-favoured action --
the "impulsive response" -- and its value. If that value exceeds
:meth:`effective_threshold`, PFC sets ``internal_state["inhibit"] = True`` and
zeroes that action's entry in the output gate (``spike_trains`` /
``internal_state["gate"]``); :class:`~modules.reasoning.decision_gate.DecisionGate`
multiplies its action probabilities by this gate before normalising.

Stress impairs control (SPEC-007 stress -> model-free transition)
-------------------------------------------------------------------
Acute stress / noradrenaline release impairs prefrontal function (Arnsten
2009): :meth:`apply_neuromodulation` raises :meth:`effective_threshold` in
proportion to noradrenaline above its baseline of ``1.0``, so under stress PFC
inhibits less often and the impulsive, model-free pathway is more likely to
reach the final decision unchecked -- complementing the arbitration shift
implemented in :class:`~modules.reasoning.decision_gate.DecisionGate`.

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

__all__ = ["PFCExecutive"]


class PFCExecutive(CognitiveModule):
    """Inhibitory-control gate over the impulsive (model-free) pathway.

    Args:
        module_id: Stable identifier for this module instance.
        n_actions: Number of discrete actions (must match the action-value
            vectors produced by :class:`~modules.reasoning.model_free.ModelFreeRL`).
        control_threshold: Baseline value above which the most-favoured
            impulsive action is inhibited.
        noradrenaline_sensitivity: How strongly noradrenaline above its
            baseline of ``1.0`` raises :meth:`effective_threshold` (stress
            impairs control).
        max_rate_hz: Firing rate mapped to gate value ``1.0``.
    """

    def __init__(
        self,
        module_id: str = "pfc_executive",
        n_actions: int = 2,
        control_threshold: float = 0.5,
        noradrenaline_sensitivity: float = 1.0,
        max_rate_hz: float = 50.0,
    ) -> None:
        if n_actions < 2:
            raise ValueError("n_actions must be >= 2")
        super().__init__(module_id, n_actions)

        self.n_actions = n_actions
        self.control_threshold = control_threshold
        self.noradrenaline_sensitivity = noradrenaline_sensitivity
        self.max_rate_hz = max_rate_hz

        self._noradrenaline = 1.0
        self._last_gate = np.ones(n_actions)
        self._last_inhibit = False
        self._last_impulsive_action: Optional[int] = None
        self._timestamp_ms = 0.0

    # -- control logic -----------------------------------------------------------

    def effective_threshold(self) -> float:
        """Control threshold after stress-driven impairment.

        ``threshold = control_threshold * (1 + sensitivity * max(0,
        noradrenaline - 1))`` -- noradrenaline at its basal level of ``1.0``
        leaves the threshold unchanged; elevated noradrenaline (stress) raises
        it, making inhibition less likely.
        """
        excess = max(0.0, self._noradrenaline - 1.0)
        return self.control_threshold * (1.0 + self.noradrenaline_sensitivity * excess)

    # -- CognitiveModule contract ------------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        """Inspect the impulsive pathway's action values and gate accordingly.

        ``inputs.spike_trains`` is expected to be the action-value /
        action-probability vector of the model-free pathway, length
        :attr:`n_actions`.
        """
        self._timestamp_ms = inputs.timestamp_ms
        self._noradrenaline = inputs.neuromodulation.noradrenaline
        values = align_to(inputs.spike_trains, self.n_actions)

        impulsive_action = int(np.argmax(values))
        impulsive_value = float(values[impulsive_action])
        threshold = self.effective_threshold()
        inhibit = impulsive_value > threshold

        gate = np.ones(self.n_actions)
        if inhibit:
            gate[impulsive_action] = 0.0

        self._last_gate = gate
        self._last_inhibit = inhibit
        self._last_impulsive_action = impulsive_action

        return ModuleOutputs(
            spike_trains=gate,
            firing_rate=gate * self.max_rate_hz,
            internal_state={
                "inhibit": inhibit,
                "inhibited_action": impulsive_action if inhibit else None,
                "impulsive_action": impulsive_action,
                "impulsive_value": impulsive_value,
                "effective_threshold": threshold,
                "gate": gate.copy(),
            },
        )

    def get_state(self) -> ModuleState:
        voltage = -70.0 + 25.0 * self._last_gate
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=voltage,
            firing_rate=self._last_gate * self.max_rate_hz,
            mean_weight=float(self._last_gate.mean()),
            active_synapses=int(np.count_nonzero(self._last_gate)),
            timestamp_ms=self._timestamp_ms,
            metadata={
                "inhibit": self._last_inhibit,
                "inhibited_action": (
                    self._last_impulsive_action if self._last_inhibit else None
                ),
                "effective_threshold": self.effective_threshold(),
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Noradrenaline raises :meth:`effective_threshold` (stress impairs control)."""
        self._noradrenaline = signal.noradrenaline

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        """PFC owns no learned synapses -- it gates other modules' outputs."""
        return []

    def reset(self) -> None:
        self._noradrenaline = 1.0
        self._last_gate = np.ones(self.n_actions)
        self._last_inhibit = False
        self._last_impulsive_action = None
        self._timestamp_ms = 0.0
