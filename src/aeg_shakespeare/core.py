"""Core public abstractions for AEG Shakespeare.

The library keeps process structure separate from the symbolic backend.  A
``ProcessSystem`` is only one concrete representation: a named derivation acting
on an assignment algebra.  Histories, relations, search budgets, and costs live
at the Shakespeare level and are not defined by ``sympy.simplify``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, Mapping, Sequence, TypeVar

import sympy as sp

StepT = TypeVar("StepT")
StateT = TypeVar("StateT")


@dataclass(frozen=True)
class ProcessWord(Generic[StepT]):
    """An ordered finite process history.

    ``ProcessWord`` deliberately stores steps without interpreting them.  The
    same history can therefore be given different semantics by different
    presentations or observers.
    """

    steps: tuple[StepT, ...] = ()

    def __iter__(self) -> Iterator[StepT]:
        return iter(self.steps)

    def __len__(self) -> int:
        return len(self.steps)

    @property
    def depth(self) -> int:
        return len(self.steps)

    def then(self, step: StepT) -> "ProcessWord[StepT]":
        return ProcessWord(self.steps + (step,))

    def compose(self, other: "ProcessWord[StepT]") -> "ProcessWord[StepT]":
        return ProcessWord(self.steps + other.steps)


@dataclass(frozen=True)
class SearchBudget:
    """Finite search limits for local representation discovery.

    Shakespeare intentionally treats bounded search as part of the public
    contract: the general word/relation problem need not be decidable.
    """

    max_history_depth: int = 8
    max_expression_degree: int = 4
    max_relation_order: int = 8
    max_new_primitives: int = 8

    def __post_init__(self) -> None:
        values = (
            self.max_history_depth,
            self.max_expression_degree,
            self.max_relation_order,
            self.max_new_primitives,
        )
        if any(value < 0 for value in values):
            raise ValueError("search-budget values must be non-negative")


@dataclass(frozen=True)
class ProcessSystem:
    """A named derivation-style representation of a local process generator.

    Parameters
    ----------
    assignments:
        Assignment symbols visible in this representation.
    rules:
        Generator action table ``D(a_i) = expression``.

    Notes
    -----
    ``derive`` is a symbolic backend for one process generator.  Shakespeare
    does not equate this representation with the full process-history ontology.
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


def interpret_history(
    history: ProcessWord[StepT],
    initial: StateT,
    transition,
) -> StateT:
    """Interpret an ordered history under a caller-supplied transition rule.

    The transition function has signature ``transition(state, step) -> state``.
    Keeping the interpreter generic lets tests and downstream packages define
    finite operation semantics without baking any benchmark into the library.
    """

    state = initial
    for step in history:
        state = transition(state, step)
    return state


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
