"""Linear/Krylov calibration backend.

This module exists to verify that ordinary linear-algebra structure can be
recovered *from process return relations*. Eigen/Jordan data are intentionally
not part of the discovery API.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from math import gcd

import sympy as sp


@dataclass(frozen=True)
class KrylovReturnRelation:
    coefficients: tuple[sp.Expr, ...]

    @property
    def order(self) -> int:
        return len(self.coefficients) - 1

    def as_polynomial(self, symbol: sp.Symbol | None = None) -> sp.Expr:
        z = symbol or sp.Symbol("X")
        return sp.expand(sum(c * z**i for i, c in enumerate(self.coefficients)))


def _primitive(v: sp.Matrix) -> tuple[sp.Expr, ...]:
    qs = [sp.Rational(x) for x in v]
    lcm = sp.ilcm(*[q.q for q in qs]) if qs else 1
    ints = [int(q * lcm) for q in qs]
    nz = [abs(i) for i in ints if i]
    common = reduce(gcd, nz) if nz else 1
    ints = [i // common for i in ints]
    if next((i for i in ints if i), 1) < 0:
        ints = [-i for i in ints]
    return tuple(sp.Integer(i) for i in ints)


def discover_krylov_relation(
    operator: sp.Matrix,
    vector: sp.Matrix,
    max_order: int | None = None,
) -> KrylovReturnRelation | None:
    """Discover the shortest bounded recurrence in ``v, Xv, X^2v, ...``."""
    operator = sp.Matrix(operator)
    vector = sp.Matrix(vector)
    if operator.rows != operator.cols:
        raise ValueError("operator must be square")
    if vector.rows != operator.rows or vector.cols != 1:
        raise ValueError("vector must be a compatible column vector")
    bound = max_order if max_order is not None else operator.rows + 1
    orbit = [vector]
    for _ in range(bound):
        orbit.append(operator * orbit[-1])
    for order in range(1, bound + 1):
        matrix = sp.Matrix.hstack(*orbit[: order + 1])
        candidates = [v for v in matrix.nullspace() if v[-1] != 0]
        if candidates:
            coeffs = _primitive(candidates[0])
            certificate = sum(
                (coeffs[i] * orbit[i] for i in range(order + 1)),
                sp.zeros(operator.rows, 1),
            )
            if certificate != sp.zeros(operator.rows, 1):
                raise AssertionError("Krylov return-relation verification failed")
            return KrylovReturnRelation(coeffs)
    return None
