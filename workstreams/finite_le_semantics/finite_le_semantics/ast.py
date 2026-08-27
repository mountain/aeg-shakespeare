"""Strict JSON AST decoding and conservative real-domain witnesses."""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Mapping

import sympy as sp

from .model import DomainWitness, FailureCode, SemanticFailure


def _rational(value: object) -> sp.Rational:
    try:
        fraction = Fraction(str(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise SemanticFailure(
            FailureCode.INVALID_RATIONAL,
            f"{value!r} is not a rational constant in the frozen grammar",
        ) from exc
    return sp.Rational(fraction.numerator, fraction.denominator)


def sign_of(data: Mapping[str, Any], assumptions: Mapping[str, str]) -> int | None:
    op = data.get("op")
    if op == "const":
        value = _rational(data.get("value"))
        return 1 if value > 0 else -1 if value < 0 else 0
    if op == "symbol":
        assumption = assumptions.get(str(data.get("name")))
        return 1 if assumption == "positive" else -1 if assumption == "negative" else None
    if op == "exp":
        return 1
    if op == "log":
        return None
    if op == "mul":
        sign = 1
        for factor in data.get("factors", []):
            child = sign_of(factor, assumptions)
            if child is None:
                return None
            sign *= child
        return sign
    if op == "add":
        signs = [sign_of(term, assumptions) for term in data.get("terms", [])]
        if signs and all(item is not None and item >= 0 for item in signs) and any(item == 1 for item in signs):
            return 1
        if signs and all(item is not None and item <= 0 for item in signs) and any(item == -1 for item in signs):
            return -1
        return 0 if signs and all(item == 0 for item in signs) else None
    if op == "pow":
        base_sign = sign_of(data.get("base", {}), assumptions)
        exponent = _rational(data.get("exponent"))
        if base_sign == 1:
            return 1
        if base_sign == -1 and exponent.q == 1:
            return 1 if int(exponent) % 2 == 0 else -1
        return None
    return None


def decode_expression(
    data: Mapping[str, Any],
    assumptions: Mapping[str, str],
    *,
    path: str = "root",
) -> tuple[sp.Expr, tuple[DomainWitness, ...], int]:
    """Decode only the frozen grammar and collect log-domain witnesses."""

    witnesses: list[DomainWitness] = []
    symbols: dict[str, sp.Symbol] = {}
    nodes = 0

    def symbol(name: str) -> sp.Symbol:
        if name not in symbols:
            if assumptions.get(name) == "positive":
                symbols[name] = sp.Symbol(name, positive=True)
            elif assumptions.get(name) == "negative":
                symbols[name] = sp.Symbol(name, negative=True)
            else:
                symbols[name] = sp.Symbol(name, real=True)
        return symbols[name]

    def visit(node: Mapping[str, Any], current: str) -> sp.Expr:
        nonlocal nodes
        nodes += 1
        op = node.get("op")
        if op == "const":
            return _rational(node.get("value"))
        if op == "symbol":
            return symbol(str(node.get("name")))
        if op == "add":
            terms = node.get("terms")
            if not isinstance(terms, list) or not terms:
                raise SemanticFailure(FailureCode.OUTSIDE_GRAMMAR, "add requires a nonempty terms list")
            return sp.Add(*(visit(item, f"{current}.{index}") for index, item in enumerate(terms)))
        if op == "mul":
            factors = node.get("factors")
            if not isinstance(factors, list) or not factors:
                raise SemanticFailure(FailureCode.OUTSIDE_GRAMMAR, "mul requires a nonempty factors list")
            return sp.Mul(*(visit(item, f"{current}.{index}") for index, item in enumerate(factors)))
        if op == "pow":
            base_data = node.get("base", {})
            exponent = _rational(node.get("exponent"))
            base_sign = sign_of(base_data, assumptions)
            if exponent.q != 1 and base_sign != 1:
                raise SemanticFailure(
                    FailureCode.OUTSIDE_GRAMMAR,
                    f"noninteger real power at {current} lacks a positive-base witness",
                )
            if exponent < 0 and base_sign in {None, 0}:
                raise SemanticFailure(
                    FailureCode.OUTSIDE_GRAMMAR,
                    f"negative power at {current} lacks a nonzero-base witness",
                )
            return sp.Pow(visit(base_data, f"{current}.0"), exponent)
        if op == "exp":
            return sp.exp(visit(node.get("argument", {}), f"{current}.0"))
        if op == "log":
            argument = node.get("argument", {})
            if sign_of(argument, assumptions) != 1:
                raise SemanticFailure(
                    FailureCode.LOG_DOMAIN,
                    f"log argument at {current} lacks a syntactic positive-real witness",
                )
            witnesses.append(DomainWitness(current, "log argument is positive in the declared real domain"))
            return sp.log(visit(argument, f"{current}.0"))
        if op in {"symbolic-iterate", "abel-task"}:
            raise SemanticFailure(
                FailureCode.SYMBOLIC_HEIGHT,
                "symbolic-height iteration is outside the finite LE semantic fragment",
            )
        raise SemanticFailure(FailureCode.OUTSIDE_GRAMMAR, f"unknown frozen expression operation {op!r}")

    return visit(data, path), tuple(witnesses), nodes
