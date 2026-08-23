"""Compatibility/backend module after semantic core decomposition.

Canonical semantic ownership is now:

- ``ProcessWord`` and ``interpret_history`` -> ``process.history``;
- ``ProcessSystem`` -> ``process.local``;
- ``SearchBudget`` -> ``presentation.budget``.

This module retains those identity-preserving imports for pre-refactor internal
paths and keeps ``homogeneous_monomials`` as a small SymPy backend helper. It is
no longer the architectural center of the public API.
"""

from __future__ import annotations

from typing import Sequence

import sympy as sp

from .presentation.budget import SearchBudget
from .process.history import ProcessWord, interpret_history
from .process.local import ProcessSystem


def homogeneous_monomials(assignments: Sequence[sp.Symbol], degree: int) -> list[sp.Expr]:
    """Enumerate commutative monomials of fixed total degree.

    This is a SymPy-backend utility, not a restriction on the process ontology.
    """
    if degree < 0:
        raise ValueError("degree must be non-negative")
    assignments = tuple(assignments)
    if not assignments:
        return [sp.S.One] if degree == 0 else []

    def compositions(total: int, n: int):
        if n == 1:
            yield (total,)
            return
        for i in range(total, -1, -1):
            for rest in compositions(total - i, n - 1):
                yield (i,) + rest

    result: list[sp.Expr] = []
    for exponents in compositions(degree, len(assignments)):
        monomial = sp.S.One
        for symbol, exponent in zip(assignments, exponents):
            monomial *= symbol**exponent
        result.append(sp.expand(monomial))
    return result


__all__ = [
    "ProcessWord",
    "interpret_history",
    "ProcessSystem",
    "SearchBudget",
    "homogeneous_monomials",
]
