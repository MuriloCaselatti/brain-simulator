"""Brain Simulator -- Language Module via Claude API (SPEC-011).

Integrates Claude as the brain's *language* cognitive region. The module is
bidirectional: incoming spike patterns (a semantic state, typically from
``SemanticMemory``) are decoded to a prompt, sent to Claude, and the textual
response is re-encoded into a spike pattern published back to the BrainBus.

Activation model
----------------
Calling an LLM on every 1 ms timestep is neither biologically sensible nor
affordable, so :class:`ClaudeModule` *gates* its calls:

    * it only "verbalises" when the incoming activation crosses
      ``activation_threshold`` (acetylcholine lowers the effective
      threshold -- attention makes the region more readily engaged), and
    * a minimum wall of ``min_call_interval_ms`` of simulated time must pass
      between two distinct API calls.

Between activations the module decays toward quiescence. Identical prompts are
served from an LRU :class:`ResponseCache`, so a stable semantic state never
pays for a repeated call.

Security
--------
**No API key is ever stored in this module or the repository.** The real
backend (:class:`AnthropicClient`) resolves credentials exclusively from the
environment (``ANTHROPIC_API_KEY``), exactly as the official SDK does. The
default client is the offline :class:`MockClaudeClient`, so tests and CI need
neither a key nor network access; the real backend is opt-in.

Implements :class:`~core.interfaces.CognitiveModule` (SPEC-001, frozen).
"""
from __future__ import annotations

import hashlib
import os
from collections import OrderedDict
from typing import List, Optional, Protocol

import numpy as np

from core.interfaces import (
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)
from modules.language.encoder import SpikeCodec

__all__ = [
    "ClaudeClient",
    "AnthropicClient",
    "MockClaudeClient",
    "ResponseCache",
    "ClaudeModule",
]

# Pinned by SPEC-011. Do not append a date suffix.
DEFAULT_MODEL = "claude-sonnet-4-6"


class ClaudeClient(Protocol):
    """Minimal contract for a Claude text-completion backend.

    Any object exposing :meth:`complete` can drive :class:`ClaudeModule` --
    the real :class:`AnthropicClient`, the offline :class:`MockClaudeClient`,
    or a user-supplied fake.
    """

    def complete(self, prompt: str) -> str:
        """Return Claude's text response to ``prompt``."""
        ...


class MockClaudeClient:
    """Deterministic, offline stand-in for the Claude API.

    Requires no API key and no network. The response is a stable function of
    the prompt (so caching/tests are reproducible) yet prompt-dependent enough
    to exercise the full encode/decode path. Pass ``responses`` to script
    exact replies for specific prompts.
    """

    def __init__(self, responses: Optional[dict[str, str]] = None) -> None:
        self._responses = dict(responses or {})
        self.call_count = 0

    def complete(self, prompt: str) -> str:
        self.call_count += 1
        if prompt in self._responses:
            return self._responses[prompt]
        digest = hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:8]
        return f"[mock-claude:{digest}] response to: {prompt.strip()[:120]}"


class AnthropicClient:
    """Real Claude backend over the official ``anthropic`` SDK.

    The API key is read from the environment (``ANTHROPIC_API_KEY``) by the
    SDK -- it is never accepted as a constructor argument, hardcoded, or
    logged. The ``anthropic`` package is imported lazily so the module (and
    the mock path) work without it installed.

    Args:
        model: Claude model id (defaults to the SPEC-011-pinned Sonnet 4.6).
        max_tokens: Output cap per call.
        system: Optional system prompt framing the language region's role.
    """

    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        max_tokens: int = 1024,
        system: Optional[str] = None,
    ) -> None:
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set in the environment. Set it "
                "(e.g. via a gitignored .env) before using AnthropicClient, "
                "or use MockClaudeClient for offline/testing."
            )
        try:
            import anthropic
        except ImportError as exc:  # pragma: no cover - depends on env
            raise RuntimeError(
                "The 'anthropic' package is required for AnthropicClient. "
                "Install it with `pip install anthropic`, or use "
                "MockClaudeClient for offline/testing."
            ) from exc

        # SDK resolves ANTHROPIC_API_KEY from the environment itself.
        self._client = anthropic.Anthropic()
        self.model = model
        self.max_tokens = int(max_tokens)
        self.system = system

    def complete(self, prompt: str) -> str:  # pragma: no cover - needs network
        kwargs = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
        if self.system:
            kwargs["system"] = self.system
        response = self._client.messages.create(**kwargs)
        return "".join(
            block.text for block in response.content if block.type == "text"
        )


class ResponseCache:
    """Bounded LRU cache of ``prompt -> response`` to avoid repeat calls."""

    def __init__(self, max_size: int = 256) -> None:
        self.max_size = int(max_size)
        self._store: "OrderedDict[str, str]" = OrderedDict()
        self.hits = 0
        self.misses = 0

    def get(self, prompt: str) -> Optional[str]:
        if prompt in self._store:
            self._store.move_to_end(prompt)
            self.hits += 1
            return self._store[prompt]
        self.misses += 1
        return None

    def put(self, prompt: str, response: str) -> None:
        self._store[prompt] = response
        self._store.move_to_end(prompt)
        while len(self._store) > self.max_size:
            self._store.popitem(last=False)

    def clear(self) -> None:
        self._store.clear()
        self.hits = 0
        self.misses = 0

    def __len__(self) -> int:
        return len(self._store)


class ClaudeModule(CognitiveModule):
    """Language region backed by Claude (bidirectional spike <-> language).

    Args:
        module_id: Stable identifier for this module instance.
        n_neurons: Width of the spike interface (in/out).
        client: A :class:`ClaudeClient`. Defaults to :class:`MockClaudeClient`
            so no API key is needed. Pass :class:`AnthropicClient` for real
            calls.
        codec: Semantic<->spike codec. Defaults to a self-contained
            :class:`~modules.language.encoder.SpikeCodec`.
        activation_threshold: Mean incoming activation (in ``[0, 1]``) above
            which the module verbalises and calls Claude.
        min_call_interval_ms: Minimum simulated time between two API calls.
        cache_size: LRU capacity for the response cache.
        decay: Per-tick multiplicative decay of the output when not activated.
    """

    def __init__(
        self,
        module_id: str = "language",
        n_neurons: int = 128,
        client: Optional[ClaudeClient] = None,
        codec: Optional[SpikeCodec] = None,
        activation_threshold: float = 0.15,
        min_call_interval_ms: float = 50.0,
        cache_size: int = 256,
        decay: float = 0.8,
    ) -> None:
        super().__init__(module_id, n_neurons)
        self.client: ClaudeClient = client if client is not None else MockClaudeClient()
        self.codec = codec if codec is not None else SpikeCodec(n_neurons=n_neurons)
        self.base_activation_threshold = float(activation_threshold)
        self.min_call_interval_ms = float(min_call_interval_ms)
        self.cache = ResponseCache(max_size=cache_size)
        self.decay = float(decay)

        self._context: Optional[str] = None
        self._signal = NeuromodulationSignal()
        self.reset()

    # -- external wiring ------------------------------------------------------

    def set_context(self, text: Optional[str]) -> None:
        """Provide human-readable semantic context (e.g. active concepts).

        ``SemanticMemory.query`` returns concept *names*; join them and pass
        them here so the prompt describes the current semantic state in words
        rather than raw activations.
        """
        self._context = text

    # -- prompt assembly ------------------------------------------------------

    def _effective_threshold(self) -> float:
        """Acetylcholine (>1 basal) lowers the bar to verbalise."""
        ach = max(0.0, float(self._signal.acetylcholine))
        return self.base_activation_threshold / max(0.25, ach)

    def _build_prompt(self, activation: np.ndarray) -> str:
        """Compose a prompt from the current context and activation pattern."""
        top = int(np.argmax(activation)) if activation.size else 0
        level = float(np.mean(activation)) if activation.size else 0.0
        if self._context:
            return (
                "You are the language region of a brain simulator. The current "
                f"semantic state is: {self._context}. Respond with a short, "
                "natural-language thought it evokes."
            )
        return (
            "You are the language region of a brain simulator. A semantic "
            f"pattern is active (peak neuron {top}, mean activation "
            f"{level:.2f}). Respond with a short, natural-language thought."
        )

    # -- CognitiveModule contract --------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        self._timestamp_ms = inputs.timestamp_ms

        cue = np.asarray(inputs.spike_trains, dtype=float)
        activation = self.codec._normalize(self.codec._project(cue, self.n_neurons))
        mean_activation = float(np.mean(activation)) if activation.size else 0.0

        elapsed = self._timestamp_ms - self._last_call_ms
        ready = self._last_call_ms < 0.0 or elapsed >= self.min_call_interval_ms
        activated = mean_activation >= self._effective_threshold() and ready

        if activated:
            prompt = self._build_prompt(activation)
            response = self.cache.get(prompt)
            if response is None:
                response = self.client.complete(prompt)
                self.cache.put(prompt, response)
                self._api_calls += 1
            self._last_call_ms = self._timestamp_ms
            self._last_prompt = prompt
            self._last_response = response
            spikes, firing_rate = self.codec.encode_text(response)
        else:
            # Quiescent: decay the previous output toward silence.
            firing_rate = self._last_firing_rate * self.decay
            spikes = (firing_rate > self.codec.spike_threshold * self.codec.max_rate_hz).astype(
                float
            )

        self._last_spikes = spikes
        self._last_firing_rate = firing_rate
        self._last_activated = activated

        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=firing_rate,
            internal_state={
                "activated": activated,
                "mean_activation": mean_activation,
                "last_prompt": self._last_prompt,
                "last_response": self._last_response,
                "api_calls": self._api_calls,
                "cache_hits": self.cache.hits,
            },
        )

    def get_state(self) -> ModuleState:
        rate = np.asarray(self._last_firing_rate, dtype=float)
        norm = np.clip(rate / self.codec.max_rate_hz, 0.0, 1.0)
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=-70.0 + 40.0 * norm,
            firing_rate=rate,
            mean_weight=0.0,
            active_synapses=int(np.count_nonzero(self._last_spikes)),
            timestamp_ms=self._timestamp_ms,
            metadata={
                "activated": self._last_activated,
                "api_calls": self._api_calls,
                "cache_hits": self.cache.hits,
                "cache_size": len(self.cache),
                "last_response": self._last_response,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        self._signal = signal

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        # The language region interfaces an external API; it exposes no
        # plastic synapses for the LearningEngine (cf. PFCExecutive).
        return []

    def reset(self) -> None:
        self._timestamp_ms = 0.0
        self._last_call_ms = -1.0
        self._api_calls = 0
        self._last_prompt: Optional[str] = None
        self._last_response: Optional[str] = None
        self._last_activated = False
        self._last_spikes = np.zeros(self.n_neurons)
        self._last_firing_rate = np.zeros(self.n_neurons)
        self._signal = NeuromodulationSignal()
        self.cache.clear()
