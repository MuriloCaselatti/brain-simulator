"""Brain Simulator -- Semantic <-> Spike Encoding (SPEC-011).

Bidirectional codec bridging the continuous *semantic* world (dense
embedding vectors, free text) and the discrete *spiking* world the
:class:`~core.brain_bus.BrainBus` exchanges between modules.

Two conversions, each its own inverse-ish counterpart:

    * ``vector_to_spikes`` / ``spikes_to_vector`` -- rate-code a dense
      semantic vector into an ``n_neurons`` binary spike mask (plus the
      per-neuron firing rates), and read a spike/rate pattern back into a
      vector of the original embedding dimensionality.
    * ``encode_text`` / ``decode...`` -- text is embedded (via an injected
      ``embed_fn`` -- e.g. ``SemanticMemory.embed`` -- or a dependency-free
      hashing fallback) and then rate-coded with ``vector_to_spikes``.

The codec is **deterministic**: the same vector/text always yields the same
spike pattern, so caching and reproducible tests work. It is pure NumPy +
stdlib (no Brian2, torch, or network access required) -- the heavy embedding
backend is optional and injected, never imported here.
"""
from __future__ import annotations

import hashlib
from typing import Callable, Optional

import numpy as np

__all__ = ["SpikeCodec"]


def _hashing_embedding(text: str, dim: int) -> np.ndarray:
    """Deterministic, dependency-free fallback embedding.

    Mirrors ``SemanticMemory``'s fallback: hashes each whitespace token into
    a signed bucket of a ``dim``-dimensional vector and L2-normalizes, so
    texts sharing tokens land closer in cosine similarity. Used only when no
    ``embed_fn`` is supplied (offline / no sentence-transformers).
    """
    vector = np.zeros(dim, dtype=float)
    for token in text.lower().split():
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        idx = int.from_bytes(digest[:4], "little") % dim
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        vector[idx] += sign
    norm = np.linalg.norm(vector)
    return vector / norm if norm > 0 else vector


class SpikeCodec:
    """Rate-coding codec between semantic vectors/text and spike patterns.

    Args:
        n_neurons: Width of the spike pattern produced/consumed (the number
            of "language neurons").
        embedding_dim: Dimensionality of semantic vectors handled by
            :meth:`embed_text` (fallback) and reconstructed by
            :meth:`spikes_to_vector`.
        embed_fn: Optional ``text -> np.ndarray`` embedding function (e.g.
            ``SemanticMemory.embed``). When ``None``, a deterministic hashing
            embedding is used so the codec is fully offline.
        max_rate_hz: Firing rate mapped to a fully-saturated neuron
            (normalized activation of ``1.0``).
        spike_threshold: Normalized-activation level (in ``[0, 1]``) above
            which a neuron emits a spike in the binary mask.
    """

    def __init__(
        self,
        n_neurons: int = 128,
        embedding_dim: int = 384,
        embed_fn: Optional[Callable[[str], np.ndarray]] = None,
        max_rate_hz: float = 50.0,
        spike_threshold: float = 0.5,
    ) -> None:
        self.n_neurons = int(n_neurons)
        self.embedding_dim = int(embedding_dim)
        self._embed_fn = embed_fn
        self.max_rate_hz = float(max_rate_hz)
        self.spike_threshold = float(spike_threshold)

    # -- embedding ------------------------------------------------------------

    def embed_text(self, text: str) -> np.ndarray:
        """Encode ``text`` to a dense vector via ``embed_fn`` or the fallback."""
        if self._embed_fn is not None:
            vector = np.asarray(self._embed_fn(text), dtype=float).reshape(-1)
            if vector.size:
                self.embedding_dim = vector.shape[0]
            return vector
        return _hashing_embedding(text, self.embedding_dim)

    # -- vector <-> spikes ----------------------------------------------------

    @staticmethod
    def _normalize(vector: np.ndarray) -> np.ndarray:
        """Map an arbitrary real vector into ``[0, 1]`` per element.

        Min-max scaling preserves the relative structure of the embedding
        while giving a bounded activation suitable for rate coding. A constant
        vector maps to all-zeros (no spurious activity).
        """
        if vector.size == 0:
            return vector
        lo = float(np.min(vector))
        hi = float(np.max(vector))
        if hi - lo <= 1e-12:
            return np.zeros_like(vector)
        return (vector - lo) / (hi - lo)

    def _project(self, vector: np.ndarray, size: int) -> np.ndarray:
        """Tile/truncate ``vector`` to exactly ``size`` elements."""
        vector = np.asarray(vector, dtype=float).reshape(-1)
        if vector.size == 0:
            return np.zeros(size)
        if vector.size == size:
            return vector
        reps = int(np.ceil(size / vector.size))
        return np.tile(vector, reps)[:size]

    def vector_to_spikes(self, vector: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Rate-code a semantic vector into ``(spikes, firing_rate)``.

        ``spikes`` is a binary mask of shape ``[n_neurons]``; ``firing_rate``
        is the per-neuron rate in Hz (normalized activation x ``max_rate_hz``).
        """
        activation = self._normalize(self._project(vector, self.n_neurons))
        spikes = (activation > self.spike_threshold).astype(float)
        firing_rate = activation * self.max_rate_hz
        return spikes, firing_rate

    def spikes_to_vector(self, pattern: np.ndarray) -> np.ndarray:
        """Read a spike/rate pattern back into an ``embedding_dim`` vector.

        Accepts either a binary spike mask or a firing-rate vector; rates are
        scaled back to ``[0, 1]`` and the pattern is projected to the embedding
        dimensionality. The inverse is approximate (rate coding discards sign
        and exact magnitude), but preserves the activation profile.
        """
        pattern = np.asarray(pattern, dtype=float).reshape(-1)
        if pattern.size == 0:
            return np.zeros(self.embedding_dim)
        peak = float(np.max(pattern))
        if peak > 1.0:  # looks like firing rates, not a 0/1 mask
            pattern = pattern / self.max_rate_hz
        return self._project(pattern, self.embedding_dim)

    # -- text -> spikes -------------------------------------------------------

    def encode_text(self, text: str) -> tuple[np.ndarray, np.ndarray]:
        """Embed ``text`` and rate-code it into ``(spikes, firing_rate)``."""
        return self.vector_to_spikes(self.embed_text(text))
