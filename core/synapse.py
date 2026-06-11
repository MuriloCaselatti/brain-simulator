"""Brain Simulator -- STDP synapse.

Implements :class:`STDPSynapse`, a vectorized pairwise spike-timing-dependent
plasticity (STDP) rule for an ``[N_pre, N_post]`` projection (SPEC-003).

The rule follows the standard trace-based formulation (e.g. the Brian2 STDP
tutorial / Song, Miller & Abbott 2000): each synapse keeps an exponentially
decaying eligibility trace per pre- and post-synaptic neuron. On a
presynaptic spike the weight is potentiated by the (decayed) postsynaptic
trace; on a postsynaptic spike it is depressed by the (decayed) presynaptic
trace. With ``A+ > 0`` and ``A- > 0`` this reproduces the classic asymmetric
LTP/LTD curve reported by Bi & Poo (1998): pre-before-post pairings
(:math:`\\Delta t = t_{post} - t_{pre} > 0`) potentiate the synapse, and
post-before-pre pairings (:math:`\\Delta t < 0`) depress it, with magnitude
decaying exponentially in :math:`|\\Delta t|`.

Standard parameters (SPEC-003)::

    A+ = 0.01    A- = 0.0105    tau+ = tau- = 20 ms
"""
from __future__ import annotations

from typing import Union

import numpy as np

__all__ = ["STDPSynapse", "A_PLUS", "A_MINUS", "TAU_PLUS", "TAU_MINUS"]

# Standard STDP parameters (SPEC-003).
A_PLUS = 0.01
A_MINUS = 0.0105
TAU_PLUS = 20.0  # ms
TAU_MINUS = 20.0  # ms


class STDPSynapse:
    """Pairwise STDP for a dense ``[N_pre, N_post]`` projection.

    Args:
        n_pre: Number of presynaptic neurons.
        n_post: Number of postsynaptic neurons.
        weight_init: Initial weight, either a scalar (broadcast to every
            connection) or an array of shape ``(n_pre, n_post)``.
        a_plus: Potentiation step size (pre-before-post).
        a_minus: Depression step size (post-before-pre).
        tau_plus: Decay time constant of the presynaptic trace, in ms.
        tau_minus: Decay time constant of the postsynaptic trace, in ms.
        w_min: Minimum synaptic weight (clamp).
        w_max: Maximum synaptic weight (clamp).
    """

    def __init__(
        self,
        n_pre: int,
        n_post: int,
        weight_init: Union[float, np.ndarray] = 0.5,
        a_plus: float = A_PLUS,
        a_minus: float = A_MINUS,
        tau_plus: float = TAU_PLUS,
        tau_minus: float = TAU_MINUS,
        w_min: float = 0.0,
        w_max: float = 1.0,
    ) -> None:
        self.n_pre = n_pre
        self.n_post = n_post
        self.a_plus = a_plus
        self.a_minus = a_minus
        self.tau_plus = tau_plus
        self.tau_minus = tau_minus
        self.w_min = w_min
        self.w_max = w_max

        if np.isscalar(weight_init):
            self.weight_matrix = np.full((n_pre, n_post), float(weight_init))
        else:
            matrix = np.array(weight_init, dtype=float, copy=True)
            if matrix.shape != (n_pre, n_post):
                raise ValueError(
                    f"weight_init shape must be ({n_pre}, {n_post}), "
                    f"got {matrix.shape}"
                )
            self.weight_matrix = matrix

        self._initial_weights = self.weight_matrix.copy()
        self.trace_pre = np.zeros(n_pre)
        self.trace_post = np.zeros(n_post)

    def update(
        self,
        dt: float,
        pre_spikes: np.ndarray,
        post_spikes: np.ndarray,
        lr_scale: float = 1.0,
    ) -> None:
        """Decay traces and apply STDP weight updates for one timestep.

        Args:
            dt: Elapsed time in ms.
            pre_spikes: Boolean/binary mask of presynaptic spikes, shape
                ``(n_pre,)``.
            post_spikes: Boolean/binary mask of postsynaptic spikes, shape
                ``(n_post,)``.
            lr_scale: Multiplicative learning-rate scale (e.g. dopamine-driven
                gain from :class:`~core.learning_engine.PlasticityScheduler`).
        """
        pre_spikes = np.asarray(pre_spikes, dtype=bool)
        post_spikes = np.asarray(post_spikes, dtype=bool)

        self.trace_pre *= np.exp(-dt / self.tau_plus)
        self.trace_post *= np.exp(-dt / self.tau_minus)

        if pre_spikes.any():
            self.trace_pre[pre_spikes] += self.a_plus * lr_scale
            self.weight_matrix[pre_spikes, :] += self.trace_post[np.newaxis, :]

        if post_spikes.any():
            self.trace_post[post_spikes] -= self.a_minus * lr_scale
            self.weight_matrix[:, post_spikes] += self.trace_pre[:, np.newaxis]

        np.clip(self.weight_matrix, self.w_min, self.w_max, out=self.weight_matrix)

    def reset(self) -> None:
        """Restore initial weights and clear eligibility traces."""
        self.weight_matrix = self._initial_weights.copy()
        self.trace_pre = np.zeros(self.n_pre)
        self.trace_post = np.zeros(self.n_post)
