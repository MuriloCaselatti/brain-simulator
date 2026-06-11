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
from core.neuron import LIFPopulation
from core.synapse import STDPSynapse
from core.learning_engine import LearningEngine, PlasticityScheduler

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
    "LIFPopulation",
    "STDPSynapse",
    "LearningEngine",
    "PlasticityScheduler",
]
