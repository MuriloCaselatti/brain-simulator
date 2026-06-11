"""Contract tests for the frozen SPEC-001 interface.

These tests pin the public surface of :mod:`core.interfaces`. A failure here
means the frozen :class:`CognitiveModule` contract -- on which every downstream
SPEC depends -- has been altered and requires an ADR.
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


class MockCognitiveModule(CognitiveModule):
    """Minimal, dependency-free module implementing the full contract."""

    def __init__(self, module_id: str, n_neurons: int = 100):
        super().__init__(module_id, n_neurons)
        self._voltage = np.full(n_neurons, -70.0)
        self._firing_rate = np.zeros(n_neurons)
        self._learning_rate = 1.0
        self._weights = np.full((n_neurons, n_neurons), 0.5)

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        spikes = np.zeros(self.n_neurons)
        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=self._firing_rate.copy(),
            internal_state={"dt": dt, "attention": inputs.attention_signal},
        )

    def get_state(self) -> ModuleState:
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=self._voltage.copy(),
            firing_rate=self._firing_rate.copy(),
            mean_weight=float(self._weights.mean()),
            active_synapses=int(self._weights.size),
            timestamp_ms=0.0,
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        self._learning_rate = signal.dopamine

    def get_synaptic_targets(self):
        return [
            SynapticTarget(
                source_module=self.module_id,
                target_module=self.module_id,
                weight_matrix=self._weights,
                synapse_type="excitatory",
            )
        ]

    def reset(self) -> None:
        self._voltage[:] = -70.0
        self._firing_rate[:] = 0.0
        self._learning_rate = 1.0


@pytest.fixture
def inputs() -> ModuleInputs:
    return ModuleInputs(
        spike_trains=np.zeros(50),
        attention_signal=1.0,
        neuromodulation=NeuromodulationSignal(),
        timestamp_ms=0.0,
    )


# --- Construction & identity -------------------------------------------------

def test_mock_module_implements_contract():
    module = MockCognitiveModule("test_module", n_neurons=100)
    assert module.module_id == "test_module"
    assert module.n_neurons == 100
    assert isinstance(module, CognitiveModule)


def test_abc_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        CognitiveModule("x", 10)  # type: ignore[abstract]


def test_incomplete_implementation_is_rejected():
    class Incomplete(CognitiveModule):
        def update(self, dt, inputs):  # missing the other abstract methods
            return ModuleOutputs(np.zeros(1), np.zeros(1))

    with pytest.raises(TypeError):
        Incomplete("partial", 10)  # type: ignore[abstract]


# --- update() ----------------------------------------------------------------

def test_update_returns_correct_types():
    module = MockCognitiveModule("test", n_neurons=50)
    inputs = ModuleInputs(
        spike_trains=np.zeros(50),
        attention_signal=1.0,
        neuromodulation=NeuromodulationSignal(),
        timestamp_ms=0.0,
    )
    outputs = module.update(dt=1.0, inputs=inputs)
    assert isinstance(outputs, ModuleOutputs)
    assert outputs.spike_trains.shape == (50,)
    assert outputs.firing_rate.shape == (50,)
    assert isinstance(outputs.internal_state, dict)


# --- get_state() -------------------------------------------------------------

def test_get_state_returns_module_state():
    module = MockCognitiveModule("hippocampus", n_neurons=200)
    state = module.get_state()
    assert isinstance(state, ModuleState)
    assert state.module_id == "hippocampus"
    assert state.n_neurons == 200
    assert state.voltage.shape == (200,)
    assert state.firing_rate.shape == (200,)
    assert isinstance(state.mean_weight, float)
    assert isinstance(state.active_synapses, int)


# --- apply_neuromodulation() -------------------------------------------------

def test_apply_neuromodulation_mutates_module():
    module = MockCognitiveModule("vta", n_neurons=20)
    module.apply_neuromodulation(NeuromodulationSignal(dopamine=1.8))
    assert module._learning_rate == 1.8


def test_neuromodulation_signal_defaults():
    signal = NeuromodulationSignal()
    assert signal.dopamine == 1.0  # basal
    assert signal.noradrenaline == 1.0
    assert signal.acetylcholine == 1.0


# --- get_synaptic_targets() --------------------------------------------------

def test_get_synaptic_targets_returns_targets():
    module = MockCognitiveModule("ca3", n_neurons=30)
    targets = module.get_synaptic_targets()
    assert isinstance(targets, list)
    assert all(isinstance(t, SynapticTarget) for t in targets)
    target = targets[0]
    assert target.weight_matrix.shape == (30, 30)
    assert target.synapse_type in ("excitatory", "inhibitory")


# --- reset() -----------------------------------------------------------------

def test_reset_restores_initial_state():
    module = MockCognitiveModule("pfc", n_neurons=100)
    module._voltage[:] = -50.0
    module._learning_rate = 0.1
    module.reset()
    assert np.all(module._voltage == -70.0)
    assert module._learning_rate == 1.0


# --- Data contracts ----------------------------------------------------------

def test_module_inputs_defaults():
    mi = ModuleInputs(spike_trains=np.zeros(5), attention_signal=0.5)
    assert isinstance(mi.neuromodulation, NeuromodulationSignal)
    assert mi.timestamp_ms == 0.0


def test_module_outputs_defaults_internal_state():
    mo = ModuleOutputs(spike_trains=np.zeros(5), firing_rate=np.zeros(5))
    assert mo.internal_state == {}


def test_repr_contains_id_and_size():
    module = MockCognitiveModule("amygdala", n_neurons=50)
    text = repr(module)
    assert "amygdala" in text
    assert "50" in text


# --- The exact acceptance scenario from SPEC-001 -----------------------------

def test_spec001_acceptance_scenario(inputs):
    module = MockCognitiveModule("test", n_neurons=100)
    outputs = module.update(dt=1.0, inputs=inputs)
    assert isinstance(outputs, ModuleOutputs)
    state = module.get_state()
    assert isinstance(state, ModuleState)
    assert state.n_neurons == 100
