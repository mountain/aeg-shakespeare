"""Finite function modules for process-based function theory.

A function module is represented by a finite basis together with explicit action
rules for named process generators.  The action table is primary; matrices are
not required by the public object.  A symbolic ``ProcessFrame`` can be attached
as a verifier so that a proposed low-complexity function language carries an
exact certificate.

This abstraction is deliberately independent of the Addition/Multiplication
(A/M) calculus.  Elliptic, projective, hyperelliptic, or other process function
theories can use the same finite-module interface when appropriate.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

import sympy as sp

from ..frame import ProcessFrame


Coordinates = tuple[sp.Expr, ...]


@dataclass(frozen=True)
class ProcessFunctionModule:
    """A finite basis closed under declared process-generator actions.

    ``actions[g][j]`` is the coordinate vector of ``g(basis[j])`` in ``basis``.
    The object therefore records a small process action table directly, rather
    than defining the module through eigenvectors or a preferred matrix form.
    """

    basis: tuple[sp.Expr, ...]
    actions: Mapping[str, tuple[Coordinates, ...]]

    def __post_init__(self) -> None:
        basis = tuple(sp.sympify(item) for item in self.basis)
        if not basis:
            raise ValueError("function module requires a non-empty basis")
        object.__setattr__(self, "basis", basis)

        dimension = len(basis)
        if not self.actions:
            raise ValueError("function module requires at least one process action")
        for generator, columns in self.actions.items():
            if not generator:
                raise ValueError("generator names must be non-empty")
            if len(columns) != dimension:
                raise ValueError(
                    f"generator {generator!r} must provide one action column per basis item"
                )
            for coordinates in columns:
                if len(coordinates) != dimension:
                    raise ValueError("action coordinate vectors must match module dimension")

    @property
    def dimension(self) -> int:
        return len(self.basis)

    @property
    def generators(self) -> tuple[str, ...]:
        return tuple(self.actions)

    def action_expression(self, generator: str, basis_index: int) -> sp.Expr:
        """Reconstruct the declared action on one basis element."""

        if generator not in self.actions:
            raise KeyError(f"unknown module generator: {generator!r}")
        coordinates = self.actions[generator][basis_index]
        return sp.expand(
            sum(
                sp.sympify(coefficient) * basis_item
                for coefficient, basis_item in zip(coordinates, self.basis)
            )
        )

    def verification_residuals(self, frame: ProcessFrame) -> Mapping[str, tuple[sp.Expr, ...]]:
        """Verify the declared action table against a symbolic process frame.

        Residuals are returned instead of silently simplifying the module into a
        matrix representation.  A zero residual table certifies exact closure.
        """

        result: dict[str, tuple[sp.Expr, ...]] = {}
        for generator in self.generators:
            if generator not in frame.generators:
                raise KeyError(f"frame does not define module generator {generator!r}")
            residuals = []
            for index, basis_item in enumerate(self.basis):
                declared = self.action_expression(generator, index)
                actual = frame.apply(generator, basis_item)
                residuals.append(sp.simplify(sp.expand(actual - declared)))
            result[generator] = tuple(residuals)
        return result

    def verify(self, frame: ProcessFrame) -> bool:
        """Whether every declared action is exactly certified by ``frame``."""

        return all(
            residual == 0
            for residuals in self.verification_residuals(frame).values()
            for residual in residuals
        )


def polynomial_am_module(
    a: sp.Symbol,
    degree: int,
) -> ProcessFunctionModule:
    """Return the finite polynomial A/M module ``span(1,a,...,a**degree)``.

    This convenience constructor encodes the arithmetic ladder

    ``A a^k = k a^(k-1)``, ``M a^k = k a^k``.

    It is a calibration family for the Addition/Multiplication function theory,
    not a claim that polynomial modules exhaust that theory.
    """

    if degree < 0:
        raise ValueError("degree must be non-negative")
    basis = tuple(a**k for k in range(degree + 1))
    dimension = degree + 1

    addition_columns: list[Coordinates] = []
    multiplication_columns: list[Coordinates] = []
    for k in range(dimension):
        addition = [sp.S.Zero] * dimension
        if k > 0:
            addition[k - 1] = sp.Integer(k)
        addition_columns.append(tuple(addition))

        multiplication = [sp.S.Zero] * dimension
        multiplication[k] = sp.Integer(k)
        multiplication_columns.append(tuple(multiplication))

    return ProcessFunctionModule(
        basis=basis,
        actions={
            "A": tuple(addition_columns),
            "M": tuple(multiplication_columns),
        },
    )
