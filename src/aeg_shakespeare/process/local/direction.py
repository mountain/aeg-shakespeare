"""Experimental local process directions over a declared ``ProcessFrame``.

This module is the first vertical slice for the canonical-observer programme.
A ``ProcessDirection`` is deliberately smaller than a path, flow, solver, or
connection: it is only the local combination

    D = sum_i u_i X_i

of already-declared process generators.  Ordinary assignment ODEs are obtained
only after projecting this process direction to the assignment symbols.

The object is intentionally not reparameterization-invariant.  Two proportional
directions can have different analytic and reconstruction costs (Sundman-type
regularization is the motivating red team), so quotienting them is a task-level
decision rather than process ontology.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import sympy as sp

from .frame import ProcessFrame
from .system import ProcessSystem


@dataclass(frozen=True)
class ProcessDirection:
    """One local linear combination of named process generators.

    Missing frame generators have coefficient zero.  Coefficients may depend on
    assignments, external parameters, or other symbolic local data; the class
    does not interpret where those coefficients came from.
    """

    frame: ProcessFrame
    coefficients: Mapping[str, sp.Expr]
    label: str = ""

    def __post_init__(self) -> None:
        unknown = set(self.coefficients) - set(self.frame.names)
        if unknown:
            raise ValueError(
                "direction coefficients reference unknown generators: "
                f"{sorted(unknown)}"
            )
        normalized = {
            name: sp.expand(sp.sympify(value))
            for name, value in self.coefficients.items()
        }
        object.__setattr__(self, "coefficients", normalized)

    def coefficient(self, generator: str) -> sp.Expr:
        if generator not in self.frame.generators:
            raise KeyError(f"unknown process generator: {generator!r}")
        return sp.sympify(self.coefficients.get(generator, sp.S.Zero))

    def apply(self, expr: sp.Expr) -> sp.Expr:
        """Apply the combined process direction to one symbolic expression."""

        out = sp.S.Zero
        for generator in self.frame.names:
            coefficient = self.coefficient(generator)
            if coefficient != 0:
                out += coefficient * self.frame.apply(generator, expr)
        return sp.expand(out)

    def assignment_rules(self) -> Mapping[sp.Symbol, sp.Expr]:
        """Return the assignment shadow of this process direction."""

        return {
            assignment: self.apply(assignment)
            for assignment in self.frame.assignments
        }

    def as_system(self, *, name: str = "D") -> ProcessSystem:
        """Lower the direction to the existing one-generator symbolic backend."""

        return ProcessSystem(
            assignments=self.frame.assignments,
            rules=self.assignment_rules(),
            name=name,
        )


__all__ = ["ProcessDirection"]
