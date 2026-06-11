"""Brain Simulator -- Predictive Coding Hierarchy (SPEC-006).

A three-level predictive-coding hierarchy after Rao & Ballard (1999) and the
Free Energy Principle (Friston 2010), exposed as a single frozen
:class:`~core.interfaces.CognitiveModule`. It owns three
:class:`~modules.predictive_coding.layer.PredictiveLayer` helpers and runs the
inference loop internally on every :meth:`update`.

Architecture
------------
Indexing the sensory input as level ``0`` and the three representation levels as
``1, 2, 3``::

        r3  (L3 prediction neurons)
        |  W3 (top-down prediction of level 2)
        v
    [eps2 error]  <-- r2  (L2 prediction neurons)
        ^             |  W2
        |             v
        |         [eps1 error]  <-- r1  (L1 prediction neurons)
        |             ^             |  W1
        |             |             v
        |             |         [eps0 error]  <-- x  (sensory input, level 0)

Each level ``l`` predicts the level below via generative weights ``W_l`` and the
error neurons of level ``l-1`` compute ``eps_{l-1} = below - W_l r_l``.

Inference (gradient descent on free energy ``F = sum_l 0.5 * pi * ||eps_l||^2``)::

    tau dr_l/dt = W_l^T (pi * eps_{l-1})   # bottom-up: ascending error
                  - pi * eps_l             # top-down: pull toward prediction from above
                  - leak * r_l             # sparsity / decay prior

Run for ``n_inference_steps`` settling iterations per tick, after which the
generative weights learn via the error-gated Hebbian rule (criterion #1).

Precision and attention (criterion #3)
--------------------------------------
The precision ``pi`` weighting every prediction error is

    pi = precision_base * (1 + precision_gain * attention_signal) * ach

where ``attention_signal`` in ``[0, 1]`` arrives from the DAN (SPEC-005) via
``ModuleInputs.attention_signal`` and ``ach`` is the acetylcholine
neuromodulator. Higher attention therefore *scales the weight of the prediction
error*, both in the inference dynamics and in the reported weighted-error norm.

Top-down modulation (criterion #2)
----------------------------------
A prior expectation can be injected at the top level via
:meth:`set_top_down_prior` (e.g. primed by Modern Hopfield memory, SPEC-004).
The prior pulls ``r3``, whose prediction reshapes ``eps2`` and so on down the
hierarchy, changing the lower-level representations.

Hybrid substrate
----------------
The inference core is rate-based (NumPy) -- this is what the acceptance criteria
test and what guarantees convergence on the target hardware (no CUDA). The
``ModuleOutputs`` are spiking-compatible (rectified rates in Hz plus a binary
spike mask) so the hierarchy plugs into the ``BrainBus`` and the 3D renderer
unchanged. Backing the representation neurons with a full
:class:`~core.neuron.LIFPopulation` is a documented extension point and is left
off by default to keep this module dependency-light and fast.
"""
from __future__ import annotations

from typing import List, Optional, Sequence

import numpy as np

from core.interfaces import (
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)
from modules.attention._utils import align_to
from modules.predictive_coding.layer import PredictiveLayer

__all__ = ["PredictiveCodingHierarchy"]


class PredictiveCodingHierarchy(CognitiveModule):
    """Three-level predictive-coding hierarchy (SPEC-006).

    Args:
        module_id: Stable identifier for this module instance.
        input_size: Number of sensory input units (level 0).
        level_sizes: Representation-neuron counts of the three levels,
            innermost last, e.g. ``(48, 32, 16)``.
        n_inference_steps: Settling iterations of the inference loop per tick.
        infer_rate: Learning-rate-like step size of the representation update.
        leak: Coefficient of the sparsity / decay prior on ``r``.
        precision_base: Baseline precision with zero attention.
        precision_gain: How strongly ``attention_signal`` raises precision.
        top_prior_precision: Precision of the top-level prior expectation.
        learning_rate: Step size of the generative weight update.
        max_rate_hz: Firing rate mapped to a fully-active representation unit.
        rng: Optional NumPy generator for reproducible weight initialisation.
    """

    def __init__(
        self,
        module_id: str = "predictive_coding",
        input_size: int = 64,
        level_sizes: Sequence[int] = (48, 32, 16),
        *,
        n_inference_steps: int = 20,
        infer_rate: float = 0.1,
        leak: float = 0.05,
        r_clip: float = 10.0,
        precision_base: float = 1.0,
        precision_gain: float = 1.0,
        top_prior_precision: float = 0.1,
        learning_rate: float = 0.02,
        max_rate_hz: float = 50.0,
        rng: Optional[np.random.Generator] = None,
    ) -> None:
        level_sizes = tuple(int(s) for s in level_sizes)
        if len(level_sizes) != 3:
            raise ValueError("SPEC-006 hierarchy requires exactly 3 levels")
        if input_size <= 0 or any(s <= 0 for s in level_sizes):
            raise ValueError("input_size and all level_sizes must be positive")

        # Representation neurons are this module's primary neuron count; error
        # neurons (one per unit of the level below each layer) are reported too.
        self._error_sizes = (input_size, level_sizes[0], level_sizes[1])
        n_neurons = sum(level_sizes) + sum(self._error_sizes)
        super().__init__(module_id, n_neurons)

        self.input_size = input_size
        self.level_sizes = level_sizes
        self.n_inference_steps = n_inference_steps
        self.infer_rate = infer_rate
        self.leak = leak
        self.r_clip = r_clip
        self.precision_base = precision_base
        self.precision_gain = precision_gain
        self.top_prior_precision = top_prior_precision
        self.max_rate_hz = max_rate_hz
        self._rng = rng if rng is not None else np.random.default_rng()

        below_sizes = (input_size, level_sizes[0], level_sizes[1])
        self.layers: List[PredictiveLayer] = [
            PredictiveLayer(
                name=f"L{i + 1}",
                n_units=level_sizes[i],
                n_below=below_sizes[i],
                learning_rate=learning_rate,
                rng=self._rng,
            )
            for i in range(3)
        ]

        self._top_prior = np.zeros(level_sizes[2])
        self._acetylcholine = 1.0
        self._learning_enabled = True
        self._last_precision = precision_base
        self._last_input = np.zeros(input_size)
        self._timestamp_ms = 0.0

    # -- top-down priming (criterion #2 / SPEC-004 hook) ---------------------

    def set_top_down_prior(self, prior: np.ndarray) -> None:
        """Inject a prior expectation at the top level (e.g. from memory)."""
        self._top_prior = align_to(prior, self.level_sizes[2])

    def clear_top_down_prior(self) -> None:
        """Remove any injected top-level prior."""
        self._top_prior = np.zeros(self.level_sizes[2])

    def set_learning_enabled(self, enabled: bool) -> None:
        """Freeze or unfreeze generative-weight plasticity."""
        self._learning_enabled = bool(enabled)

    # -- precision -----------------------------------------------------------

    def _precision(self, attention_signal: float) -> float:
        attention = float(np.clip(attention_signal, 0.0, 1.0))
        return (
            self.precision_base
            * (1.0 + self.precision_gain * attention)
            * max(0.0, self._acetylcholine)
        )

    # -- inference -----------------------------------------------------------

    def _infer(self, x: np.ndarray, precision: float) -> None:
        """Run the settling loop, updating every level's representation."""
        for _ in range(self.n_inference_steps):
            belows = [x, self.layers[0].r, self.layers[1].r]
            for i, layer in enumerate(self.layers):
                layer.compute_error(belows[i])

            deltas = []
            for i, layer in enumerate(self.layers):
                bottom_up = layer.ascending_drive(precision)
                if i < len(self.layers) - 1:
                    top_down = precision * self.layers[i + 1].error
                else:
                    top_down = self.top_prior_precision * (
                        layer.r - self._top_prior
                    )
                dr = bottom_up - top_down - self.leak * layer.r
                deltas.append(self.infer_rate * dr)

            for layer, delta in zip(self.layers, deltas):
                layer.r = np.clip(layer.r + delta, -self.r_clip, self.r_clip)

        # Refresh errors against the settled representations for reporting.
        belows = [x, self.layers[0].r, self.layers[1].r]
        for i, layer in enumerate(self.layers):
            layer.compute_error(belows[i])

    # -- output assembly -----------------------------------------------------

    def _firing_rates(self) -> np.ndarray:
        """Rectified representation + error activity, in Hz, length n_neurons."""
        parts: List[np.ndarray] = []
        for layer in self.layers:
            parts.append(np.maximum(layer.r, 0.0))
        for layer in self.layers:
            parts.append(np.abs(layer.error))
        activity = np.concatenate(parts)
        peak = float(activity.max()) if activity.size else 0.0
        if peak <= 0.0:
            return np.zeros(self.n_neurons)
        return activity / peak * self.max_rate_hz

    def _error_norms(self) -> List[float]:
        return [float(np.linalg.norm(layer.error)) for layer in self.layers]

    def _free_energy(self, precision: float) -> float:
        return float(
            0.5
            * precision
            * sum(float(layer.error @ layer.error) for layer in self.layers)
        )

    # -- CognitiveModule contract --------------------------------------------

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        x = align_to(inputs.spike_trains, self.input_size)
        self._last_input = x
        precision = self._precision(inputs.attention_signal)
        self._last_precision = precision

        self._infer(x, precision)
        if self._learning_enabled:
            for layer in self.layers:
                layer.learn(precision)

        self._timestamp_ms = inputs.timestamp_ms

        firing_rate = self._firing_rates()
        spike_trains = (firing_rate > 0.5 * self.max_rate_hz).astype(float)
        error_norms = self._error_norms()

        return ModuleOutputs(
            spike_trains=spike_trains,
            firing_rate=firing_rate,
            internal_state={
                "prediction_error_per_level": error_norms,
                "weighted_error_per_level": [
                    precision * e for e in error_norms
                ],
                "total_prediction_error": float(sum(error_norms)),
                "free_energy": self._free_energy(precision),
                "precision": precision,
                "attention_signal": float(np.clip(inputs.attention_signal, 0, 1)),
                "top_prediction": self.layers[0].predict(),
            },
        )

    def get_state(self) -> ModuleState:
        firing_rate = self._firing_rates()
        # Map rectified rates to a plausible membrane voltage for the renderer.
        voltage = -70.0 + 25.0 * (firing_rate / self.max_rate_hz)
        mean_weight = float(
            np.mean([float(np.mean(layer.W)) for layer in self.layers])
        )
        active = sum(int(np.count_nonzero(layer.W)) for layer in self.layers)
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=voltage,
            firing_rate=firing_rate,
            mean_weight=mean_weight,
            active_synapses=active,
            timestamp_ms=self._timestamp_ms,
            metadata={
                "level_sizes": self.level_sizes,
                "error_sizes": self._error_sizes,
                "prediction_error_per_level": self._error_norms(),
                "precision": self._last_precision,
            },
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        """Acetylcholine gates precision (attentional signal-to-noise)."""
        self._acetylcholine = max(0.0, signal.acetylcholine)

    def get_synaptic_targets(self) -> List[SynapticTarget]:
        """Expose the generative weights for inspection.

        Predictive-coding plasticity is applied *internally* by this module
        (the error-gated Hebbian rule is not STDP), so these targets are
        published for observability rather than for the ``LearningEngine``.
        """
        targets: List[SynapticTarget] = []
        below_ids = [f"{self.module_id}.L0_input"] + [
            f"{self.module_id}.L{i}" for i in range(1, 3)
        ]
        for i, layer in enumerate(self.layers):
            targets.append(
                SynapticTarget(
                    source_module=f"{self.module_id}.{layer.name}",
                    target_module=below_ids[i],
                    weight_matrix=layer.W,
                    synapse_type="excitatory",
                )
            )
        return targets

    def reset(self) -> None:
        for layer in self.layers:
            layer.reset()
            layer.reset_weights()
        self._top_prior = np.zeros(self.level_sizes[2])
        self._acetylcholine = 1.0
        self._learning_enabled = True
        self._last_precision = self.precision_base
        self._last_input = np.zeros(self.input_size)
        self._timestamp_ms = 0.0
