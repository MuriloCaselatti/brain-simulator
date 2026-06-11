"""Brain Simulator -- shared helpers for SPEC-005 attention modules."""
from __future__ import annotations

import numpy as np

__all__ = ["align_to", "normalize", "center_surround_contrast"]


def align_to(array: np.ndarray, n: int) -> np.ndarray:
    """Coerce ``array`` to a flat float array of length ``n``.

    Pads with zeros if shorter, truncates if longer. The
    ``SimulationEngine`` concatenates the spike trains of *all* of a
    module's dependencies, so a module's input may not match its own
    population size.
    """
    array = np.asarray(array, dtype=float).ravel()
    if array.size == n:
        return array
    if array.size > n:
        return array[:n]
    return np.pad(array, (0, n - array.size))


def normalize(values: np.ndarray) -> np.ndarray:
    """Scale ``values`` to ``[0, 1]`` by their maximum (zeros if all <= 0)."""
    if values.size == 0:
        return values
    max_val = float(values.max())
    if max_val <= 0.0:
        return np.zeros_like(values)
    return values / max_val


def center_surround_contrast(activity: np.ndarray) -> np.ndarray:
    """Per-element difference between ``activity`` and its 1D ring neighbours.

    A simple discrete center-surround receptive field:
    ``contrast[i] = activity[i] - mean(activity[i-1], activity[i+1])``.
    """
    n = activity.size
    if n < 3:
        return np.zeros(n)
    left = np.roll(activity, 1)
    right = np.roll(activity, -1)
    surround = (left + right) / 2.0
    return activity - surround
