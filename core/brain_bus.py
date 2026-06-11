"""Brain Simulator -- BrainBus (STUB).

Synchronous, in-process event broker connecting all cognitive modules on a
shared timestep (dt = 1ms). Every module publishes and subscribes within the
same tick, guaranteeing biological causality (ADR-003).

STATUS: stub only. The behaviour declared here is implemented in SPEC-002
(``BrainBus + SimulationEngine``). The signatures are intentionally minimal so
that SPEC-002 can finalise the event and snapshot types without breaking the
frozen :mod:`core.interfaces` contract.
"""
from __future__ import annotations

from typing import Any, Callable, List


class BrainBus:
    """Synchronous per-timestep event broker (stub -- implemented in SPEC-002)."""

    def publish(self, event: Any) -> None:
        """Publish an event to subscribers for the current tick."""
        raise NotImplementedError("BrainBus.publish is implemented in SPEC-002")

    def subscribe(self, event_type: str, handler: Callable[[Any], None]) -> None:
        """Register ``handler`` to receive events of ``event_type``."""
        raise NotImplementedError("BrainBus.subscribe is implemented in SPEC-002")

    def tick(self) -> Any:
        """Close the current timestep and return its complete snapshot."""
        raise NotImplementedError("BrainBus.tick is implemented in SPEC-002")

    def get_history(self, n_steps: int) -> List[Any]:
        """Return the snapshots of the last ``n_steps`` timesteps."""
        raise NotImplementedError("BrainBus.get_history is implemented in SPEC-002")
