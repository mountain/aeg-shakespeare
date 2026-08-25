"""Incubating local canonical-observer records.

Theory position
---------------
This module keeps three executable H4 slices together without promoting a
generic canonicalization or observer-geometry ontology:

* ``ConstraintCanonicalization`` selects local observer parameters by exact
  algebraic constraints;
* ``ObserverConnection`` records the induced local transport and its exact
  residual certificate; and
* ``CanonicalDecomposition`` records caller-certified renormalizable,
  resonant/transport, and completion sectors.

The classes survived several continuous calibrations, but the foundation has
not supplied a generic observer topology, a canonical history lift, a unique
task-covariant ruler, or a universal decomposition theorem.  Their canonical
home is therefore ``process_geometry.experimental``.  Historical imports from
``presentation.canonicalization``, ``analysis.connection``, and
``analysis.decomposition`` remain compatibility shims during the 0.0.x phase.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Mapping, TypeVar

import sympy as sp

CanonicalizationT = TypeVar("CanonicalizationT")
SourceT = TypeVar("SourceT")
PartT = TypeVar("PartT")
CertificateT = TypeVar("CertificateT")


@dataclass(frozen=True)
class ObserverConnection(Generic[CanonicalizationT]):
    """Local observer transport with canonicalization provenance.

    This is an exact evidence record for one declared local construction.  It
    is not a generic principal-bundle connection and does not assert that the
    source canonicalization is task-global or unique.
    """

    canonicalization: CanonicalizationT
    base_rates: Mapping[sp.Symbol, sp.Expr]
    observer_rates: Mapping[sp.Symbol, sp.Expr]
    residuals: tuple[sp.Expr, ...]
    label: str = ""

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "base_rates",
            {
                symbol: sp.expand(sp.sympify(value))
                for symbol, value in self.base_rates.items()
            },
        )
        object.__setattr__(
            self,
            "observer_rates",
            {
                symbol: sp.simplify(sp.sympify(value))
                for symbol, value in self.observer_rates.items()
            },
        )
        object.__setattr__(
            self,
            "residuals",
            tuple(sp.simplify(sp.sympify(value)) for value in self.residuals),
        )

    @property
    def certified(self) -> bool:
        """Whether every supplied canonicalization residual vanishes."""

        return all(sp.simplify(residual) == 0 for residual in self.residuals)

    def rate(self, observer_parameter: sp.Symbol) -> sp.Expr:
        """Return the induced rate of one observer parameter."""

        try:
            return sp.sympify(self.observer_rates[observer_parameter])
        except KeyError as exc:
            raise KeyError(
                f"unknown observer parameter: {observer_parameter!r}"
            ) from exc


@dataclass(frozen=True)
class ConstraintCanonicalization:
    """Exact local constraints selecting observer parameters.

    Only the finite-equation backend is implemented.  Residual gauge freedom,
    singular strata, branch selection, stationarity, and history-global
    canonical lifts remain outside this contract.
    """

    observer_parameters: tuple[sp.Symbol, ...]
    constraints: tuple[sp.Expr, ...]
    label: str = ""

    def __post_init__(self) -> None:
        parameters = tuple(self.observer_parameters)
        if not parameters:
            raise ValueError("canonicalization requires observer parameters")
        if len(set(parameters)) != len(parameters):
            raise ValueError("observer parameters must be distinct")
        constraints = tuple(
            sp.expand(sp.sympify(constraint))
            for constraint in self.constraints
            if sp.expand(sp.sympify(constraint)) != 0
        )
        if not constraints:
            raise ValueError("canonicalization requires at least one nonzero constraint")
        object.__setattr__(self, "observer_parameters", parameters)
        object.__setattr__(self, "constraints", constraints)

    def differentiated_constraints(
        self,
        base_rates: Mapping[sp.Symbol, sp.Expr],
        observer_rates: Mapping[sp.Symbol, sp.Expr],
    ) -> tuple[sp.Expr, ...]:
        """Differentiate ``Phi=0`` along declared local rates."""

        missing = set(self.observer_parameters) - set(observer_rates)
        if missing:
            raise ValueError(
                "missing rates for observer parameters: "
                f"{sorted(map(str, missing))}"
            )

        rates = {
            **{
                symbol: sp.sympify(value)
                for symbol, value in base_rates.items()
            },
            **{
                symbol: sp.sympify(value)
                for symbol, value in observer_rates.items()
            },
        }
        return tuple(
            sp.expand(
                sum(
                    sp.diff(constraint, symbol) * rate
                    for symbol, rate in rates.items()
                )
            )
            for constraint in self.constraints
        )

    def induced_connection(
        self,
        base_rates: Mapping[sp.Symbol, sp.Expr],
        *,
        label: str = "",
    ) -> ObserverConnection["ConstraintCanonicalization"]:
        """Solve the differentiated constraints for local observer rates.

        The current implementation requires a unique symbolic local solution;
        it never resolves residual gauge or branch ambiguity silently.
        """

        rate_symbols = {
            parameter: sp.Dummy(f"d_{parameter}")
            for parameter in self.observer_parameters
        }
        equations = self.differentiated_constraints(base_rates, rate_symbols)
        unknowns = tuple(
            rate_symbols[parameter] for parameter in self.observer_parameters
        )
        solutions = sp.solve(
            tuple(sp.Eq(equation, 0) for equation in equations),
            unknowns,
            dict=True,
            simplify=True,
        )
        if len(solutions) != 1 or any(
            unknown not in solutions[0]
            for unknown in unknowns
        ):
            raise ValueError(
                "canonicalization does not induce a unique local observer connection"
            )

        solution = solutions[0]
        observer_rates = {
            parameter: sp.simplify(solution[rate_symbols[parameter]])
            for parameter in self.observer_parameters
        }
        residuals = self.differentiated_constraints(base_rates, observer_rates)
        return ObserverConnection(
            canonicalization=self,
            base_rates=base_rates,
            observer_rates=observer_rates,
            residuals=residuals,
            label=label or self.label,
        )


@dataclass(frozen=True)
class CanonicalDecomposition(Generic[SourceT, PartT, CertificateT]):
    """Caller-certified local split into three process roles.

    The record does not claim that the split is unique, globally canonical, or
    discovered by one universal backend.
    """

    source: SourceT
    renormalizable: PartT
    resonant: PartT
    completion: PartT
    certificate: CertificateT
    label: str = ""


__all__ = [
    "ConstraintCanonicalization",
    "ObserverConnection",
    "CanonicalDecomposition",
]
