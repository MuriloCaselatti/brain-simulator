"""Tests for SPEC-005 -- DAN, VAN and SaliencyMap.

Covers the :class:`~core.interfaces.CognitiveModule` contract for each
module and the SPEC-005 acceptance criteria:

* DAN amplifies a target representation >= 2x vs. distractors.
* VAN interrupts (within a single dt=1ms tick, well under 20ms simulated)
  for high-saliency events.
* DAN-VAN anticorrelation: each module's activation suppresses the other.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.interfaces import (  # noqa: E402
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
)
from modules.attention.dan import DAN, DEFAULT_GAIN_AMPLIFICATION  # noqa: E402
from modules.attention.saliency import SaliencyMap  # noqa: E402
from modules.attention.van import VAN, DEFAULT_INTERRUPT_THRESHOLD  # noqa: E402

N = 8


def make_inputs(spike_trains, attention_signal=1.0, neuromodulation=None, timestamp_ms=0.0):
    return ModuleInputs(
        spike_trains=np.asarray(spike_trains, dtype=float),
        attention_signal=attention_signal,
        neuromodulation=neuromodulation or NeuromodulationSignal(),
        timestamp_ms=timestamp_ms,
    )


# --- SaliencyMap ---------------------------------------------------------------------


def test_saliency_map_is_cognitive_module():
    sm = SaliencyMap("saliency", n_neurons=N)
    assert isinstance(sm, CognitiveModule)
    assert sm.module_id == "saliency"
    assert sm.n_neurons == N
    assert sm.get_synaptic_targets() == []


def test_saliency_map_update_returns_correct_shapes():
    sm = SaliencyMap("saliency", n_neurons=N)
    activity = np.zeros(N)
    activity[3] = 1.0

    outputs = sm.update(dt=1.0, inputs=make_inputs(activity))

    assert isinstance(outputs, ModuleOutputs)
    assert outputs.spike_trains.shape == (N,)
    assert outputs.firing_rate.shape == (N,)
    assert np.all(outputs.spike_trains >= 0.0)
    assert np.all(outputs.spike_trains <= 1.0)


def test_saliency_map_flags_novel_or_contrasting_location_as_most_salient():
    sm = SaliencyMap("saliency", n_neurons=N)

    # Constant background for several ticks (becomes the running average).
    background = np.full(N, 0.2)
    for _ in range(20):
        sm.update(dt=1.0, inputs=make_inputs(background))

    # A single location suddenly spikes much higher -- should dominate saliency.
    novel = background.copy()
    novel[5] = 1.0
    outputs = sm.update(dt=1.0, inputs=make_inputs(novel))

    assert outputs.internal_state["max_saliency_index"] == 5
    assert outputs.internal_state["max_saliency"] == pytest.approx(1.0)


def test_saliency_map_noradrenaline_increases_sensitivity():
    sm_base = SaliencyMap("saliency_base", n_neurons=N, salience_threshold=0.9)
    sm_aroused = SaliencyMap("saliency_aroused", n_neurons=N, salience_threshold=0.9)
    sm_aroused.apply_neuromodulation(NeuromodulationSignal(noradrenaline=2.0))

    activity = np.zeros(N)
    activity[2] = 1.0

    out_base = sm_base.update(dt=1.0, inputs=make_inputs(activity))
    out_aroused = sm_aroused.update(dt=1.0, inputs=make_inputs(activity))

    # Both are normalized to a max of 1.0, but the aroused map's raw
    # (pre-normalization) saliency should be higher -- check via the gain
    # applied internally.
    assert sm_aroused._noradrenaline_gain > sm_base._noradrenaline_gain
    assert out_base.internal_state["max_saliency"] == pytest.approx(1.0)
    assert out_aroused.internal_state["max_saliency"] == pytest.approx(1.0)


def test_saliency_map_reset_clears_running_average():
    sm = SaliencyMap("saliency", n_neurons=N)
    sm.update(dt=1.0, inputs=make_inputs(np.full(N, 1.0)))
    assert np.any(sm._running_avg != 0.0)

    sm.reset()

    assert np.all(sm._running_avg == 0.0)
    assert np.all(sm._saliency_map == 0.0)
    assert sm._noradrenaline_gain == 1.0


def test_saliency_map_get_state():
    sm = SaliencyMap("saliency", n_neurons=N)
    activity = np.zeros(N)
    activity[1] = 1.0
    sm.update(dt=1.0, inputs=make_inputs(activity, timestamp_ms=42.0))

    state = sm.get_state()

    assert isinstance(state, ModuleState)
    assert state.n_neurons == N
    assert state.timestamp_ms == 42.0
    assert state.metadata["max_saliency_index"] == 1


# --- DAN -------------------------------------------------------------------------------


def test_dan_is_cognitive_module():
    dan = DAN("dan", n_neurons=N)
    assert isinstance(dan, CognitiveModule)
    assert dan.module_id == "dan"
    assert dan.n_neurons == N
    assert dan.get_synaptic_targets() == []


def test_dan_amplifies_target_at_least_2x_vs_distractors():
    dan = DAN("dan", n_neurons=N)

    pfc_signal = np.zeros(N)
    target_idx = 3
    pfc_signal[target_idx] = 1.0  # full top-down drive at the target location

    outputs = dan.update(dt=1.0, inputs=make_inputs(pfc_signal))

    gain_map = outputs.internal_state["gain_map"]
    target_gain = gain_map[target_idx]
    distractor_gain = gain_map[0]

    assert distractor_gain == pytest.approx(dan.baseline_gain)
    assert target_gain >= 2.0 * distractor_gain
    assert target_gain == pytest.approx(
        dan.baseline_gain + DEFAULT_GAIN_AMPLIFICATION
    )


def test_dan_publishes_attention_signal_in_unit_range():
    dan = DAN("dan", n_neurons=N)
    pfc_signal = np.zeros(N)
    pfc_signal[0] = 1.0

    outputs = dan.update(dt=1.0, inputs=make_inputs(pfc_signal))

    assert 0.0 <= outputs.internal_state["attention_signal"] <= 1.0
    assert outputs.internal_state["dan_focus"] == pytest.approx(dan.dan_focus)


def test_dan_acetylcholine_scales_gain():
    dan = DAN("dan", n_neurons=N)
    dan.apply_neuromodulation(NeuromodulationSignal(acetylcholine=0.0))

    pfc_signal = np.zeros(N)
    pfc_signal[0] = 1.0
    outputs = dan.update(dt=1.0, inputs=make_inputs(pfc_signal))

    # No acetylcholine -> no top-down amplification, gain falls back to baseline.
    assert np.allclose(outputs.internal_state["gain_map"], dan.baseline_gain)


def test_dan_van_activation_suppresses_top_down_gain():
    dan = DAN("dan", n_neurons=N, van_suppression_strength=1.0)
    dan.set_van_activation(1.0)  # full bottom-up interrupt

    pfc_signal = np.zeros(N)
    pfc_signal[0] = 1.0
    outputs = dan.update(dt=1.0, inputs=make_inputs(pfc_signal))

    assert np.allclose(outputs.internal_state["gain_map"], dan.baseline_gain)
    assert outputs.internal_state["dan_focus"] == pytest.approx(0.0)


def test_dan_reset():
    dan = DAN("dan", n_neurons=N)
    dan.set_van_activation(1.0)
    pfc_signal = np.full(N, 1.0)
    dan.update(dt=1.0, inputs=make_inputs(pfc_signal))

    dan.reset()

    assert np.allclose(dan.gain_map, dan.baseline_gain)
    assert dan.dan_focus == 0.0
    assert dan._van_activation == 0.0


# --- VAN -------------------------------------------------------------------------------


def test_van_is_cognitive_module():
    van = VAN("van", n_neurons=N)
    assert isinstance(van, CognitiveModule)
    assert van.module_id == "van"
    assert van.n_neurons == N
    assert van.get_synaptic_targets() == []


def test_van_interrupts_within_one_tick_for_high_saliency():
    van = VAN("van", n_neurons=N, interrupt_threshold=DEFAULT_INTERRUPT_THRESHOLD)

    saliency = np.zeros(N)
    saliency[6] = 1.0  # well above the default 0.7 threshold

    outputs = van.update(dt=1.0, inputs=make_inputs(saliency))

    # SPEC-005: interrupt must be raised within < 20ms simulated -- here it
    # is decided synchronously within a single dt=1ms tick.
    assert outputs.internal_state["interrupt"] is True
    assert outputs.internal_state["interrupt_location"] == 6
    assert outputs.spike_trains[6] == 1.0
    assert "attention_signal" in outputs.internal_state


def test_van_does_not_interrupt_for_low_saliency():
    van = VAN("van", n_neurons=N, interrupt_threshold=DEFAULT_INTERRUPT_THRESHOLD)

    saliency = np.full(N, 0.1)
    outputs = van.update(dt=1.0, inputs=make_inputs(saliency))

    assert outputs.internal_state["interrupt"] is False
    assert outputs.internal_state["interrupt_location"] == -1
    assert "attention_signal" not in outputs.internal_state
    assert np.all(outputs.spike_trains == 0.0)


def test_van_dan_suppression_raises_effective_threshold():
    van = VAN("van", n_neurons=N, interrupt_threshold=0.5, dan_suppression_strength=1.0)

    saliency = np.zeros(N)
    saliency[0] = 0.7  # would interrupt at the base threshold of 0.5

    # Without DAN suppression -- interrupts.
    out_unsuppressed = van.update(dt=1.0, inputs=make_inputs(saliency))
    assert out_unsuppressed.internal_state["interrupt"] is True

    # A strongly engaged DAN raises the threshold above the saliency level.
    van.set_dan_suppression(1.0)  # threshold becomes 0.5 + 1.0 = 1.5
    out_suppressed = van.update(dt=1.0, inputs=make_inputs(saliency))
    assert out_suppressed.internal_state["interrupt"] is False


def test_van_acetylcholine_lowers_effective_threshold():
    van = VAN("van", n_neurons=N, interrupt_threshold=0.7)
    base_threshold = van.effective_threshold

    van.apply_neuromodulation(NeuromodulationSignal(acetylcholine=2.0))

    assert van.effective_threshold < base_threshold


def test_van_reset():
    van = VAN("van", n_neurons=N)
    saliency = np.zeros(N)
    saliency[0] = 1.0
    van.update(dt=1.0, inputs=make_inputs(saliency))
    van.set_dan_suppression(0.5)
    assert van.interrupt is True

    van.reset()

    assert van.interrupt is False
    assert van.interrupt_location == -1
    assert van.van_activation == 0.0
    assert van._dan_focus == 0.0


# --- DAN-VAN anticorrelation integration ----------------------------------------------


def test_dan_van_anticorrelation_round_trip():
    dan = DAN("dan", n_neurons=N)
    van = VAN("van", n_neurons=N, interrupt_threshold=0.5, dan_suppression_strength=0.3)

    # 1. DAN focuses strongly on a target -> high dan_focus.
    pfc_signal = np.zeros(N)
    pfc_signal[0] = 1.0
    dan_outputs = dan.update(dt=1.0, inputs=make_inputs(pfc_signal))
    assert dan_outputs.internal_state["dan_focus"] > 0.5

    # 2. VAN reads DAN's focus and becomes less reflexive to a moderate
    #    saliency event.
    van.set_dan_suppression(dan_outputs.internal_state["dan_focus"])
    moderate_saliency = np.zeros(N)
    moderate_saliency[3] = 0.6
    van_outputs = van.update(dt=1.0, inputs=make_inputs(moderate_saliency))
    assert van_outputs.internal_state["interrupt"] is False

    # 3. A very high saliency event still gets through and VAN activates.
    high_saliency = np.zeros(N)
    high_saliency[3] = 1.0
    van_outputs = van.update(dt=1.0, inputs=make_inputs(high_saliency))
    assert van_outputs.internal_state["interrupt"] is True
    assert van_outputs.internal_state["van_activation"] > 0.0

    # 4. DAN reads VAN's activation back and its top-down gain is suppressed.
    dan.set_van_activation(van_outputs.internal_state["van_activation"])
    dan_outputs = dan.update(dt=1.0, inputs=make_inputs(pfc_signal))
    assert dan_outputs.internal_state["dan_focus"] < 0.5
