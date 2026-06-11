// Brain Simulator -- WebSocket client + control wiring (SPEC-009).
//
// Opens the bidirectional WebSocket: inbound `layout`/`frame` messages drive the
// scene; the play/pause/step/speed/isolate/reset controls send commands back.

export function setupControls(scene, chartHud) {
  const proto = location.protocol === "https:" ? "wss" : "ws";
  const url = `${proto}://${location.host}/ws`;
  let ws = null;
  let isolateMode = false;

  const hud = {
    status: document.getElementById("status"),
    time: document.getElementById("sim-time"),
    dopamine: document.getElementById("dopamine"),
    speed: document.getElementById("speed-label"),
  };

  function send(command) {
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(command));
    }
  }

  function connect() {
    ws = new WebSocket(url);
    ws.onopen = () => setStatus("connected");
    ws.onclose = () => {
      setStatus("disconnected — retrying");
      setTimeout(connect, 1000);
    };
    ws.onerror = () => ws.close();
    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.type === "layout") {
        scene.build(msg);
        chartHud?.build(msg);
      } else if (msg.type === "frame") {
        scene.applyFrame(msg);
        chartHud?.applyFrame(msg);
        updateHud(msg);
      }
    };
  }

  function setStatus(text) {
    if (hud.status) hud.status.textContent = text;
  }

  function updateHud(frame) {
    if (hud.time) hud.time.textContent = `${(frame.timestamp_ms / 1000).toFixed(2)} s`;
    if (hud.dopamine) hud.dopamine.textContent = frame.dopamine.toFixed(2);
    if (hud.speed) hud.speed.textContent = `${frame.speed}×`;
    const playBtn = document.getElementById("btn-play");
    if (playBtn) playBtn.textContent = frame.playing ? "⏸ Pause" : "▶ Play";
  }

  // -- Button wiring -----------------------------------------------------------

  const playBtn = document.getElementById("btn-play");
  if (playBtn) {
    playBtn.addEventListener("click", () => {
      send({ cmd: playBtn.textContent.includes("Play") ? "play" : "pause" });
    });
  }

  bind("btn-step", () => send({ cmd: "step", value: 1 }));
  bind("btn-reset", () => send({ cmd: "reset" }));

  const speedInput = document.getElementById("speed");
  if (speedInput) {
    speedInput.addEventListener("input", () => {
      send({ cmd: "speed", value: parseFloat(speedInput.value) });
    });
  }

  const isolateBtn = document.getElementById("btn-isolate");
  if (isolateBtn) {
    isolateBtn.addEventListener("click", () => {
      isolateMode = !isolateMode;
      isolateBtn.classList.toggle("active", isolateMode);
      isolateBtn.textContent = isolateMode ? "🔍 Isolate: ON" : "🔍 Isolate";
      if (!isolateMode) send({ cmd: "clear_isolate" });
    });
  }

  // Click a region in the 3D view to isolate/focus it (when isolate mode is on).
  scene.renderer.domElement.addEventListener("click", (event) => {
    if (!isolateMode) return;
    const region = pickRegion(event);
    if (region) {
      send({ cmd: "isolate", module: region.id });
      scene.focusRegion(region.id);
    }
  });

  function pickRegion(event) {
    const rect = scene.renderer.domElement.getBoundingClientRect();
    const ndc = {
      x: ((event.clientX - rect.left) / rect.width) * 2 - 1,
      y: -((event.clientY - rect.top) / rect.height) * 2 + 1,
    };
    return scene.raycast(ndc);
  }

  function bind(id, handler) {
    const el = document.getElementById(id);
    if (el) el.addEventListener("click", handler);
  }

  connect();
  return { send };
}
