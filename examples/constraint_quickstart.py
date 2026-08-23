"""Constraint-quotient quickstart using the semantic public namespaces.

A relation is treated as part of the represented presentation space, not merely
as an expression to simplify away. The Groebner backend supplies an exact
quotient certificate while Process Geometry keeps that equality layer explicit.
"""

import sympy as sp

from process_geometry.presentation.constraints import AlgebraicConstraintSet

x, y = sp.symbols("x y")
quotient = AlgebraicConstraintSet(
    variables=(x, y),
    relations=(x**2 + y**2 - 1,),
)

expr = x**2 + y**2
print("normal remainder:", quotient.reduce(expr))
print("equal to 1 modulo the constraint:", quotient.equivalent(expr, 1))
