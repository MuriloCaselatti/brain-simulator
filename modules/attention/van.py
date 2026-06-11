"""Brain Simulator -- VAN (Ventral Attention Network).

Implements :class:`VAN`, the bottom-up reflexive attention module (SPEC-005).
VAN consumes the per-location saliency values produced by
:class:`~modules.attention.saliency.SaliencyMap` (via
``ModuleInputs.spike_trains``) and, when the maximum saliency exceeds an
effective interrupt threshold, raises an "interrupt" for the current tick.
Conforms to the frozen SPEC-001 :class:`~core.interfaces.CognitiveModule`
contract.

Because the BrainBus/SimulationEngine clock is synchronous at ``dt = 1ms``
(ADR-003), VAN's interrupt decision is computed and published within the same
1ms tick that the triggering saliency event arrives -- well within the
SPEC-005 acceptance criterion of interrupting in < 20ms simulated.

Wiring convention
------------------
``VAN`` is registered with ``depends_on=[saliency_module_id]``. When
triggered, ``ModuleOutputs.internal_state["interrupt"]`` is ``True``,
``["interrupt_location"]`` indexes the salient location, and
``["attention_signal"]`` is set to :attr:`redirect_attention_signal` -- a low
value that, propagated by the :class:`~core.simulation_engine.SimulationEngine`
as ``ModuleInputs.attention_signal`` on the following tick, redirects gain
away from the previous top-down focus toward the bottom-up event.

DAN-VAN anticorrelation (SPEC-005 acceptance criteria)
-------------------------------------------------------
VAN's own activation is exposed via :attr:`van_activation` for
:meth:`modules.attention.dan.DAN.set_van_activation`. Symmetrically, DAN's
current top-down focus is read back via :meth:`set_dan_suppression`, raising
VAN's effective threshold while DAN is strongly engaged -- so a focused
top-down search is less easily derailed by minor distractors.
"""
from __future__ import annotations

from typing import List

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

__all__ = ["VAN", "DEFAULT_INTERRUPT_THRESHOLD"]

DEFAULT_INTERRUPT_THRESHOLD = 0.7


class VAN(CognitiveModule):
    """Ventral Attention Network -- bottom-up reflexive attention.

    Args:
        module_id: Stable identifier for this module instance.
        n_neurons: Size of the map. Should match the size of the
            :class:`~modules.attention.saliency.SaliencyMap` it observes.
        interrupt_threshold: Saliency level (in ``[0, 1]``) above which the
            maximum-saliency location triggers an interrupt.
        dan_suppression_strength: How strongly DAN's top-down focus (set via
            :meth:`set_dan_suppression`) raises the effective interrupt
            threshold, in ``[0, 1]``.
        redirect_attention_signal: The ``attention_signal`` value published
            when an interrupt fires, redirecting gain toward the
            bottom-up event.
    """

    def __init__(
        self,
        module_id: str,
        n_neurons: int,
        interrupt_threshold: float = DEFAULT_INTERRUPT_THRESHOLD,
        dan_suppression_strength: float = 1.0,
        redirect_attention_signal: float = 0.1,
    ) -> None:
        super().__init__(module_id, n_neurons)
        self.interrupt_threshold = interrupt_threshold
        self.dan_suppression_strength = dan_suppression_strength
        self.redirect_attention_signal = redirect_attention_signal

        self._acetylcholine_gain = 1.0
        self._dan_focus = 0.0

        self.van_activation = 0.0
        self.interrupt = False
        self.interrupt_location = -1
        self._timestamp_ms = 0.0

    # -- DAN-VAN coupling -----------------------------------------------------

    def set_dan_suppression(self, dan_focus: float) -> None:
        """Receive DAN's current top-down focus for DAN-VAN anticorrelation.

        ``dan_focus`` is clamped to ``[0, 1]``. A strongly engaged DAN raises
        VAN's effective interrupt threshold proportionally to
        :attr:`dan_suppression_strength`.
        """
        self._dan_focus = float(np.clip(dan_focus, 0.0, 1.0))

    @property
    def effective_threshold(self) -> float:
        """The current interrupt threshold after DAN suppression and ACh gating."""
        raised = self.interrupt_threshold + self._dan_focus * self.dan_suppression_strength
        return raised / max(self._acetylcholine_gain, 1e-3)

    # -- CognitiveModule contract -------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        saliency = align_to(inputs.spike_trains, self.n_neurons)

        max_saliency = float(saliency.max()) if saliency.size else 0.0
        max_idx = int(np.argmax(saliency)) if saliency.size else -1

        triggered = max_saliency >= self.effective_threshold

        self.interrupt = triggered
        self.interrupt_location = max_idx if triggered else -1
        self.van_activation = max_saliency if triggered else 0.0
        self._timestamp_ms = inputs.timestamp_ms

        spikes = np.zeros(self.n_neurons)
        internal_state = {
            "interrupt": triggered,
            "interrupt_location": self.interrupt_location,
            "van_activation": self.van_activation,
            "max_saliency": max_saliency,
        }
        if triggered:
            spikes[max_idx] = 1.0
            internal_state["attention_signal"] = self.redirect_attention_signal

        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=spikes * 100.0,
            internal_state=internal_state,
        )

    def get_state(self) -> ModuleState:
        firing_rate = np.zeros(self.n_neurons)
        if self.interrupt and 0 <= self.interrupt_location < self.n_neurons:
            firing_rate[self.interrupt_location] = 100.0
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=np.zeros(self.n_neurons),
            firing_rate=firing_rate,
            mean_weight=0.0,
            active_synapses=0,
            timestamp_ms=self._timestamp_ms,
            metadata={
                "interrupt": self.interrupt,
                "interrupt_location": self.interrupt_location,
                "van_activation": self.van_activation,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Acetylcholine sharpens reflexive sensitivity by lowering the
        effective interrupt threshold (see :attr:`effective_threshold`)."""
        self._acetylcholine_gain = max(0.0, signal.acetylcholine)

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        # VAN has no plastic synapses of its own.
        return []

    def reset(self) -> None:
        self.van_activation = 0.0
        self.interrupt = False
        self.interrupt_location = -1
        self._dan_focus = 0.0
        self._acetylcholine_gain = 1.0
        self._timestamp_ms = 0.0
