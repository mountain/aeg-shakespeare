"""One-generator local process realizations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import sympy as sp


@dataclass(frozen=True)
class ProcessSystem:
    """A named derivation-style representation of a local process generator.

    ``derive`` is one symbolic realization of process action. Shakespeare does
    not equate this backend with the full process-history ontology.
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
        for assignment in self.assignments:
            out += sp.diff(expr, assignment) * self.rules[assignment]
        return sp.expand(out)

    def iterate(self, expr: sp.Expr, depth: int) -> list[sp.Expr]:
        """Return ``[expr, D(expr), ..., D**depth(expr)]``."""
        if depth < 0:
            raise ValueError("depth must be non-negative")
        orbit = [sp.expand(sp.sympify(expr))]
        for _ in range(depth):
            orbit.append(self.derive(orbit[-1]))
        return orbit
