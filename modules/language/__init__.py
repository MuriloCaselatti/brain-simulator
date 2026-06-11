"""Brain Simulator -- Language module (SPEC-011).

Claude API as the brain's language region, plus the semantic<->spike codec.
"""
from modules.language.claude_module import (
    AnthropicClient,
    ClaudeClient,
    ClaudeModule,
    MockClaudeClient,
    ResponseCache,
)
from modules.language.encoder import SpikeCodec

__all__ = [
    "ClaudeModule",
    "ClaudeClient",
    "AnthropicClient",
    "MockClaudeClient",
    "ResponseCache",
    "SpikeCodec",
]
