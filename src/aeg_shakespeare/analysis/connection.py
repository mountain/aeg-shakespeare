"""Experimental observer-connection certificates.

An observer connection is not introduced here as a general principal-bundle
object.  The current vertical slice records only what the first independent
calibrations need: a local canonicalization, declared base rates, the induced
observer-parameter rates, and exact residuals certifying that the differentiated
canonicalization constraints remain satisfied.

Construction should normally go through
``Canonicalization.induced_connection`` so that observer motion retains its
canonicalization provenance instead of being supplied as an arbitrary ODE.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, TYPE_CHECKING

import sympy as sp

if TYPE_CHECKING:
    from ..presentation.canonicalization import Canonicalization


@dataclass(frozen=True)
class ObserverConnection:
    """Local observer transport induced by maintaining canonicalization."""

    canonicalization: "Canonicalization"
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
        """Whether every differentiated canonicalization residual vanishes."""

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
