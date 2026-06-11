"""Brain Simulator -- Episodic Memory Module (SPEC-004).

Implements a *Modern* Hopfield Network (Ramsauer et al., 2020,
"Hopfield Networks is All You Need") -- **not** the classical binary
Hopfield network of Hopfield (1982).

The classical network stores patterns in a symmetric weight matrix
``W = sum_p p p^T`` and has a storage capacity of roughly ``0.14 * N``
patterns. The modern, continuous-state variant instead keeps the stored
patterns as rows of a matrix ``X`` and retrieves via a single
softmax-weighted update:

    xi_new = X^T softmax(beta * X xi)

This is exactly one step of attention (query ``xi``, keys/values ``X``).
For well-separated patterns and a sufficiently large inverse temperature
``beta``, this update converges in **one step** and the storage capacity
is exponential in the pattern dimension ``N`` -- in contrast to the
classical model's linear capacity.

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

__all__ = ["EpisodicMemory"]


def _softmax(x: np.ndarray) -> np.ndarray:
    shifted = x - np.max(x)
    exp = np.exp(shifted)
    return exp / exp.sum()


class EpisodicMemory(CognitiveModule):
    """Modern Hopfield Network associative memory.

    Stored patterns live in ``self._patterns`` with shape
    ``[n_patterns, n_neurons]``. Each row is a memory; retrieval is the
    continuous Ramsauer et al. (2020) update rule, applied for
    :attr:`n_iters` steps (default ``1``, which already converges for
    well-separated bipolar patterns).

    Args:
        module_id: Stable identifier for this module instance.
        n_neurons: Pattern dimensionality ``N``.
        beta: Inverse temperature controlling retrieval sharpness. Larger
            values give sharper (more separated) retrieval and higher
            effective capacity.
        max_patterns: Maximum number of stored patterns; oldest patterns
            are evicted (FIFO) once exceeded.
        n_iters: Number of softmax-update iterations applied per
            :meth:`retrieve` call.
        max_rate_hz: Firing rate corresponding to a fully "+1" neuron.
    """

    def __init__(
        self,
        module_id: str = "episodic_memory",
        n_neurons: int = 100,
        beta: float = 8.0,
        max_patterns: int = 64,
        n_iters: int = 1,
        max_rate_hz: float = 50.0,
    ) -> None:
        super().__init__(module_id, n_neurons)
        self._beta = beta
        self._max_patterns = max_patterns
        self._n_iters = max(1, n_iters)
        self._max_rate_hz = max_rate_hz

        self._patterns = np.zeros((0, n_neurons))
        self._labels: List[str] = []
        self._state = np.zeros(n_neurons)
        self._last_retrieval_index: Optional[int] = None
        self._last_confidence = 0.0
        self._last_signal = NeuromodulationSignal()
        self._timestamp_ms = 0.0

    @property
    def n_patterns(self) -> int:
        return self._patterns.shape[0]

    # -- storage / retrieval --------------------------------------------------

    def store_pattern(self, pattern, label: Optional[str] = None) -> int:
        """Store a pattern (shape ``[n_neurons]``), returning its index.

        If :attr:`max_patterns` is exceeded, the oldest stored pattern is
        evicted (FIFO).
        """
        pattern = np.asarray(pattern, dtype=float).reshape(-1)
        if pattern.shape[0] != self.n_neurons:
            raise ValueError(
                f"pattern has dimension {pattern.shape[0]}, "
                f"expected {self.n_neurons}"
            )
        if self.n_patterns >= self._max_patterns:
            self._patterns = self._patterns[1:]
            self._labels = self._labels[1:]
        self._patterns = np.vstack([self._patterns, pattern])
        self._labels.append(label if label is not None else f"pattern_{self.n_patterns - 1}")
        return self.n_patterns - 1

    def retrieve(
        self,
        query,
        n_iters: Optional[int] = None,
        beta: Optional[float] = None,
    ) -> np.ndarray:
        """Run the Modern Hopfield update ``xi <- X^T softmax(beta X xi)``.

        Returns the retrieved (continuous) state, shape ``[n_neurons]``.
        If no patterns are stored, returns the query unchanged.
        """
        query = np.asarray(query, dtype=float).reshape(-1)
        if query.shape[0] != self.n_neurons:
            raise ValueError(
                f"query has dimension {query.shape[0]}, expected {self.n_neurons}"
            )
        if self.n_patterns == 0:
            self._last_retrieval_index = None
            self._last_confidence = 0.0
            return query.copy()

        beta = self._effective_beta() if beta is None else beta
        n_iters = self._n_iters if n_iters is None else max(1, n_iters)

        state = query.copy()
        weights = None
        for _ in range(n_iters):
            scores = beta * (self._patterns @ state)
            weights = _softmax(scores)
            state = weights @ self._patterns

        self._last_retrieval_index = int(np.argmax(weights))
        self._last_confidence = float(weights.max())
        return state

    def _effective_beta(self) -> float:
        return self._beta * self._last_signal.dopamine

    def _project_cue(self, spike_trains: np.ndarray) -> np.ndarray:
        spike_trains = np.asarray(spike_trains, dtype=float)
        if spike_trains.size == 0:
            return np.zeros(self.n_neurons)
        if spike_trains.size == self.n_neurons:
            cue = spike_trains
        else:
            reps = int(np.ceil(self.n_neurons / spike_trains.size))
            cue = np.tile(spike_trains, reps)[: self.n_neurons]
        # Map binary {0, 1} spikes to bipolar {-1, +1} for Hopfield retrieval.
        return np.where(cue > 0, 1.0, -1.0)

    # -- CognitiveModule contract --------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        cue = self._project_cue(inputs.spike_trains)
        self._state = self.retrieve(cue)
        self._timestamp_ms = inputs.timestamp_ms

        spikes = (self._state > 0).astype(float)
        firing_rate = ((self._state + 1.0) / 2.0) * self._max_rate_hz

        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=firing_rate,
            internal_state={
                "retrieved_pattern_index": self._last_retrieval_index,
                "retrieval_confidence": self._last_confidence,
                "n_patterns": self.n_patterns,
            },
        )

    def get_state(self) -> ModuleState:
        normalized = (self._state + 1.0) / 2.0
        weight_matrix = self._patterns.T if self.n_patterns else np.zeros((self.n_neurons, 0))
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=-70.0 + 40.0 * normalized,
            firing_rate=normalized * self._max_rate_hz,
            mean_weight=float(weight_matrix.mean()) if weight_matrix.size else 0.0,
            active_synapses=int(weight_matrix.size),
            timestamp_ms=self._timestamp_ms,
            metadata={
                "n_patterns": self.n_patterns,
                "retrieved_pattern_index": self._last_retrieval_index,
                "retrieval_confidence": self._last_confidence,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        self._last_signal = signal

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        weight_matrix = self._patterns.T if self.n_patterns else np.zeros((self.n_neurons, 0))
        return [
            SynapticTarget(
                source_module=self.module_id,
                target_module=self.module_id,
                weight_matrix=weight_matrix,
                synapse_type="excitatory",
            )
        ]

    def reset(self) -> None:
        self._patterns = np.zeros((0, self.n_neurons))
        self._labels = []
        self._state = np.zeros(self.n_neurons)
        self._last_retrieval_index = None
        self._last_confidence = 0.0
        self._last_signal = NeuromodulationSignal()
        self._timestamp_ms = 0.0
