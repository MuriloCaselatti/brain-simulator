"""Brain Simulator -- Acetylcholine system (SPEC-008).

Implements :class:`AcetylcholineSystem`, the attentional signal-to-noise /
plasticity channel of the global neuromodulatory state (basal forebrain;
Yu & Dayan 2005 -- expected uncertainty). Acetylcholine rises with top-down
attention and with expected uncertainty, and is consumed downstream by:

    * :meth:`~core.neuron.LIFPopulation.apply_neuromodulation` -- scales the
      attentional signal-to-noise gain on the presynaptic drive;
    * :class:`~core.learning_engine.PlasticityScheduler` -- gates STDP on/off
      (plasticity only runs while ``acetylcholine >= threshold``, default 0.3).

Like the other channels this is a plain helper owned by
:class:`~modules.neuromodulation.system.NeuromodulatorSystem`, not a
:class:`~core.interfaces.CognitiveModule`.
"""
from __future__ import annotations

import math

from modules.neuromodulation.dopamine import BASAL_LEVEL, _clip

__all__ = ["AcetylcholineSystem"]


class AcetylcholineSystem:
    """Maps top-down attention and expected uncertainty to an ACh level.

    The level is ``clip(1.0 + attention_gain * (attention - 0.5)
    + uncertainty_gain * uncertainty, 0, 2)``:

        * a neutral attention drive (``0.5``) with no uncertainty leaves the
          system at the basal level ``1.0``;
        * strong attention raises ACh (sharper signal-to-noise, plasticity
          open);
        * low attention lowers ACh and can close the plasticity gate.

    Args:
        attention_gain: Sensitivity of the level to the (centred) attention
            drive.
        uncertainty_gain: Additional drive contributed by expected uncertainty.
        tau_ms: Time constant (ms) of the relaxation of attention back to the
            neutral baseline (``0.5``) and uncertainty back to zero.
    """

    NEUTRAL_ATTENTION = 0.5

    def __init__(
        self,
        attention_gain: float = 1.0,
        uncertainty_gain: float = 0.5,
        tau_ms: float = 100.0,
    ) -> None:
        self.attention_gain = attention_gain
        self.uncertainty_gain = uncertainty_gain
        self.tau_ms = tau_ms
        self.level = BASAL_LEVEL
        self._attention = self.NEUTRAL_ATTENTION
        self._uncertainty = 0.0

    def set_attention(self, attention: float) -> None:
        """Set the top-down attention drive, clamped to ``[0, 1]``."""
        self._attention = max(0.0, min(1.0, float(attention)))

    def set_uncertainty(self, uncertainty: float) -> None:
        """Set the expected-uncertainty drive, clamped to ``[0, 1]``."""
        self._uncertainty = max(0.0, min(1.0, float(uncertainty)))

    def step(self, dt: float) -> float:
        """Advance by ``dt`` ms and return the current acetylcholine level."""
        self.level = _clip(
            BASAL_LEVEL
            + self.attention_gain * (self._attention - self.NEUTRAL_ATTENTION)
            + self.uncertainty_gain * self._uncertainty
        )
        if self.tau_ms > 0.0:
            decay = math.exp(-dt / self.tau_ms)
            self._attention = self.NEUTRAL_ATTENTION + (
                self._attention - self.NEUTRAL_ATTENTION
            ) * decay
            self._uncertainty *= decay
        else:
            self._attention = self.NEUTRAL_ATTENTION
            self._uncertainty = 0.0
        return self.level

    def reset(self) -> None:
        self.level = BASAL_LEVEL
        self._attention = self.NEUTRAL_ATTENTION
        self._uncertainty = 0.0
