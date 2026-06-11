"""Tests for SPEC-011 -- Language module (Claude API + spike codec).

Covers the frozen SPEC-001 :class:`~core.interfaces.CognitiveModule` contract,
the bidirectional semantic<->spike codec, activation gating, response caching,
neuromodulatory gating, and the offline mock backend (no API key required).
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
from modules.language.claude_module import (  # noqa: E402
    AnthropicClient,
    ClaudeModule,
    MockClaudeClient,
    ResponseCache,
)
from modules.language.encoder import SpikeCodec  # noqa: E402


def _inputs(spike_trains, attention_signal=1.0, neuromodulation=None, timestamp_ms=0.0):
    return ModuleInputs(
        spike_trains=np.asarray(spike_trains, dtype=float),
        attention_signal=attention_signal,
        neuromodulation=neuromodulation or NeuromodulationSignal(),
        timestamp_ms=timestamp_ms,
    )


def _strong_cue(n):
    """A high-contrast cue that comfortably crosses the activation threshold."""
    cue = np.zeros(n)
    cue[: n // 2] = 1.0  # mean activation ~0.5, well above default threshold
    return cue


# --- CognitiveModule contract conformance -----------------------------------


def test_module_implements_cognitive_module_contract():
    module = ClaudeModule(n_neurons=64)
    assert isinstance(module, CognitiveModule)
    assert isinstance(module.module_id, str)
    assert isinstance(module.n_neurons, int)

    state = module.get_state()
    assert isinstance(state, ModuleState)
    assert state.n_neurons == module.n_neurons
    assert state.voltage.shape == (module.n_neurons,)
    assert state.firing_rate.shape == (module.n_neurons,)
    assert isinstance(state.mean_weight, float)

    out = module.update(1.0, _inputs(_strong_cue(64)))
    assert isinstance(out, ModuleOutputs)
    assert out.spike_trains.shape == (64,)
    assert out.firing_rate.shape == (64,)

    assert module.get_synaptic_targets() == []
    module.apply_neuromodulation(NeuromodulationSignal())
    module.reset()


def test_get_synaptic_targets_is_empty():
    # The language region exposes no plastic synapses (external API).
    assert ClaudeModule().get_synaptic_targets() == []


# --- Mock backend: no API key required --------------------------------------


def test_mock_requires_no_api_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    module = ClaudeModule(n_neurons=32)  # defaults to MockClaudeClient
    out = module.update(1.0, _inputs(_strong_cue(32)))
    assert out.internal_state["activated"] is True
    assert out.internal_state["last_response"]


def test_mock_is_deterministic():
    client = MockClaudeClient()
    assert client.complete("hello") == client.complete("hello")
    assert client.complete("hello") != client.complete("world")


def test_scripted_mock_responses():
    client = MockClaudeClient(responses={"PROMPT": "scripted reply"})
    assert client.complete("PROMPT") == "scripted reply"


# --- Activation gating -------------------------------------------------------


def test_activates_on_strong_cue_calls_api():
    client = MockClaudeClient()
    module = ClaudeModule(n_neurons=64, client=client)
    out = module.update(1.0, _inputs(_strong_cue(64)))
    assert out.internal_state["activated"] is True
    assert client.call_count == 1


def test_silent_on_empty_cue():
    client = MockClaudeClient()
    module = ClaudeModule(n_neurons=64, client=client)
    out = module.update(1.0, _inputs(np.zeros(64)))
    assert out.internal_state["activated"] is False
    assert client.call_count == 0


def test_min_call_interval_throttles_calls():
    client = MockClaudeClient()
    module = ClaudeModule(
        n_neurons=64, client=client, min_call_interval_ms=50.0
    )
    # A second, distinct strong cue so the prompt differs (no cache masking).
    other = np.zeros(64)
    other[32:] = 1.0
    module.update(1.0, _inputs(_strong_cue(64), timestamp_ms=0.0))
    # 10ms later: strong cue again, but too soon -> must not call.
    out = module.update(1.0, _inputs(other, timestamp_ms=10.0))
    assert out.internal_state["activated"] is False
    assert client.call_count == 1
    # 60ms later: interval elapsed, may call again.
    module.update(1.0, _inputs(other, timestamp_ms=60.0))
    assert client.call_count == 2


# --- Response caching --------------------------------------------------------


def test_repeated_state_uses_cache_not_api():
    client = MockClaudeClient()
    module = ClaudeModule(n_neurons=64, client=client, min_call_interval_ms=0.0)
    module.set_context("dog cat tree")
    cue = _strong_cue(64)
    module.update(1.0, _inputs(cue, timestamp_ms=0.0))
    module.update(1.0, _inputs(cue, timestamp_ms=100.0))
    module.update(1.0, _inputs(cue, timestamp_ms=200.0))
    # Same context -> same prompt -> only one real API call.
    assert client.call_count == 1
    assert module.cache.hits >= 2


def test_response_cache_lru_eviction():
    cache = ResponseCache(max_size=2)
    cache.put("a", "1")
    cache.put("b", "2")
    cache.get("a")  # 'a' now most-recent
    cache.put("c", "3")  # evicts least-recent ('b')
    assert cache.get("b") is None
    assert cache.get("a") == "1"
    assert cache.get("c") == "3"


# --- Bidirectional encoding --------------------------------------------------


def test_semantic_memory_vector_to_spikes_roundtrip():
    codec = SpikeCodec(n_neurons=128, embedding_dim=384)
    vec = np.random.default_rng(0).standard_normal(384)
    spikes, rate = codec.vector_to_spikes(vec)
    assert spikes.shape == (128,)
    assert set(np.unique(spikes)).issubset({0.0, 1.0})
    assert rate.max() <= codec.max_rate_hz + 1e-9
    back = codec.spikes_to_vector(rate)
    assert back.shape == (384,)


def test_encode_text_is_deterministic_and_spiking():
    codec = SpikeCodec(n_neurons=64)
    s1, r1 = codec.encode_text("a thought about rivers")
    s2, r2 = codec.encode_text("a thought about rivers")
    assert np.array_equal(s1, s2)
    assert np.array_equal(r1, r2)
    assert s1.shape == (64,)


def test_module_receives_semantic_vector_and_returns_encoding():
    # SPEC-011: receives a semantic vector, returns a spike encoding.
    module = ClaudeModule(n_neurons=96)
    semantic_vector = SpikeCodec(n_neurons=96).vector_to_spikes(
        np.random.default_rng(1).standard_normal(384)
    )[0]
    out = module.update(1.0, _inputs(semantic_vector))
    assert out.spike_trains.shape == (96,)
    assert out.firing_rate.shape == (96,)


# --- Neuromodulation ---------------------------------------------------------


def test_acetylcholine_lowers_activation_threshold():
    # ACh above basal makes the region verbalise on a weaker cue.
    weak = np.zeros(64)
    weak[0] = 1.0  # very sparse -> low mean activation
    base = ClaudeModule(n_neurons=64, activation_threshold=0.3)
    assert base.update(1.0, _inputs(weak)).internal_state["activated"] is False

    primed = ClaudeModule(n_neurons=64, activation_threshold=0.3)
    primed.apply_neuromodulation(NeuromodulationSignal(acetylcholine=2.0))
    # Not asserting it must fire (depends on cue), just that the bar dropped.
    assert primed._effective_threshold() < base._effective_threshold()


# --- Reset -------------------------------------------------------------------


def test_reset_clears_state_and_cache():
    client = MockClaudeClient()
    module = ClaudeModule(n_neurons=64, client=client)
    module.update(1.0, _inputs(_strong_cue(64)))
    assert len(module.cache) >= 1
    module.reset()
    assert len(module.cache) == 0
    assert module.get_state().metadata["api_calls"] == 0
    assert np.count_nonzero(module._last_firing_rate) == 0


# --- Real backend guard rails (no network) -----------------------------------


def test_anthropic_client_raises_without_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="ANTHROPIC_API_KEY"):
        AnthropicClient()


# --- Engine integration ------------------------------------------------------


def test_integrates_with_simulation_engine():
    from core.simulation_engine import SimulationEngine

    engine = SimulationEngine()
    module = ClaudeModule(n_neurons=32)
    engine.add_module(module)
    engine.step()
    history = engine.get_history(1)
    assert history
