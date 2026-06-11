"""Brain Simulator memory modules (SPEC-004).

Exposes :class:`WorkingMemory`, :class:`EpisodicMemory` and
:class:`SemanticMemory`, all implementing the frozen
:class:`~core.interfaces.CognitiveModule` contract (SPEC-001).
"""
from modules.memory.episodic import EpisodicMemory
from modules.memory.semantic import SemanticMemory
from modules.memory.working import WorkingMemory

__all__ = ["WorkingMemory", "EpisodicMemory", "SemanticMemory"]
