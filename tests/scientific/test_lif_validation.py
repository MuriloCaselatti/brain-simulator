"""SPEC-003 -- Scientific validation (Brian2 as oracle).

This suite validates the LIF + STDP + TD-Learning implementation against
quantitative claims from the literature, using Brian2 directly as the
"ground truth" simulator (Brian2 *is* the runtime backing
:class:`~core.neuron.LIFPopulation`, so these tests exercise the same
integration machinery the module uses).

References:
    * Adrian (1926) -- cortical/sensory neuron firing rates fall in the
      ~10-100 Hz range for physiological drive.
    * Bi & Poo (1998) -- pairwise STDP produces an asymmetric LTP/LTD curve:
      pre-before-post potentiates, post-before-pre depresses, with magnitude
      decaying exponentially in |Delta t|.
    * Schultz (1997) -- the dopaminergic TD-error signal is positive when
      reward exceeds the value prediction.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.interfaces import ModuleInputs, NeuromodulationSignal  # noqa: E402
from core.learning_engine import LearningEngine  # noqa: E402
from core.neuron import MIN_NEURONS, V_REST, V_RESET, V_THRESH, LIFPopulation  # noqa: E402
from core.synapse import STDPSynapse  # noqa: E402

# Driving current (mV-equivalent) above the rheobase (V_THRESH - V_REST = 15mV).
PHYSIOLOGICAL_CURRENT_MV = 20.0
SUBTHRESHOLD_CURRENT_MV = 10.0


def _idle_inputs() -> ModuleInputs:
    return ModuleInputs(
        spike_trains=np.zeros(0),
        attention_signal=0.5,
        neuromodulation=NeuromodulationSignal(),
        timestamp_ms=0.0,
    )


# --- LIF firing rate (Adrian 1926) -----------------------------------------------------


def test_lif_firing_rate_within_biological_range():
    """A population driven by physiological current fires at 10-100 Hz."""
    pop = LIFPopulation("validation_pop", n_neurons=MIN_NEURONS)
    pop.set_input_current(PHYSIOLOGICAL_CURRENT_MV)

    outputs = pop.update(dt=1000.0, inputs=_idle_inputs())

    mean_rate = float(np.mean(outputs.firing_rate))
    assert 10.0 <= mean_rate <= 100.0, f"mean firing rate {mean_rate} Hz out of range"

    # The whole population is identical and identically driven, so individual
    # rates should agree closely with the population mean.
    assert np.allclose(outputs.firing_rate, mean_rate, rtol=0.2)


def test_lif_subthreshold_current_does_not_fire():
    """Current below rheobase (V_THRESH - V_REST = 15mV) never reaches threshold."""
    pop = LIFPopulation("subthreshold_pop", n_neurons=MIN_NEURONS)
    pop.set_input_current(SUBTHRESHOLD_CURRENT_MV)

    outputs = pop.update(dt=500.0, inputs=_idle_inputs())

    assert np.all(outputs.firing_rate == 0.0)
    assert np.all(outputs.spike_trains == 0.0)


# --- All-or-none law -----------------------------------------------------------------------


def test_all_or_none_law():
    """Spike output is binary and the reset potential is independent of drive
    strength -- the hallmark of the all-or-none action potential law."""
    pop_weak = LIFPopulation("aon_weak", n_neurons=MIN_NEURONS)
    pop_strong = LIFPopulation("aon_strong", n_neurons=MIN_NEURONS)

    pop_weak.set_input_current(PHYSIOLOGICAL_CURRENT_MV)
    pop_strong.set_input_current(PHYSIOLOGICAL_CURRENT_MV * 2)

    out_weak = pop_weak.update(dt=200.0, inputs=_idle_inputs())
    out_strong = pop_strong.update(dt=200.0, inputs=_idle_inputs())

    # Spike trains are strictly binary regardless of drive amplitude.
    assert set(np.unique(out_weak.spike_trains)).issubset({0.0, 1.0})
    assert set(np.unique(out_strong.spike_trains)).issubset({0.0, 1.0})

    # Both populations spike (suprathreshold), confirming the stronger drive
    # doesn't change the *kind* of response, only its frequency.
    assert out_weak.firing_rate.mean() > 0
    assert out_strong.firing_rate.mean() > 0
    assert out_strong.firing_rate.mean() > out_weak.firing_rate.mean()

    # Membrane potential always resets to V_RESET, never overshoots/undershoots
    # proportionally to the input current.
    state_weak = pop_weak.get_state()
    state_strong = pop_strong.get_state()
    assert np.all(state_weak.voltage <= V_THRESH + 1e-6)
    assert np.all(state_strong.voltage <= V_THRESH + 1e-6)
    assert np.all(state_weak.voltage >= V_RESET - 1e-6)
    assert np.all(state_strong.voltage >= V_RESET - 1e-6)


# --- STDP vs. Brian2 oracle (Bi & Poo 1998) ----------------------------------------------


def _stdp_synapse_delta_w(delta_t_ms: float, dt: float = 1.0, pre_time: float = 20.0) -> float:
    """Run :class:`STDPSynapse` with a single pre/post spike pair separated by
    ``delta_t_ms = t_post - t_pre`` and return the resulting weight change."""
    syn = STDPSynapse(n_pre=1, n_post=1, weight_init=0.5, w_min=-1.0, w_max=2.0)
    post_time = pre_time + delta_t_ms
    duration = max(pre_time, post_time) + 40.0

    n_steps = int(round(duration / dt))
    for step in range(n_steps):
        t = step * dt
        pre_spike = abs(t - pre_time) < dt / 2
        post_spike = abs(t - post_time) < dt / 2
        syn.update(dt, pre_spikes=[pre_spike], post_spikes=[post_spike])

    return float(syn.weight_matrix[0, 0] - 0.5)


def _brian2_stdp_delta_w(delta_t_ms: float, pre_time: float = 20.0) -> float:
    """Brian2 ``Synapses`` STDP oracle for a single pre/post spike pair.

    Implements the textbook trace-based STDP rule (same equations our
    :class:`STDPSynapse` follows numerically) directly in Brian2.
    """
    from brian2 import Network, Synapses, SpikeGeneratorGroup, ms

    from core.synapse import A_MINUS, A_PLUS, TAU_MINUS, TAU_PLUS

    post_time = pre_time + delta_t_ms
    duration = max(pre_time, post_time) + 40.0

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


@pytest.mark.parametrize("delta_t_ms", [5.0, 15.0])
def test_stdp_pre_before_post_potentiates(delta_t_ms):
    """Bi & Poo 1998: pre-before-post (Delta t > 0) -> LTP (Delta w > 0)."""
    dw_synapse = _stdp_synapse_delta_w(delta_t_ms)
    dw_oracle = _brian2_stdp_delta_w(delta_t_ms)

    assert dw_synapse > 0
    assert dw_oracle > 0


@pytest.mark.parametrize("delta_t_ms", [-5.0, -15.0])
def test_stdp_post_before_pre_depresses(delta_t_ms):
    """Bi & Poo 1998: post-before-pre (Delta t < 0) -> LTD (Delta w < 0)."""
    dw_synapse = _stdp_synapse_delta_w(delta_t_ms)
    dw_oracle = _brian2_stdp_delta_w(delta_t_ms)

    assert dw_synapse < 0
    assert dw_oracle < 0


def test_stdp_curve_decays_with_timing_distance():
    """The magnitude of the STDP weight change decays with |Delta t|,
    consistent with the exponential STDP window of Bi & Poo (1998)."""
    dw_close = _stdp_synapse_delta_w(5.0)
    dw_far = _stdp_synapse_delta_w(15.0)

    assert abs(dw_close) > abs(dw_far)

    oracle_close = _brian2_stdp_delta_w(5.0)
    oracle_far = _brian2_stdp_delta_w(15.0)

    assert abs(oracle_close) > abs(oracle_far)


def test_stdp_synapse_matches_brian2_oracle_qualitatively():
    """Our vectorized STDPSynapse agrees in sign and rough magnitude with the
    Brian2 reference implementation across a range of timing offsets."""
    for delta_t_ms in [-15.0, -5.0, 5.0, 15.0]:
        dw_synapse = _stdp_synapse_delta_w(delta_t_ms)
        dw_oracle = _brian2_stdp_delta_w(delta_t_ms)

        assert np.sign(dw_synapse) == np.sign(dw_oracle)
        assert dw_synapse == pytest.approx(dw_oracle, abs=2e-3)


# --- TD-error sign (Schultz 1997) ---------------------------------------------------------


def test_td_error_positive_when_reward_exceeds_expectation():
    engine = LearningEngine()
    engine.value_estimate = 0.0

    td_error = engine.compute_td_error(reward=1.0, value_next=0.0)

    assert td_error > 0


def test_td_error_zero_when_reward_matches_expectation():
    engine = LearningEngine(gamma=0.0)
    engine.value_estimate = 1.0

    td_error = engine.compute_td_error(reward=1.0, value_next=0.0)

    assert td_error == pytest.approx(0.0)
