// Brain Simulator -- canvas2D chart primitives for the SPEC-010 HUD.
//
// These are deliberately plain canvas 2D (NOT Three.js/WebGL -- WebGL is
// reserved for the 3D scene in brain_scene.js). Each chart owns a small
// rolling buffer; callers push new samples once per incoming `frame` message.
// Skipping push() (e.g. while paused) simply freezes the plot in place --
// nothing is corrupted by duplicate or out-of-order frames as long as the
// caller de-duplicates by `timestamp_ms` (see hud.js).

const BG = "#070b14";
const GRID = "#1f2a40";
const ZERO_LINE = "#3a4a6a";

export function colorToCss(intColor) {
  return `#${(intColor >>> 0).toString(16).padStart(6, "0")}`;
}

// Scrolling spike raster: one column pushed per call, one row per (subsampled)
// neuron. Rendered at native (small) resolution and scaled up via CSS
// `image-rendering: pixelated` for a crisp, classic raster look.
export class RasterPlot {
  constructor(canvas, { nNeurons = 64, historyLength = 150, color = "#4fc3f7" } = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.nNeurons = nNeurons;
    this.color = color;
    canvas.width = historyLength;
    canvas.height = nNeurons;
    this.clear();
  }

  setColor(color) {
    this.color = color;
  }

  clear() {
    this.ctx.fillStyle = BG;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
  }

  // spikes: array of 0/1 (or truthy/falsy), length >= nNeurons.
  push(spikes) {
    const { ctx, canvas } = this;
    const w = canvas.width;
    const h = canvas.height;
    // Shift the whole raster one pixel to the left.
    const image = ctx.getImageData(1, 0, w - 1, h);
    ctx.putImageData(image, 0, 0);
    // Draw the new column at the right edge.
    ctx.fillStyle = BG;
    ctx.fillRect(w - 1, 0, 1, h);
    ctx.fillStyle = this.color;
    for (let i = 0; i < this.nNeurons; i++) {
      if (spikes[i]) ctx.fillRect(w - 1, i, 1, 1);
    }
  }
}

// Generic rolling multi-series line chart (firing rate per module, TD-error).
export class LineChart {
  constructor(canvas, { series, maxPoints = 150, yMin = null, yMax = null, zeroLine = false } = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.series = series; // [{id, label, color}]
    this.maxPoints = maxPoints;
    this.fixedYMin = yMin;
    this.fixedYMax = yMax;
    this.zeroLine = zeroLine;
    this.buffers = new Map(series.map((s) => [s.id, []]));
  }

  push(values) {
    for (const s of this.series) {
      const v = values[s.id];
      if (v === undefined) continue;
      const buf = this.buffers.get(s.id);
      buf.push(v);
      if (buf.length > this.maxPoints) buf.shift();
    }
  }

  clear() {
    for (const buf of this.buffers.values()) buf.length = 0;
  }

  draw() {
    const { ctx, canvas } = this;
    const w = canvas.width;
    const h = canvas.height;
    ctx.fillStyle = BG;
    ctx.fillRect(0, 0, w, h);

    let yMin = this.fixedYMin;
    let yMax = this.fixedYMax;
    if (yMin === null || yMax === null) {
      let lo = Infinity;
      let hi = -Infinity;
      for (const buf of this.buffers.values()) {
        for (const v of buf) {
          if (v < lo) lo = v;
          if (v > hi) hi = v;
        }
      }
      if (!isFinite(lo)) {
        lo = 0;
        hi = 1;
      }
      if (lo === hi) {
        lo -= 1;
        hi += 1;
      }
      const pad = (hi - lo) * 0.15;
      if (yMin === null) yMin = lo - pad;
      if (yMax === null) yMax = hi + pad;
    }
    const span = yMax - yMin || 1;

    // Horizontal grid lines.
    ctx.strokeStyle = GRID;
    ctx.lineWidth = 1;
    for (let i = 1; i < 4; i++) {
      const y = (h / 4) * i;
      ctx.beginPath();
      ctx.moveTo(0, y + 0.5);
      ctx.lineTo(w, y + 0.5);
      ctx.stroke();
    }

    if (this.zeroLine && yMin < 0 && yMax > 0) {
      const y = h - ((0 - yMin) / span) * h;
      ctx.strokeStyle = ZERO_LINE;
      ctx.beginPath();
      ctx.moveTo(0, y + 0.5);
      ctx.lineTo(w, y + 0.5);
      ctx.stroke();
    }

    for (const s of this.series) {
      const buf = this.buffers.get(s.id);
      if (buf.length < 2) continue;
      ctx.strokeStyle = s.color;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let i = 0; i < buf.length; i++) {
        const x = (i / (this.maxPoints - 1)) * w;
        const y = h - ((buf[i] - yMin) / span) * h;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }
  }
}
