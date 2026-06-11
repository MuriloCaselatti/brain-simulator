"""Brain Simulator -- visualization server (SPEC-009).

A FastAPI + WebSocket server that runs the demo brain (see
:mod:`visualization.demo_brain`) on a background thread and streams its state to
a Three.js scene in the browser at ~30fps.

Architecture
------------
* The :class:`SimulationEngine` clock runs in its own daemon thread
  (:class:`SimulationRunner`), paced to the requested speed.
* A :meth:`~core.simulation_engine.SimulationEngine.register_state_renderer`
  callback serializes the latest :class:`~core.brain_bus.BusSnapshot` into a
  small JSON-ready dict and stores it -- **without ever blocking the clock**
  (the engine already swallows renderer exceptions; the callback itself only
  takes a brief lock and is throttled to the streaming rate).
* An async broadcaster task reads that latest frame ~30 times/s and pushes it to
  every connected WebSocket. Browser control messages (play/pause/step/speed/
  isolate/reset) flow back over the same socket.

Run with::

    python -m visualization.server      # then open http://127.0.0.1:8000
"""
from __future__ import annotations

import asyncio
import math
import mimetypes
import threading
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

# Serve ES modules with a JavaScript MIME type. On Windows the system registry
# often maps ".js" to "text/plain", which browsers reject for
# `<script type="module">` (strict MIME checking) -- the module then silently
# fails to load. Force the correct types before StaticFiles guesses them.
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("text/javascript", ".mjs")

import numpy as np
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from core.brain_bus import BusSnapshot
from core.simulation_engine import SimulationEngine
from visualization.demo_brain import (
    NEUROMODULATOR_ID,
    REGION_CONNECTIONS,
    REGION_LAYOUT,
    build_demo_brain,
)

STATIC_DIR = Path(__file__).parent / "static"

# Streaming / pacing constants.
STREAM_FPS = 30.0
STREAM_INTERVAL_S = 1.0 / STREAM_FPS
# A region "spikes" (flash) when its mean firing rate crosses this, in Hz.
SPIKE_FLASH_HZ = 25.0
# Per-module spike sample size sent for the SPEC-010 raster plot HUD (one row
# per entry; subsampled so the stream stays light at 30fps).
RASTER_NEURONS = 64
# Time constant (ms) for the TD-error HUD signal's decay back to 0 between
# reward events -- mirrors DopamineSystem's default phasic-drive tau.
TD_ERROR_TAU_MS = 50.0


# -- Snapshot serialization -----------------------------------------------------


def _subsample_spikes(spikes: np.ndarray, n: int) -> List[int]:
    """Down/up-sample a spike mask to exactly ``n`` 0/1 entries for the raster."""
    if spikes.size == 0:
        return [0] * n
    if spikes.size <= n:
        idx = np.arange(spikes.size)
    else:
        idx = np.linspace(0, spikes.size - 1, n).astype(int)
    sample = (spikes[idx] > 0).astype(int).tolist()
    if len(sample) < n:
        sample.extend([0] * (n - len(sample)))
    return sample

def serialize_layout() -> Dict[str, Any]:
    """Static scene description sent once per client connection."""
    return {
        "type": "layout",
        "regions": [
            {
                "id": region_id,
                "pos": cfg["pos"],
                "color": cfg["color"],
                "radius": cfg["radius"],
                "label": cfg["label"],
            }
            for region_id, cfg in REGION_LAYOUT.items()
        ],
        "connections": [
            {"source": s, "target": t, "type": kind}
            for (s, t, kind) in REGION_CONNECTIONS
        ],
    }


def serialize_frame(
    snapshot: BusSnapshot,
    *,
    dopamine: float,
    noradrenaline: float,
    acetylcholine: float,
    playing: bool,
    speed: float,
    isolated: Set[str],
    td_error: float = 0.0,
) -> Dict[str, Any]:
    """Turn a :class:`BusSnapshot` into a compact JSON-ready frame.

    Per-region summaries (mean/max firing rate, mean voltage, a spike-flash
    flag) plus a subsampled spike raster (:data:`RASTER_NEURONS` entries) for
    the SPEC-010 HUD -- never the full per-neuron arrays -- to keep the stream
    light enough for 30fps over a localhost WebSocket.
    """
    # A region flashes if it emitted any spikes this tick; also feeds the raster.
    spiked: Dict[str, bool] = {}
    spike_arrays: Dict[str, np.ndarray] = {}
    for event in snapshot.events:
        if event.event_type != "module_output":
            continue
        outputs = event.payload
        spikes = np.asarray(getattr(outputs, "spike_trains", np.zeros(0)))
        spike_arrays[event.source_module] = spikes
        spiked[event.source_module] = bool(spikes.size) and bool(spikes.any())

    regions: List[Dict[str, Any]] = []
    for region_id in REGION_LAYOUT:
        state = snapshot.states.get(region_id)
        if state is None:
            continue
        rate = np.asarray(state.firing_rate, dtype=float)
        voltage = np.asarray(state.voltage, dtype=float)
        mean_hz = float(rate.mean()) if rate.size else 0.0
        regions.append(
            {
                "id": region_id,
                "firing_rate": round(mean_hz, 2),
                "max_rate": round(float(rate.max()), 2) if rate.size else 0.0,
                "voltage": round(float(voltage.mean()), 2) if voltage.size else 0.0,
                "n_neurons": int(state.n_neurons),
                "mean_weight": round(float(state.mean_weight), 3),
                "spike": bool(spiked.get(region_id, False)) or mean_hz >= SPIKE_FLASH_HZ,
                "isolated": region_id in isolated,
                "raster": _subsample_spikes(
                    spike_arrays.get(region_id, np.zeros(0)), RASTER_NEURONS
                ),
            }
        )

    return {
        "type": "frame",
        "timestamp_ms": round(float(snapshot.timestamp_ms), 1),
        "playing": playing,
        "speed": speed,
        "dopamine": round(float(dopamine), 3),
        "noradrenaline": round(float(noradrenaline), 3),
        "acetylcholine": round(float(acetylcholine), 3),
        "td_error": round(float(td_error), 4),
        "regions": regions,
    }


# -- Simulation runner ----------------------------------------------------------

class SimulationRunner:
    """Drives a :class:`SimulationEngine` on a background thread.

    Thread-safety: control flags are plain attributes (assignment is atomic in
    CPython); the latest serialized frame and the isolate set are guarded by a
    lock. The engine itself is only ever touched from the runner thread, except
    for the read-only neuromodulation levels sampled during serialization.
    """

    def __init__(self, engine: Optional[SimulationEngine] = None) -> None:
        self.engine = engine if engine is not None else build_demo_brain()
        self.engine.register_state_renderer(self._on_snapshot)
        self._neuromod = self.engine._modules.get(NEUROMODULATOR_ID)  # may be None

        self.playing = False
        self.speed = 1.0
        self.isolated: Set[str] = set()

        self._step_requests = 0
        self._stop = False
        self._thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()
        self._latest: Optional[Dict[str, Any]] = None
        self._last_emit = 0.0
        # TD-error HUD signal (SPEC-010): phasic on reward, decays toward 0.
        self._last_td_error = 0.0

    # -- lifecycle ----------------------------------------------------------

    def start(self) -> None:
        if self._thread is not None:
            return
        self._thread = threading.Thread(target=self._run, name="sim-clock", daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop = True
        if self._thread is not None:
            self._thread.join(timeout=1.0)
            self._thread = None

    # -- control ------------------------------------------------------------

    def handle_command(self, command: Dict[str, Any]) -> None:
        """Apply a control command from the browser. Unknown commands are ignored."""
        cmd = command.get("cmd")
        if cmd == "play":
            self.playing = True
        elif cmd == "pause":
            self.playing = False
        elif cmd == "step":
            self.playing = False
            with self._lock:
                self._step_requests += int(command.get("value", 1) or 1)
        elif cmd == "speed":
            try:
                self.speed = max(0.1, min(50.0, float(command.get("value", 1.0))))
            except (TypeError, ValueError):
                pass
        elif cmd == "isolate":
            module = command.get("module")
            if module in REGION_LAYOUT:
                with self._lock:
                    if module in self.isolated:
                        self.isolated.discard(module)
                    else:
                        self.isolated.add(module)
        elif cmd == "clear_isolate":
            with self._lock:
                self.isolated.clear()
        elif cmd == "reset":
            self.playing = False
            self.engine.reset()
            self._last_td_error = 0.0
            with self._lock:
                self._step_requests = 0

    # -- stepping -----------------------------------------------------------

    def _drive_neuromodulators(self) -> None:
        """Animate dopamine/noradrenaline so the halo and arousal visibly move.

        Drives a slow arousal sine plus a periodic reward burst -- the engine
        broadcasts the resulting signal to every region on the next tick.
        """
        if self._neuromod is None:
            return
        t_s = self.engine.current_time_ms / 1000.0
        self._neuromod.set_arousal(0.4 + 0.4 * float(np.sin(2.0 * np.pi * 0.15 * t_s)))
        self._neuromod.set_attention(0.5 + 0.3 * float(np.sin(2.0 * np.pi * 0.25 * t_s)))
        # TD-error HUD signal: relaxes exponentially toward 0 between events.
        self._last_td_error *= math.exp(-self.engine.DT_MS / TD_ERROR_TAU_MS)
        # A reward burst roughly once per simulated second.
        if int(self.engine.current_time_ms) % 1000 == 0:
            self._last_td_error = self._neuromod.observe_reward(1.0, value_estimate=0.0)

    def _advance(self) -> BusSnapshot:
        """Drive neuromodulators and advance the engine one tick."""
        self._drive_neuromodulators()
        return self.engine.step()

    def _run(self) -> None:
        next_tick = time.perf_counter()
        while not self._stop:
            do_step = False
            if self.playing:
                do_step = True
            else:
                with self._lock:
                    if self._step_requests > 0:
                        self._step_requests -= 1
                        do_step = True

            if not do_step:
                next_tick = time.perf_counter()
                time.sleep(0.01)
                continue

            self._advance()

            if self.playing:
                # Pace: one simulated ms per (1 / speed) wall-ms.
                next_tick += (self.engine.DT_MS / 1000.0) / self.speed
                delay = next_tick - time.perf_counter()
                if delay > 0.0005:
                    time.sleep(delay)
                elif delay < -0.1:
                    next_tick = time.perf_counter()  # fell behind; resync

    # -- renderer callback (NEVER blocks the clock) -------------------------

    def _on_snapshot(self, snapshot: BusSnapshot) -> None:
        """StateRenderer callback: throttle to the stream rate, then store a frame.

        Runs on the clock thread. It does no I/O and only serializes a small
        summary at most ~30 times/s, so it cannot slow the simulation; the engine
        also swallows any exception raised here.
        """
        now = time.perf_counter()
        if self.playing and (now - self._last_emit) < STREAM_INTERVAL_S:
            return
        self._last_emit = now

        signal = self.engine.neuromodulation
        with self._lock:
            isolated = set(self.isolated)
        frame = serialize_frame(
            snapshot,
            dopamine=signal.dopamine,
            noradrenaline=signal.noradrenaline,
            acetylcholine=signal.acetylcholine,
            playing=self.playing,
            speed=self.speed,
            isolated=isolated,
            td_error=self._last_td_error,
        )
        with self._lock:
            self._latest = frame

    def latest_frame(self) -> Optional[Dict[str, Any]]:
        with self._lock:
            return self._latest


# -- Connection manager ---------------------------------------------------------

class ConnectionManager:
    """Tracks connected WebSockets and broadcasts frames to all of them."""

    def __init__(self) -> None:
        self._connections: Set[WebSocket] = set()
        self._lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self._lock:
            self._connections.add(websocket)

    async def disconnect(self, websocket: WebSocket) -> None:
        async with self._lock:
            self._connections.discard(websocket)

    async def broadcast(self, message: Dict[str, Any]) -> None:
        async with self._lock:
            targets = list(self._connections)
        dead: List[WebSocket] = []
        for ws in targets:
            try:
                await ws.send_json(message)
            except Exception:
                dead.append(ws)
        if dead:
            async with self._lock:
                for ws in dead:
                    self._connections.discard(ws)


# -- FastAPI app ----------------------------------------------------------------

runner = SimulationRunner()
manager = ConnectionManager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    runner.start()
    broadcaster = asyncio.create_task(_broadcast_loop())
    try:
        yield
    finally:
        broadcaster.cancel()
        runner.stop()


app = FastAPI(title="Brain Simulator -- Visualization", lifespan=lifespan)


async def _broadcast_loop() -> None:
    """Push the latest frame to every client ~30 times/s."""
    while True:
        await asyncio.sleep(STREAM_INTERVAL_S)
        frame = runner.latest_frame()
        if frame is not None:
            await manager.broadcast(frame)


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/layout")
async def layout() -> Dict[str, Any]:
    return serialize_layout()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await manager.connect(websocket)
    try:
        await websocket.send_json(serialize_layout())
        frame = runner.latest_frame()
        if frame is not None:
            await websocket.send_json(frame)
        while True:
            command = await websocket.receive_json()
            runner.handle_command(command)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
    except Exception:
        await manager.disconnect(websocket)


if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")


if __name__ == "__main__":
    main()
