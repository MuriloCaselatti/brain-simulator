"""SPEC-013 -- TD-error reproduces the Schultz (1997) dopamine signal.

Schultz, Dayan & Montague (1997) showed that midbrain dopamine neurons encode
a **reward-prediction error**, not reward per se:

    1. an *unexpected* reward elicits a phasic **burst**;
    2. once the reward is *fully predicted*, the burst **transfers away** from
       the reward and the response at reward time decays to baseline; and
    3. *omission* of a predicted reward produces a phasic **dip** below
       baseline at the expected reward time.

These are exactly the sign and dynamics of the temporal-difference error
``delta = r + gamma * V(s') - V(s)`` learned online. This suite drives the
SPEC-003 :class:`~core.learning_engine.LearningEngine` value learner through
the canonical single-cue conditioning protocol and checks that the TD signal
-- and the SPEC-008 :class:`~modules.neuromodulation.DopamineSystem` that reads
it -- reproduce all three phenomena.

References:
    * Schultz, Dayan & Montague (1997). A neural substrate of prediction and
      reward. Science 275: 1593-1599.
    * Sutton & Barto (1998/2018). Reinforcement Learning, ch. 6 (TD learning).
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from core.learning_engine import LearningEngine  # noqa: E402
from modules.neuromodulation import DopamineSystem  # noqa: E402


def _train_until_predicted(reward: float = 1.0, n_trials: int = 80):
    """Run single-state TD conditioning and return the TD-error trajectory.

    ``gamma = 0`` makes each trial a terminal one-step prediction
    ``delta = reward - V``; repeated updates drive ``V -> reward`` so the TD
    error decays from an initial burst to ~0 (the Schultz "response transfer").
    """
    engine = LearningEngine(gamma=0.0)
    trajectory = []
    for _ in range(n_trials):
        td = engine.compute_td_error(reward=reward, value_next=0.0)
        trajectory.append(td)
        engine.apply_td_update(td)
    return engine, np.array(trajectory)


# --- Phenomenon 1: unexpected reward -> positive TD (burst) ------------------


def test_unexpected_reward_produces_positive_td_burst():
    """On the first, fully unexpected reward the TD error is strongly positive
    and the dopamine channel responds with a burst above its basal level."""
    engine = LearningEngine(gamma=0.0)
    engine.value_estimate = 0.0  # nothing predicted yet

    td = engine.compute_td_error(reward=1.0, value_next=0.0)
    assert td == pytest.approx(1.0)

    da = DopamineSystem(gain=1.0, tau_ms=50.0)
    da.set_td_error(td)
    assert da.step(1.0) > 1.0  # phasic burst


# --- Phenomenon 2: response transfers away as reward becomes predicted -------


def test_response_decays_as_reward_becomes_predicted():
    """Across trials the TD error decays monotonically from the initial burst
    toward zero as the value estimate learns to predict the reward."""
    engine, trajectory = _train_until_predicted(reward=1.0)

    assert trajectory[0] == pytest.approx(1.0)          # initial burst
    assert trajectory[-1] == pytest.approx(0.0, abs=0.05)  # vanishes once predicted
    assert np.all(np.diff(trajectory) < 0)              # strictly decaying
    assert engine.value_estimate == pytest.approx(1.0, abs=0.05)


def test_fully_predicted_reward_evokes_no_dopamine_response():
    """After learning, delivering the predicted reward yields ~basal dopamine
    (no burst) -- the hallmark of a fully predicted outcome."""
    engine, _ = _train_until_predicted(reward=1.0)

    td_predicted = engine.compute_td_error(reward=1.0, value_next=0.0)
    assert td_predicted == pytest.approx(0.0, abs=0.05)

    da = DopamineSystem(gain=1.0, tau_ms=50.0)
    da.set_td_error(td_predicted)
    assert da.step(1.0) == pytest.approx(1.0, abs=0.05)  # stays at baseline


# --- Phenomenon 3: omission of a predicted reward -> negative TD (dip) --------


def test_omission_of_predicted_reward_produces_negative_td_dip():
    """Once a reward is predicted, omitting it drives the TD error negative and
    the dopamine channel dips below baseline at the expected reward time."""
    engine, _ = _train_until_predicted(reward=1.0)

    td_omission = engine.compute_td_error(reward=0.0, value_next=0.0)
    assert td_omission < 0
    assert td_omission == pytest.approx(-engine.value_estimate, abs=1e-6)

    da = DopamineSystem(gain=1.0, tau_ms=50.0)
    da.set_td_error(td_omission)
    assert da.step(1.0) < 1.0  # phasic dip


# --- Discounting: future value contributes to the prediction error -----------


def test_td_error_discounts_future_value():
    """With gamma > 0 an unexpected future value also drives a positive TD
    error, scaled by the discount factor (``delta = r + gamma V' - V``)."""
    engine = LearningEngine(gamma=0.95)
    engine.value_estimate = 0.0

    td = engine.compute_td_error(reward=0.0, value_next=1.0)
    assert td == pytest.approx(0.95)
