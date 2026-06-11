"""Brain Simulator -- Reasoning modules (SPEC-007).

Exposes :class:`~modules.reasoning.model_free.ModelFreeRL`,
:class:`~modules.reasoning.model_based.ModelBasedRL`,
:class:`~modules.reasoning.pfc.PFCExecutive` and
:class:`~modules.reasoning.decision_gate.DecisionGate`, all conforming to the
frozen SPEC-001 :class:`~core.interfaces.CognitiveModule` contract.
"""
from modules.reasoning.decision_gate import DecisionGate
from modules.reasoning.model_based import ModelBasedRL
from modules.reasoning.model_free import ModelFreeRL
from modules.reasoning.pfc import PFCExecutive

__all__ = ["ModelFreeRL", "ModelBasedRL", "PFCExecutive", "DecisionGate"]
