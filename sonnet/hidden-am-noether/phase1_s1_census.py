"""Exact S1 visible-symmetry census for the frozen depth-one grammar."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import sympy as sp

from phase0_contract import (
    Expression,
    GENERATORS,
    expressions_through_depth_one,
    projective_generator_coefficients,
)


X, Y, VX, VY = sp.symbols("x y vx vy", real=True)
SYMBOLS = {"x": X, "y": Y, "vx": VX, "vy": VY}


def expression_semantics(expression: Expression) -> sp.Expr:
    if not expression.arguments:
        if expression.operation in SYMBOLS:
            return SYMBOLS[expression.operation]
        return sp.Integer(expression.operation)
    left, right = map(expression_semantics, expression.arguments)
    if expression.operation == "add":
        return sp.expand(left + right)
    if expression.operation == "mul":
        return sp.expand(left * right)
    raise ValueError(f"unknown frozen operation: {expression.operation!r}")


def canonicalize_expressions(expressions) -> tuple[sp.Expr, ...]:
    representatives = {
        sp.srepr(sp.expand(expression_semantics(expression))): sp.expand(
            expression_semantics(expression)
        )
        for expression in expressions
    }
    return tuple(sorted(representatives.values(), key=sp.default_sort_key))


@lru_cache(maxsize=1)
def canonical_semantic_expressions() -> tuple[sp.Expr, ...]:
    return canonicalize_expressions(expressions_through_depth_one())


def generator_assignment_rules(coefficients):
    ax, mx, ay, my = map(sp.Integer, coefficients)
    return {
        X: ax + mx * X,
        Y: ay + my * Y,
        VX: mx * VX,
        VY: my * VY,
    }


def exact_process_residual(expression, coefficients):
    rules = generator_assignment_rules(coefficients)
    residual = sum(
        sp.diff(expression, assignment) * rule
        for assignment, rule in rules.items()
    )
    return sp.expand(residual)


def unrestricted_generator_matrix(expression):
    """Coefficient matrix for every constant linear A/M generator.

    This is a red-team certificate, not an expansion of the frozen discovery
    grammar.  A nontrivial nullspace proves that a claimed asymmetric input is
    merely hidden by the {-1,0,1} coefficient bound.
    """

    basis_residuals = [
        exact_process_residual(
            expression,
            tuple(1 if index == basis else 0 for index in range(len(GENERATORS))),
        )
        for basis in range(len(GENERATORS))
    ]
    monomials = sorted(
        set().union(
            *(
                sp.Poly(residual, X, Y, VX, VY).monoms()
                for residual in basis_residuals
            )
        )
    )
    rows = []
    for monomial in monomials:
        rows.append(
            [
                sp.Poly(residual, X, Y, VX, VY).coeff_monomial(monomial)
                for residual in basis_residuals
            ]
        )
    return sp.Matrix(rows)


def unrestricted_generator_nullspace(expression):
    return tuple(unrestricted_generator_matrix(expression).nullspace())


@dataclass(frozen=True)
class VisibleSymmetryWitness:
    expression: sp.Expr
    generator_coefficients: tuple[int, ...]
    residual: sp.Expr

    @property
    def generator_label(self) -> str:
        terms = [
            f"{coefficient:+d}{name}"
            for coefficient, name in zip(self.generator_coefficients, GENERATORS)
            if coefficient
        ]
        return "".join(terms).lstrip("+")


@dataclass(frozen=True)
class S1Census:
    raw_expression_count: int
    semantic_expression_count: int
    generator_count: int
    tested_pair_count: int
    visible_witnesses: tuple[VisibleSymmetryWitness, ...]
    asymmetric_expressions: tuple[sp.Expr, ...]


def run_census(raw) -> S1Census:
    expressions = canonicalize_expressions(raw)
    generators = projective_generator_coefficients()
    witnesses = []
    asymmetric = []

    for expression in expressions:
        expression_witnesses = []
        for coefficients in generators:
            residual = exact_process_residual(expression, coefficients)
            if residual == 0:
                expression_witnesses.append(
                    VisibleSymmetryWitness(expression, coefficients, residual)
                )
        if expression_witnesses:
            witnesses.extend(expression_witnesses)
        else:
            asymmetric.append(expression)

    return S1Census(
        raw_expression_count=len(raw),
        semantic_expression_count=len(expressions),
        generator_count=len(generators),
        tested_pair_count=len(expressions) * len(generators),
        visible_witnesses=tuple(witnesses),
        asymmetric_expressions=tuple(asymmetric),
    )


@lru_cache(maxsize=1)
def run_s1_census() -> S1Census:
    return run_census(expressions_through_depth_one())
