// Brain Simulator -- main Three.js scene (SPEC-009).
//
// Owns the renderer, camera, lights and the collection of visual objects, and
// applies streamed frames from the WebSocket. The render loop is independent of
// the data rate: frames arrive at ~30fps, the scene renders at the display
// refresh rate and interpolates spike/pulse decay smoothly in between.

import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import {
  BrainRegion,
  SynapticArc,
  SpikeParticle,
  DopamineHalo,
} from "./neural_objects.js";
import { setupControls } from "./controls.js";

class BrainScene {
  constructor(container) {
    this.container = container;
    this.regions = new Map();
    this.arcs = [];
    this.particles = [];
    this.halo = null;
    this.clock = new THREE.Clock();

    this._initRenderer();
    this._initSceneGraph();
    this._fpsSamples = [];
    this._lastFpsUpdate = performance.now();

    window.addEventListener("resize", () => this._onResize());
  }

  _initRenderer() {
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x070b14);

    const { clientWidth: w, clientHeight: h } = this.container;
    this.camera = new THREE.PerspectiveCamera(55, w / h, 0.1, 100);
    this.camera.position.set(6, 4, 9);

    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.setSize(w, h);
    this.container.appendChild(this.renderer.domElement);

    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.target.set(0, 1, 0);
  }

  _initSceneGraph() {
    this.scene.add(new THREE.AmbientLight(0x404a5c, 1.2));
    const key = new THREE.PointLight(0xffffff, 1.1, 100);
    key.position.set(8, 12, 10);
    this.scene.add(key);
    const rim = new THREE.PointLight(0x4466ff, 0.6, 100);
    rim.position.set(-10, -6, -8);
    this.scene.add(rim);

    const grid = new THREE.GridHelper(20, 20, 0x1b2436, 0x111722);
    grid.position.y = -3;
    this.scene.add(grid);
  }

  build(layout) {
    // Clear any previous build (on reconnect).
    for (const region of this.regions.values()) this.scene.remove(region.mesh);
    for (const arc of this.arcs) this.scene.remove(arc.mesh);
    this.regions.clear();
    this.arcs = [];

    for (const cfg of layout.regions) {
      this.regions.set(cfg.id, new BrainRegion(this.scene, cfg));
    }
    for (const conn of layout.connections) {
      const from = this.regions.get(conn.source);
      const to = this.regions.get(conn.target);
      if (from && to) {
        this.arcs.push(new SynapticArc(this.scene, from, to, conn.type));
      }
    }
    if (!this.halo) this.halo = new DopamineHalo(this.scene);
  }

  applyFrame(frame) {
    const anyIsolated = frame.regions.some((r) => r.isolated);
    const rateById = new Map();
    for (const data of frame.regions) {
      const region = this.regions.get(data.id);
      if (!region) continue;
      rateById.set(data.id, data.firing_rate);
      region.applyState(data);
      region.setIsolation(anyIsolated, data.isolated);
      const visible = !anyIsolated || data.isolated;
      if (data.spike && visible) this._emitSpike(region);
    }
    // Arc strength: source region drive normalized to ~[0,1] (60 Hz ceiling).
    for (const arc of this.arcs) {
      const rate = rateById.get(arc.sourceId) || 0;
      arc.setStrength(rate / 60);
    }
    if (this.halo) this.halo.setLevel(frame.dopamine);
  }

  _emitSpike(region) {
    this.particles.push(
      new SpikeParticle(this.scene, region.position, region.material.color)
    );
    // Cap particle count for performance.
    if (this.particles.length > 200) {
      const old = this.particles.shift();
      old.update(10); // force-expire
    }
  }

  _onResize() {
    const { clientWidth: w, clientHeight: h } = this.container;
    this.camera.aspect = w / h;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(w, h);
  }

  focusRegion(regionId) {
    const region = this.regions.get(regionId);
    if (!region) return;
    this.controls.target.copy(region.position);
  }

  // ndc: {x, y} normalized device coords. Returns the BrainRegion under the
  // pointer, or null.
  raycast(ndc) {
    if (!this._raycaster) this._raycaster = new THREE.Raycaster();
    this._raycaster.setFromCamera(new THREE.Vector2(ndc.x, ndc.y), this.camera);
    const meshes = Array.from(this.regions.values()).map((r) => r.mesh);
    const hits = this._raycaster.intersectObjects(meshes, false);
    return hits.length ? hits[0].object.userData.region : null;
  }

  start(onFps) {
    const animate = () => {
      requestAnimationFrame(animate);
      const dt = Math.min(0.1, this.clock.getDelta());

      for (const region of this.regions.values()) region.update(dt);
      this.particles = this.particles.filter((p) => p.update(dt));
      if (this.halo) this.halo.update(dt);

      this.controls.update();
      this.renderer.render(this.scene, this.camera);

      // FPS measurement.
      const now = performance.now();
      this._fpsSamples.push(now);
      while (this._fpsSamples.length && now - this._fpsSamples[0] > 1000) {
        this._fpsSamples.shift();
      }
      if (onFps && now - this._lastFpsUpdate > 250) {
        this._lastFpsUpdate = now;
        onFps(this._fpsSamples.length);
      }
    };
    animate();
  }
}

// -- Bootstrap -----------------------------------------------------------------

const container = document.getElementById("scene");
const scene = new BrainScene(container);
scene.start((fps) => {
  const el = document.getElementById("fps");
  if (el) el.textContent = fps.toString();
});

setupControls(scene);
