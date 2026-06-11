"""Brain Simulator core package.

Exposes the frozen SPEC-001 contract (see :mod:`core.interfaces`).
"""
from core.interfaces import (
    INTERFACE_VERSION,
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)

__all__ = [
    "INTERFACE_VERSION",
    "CognitiveModule",
    "ModuleInputs",
    "ModuleOutputs",
    "ModuleState",
    "NeuromodulationSignal",
    "SynapticTarget",
]
