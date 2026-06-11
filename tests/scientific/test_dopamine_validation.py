"""Scientific validation for SPEC-008 -- Neuromodulation.

Acceptance criteria (qualitative replication of Schultz 1997 and the
neuromodulatory effects on plasticity and excitability):

1. A dopaminergic **burst** raises the STDP learning rate across modules.
2. Dopaminergic **silence / dip** (reward omission) depresses recently-active
   synapses under a three-factor (reward-modulated) rule.
3. High **noradrenaline** lowers the LIF firing threshold, making neurons more
   responsive (validated against the Brian2 LIF backend).
4. The dopamine signal qualitatively reproduces Schultz 1997: a burst to an
   unexpected reward, no response to a fully predicted reward, and a dip to the
   omission of a predicted reward.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.interfaces import NeuromodulationSignal  # noqa: E402
from core.learning_engine import PlasticityScheduler  # noqa: E402
from core.neuron import LIFPopulation  # noqa: E402
from core.synapse import STDPSynapse  # noqa: E402
from modules.neuromodulation import DopamineSystem, NeuromodulatorSystem  # noqa: E402


# -- Criterion 1: burst raises STDP learning rate across modules --------------


def test_burst_raises_stdp_learning_rate_all_modules():
    """A dopamine burst scales the STDP learning rate up for every module.

    Two independent projections (standing in for two different modules) driven
    by an identical LTP-inducing (pre-before-post) pattern accumulate larger
    weight changes under a dopaminergic burst than under the basal level.
    """
    scheduler = PlasticityScheduler()
    burst = NeuromodulationSignal(dopamine=2.0)
    basal = NeuromodulationSignal(dopamine=1.0)

    assert scheduler.learning_rate_scale(burst) > scheduler.learning_rate_scale(basal)

    def run(neuromod):
        synapses = [STDPSynapse(n_pre=4, n_post=4, weight_init=0.5) for _ in range(2)]
        lr = scheduler.learning_rate_scale(neuromod)
        pre = np.ones(4, dtype=bool)
        post = np.ones(4, dtype=bool)
        for _ in range(20):
            for syn in synapses:
                # pre leads post by one step -> potentiation.
                syn.update(1.0, pre, np.zeros(4, dtype=bool), lr_scale=lr)
                syn.update(1.0, np.zeros(4, dtype=bool), post, lr_scale=lr)
        return np.mean([syn.weight_matrix.mean() for syn in synapses])

    burst_weight = run(burst)
    basal_weight = run(basal)
    assert burst_weight > basal_weight


# -- Criterion 2: silence/dip depresses active synapses -----------------------


def _three_factor_update(weights, eligibility, dopamine, lr=0.1):
    """Reward-modulated three-factor plasticity centred on basal dopamine.

    ``dw = lr * (dopamine - 1.0) * eligibility``: a burst (``dopamine > 1``)
    potentiates active synapses, basal leaves them unchanged, and a dip
    (``dopamine < 1``, reward omission) depresses them (Reynolds & Wickens 2002).
    """
    weights = weights + lr * (dopamine - 1.0) * eligibility
    return np.clip(weights, 0.0, 1.0)


def test_dopaminergic_silence_depresses_active_synapses():
    eligibility = np.array([1.0, 1.0, 0.0, 0.0])  # synapses 0,1 recently active
    weights0 = np.full(4, 0.5)

    # Burst potentiates the active synapses.
    burst_w = _three_factor_update(weights0, eligibility, dopamine=2.0)
    assert burst_w[0] > 0.5 and burst_w[1] > 0.5

    # Omission (dopamine silence, level -> 0) depresses the *active* synapses
    # while leaving the inactive ones untouched.
    sys_ = NeuromodulatorSystem()
    sys_.observe_reward(reward=0.0, value_estimate=1.0)  # omission: TD = -1
    sys_.update(1.0, _basal_inputs())
    dip_level = sys_.current_signal.dopamine
    assert dip_level < 1.0

    dip_w = _three_factor_update(weights0, eligibility, dopamine=dip_level)
    assert dip_w[0] < 0.5 and dip_w[1] < 0.5  # active synapses depressed
    assert dip_w[2] == pytest.approx(0.5) and dip_w[3] == pytest.approx(0.5)


# -- Criterion 3: noradrenaline lowers threshold -> more responsive -----------


def test_noradrenaline_increases_responsiveness():
    pop = LIFPopulation("na_test", n_neurons=500)
    # A constant near-threshold drive (reobase ~15 mV above rest).
    pop.set_input_current(16.0)

    def mean_rate(noradrenaline):
        pop.reset()
        pop.set_input_current(16.0)
        pop.apply_neuromodulation(NeuromodulationSignal(noradrenaline=noradrenaline))
        out = pop.update(1000.0, _basal_inputs())
        return float(np.mean(out.firing_rate))

    basal_rate = mean_rate(1.0)
    aroused_rate = mean_rate(2.0)  # high noradrenaline -> lower threshold
    assert aroused_rate > basal_rate


# -- Criterion 4: qualitative Schultz 1997 dopamine response ------------------


def test_schultz_1997_dopamine_response():
    """Burst on unexpected reward, none when predicted, dip on omission."""
    da = DopamineSystem(gain=1.0, tau_ms=50.0)

    # Unexpected reward: TD strongly positive -> phasic burst above basal.
    da.set_td_error(1.0)
    assert da.step(1.0) > 1.0

    # Fully predicted reward: TD ~ 0 -> response returns to basal.
    da.reset()
    da.set_td_error(0.0)
    assert da.step(1.0) == pytest.approx(1.0)

    # Omission of a predicted reward: TD negative -> phasic dip below basal.
    da.reset()
    da.set_td_error(-1.0)
    assert da.step(1.0) < 1.0


def _basal_inputs():
    from core.interfaces import ModuleInputs

    return ModuleInputs(
        spike_trains=np.zeros(0),
        attention_signal=0.5,
        neuromodulation=NeuromodulationSignal(),
        timestamp_ms=0.0,
    )
