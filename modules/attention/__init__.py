"""Brain Simulator -- Attention modules (SPEC-005).

Exposes :class:`~modules.attention.dan.DAN`,
:class:`~modules.attention.van.VAN` and
:class:`~modules.attention.saliency.SaliencyMap`, all conforming to the
frozen SPEC-001 :class:`~core.interfaces.CognitiveModule` contract.
"""
from modules.attention.dan import DAN
from modules.attention.saliency import SaliencyMap
from modules.attention.van import VAN

__all__ = ["DAN", "VAN", "SaliencyMap"]
