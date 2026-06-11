"""Brain Simulator -- Noradrenaline system (SPEC-008).

Implements :class:`NoradrenalineSystem`, the arousal channel of the global
neuromodulatory state (locus coeruleus; Aston-Jones & Cohen 2005). Noradrenaline
tracks arousal / unexpected uncertainty and is consumed by
:meth:`~core.neuron.LIFPopulation.apply_neuromodulation`, where an above-basal
level *lowers* the firing threshold and makes neurons more responsive
(SPEC-008 acceptance criterion).

Like :class:`~modules.neuromodulation.dopamine.DopamineSystem`, this is a plain
helper owned by :class:`~modules.neuromodulation.system.NeuromodulatorSystem`,
not a :class:`~core.interfaces.CognitiveModule`.
"""
from __future__ import annotations

import math

from modules.neuromodulation.dopamine import BASAL_LEVEL, _clip

__all__ = ["NoradrenalineSystem"]


class NoradrenalineSystem:
    """Maps an arousal drive in ``[0, 1]`` to a noradrenaline level.

    The level is ``clip(1.0 + gain * arousal, 0, 2)``: zero arousal leaves the
    system at the basal level ``1.0``; maximal arousal (``arousal == 1`` with
    ``gain == 1``) drives it to ``2.0``, the strongest excitability boost.

    Args:
        gain: Sensitivity of the level to the arousal drive.
        tau_ms: Time constant (ms) of the exponential relaxation of arousal
            back to its tonic baseline of zero.
    """

    def __init__(self, gain: float = 1.0, tau_ms: float = 200.0) -> None:
        self.gain = gain
        self.tau_ms = tau_ms
        self.level = BASAL_LEVEL
        self._arousal = 0.0

    def set_arousal(self, arousal: float) -> None:
        """Set the current arousal drive, clamped to ``[0, 1]``."""
        self._arousal = max(0.0, min(1.0, float(arousal)))

    def step(self, dt: float) -> float:
        """Advance by ``dt`` ms and return the current noradrenaline level."""
        self.level = _clip(BASAL_LEVEL + self.gain * self._arousal)
        if self.tau_ms > 0.0:
            self._arousal *= math.exp(-dt / self.tau_ms)
        else:
            self._arousal = 0.0
        return self.level

    def reset(self) -> None:
        self.level = BASAL_LEVEL
        self._arousal = 0.0
