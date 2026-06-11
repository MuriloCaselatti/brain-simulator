"""Brain Simulator -- Learning Engine.

Implements :class:`LearningEngine`, the SPEC-003 module that drives synaptic
plasticity (STDP via :class:`~core.synapse.STDPSynapse`) and TD-Learning, and
:class:`PlasticityScheduler`, which gates plasticity and scales learning
rates from the global :class:`~core.interfaces.NeuromodulationSignal`.

``LearningEngine`` conforms to the frozen SPEC-001
:class:`~core.interfaces.CognitiveModule` contract so it can be plugged into
the :class:`~core.simulation_engine.SimulationEngine` like any other module.

Wiring convention
------------------
A :class:`LearningEngine` is registered with ``depends_on=[pre_module_id,
post_module_id, ...]`` for each STDP projection it manages, via
:meth:`LearningEngine.register_projection`. The
:class:`~core.simulation_engine.SimulationEngine` concatenates the
dependencies' spike trains in insertion order when building
:attr:`~core.interfaces.ModuleInputs.spike_trains`; :meth:`LearningEngine.update`
consumes that concatenation by walking the registered projections in the same
order, splitting off ``n_pre`` then ``n_post`` entries for each.

TD-Learning
-----------
Standard parameters (SPEC-003)::

    alpha = 0.1   gamma = 0.95

:meth:`LearningEngine.compute_td_error` implements the canonical one-step
TD(0) error ``delta = reward + gamma * V(s') - V(s)``, which is positive
whenever the received reward exceeds the current value estimate (Schultz
1997 dopaminergic prediction-error encoding).
"""
from __future__ import annotations

from dataclasses import dataclass
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
from core.synapse import STDPSynapse

__all__ = ["LearningEngine", "PlasticityScheduler", "TD_ALPHA", "TD_GAMMA"]

# Standard TD-Learning parameters (SPEC-003).
TD_ALPHA = 0.1
TD_GAMMA = 0.95


@dataclass
class _Projection:
    """A registered STDP projection between two modules."""

    synapse: STDPSynapse
    source_module: str
    target_module: str
    n_pre: int
    n_post: int


class PlasticityScheduler:
    """Gates STDP plasticity and scales its learning rate via neuromodulation.

    * ``acetylcholine`` gates plasticity on/off: STDP only runs while
      ``acetylcholine >= acetylcholine_threshold`` (and the scheduler has not
      been explicitly :meth:`disable`d).
    * ``dopamine`` scales the effective learning rate of both STDP
      (``lr_scale`` passed to :meth:`~core.synapse.STDPSynapse.update`) and
      TD-Learning value updates.
    """

    def __init__(self, acetylcholine_threshold: float = 0.3) -> None:
        self.acetylcholine_threshold = acetylcholine_threshold
        self._enabled = True

    def enable(self) -> None:
        """Re-enable plasticity (default state)."""
        self._enabled = True

    def disable(self) -> None:
        """Disable plasticity regardless of neuromodulation."""
        self._enabled = False

    def is_plastic(self, neuromodulation: NeuromodulationSignal) -> bool:
        """Return whether STDP/TD updates should be applied this timestep."""
        return self._enabled and neuromodulation.acetylcholine >= self.acetylcholine_threshold

    def learning_rate_scale(self, neuromodulation: NeuromodulationSignal) -> float:
        """Return the dopamine-driven learning-rate multiplier (>= 0)."""
        return max(0.0, neuromodulation.dopamine)


class LearningEngine(CognitiveModule):
    """Applies STDP to registered projections and tracks a TD-Learning value.

    ``LearningEngine`` owns no neurons of its own (``n_neurons == 0``); its
    "state" is the set of synaptic weight matrices it manages plus the scalar
    TD value estimate.
    """

    def __init__(
        self,
        module_id: str = "learning_engine",
        alpha: float = TD_ALPHA,
        gamma: float = TD_GAMMA,
    ) -> None:
        super().__init__(module_id, n_neurons=0)
        self.alpha = alpha
        self.gamma = gamma
        self.scheduler = PlasticityScheduler()

        self._projections: List[_Projection] = []
        self.value_estimate = 0.0
        self.last_td_error = 0.0
        self._last_timestamp_ms = 0.0
        self._last_neuromodulation = NeuromodulationSignal()

    # -- Configuration --------------------------------------------------------

    def register_projection(
        self,
        synapse: STDPSynapse,
        source_module: str,
        target_module: str,
        n_pre: Optional[int] = None,
        n_post: Optional[int] = None,
    ) -> None:
        """Register an STDP projection to be updated each tick.

        Args:
            synapse: The :class:`~core.synapse.STDPSynapse` instance.
            source_module: ``module_id`` of the presynaptic module. Must
                appear in this :class:`LearningEngine`'s ``depends_on`` list.
            target_module: ``module_id`` of the postsynaptic module. Must
                appear in this :class:`LearningEngine`'s ``depends_on`` list,
                after ``source_module``.
            n_pre: Number of presynaptic spike-train entries (defaults to
                ``synapse.n_pre``).
            n_post: Number of postsynaptic spike-train entries (defaults to
                ``synapse.n_post``).
        """
        self._projections.append(
            _Projection(
                synapse=synapse,
                source_module=source_module,
                target_module=target_module,
                n_pre=n_pre if n_pre is not None else synapse.n_pre,
                n_post=n_post if n_post is not None else synapse.n_post,
            )
        )

    # -- CognitiveModule contract ----------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        """Apply STDP to every registered projection for this timestep.

        ``inputs.spike_trains`` is expected to be the concatenation of the
        pre- and post-synaptic spike trains for each registered projection,
        in registration order (see module docstring).
        """
        self._last_timestamp_ms = inputs.timestamp_ms
        self._last_neuromodulation = inputs.neuromodulation

        plastic = self.scheduler.is_plastic(inputs.neuromodulation)
        lr_scale = self.scheduler.learning_rate_scale(inputs.neuromodulation)

        offset = 0
        total = inputs.spike_trains.size
        for projection in self._projections:
            needed = projection.n_pre + projection.n_post
            if offset + needed > total:
                break

            pre_spikes = inputs.spike_trains[offset : offset + projection.n_pre]
            offset += projection.n_pre
            post_spikes = inputs.spike_trains[offset : offset + projection.n_post]
            offset += projection.n_post

            if plastic:
                projection.synapse.update(dt, pre_spikes, post_spikes, lr_scale=lr_scale)

        return ModuleOutputs(
            spike_trains=np.zeros(0),
            firing_rate=np.zeros(0),
            internal_state={
                "plastic": plastic,
                "td_error": self.last_td_error,
                "value_estimate": self.value_estimate,
            },
        )

    def get_state(self) -> ModuleState:
        weight_means = [float(p.synapse.weight_matrix.mean()) for p in self._projections]
        active_synapses = sum(
            int(np.sum(p.synapse.weight_matrix > p.synapse.w_min)) for p in self._projections
        )
        return ModuleState(
            module_id=self.module_id,
            n_neurons=0,
            voltage=np.zeros(0),
            firing_rate=np.zeros(0),
            mean_weight=float(np.mean(weight_means)) if weight_means else 0.0,
            active_synapses=active_synapses,
            timestamp_ms=self._last_timestamp_ms,
            metadata={
                "td_error": self.last_td_error,
                "value_estimate": self.value_estimate,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        self._last_neuromodulation = signal

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        return [
            SynapticTarget(
                source_module=p.source_module,
                target_module=p.target_module,
                weight_matrix=p.synapse.weight_matrix,
            )
            for p in self._projections
        ]

    def reset(self) -> None:
        for projection in self._projections:
            projection.synapse.reset()
        self.value_estimate = 0.0
        self.last_td_error = 0.0
        self._last_timestamp_ms = 0.0
        self._last_neuromodulation = NeuromodulationSignal()

    # -- TD-Learning ------------------------------------------------------------

    def compute_td_error(self, reward: float, value_next: float = 0.0) -> float:
        """Compute and store the one-step TD(0) error.

        ``delta = reward + gamma * value_next - value_estimate``. Positive
        when ``reward`` exceeds the current value prediction (Schultz 1997).
        """
        td_error = reward + self.gamma * value_next - self.value_estimate
        self.last_td_error = td_error
        return td_error

    def apply_td_update(self, td_error: Optional[float] = None) -> float:
        """Apply a TD(0) update to :attr:`value_estimate`.

        Uses ``td_error`` if given, otherwise :attr:`last_td_error`. The
        learning rate ``alpha`` is scaled by the current dopamine level via
        :class:`PlasticityScheduler`.
        """
        if td_error is None:
            td_error = self.last_td_error
        lr_scale = self.scheduler.learning_rate_scale(self._last_neuromodulation)
        self.value_estimate += self.alpha * lr_scale * td_error
        return self.value_estimate
