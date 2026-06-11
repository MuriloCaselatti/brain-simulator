"""Brain Simulator -- Dopamine system (SPEC-008).

Implements :class:`DopamineSystem`, the reward-prediction-error channel of the
global neuromodulatory state. Dopamine encodes the temporal-difference (TD)
error broadcast by the :class:`~core.learning_engine.LearningEngine`
(Schultz 1997):

    * a **positive** TD-error (better-than-expected outcome) produces a phasic
      **burst** -- dopamine rises *above* the basal level ``1.0``;
    * a **negative** TD-error (omission of an expected reward) produces a phasic
      **dip** -- dopamine falls *below* basal toward ``0.0`` ("silence");
    * a **zero** TD-error (fully predicted outcome) leaves dopamine at basal.

The level is a multiplicative learning-rate factor consumed downstream by
:class:`~core.learning_engine.PlasticityScheduler.learning_rate_scale`, so a
burst amplifies STDP/TD learning across every module while a dip suppresses it.

This is a plain helper class -- like :class:`~core.synapse.STDPSynapse` and
:class:`~modules.predictive_coding.layer.PredictiveLayer`, it is **not** a
:class:`~core.interfaces.CognitiveModule`. It is owned and stepped by
:class:`~modules.neuromodulation.system.NeuromodulatorSystem`.
"""
from __future__ import annotations

import math

__all__ = ["DopamineSystem"]

# Convention shared across the neuromodulatory channels.
BASAL_LEVEL = 1.0
MIN_LEVEL = 0.0
MAX_LEVEL = 2.0


class DopamineSystem:
    """Maps TD-error to a phasic dopamine level centred on basal ``1.0``.

    Args:
        gain: Sensitivity of the level to the TD-error drive. The phasic
            response is ``clip(1.0 + gain * drive, 0, 2)``.
        tau_ms: Time constant (ms) of the exponential relaxation of the phasic
            drive back to zero (tonic baseline). Larger values sustain a burst
            for longer.
    """

    def __init__(self, gain: float = 1.0, tau_ms: float = 50.0) -> None:
        self.gain = gain
        self.tau_ms = tau_ms
        self.level = BASAL_LEVEL
        self._drive = 0.0

    def set_td_error(self, td_error: float) -> None:
        """Inject a new TD-error event, driving the next phasic response."""
        self._drive = float(td_error)

    def step(self, dt: float) -> float:
        """Advance by ``dt`` ms and return the current dopamine level.

        The level tracks the (decaying) TD-error drive; the drive itself
        relaxes exponentially toward zero so that, absent new events, dopamine
        returns to basal.
        """
        self.level = _clip(BASAL_LEVEL + self.gain * self._drive)
        if self.tau_ms > 0.0:
            self._drive *= math.exp(-dt / self.tau_ms)
        else:
            self._drive = 0.0
        return self.level

    @property
    def is_burst(self) -> bool:
        """Whether dopamine is currently above basal (phasic burst)."""
        return self.level > BASAL_LEVEL

    @property
    def is_dip(self) -> bool:
        """Whether dopamine is currently below basal (phasic dip / silence)."""
        return self.level < BASAL_LEVEL

    def reset(self) -> None:
        self.level = BASAL_LEVEL
        self._drive = 0.0


def _clip(value: float) -> float:
    return max(MIN_LEVEL, min(MAX_LEVEL, value))
