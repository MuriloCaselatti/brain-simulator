"""Brain Simulator -- DAN (Dorsal Attention Network).

Implements :class:`DAN`, the top-down voluntary attention module (SPEC-005).
DAN receives a target representation from the prefrontal cortex (PFC) via
``ModuleInputs.spike_trains`` -- a per-location vector in ``[0, 1]`` encoding
how strongly each location of the sensory population is the current
behavioural goal -- and produces a per-location gain map that amplifies that
target representation relative to distractors. Conforms to the frozen
SPEC-001 :class:`~core.interfaces.CognitiveModule` contract.

Wiring convention
------------------
``DAN`` is registered with ``depends_on=[pfc_module_id]``. Its output gain
map is exposed both as ``ModuleOutputs.spike_trains`` and as
``ModuleOutputs.internal_state["gain_map"]``, for a sensory module
(:class:`~core.neuron.LIFPopulation`) to apply as a per-neuron multiplicative
drive. A scalar summary is also published as
``ModuleOutputs.internal_state["attention_signal"]``, which the
:class:`~core.simulation_engine.SimulationEngine` propagates as
``ModuleInputs.attention_signal`` on the following tick.

DAN-VAN anticorrelation (SPEC-005 acceptance criteria)
-------------------------------------------------------
A high :class:`~modules.attention.van.VAN` activation -- signalling a
bottom-up interrupt -- suppresses DAN's top-down gain via
:meth:`set_van_activation`. Symmetrically, DAN's own focus strength
(:attr:`dan_focus`) is exposed for VAN to read back via
:meth:`modules.attention.van.VAN.set_dan_suppression`, raising VAN's
threshold while DAN is strongly engaged.
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

__all__ = ["DAN", "DEFAULT_GAIN_AMPLIFICATION", "DEFAULT_BASELINE_GAIN"]

# SPEC-005 acceptance: with a fully-engaged target (pfc_signal == 1.0) and a
# fully-suppressed distractor (pfc_signal == 0.0), the target gain must be
# >= 2x the distractor gain: (baseline + 1.0 * amplification) / baseline >= 2.
DEFAULT_GAIN_AMPLIFICATION = 2.5
DEFAULT_BASELINE_GAIN = 1.0


class DAN(CognitiveModule):
    """Dorsal Attention Network -- top-down voluntary attention.

    Args:
        module_id: Stable identifier for this module instance.
        n_neurons: Size of the gain map. Should match the size of the
            sensory population it modulates.
        gain_amplification: Additional gain (on top of
            :attr:`baseline_gain`) applied at locations where the PFC
            top-down signal is at its maximum (``1.0``).
        baseline_gain: Gain applied at locations with no top-down drive
            (distractors).
        van_suppression_strength: How strongly a high
            :class:`~modules.attention.van.VAN` activation (set via
            :meth:`set_van_activation`) suppresses the top-down gain,
            in ``[0, 1]``: ``1.0`` means full VAN activation zeroes out
            the top-down amplification entirely.
    """

    def __init__(
        self,
        module_id: str,
        n_neurons: int,
        gain_amplification: float = DEFAULT_GAIN_AMPLIFICATION,
        baseline_gain: float = DEFAULT_BASELINE_GAIN,
        van_suppression_strength: float = 1.0,
    ) -> None:
        super().__init__(module_id, n_neurons)
        self.gain_amplification = gain_amplification
        self.baseline_gain = baseline_gain
        self.van_suppression_strength = van_suppression_strength

        self._acetylcholine_gain = 1.0
        self._van_activation = 0.0

        self._gain_map = np.full(n_neurons, baseline_gain)
        self.dan_focus = 0.0
        self._timestamp_ms = 0.0

    # -- DAN-VAN coupling -----------------------------------------------------

    def set_van_activation(self, activation: float) -> None:
        """Receive VAN's current activation for DAN-VAN anticorrelation.

        ``activation`` is clamped to ``[0, 1]``. A strong bottom-up
        interrupt suppresses DAN's top-down gain proportionally to
        :attr:`van_suppression_strength`.
        """
        self._van_activation = float(np.clip(activation, 0.0, 1.0))

    @property
    def gain_map(self) -> np.ndarray:
        """The most recently computed per-location gain map."""
        return self._gain_map

    # -- CognitiveModule contract -------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        pfc_signal = np.clip(align_to(inputs.spike_trains, self.n_neurons), 0.0, None)

        suppression = max(
            0.0, 1.0 - self._van_activation * self.van_suppression_strength
        )

        gain_map = self.baseline_gain + (
            pfc_signal * self.gain_amplification * self._acetylcholine_gain * suppression
        )
        self._gain_map = gain_map
        self._timestamp_ms = inputs.timestamp_ms

        self.dan_focus = float(np.max(pfc_signal)) * self._acetylcholine_gain * suppression
        attention_signal = float(np.clip(self.dan_focus, 0.0, 1.0))

        return ModuleOutputs(
            spike_trains=gain_map,
            firing_rate=gain_map * 10.0,
            internal_state={
                "gain_map": gain_map,
                "attention_signal": attention_signal,
                "dan_focus": self.dan_focus,
            },
        )

    def get_state(self) -> ModuleState:
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=np.zeros(self.n_neurons),
            firing_rate=self._gain_map * 10.0,
            mean_weight=float(np.mean(self._gain_map)),
            active_synapses=0,
            timestamp_ms=self._timestamp_ms,
            metadata={
                "dan_focus": self.dan_focus,
                "van_activation": self._van_activation,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Acetylcholine scales the top-down gain amplification.

        Mirrors :meth:`core.neuron.LIFPopulation.apply_neuromodulation`'s
        acetylcholine gating of attentional signal-to-noise.
        """
        self._acetylcholine_gain = max(0.0, signal.acetylcholine)

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        # DAN has no plastic synapses of its own.
        return []

    def reset(self) -> None:
        self._gain_map = np.full(self.n_neurons, self.baseline_gain)
        self.dan_focus = 0.0
        self._van_activation = 0.0
        self._acetylcholine_gain = 1.0
        self._timestamp_ms = 0.0
