"""Brain Simulator -- demo brain assembly for the 3D visualization (SPEC-009).

SPEC-009 is a *visualization* spec: its job is to render, in real time, the
state the :class:`~core.simulation_engine.SimulationEngine` publishes on the
:class:`~core.brain_bus.BrainBus`. To do that it needs something stepping
through the engine fast enough for ~30fps on the target hardware (Acer Aspire 3,
integrated GPU, no CUDA).

The full SPEC-003..008 cognitive modules are either heavy (Brian2 LIF settles in
~70ms per ``net.run``; sentence-transformers for semantic memory) or require
task-specific inputs, so driving eight of them at 1000 ticks/s in real time is
out of scope here. Instead this module provides :class:`DemoRegion`, a
lightweight rate-based :class:`~core.interfaces.CognitiveModule` that produces
biologically-plausible, time-varying, input-driven firing. The eight regions are
registered and stepped through the **real** engine and BrainBus, so the data the
visualization renders is genuinely produced by the simulation pipeline -- only
the per-region dynamics are simplified. Swapping in a real cognitive module is
just a different :meth:`~core.simulation_engine.SimulationEngine.add_module`
call.

Anatomy (positions/colours/radii) mirrors ``specs/BLUEPRINT.md`` section 11.
"""
from __future__ import annotations

from typing import Dict, List, Optional, Tuple

import numpy as np

from core.interfaces import (
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)
from core.simulation_engine import SimulationEngine
from modules.neuromodulation.system import NeuromodulatorSystem

__all__ = [
    "DemoRegion",
    "REGION_LAYOUT",
    "REGION_CONNECTIONS",
    "EXECUTION_DEPENDENCIES",
    "NEUROMODULATOR_ID",
    "build_demo_brain",
]

# LIF-like membrane constants (mV) -- only used to give get_state().voltage a
# plausible range for the visualization; this is not a Brian2 integrator.
V_REST = -70.0
V_THRESH = -55.0
V_RESET = -75.0

# -- Anatomy (BLUEPRINT.md section 11) ------------------------------------------
# pos in Three.js world units, color as a 0xRRGGBB int, radius in world units.
REGION_LAYOUT: Dict[str, Dict[str, object]] = {
    "sensory":         {"pos": [0.0, -1.0, 2.0],  "color": 0x4FC3F7, "radius": 0.6,
                        "label": "Sensory"},
    "attention_dan":   {"pos": [1.5, 1.0, 1.0],   "color": 0xAB47BC, "radius": 0.5,
                        "label": "Attention (DAN)"},
    "attention_van":   {"pos": [-1.5, 1.0, 1.0],  "color": 0x7E57C2, "radius": 0.5,
                        "label": "Attention (VAN)"},
    "working_memory":  {"pos": [0.0, 2.0, 0.0],   "color": 0x26A69A, "radius": 0.7,
                        "label": "Working Memory"},
    "episodic_memory": {"pos": [1.0, 0.0, -1.0],  "color": 0x42A5F5, "radius": 0.6,
                        "label": "Episodic Memory"},
    "semantic_memory": {"pos": [-1.0, 0.0, -1.0], "color": 0x5C6BC0, "radius": 0.6,
                        "label": "Semantic Memory"},
    "pfc":             {"pos": [0.0, 3.0, 0.0],   "color": 0xEF5350, "radius": 0.8,
                        "label": "PFC"},
    "amygdala":        {"pos": [1.0, -1.0, 0.0],  "color": 0xFF7043, "radius": 0.4,
                        "label": "Amygdala"},
}

NEUROMODULATOR_ID = "neuromodulators"

# Visual synaptic arcs (source -> target, type). Includes top-down feedback
# loops, which are purely cosmetic -- they do NOT constrain execution order.
REGION_CONNECTIONS: List[Tuple[str, str, str]] = [
    ("sensory", "attention_dan", "excitatory"),
    ("sensory", "attention_van", "excitatory"),
    ("sensory", "episodic_memory", "excitatory"),
    ("sensory", "amygdala", "excitatory"),
    ("attention_dan", "working_memory", "excitatory"),
    ("attention_van", "working_memory", "excitatory"),
    ("attention_dan", "sensory", "excitatory"),        # top-down feedback (visual only)
    ("semantic_memory", "episodic_memory", "excitatory"),
    ("episodic_memory", "working_memory", "excitatory"),
    ("working_memory", "pfc", "excitatory"),
    ("amygdala", "pfc", "excitatory"),
    ("pfc", "working_memory", "excitatory"),           # top-down feedback (visual only)
    ("pfc", "attention_dan", "excitatory"),            # top-down feedback (visual only)
    ("pfc", "amygdala", "inhibitory"),                 # executive down-regulation
]

# Execution dependencies fed to SimulationEngine.add_module(depends_on=...).
# A strict DAG (no feedback edges) so Kahn's topological sort never sees a cycle.
EXECUTION_DEPENDENCIES: Dict[str, List[str]] = {
    "sensory": [],
    "semantic_memory": [],
    "attention_dan": ["sensory"],
    "attention_van": ["sensory"],
    "amygdala": ["sensory"],
    "episodic_memory": ["sensory", "semantic_memory"],
    "working_memory": ["attention_dan", "attention_van", "episodic_memory"],
    "pfc": ["working_memory", "amygdala"],
}


class DemoRegion(CognitiveModule):
    """A lightweight rate-based population for the SPEC-009 demo.

    Each neuron fires as an inhomogeneous Poisson process whose rate combines a
    baseline, an intrinsic oscillation (so source regions pulse without external
    input), and a drive proportional to the fraction of active afferent spikes.
    Noradrenaline and acetylcholine (broadcast by the engine when a
    :class:`NeuromodulatorSystem` is registered) scale the rate, so dopaminergic
    bursts visibly ripple through the network.

    The dynamics are intentionally simple -- this is a renderer test fixture, not
    a scientific model. See the module docstring.

    Args:
        module_id: Stable identifier (one of :data:`REGION_LAYOUT`).
        n_neurons: Population size.
        baseline_hz: Resting firing rate (Hz).
        intrinsic_hz: Amplitude of the intrinsic oscillatory drive (Hz).
        osc_freq_hz: Frequency of the intrinsic oscillation (Hz); 0 disables it.
        input_gain: Hz of drive per unit of afferent activity fraction.
        seed: Optional RNG seed for reproducibility.
    """

    MAX_HZ = 120.0

    def __init__(
        self,
        module_id: str,
        n_neurons: int = 200,
        baseline_hz: float = 4.0,
        intrinsic_hz: float = 0.0,
        osc_freq_hz: float = 0.0,
        input_gain: float = 60.0,
        seed: Optional[int] = None,
    ) -> None:
        super().__init__(module_id, n_neurons)
        self.baseline_hz = baseline_hz
        self.intrinsic_hz = intrinsic_hz
        self.osc_freq_hz = osc_freq_hz
        self.input_gain = input_gain
        self._seed = seed
        self._rng = np.random.default_rng(seed)

        self._voltage = np.full(n_neurons, V_REST)
        self._rate = np.full(n_neurons, baseline_hz)
        self._spikes = np.zeros(n_neurons)
        self._na_gain = 1.0
        self._ach_gain = 1.0
        self._timestamp_ms = 0.0
        # Per-neuron heterogeneity, fixed for the life of the population.
        self._excitability = 0.5 + self._rng.random(n_neurons)

    # -- CognitiveModule contract -------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        self._timestamp_ms = inputs.timestamp_ms
        t_s = inputs.timestamp_ms / 1000.0

        afferent = np.asarray(inputs.spike_trains, dtype=float)
        drive = float(afferent.mean()) if afferent.size else 0.0

        if self.osc_freq_hz > 0.0:
            osc = 0.5 * (1.0 + np.sin(2.0 * np.pi * self.osc_freq_hz * t_s))
        else:
            osc = 0.0

        attention = float(np.clip(inputs.attention_signal, 0.0, 2.0))
        target_hz = (
            self.baseline_hz
            + self.intrinsic_hz * osc
            + self.input_gain * drive * attention * self._ach_gain
        )
        target_hz *= self._na_gain

        rate = np.clip(target_hz * self._excitability, 0.0, self.MAX_HZ)
        p_spike = np.clip(rate * dt / 1000.0, 0.0, 1.0)
        spikes = (self._rng.random(self.n_neurons) < p_spike).astype(float)

        # Plausible membrane voltage for the renderer: scales toward threshold
        # with rate, resets where a spike fired.
        depol = (V_THRESH - V_REST) * np.clip(rate / self.MAX_HZ, 0.0, 1.0)
        voltage = V_REST + depol + self._rng.normal(0.0, 1.0, self.n_neurons)
        voltage[spikes > 0] = V_RESET

        self._rate = rate
        self._spikes = spikes
        self._voltage = voltage

        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=rate,
            internal_state={
                "mean_hz": float(rate.mean()),
                "n_spikes": int(spikes.sum()),
            },
        )

    def get_state(self) -> ModuleState:
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=self._voltage,
            firing_rate=self._rate,
            mean_weight=0.5,
            active_synapses=self.n_neurons,
            timestamp_ms=self._timestamp_ms,
            metadata={"n_spikes": int(self._spikes.sum())},
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Noradrenaline scales overall excitability; acetylcholine the gain on
        afferent (attended) drive -- mirrors the SPEC-008 conventions."""
        self._na_gain = max(0.0, float(signal.noradrenaline))
        self._ach_gain = max(0.0, float(signal.acetylcholine))

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        return []

    def reset(self) -> None:
        self._rng = np.random.default_rng(self._seed)
        self._voltage = np.full(self.n_neurons, V_REST)
        self._rate = np.full(self.n_neurons, self.baseline_hz)
        self._spikes = np.zeros(self.n_neurons)
        self._na_gain = 1.0
        self._ach_gain = 1.0
        self._timestamp_ms = 0.0
        self._excitability = 0.5 + self._rng.random(self.n_neurons)


# Per-region dynamics tuning. Source regions (no afferents) get an intrinsic
# oscillation so the network is driven; downstream regions inherit activity.
_REGION_DYNAMICS: Dict[str, Dict[str, float]] = {
    "sensory":         {"baseline_hz": 8.0,  "intrinsic_hz": 45.0, "osc_freq_hz": 1.2},
    "semantic_memory": {"baseline_hz": 6.0,  "intrinsic_hz": 18.0, "osc_freq_hz": 0.4},
    "attention_dan":   {"baseline_hz": 4.0,  "input_gain": 70.0},
    "attention_van":   {"baseline_hz": 4.0,  "input_gain": 70.0},
    "amygdala":        {"baseline_hz": 5.0,  "input_gain": 80.0},
    "episodic_memory": {"baseline_hz": 4.0,  "input_gain": 55.0},
    "working_memory":  {"baseline_hz": 5.0,  "intrinsic_hz": 6.0, "osc_freq_hz": 6.0,
                        "input_gain": 50.0},
    "pfc":             {"baseline_hz": 3.0,  "input_gain": 45.0},
}


def build_demo_brain(
    n_neurons: int = 200, seed: Optional[int] = 7
) -> SimulationEngine:
    """Assemble the 8-region demo brain on a real :class:`SimulationEngine`.

    Registers one :class:`DemoRegion` per :data:`REGION_LAYOUT` entry (wired via
    :data:`EXECUTION_DEPENDENCIES`) plus a :class:`NeuromodulatorSystem` for the
    dopamine halo, and designates the latter as the global neuromodulation source
    so noradrenaline/acetylcholine are broadcast to every region each tick.

    Args:
        n_neurons: Neurons per region.
        seed: Base RNG seed; each region is seeded deterministically from it.

    Returns:
        A configured engine, ready to :meth:`~core.simulation_engine.SimulationEngine.step`.
    """
    engine = SimulationEngine()

    for i, region_id in enumerate(REGION_LAYOUT):
        params = dict(_REGION_DYNAMICS.get(region_id, {}))
        region = DemoRegion(
            module_id=region_id,
            n_neurons=n_neurons,
            seed=None if seed is None else seed + i,
            **params,
        )
        engine.add_module(region, depends_on=EXECUTION_DEPENDENCIES[region_id])

    neuromod = NeuromodulatorSystem(module_id=NEUROMODULATOR_ID)
    # Depends on PFC so it sits late in the chain (Reasoning -> Neuromodulators).
    engine.add_module(neuromod, depends_on=["pfc"])
    engine.register_neuromodulator(NEUROMODULATOR_ID)

    # Force a topological-order computation now so wiring errors surface eagerly.
    _ = engine.execution_order
    return engine
