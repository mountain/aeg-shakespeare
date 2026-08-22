"""Generic symbolic frames with multiple ordered process generators.

A ``ProcessFrame`` is a representation backend for several named derivations on
one assignment algebra.  It connects Shakespeare's literal ``ProcessWord``
layer to symbolic process calculus without assuming that the generators commute
or that a particular Lie algebra is universal.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import sympy as sp

from .core import ProcessWord


@dataclass(frozen=True)
class ProcessFrame:
    """A finite family of named derivations on a symbolic assignment algebra.

    ``generators`` maps each generator name to its action on every assignment
    symbol.  Generator composition is ordered.  No commutator relation is
    assumed unless it follows from these actions or is supplied elsewhere as a
    process relation.
    """

    assignments: tuple[sp.Symbol, ...]
    generators: Mapping[str, Mapping[sp.Symbol, sp.Expr]]

    def __post_init__(self) -> None:
        if not self.assignments:
            raise ValueError("process frame requires at least one assignment")
        if not self.generators:
            raise ValueError("process frame requires at least one generator")
        for name, rules in self.generators.items():
            if not name:
                raise ValueError("generator names must be non-empty")
            missing = [symbol for symbol in self.assignments if symbol not in rules]
            if missing:
                raise ValueError(f"generator {name!r} is missing rules for {missing}")

    @property
    def names(self) -> tuple[str, ...]:
        return tuple(self.generators)

    def apply(self, generator: str, expr: sp.Expr) -> sp.Expr:
        """Apply one named derivation using the Leibniz/chain rule."""

        if generator not in self.generators:
            raise KeyError(f"unknown process generator: {generator!r}")
        expr = sp.sympify(expr)
        rules = self.generators[generator]
        out = sp.S.Zero
        for assignment in self.assignments:
            out += sp.diff(expr, assignment) * rules[assignment]
        return sp.expand(out)

    def apply_word(self, word: ProcessWord[str], expr: sp.Expr) -> sp.Expr:
        """Apply generators in literal process-history order.

        For ``ProcessWord((\"A\", \"M\"))`` the result is ``M(A(expr))``: the
        first recorded step acts first.  This convention matches Shakespeare's
        execution-history semantics and is deliberately explicit about the
        distinction between history order and conventional right-to-left
        operator notation.
        """

        value = sp.sympify(expr)
        for generator in word:
            value = self.apply(generator, value)
        return sp.expand(value)

    def commutator(self, left: str, right: str, expr: sp.Expr) -> sp.Expr:
        """Return ``[left,right] expr = left(right(expr))-right(left(expr))``."""

        return sp.expand(
            self.apply(left, self.apply(right, expr))
            - self.apply(right, self.apply(left, expr))
        )

    def iterate(self, generator: str, expr: sp.Expr, count: int) -> sp.Expr:
        """Apply one generator repeatedly ``count`` times."""

        if count < 0:
            raise ValueError("count must be non-negative")
        value = sp.sympify(expr)
        for _ in range(count):
            value = self.apply(generator, value)
        return sp.expand(value)
