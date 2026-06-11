"""Brain Simulator -- LIF neuron population (Brian2-backed).

Implements :class:`LIFPopulation`, a vectorized Leaky Integrate-and-Fire
population for 500-2000 neurons (SPEC-003), built on top of Brian2's
``NeuronGroup``. Conforms to the frozen SPEC-001
:class:`~core.interfaces.CognitiveModule` contract.

Standard biological parameters (SPEC-003)::

    V_REST    = -70.0 mV
    V_THRESH  = -55.0 mV
    V_RESET   = -70.0 mV
    TAU_M     =  20.0 ms
    T_REFRACT =   2.0 ms

Codegen note: ``prefs.codegen.target`` is pinned to ``"numpy"`` so the
population runs on any machine without a configured C++ compiler -- the
target hardware (ADR-001) has no CUDA and is not guaranteed to have a working
Cython toolchain.
"""
from __future__ import annotations

from collections import deque
from typing import Deque, List, Tuple, Union

import numpy as np
from brian2 import Clock, NeuronGroup, Network, SpikeMonitor, mV, ms, prefs

from core.interfaces import (
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)

prefs.codegen.target = "numpy"

__all__ = [
    "LIFPopulation",
    "V_REST",
    "V_THRESH",
    "V_RESET",
    "TAU_M",
    "T_REFRACT",
    "MIN_NEURONS",
    "MAX_NEURONS",
]

# Standard biological parameters (SPEC-003).
V_REST = -70.0  # mV
V_THRESH = -55.0  # mV
V_RESET = -70.0  # mV
TAU_M = 20.0  # ms
T_REFRACT = 2.0  # ms

MIN_NEURONS = 500
MAX_NEURONS = 2000

# Internal Brian2 integration step. Smaller than the 1ms BrainBus tick for
# numerical accuracy of the leaky-integration dynamics.
_BRIAN_DT_MS = 0.1

_LIF_EQS = """
dv/dt = (v_rest - v + I) / tau_m : volt (unless refractory)
v_rest : volt
v_thresh : volt
v_reset : volt
I : volt
"""


class LIFPopulation(CognitiveModule):
    """A vectorized population of Leaky Integrate-and-Fire neurons.

    Wraps a Brian2 ``NeuronGroup`` + ``SpikeMonitor`` in its own ``Network``
    and ``Clock``, so multiple populations can coexist and be advanced
    independently via :meth:`update`.

    Args:
        module_id: Stable identifier for this module instance.
        n_neurons: Population size, constrained to ``[500, 2000]`` per
            SPEC-003 (hardware constraint, ADR-001).
        v_rest, v_thresh, v_reset, tau_m, t_refract: Biological parameters,
            default to the SPEC-003 standard values above.
        input_gain: Scalar (mV per spike) converting the summed presynaptic
            spike count from :attr:`ModuleInputs.spike_trains` into an
            additional driving current applied uniformly to the population.
        rate_window_ms: Length of the sliding window (in ms of simulated
            time) used to estimate :attr:`ModuleOutputs.firing_rate`.
    """

    def __init__(
        self,
        module_id: str,
        n_neurons: int,
        v_rest: float = V_REST,
        v_thresh: float = V_THRESH,
        v_reset: float = V_RESET,
        tau_m: float = TAU_M,
        t_refract: float = T_REFRACT,
        input_gain: float = 0.5,
        rate_window_ms: float = 100.0,
    ) -> None:
        if not (MIN_NEURONS <= n_neurons <= MAX_NEURONS):
            raise ValueError(
                f"n_neurons must be within [{MIN_NEURONS}, {MAX_NEURONS}] "
                f"per SPEC-003, got {n_neurons}"
            )

        super().__init__(module_id, n_neurons)

        self._v_rest = v_rest
        self._v_thresh_base = v_thresh
        self._v_reset = v_reset
        self._tau_m = tau_m
        self._t_refract = t_refract
        self._input_gain = input_gain
        self._rate_window_ms = rate_window_ms

        self._external_current = np.zeros(n_neurons)  # mV-equivalent drive
        self._acetylcholine_gain = 1.0

        # (spiked_mask, dt_ms) pairs for the sliding firing-rate estimate.
        self._spike_history: Deque[Tuple[np.ndarray, float]] = deque(maxlen=1000)

        self._build_network()

    # -- Network construction ---------------------------------------------

    def _build_network(self) -> None:
        clock = Clock(dt=_BRIAN_DT_MS * ms)
        group = NeuronGroup(
            self.n_neurons,
            _LIF_EQS,
            threshold="v > v_thresh",
            reset="v = v_reset",
            refractory=self._t_refract * ms,
            method="euler",
            clock=clock,
            namespace={"tau_m": self._tau_m * ms},
        )
        group.v = self._v_rest * mV
        group.v_rest = self._v_rest * mV
        group.v_thresh = self._v_thresh_base * mV
        group.v_reset = self._v_reset * mV
        group.I = 0 * mV

        monitor = SpikeMonitor(group)

        self._clock = clock
        self._group = group
        self._monitor = monitor
        self._network = Network(group, monitor)
        self._prev_counts = np.zeros(self.n_neurons, dtype=int)

    # -- External drive -----------------------------------------------------

    def set_input_current(self, current_mV: Union[float, np.ndarray]) -> None:
        """Set a constant per-neuron baseline current (in mV-equivalent units).

        Used directly by scientific experiments that bypass
        :attr:`ModuleInputs.spike_trains` to characterise the neuron's f-I
        curve.
        """
        current = np.asarray(current_mV, dtype=float)
        if current.ndim == 0:
            current = np.full(self.n_neurons, float(current))
        if current.shape != (self.n_neurons,):
            raise ValueError(
                f"current_mV must be scalar or shape ({self.n_neurons},), "
                f"got {current.shape}"
            )
        self._external_current = current

    # -- CognitiveModule contract -------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        """Advance the population by ``dt`` ms and return its spikes/rates.

        The driving current applied to every neuron is the sum of:

        * :meth:`set_input_current`'s per-neuron baseline, and
        * the total presynaptic spike count in ``inputs.spike_trains``
          scaled by ``input_gain``, applied uniformly to the population,

        further scaled by an attentional gain derived from
        ``inputs.attention_signal`` and the acetylcholine-modulated
        signal-to-noise gain (see :meth:`apply_neuromodulation`).
        """
        presynaptic_drive = float(np.sum(inputs.spike_trains)) * self._input_gain
        attention_gain = 1.0 + (inputs.attention_signal - 0.5) * self._acetylcholine_gain

        total_current = (self._external_current + presynaptic_drive) * attention_gain
        self._group.I = total_current * mV

        self._network.run(dt * ms)

        counts = np.array(self._monitor.count, dtype=int)
        delta_counts = counts - self._prev_counts
        spiked = delta_counts > 0
        self._prev_counts = counts

        # Store spike *counts* (not just the binary mask) so the firing-rate
        # estimate is correct even when dt spans multiple spikes per neuron
        # (e.g. long single-shot updates used in scientific validation).
        self._spike_history.append((delta_counts.astype(float), dt))

        return ModuleOutputs(
            spike_trains=spiked.astype(float),
            firing_rate=self._compute_firing_rate(),
            internal_state={
                "mean_voltage_mV": float(np.mean(self._group.v / mV)),
            },
        )

    def get_state(self) -> ModuleState:
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=np.array(self._group.v / mV),
            firing_rate=self._compute_firing_rate(),
            mean_weight=float(self._input_gain),
            active_synapses=0,
            timestamp_ms=float(self._network.t / ms),
            metadata={
                "v_thresh_mV": float(np.mean(self._group.v_thresh / mV)),
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Apply global neuromodulation.

        * ``noradrenaline`` shifts the firing threshold: above-basal levels
          (arousal) lower the threshold, increasing excitability.
        * ``acetylcholine`` scales the attentional signal-to-noise gain
          applied to the presynaptic drive in :meth:`update`.
        """
        threshold_shift_mV = (signal.noradrenaline - 1.0) * 5.0
        self._group.v_thresh = (self._v_thresh_base - threshold_shift_mV) * mV
        self._acetylcholine_gain = max(0.0, signal.acetylcholine)

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        # LIFPopulation has no intrinsic recurrent connectivity; afferent
        # projections are owned by STDPSynapse/LearningEngine (SPEC-003).
        return []

    def reset(self) -> None:
        self._build_network()
        self._spike_history.clear()
        self._external_current[:] = 0.0
        self._acetylcholine_gain = 1.0

    # -- Helpers --------------------------------------------------------------

    def _compute_firing_rate(self) -> np.ndarray:
        if not self._spike_history:
            return np.zeros(self.n_neurons)

        total_spikes = np.zeros(self.n_neurons)
        total_time_ms = 0.0
        for spiked, dt in self._spike_history:
            total_spikes += spiked
            total_time_ms += dt

        # Only average over the configured window.
        if total_time_ms > self._rate_window_ms and len(self._spike_history) > 1:
            # Recompute using only the most recent entries within the window.
            total_spikes = np.zeros(self.n_neurons)
            total_time_ms = 0.0
            for spiked, dt in reversed(self._spike_history):
                total_spikes += spiked
                total_time_ms += dt
                if total_time_ms >= self._rate_window_ms:
                    break

        if total_time_ms <= 0:
            return np.zeros(self.n_neurons)

        return total_spikes / (total_time_ms / 1000.0)
