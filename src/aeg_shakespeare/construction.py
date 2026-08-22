"""Construction-history-preserving primitive proposals.

Candidate primitives should not be identified merely because their final SymPy
expressions are equal. This module provides a small symbolic proposal IR that
keeps an explicit construction tree, operation costs, and bounded generation.
It is intentionally separate from presentation evaluation/Pareto search.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product
import math
from typing import Callable, Sequence

import sympy as sp


@dataclass(frozen=True)
class SymbolicOperation:
    """Caller-declared symbolic operation available to proposal generation.

    Parameters
    ----------
    name:
        Stable display name used in construction certificates.
    arity:
        Number of input expressions.
    apply:
        Callable implementing the operation's symbolic semantics. Callable
        identity remains part of construction identity, so two operations with
        the same display name are not silently equated.
    cost:
        Non-negative construction cost of one use.
    commutative:
        If true, argument permutations are considered the same construction for
        this operation. Associativity is *not* assumed automatically.
    """

    name: str
    arity: int
    apply: Callable[..., sp.Expr] = field(repr=False)
    cost: float = 1.0
    commutative: bool = False

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("operation name must be non-empty")
        if self.arity < 1:
            raise ValueError("operation arity must be positive")
        if not math.isfinite(float(self.cost)) or self.cost < 0:
            raise ValueError("operation cost must be finite and non-negative")


@dataclass(frozen=True)
class PrimitiveConstruction:
    """A tree certificate for how one candidate primitive was built."""

    atom: sp.Expr | None = None
    operation: SymbolicOperation | None = None
    children: tuple["PrimitiveConstruction", ...] = ()

    def __post_init__(self) -> None:
        has_atom = self.atom is not None
        has_operation = self.operation is not None
        if has_atom == has_operation:
            raise ValueError("construction must contain exactly one atom or operation")
        if has_atom:
            if self.children:
                raise ValueError("atomic construction cannot have children")
            object.__setattr__(self, "atom", sp.expand(sp.sympify(self.atom)))
            return
        assert self.operation is not None
        if len(self.children) != self.operation.arity:
            raise ValueError("construction child count must match operation arity")

    @classmethod
    def atomic(cls, expr: sp.Expr) -> "PrimitiveConstruction":
        return cls(atom=sp.expand(sp.sympify(expr)))

    @property
    def depth(self) -> int:
        if self.atom is not None:
            return 0
        return 1 + max((child.depth for child in self.children), default=0)

    @property
    def operation_count(self) -> int:
        if self.atom is not None:
            return 0
        return 1 + sum(child.operation_count for child in self.children)

    @property
    def cost(self) -> float:
        if self.atom is not None:
            return 0.0
        assert self.operation is not None
        return float(self.operation.cost) + sum(child.cost for child in self.children)

    def recipe(self) -> str:
        if self.atom is not None:
            return str(self.atom)
        assert self.operation is not None
        arguments = ", ".join(child.recipe() for child in self.children)
        return f"{self.operation.name}({arguments})"


@dataclass(frozen=True)
class PrimitiveProposal:
    """A candidate expression together with its non-erased construction tree."""

    expression: sp.Expr
    construction: PrimitiveConstruction

    @property
    def cost(self) -> float:
        return self.construction.cost


@dataclass(frozen=True)
class RejectedPrimitiveProposal:
    construction: PrimitiveConstruction
    reason: str


@dataclass(frozen=True)
class PrimitiveProposalResult:
    proposals: tuple[PrimitiveProposal, ...]
    rejected: tuple[RejectedPrimitiveProposal, ...]
    truncated: bool = False

    @property
    def semantic_expression_count(self) -> int:
        """Count distinct final expressions without erasing proposal histories."""

        return len({sp.srepr(proposal.expression) for proposal in self.proposals})


def _polynomial_degree(expr: sp.Expr, variables: Sequence[sp.Symbol]) -> int:
    try:
        degree = sp.Poly(sp.expand(expr), *variables).total_degree()
    except sp.PolynomialError as exc:
        raise ValueError("proposal is not polynomial in the declared variables") from exc
    if degree is sp.S.NegativeInfinity:
        return 0
    return int(degree)


def _construction_key(construction: PrimitiveConstruction) -> str:
    return construction.recipe()


def generate_primitive_proposals(
    atoms: Sequence[sp.Expr],
    operations: Sequence[SymbolicOperation],
    *,
    variables: Sequence[sp.Symbol],
    max_depth: int,
    max_degree: int,
    max_candidates: int = 256,
    include_atoms: bool = True,
) -> PrimitiveProposalResult:
    """Generate bounded symbolic primitive proposals without erasing recipes.

    Generation proceeds by construction depth. Semantic duplicates are kept if
    they have different construction trees. The only automatic construction
    quotient is argument permutation for operations explicitly declared
    commutative by the caller.

    ``max_candidates`` bounds generated non-atomic proposals; atoms are caller
    inputs and are not charged against that bound.
    """

    if max_depth < 0:
        raise ValueError("max_depth must be non-negative")
    if max_degree < 0:
        raise ValueError("max_degree must be non-negative")
    if max_candidates < 0:
        raise ValueError("max_candidates must be non-negative")

    variables = tuple(variables)
    constructions: list[PrimitiveConstruction] = []
    seen_constructions: set[PrimitiveConstruction] = set()
    proposals: list[PrimitiveProposal] = []
    rejected: list[RejectedPrimitiveProposal] = []

    for atom in atoms:
        construction = PrimitiveConstruction.atomic(atom)
        if construction in seen_constructions:
            continue
        seen_constructions.add(construction)
        expression = construction.atom
        assert expression is not None
        try:
            degree = _polynomial_degree(expression, variables)
        except ValueError as exc:
            rejected.append(RejectedPrimitiveProposal(construction, str(exc)))
            continue
        if degree > max_degree:
            rejected.append(
                RejectedPrimitiveProposal(
                    construction,
                    f"polynomial degree {degree} exceeds bound {max_degree}",
                )
            )
            continue
        constructions.append(construction)
        if include_atoms:
            proposals.append(PrimitiveProposal(expression, construction))

    if max_candidates == 0:
        return PrimitiveProposalResult(
            proposals=tuple(proposals),
            rejected=tuple(rejected),
            truncated=max_depth > 0 and bool(operations) and bool(constructions),
        )

    generated_nonatoms = 0

    for depth in range(1, max_depth + 1):
        pool = tuple(constructions)
        if not pool:
            break

        for operation in operations:
            for children in product(pool, repeat=operation.arity):
                if max(child.depth for child in children) != depth - 1:
                    continue
                if operation.commutative:
                    keys = tuple(_construction_key(child) for child in children)
                    if keys != tuple(sorted(keys)):
                        continue

                construction = PrimitiveConstruction(
                    operation=operation,
                    children=tuple(children),
                )
                if construction in seen_constructions:
                    continue
                seen_constructions.add(construction)

                try:
                    expression = _evaluate_construction(construction)
                except Exception as exc:  # caller operation boundary
                    rejected.append(
                        RejectedPrimitiveProposal(
                            construction,
                            f"operation evaluation failed: {exc}",
                        )
                    )
                    continue

                if expression == 0:
                    rejected.append(
                        RejectedPrimitiveProposal(
                            construction,
                            "zero is not a primitive proposal",
                        )
                    )
                    continue

                try:
                    degree = _polynomial_degree(expression, variables)
                except ValueError as exc:
                    rejected.append(RejectedPrimitiveProposal(construction, str(exc)))
                    continue
                if degree > max_degree:
                    rejected.append(
                        RejectedPrimitiveProposal(
                            construction,
                            f"polynomial degree {degree} exceeds bound {max_degree}",
                        )
                    )
                    continue

                proposals.append(PrimitiveProposal(expression, construction))
                constructions.append(construction)
                generated_nonatoms += 1
                if generated_nonatoms >= max_candidates:
                    return PrimitiveProposalResult(
                        proposals=tuple(proposals),
                        rejected=tuple(rejected),
                        truncated=True,
                    )

    return PrimitiveProposalResult(
        proposals=tuple(proposals),
        rejected=tuple(rejected),
        truncated=False,
    )


def _evaluate_construction(construction: PrimitiveConstruction) -> sp.Expr:
    if construction.atom is not None:
        return construction.atom
    assert construction.operation is not None
    return sp.expand(
        sp.sympify(
            construction.operation.apply(
                *[_evaluate_construction(child) for child in construction.children]
            )
        )
    )
