"""Core process-presentation objects.

The ontology here is deliberately small: assignments, process action rules,
and ordered derivation histories. SymPy is used as an algebra backend, not as
the definition of process equality.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

import sympy as sp


@dataclass(frozen=True)
class ProcessSystem:
    """A derivation-style representation of a local process presentation.

    Parameters
    ----------
    assignments:
        The assignment symbols visible in this representation.
    rules:
        Generator action table ``D(a_i) = expression``.

    Notes
    -----
    ``derive`` is a *representation backend* for a process generator. The
    project intentionally does not equate this SymPy derivation with the full
    history ontology.
    """

    assignments: tuple[sp.Symbol, ...]
    rules: Mapping[sp.Symbol, sp.Expr]
    name: str = "D"

    def __post_init__(self) -> None:
        missing = [a for a in self.assignments if a not in self.rules]
        if missing:
            raise ValueError(f"missing process rules for assignments: {missing}")

    def derive(self, expr: sp.Expr) -> sp.Expr:
        """Apply the represented process generator using the Leibniz chain rule."""
        expr = sp.sympify(expr)
        out = sp.S.Zero
        for a in self.assignments:
            out += sp.diff(expr, a) * self.rules[a]
        return sp.expand(out)

    def iterate(self, expr: sp.Expr, depth: int) -> list[sp.Expr]:
        """Return ``[expr, D(expr), ..., D**depth(expr)]``."""
        if depth < 0:
            raise ValueError("depth must be non-negative")
        orbit = [sp.expand(sp.sympify(expr))]
        for _ in range(depth):
            orbit.append(self.derive(orbit[-1]))
        return orbit


def homogeneous_monomials(assignments: Sequence[sp.Symbol], degree: int) -> list[sp.Expr]:
    """Enumerate commutative monomials of fixed total degree.

    v0.1 intentionally uses a commutative assignment algebra. Ordered process
    composition is kept at the process level; later versions can swap this
    backend without changing the presentation API.
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
            monomial *= symbol ** exponent
        result.append(sp.expand(monomial))
    return result
