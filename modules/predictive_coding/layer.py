"""Brain Simulator -- Predictive Coding Layer (SPEC-006).

A single level of the Rao & Ballard (1999) predictive-coding hierarchy. Each
:class:`PredictiveLayer` owns two functional neuron populations, exactly as the
canonical cortical microcircuit prescribes (Bastos et al. 2012):

* **Prediction / representation neurons** ``r`` -- the level's current estimate
  of its latent cause. They project a *top-down generative prediction*
  ``p = W @ r`` of the activity of the level **below**.
* **Error neurons** ``error`` -- one per unit of the level below. They compute
  the prediction error ``epsilon = below_activity - p`` (a balance of
  excitatory bottom-up drive and inhibitory top-down prediction).

This class is a plain numerical helper, **not** a
:class:`~core.interfaces.CognitiveModule`. It is owned and orchestrated by
:class:`~modules.predictive_coding.hierarchy.PredictiveCodingHierarchy`, mirroring
the way :class:`~core.synapse.STDPSynapse` is a helper mutated by the
``LearningEngine`` rather than a module in its own right (ADR-008).

Mathematics (confirmed with Opus 4.8 before implementation)
-----------------------------------------------------------
For a level ``l`` predicting the level below ``l-1``:

    prediction      p_{l-1} = W_l @ r_l                       (generative)
    error           eps_{l-1} = below_activity - p_{l-1}      (error neurons)
    ascending drive a_l = W_l^T @ (pi * eps_{l-1})            (bottom-up)
    learning        W_l += lr * pi * outer(eps_{l-1}, r_l)    (Hebbian, error-gated)

``pi`` is the *precision* (inverse variance) of the error, scaled by attention
-- see :class:`PredictiveCodingHierarchy`. The learning rule is gradient descent
on the precision-weighted squared error ``0.5 * pi * ||eps||^2`` with respect to
``W``, so repeated exposure to the same stimulus monotonically reduces the error
(SPEC-006 acceptance criterion #1).
"""
from __future__ import annotations

from typing import Optional

import numpy as np

__all__ = ["PredictiveLayer"]


class PredictiveLayer:
    """One level of a predictive-coding hierarchy.

    Args:
        name: Human-readable label, e.g. ``"L1"``.
        n_units: Number of representation / prediction neurons at this level.
        n_below: Number of units in the level immediately below (the size of
            this level's prediction and of its error population).
        learning_rate: Step size of the error-gated Hebbian weight update.
        weight_decay: Coefficient of the ``-decay * W`` regulariser applied on
            every learning step (the ``alpha ||W||^2`` prior of the generative
            model). Together with :attr:`max_col_norm` it keeps the joint
            inference/learning dynamics bounded.
        max_col_norm: Maximum L2 norm of each generative-weight column. Columns
            that exceed it are rescaled back, removing the sparse-coding
            degeneracy where ``W`` grows without bound while ``r`` shrinks.
        weight_scale: Standard deviation of the initial random generative
            weights.
        rng: Optional NumPy random generator for reproducible initialisation.
    """

    def __init__(
        self,
        name: str,
        n_units: int,
        n_below: int,
        *,
        learning_rate: float = 0.02,
        weight_decay: float = 0.01,
        max_col_norm: float = 1.0,
        weight_scale: float = 0.1,
        rng: Optional[np.random.Generator] = None,
    ) -> None:
        if n_units <= 0 or n_below <= 0:
            raise ValueError("n_units and n_below must be positive")

        self.name = name
        self.n_units = n_units
        self.n_below = n_below
        self.learning_rate = learning_rate
        self.weight_decay = weight_decay
        self.max_col_norm = max_col_norm
        self._weight_scale = weight_scale
        self._rng = rng if rng is not None else np.random.default_rng()

        # Generative (top-down) weights: predict the level below from r.
        self.W = self._rng.normal(0.0, weight_scale, size=(n_below, n_units))
        # Representation neurons (latent cause estimate).
        self.r = np.zeros(n_units)
        # Error neurons (one per unit of the level below).
        self.error = np.zeros(n_below)

    # -- forward / generative pass ------------------------------------------

    def predict(self) -> np.ndarray:
        """Top-down generative prediction of the level below: ``W @ r``."""
        return self.W @ self.r

    def compute_error(self, below_activity: np.ndarray) -> np.ndarray:
        """Set and return the prediction error ``below_activity - predict()``.

        ``below_activity`` must have length :attr:`n_below`.
        """
        self.error = np.asarray(below_activity, dtype=float) - self.predict()
        return self.error

    # -- inference / learning ------------------------------------------------

    def ascending_drive(self, precision: float) -> np.ndarray:
        """Bottom-up drive to this level's representation: ``W^T (pi * eps)``."""
        return self.W.T @ (precision * self.error)

    def learn(self, precision: float) -> None:
        """Apply the error-gated Hebbian update to the generative weights.

        ``W += lr * (pi * outer(error, r) - decay * W)`` -- gradient descent on
        the precision-weighted squared prediction error with an ``L2`` weight
        prior. Columns are then clipped to :attr:`max_col_norm` so the joint
        inference/learning dynamics stay bounded.
        """
        self.W += self.learning_rate * (
            precision * np.outer(self.error, self.r) - self.weight_decay * self.W
        )
        self._enforce_col_norm()

    def _enforce_col_norm(self) -> None:
        norms = np.linalg.norm(self.W, axis=0)
        over = norms > self.max_col_norm
        if np.any(over):
            scale = np.ones_like(norms)
            scale[over] = self.max_col_norm / norms[over]
            self.W *= scale

    # -- housekeeping --------------------------------------------------------

    def reset(self) -> None:
        """Zero the representation and error neurons (weights are preserved)."""
        self.r = np.zeros(self.n_units)
        self.error = np.zeros(self.n_below)

    def reset_weights(self) -> None:
        """Re-draw the generative weights from the initial distribution."""
        self.W = self._rng.normal(
            0.0, self._weight_scale, size=(self.n_below, self.n_units)
        )

    def __repr__(self) -> str:
        return (
            f"PredictiveLayer(name={self.name!r}, n_units={self.n_units}, "
            f"n_below={self.n_below})"
        )
