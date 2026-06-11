// Brain Simulator -- visual primitives for the 3D scene (SPEC-009).
//
// BrainRegion  -> a sphere per cognitive module; colour = firing rate (heatmap),
//                 emissive pulse + spawned particle = spike event.
// SynapticArc  -> a curved tube between two regions; thickness/opacity scale with
//                 synaptic strength, colour by type (excitatory/inhibitory).
// SpikeParticle-> a short-lived expanding glow emitted on a spike.
// DopamineHalo -> a global ring whose brightness/scale tracks dopamine level.

import * as THREE from "three";

// Firing rate (Hz) mapped to a blue -> cyan -> yellow -> red heatmap.
const MAX_RATE_HZ = 60.0;

export function heatmapColor(rateHz) {
  const t = Math.max(0, Math.min(1, rateHz / MAX_RATE_HZ));
  // Hue 240deg (blue) down to 0deg (red); brighten with activity.
  const hue = (1 - t) * 0.66; // 0.66 ~ 240deg
  const light = 0.35 + 0.25 * t;
  const color = new THREE.Color();
  color.setHSL(hue, 0.9, light);
  return color;
}

export class SpikeParticle {
  constructor(scene, position, color) {
    const geometry = new THREE.SphereGeometry(0.12, 12, 12);
    const material = new THREE.MeshBasicMaterial({
      color: color,
      transparent: true,
      opacity: 0.9,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
    });
    this.mesh = new THREE.Mesh(geometry, material);
    this.mesh.position.copy(position);
    this.life = 1.0;
    this.scene = scene;
    scene.add(this.mesh);
  }

  // Returns false when the particle has expired and was removed.
  update(dt) {
    this.life -= dt * 2.5;
    if (this.life <= 0) {
      this.scene.remove(this.mesh);
      this.mesh.geometry.dispose();
      this.mesh.material.dispose();
      return false;
    }
    const scale = 1 + (1 - this.life) * 4;
    this.mesh.scale.setScalar(scale);
    this.mesh.material.opacity = this.life * 0.9;
    return true;
  }
}

export class BrainRegion {
  constructor(scene, cfg) {
    this.id = cfg.id;
    this.label = cfg.label;
    this.baseColor = new THREE.Color(cfg.color);
    this.radius = cfg.radius;
    this.scene = scene;

    const geometry = new THREE.SphereGeometry(cfg.radius, 32, 32);
    this.material = new THREE.MeshStandardMaterial({
      color: this.baseColor,
      emissive: this.baseColor.clone().multiplyScalar(0.2),
      roughness: 0.45,
      metalness: 0.1,
      transparent: true,
      opacity: 0.92,
    });
    this.mesh = new THREE.Mesh(geometry, this.material);
    this.mesh.position.fromArray(cfg.pos);
    this.mesh.userData.region = this;
    scene.add(this.mesh);

    // Wireframe shell to suggest a neural population.
    const shell = new THREE.Mesh(
      new THREE.SphereGeometry(cfg.radius * 1.05, 16, 16),
      new THREE.MeshBasicMaterial({ color: this.baseColor, wireframe: true, transparent: true, opacity: 0.15 })
    );
    this.mesh.add(shell);

    this.pulse = 0;
    this.isolated = false;
    this.firingRate = 0;
  }

  get position() {
    return this.mesh.position;
  }

  applyState(data) {
    this.firingRate = data.firing_rate;
    const heat = heatmapColor(data.firing_rate);
    this.material.color.copy(heat);
    if (data.spike) {
      this.pulse = 1.0;
    }
  }

  setIsolation(anyIsolated, isIsolated) {
    this.isolated = isIsolated;
    if (!anyIsolated) {
      this.material.opacity = 0.92;
    } else {
      this.material.opacity = isIsolated ? 1.0 : 0.12;
    }
  }

  update(dt) {
    // Emissive pulse decays after a spike.
    if (this.pulse > 0) {
      this.pulse = Math.max(0, this.pulse - dt * 3.0);
    }
    const emissiveStrength = 0.2 + this.pulse * 0.8;
    this.material.emissive.copy(this.material.color).multiplyScalar(emissiveStrength);
    const scale = 1 + this.pulse * 0.18;
    this.mesh.scale.setScalar(scale);
  }
}

export class SynapticArc {
  constructor(scene, fromRegion, toRegion, type) {
    this.type = type;
    this.sourceId = fromRegion.id;
    this.targetId = toRegion.id;
    const from = fromRegion.position.clone();
    const to = toRegion.position.clone();
    // Lift the control point to bow the arc outward.
    const mid = from.clone().add(to).multiplyScalar(0.5);
    const lift = mid.clone().normalize().multiplyScalar(0.9 + from.distanceTo(to) * 0.25);
    mid.add(lift);
    this.curve = new THREE.QuadraticBezierCurve3(from, mid, to);

    this.color = type === "inhibitory" ? new THREE.Color(0xff5252) : new THREE.Color(0x66ff99);
    const geometry = new THREE.TubeGeometry(this.curve, 24, 0.025, 8, false);
    this.material = new THREE.MeshBasicMaterial({
      color: this.color,
      transparent: true,
      opacity: 0.35,
    });
    this.mesh = new THREE.Mesh(geometry, this.material);
    scene.add(this.mesh);
  }

  setStrength(weight) {
    // weight ~ [0,1]; map to opacity for a "thickness" feel without rebuilding.
    this.material.opacity = 0.18 + Math.max(0, Math.min(1, weight)) * 0.6;
  }
}

export class DopamineHalo {
  constructor(scene) {
    const geometry = new THREE.TorusGeometry(4.2, 0.08, 16, 120);
    this.material = new THREE.MeshBasicMaterial({
      color: 0xffd54f,
      transparent: true,
      opacity: 0.3,
      blending: THREE.AdditiveBlending,
    });
    this.mesh = new THREE.Mesh(geometry, this.material);
    this.mesh.rotation.x = Math.PI / 2;
    this.mesh.position.y = 1.0;
    scene.add(this.mesh);
  }

  // dopamine in [0, 2], basal = 1.
  setLevel(dopamine) {
    const drive = Math.max(0, Math.min(2, dopamine)) / 2; // 0..1
    this.material.opacity = 0.12 + drive * 0.6;
    const scale = 0.85 + drive * 0.4;
    this.mesh.scale.set(scale, scale, scale);
  }

  update(dt) {
    this.mesh.rotation.z += dt * 0.2;
  }
}
