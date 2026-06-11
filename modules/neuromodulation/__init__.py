"""Brain Simulator -- Neuromodulation (SPEC-008).

Global neuromodulatory channels broadcast by the
:class:`~core.simulation_engine.SimulationEngine` to every module each tick:

    * :class:`~modules.neuromodulation.dopamine.DopamineSystem` -- TD-error.
    * :class:`~modules.neuromodulation.noradrenaline.NoradrenalineSystem` -- arousal.
    * :class:`~modules.neuromodulation.acetylcholine.AcetylcholineSystem` -- attention/SNR.

:class:`~modules.neuromodulation.system.NeuromodulatorSystem` centralises the
three channels behind the frozen SPEC-001
:class:`~core.interfaces.CognitiveModule` contract.
"""
from modules.neuromodulation.acetylcholine import AcetylcholineSystem
from modules.neuromodulation.dopamine import DopamineSystem
from modules.neuromodulation.noradrenaline import NoradrenalineSystem
from modules.neuromodulation.system import NeuromodulatorSystem

__all__ = [
    "DopamineSystem",
    "NoradrenalineSystem",
    "AcetylcholineSystem",
    "NeuromodulatorSystem",
]
