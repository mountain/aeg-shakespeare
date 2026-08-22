"""Constraint-quotient quickstart for AEG Shakespeare 0.0.1.

A relation is treated as part of the represented process space, not merely as an
expression to simplify away.  The Groebner backend supplies an exact quotient
certificate while Shakespeare keeps that equality layer explicit.
"""

import sympy as sp

from aeg_shakespeare import AlgebraicConstraintSet

x, y = sp.symbols("x y")
quotient = AlgebraicConstraintSet(
    variables=(x, y),
    relations=(x**2 + y**2 - 1,),
)

expr = x**2 + y**2
print("normal remainder:", quotient.reduce(expr))
print("equal to 1 modulo the constraint:", quotient.equivalent(expr, 1))
