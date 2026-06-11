"""Tests for SPEC-008 -- Neuromodulation.

Covers the three channels (dopamine / noradrenaline / acetylcholine), the
:class:`~core.interfaces.CognitiveModule` contract of
:class:`~modules.neuromodulation.system.NeuromodulatorSystem`, and the global
broadcast wired into the :class:`~core.simulation_engine.SimulationEngine`.

The Schultz 1997 dopamine-response criterion is validated separately in
``tests/scientific/test_dopamine_validation.py``.
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
    SynapticTarget,
)
from core.simulation_engine import SimulationEngine  # noqa: E402
from modules.neuromodulation import (  # noqa: E402
    AcetylcholineSystem,
    DopamineSystem,
    NeuromodulatorSystem,
    NoradrenalineSystem,
)


def make_inputs(attention_signal=0.5, neuromodulation=None, timestamp_ms=0.0):
    return ModuleInputs(
        spike_trains=np.zeros(0),
        attention_signal=attention_signal,
        neuromodulation=neuromodulation or NeuromodulationSignal(),
        timestamp_ms=timestamp_ms,
    )


# -- DopamineSystem -----------------------------------------------------------


def test_dopamine_basal_when_no_drive():
    da = DopamineSystem()
    assert da.step(1.0) == pytest.approx(1.0)


def test_dopamine_positive_td_error_is_burst():
    da = DopamineSystem(gain=1.0)
    da.set_td_error(0.5)
    level = da.step(1.0)
    assert level > 1.0
    assert da.is_burst and not da.is_dip


def test_dopamine_negative_td_error_is_dip():
    da = DopamineSystem(gain=1.0)
    da.set_td_error(-0.5)
    level = da.step(1.0)
    assert level < 1.0
    assert da.is_dip and not da.is_burst


def test_dopamine_zero_td_error_is_basal():
    da = DopamineSystem(gain=1.0)
    da.set_td_error(0.0)
    assert da.step(1.0) == pytest.approx(1.0)


def test_dopamine_is_clamped():
    da = DopamineSystem(gain=10.0)
    da.set_td_error(5.0)
    assert da.step(1.0) == pytest.approx(2.0)
    da.set_td_error(-5.0)
    assert da.step(1.0) == pytest.approx(0.0)


def test_dopamine_phasic_decays_to_basal():
    da = DopamineSystem(gain=1.0, tau_ms=10.0)
    da.set_td_error(1.0)
    da.step(1.0)
    # After many tau the drive has decayed and dopamine returns to basal.
    for _ in range(200):
        da.step(1.0)
    assert da.level == pytest.approx(1.0, abs=1e-3)


# -- NoradrenalineSystem ------------------------------------------------------


def test_noradrenaline_basal_at_zero_arousal():
    na = NoradrenalineSystem()
    assert na.step(1.0) == pytest.approx(1.0)


def test_noradrenaline_high_arousal_above_basal():
    na = NoradrenalineSystem(gain=1.0)
    na.set_arousal(1.0)
    assert na.step(1.0) == pytest.approx(2.0)


def test_noradrenaline_clamps_arousal_input():
    na = NoradrenalineSystem(gain=1.0)
    na.set_arousal(5.0)
    assert na.step(1.0) == pytest.approx(2.0)


# -- AcetylcholineSystem ------------------------------------------------------


def test_acetylcholine_neutral_attention_is_basal():
    ach = AcetylcholineSystem()
    ach.set_attention(0.5)
    assert ach.step(1.0) == pytest.approx(1.0)


def test_acetylcholine_high_attention_raises_level():
    ach = AcetylcholineSystem(attention_gain=1.0)
    ach.set_attention(1.0)
    assert ach.step(1.0) > 1.0


def test_acetylcholine_low_attention_lowers_level():
    ach = AcetylcholineSystem(attention_gain=1.0)
    ach.set_attention(0.0)
    assert ach.step(1.0) < 1.0


def test_acetylcholine_uncertainty_adds_drive():
    ach = AcetylcholineSystem(attention_gain=1.0, uncertainty_gain=0.5)
    ach.set_attention(0.5)
    ach.set_uncertainty(1.0)
    assert ach.step(1.0) == pytest.approx(1.5)


# -- NeuromodulatorSystem: CognitiveModule contract ---------------------------


def test_system_is_cognitive_module():
    sys_ = NeuromodulatorSystem()
    assert isinstance(sys_, CognitiveModule)
    assert sys_.n_neurons == 0


def test_system_update_returns_outputs():
    sys_ = NeuromodulatorSystem()
    out = sys_.update(1.0, make_inputs())
    assert isinstance(out, ModuleOutputs)
    for key in ("dopamine", "noradrenaline", "acetylcholine"):
        assert key in out.internal_state


def test_system_get_state():
    sys_ = NeuromodulatorSystem()
    sys_.update(1.0, make_inputs(timestamp_ms=7.0))
    state = sys_.get_state()
    assert isinstance(state, ModuleState)
    assert state.timestamp_ms == 7.0


def test_system_get_synaptic_targets_empty():
    assert NeuromodulatorSystem().get_synaptic_targets() == []


def test_system_apply_neuromodulation_is_noop():
    sys_ = NeuromodulatorSystem()
    sys_.apply_neuromodulation(NeuromodulationSignal(dopamine=2.0))
    # Source, not a sink: its own level is unaffected by an external signal.
    assert sys_.current_signal.dopamine == pytest.approx(1.0)


def test_system_current_signal_reflects_channels():
    sys_ = NeuromodulatorSystem()
    sys_.set_td_error(0.5)
    sys_.set_arousal(1.0)
    sys_.set_attention(1.0)
    sys_.update(1.0, make_inputs())
    sig = sys_.current_signal
    assert sig.dopamine > 1.0
    assert sig.noradrenaline > 1.0
    assert sig.acetylcholine > 1.0


def test_system_default_attention_from_inputs():
    sys_ = NeuromodulatorSystem()
    sys_.update(1.0, make_inputs(attention_signal=1.0))
    # No explicit set_attention -> ACh tracks inputs.attention_signal.
    assert sys_.current_signal.acetylcholine > 1.0


def test_system_observe_reward_computes_td_error():
    sys_ = NeuromodulatorSystem()
    td = sys_.observe_reward(reward=1.0, value_estimate=0.0)
    assert td == pytest.approx(1.0)
    sys_.update(1.0, make_inputs())
    assert sys_.current_signal.dopamine > 1.0


def test_system_reset():
    sys_ = NeuromodulatorSystem()
    sys_.set_td_error(1.0)
    sys_.set_arousal(1.0)
    sys_.update(1.0, make_inputs())
    sys_.reset()
    sig = sys_.current_signal
    assert sig.dopamine == pytest.approx(1.0)
    assert sig.noradrenaline == pytest.approx(1.0)
    assert sig.acetylcholine == pytest.approx(1.0)


def test_system_connect_learning_engine_pulls_td_error():
    class FakeEngine:
        last_td_error = 0.8

    sys_ = NeuromodulatorSystem()
    sys_.connect_learning_engine(FakeEngine())
    sys_.update(1.0, make_inputs())
    assert sys_.current_signal.dopamine > 1.0
    assert sys_.get_state().metadata["td_error"] == pytest.approx(0.8)


# -- SimulationEngine integration ---------------------------------------------


class _RecordingModule(CognitiveModule):
    """Minimal module that records the last neuromodulation it was given."""

    def __init__(self, module_id="rec"):
        super().__init__(module_id, n_neurons=1)
        self.last_applied = NeuromodulationSignal()
        self.last_input = NeuromodulationSignal()

    def update(self, dt, inputs):
        self.last_input = inputs.neuromodulation
        return ModuleOutputs(spike_trains=np.zeros(1), firing_rate=np.zeros(1))

    def get_state(self):
        return ModuleState(self.module_id, 1, np.zeros(1), np.zeros(1), 0.0, 0, 0.0)

    def apply_neuromodulation(self, signal):
        self.last_applied = signal

    def get_synaptic_targets(self):
        return []

    def reset(self):
        self.last_applied = NeuromodulationSignal()
        self.last_input = NeuromodulationSignal()


def test_engine_register_neuromodulator_validates():
    engine = SimulationEngine()
    with pytest.raises(ValueError):
        engine.register_neuromodulator("missing")
    engine.add_module(_RecordingModule("rec"))
    with pytest.raises(ValueError):
        engine.register_neuromodulator("rec")  # no current_signal


def test_engine_broadcasts_neuromodulation_next_tick():
    engine = SimulationEngine()
    rec = _RecordingModule("rec")
    nm = NeuromodulatorSystem("neuromodulators")
    engine.add_module(rec)
    engine.add_module(nm, depends_on=["rec"])
    engine.register_neuromodulator("neuromodulators")

    nm.set_td_error(1.0)
    nm.set_arousal(1.0)

    # Tick 1: signal emitted by nm at end of tick; engine refreshes for next.
    engine.step()
    assert engine.neuromodulation.dopamine > 1.0

    # Tick 2: the elevated signal is applied to every module.
    engine.step()
    assert rec.last_applied.dopamine > 1.0
    assert rec.last_input.dopamine > 1.0


def test_engine_without_neuromodulator_stays_basal():
    engine = SimulationEngine()
    rec = _RecordingModule("rec")
    engine.add_module(rec)
    engine.step()
    # apply_neuromodulation is not invoked when no neuromodulator is registered.
    assert rec.last_applied.dopamine == pytest.approx(1.0)
    assert engine.neuromodulation.dopamine == pytest.approx(1.0)
