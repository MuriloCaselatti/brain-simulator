"""Brain Simulator -- BrainBus.

Synchronous, in-process event broker connecting all cognitive modules on a
shared timestep (dt = 1ms). Every module publishes and subscribes within the
same tick, guaranteeing biological causality (ADR-003).

Implemented in SPEC-002 against the frozen :mod:`core.interfaces` contract
(SPEC-001). See ``specs/SPEC-002-brain-bus.md``.
"""
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Any, Callable, Deque, Dict, List

from core.interfaces import ModuleState

__all__ = ["BusEvent", "BusSnapshot", "BrainBus"]

# Replay window: 10s of simulation at dt=1ms.
HISTORY_MAXLEN = 10_000


@dataclass
class BusEvent:
    """A single event published to the BrainBus during a timestep.

    Attributes:
        event_type: Logical channel of the event (e.g. ``"module_output"``).
        source_module: ``module_id`` of the publisher.
        payload: Arbitrary event data. Often a :class:`~core.interfaces.ModuleOutputs`.
        timestamp_ms: Absolute simulation time in milliseconds.
    """

    event_type: str
    source_module: str
    payload: Any
    timestamp_ms: float


@dataclass
class BusSnapshot:
    """Complete record of a single closed timestep.

    Attributes:
        timestamp_ms: Absolute simulation time in milliseconds for this tick.
        events: All events published during the tick, in publish order.
        states: Latest :class:`~core.interfaces.ModuleState` per module,
            keyed by ``module_id``.
    """

    timestamp_ms: float
    events: List[BusEvent] = field(default_factory=list)
    states: Dict[str, ModuleState] = field(default_factory=dict)


class BrainBus:
    """Synchronous per-timestep event broker.

    All modules publish and subscribe within the same tick (dt = 1ms),
    so handlers run synchronously and immediately as ``publish`` is called --
    this guarantees that within-tick causality matches the topological
    execution order of the :class:`~core.simulation_engine.SimulationEngine`.

    ``tick()`` closes the current timestep, archiving everything published
    since the previous ``tick()`` into a :class:`BusSnapshot` and appending it
    to a bounded replay buffer (last ``HISTORY_MAXLEN`` timesteps, i.e. the
    last 10s of simulated time at dt=1ms).
    """

    def __init__(self, history_maxlen: int = HISTORY_MAXLEN) -> None:
        self._subscribers: Dict[str, List[Callable[[BusEvent], None]]] = defaultdict(list)
        self._pending_events: List[BusEvent] = []
        self._pending_states: Dict[str, ModuleState] = {}
        self._history: Deque[BusSnapshot] = deque(maxlen=history_maxlen)

    def publish(self, event: BusEvent) -> None:
        """Publish ``event`` and synchronously notify matching subscribers.

        Subscribers registered for ``event.event_type`` and subscribers
        registered for the wildcard ``"*"`` are both invoked, in
        registration order.
        """
        self._pending_events.append(event)
        for handler in self._subscribers.get(event.event_type, []):
            handler(event)
        for handler in self._subscribers.get("*", []):
            handler(event)

    def subscribe(self, event_type: str, handler: Callable[[BusEvent], None]) -> None:
        """Register ``handler`` to receive events of ``event_type``.

        Use ``event_type="*"`` to receive every event regardless of type.
        """
        self._subscribers[event_type].append(handler)

    def publish_state(self, state: ModuleState) -> None:
        """Record ``state`` as the latest module state for the current tick.

        Consumed by :meth:`tick` to populate :attr:`BusSnapshot.states`.
        """
        self._pending_states[state.module_id] = state

    def tick(self, timestamp_ms: float = 0.0) -> BusSnapshot:
        """Close the current timestep and return its complete snapshot.

        All events and states accumulated since the previous call to
        ``tick()`` are archived into the returned :class:`BusSnapshot`, the
        snapshot is appended to the replay history, and the pending buffers
        are cleared for the next timestep.
        """
        snapshot = BusSnapshot(
            timestamp_ms=timestamp_ms,
            events=list(self._pending_events),
            states=dict(self._pending_states),
        )
        self._history.append(snapshot)
        self._pending_events = []
        self._pending_states = {}
        return snapshot

    def get_history(self, n_steps: int) -> List[BusSnapshot]:
        """Return up to the last ``n_steps`` :class:`BusSnapshot` entries.

        Snapshots are returned oldest-first. If fewer than ``n_steps``
        snapshots have been recorded, all available snapshots are returned.
        """
        if n_steps <= 0:
            return []
        history = list(self._history)
        return history[-n_steps:]

    def reset(self) -> None:
        """Clear all pending state and replay history."""
        self._pending_events = []
        self._pending_states = {}
        self._history.clear()
