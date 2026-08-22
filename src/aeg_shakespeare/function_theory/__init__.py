"""Optional process-generated function-theory layers.

Addition/Multiplication (A/M) is the first concrete arithmetic theory.  Algebraic
quotient profiles provide a second route for processes whose reduced geometry
forces elliptic/Abelian or higher-genus function languages.
"""

from .algebraic import HyperellipticProfile, hyperelliptic_profile
from .am import (
    AMFunctionTheory,
    AMPathFlow,
    AMPowerWeight,
    AMPrimitive,
    AMState,
    affine_am_frame,
)
from .module import ProcessFunctionModule, polynomial_am_module

__all__ = [
    "HyperellipticProfile",
    "hyperelliptic_profile",
    "AMFunctionTheory",
    "AMPathFlow",
    "AMPowerWeight",
    "AMPrimitive",
    "AMState",
    "affine_am_frame",
    "ProcessFunctionModule",
    "polynomial_am_module",
]
