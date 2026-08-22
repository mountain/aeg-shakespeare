"""Additive central residuals for finite process-family composition.

This module is intentionally narrower than a central-extension or cohomology
framework.  It records one structure now forced independently by Galilean
mechanics and magnetic translations:

* a visible ``ProcessFamily`` has its ordinary parameter-composition law;
* a lifted realization may compose with an additional additive scalar residual
  ``omega(g, h)``; and
* associativity of the lifted composition is exactly the 2-cocycle identity.

The central value is represented by a SymPy expression and combined additively.
It may be an action-like quantity, a phase exponent, or another caller-defined
central coordinate.  Shakespeare does not identify it with U(1), choose a
quantization convention, quotient cocycles by coboundaries, or construct a full
central-extension group.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Generic, Sequence, TypeVar

import sympy as sp

from .families import ProcessFamily

ParamT = TypeVar("ParamT")


@dataclass(frozen=True)
class ProcessCocycle(Generic[ParamT]):
    """An additive central composition residual over one ``ProcessFamily``.

    For a visible composition ``g*h``, a lifted realization is represented by

    ``(g, z) * (h, w) = (g*h, z + w + omega(g, h))``.

    The object stores only ``omega`` and the visible family.  Whether a given
    residual is physically a phase, action, charge, mass contribution, flux, or
    something else belongs to the caller's realization.
    """

    family: ProcessFamily[ParamT]
    residual: Callable[[ParamT, ParamT], sp.Expr] = field(repr=False, compare=False)
    label: object | None = None
    simplify: Callable[[sp.Expr], sp.Expr] = field(
        default=sp.simplify,
        repr=False,
        compare=False,
    )

    def value(self, left: ParamT, right: ParamT) -> sp.Expr:
        return sp.sympify(self.simplify(sp.sympify(self.residual(left, right))))

    def cocycle_residual(self, first: ParamT, second: ParamT, third: ParamT) -> sp.Expr:
        """Residual of the additive 2-cocycle identity.

        Exact associativity of lifted composition requires

        ``omega(g,h) + omega(g*h,k) = omega(h,k) + omega(g,h*k)``.
        """

        gh = self.family.compose_parameters(first, second)
        hk = self.family.compose_parameters(second, third)
        residual = (
            self.value(first, second)
            + self.value(gh, third)
            - self.value(second, third)
            - self.value(first, hk)
        )
        return sp.sympify(self.simplify(sp.expand(residual)))

    def compose_lifted(
        self,
        left: tuple[ParamT, sp.Expr],
        right: tuple[ParamT, sp.Expr],
    ) -> tuple[ParamT, sp.Expr]:
        """Compose two lifted elements using the declared central residual."""

        left_parameter, left_central = left
        right_parameter, right_central = right
        parameter = self.family.compose_parameters(left_parameter, right_parameter)
        central = self.simplify(
            sp.sympify(left_central)
            + sp.sympify(right_central)
            + self.value(left_parameter, right_parameter)
        )
        return parameter, sp.sympify(central)


@dataclass(frozen=True)
class CocycleVerification:
    """Bounded exact certificate for a ``ProcessCocycle``."""

    cocycle_residuals: tuple[sp.Expr, ...]
    normalization_residuals: tuple[sp.Expr, ...] = ()

    @property
    def exact(self) -> bool:
        return all(
            residual == 0
            for residual in (*self.cocycle_residuals, *self.normalization_residuals)
        )


def verify_process_cocycle(
    cocycle: ProcessCocycle[ParamT],
    triples: Sequence[tuple[ParamT, ParamT, ParamT]],
    *,
    normalization_parameters: Sequence[ParamT] = (),
) -> CocycleVerification:
    """Verify the cocycle law and optional identity normalization exactly.

    Like the family/character verification layer, this is a bounded certificate.
    Symbolic triples may establish identities over an unbounded parameter domain
    when the backend simplifies the resulting residuals exactly.
    """

    cocycle_residuals = tuple(
        cocycle.cocycle_residual(first, second, third)
        for first, second, third in triples
    )

    normalization: list[sp.Expr] = []
    if normalization_parameters:
        if cocycle.family.identity is None:
            raise ValueError("cocycle normalization requires a declared family identity")
        identity = cocycle.family.identity
        for parameter in normalization_parameters:
            normalization.append(cocycle.value(identity, parameter))
            normalization.append(cocycle.value(parameter, identity))

    return CocycleVerification(
        cocycle_residuals=cocycle_residuals,
        normalization_residuals=tuple(normalization),
    )


def central_commutator_residual(
    cocycle: ProcessCocycle[ParamT],
    left: ParamT,
    right: ParamT,
    *,
    require_visible_commutation: bool = True,
) -> sp.Expr:
    """Return the ordering residual for visibly commuting family elements.

    If the base compositions ``left*right`` and ``right*left`` agree, their
    lifted compositions can still differ centrally by

    ``omega(left,right) - omega(right,left)``.

    By default the function refuses to call this a *central commutator* unless
    the visible family elements commute.  Callers studying noncommuting base
    elements should inspect the two cocycle values directly.
    """

    if require_visible_commutation:
        left_right = cocycle.family.compose_parameters(left, right)
        right_left = cocycle.family.compose_parameters(right, left)
        if not cocycle.family.parameters_equivalent(left_right, right_left):
            raise ValueError("central commutator residual requires visibly commuting parameters")

    residual = cocycle.value(left, right) - cocycle.value(right, left)
    return sp.sympify(cocycle.simplify(sp.expand(residual)))
