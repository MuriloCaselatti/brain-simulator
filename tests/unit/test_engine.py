"""Tests for SPEC-002 -- BrainBus + SimulationEngine.

Pins the synchronous, topologically-ordered TimeLoop on top of the frozen
SPEC-001 :class:`~core.interfaces.CognitiveModule` contract.
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.brain_bus import BrainBus, BusEvent, BusSnapshot  # noqa: E402
from core.interfaces import (  # noqa: E402
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    ModuleState,
    NeuromodulationSignal,
    SynapticTarget,
)
from core.simulation_engine import SimulationEngine  # noqa: E402


class MockModule(CognitiveModule):
    """Minimal mock module that records calls and emits a fixed-size spike train."""

    def __init__(self, module_id: str, n_neurons: int = 4, attention_signal=None):
        super().__init__(module_id, n_neurons)
        self._attention_signal = attention_signal
        self.update_calls = []
        self.reset_calls = 0
        self.applied_signals = []
        self._weights = np.full((n_neurons, n_neurons), 0.5)

    def update(self, dt: float, inputs: ModuleInputs) -> ModuleOutputs:
        self.update_calls.append(inputs)
        spikes = np.ones(self.n_neurons)
        internal_state = {"received_pre": int(inputs.spike_trains.size)}
        if self._attention_signal is not None:
            internal_state["attention_signal"] = self._attention_signal
        return ModuleOutputs(
            spike_trains=spikes,
            firing_rate=spikes * 10.0,
            internal_state=internal_state,
        )

    def get_state(self) -> ModuleState:
        return ModuleState(
            module_id=self.module_id,
            n_neurons=self.n_neurons,
            voltage=np.full(self.n_neurons, -70.0),
            firing_rate=np.zeros(self.n_neurons),
            mean_weight=float(self._weights.mean()),
            active_synapses=int(self._weights.size),
            timestamp_ms=0.0,
        )

    def apply_neuromodulation(self, signal: NeuromodulationSignal) -> None:
        self.applied_signals.append(signal)

    def get_synaptic_targets(self):
        return [
            SynapticTarget(
                source_module=self.module_id,
                target_module=self.module_id,
                weight_matrix=self._weights,
            )
        ]

    def reset(self) -> None:
        self.reset_calls += 1
        self.update_calls = []


# --- BrainBus ------------------------------------------------------------


def test_publish_notifies_subscribers_synchronously():
    bus = BrainBus()
    received = []
    bus.subscribe("spike", lambda event: received.append(event))

    event = BusEvent(event_type="spike", source_module="m1", payload=42, timestamp_ms=0.0)
    bus.publish(event)

    assert received == [event]


def test_wildcard_subscriber_receives_all_event_types():
    bus = BrainBus()
    received = []
    bus.subscribe("*", lambda event: received.append(event))

    bus.publish(BusEvent("a", "m1", 1, 0.0))
    bus.publish(BusEvent("b", "m1", 2, 0.0))

    assert [e.event_type for e in received] == ["a", "b"]


def test_tick_returns_snapshot_and_clears_pending_state():
    bus = BrainBus()
    bus.publish(BusEvent("module_output", "m1", "payload", timestamp_ms=5.0))
    state = ModuleState("m1", 4, np.zeros(4), np.zeros(4), 0.5, 16, 5.0)
    bus.publish_state(state)

    snapshot = bus.tick(timestamp_ms=5.0)

    assert isinstance(snapshot, BusSnapshot)
    assert snapshot.timestamp_ms == 5.0
    assert len(snapshot.events) == 1
    assert snapshot.states["m1"] is state

    # Pending buffers are cleared for the next tick.
    empty_snapshot = bus.tick(timestamp_ms=6.0)
    assert empty_snapshot.events == []
    assert empty_snapshot.states == {}


def test_get_history_returns_last_n_steps_oldest_first():
    bus = BrainBus()
    for t in range(5):
        bus.tick(timestamp_ms=float(t))

    history = bus.get_history(3)

    assert [s.timestamp_ms for s in history] == [2.0, 3.0, 4.0]


def test_get_history_caps_at_available_history():
    bus = BrainBus()
    bus.tick(timestamp_ms=0.0)

    assert len(bus.get_history(100)) == 1


def test_history_buffer_is_bounded_to_10000_steps():
    bus = BrainBus()
    for t in range(10_050):
        bus.tick(timestamp_ms=float(t))

    history = bus.get_history(10_050)

    assert len(history) == 10_000
    assert history[0].timestamp_ms == 50.0
    assert history[-1].timestamp_ms == 10_049.0


# --- SimulationEngine: topological ordering -------------------------------


def test_execution_order_follows_declared_dependencies():
    engine = SimulationEngine()
    sensory = MockModule("sensory")
    attention = MockModule("attention")
    memory = MockModule("memory")
    learning = MockModule("learning")

    # Register out of order; topological sort must still respect dependencies.
    engine.add_module(memory, depends_on=["attention"])
    engine.add_module(learning, depends_on=["memory"])
    engine.add_module(sensory)
    engine.add_module(attention, depends_on=["sensory"])

    order = engine.execution_order

    assert order.index("sensory") < order.index("attention")
    assert order.index("attention") < order.index("memory")
    assert order.index("memory") < order.index("learning")


def test_duplicate_module_id_rejected():
    engine = SimulationEngine()
    engine.add_module(MockModule("dup"))

    with pytest.raises(ValueError):
        engine.add_module(MockModule("dup"))


def test_dependency_on_unknown_module_raises():
    engine = SimulationEngine()
    engine.add_module(MockModule("a"), depends_on=["ghost"])

    with pytest.raises(ValueError):
        _ = engine.execution_order


def test_dependency_cycle_raises():
    engine = SimulationEngine()
    engine.add_module(MockModule("a"), depends_on=["b"])
    engine.add_module(MockModule("b"), depends_on=["a"])

    with pytest.raises(ValueError):
        _ = engine.execution_order


# --- SimulationEngine: clock & synchronous causality -----------------------


def test_step_advances_clock_by_one_dt():
    engine = SimulationEngine()
    engine.add_module(MockModule("only"))

    assert engine.current_time_ms == 0.0
    engine.step()
    assert engine.current_time_ms == 1.0


def test_downstream_module_receives_upstream_spikes_same_tick():
    engine = SimulationEngine()
    upstream = MockModule("upstream", n_neurons=4)
    downstream = MockModule("downstream", n_neurons=4)
    engine.add_module(upstream)
    engine.add_module(downstream, depends_on=["upstream"])

    engine.step()

    # downstream's input spike_trains came from upstream's same-tick output.
    downstream_inputs = downstream.update_calls[0]
    assert downstream_inputs.spike_trains.shape == (4,)
    assert np.all(downstream_inputs.spike_trains == 1.0)


def test_module_without_dependencies_receives_empty_spike_trains():
    engine = SimulationEngine()
    engine.add_module(MockModule("solo"))

    engine.step()

    inputs = engine._modules["solo"].update_calls[0]
    assert inputs.spike_trains.shape == (0,)


def test_attention_signal_propagates_to_later_modules_same_tick():
    engine = SimulationEngine()
    attention = MockModule("attention", attention_signal=0.25)
    downstream = MockModule("downstream")
    engine.add_module(attention)
    engine.add_module(downstream, depends_on=["attention"])

    engine.step()

    assert downstream.update_calls[0].attention_signal == 0.25


def test_default_attention_signal_is_one():
    engine = SimulationEngine()
    engine.add_module(MockModule("only"))

    engine.step()

    assert engine._modules["only"].update_calls[0].attention_signal == 1.0


# --- SPEC-002 acceptance scenario: 100ms with 3 mock modules ---------------


def test_run_simulates_100ms_with_three_mock_modules():
    engine = SimulationEngine()
    sensory = MockModule("sensory", n_neurons=4)
    attention = MockModule("attention", n_neurons=4)
    learning = MockModule("learning", n_neurons=4)

    engine.add_module(sensory)
    engine.add_module(attention, depends_on=["sensory"])
    engine.add_module(learning, depends_on=["attention"])

    snapshots = engine.run(duration_ms=100.0)

    assert len(snapshots) == 100
    assert engine.current_time_ms == 100.0

    for module in (sensory, attention, learning):
        assert len(module.update_calls) == 100

    # BrainBus published events in topological order on every tick.
    last_snapshot = snapshots[-1]
    sources = [e.source_module for e in last_snapshot.events]
    assert sources == ["sensory", "attention", "learning"]
    assert set(last_snapshot.states) == {"sensory", "attention", "learning"}


# --- StateRenderer: notified, never blocks the clock ------------------------


def test_state_renderer_is_notified_each_tick():
    engine = SimulationEngine()
    engine.add_module(MockModule("only"))
    received = []
    engine.register_state_renderer(received.append)

    engine.run(duration_ms=5.0)

    assert len(received) == 5
    assert all(isinstance(s, BusSnapshot) for s in received)


def test_state_renderer_exception_does_not_stop_clock():
    engine = SimulationEngine()
    engine.add_module(MockModule("only"))

    def broken_renderer(_snapshot):
        raise RuntimeError("renderer exploded")

    engine.register_state_renderer(broken_renderer)

    snapshots = engine.run(duration_ms=10.0)

    assert len(snapshots) == 10
    assert engine.current_time_ms == 10.0


# --- pause / resume ----------------------------------------------------------


def test_pause_stops_run_early():
    engine = SimulationEngine()
    module = MockModule("only")
    engine.add_module(module)

    def pause_after_three(_snapshot):
        if engine.current_time_ms >= 3.0:
            engine.pause()

    engine.register_state_renderer(pause_after_three)
    snapshots = engine.run(duration_ms=100.0)

    assert len(snapshots) == 4
    assert engine.is_paused is True

    engine.resume()
    assert engine.is_paused is False


# --- reset ---------------------------------------------------------------


def test_reset_rewinds_clock_resets_modules_and_clears_history():
    engine = SimulationEngine()
    module = MockModule("only")
    engine.add_module(module)

    engine.run(duration_ms=10.0)
    assert engine.current_time_ms == 10.0
    assert module.reset_calls == 0

    engine.reset()

    assert engine.current_time_ms == 0.0
    assert module.reset_calls == 1
    assert engine.get_history(100) == []


# --- StateBuffer / replay ----------------------------------------------------


def test_get_history_through_engine_matches_run():
    engine = SimulationEngine()
    engine.add_module(MockModule("only"))

    engine.run(duration_ms=20.0)
    history = engine.get_history(5)

    assert [s.timestamp_ms for s in history] == [15.0, 16.0, 17.0, 18.0, 19.0]
