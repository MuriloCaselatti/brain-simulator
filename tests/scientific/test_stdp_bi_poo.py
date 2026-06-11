"""SPEC-013 -- STDP replicates the Bi & Poo (1998) timing window.

Bi & Poo (1998) measured, in cultured hippocampal neurons, how the change in
synaptic strength depends on the relative timing
:math:`\\Delta t = t_{post} - t_{pre}` of a single pre/post spike pair:

    * :math:`\\Delta t > 0` (pre fires *before* post) -> potentiation (LTP),
    * :math:`\\Delta t < 0` (post fires *before* pre) -> depression (LTD),
    * the magnitude of the change decays roughly **exponentially** in
      :math:`|\\Delta t|`, with two time constants on the order of ~20 ms.

This suite reconstructs the full :math:`\\Delta w(\\Delta t)` curve for our
:class:`~core.synapse.STDPSynapse` and validates it against two references:

    1. a Brian2 ``Synapses`` STDP oracle implementing the same trace-based
       equations (Brian2 is the project's reference simulator), and
    2. the analytic STDP window :math:`A_\\pm \\exp(-|\\Delta t| / \\tau_\\pm)`.

Per SPEC-013 the agreement criterion is a coefficient of determination
``R^2 > 0.90`` for the reconstructed curve.

References:
    * Bi, G. & Poo, M. (1998). Synaptic modifications in cultured hippocampal
      neurons. J. Neurosci. 18(24): 10464-10472.
    * Song, Miller & Abbott (2000). Competitive Hebbian learning through STDP.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.synapse import (  # noqa: E402
    A_MINUS,
    A_PLUS,
    TAU_MINUS,
    TAU_PLUS,
    STDPSynapse,
)

# Timing offsets (ms) spanning both branches of the window, excluding the
# ambiguous coincident case (Delta t == 0).
DELTA_T_GRID = [-40.0, -30.0, -20.0, -15.0, -10.0, -5.0, -2.0,
                2.0, 5.0, 10.0, 15.0, 20.0, 30.0, 40.0]

# Agreement criterion (SPEC-013).
R2_THRESHOLD = 0.90


def _r_squared(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Coefficient of determination of ``y_pred`` against ``y_true``."""
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    ss_res = float(np.sum((y_true - y_pred) ** 2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    if ss_tot == 0.0:
        return 1.0 if ss_res == 0.0 else 0.0
    return 1.0 - ss_res / ss_tot


def _stdp_synapse_delta_w(delta_t_ms: float, dt: float = 1.0, pre_time: float = 60.0) -> float:
    """Weight change of :class:`STDPSynapse` for one pre/post pair.

    ``delta_t_ms = t_post - t_pre``. Weights are clamped well away from the
    saturating bounds so the response is the raw STDP increment.
    """
    syn = STDPSynapse(n_pre=1, n_post=1, weight_init=0.5, w_min=-2.0, w_max=2.0)
    post_time = pre_time + delta_t_ms
    duration = max(pre_time, post_time) + 60.0

    n_steps = int(round(duration / dt))
    for step in range(n_steps):
        t = step * dt
        pre_spike = abs(t - pre_time) < dt / 2
        post_spike = abs(t - post_time) < dt / 2
        syn.update(dt, pre_spikes=[pre_spike], post_spikes=[post_spike])

    return float(syn.weight_matrix[0, 0] - 0.5)


def _brian2_stdp_delta_w(delta_t_ms: float, pre_time: float = 60.0) -> float:
    """Brian2 ``Synapses`` STDP oracle for one pre/post pair."""
    from brian2 import Network, Synapses, SpikeGeneratorGroup, ms

    post_time = pre_time + delta_t_ms
    duration = max(pre_time, post_time) + 60.0

    pre = SpikeGeneratorGroup(1, [0], [pre_time] * ms)
    post = SpikeGeneratorGroup(1, [0], [max(post_time, 0.0)] * ms)

    synapses = Synapses(
        pre,
        post,
        model="""
        w : 1
        dapre/dt = -apre / taupre : 1 (event-driven)
        dapost/dt = -apost / taupost : 1 (event-driven)
        """,
        on_pre="""
        apre += Apre
        w = w + apost
        """,
        on_post="""
        apost += Apost
        w = w + apre
        """,
        namespace={
            "taupre": TAU_PLUS * ms,
            "taupost": TAU_MINUS * ms,
            "Apre": A_PLUS,
            "Apost": -A_MINUS,
        },
    )
    synapses.connect(i=0, j=0)
    synapses.w = 0.5

    net = Network(pre, post, synapses)
    net.run(duration * ms)
    return float(synapses.w[0]) - 0.5


def _analytic_delta_w(delta_t_ms: float) -> float:
    """Textbook exponential STDP window ``A+/-`` exp(-|dt|/tau)."""
    if delta_t_ms > 0:
        return A_PLUS * np.exp(-delta_t_ms / TAU_PLUS)
    return -A_MINUS * np.exp(delta_t_ms / TAU_MINUS)


# --- Curve shape: asymmetry (Bi & Poo 1998) ----------------------------------


def test_window_is_asymmetric_ltp_for_positive_dt():
    """Every pre-before-post pairing potentiates; every post-before-pre
    pairing depresses -- the defining asymmetry of the STDP window."""
    for dt in DELTA_T_GRID:
        dw = _stdp_synapse_delta_w(dt)
        if dt > 0:
            assert dw > 0, f"expected LTP at dt={dt}, got {dw}"
        else:
            assert dw < 0, f"expected LTD at dt={dt}, got {dw}"


def test_window_magnitude_decays_with_timing_distance():
    """On each branch the magnitude of the change shrinks monotonically as the
    spikes are separated further in time (exponential window)."""
    positive = sorted([dt for dt in DELTA_T_GRID if dt > 0])
    negative = sorted([dt for dt in DELTA_T_GRID if dt < 0], reverse=True)

    pos_mag = [abs(_stdp_synapse_delta_w(dt)) for dt in positive]
    neg_mag = [abs(_stdp_synapse_delta_w(dt)) for dt in negative]

    assert all(np.diff(pos_mag) < 0), f"LTP magnitudes not decreasing: {pos_mag}"
    assert all(np.diff(neg_mag) < 0), f"LTD magnitudes not decreasing: {neg_mag}"


# --- Quantitative agreement: R^2 > 0.90 (SPEC-013) ---------------------------


def test_stdp_curve_matches_brian2_oracle_r2():
    """The reconstructed ``Delta w(Delta t)`` curve agrees with the Brian2
    oracle with R^2 > 0.90 across the full window."""
    ours = np.array([_stdp_synapse_delta_w(dt) for dt in DELTA_T_GRID])
    oracle = np.array([_brian2_stdp_delta_w(dt) for dt in DELTA_T_GRID])

    r2 = _r_squared(oracle, ours)
    assert r2 > R2_THRESHOLD, f"R^2 vs Brian2 oracle = {r2:.4f} (<= {R2_THRESHOLD})"


def test_stdp_curve_matches_analytic_window_r2():
    """The curve also matches the analytic exponential STDP window
    ``A+/- exp(-|dt|/tau)`` with R^2 > 0.90."""
    ours = np.array([_stdp_synapse_delta_w(dt) for dt in DELTA_T_GRID])
    analytic = np.array([_analytic_delta_w(dt) for dt in DELTA_T_GRID])

    r2 = _r_squared(analytic, ours)
    assert r2 > R2_THRESHOLD, f"R^2 vs analytic window = {r2:.4f} (<= {R2_THRESHOLD})"


def test_ltp_branch_is_exponential_in_dt():
    """log|Delta w| is linear in Delta t on the LTP branch (an exponential
    decay), with the fitted time constant close to TAU_PLUS."""
    positive = sorted([dt for dt in DELTA_T_GRID if dt > 0])
    log_mag = np.log([_stdp_synapse_delta_w(dt) for dt in positive])

    # Linear fit log|dw| = log(A+) - dt / tau+  ->  slope = -1/tau+.
    slope, intercept = np.polyfit(positive, log_mag, 1)
    fitted = slope * np.array(positive) + intercept
    r2 = _r_squared(log_mag, fitted)
    assert r2 > R2_THRESHOLD, f"LTP branch log-linearity R^2 = {r2:.4f}"

    fitted_tau = -1.0 / slope
    assert fitted_tau == pytest.approx(TAU_PLUS, rel=0.15), (
        f"fitted tau+ = {fitted_tau:.2f} ms vs TAU_PLUS = {TAU_PLUS} ms"
    )
