"""Predictive Coding module (SPEC-006).

Three-level Rao & Ballard (1999) predictive-coding hierarchy: bottom-up
prediction error, top-down prediction, attention-modulated precision.
"""
from modules.predictive_coding.hierarchy import PredictiveCodingHierarchy
from modules.predictive_coding.layer import PredictiveLayer

__all__ = ["PredictiveCodingHierarchy", "PredictiveLayer"]
