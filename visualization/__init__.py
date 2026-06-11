"""Brain Simulator -- 3D neural visualization (SPEC-009).

A FastAPI + WebSocket server streaming :class:`~core.brain_bus.BusSnapshot`
state from a live :class:`~core.simulation_engine.SimulationEngine` to a Three.js
scene in the browser, plus a self-contained 8-region demo brain that exercises
the real engine/BrainBus/StateRenderer path.
"""
