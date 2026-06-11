"""Brain Simulator -- SaliencyMap.

Implements :class:`SaliencyMap`, a computational saliency map (SPEC-005) that
prioritizes sensory input by combining a center-surround spatial contrast
with a temporal novelty signal (deviation from a running average of
activity). Conforms to the frozen SPEC-001
:class:`~core.interfaces.CognitiveModule` contract.

Wiring convention
------------------
``SaliencyMap`` is registered with ``depends_on=[sensory_module_id]``: each
tick, ``ModuleInputs.spike_trains`` is the sensory population's spike output.
Its own output -- a per-location saliency value in ``[0, 1]`` -- is exposed
both as ``ModuleOutputs.spike_trains`` and as
``ModuleOutputs.internal_state["saliency_map"]``, and is consumed by
:class:`~modules.attention.van.VAN` (registered with
``depends_on=[saliency_module_id]``) to detect high-saliency events.
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
from modules.attention._utils import align_to, center_surround_contrast, normalize

__all__ = ["SaliencyMap"]


class SaliencyMap(CognitiveModule):
    """Computational saliency map over a sensory population.

    For each location ``i`` the raw saliency combines:

    * **Novelty** -- ``|activity[i] - running_avg[i]|``, where
      ``running_avg`` is an exponential moving average of ``activity`` with
      time constant :attr:`novelty_tau_ms`.
    * **Spatial contrast** -- ``|center_surround_contrast(activity)[i]|``,
      a discrete center-surround receptive field (see
      :func:`modules.attention._utils.center_surround_contrast`), weighted by
      :attr:`contrast_weight`.

    The combined raw saliency is scaled by the noradrenaline-driven arousal
    gain (see :meth:`apply_neuromodulation`) and normalized to ``[0, 1]``.

    Args:
        module_id: Stable identifier for this module instance.
        n_neurons: Size of the saliency map. Should match the size of the
            sensory population it observes.
        novelty_tau_ms: Time constant (ms) of the running-average novelty
            detector.
        contrast_weight: Weight of the spatial contrast term relative to
            novelty.
        salience_threshold: Saliency level (in ``[0, 1]``) above which a
            location is reported as "salient" via ``firing_rate``.
    """

    def __init__(
        self,
        module_id: str,
        n_neurons: int,
        novelty_tau_ms: float = 50.0,
        contrast_weight: float = 0.5,
        salience_threshold: float = 0.3,
    ) -> None:
        if novelty_tau_ms <= 0:
            raise ValueError("novelty_tau_ms must be positive")

        super().__init__(module_id, n_neurons)
        self.novelty_tau_ms = novelty_tau_ms
        self.contrast_weight = contrast_weight
        self.salience_threshold = salience_threshold

        self._running_avg = np.zeros(n_neurons)
        self._noradrenaline_gain = 1.0
        self._saliency_map = np.zeros(n_neurons)
        self._timestamp_ms = 0.0

    # -- CognitiveModule contract -------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        activity = align_to(inputs.spike_trains, self.n_neurons)

        novelty = np.abs(activity - self._running_avg)
        alpha = min(1.0, dt / self.novelty_tau_ms)
        self._running_avg += alpha * (activity - self._running_avg)

        contrast = np.abs(center_surround_contrast(activity))

        raw = (novelty + self.contrast_weight * contrast) * self._noradrenaline_gain
        saliency = normalize(raw)

        self._saliency_map = saliency
        self._timestamp_ms = inputs.timestamp_ms

        salient_mask = (saliency >= self.salience_threshold).astype(float)
        max_saliency = float(saliency.max()) if saliency.size else 0.0
        max_idx = int(np.argmax(saliency)) if saliency.size else -1

        return ModuleOutputs(
            spike_trains=saliency,
            firing_rate=salient_mask * 100.0,
            internal_state={
                "saliency_map": saliency,
                "max_saliency": max_saliency,
                "max_saliency_index": max_idx,
            },
        )

    def get_state(self) -> ModuleState:
        max_saliency = float(self._saliency_map.max()) if self._saliency_map.size else 0.0
        max_idx = int(np.argmax(self._saliency_map)) if self._saliency_map.size else -1
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=np.zeros(self.n_neurons),
            firing_rate=self._saliency_map * 100.0,
            mean_weight=0.0,
            active_synapses=0,
            timestamp_ms=self._timestamp_ms,
            metadata={
                "max_saliency": max_saliency,
                "max_saliency_index": max_idx,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Noradrenaline scales the arousal gain applied to raw saliency.

        Above-basal noradrenaline (arousal) amplifies novelty/contrast
        signals before normalization, making the map more sensitive overall.
        """
        self._noradrenaline_gain = max(0.0, signal.noradrenaline)

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        # SaliencyMap has no plastic synapses of its own.
        return []

    def reset(self) -> None:
        self._running_avg = np.zeros(self.n_neurons)
        self._saliency_map = np.zeros(self.n_neurons)
        self._noradrenaline_gain = 1.0
        self._timestamp_ms = 0.0
