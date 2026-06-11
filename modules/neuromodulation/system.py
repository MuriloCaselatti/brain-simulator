"""Brain Simulator -- NeuromodulatorSystem (SPEC-008).

Implements :class:`NeuromodulatorSystem`, the single :class:`CognitiveModule`
that centralises the three neuromodulatory channels -- dopamine, noradrenaline
and acetylcholine -- and emits the **global** :class:`NeuromodulationSignal`
that the :class:`~core.simulation_engine.SimulationEngine` broadcasts to every
module each tick.

It sits late in the documented execution chain
(``Reasoning -> Neuromodulators -> LearningEngine``): it samples this tick's
drivers (TD-error, arousal, attention/uncertainty), advances the three
sub-systems, and publishes the resulting signal, which the engine applies to all
modules on the *next* tick (the synchronous one-tick BrainBus latency).

Drivers
-------
* **Dopamine** -- the TD-error. Either fed explicitly via :meth:`set_td_error`
  / :meth:`observe_reward`, or pulled automatically from a connected
  :class:`~core.learning_engine.LearningEngine` (see :meth:`connect_learning_engine`).
* **Noradrenaline** -- an arousal level in ``[0, 1]`` via :meth:`set_arousal`.
* **Acetylcholine** -- top-down attention (defaults to ``inputs.attention_signal``)
  and expected uncertainty via :meth:`set_attention` / :meth:`set_uncertainty`.

The three channels are plain helpers (``DopamineSystem`` etc.), mutated in place
by this owner -- the same ownership pattern as
:class:`~core.synapse.STDPSynapse` under
:class:`~core.learning_engine.LearningEngine` (ADR-008).
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
from modules.neuromodulation.acetylcholine import AcetylcholineSystem
from modules.neuromodulation.dopamine import DopamineSystem
from modules.neuromodulation.noradrenaline import NoradrenalineSystem

__all__ = ["NeuromodulatorSystem"]


class NeuromodulatorSystem(CognitiveModule):
    """Centralises the dopamine, noradrenaline and acetylcholine channels.

    Owns no neurons (``n_neurons == 0``); its observable "state" is the current
    global :class:`NeuromodulationSignal`, exposed via :attr:`current_signal`.
    """

    def __init__(self, module_id: str = "neuromodulators") -> None:
        super().__init__(module_id, n_neurons=0)
        self.dopamine = DopamineSystem()
        self.noradrenaline = NoradrenalineSystem()
        self.acetylcholine = AcetylcholineSystem()

        self._learning_engine = None  # type: Optional[object]
        self._explicit_attention = False
        self._last_timestamp_ms = 0.0
        self._last_td_error = 0.0

    # -- Configuration ---------------------------------------------------------

    def connect_learning_engine(self, learning_engine) -> None:
        """Pull the TD-error from ``learning_engine`` automatically each tick.

        The dopamine drive is taken from ``learning_engine.last_td_error`` at
        the start of every :meth:`update`, closing the loop in which a
        dopaminergic burst scales STDP/TD learning back in the
        :class:`~core.learning_engine.PlasticityScheduler`.
        """
        self._learning_engine = learning_engine

    # -- Drivers ---------------------------------------------------------------

    def set_td_error(self, td_error: float) -> None:
        """Drive dopamine directly with a TD-error event."""
        self.dopamine.set_td_error(td_error)

    def observe_reward(self, reward: float, value_estimate: float = 0.0) -> float:
        """Convenience: drive dopamine from a reward vs. its prediction.

        Computes ``td_error = reward - value_estimate`` (Schultz 1997
        reward-prediction error) and feeds it to the dopamine channel.
        Returns the TD-error.
        """
        td_error = float(reward) - float(value_estimate)
        self.dopamine.set_td_error(td_error)
        return td_error

    def set_arousal(self, arousal: float) -> None:
        """Drive noradrenaline with an arousal level in ``[0, 1]``."""
        self.noradrenaline.set_arousal(arousal)

    def set_attention(self, attention: float) -> None:
        """Drive acetylcholine with a top-down attention level in ``[0, 1]``.

        Setting this overrides the default of reading ``inputs.attention_signal``
        in :meth:`update`.
        """
        self._explicit_attention = True
        self.acetylcholine.set_attention(attention)

    def set_uncertainty(self, uncertainty: float) -> None:
        """Drive acetylcholine with an expected-uncertainty level in ``[0, 1]``."""
        self.acetylcholine.set_uncertainty(uncertainty)

    # -- CognitiveModule contract ----------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        """Sample drivers, advance the three channels, emit the global signal."""
        self._last_timestamp_ms = inputs.timestamp_ms

        if self._learning_engine is not None:
            td = float(getattr(self._learning_engine, "last_td_error", 0.0))
            self._last_td_error = td
            self.dopamine.set_td_error(td)

        # Default the ACh attention drive to the engine-propagated attention
        # signal unless an explicit override was provided this tick.
        if not self._explicit_attention:
            self.acetylcholine.set_attention(inputs.attention_signal)
        self._explicit_attention = False

        da = self.dopamine.step(dt)
        na = self.noradrenaline.step(dt)
        ach = self.acetylcholine.step(dt)

        return ModuleOutputs(
            spike_trains=np.zeros(0),
            firing_rate=np.zeros(0),
            internal_state={
                "dopamine": da,
                "noradrenaline": na,
                "acetylcholine": ach,
                "td_error": self._last_td_error,
                "dopamine_burst": self.dopamine.is_burst,
                "dopamine_dip": self.dopamine.is_dip,
            },
        )

    @property
    def current_signal(self) -> NeuromodulationSignal:
        """The current global neuromodulatory signal (broadcast by the engine)."""
        return NeuromodulationSignal(
            dopamine=self.dopamine.level,
            noradrenaline=self.noradrenaline.level,
            acetylcholine=self.acetylcholine.level,
        )

    def get_state(self) -> ModuleState:
        return ModuleState(
            module_id=self.module_id,
            n_neurons=0,
            voltage=np.zeros(0),
            firing_rate=np.zeros(0),
            mean_weight=0.0,
            active_synapses=0,
            timestamp_ms=self._last_timestamp_ms,
            metadata={
                "dopamine": self.dopamine.level,
                "noradrenaline": self.noradrenaline.level,
                "acetylcholine": self.acetylcholine.level,
                "td_error": self._last_td_error,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        # The NeuromodulatorSystem is the *source* of the global signal, not a
        # sink: it does not modulate itself. Implemented as a no-op to satisfy
        # the frozen CognitiveModule contract.
        return None

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        return []

    def reset(self) -> None:
        self.dopamine.reset()
        self.noradrenaline.reset()
        self.acetylcholine.reset()
        self._explicit_attention = False
        self._last_timestamp_ms = 0.0
        self._last_td_error = 0.0
