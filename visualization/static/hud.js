// Brain Simulator -- floating scientific HUD (SPEC-010).
//
// Builds on the SPEC-009 WebSocket stream: a per-module spike raster, a
// firing-rate line per module, and the TD-error temporal signal. All plots use
// canvas 2D (charts.js) -- WebGL stays in brain_scene.js for the 3D scene.

import { RasterPlot, LineChart, colorToCss } from "./charts.js";

const RATE_Y_MAX_HZ = 60;

export class Hud {
  constructor() {
    this.regions = [];
    this.raster = null;
    this.rateChart = null;
    this.tdChart = null;
    this.selectedModule = null;
    this.lastTimestampMs = null;

    this.rasterCanvas = document.getElementById("raster-canvas");
    this.rateCanvas = document.getElementById("rate-canvas");
    this.tdCanvas = document.getElementById("td-canvas");
    this.select = document.getElementById("raster-select");
    this.legend = document.getElementById("rate-legend");
  }

  // Called once per WebSocket connection when the `layout` message arrives.
  build(layout) {
    this.regions = layout.regions;
    this.selectedModule = this.regions[0]?.id ?? null;

    this._buildSelector();
    this._buildLegend();

    if (this.rasterCanvas) {
      const color = colorToCss(this._selectedColor());
      this.raster = new RasterPlot(this.rasterCanvas, { nNeurons: 64, color });
    }
    if (this.rateCanvas) {
      const series = this.regions.map((r) => ({
        id: r.id,
        label: r.label,
        color: colorToCss(r.color),
      }));
      this.rateChart = new LineChart(this.rateCanvas, {
        series,
        maxPoints: 150,
        yMin: 0,
        yMax: RATE_Y_MAX_HZ,
      });
    }
    if (this.tdCanvas) {
      this.tdChart = new LineChart(this.tdCanvas, {
        series: [{ id: "td", label: "TD-error", color: "#ffd54f" }],
        maxPoints: 150,
        zeroLine: true,
      });
    }
    this.lastTimestampMs = null;
  }

  // Called for every streamed `frame` message.
  applyFrame(frame) {
    if (!this.rateChart && !this.tdChart && !this.raster) return;

    // The broadcaster re-sends the latest frame ~30x/s even while paused (and
    // a reset rewinds the clock). De-duplicate / clear so pause-resume-replay
    // never corrupts the rolling buffers.
    if (this.lastTimestampMs !== null) {
      if (frame.timestamp_ms === this.lastTimestampMs) return;
      if (frame.timestamp_ms < this.lastTimestampMs) {
        this.raster?.clear();
        this.rateChart?.clear();
        this.tdChart?.clear();
      }
    }
    this.lastTimestampMs = frame.timestamp_ms;

    const rates = {};
    let rasterRow = null;
    for (const region of frame.regions) {
      rates[region.id] = region.firing_rate;
      if (region.id === this.selectedModule) rasterRow = region.raster;
    }

    if (this.rateChart) {
      this.rateChart.push(rates);
      this.rateChart.draw();
    }
    if (this.tdChart) {
      this.tdChart.push({ td: frame.td_error ?? 0 });
      this.tdChart.draw();
    }
    if (this.raster && rasterRow) {
      this.raster.push(rasterRow);
    }
  }

  // -- internals ------------------------------------------------------------

  _selectedColor() {
    return this.regions.find((r) => r.id === this.selectedModule)?.color ?? 0x4fc3f7;
  }

  _buildSelector() {
    if (!this.select) return;
    this.select.innerHTML = "";
    for (const region of this.regions) {
      const opt = document.createElement("option");
      opt.value = region.id;
      opt.textContent = region.label;
      this.select.appendChild(opt);
    }
    this.select.value = this.selectedModule;
    this.select.onchange = () => {
      this.selectedModule = this.select.value;
      this.raster?.setColor(colorToCss(this._selectedColor()));
      this.raster?.clear();
    };
  }

  _buildLegend() {
    if (!this.legend) return;
    this.legend.innerHTML = "";
    for (const region of this.regions) {
      const row = document.createElement("div");
      row.className = "legend-row";
      const swatch = document.createElement("div");
      swatch.className = "swatch";
      swatch.style.background = colorToCss(region.color);
      row.appendChild(swatch);
      row.appendChild(document.createTextNode(region.label));
      this.legend.appendChild(row);
    }
  }
}
