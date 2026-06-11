"""SPEC-013 -- Working memory persistent activity (Compte 2000).

Compte, Brunel, Goldman-Rakic & Wang (2000) modelled prefrontal working memory
as a recurrent attractor network whose hallmark is **delay-period persistent
activity**: a transient cue drives a population into a self-sustaining
high-activity state that outlasts the stimulus, holding the memory across a
delay with no further input. The same network is selective (it does not switch
to a memory on a weak, sub-threshold distractor) and silent in the absence of a
cue.

This suite validates the SPEC-004 :class:`~modules.memory.working.WorkingMemory`
attractor network against those three properties, the mandatory SPEC-013
"Working Memory / Compte 2000 / persistence post-stimulus" criterion.

References:
    * Compte, Brunel, Goldman-Rakic & Wang (2000). Synaptic mechanisms and
      network dynamics underlying spatial working memory. Cereb. Cortex 10(9).
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.interfaces import ModuleInputs, NeuromodulationSignal  # noqa: E402
from modules.memory.working import WorkingMemory  # noqa: E402

N_NEURONS = 70
CUE_MS = 50
DELAY_MS = 500


def _inputs(spike_trains: np.ndarray, timestamp_ms: float) -> ModuleInputs:
    return ModuleInputs(
        spike_trains=np.asarray(spike_trains, dtype=float),
        attention_signal=1.0,
        neuromodulation=NeuromodulationSignal(),
        timestamp_ms=timestamp_ms,
    )


def _pool_cue(wm: WorkingMemory, pool: int) -> np.ndarray:
    """A cue that fully overlaps attractor ``pool``."""
    per = wm._neurons_per_attractor
    cue = np.zeros(wm.n_neurons)
    cue[pool * per : (pool + 1) * per] = 1.0
    return cue


def _present(wm: WorkingMemory, cue: np.ndarray, n_ms: int, start_ms: float):
    out = None
    for t in range(n_ms):
        out = wm.update(1.0, _inputs(cue, start_ms + t))
    return out


# --- Persistence after stimulus removal (the core Compte 2000 result) --------


def test_persistent_activity_outlasts_the_cue():
    """A brief cue drives an attractor high; with the cue removed the activity
    persists at the high fixed point for the whole delay period."""
    wm = WorkingMemory(n_neurons=N_NEURONS)
    target = 3

    out = _present(wm, _pool_cue(wm, target), CUE_MS, start_ms=0.0)
    assert out.internal_state["active_attractor"] == target
    level_after_cue = out.internal_state["level"]
    assert level_after_cue > 0.8  # driven into the high-activity state

    # Delay period: NO input at all.
    out = _present(wm, np.zeros(N_NEURONS), DELAY_MS, start_ms=CUE_MS)

    assert out.internal_state["active_attractor"] == target  # same memory held
    assert out.internal_state["level"] > 0.8  # still in the high fixed point
    # Firing of the remembered pool remains elevated.
    per = wm._neurons_per_attractor
    pool_rate = out.firing_rate[target * per : (target + 1) * per]
    assert np.all(pool_rate > 0.5 * wm._max_rate_hz)


def test_no_persistent_activity_without_a_cue():
    """With no cue ever presented the network stays in its low (silent) fixed
    point -- persistent activity is cue-triggered, not spontaneous."""
    wm = WorkingMemory(n_neurons=N_NEURONS)

    out = _present(wm, np.zeros(N_NEURONS), CUE_MS + DELAY_MS, start_ms=0.0)

    assert out.internal_state["active_attractor"] is None
    assert out.internal_state["level"] < 0.1
    assert np.all(out.firing_rate < 0.5 * wm._max_rate_hz)


def test_memory_is_selective_to_strong_cues():
    """Once a memory is held, a weak distractor whose overlap is below the
    match threshold does not capture the network -- the original memory
    survives the distractor."""
    wm = WorkingMemory(n_neurons=N_NEURONS)
    target = 2

    _present(wm, _pool_cue(wm, target), CUE_MS, start_ms=0.0)

    # A weak distractor on a *different* pool: only a couple of its units are
    # active, so the normalized overlap stays below match_threshold (0.5).
    per = wm._neurons_per_attractor
    distractor = np.zeros(N_NEURONS)
    other = 5
    distractor[other * per : other * per + max(1, per // 4)] = 1.0

    out = _present(wm, distractor, 100, start_ms=CUE_MS)

    assert out.internal_state["active_attractor"] == target  # not captured
    assert out.internal_state["level"] > 0.8
