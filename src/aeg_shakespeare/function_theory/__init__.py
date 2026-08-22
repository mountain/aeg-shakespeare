"""Optional process-generated function-theory layers.

Addition/Multiplication (A/M) is the first concrete theory implemented here.
The package also exposes a generic finite process-function module abstraction so
other function theories can coexist without changing Shakespeare's core
history/grammar/search interfaces.
"""

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
    "AMFunctionTheory",
    "AMPathFlow",
    "AMPowerWeight",
    "AMPrimitive",
    "AMState",
    "affine_am_frame",
    "ProcessFunctionModule",
    "polynomial_am_module",
]
