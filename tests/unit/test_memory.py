"""Tests for SPEC-004 -- Memory modules.

WorkingMemory (discrete attractor network), EpisodicMemory (Modern
Hopfield Network, Ramsauer et al. 2020) and SemanticMemory (embeddings +
NetworkX graph) all implement the frozen SPEC-001
:class:`~core.interfaces.CognitiveModule` contract.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.interfaces import (  # noqa: E402
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)
from modules.memory.episodic import EpisodicMemory  # noqa: E402
from modules.memory.semantic import SemanticMemory  # noqa: E402
from modules.memory.working import WorkingMemory  # noqa: E402


def _inputs(spike_trains, attention_signal=1.0, neuromodulation=None, timestamp_ms=0.0):
    return ModuleInputs(
        spike_trains=np.asarray(spike_trains, dtype=float),
        attention_signal=attention_signal,
        neuromodulation=neuromodulation or NeuromodulationSignal(),
        timestamp_ms=timestamp_ms,
    )


# --- CognitiveModule contract conformance -----------------------------------


@pytest.mark.parametrize(
    "module",
    [
        WorkingMemory(),
        EpisodicMemory(),
        SemanticMemory(model_name=None),
    ],
    ids=["WorkingMemory", "EpisodicMemory", "SemanticMemory"],
)
def test_module_implements_cognitive_module_contract(module):
    assert isinstance(module, CognitiveModule)
    assert isinstance(module.module_id, str)
    assert isinstance(module.n_neurons, int)

    state = module.get_state()
    assert isinstance(state, ModuleState)
    assert state.n_neurons == module.n_neurons
    assert state.voltage.shape == (module.n_neurons,)
    assert state.firing_rate.shape == (module.n_neurons,)
    assert isinstance(state.mean_weight, float)
    assert isinstance(state.active_synapses, int)

    outputs = module.update(dt=1.0, inputs=_inputs(np.zeros(module.n_neurons)))
    assert isinstance(outputs, ModuleOutputs)
    assert outputs.spike_trains.shape == (module.n_neurons,)
    assert outputs.firing_rate.shape == (module.n_neurons,)
    assert isinstance(outputs.internal_state, dict)

    targets = module.get_synaptic_targets()
    assert isinstance(targets, list)
    assert all(isinstance(t, SynapticTarget) for t in targets)

    module.apply_neuromodulation(NeuromodulationSignal(dopamine=1.5))
    module.reset()


# --- WorkingMemory: ~7-attractor persistent activity -------------------------


class TestWorkingMemory:
    def test_n_attractors_is_seven(self):
        wm = WorkingMemory(n_neurons=70)
        assert wm.N_ATTRACTORS == 7
        assert wm._patterns.shape == (7, 70)

    def test_persists_pattern_for_500ms_without_input(self):
        wm = WorkingMemory(n_neurons=70)

        # Cue strongly overlapping attractor pool 3 (neurons 30:40).
        cue = np.zeros(70)
        cue[30:40] = 1.0

        for _ in range(50):
            outputs = wm.update(dt=1.0, inputs=_inputs(cue))

        assert outputs.internal_state["active_attractor"] == 3
        assert outputs.internal_state["level"] > 0.5

        # Remove all input for 500ms.
        zero_cue = np.zeros(70)
        for _ in range(500):
            outputs = wm.update(dt=1.0, inputs=_inputs(zero_cue))

        assert outputs.internal_state["active_attractor"] == 3
        assert outputs.internal_state["level"] > 0.5
        assert np.all(outputs.spike_trains[30:40] == 1.0)
        assert np.all(outputs.spike_trains[:30] == 0.0)
        assert np.all(outputs.spike_trains[40:] == 0.0)

    def test_no_persistent_activity_without_stimulus(self):
        wm = WorkingMemory(n_neurons=70)

        outputs = None
        for _ in range(500):
            outputs = wm.update(dt=1.0, inputs=_inputs(np.zeros(70)))

        assert outputs.internal_state["active_attractor"] is None
        assert outputs.internal_state["level"] < 0.5
        assert np.all(outputs.spike_trains == 0.0)

    def test_reset_clears_active_attractor(self):
        wm = WorkingMemory(n_neurons=70)
        cue = np.zeros(70)
        cue[:10] = 1.0
        for _ in range(50):
            wm.update(dt=1.0, inputs=_inputs(cue))

        wm.reset()

        state = wm.get_state()
        assert state.metadata["active_attractor"] is None
        assert state.metadata["level"] < 0.5


# --- EpisodicMemory: Modern Hopfield Network ----------------------------------


class TestEpisodicMemory:
    def test_retrieves_pattern_with_30_percent_noise(self):
        rng = np.random.default_rng(0)
        em = EpisodicMemory(n_neurons=100, beta=8.0)

        patterns = rng.choice([-1.0, 1.0], size=(5, 100)).astype(float)
        for i, pattern in enumerate(patterns):
            em.store_pattern(pattern, label=f"episode_{i}")

        target_idx = 2
        target = patterns[target_idx]
        noisy = target.copy()
        flip_idx = rng.choice(100, size=30, replace=False)
        noisy[flip_idx] *= -1

        retrieved = em.retrieve(noisy)
        recovered = np.sign(retrieved)
        recovered[recovered == 0] = 1.0

        assert np.array_equal(recovered, target)
        assert em._last_retrieval_index == target_idx

    def test_update_returns_spike_trains_for_retrieved_pattern(self):
        em = EpisodicMemory(n_neurons=20, beta=8.0)
        pattern = np.ones(20)
        pattern[10:] = -1.0
        em.store_pattern(pattern)

        noisy = pattern.copy()
        noisy[:6] *= -1  # 30% noise on a 20-d pattern

        cue_spikes = (noisy > 0).astype(float)
        outputs = em.update(dt=1.0, inputs=_inputs(cue_spikes))

        expected_spikes = (pattern > 0).astype(float)
        assert np.array_equal(outputs.spike_trains, expected_spikes)
        assert outputs.internal_state["n_patterns"] == 1
        assert outputs.internal_state["retrieved_pattern_index"] == 0

    def test_empty_memory_returns_query_unchanged(self):
        em = EpisodicMemory(n_neurons=10)
        query = np.ones(10)

        retrieved = em.retrieve(query)

        assert np.array_equal(retrieved, query)
        assert em._last_retrieval_index is None

    def test_max_patterns_evicts_oldest_fifo(self):
        em = EpisodicMemory(n_neurons=10, max_patterns=2)
        em.store_pattern(np.ones(10), label="a")
        em.store_pattern(-np.ones(10), label="b")
        em.store_pattern(np.ones(10), label="c")

        assert em.n_patterns == 2
        assert em._labels == ["b", "c"]

    def test_reset_clears_stored_patterns(self):
        em = EpisodicMemory(n_neurons=10)
        em.store_pattern(np.ones(10))

        em.reset()

        assert em.n_patterns == 0
        retrieved = em.retrieve(np.ones(10))
        assert np.array_equal(retrieved, np.ones(10))


# --- SemanticMemory: embeddings + NetworkX graph ------------------------------


class TestSemanticMemory:
    @pytest.fixture(scope="class")
    def memory(self):
        sm = SemanticMemory(n_neurons=16)
        concepts = {
            "cat": "a small domesticated carnivorous mammal",
            "kitten": "a young cat",
            "dog": "a domesticated canine companion animal",
            "puppy": "a young dog",
            "lion": "a large wild cat found in africa",
            "car": "a road vehicle with an engine",
            "automobile": "a motor vehicle for transportation",
            "bicycle": "a pedal-powered two-wheeled vehicle",
            "banana": "a long curved tropical fruit",
            "apple": "a round fruit with red or green skin",
        }
        for name, text in concepts.items():
            sm.add_concept(name, text=text)
        sm.add_relation("cat", "kitten", relation_type="is_a")
        sm.add_relation("dog", "puppy", relation_type="is_a")
        return sm

    def test_query_top5_returns_semantically_related_concepts(self, memory):
        results = memory.query("cat", top_k=5)
        names = [name for name, _ in results]

        assert len(results) == 5
        # Similarities must be sorted descending.
        scores = [score for _, score in results]
        assert scores == sorted(scores, reverse=True)

        animal_names = {"cat", "kitten", "dog", "puppy", "lion"}
        assert sum(1 for n in names if n in animal_names) >= 4

    def test_query_ranks_self_highest_for_close_match(self, memory):
        results = memory.query("automobile", top_k=1)
        assert results[0][0] == "automobile"

    def test_relations_are_queryable(self, memory):
        neighbors = memory.neighbors("cat")
        assert ("kitten", 1.0, "is_a") in neighbors

    def test_synaptic_targets_reflect_relations(self, memory):
        targets = memory.get_synaptic_targets()

        assert len(targets) == 1
        weight_matrix = targets[0].weight_matrix
        assert weight_matrix.shape == (memory.n_neurons, memory.n_neurons)
        assert np.count_nonzero(weight_matrix) > 0

    def test_add_concept_with_explicit_embedding(self):
        sm = SemanticMemory(n_neurons=8, embedding_dim=4, model_name=None)
        sm.add_concept("a", embedding=np.array([1.0, 0.0, 0.0, 0.0]))
        sm.add_concept("b", embedding=np.array([0.0, 1.0, 0.0, 0.0]))
        sm.add_concept("c", embedding=np.array([1.0, 0.0, 0.0, 0.0]))

        results = sm.query(np.array([1.0, 0.0, 0.0, 0.0]), top_k=2)
        names = [name for name, _ in results]

        assert names[0] in ("a", "c")
        assert set(names) == {"a", "c"}

    def test_reset_clears_concepts(self):
        sm = SemanticMemory(n_neurons=8, embedding_dim=4, model_name=None)
        sm.add_concept("x", text="x")

        sm.reset()

        assert sm.n_concepts == 0
        assert sm.query("x") == []
