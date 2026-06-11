"""Brain Simulator -- Semantic Memory Module (SPEC-004).

Implements a semantic memory store: a graph of concepts (NetworkX) where
each node carries a dense embedding vector. Two concepts are "related" if
an edge connects them (explicit relations) and/or if their embeddings are
close in cosine similarity (similarity-based recall via :meth:`query`).

Embedding backend
------------------
Embeddings are produced by a ``sentence-transformers`` model
(``all-MiniLM-L6-v2`` by default) when the package and model weights are
available. On constrained/offline hardware where the model cannot be
loaded (e.g. no network on first run), :meth:`embed` transparently falls
back to a deterministic hashing-based embedding so the module remains
fully functional, dependency-free and reproducible. Loaded models are
cached at module scope so multiple instances share one copy.

Implements :class:`~core.interfaces.CognitiveModule` (SPEC-001, frozen).
"""
from __future__ import annotations

import hashlib
from typing import Any, Dict, List, Optional, Tuple, Union

import networkx as nx
import numpy as np

from core.interfaces import (
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)

__all__ = ["SemanticMemory"]

# Module-scope cache so the (potentially expensive) sentence-transformers
# model is loaded at most once per process, shared across instances.
_MODEL_CACHE: Dict[str, Any] = {}


def _hashing_embedding(text: str, dim: int) -> np.ndarray:
    """Deterministic, dependency-free fallback embedding.

    Hashes each whitespace-separated token into a signed bucket of a
    ``dim``-dimensional vector and L2-normalizes the result. Texts that
    share tokens land closer together in cosine similarity.
    """
    vector = np.zeros(dim, dtype=float)
    for token in text.lower().split():
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        idx = int.from_bytes(digest[:4], "little") % dim
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        vector[idx] += sign
    norm = np.linalg.norm(vector)
    return vector / norm if norm > 0 else vector


def _cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0.0:
        return 0.0
    return float(np.dot(a, b) / denom)


class SemanticMemory(CognitiveModule):
    """Concept graph with embedding-based similarity search.

    Args:
        module_id: Stable identifier for this module instance.
        n_neurons: Number of "concept-neuron" output slots. Concepts are
            mapped to slots in insertion order; :meth:`query` itself
            searches the *entire* graph regardless of ``n_neurons``.
        embedding_dim: Dimensionality used by the fallback hashing
            embedding, and the expected dimensionality of externally
            supplied embeddings/cues. Updated automatically to match the
            sentence-transformers model's output dimension once it is
            loaded.
        model_name: ``sentence-transformers`` model identifier, or
            ``None`` to always use the hashing fallback.
        max_rate_hz: Firing rate corresponding to a cosine similarity of
            ``1.0``.
    """

    DEFAULT_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(
        self,
        module_id: str = "semantic_memory",
        n_neurons: int = 256,
        embedding_dim: int = 384,
        model_name: Optional[str] = DEFAULT_MODEL_NAME,
        max_rate_hz: float = 50.0,
    ) -> None:
        super().__init__(module_id, n_neurons)
        self._embedding_dim = embedding_dim
        self._model_name = model_name
        self._max_rate_hz = max_rate_hz

        self._graph = nx.Graph()
        self._order: List[str] = []  # insertion order -> output slot mapping
        self._last_activation = np.zeros(n_neurons)
        self._last_top_matches: List[str] = []
        self._last_signal = NeuromodulationSignal()
        self._timestamp_ms = 0.0

    # -- embedding backend ----------------------------------------------------

    def _get_model(self):
        if self._model_name is None:
            return None
        if self._model_name not in _MODEL_CACHE:
            try:
                from sentence_transformers import SentenceTransformer

                _MODEL_CACHE[self._model_name] = SentenceTransformer(self._model_name)
            except Exception:
                _MODEL_CACHE[self._model_name] = None
        return _MODEL_CACHE[self._model_name]

    def embed(self, text: str) -> np.ndarray:
        """Encode ``text`` into a dense vector.

        Uses the cached sentence-transformers model when available,
        otherwise the deterministic hashing fallback (see module
        docstring).
        """
        model = self._get_model()
        if model is not None:
            vector = np.asarray(model.encode(text), dtype=float).reshape(-1)
            self._embedding_dim = vector.shape[0]
            return vector
        return _hashing_embedding(text, self._embedding_dim)

    # -- concept graph API ------------------------------------------------------

    def add_concept(
        self,
        name: str,
        text: Optional[str] = None,
        embedding: Optional[np.ndarray] = None,
        **attrs: Any,
    ) -> np.ndarray:
        """Add (or update) a concept node, returning its embedding.

        If ``embedding`` is not given, it is computed via :meth:`embed`
        from ``text`` (defaulting to ``name`` itself).
        """
        if embedding is None:
            embedding = self.embed(text if text is not None else name)
        embedding = np.asarray(embedding, dtype=float).reshape(-1)

        is_new = name not in self._graph
        self._graph.add_node(name, embedding=embedding, text=text, **attrs)
        if is_new:
            self._order.append(name)
        return embedding

    def add_relation(
        self,
        source: str,
        target: str,
        weight: float = 1.0,
        relation_type: str = "related_to",
    ) -> None:
        """Add a typed, weighted edge between two existing concepts."""
        if source not in self._graph or target not in self._graph:
            raise ValueError("both concepts must be added before relating them")
        self._graph.add_edge(source, target, weight=weight, relation_type=relation_type)

    def query(
        self, query: Union[str, np.ndarray], top_k: int = 5
    ) -> List[Tuple[str, float]]:
        """Return the ``top_k`` concepts most similar to ``query``.

        ``query`` may be free text (embedded via :meth:`embed`) or a
        precomputed embedding vector. Results are ``(concept_name,
        cosine_similarity)`` pairs sorted by descending similarity.
        """
        if isinstance(query, str):
            query_vec = self.embed(query)
        else:
            query_vec = np.asarray(query, dtype=float).reshape(-1)

        scored = [
            (name, _cosine_similarity(query_vec, self._graph.nodes[name]["embedding"]))
            for name in self._order
        ]
        scored.sort(key=lambda item: item[1], reverse=True)
        return scored[:top_k]

    def neighbors(self, name: str) -> List[Tuple[str, float, str]]:
        """Return ``(neighbor, weight, relation_type)`` for ``name``'s edges."""
        return [
            (other, data.get("weight", 1.0), data.get("relation_type", "related_to"))
            for other, data in self._graph.adj[name].items()
        ]

    @property
    def n_concepts(self) -> int:
        return len(self._order)

    # -- CognitiveModule contract --------------------------------------------

    def _project_cue(self, cue: np.ndarray) -> np.ndarray:
        if cue.size == self._embedding_dim:
            return cue
        reps = int(np.ceil(self._embedding_dim / cue.size))
        return np.tile(cue, reps)[: self._embedding_dim]

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        cue = np.asarray(inputs.spike_trains, dtype=float)
        activation = np.zeros(self.n_neurons)
        top_matches: List[str] = []

        if self._order and cue.size:
            cue_vec = self._project_cue(cue)
            scored = self.query(cue_vec, top_k=min(5, len(self._order)))
            top_matches = [name for name, _ in scored]

            for slot, name in enumerate(self._order[: self.n_neurons]):
                activation[slot] = _cosine_similarity(
                    cue_vec, self._graph.nodes[name]["embedding"]
                )

        self._last_activation = activation
        self._last_top_matches = top_matches
        self._timestamp_ms = inputs.timestamp_ms

        spikes = (activation > 0.5).astype(float)
        firing_rate = np.clip(activation, 0.0, 1.0) * self._max_rate_hz

        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=firing_rate,
            internal_state={
                "n_concepts": self.n_concepts,
                "top_matches": top_matches,
            },
        )

    def get_state(self) -> ModuleState:
        clipped = np.clip(self._last_activation, 0.0, 1.0)
        edge_weights = [data.get("weight", 1.0) for _, _, data in self._graph.edges(data=True)]
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=-70.0 + 40.0 * clipped,
            firing_rate=clipped * self._max_rate_hz,
            mean_weight=float(np.mean(edge_weights)) if edge_weights else 0.0,
            active_synapses=self._graph.number_of_edges(),
            timestamp_ms=self._timestamp_ms,
            metadata={
                "n_concepts": self.n_concepts,
                "top_matches": self._last_top_matches,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        self._last_signal = signal

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        n = min(self.n_concepts, self.n_neurons)
        weight_matrix = np.zeros((self.n_neurons, self.n_neurons))
        slot = {name: i for i, name in enumerate(self._order[:n])}
        for u, v, data in self._graph.edges(data=True):
            if u in slot and v in slot:
                w = data.get("weight", 1.0)
                weight_matrix[slot[u], slot[v]] = w
                weight_matrix[slot[v], slot[u]] = w
        return [
            SynapticTarget(
                source_module=self.module_id,
                target_module=self.module_id,
                weight_matrix=weight_matrix,
                synapse_type="excitatory",
            )
        ]

    def reset(self) -> None:
        self._graph = nx.Graph()
        self._order = []
        self._last_activation = np.zeros(self.n_neurons)
        self._last_top_matches = []
        self._last_signal = NeuromodulationSignal()
        self._timestamp_ms = 0.0
