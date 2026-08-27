"""Automatic distinguished-scaling inference for exponential phases."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Mapping, Sequence

import sympy as sp

from .ir import Add, Const, Exp, Expr, Log, Mul, Pow, Var, walk
from .scale import Scale


class BalanceError(Exception):
    code = "balance-error"


class UnsupportedPolynomialError(BalanceError):
    code = "unsupported-polynomial"


class InconsistentBalanceError(BalanceError):
    code = "inconsistent-balance"


class UnderdeterminedBalanceError(BalanceError):
    code = "underdetermined-balance"


class SearchBudgetExceededError(BalanceError):
    code = "search-budget-exceeded"


@dataclass(frozen=True)
class BalanceBudget:
    max_input_nodes: int = 256
    max_expanded_terms: int = 256
    max_unknown_scales: int = 8


@dataclass(frozen=True)
class Monomial:
    coefficient: sp.Expr
    powers: Mapping[str, int]


@dataclass(frozen=True)
class BalanceEquation:
    term: Monomial
    coefficients: tuple[Fraction, ...]
    right_hand_side: Fraction


@dataclass(frozen=True)
class BalanceResult:
    status: str
    scales: Mapping[str, Scale]
    equations: tuple[BalanceEquation, ...]
    term_orders: tuple[Scale, ...]
    input_term_count: int
    solve_rank: int
    normalized_phase: sp.Expr
    scope: str
    certificate_checks: tuple[bool, ...]

    @property
    def certified(self) -> bool:
        return self.status == "ok" and all(self.certificate_checks)


def infer_distinguished_scaling(
    expression: Expr,
    unknown_scales: Sequence[str],
    fixed_scales: Mapping[str, Scale] | None = None,
    target_order: Scale | None = None,
    budget: BalanceBudget | None = None,
) -> BalanceResult:
    """Infer variable scales by making every exponential-phase term ``O(1)``.

    No expected scale, named normal form, or solved chart is supplied.
    """

    fixed_scales = dict(fixed_scales or {"N": Scale(1)})
    target_order = target_order or Scale(0)
    budget = budget or BalanceBudget()
    input_nodes = len({id(node) for node in walk(expression)})
    if input_nodes > budget.max_input_nodes:
        raise SearchBudgetExceededError("expression DAG exceeds the frozen node budget")
    if len(unknown_scales) > budget.max_unknown_scales:
        raise SearchBudgetExceededError("unknown scale count exceeds the frozen solve budget")
    phase = expression.argument if isinstance(expression, Exp) else expression
    expanded = _expand_polynomial(phase, budget.max_expanded_terms)
    monomials = _combine_like(expanded)
    if len(monomials) > budget.max_expanded_terms:
        raise SearchBudgetExceededError("expanded phase exceeds the frozen term budget")
    if not monomials:
        raise InconsistentBalanceError("phase has no nonzero monomials")

    unknowns = tuple(unknown_scales)
    equations: list[BalanceEquation] = []
    rows: list[list[sp.Rational]] = []
    rhs: list[sp.Rational] = []
    for monomial in monomials:
        coefficients = tuple(Fraction(monomial.powers.get(name, 0)) for name in unknowns)
        fixed_order = Fraction(0)
        for name, power in monomial.powers.items():
            if name in unknowns:
                continue
            if name not in fixed_scales:
                raise UnsupportedPolynomialError(
                    f"variable {name!r} has neither an unknown nor fixed scale"
                )
            fixed_order += power * fixed_scales[name].power
        right = target_order.power - fixed_order
        equations.append(BalanceEquation(monomial, coefficients, right))
        rows.append([sp.Rational(value.numerator, value.denominator) for value in coefficients])
        rhs.append(sp.Rational(right.numerator, right.denominator))

    matrix = sp.Matrix(rows)
    vector = sp.Matrix(rhs)
    rank = int(matrix.rank())
    augmented_rank = int(matrix.row_join(vector).rank())
    if augmented_rank > rank:
        raise InconsistentBalanceError("phase terms cannot all occupy the requested visible order")
    if rank < len(unknowns):
        raise UnderdeterminedBalanceError(
            "phase balance does not determine every requested scale; add a task constraint"
        )
    solution_set = sp.linsolve((matrix, vector))
    solution_tuple = next(iter(solution_set))
    if any(value.free_symbols for value in solution_tuple):
        raise UnderdeterminedBalanceError("balance solution retains free scale parameters")

    scales = {
        name: Scale(Fraction(int(value.p), int(value.q)))
        for name, value in zip(unknowns, solution_tuple)
    }
    term_orders = tuple(
        Scale(
            sum(
                power
                * (scales[name].power if name in scales else fixed_scales[name].power)
                for name, power in monomial.powers.items()
            )
        )
        for monomial in monomials
    )
    normalized_phase = _normalized_phase(monomials, unknowns, term_orders)
    equation_checks = tuple(
        sum(
            coefficient * scales[name].power
            for name, coefficient in zip(unknowns, equation.coefficients)
        )
        == equation.right_hand_side
        for equation in equations
    )
    order_checks = tuple(order == target_order for order in term_orders)
    return BalanceResult(
        status="ok",
        scales=scales,
        equations=tuple(equations),
        term_orders=term_orders,
        input_term_count=len(monomials),
        solve_rank=rank,
        normalized_phase=normalized_phase,
        scope="all nonzero polynomial phase monomials are required to occupy the declared target order",
        certificate_checks=equation_checks + order_checks,
    )


def _expand_polynomial(expression: Expr, max_terms: int) -> list[Monomial]:
    if isinstance(expression, Const):
        return [Monomial(expression.value, {})]
    if isinstance(expression, Var):
        return [Monomial(sp.S.One, {expression.name: 1})]
    if isinstance(expression, Add):
        result: list[Monomial] = []
        for term in expression.terms:
            result.extend(_expand_polynomial(term, max_terms))
            if len(result) > max_terms:
                raise SearchBudgetExceededError("polynomial distribution exceeded the frozen term budget")
        return result
    if isinstance(expression, Mul):
        result = [Monomial(sp.S.One, {})]
        for factor in expression.factors:
            expanded = _expand_polynomial(factor, max_terms)
            multiplied: list[Monomial] = []
            for left, right in product(result, expanded):
                powers = dict(left.powers)
                for name, power in right.powers.items():
                    powers[name] = powers.get(name, 0) + power
                multiplied.append(Monomial(sp.simplify(left.coefficient * right.coefficient), powers))
            result = multiplied
            if len(result) > max_terms:
                raise SearchBudgetExceededError("polynomial distribution exceeded the frozen term budget")
        return result
    if isinstance(expression, Pow):
        if not isinstance(expression.exponent, Const) or not expression.exponent.value.is_Integer:
            raise UnsupportedPolynomialError("phase powers must be nonnegative integer constants")
        exponent = int(expression.exponent.value)
        if isinstance(expression.base, Const):
            return [Monomial(sp.simplify(expression.base.value ** exponent), {})]
        if exponent < 0:
            raise UnsupportedPolynomialError("negative powers are outside polynomial phase extraction")
        result = [Monomial(sp.S.One, {})]
        base = _expand_polynomial(expression.base, max_terms)
        for _ in range(exponent):
            multiplied: list[Monomial] = []
            for left, right in product(result, base):
                powers = dict(left.powers)
                for name, power in right.powers.items():
                    powers[name] = powers.get(name, 0) + power
                multiplied.append(Monomial(sp.simplify(left.coefficient * right.coefficient), powers))
            result = multiplied
            if len(result) > max_terms:
                raise SearchBudgetExceededError("polynomial power exceeded the frozen term budget")
        return result
    if isinstance(expression, (Exp, Log)):
        raise UnsupportedPolynomialError("nested log/exp is not a polynomial phase")
    raise UnsupportedPolynomialError(f"unsupported phase node {type(expression).__name__}")


def _combine_like(monomials: list[Monomial]) -> list[Monomial]:
    grouped: dict[tuple[tuple[str, int], ...], sp.Expr] = {}
    for monomial in monomials:
        key = tuple(sorted((name, power) for name, power in monomial.powers.items() if power))
        grouped[key] = sp.simplify(grouped.get(key, 0) + monomial.coefficient)
    return [
        Monomial(coefficient, dict(key))
        for key, coefficient in grouped.items()
        if sp.simplify(coefficient) != 0
    ]


def _normalized_phase(
    monomials: Sequence[Monomial],
    unknowns: Sequence[str],
    term_orders: Sequence[Scale],
) -> sp.Expr:
    hats = {name: sp.Symbol(f"{name}_hat") for name in unknowns}
    scale_symbol = sp.Symbol("N", positive=True)
    terms: list[sp.Expr] = []
    for monomial, order in zip(monomials, term_orders):
        term = monomial.coefficient * scale_symbol ** sp.Rational(
            order.power.numerator, order.power.denominator
        )
        for name in unknowns:
            term *= hats[name] ** monomial.powers.get(name, 0)
        terms.append(term)
    return sp.simplify(sum(terms, sp.S.Zero))
