"""Brain Simulator -- Core Interfaces and Data Contracts.

This module defines the immutable contractual foundation of the Brain Simulator:
the :class:`CognitiveModule` abstract base class and the data structures that
flow across the :class:`~core.brain_bus.BrainBus` between cognitive modules on
every simulation timestep.

Design constraints (SPEC-001):
    * Standard library + NumPy only. No Brian2, no PyTorch, no framework imports.
      Concrete numerical/runtime backends are introduced in later SPECs and must
      depend on this contract, never the reverse.
    * Pure data contracts. The dataclasses below carry state; they contain no
      simulation logic. Behaviour lives in the concrete modules (SPEC-003+).

FROZEN CONTRACT
---------------
The public surface of this module -- the field names and types of every
dataclass and the abstract method signatures of :class:`CognitiveModule` -- is
frozen as of SPEC-001 approval. Any change requires an ADR in
``specs/DECISIONS.md`` and review with Opus 4.8, because all downstream modules
(SPEC-002 through SPEC-013) are written against exactly this interface.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List

import numpy as np

__all__ = [
    "NeuromodulationSignal",
    "ModuleInputs",
    "ModuleOutputs",
    "ModuleState",
    "SynapticTarget",
    "CognitiveModule",
]

# Contract version. Bump only alongside an ADR documenting the change.
INTERFACE_VERSION = "1.0.0"


@dataclass
class NeuromodulationSignal:
    """Global neuromodulatory levels broadcast to every module each timestep.

    Each value is a multiplicative factor centred on a basal level of ``1.0``
    and clamped, by convention, to the range ``[0.0, 2.0]``:

        * ``dopamine`` -- scales the global learning rate (TD-error broadcast).
        * ``noradrenaline`` -- modulates arousal / firing threshold gain.
        * ``acetylcholine`` -- gates attentional signal-to-noise and plasticity.
    """

    dopamine: float = 1.0
    noradrenaline: float = 1.0
    acetylcholine: float = 1.0


@dataclass
class ModuleInputs:
    """Inputs delivered to a cognitive module on a single timestep.

    Attributes:
        spike_trains: Boolean/binary spike mask from presynaptic sources,
            shape ``[N_pre]``.
        attention_signal: Top-down attentional gain in ``[0.0, 1.0]`` provided
            by the dorsal attention network (DAN).
        neuromodulation: Current global neuromodulatory state.
        timestamp_ms: Absolute simulation time in milliseconds.
    """

    spike_trains: np.ndarray
    attention_signal: float
    neuromodulation: NeuromodulationSignal = field(
        default_factory=NeuromodulationSignal
    )
    timestamp_ms: float = 0.0


@dataclass
class ModuleOutputs:
    """Outputs produced by a cognitive module on a single timestep.

    Attributes:
        spike_trains: Postsynaptic spike mask, shape ``[N_post]``.
        firing_rate: Instantaneous firing rate per neuron in spikes/s,
            shape ``[N]``.
        internal_state: Arbitrary module-specific payload published to the
            BrainBus (e.g. attractor id, prediction error). Not part of the
            numerical contract -- consumers must treat keys as optional.
    """

    spike_trains: np.ndarray
    firing_rate: np.ndarray
    internal_state: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ModuleState:
    """Complete observable state of a module for the BrainBus and renderer.

    Attributes:
        module_id: Stable identifier of the owning module.
        n_neurons: Number of neurons in the module.
        voltage: Membrane potential per neuron in mV, shape ``[N]``.
        firing_rate: Firing rate per neuron in Hz, shape ``[N]``.
        mean_weight: Mean synaptic weight across the module's afferents.
        active_synapses: Count of synapses currently above the activity floor.
        timestamp_ms: Absolute simulation time in milliseconds.
        metadata: Optional auxiliary diagnostics (not rendered numerically).
    """

    module_id: str
    n_neurons: int
    voltage: np.ndarray
    firing_rate: np.ndarray
    mean_weight: float
    active_synapses: int
    timestamp_ms: float
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SynapticTarget:
    """A connection exposed by a module for external plasticity rules.

    The LearningEngine (STDP / Hebbian, SPEC-003) reads and mutates the
    referenced ``weight_matrix`` in place.

    Attributes:
        source_module: Identifier of the presynaptic module.
        target_module: Identifier of the postsynaptic module.
        weight_matrix: Synaptic weights, shape ``[N_pre, N_post]``.
        synapse_type: ``"excitatory"`` or ``"inhibitory"``.
    """

    source_module: str
    target_module: str
    weight_matrix: np.ndarray
    synapse_type: str = "excitatory"


class CognitiveModule(ABC):
    """Abstract contract implemented by every cognitive module.

    A cognitive module models a functional brain region (e.g. hippocampus,
    prefrontal cortex, an attention network). The :class:`SimulationEngine`
    drives all modules in topological order once per timestep via
    :meth:`update`, and the :class:`BrainBus` exchanges their state.

    Every concrete module MUST implement all abstract methods. This class is
    frozen as of SPEC-001 -- see the module docstring.

    Attributes:
        module_id: Stable, unique identifier for this module instance.
        n_neurons: Number of neurons owned by this module.
    """

    module_id: str
    n_neurons: int

    def __init__(self, module_id: str, n_neurons: int) -> None:
        self.module_id = module_id
        self.n_neurons = n_neurons

    @abstractmethod
    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        """Advance the module by ``dt`` milliseconds.

        Called once per timestep by the SimulationEngine.

        Args:
            dt: Integration step in milliseconds (1.0 in the standard config).
            inputs: Presynaptic spikes, attention and neuromodulation for this
                timestep.

        Returns:
            The module's spike output and firing rates for this timestep.
        """

    @abstractmethod
    def get_state(self) -> ModuleState:
        """Return the current observable state of the module.

        Consumed by the BrainBus and the StateRenderer (3D visualization).
        """

    @abstractmethod
    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Apply a global neuromodulatory signal to the module in place.

        Dopamine scales learning rate, noradrenaline adjusts firing threshold,
        acetylcholine gates attentional signal-to-noise and plasticity.
        """

    @abstractmethod
    def get_synaptic_targets(self) -> List[SynapticTarget]:
        """Return the synaptic connections this module exposes for learning.

        Used by the LearningEngine to apply STDP / Hebbian updates.
        """

    @abstractmethod
    def reset(self) -> None:
        """Reset all internal state to initial conditions."""

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(module_id={self.module_id!r}, n_neurons={self.n_neurons})"
        )
