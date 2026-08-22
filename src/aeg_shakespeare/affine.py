"""Finite add/multiply history normalization (P0 benchmark)."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class Add:
    amount: sp.Expr


@dataclass(frozen=True)
class Scale:
    factor: sp.Expr


@dataclass(frozen=True)
class AffineNormalForm:
    """Canonical semantic form ``x -> scale*x + shift``."""

    scale: sp.Expr
    shift: sp.Expr


def normalize_affine_history(history: list[Add | Scale]) -> AffineNormalForm:
    scale = sp.S.One
    shift = sp.S.Zero
    for step in history:
        if isinstance(step, Add):
            shift = sp.expand(shift + step.amount)
        elif isinstance(step, Scale):
            scale = sp.expand(step.factor * scale)
            shift = sp.expand(step.factor * shift)
        else:
            raise TypeError(f"unsupported affine process step: {step!r}")
    return AffineNormalForm(sp.simplify(scale), sp.simplify(shift))
