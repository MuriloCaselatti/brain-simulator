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
from core.brain_bus import BrainBus, BusEvent, BusSnapshot
from core.simulation_engine import SimulationEngine

__all__ = [
    "INTERFACE_VERSION",
    "CognitiveModule",
    "ModuleInputs",
    "ModuleOutputs",
    "ModuleState",
    "NeuromodulationSignal",
    "SynapticTarget",
    "BrainBus",
    "BusEvent",
    "BusSnapshot",
    "SimulationEngine",
]
