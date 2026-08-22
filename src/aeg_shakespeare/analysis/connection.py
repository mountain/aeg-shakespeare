"""Experimental observer-connection certificates.

An observer connection is not introduced here as a general principal-bundle
object.  The current vertical slice records only what the first calibrations
need: canonicalization provenance, declared base rates, induced observer rates,
and exact residuals certifying the maintained local condition.

The provenance carrier is generic on purpose.  Exact constraint
canonicalization is the first backend; later orthogonality, osculation, or
stationarity backends should be able to produce the same connection record
without pretending to be algebraic constraints.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Mapping, TypeVar

import sympy as sp

CanonicalizationT = TypeVar("CanonicalizationT")


@dataclass(frozen=True)
class ObserverConnection(Generic[CanonicalizationT]):
    """Local observer transport together with canonicalization provenance."""

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


__all__ = ["ObserverConnection"]
