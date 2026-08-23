"""Minimal structured-observer proposals for process discovery.

This module is deliberately narrower than a general typed mathematical IR.
The first calibration only needs one fact that bare scalar assignment symbols
cannot express: several primitive objects may belong to the same pairable sort,
and a caller-supplied pairing may turn two such objects into a scalar observer.

The abstraction stops there.  It does not assume vector-space addition, scalar
multiplication, bases, matrices, Fourier analysis, or a universal theory
protocol.  Those structures should enter only when later mathematical
vignettes force them.

A proposal retains two layers at once:

* ``construction`` records the structured recipe, e.g. ``pair(q,e)``;
* ``expression`` is the scalar backend lowering consumed by the existing
  polynomial discovery layer.

Thus a coordinate expression such as ``qy`` need not become the ontology of
an observer whose actual construction is ``pair(q,e)``.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement, product
from typing import Callable, Sequence

import sympy as sp


@dataclass(frozen=True)
class PairableAtom:
    """One named structured atom with a backend component realization.

    ``sort`` is intentionally only an equality tag.  The current layer knows no
    axioms associated with that tag; it merely prevents a pairing from being
    applied across incompatible primitive kinds.
    """

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

    ``lower`` receives the two component tuples and returns the exact scalar
    backend expression.  Symmetry affects construction enumeration only; no
    bilinearity, positivity, or other vector-space law is inferred.
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
    """Construction certificate for one scalar observer proposal."""

    pairing_name: str
    left_name: str
    right_name: str
    cost: float

    def recipe(self) -> str:
        return f"{self.pairing_name}({self.left_name},{self.right_name})"


@dataclass(frozen=True)
class StructuredObserverProposal:
    """A scalar backend expression together with its structured origin."""

    expression: sp.Expr
    construction: PairingConstruction

    @property
    def cost(self) -> float:
        return self.construction.cost


@dataclass(frozen=True)
class StructuredObserverProposalResult:
    proposals: tuple[StructuredObserverProposal, ...]
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


def generate_pairing_observers(
    atoms: Sequence[PairableAtom],
    pairing: PairingSpec,
) -> StructuredObserverProposalResult:
    """Generate all bounded depth-one scalar observers from one pairing.

    The caller supplies the primitive atoms and the pairing itself.  Shakespeare
    supplies no vector-space laws beyond the explicitly declared symmetry used
    to avoid duplicate recipes.
    """

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
        return StructuredObserverProposalResult((), rejected)

    pairs = (
        combinations_with_replacement(eligible, 2)
        if pairing.symmetric
        else product(eligible, repeat=2)
    )
    proposals: list[StructuredObserverProposal] = []
    for left, right in pairs:
        try:
            expression = sp.expand(
                sp.sympify(pairing.lower(left.components, right.components))
            )
        except Exception as exc:  # caller pairing boundary
            rejected += (f"{pairing.name}({left.name},{right.name}): {exc}",)
            continue
        proposals.append(
            StructuredObserverProposal(
                expression=expression,
                construction=PairingConstruction(
                    pairing_name=pairing.name,
                    left_name=left.name,
                    right_name=right.name,
                    cost=float(pairing.cost),
                ),
            )
        )

    return StructuredObserverProposalResult(tuple(proposals), rejected)


def nonstationary_observer_proposals(
    system,
    proposals: Sequence[StructuredObserverProposal],
    *,
    constraints,
) -> tuple[StructuredObserverProposal, ...]:
    """Keep proposals whose first process derivative survives the quotient.

    This is a task filter, not an equality rule: stationary constructions remain
    valid constructions, but they are insufficient for the present task of
    finding a one-dimensional evolving observer.
    """

    return tuple(
        proposal
        for proposal in proposals
        if not constraints.contains(system.derive(proposal.expression))
    )
