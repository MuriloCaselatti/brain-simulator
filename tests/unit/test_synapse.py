"""Tests for SPEC-003 -- STDPSynapse.

Pure-NumPy unit tests for the trace-based pairwise STDP rule. Cross-validation
against a Brian2 ``Synapses`` STDP oracle (Bi & Poo 1998 curve shape) lives in
``tests/scientific/test_lif_validation.py``.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.synapse import STDPSynapse  # noqa: E402


def test_initial_weight_matrix_scalar():
    syn = STDPSynapse(n_pre=4, n_post=3, weight_init=0.5)
    assert syn.weight_matrix.shape == (4, 3)
    assert np.all(syn.weight_matrix == 0.5)


def test_initial_weight_matrix_array():
    init = np.full((4, 3), 0.2)
    syn = STDPSynapse(n_pre=4, n_post=3, weight_init=init)
    assert np.array_equal(syn.weight_matrix, init)


def test_initial_weight_matrix_wrong_shape_rejected():
    with pytest.raises(ValueError):
        STDPSynapse(n_pre=4, n_post=3, weight_init=np.zeros((3, 4)))


# --- Direction of plasticity (Bi & Poo 1998 sign convention) ---------------------


def test_pre_before_post_potentiates():
    """Pre fires, then (after a short delay) post fires -> LTP."""
    syn = STDPSynapse(n_pre=1, n_post=1, weight_init=0.5)
    w0 = syn.weight_matrix.copy()

    # t=0: presynaptic spike.
    syn.update(dt=1.0, pre_spikes=[True], post_spikes=[False])
    # t=1..10: postsynaptic spike a few ms later (pre-before-post, dt > 0).
    for _ in range(9):
        syn.update(dt=1.0, pre_spikes=[False], post_spikes=[False])
    syn.update(dt=1.0, pre_spikes=[False], post_spikes=[True])

    assert syn.weight_matrix[0, 0] > w0[0, 0]


def test_post_before_pre_depresses():
    """Post fires, then (after a short delay) pre fires -> LTD."""
    syn = STDPSynapse(n_pre=1, n_post=1, weight_init=0.5)
    w0 = syn.weight_matrix.copy()

    syn.update(dt=1.0, pre_spikes=[False], post_spikes=[True])
    for _ in range(9):
        syn.update(dt=1.0, pre_spikes=[False], post_spikes=[False])
    syn.update(dt=1.0, pre_spikes=[True], post_spikes=[False])

    assert syn.weight_matrix[0, 0] < w0[0, 0]


# --- Clamping ----------------------------------------------------------------------


def test_weights_clamped_to_bounds():
    syn = STDPSynapse(
        n_pre=1, n_post=1, weight_init=0.999, w_min=0.0, w_max=1.0,
        a_plus=0.5, a_minus=0.5,
    )
    for _ in range(50):
        syn.update(dt=1.0, pre_spikes=[True], post_spikes=[True])

    assert syn.weight_matrix[0, 0] <= 1.0
    assert syn.weight_matrix[0, 0] >= 0.0


# --- lr_scale ------------------------------------------------------------------------


def test_lr_scale_zero_freezes_weights():
    syn = STDPSynapse(n_pre=1, n_post=1, weight_init=0.5)
    w0 = syn.weight_matrix.copy()

    syn.update(dt=1.0, pre_spikes=[True], post_spikes=[True], lr_scale=0.0)

    assert np.array_equal(syn.weight_matrix, w0)


# --- reset() -------------------------------------------------------------------------


def test_reset_restores_initial_weights_and_traces():
    syn = STDPSynapse(n_pre=2, n_post=2, weight_init=0.5)
    w0 = syn.weight_matrix.copy()

    syn.update(dt=1.0, pre_spikes=[True, False], post_spikes=[False, True])
    assert not np.array_equal(syn.weight_matrix, w0)
    assert np.any(syn.trace_pre != 0.0) or np.any(syn.trace_post != 0.0)

    syn.reset()

    assert np.array_equal(syn.weight_matrix, w0)
    assert np.all(syn.trace_pre == 0.0)
    assert np.all(syn.trace_post == 0.0)
