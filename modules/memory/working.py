"""Brain Simulator -- Working Memory Module (SPEC-004).

Implements a discrete-attractor recurrent network modelling prefrontal
"working memory": ~7 mutually-inhibiting neuron pools (Miller's magic
number), each of which is bistable. A cue that strongly overlaps one pool
pushes that pool into a high-activity fixed point; once there, recurrent
self-excitation sustains the activity for hundreds of milliseconds with
*no further input* -- the hallmark of delay-period persistent activity
recorded in PFC during working-memory tasks.

Dynamics
--------
Each attractor pool has a single scalar activation "level" in ``[0, 1]``
(shared by every neuron in the pool while it is the active attractor).
The level evolves under leaky, self-exciting dynamics::

    x = gain * level - threshold + drive
    level += dt/tau * (-level + sigmoid(x))

With ``gain=8`` and ``threshold=4`` this ODE is bistable: a "low" fixed
point near ``sigmoid(-4) ~= 0.018`` and a "high" fixed point near
``sigmoid(4) ~= 0.982``. A cue matching a pool injects ``drive`` into
``x``, kicking that pool's level from low to high. With no input
(``drive = 0``) the high fixed point remains a stable attractor, so the
pattern persists.

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

__all__ = ["WorkingMemory"]


def _sigmoid(x: float) -> float:
    return 1.0 / (1.0 + np.exp(-x))


class WorkingMemory(CognitiveModule):
    """Recurrent attractor network with ``N_ATTRACTORS`` discrete slots.

    Args:
        module_id: Stable identifier for this module instance.
        n_neurons: Total neuron count, split evenly across
            :attr:`N_ATTRACTORS` pools (extra neurons beyond the last
            full pool are inert "spare" units).
        gain: Recurrent self-excitation gain of the active pool.
        threshold: Activation threshold (bias) of the bistable dynamics.
        tau_ms: Time constant of the leaky integrator, in milliseconds.
        drive_strength: Scaling of the external cue drive that can switch
            the active attractor.
        match_threshold: Minimum normalized cue/pattern overlap, in
            ``[0, 1]``, required to (re)select an attractor.
        max_rate_hz: Firing rate corresponding to ``level == 1.0``.
    """

    N_ATTRACTORS = 7

    def __init__(
        self,
        module_id: str = "working_memory",
        n_neurons: int = 70,
        gain: float = 8.0,
        threshold: float = 4.0,
        tau_ms: float = 20.0,
        drive_strength: float = 10.0,
        match_threshold: float = 0.5,
        max_rate_hz: float = 50.0,
    ) -> None:
        super().__init__(module_id, n_neurons)
        if n_neurons < self.N_ATTRACTORS:
            raise ValueError(
                f"n_neurons ({n_neurons}) must be >= N_ATTRACTORS "
                f"({self.N_ATTRACTORS})"
            )

        self._gain = gain
        self._threshold = threshold
        self._tau_ms = tau_ms
        self._drive_strength = drive_strength
        self._match_threshold = match_threshold
        self._max_rate_hz = max_rate_hz

        self._neurons_per_attractor = n_neurons // self.N_ATTRACTORS
        self._patterns = np.zeros((self.N_ATTRACTORS, n_neurons))
        for k in range(self.N_ATTRACTORS):
            start = k * self._neurons_per_attractor
            end = start + self._neurons_per_attractor
            self._patterns[k, start:end] = 1.0

        self._weights = self._build_weight_matrix()
        self._low_fixed_point = float(_sigmoid(-self._threshold))

        self._level = self._low_fixed_point
        self._active_attractor: Optional[int] = None
        self._last_signal = NeuromodulationSignal()
        self._timestamp_ms = 0.0

    # -- internal helpers ---------------------------------------------------

    def _build_weight_matrix(self) -> np.ndarray:
        """Block-structured recurrent weights: excitatory within a pool,
        inhibitory across pools (winner-take-all)."""
        n = self.n_neurons
        weights = np.full((n, n), -0.1)
        for k in range(self.N_ATTRACTORS):
            start = k * self._neurons_per_attractor
            end = start + self._neurons_per_attractor
            weights[start:end, start:end] = 1.0
        np.fill_diagonal(weights, 0.0)
        return weights

    def _project_cue(self, spike_trains: np.ndarray) -> np.ndarray:
        spike_trains = np.asarray(spike_trains, dtype=float)
        if spike_trains.size == 0:
            return np.zeros(self.n_neurons)
        if spike_trains.size == self.n_neurons:
            return spike_trains
        reps = int(np.ceil(self.n_neurons / spike_trains.size))
        return np.tile(spike_trains, reps)[: self.n_neurons]

    def _activity(self) -> np.ndarray:
        if self._active_attractor is None:
            return np.zeros(self.n_neurons)
        return self._patterns[self._active_attractor] * self._level

    # -- CognitiveModule contract --------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        cue = self._project_cue(inputs.spike_trains)

        matches = self._patterns @ cue
        if self._neurons_per_attractor > 0:
            matches = matches / self._neurons_per_attractor

        best = int(np.argmax(matches))
        drive = 0.0
        if matches[best] > self._match_threshold:
            self._active_attractor = best
            drive = (
                self._drive_strength * matches[best] * inputs.attention_signal
            )

        gain = self._gain * self._last_signal.noradrenaline
        x = gain * self._level - self._threshold + drive
        self._level += dt * (-self._level + _sigmoid(x)) / self._tau_ms
        self._level = float(np.clip(self._level, 0.0, 1.0))

        self._timestamp_ms = inputs.timestamp_ms
        activity = self._activity()
        spikes = (activity > 0.5).astype(float)
        firing_rate = activity * self._max_rate_hz

        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=firing_rate,
            internal_state={
                "active_attractor": self._active_attractor,
                "level": self._level,
            },
        )

    def get_state(self) -> ModuleState:
        activity = self._activity()
        voltage = -70.0 + 40.0 * activity
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=voltage,
            firing_rate=activity * self._max_rate_hz,
            mean_weight=float(self._weights.mean()),
            active_synapses=int(np.count_nonzero(self._weights)),
            timestamp_ms=self._timestamp_ms,
            metadata={
                "active_attractor": self._active_attractor,
                "level": self._level,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        self._last_signal = signal

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        return [
            SynapticTarget(
                source_module=self.module_id,
                target_module=self.module_id,
                weight_matrix=self._weights,
                synapse_type="excitatory",
            )
        ]

    def reset(self) -> None:
        self._level = self._low_fixed_point
        self._active_attractor = None
        self._last_signal = NeuromodulationSignal()
        self._timestamp_ms = 0.0
