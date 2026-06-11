"""SPEC-012 acceptance criterion -- 10s simulation logs to HDF5 under 50MB.

Runs a full 10,000-tick (10s at dt=1ms) demo-brain simulation with
:class:`~core.instrumentation.InstrumentationLogger` attached and checks the
resulting HDF5 file stays under the 50MB budget. Lives alongside the other
acceptance-criteria runs in ``tests/scientific`` because a real 10s run is
slow (~2 minutes) -- ``tests/unit/test_instrumentation.py`` covers the
logger's correctness on short runs.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.instrumentation import InstrumentationConfig, InstrumentationLogger  # noqa: E402
from visualization.demo_brain import build_demo_brain  # noqa: E402


def test_10s_simulation_hdf5_under_50mb(tmp_path):
    engine = build_demo_brain(n_neurons=50, seed=3)
    config = InstrumentationConfig(
        output_dir=tmp_path, run_name="run_10s", log_every_n_steps=10
    )
    logger = InstrumentationLogger(config)
    engine.register_state_renderer(logger.record)

    n_steps = 10_000  # 10s of simulated time at dt=1ms.
    for _ in range(n_steps):
        engine.step()
    logger.close()

    assert logger.sampled_steps == n_steps // config.log_every_n_steps

    size_mb = logger.hdf5_path.stat().st_size / (1024 * 1024)
    assert size_mb < 50, f"HDF5 output is {size_mb:.2f}MB, expected < 50MB"
