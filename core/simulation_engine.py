"""Brain Simulator -- SimulationEngine.

Drives the global synchronous clock (dt = 1ms): every registered
:class:`~core.interfaces.CognitiveModule` is advanced once per tick, in
topological order, with inputs derived from the outputs its dependencies
produced *during the same tick* (ADR-003 -- BrainBus is synchronous).

Implemented in SPEC-002 against the frozen :mod:`core.interfaces` contract
(SPEC-001). See ``specs/SPEC-002-brain-bus.md``.
"""
from __future__ import annotations

from typing import Callable, Dict, Iterable, List, Optional, Set

import numpy as np

from core.brain_bus import BrainBus, BusEvent, BusSnapshot
from core.interfaces import (
    CognitiveModule,
    ModuleInputs,
    ModuleOutputs,
    NeuromodulationSignal,
)

__all__ = ["SimulationEngine"]


class SimulationEngine:
    """Global TimeLoop coordinating modules, the BrainBus and the StateBuffer.

    The execution order per tick is computed topologically from the
    dependency graph declared via :meth:`add_module`:

        Sensory -> Attention -> WorkingMemory -> EpisodicMemory ->
        SemanticMemory -> PredictiveCoding -> Reasoning ->
        Neuromodulators -> LearningEngine

    A :class:`~core.brain_bus.BrainBus` instance acts as the StateBuffer: its
    bounded replay history (last 10s == 10,000 timesteps at dt=1ms) is
    accessible via :meth:`get_history`.

    StateRenderer callbacks (registered via :meth:`register_state_renderer`)
    are invoked with each :class:`~core.brain_bus.BusSnapshot` after the tick
    closes, but exceptions raised by them never interrupt the clock.
    """

    DT_MS = 1.0

    def __init__(self, bus: Optional[BrainBus] = None) -> None:
        self.bus = bus if bus is not None else BrainBus()
        self._modules: Dict[str, CognitiveModule] = {}
        self._dependencies: Dict[str, Set[str]] = {}
        self._insertion_order: List[str] = []
        self._execution_order: List[str] = []
        self._order_dirty = True

        self._renderer_callbacks: List[Callable[[BusSnapshot], None]] = []

        self.current_time_ms = 0.0
        self._paused = False

        self.neuromodulation = NeuromodulationSignal()
        self._last_outputs: Dict[str, ModuleOutputs] = {}
        self._attention_signal = 1.0
        self._neuromodulator_id: Optional[str] = None

    # -- Configuration ---------------------------------------------------

    def add_module(
        self, module: CognitiveModule, depends_on: Optional[Iterable[str]] = None
    ) -> None:
        """Register ``module`` with the engine.

        Args:
            module: A fully constructed :class:`CognitiveModule`.
            depends_on: ``module_id``s of modules whose outputs from the
                *same* tick feed this module's inputs. Determines the
                topological execution order.

        Raises:
            ValueError: If ``module.module_id`` is already registered.
        """
        module_id = module.module_id
        if module_id in self._modules:
            raise ValueError(f"module_id {module_id!r} already registered")

        self._modules[module_id] = module
        self._dependencies[module_id] = set(depends_on or ())
        self._insertion_order.append(module_id)
        self._order_dirty = True

    def register_neuromodulator(self, module_id: str) -> None:
        """Designate a registered module as the global neuromodulation source.

        The named module (a SPEC-008
        :class:`~modules.neuromodulation.system.NeuromodulatorSystem`, or any
        module exposing a ``current_signal`` :class:`NeuromodulationSignal`
        property) becomes the authority for :attr:`neuromodulation`.

        While a neuromodulator is registered, :meth:`step` (a) applies the
        current global signal to *every* module via
        :meth:`~core.interfaces.CognitiveModule.apply_neuromodulation` before
        the tick runs, and (b) refreshes :attr:`neuromodulation` from the
        source's ``current_signal`` after it updates -- so the signal it emits
        on tick ``N`` is broadcast on tick ``N + 1`` (the synchronous one-tick
        BrainBus latency). Until one is registered the engine keeps the basal
        signal and does not call ``apply_neuromodulation`` (preserving the
        pre-SPEC-008 behaviour).

        Raises:
            ValueError: If ``module_id`` is not registered, or the module does
                not expose a ``current_signal`` attribute.
        """
        if module_id not in self._modules:
            raise ValueError(f"unknown module_id {module_id!r}")
        if not hasattr(self._modules[module_id], "current_signal"):
            raise ValueError(
                f"module {module_id!r} does not expose a 'current_signal' property"
            )
        self._neuromodulator_id = module_id

    def register_state_renderer(self, callback: Callable[[BusSnapshot], None]) -> None:
        """Register a callback notified with each tick's :class:`BusSnapshot`.

        Renderer callbacks run synchronously after the tick closes, but they
        never block or abort the clock: any exception they raise is
        swallowed.
        """
        self._renderer_callbacks.append(callback)

    # -- Topological ordering ---------------------------------------------

    def _compute_order(self) -> None:
        """Compute the topological execution order via Kahn's algorithm.

        Modules with no remaining dependencies are processed in the order
        they were registered, which preserves the documented default chain
        (Sensory -> Attention -> Memory -> ... -> LearningEngine) when
        modules are added in that order.
        """
        in_degree = {
            module_id: len(deps) for module_id, deps in self._dependencies.items()
        }
        dependents: Dict[str, List[str]] = {module_id: [] for module_id in self._modules}
        for module_id, deps in self._dependencies.items():
            for dep in deps:
                if dep not in self._modules:
                    raise ValueError(
                        f"module {module_id!r} depends on unknown module {dep!r}"
                    )
                dependents[dep].append(module_id)

        ready = [m for m in self._insertion_order if in_degree[m] == 0]
        order: List[str] = []

        while ready:
            ready.sort(key=self._insertion_order.index)
            current = ready.pop(0)
            order.append(current)
            for dependent in dependents[current]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    ready.append(dependent)

        if len(order) != len(self._modules):
            raise ValueError("dependency cycle detected among registered modules")

        self._execution_order = order
        self._order_dirty = False

    @property
    def execution_order(self) -> List[str]:
        """The current topological execution order (computed lazily)."""
        if self._order_dirty:
            self._compute_order()
        return list(self._execution_order)

    # -- Clock --------------------------------------------------------------

    def step(self) -> BusSnapshot:
        """Advance the simulation by one ``dt`` (1ms) tick.

        Every module is updated once, in topological order, with
        ``ModuleInputs`` built from the outputs its dependencies produced
        earlier in *this same tick*. Each module's outputs and state are
        published to the BrainBus, the tick is closed into a
        :class:`~core.brain_bus.BusSnapshot`, and registered StateRenderer
        callbacks are notified (without blocking the clock).

        Returns:
            The :class:`~core.brain_bus.BusSnapshot` for this tick.
        """
        if self._order_dirty:
            self._compute_order()

        # Broadcast the current global neuromodulatory signal to every module
        # before the tick runs (SPEC-008). Only active once a neuromodulator is
        # registered, so the basal pre-SPEC-008 behaviour is preserved.
        if self._neuromodulator_id is not None:
            for module in self._modules.values():
                module.apply_neuromodulation(self.neuromodulation)

        for module_id in self._execution_order:
            module = self._modules[module_id]
            inputs = self._build_inputs(module_id)

            outputs = module.update(self.DT_MS, inputs)
            self._last_outputs[module_id] = outputs

            if module_id == self._neuromodulator_id:
                self.neuromodulation = module.current_signal

            attention = outputs.internal_state.get("attention_signal")
            if attention is not None:
                self._attention_signal = float(attention)

            self.bus.publish(
                BusEvent(
                    event_type="module_output",
                    source_module=module_id,
                    payload=outputs,
                    timestamp_ms=self.current_time_ms,
                )
            )
            self.bus.publish_state(module.get_state())

        snapshot = self.bus.tick(self.current_time_ms)

        for callback in self._renderer_callbacks:
            try:
                callback(snapshot)
            except Exception:
                # StateRenderer must never block or break the main clock.
                pass

        self.current_time_ms += self.DT_MS
        return snapshot

    def _build_inputs(self, module_id: str) -> ModuleInputs:
        deps = sorted(self._dependencies[module_id], key=self._insertion_order.index)
        if deps:
            spike_trains = np.concatenate(
                [self._last_outputs[dep].spike_trains for dep in deps]
            )
        else:
            spike_trains = np.zeros(0)

        return ModuleInputs(
            spike_trains=spike_trains,
            attention_signal=self._attention_signal,
            neuromodulation=self.neuromodulation,
            timestamp_ms=self.current_time_ms,
        )

    def run(self, duration_ms: float) -> List[BusSnapshot]:
        """Run the simulation for ``duration_ms`` milliseconds.

        Equivalent to calling :meth:`step` ``duration_ms / DT_MS`` times.
        Stops early if :meth:`pause` is called during the run.

        Returns:
            The list of :class:`~core.brain_bus.BusSnapshot` produced.
        """
        n_steps = int(round(duration_ms / self.DT_MS))
        snapshots: List[BusSnapshot] = []
        for _ in range(n_steps):
            if self._paused:
                break
            snapshots.append(self.step())
        return snapshots

    def pause(self) -> None:
        """Pause the clock. :meth:`run` returns after the current step."""
        self._paused = True

    def resume(self) -> None:
        """Resume the clock after :meth:`pause`."""
        self._paused = False

    @property
    def is_paused(self) -> bool:
        return self._paused

    def reset(self) -> None:
        """Reset the engine: rewind the clock and reset every module.

        Each registered module's :meth:`~core.interfaces.CognitiveModule.reset`
        is called, the BrainBus replay history is cleared, and
        ``current_time_ms`` returns to ``0.0``. Registered modules,
        dependencies and StateRenderer callbacks are preserved.
        """
        for module in self._modules.values():
            module.reset()
        self.bus.reset()
        self._last_outputs = {}
        self._attention_signal = 1.0
        self.neuromodulation = NeuromodulationSignal()
        self.current_time_ms = 0.0
        self._paused = False

    # -- Replay ---------------------------------------------------------------

    def get_history(self, n_steps: int) -> List[BusSnapshot]:
        """Return up to the last ``n_steps`` snapshots from the StateBuffer."""
        return self.bus.get_history(n_steps)
