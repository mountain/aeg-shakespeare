"""A deliberately finite expression IR for the first compiler experiment."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from numbers import Number
from typing import Iterable, Union

import sympy as sp


Scalar = Union[int, float, Fraction, sp.Expr]


def as_expr(value: "Expr | Scalar") -> "Expr":
    return value if isinstance(value, Expr) else Const(value)


class Expr:
    """Base class with enough operator sugar to state calibration problems."""

    def __add__(self, other: "Expr | Scalar") -> "Expr":
        return add(self, as_expr(other))

    def __radd__(self, other: "Expr | Scalar") -> "Expr":
        return add(as_expr(other), self)

    def __sub__(self, other: "Expr | Scalar") -> "Expr":
        return add(self, -as_expr(other))

    def __rsub__(self, other: "Expr | Scalar") -> "Expr":
        return add(as_expr(other), -self)

    def __mul__(self, other: "Expr | Scalar") -> "Expr":
        return mul(self, as_expr(other))

    def __rmul__(self, other: "Expr | Scalar") -> "Expr":
        return mul(as_expr(other), self)

    def __truediv__(self, other: "Expr | Scalar") -> "Expr":
        return mul(self, Pow(as_expr(other), Const(-1)))

    def __rtruediv__(self, other: "Expr | Scalar") -> "Expr":
        return mul(as_expr(other), Pow(self, Const(-1)))

    def __pow__(self, exponent: "Expr | Scalar") -> "Expr":
        return Pow(self, as_expr(exponent))

    def __neg__(self) -> "Expr":
        return mul(Const(-1), self)


@dataclass(frozen=True)
class Const(Expr):
    value: sp.Expr

    def __init__(self, value: Scalar):
        object.__setattr__(self, "value", sp.sympify(value))


@dataclass(frozen=True)
class Var(Expr):
    name: str


@dataclass(frozen=True)
class Add(Expr):
    terms: tuple[Expr, ...]


@dataclass(frozen=True)
class Mul(Expr):
    factors: tuple[Expr, ...]


@dataclass(frozen=True)
class Pow(Expr):
    base: Expr
    exponent: Expr


@dataclass(frozen=True)
class Exp(Expr):
    argument: Expr


@dataclass(frozen=True)
class Log(Expr):
    argument: Expr


def add(*terms: Expr) -> Expr:
    flat: list[Expr] = []
    constant = sp.S.Zero
    for term in terms:
        if isinstance(term, Add):
            flat.extend(term.terms)
        elif isinstance(term, Const):
            constant += term.value
        else:
            flat.append(term)
    constant = sp.simplify(constant)
    if constant != 0:
        flat.append(Const(constant))
    if not flat:
        return Const(0)
    if len(flat) == 1:
        return flat[0]
    return Add(tuple(flat))


def mul(*factors: Expr) -> Expr:
    flat: list[Expr] = []
    constant = sp.S.One
    for factor in factors:
        if isinstance(factor, Mul):
            flat.extend(factor.factors)
        elif isinstance(factor, Const):
            constant *= factor.value
        else:
            flat.append(factor)
    constant = sp.simplify(constant)
    if constant == 0:
        return Const(0)
    if constant != 1:
        flat.insert(0, Const(constant))
    if not flat:
        return Const(constant)
    if len(flat) == 1:
        return flat[0]
    return Mul(tuple(flat))


def exp(argument: Expr | Scalar) -> Expr:
    return Exp(as_expr(argument))


def log(argument: Expr | Scalar) -> Expr:
    return Log(as_expr(argument))


def walk(expr: Expr) -> Iterable[Expr]:
    """Preorder traversal used for transparent cost accounting."""

    yield expr
    if isinstance(expr, Add):
        for term in expr.terms:
            yield from walk(term)
    elif isinstance(expr, Mul):
        for factor in expr.factors:
            yield from walk(factor)
    elif isinstance(expr, Pow):
        yield from walk(expr.base)
        yield from walk(expr.exponent)
    elif isinstance(expr, (Exp, Log)):
        yield from walk(expr.argument)
