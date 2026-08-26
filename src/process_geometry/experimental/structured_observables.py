"""Incubating structured-observable proposals for process discovery.

This slice records one useful construction forced by the pendulum calibration:
primitive objects of a declared pairable sort can be lowered through a
caller-supplied pairing to scalar observable candidates. It remains
Experimental because the present evidence does not yet justify a general
structured-observable ontology or a stable public grammar.

A proposal retains two layers at once:

* ``construction`` records the structured recipe, for example ``pair(q,e)``;
* ``expression`` is the scalar backend lowering consumed by polynomial
  discovery.

No vector-space operations, bases, matrices, positivity, or universal theory
protocol are inferred from the pairing tag.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement, product
from typing import Callable, Sequence

import sympy as sp


@dataclass(frozen=True)
class PairableAtom:
    """One named structured atom with a backend component realization."""

    name: str
    components: tuple[sp.Expr, ...]
    sort: str = "pairable"

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("structured atom name must be non-empty")
        if not self.sort:
            raise ValueError("structured atom sort must be non-empty")
        components = tuple(sp.expand(sp.sympify(item)) for item in self.components)
        if not components:
            raise ValueError("pairable atom requires at least one component")
        object.__setattr__(self, "components", components)


@dataclass(frozen=True)
class PairingSpec:
    """A caller-declared scalar pairing on one structured sort.

    ``lower`` receives two component tuples and returns an exact scalar backend
    expression. Symmetry affects construction enumeration only.
    """

    name: str
    sort: str
    lower: Callable[[tuple[sp.Expr, ...], tuple[sp.Expr, ...]], sp.Expr]
    symmetric: bool = True
    cost: float = 1.0

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("pairing name must be non-empty")
        if not self.sort:
            raise ValueError("pairing sort must be non-empty")
        if self.cost < 0:
            raise ValueError("pairing cost must be non-negative")


@dataclass(frozen=True)
class PairingConstruction:
    """Construction certificate for one scalar observable proposal."""

    pairing_name: str
    left_name: str
    right_name: str
    cost: float

    def recipe(self) -> str:
        return f"{self.pairing_name}({self.left_name},{self.right_name})"


@dataclass(frozen=True)
class StructuredObservableProposal:
    """A scalar backend expression together with its structured origin."""

    expression: sp.Expr
    construction: PairingConstruction

    @property
    def cost(self) -> float:
        return self.construction.cost


@dataclass(frozen=True)
class StructuredObservableProposalResult:
    proposals: tuple[StructuredObservableProposal, ...]
    rejected: tuple[str, ...] = ()


def euclidean_pairing(
    *,
    name: str = "pair",
    sort: str = "euclidean",
    cost: float = 1.0,
) -> PairingSpec:
    """Return the finite-coordinate Euclidean pairing used by calibrations.

    This convenience constructor is a backend realization, not a declaration
    that every pairable sort is Euclidean.
    """

    def lower(left: tuple[sp.Expr, ...], right: tuple[sp.Expr, ...]) -> sp.Expr:
        if len(left) != len(right):
            raise ValueError("pairing requires equal component dimensions")
        return sp.expand(sum(a * b for a, b in zip(left, right)))

    return PairingSpec(name=name, sort=sort, lower=lower, symmetric=True, cost=cost)


def generate_pairing_observables(
    atoms: Sequence[PairableAtom],
    pairing: PairingSpec,
) -> StructuredObservableProposalResult:
    """Generate bounded depth-one scalar observables from one pairing."""

    atoms = tuple(atoms)
    if not atoms:
        raise ValueError("at least one structured atom is required")

    eligible = tuple(atom for atom in atoms if atom.sort == pairing.sort)
    rejected = tuple(
        f"{atom.name}: sort {atom.sort!r} is incompatible with pairing sort {pairing.sort!r}"
        for atom in atoms
        if atom.sort != pairing.sort
    )
    if not eligible:
        return StructuredObservableProposalResult((), rejected)

    pairs = (
        combinations_with_replacement(eligible, 2)
        if pairing.symmetric
        else product(eligible, repeat=2)
    )
    proposals: list[StructuredObservableProposal] = []
    for left, right in pairs:
        try:
            expression = sp.expand(
                sp.sympify(pairing.lower(left.components, right.components))
            )
        except Exception as exc:  # caller pairing boundary
            rejected += (f"{pairing.name}({left.name},{right.name}): {exc}",)
            continue
        proposals.append(
            StructuredObservableProposal(
                expression=expression,
                construction=PairingConstruction(
                    pairing_name=pairing.name,
                    left_name=left.name,
                    right_name=right.name,
                    cost=float(pairing.cost),
                ),
            )
        )

    return StructuredObservableProposalResult(tuple(proposals), rejected)


def nonstationary_observable_proposals(
    system,
    proposals: Sequence[StructuredObservableProposal],
    *,
    constraints,
) -> tuple[StructuredObservableProposal, ...]:
    """Keep proposals whose first process derivative survives the constraints.

    This is a task filter, not an equality rule: stationary constructions remain
    valid constructions, but are insufficient for the current search task.
    """

    return tuple(
        proposal
        for proposal in proposals
        if not constraints.contains(system.derive(proposal.expression))
    )

