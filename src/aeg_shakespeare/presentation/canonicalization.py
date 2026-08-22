"""Experimental local canonicalization constraints.

The first canonical-observer API is intentionally narrow.  ``Canonicalization``
represents an exact finite family of local equations

    Phi(local data, observer parameters) = 0.

Observer motion is obtained by differentiating these equations along declared
base rates and solving for the observer-parameter rates.  This realizes the
research principle

    local canonicalization -> connection -> observer ODE

without introducing a general bundle, gauge, curvature, or numerical-flow API.
A stationary/cost-based canonicalization should be added only after an
independent calibration fixes the information its Hessian transport must retain.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import sympy as sp


@dataclass(frozen=True)
class Canonicalization:
    """Exact local constraints selecting observer parameters."""

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
        """Differentiate ``Phi=0`` along base and observer parameter rates.

        Symbols not named in either mapping are treated as locally frozen
        parameters.  This keeps the operation explicitly local and prevents the
        canonicalization object from reaching into a trajectory or propagator.
        """

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
    ):
        """Solve the differentiated canonicalization for observer rates.

        The current implementation requires a unique symbolic local solution.
        Residual gauge freedom, singular strata, least-squares stationarity, and
        branch selection remain explicit future API questions rather than being
        silently resolved here.
        """

        from ..analysis.connection import ObserverConnection

        rate_symbols = {
            parameter: sp.Dummy(f"d_{parameter}")
            for parameter in self.observer_parameters
        }
        equations = self.differentiated_constraints(base_rates, rate_symbols)
        unknowns = tuple(rate_symbols[parameter] for parameter in self.observer_parameters)
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


__all__ = ["Canonicalization"]
