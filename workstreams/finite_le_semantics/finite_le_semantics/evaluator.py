"""Exact single-exponential-scale evaluator without a generic limit oracle."""

from __future__ import annotations

from dataclasses import replace
from functools import reduce
from math import lcm
from typing import Any, Mapping

import sympy as sp

from .ast import decode_expression
from .model import (
    CostLedger,
    EvaluatorBudget,
    FailureCode,
    LESemanticCertificate,
    SemanticFailure,
    Status,
    canonical_json,
    digest,
)


SCHEMA = "process-geometry/finite-le-semantic-certificate/v0"
CLAIM_SCOPE = (
    "exact semantics only for the frozen real single-exponential rational-rate "
    "Laurent/Taylor fragment; no general LE, transseries, hyperserial, or surreal claim"
)
DISCHARGED = ("le-normal-form", "le-domain-branches", "le-comparison")


def _direct_rate(argument: sp.Expr, parameter: sp.Symbol) -> tuple[sp.Expr, sp.Expr]:
    expanded = sp.expand(argument)
    rate = expanded.coeff(parameter)
    if rate.has(parameter):
        raise SemanticFailure(FailureCode.IRRATIONAL_RATE, "linear exponential rate depends on the parameter")
    if rate != 0 and not rate.is_Rational:
        raise SemanticFailure(FailureCode.IRRATIONAL_RATE, f"exponential rate {rate} is not rational")
    residual = sp.simplify(expanded - rate * parameter)
    return rate, residual


def _collect_rates(expr: sp.Expr, parameter: sp.Symbol) -> tuple[sp.Rational, ...]:
    rates: list[sp.Rational] = []
    for node in sp.preorder_traversal(expr):
        if node.func is sp.exp:
            rate, _ = _direct_rate(node.args[0], parameter)
            if rate != 0:
                rates.append(sp.Rational(rate))
    return tuple(rates)


def _chart_denominator(rates: tuple[sp.Rational, ...]) -> int:
    return reduce(lcm, (int(rate.q) for rate in rates), 1)


def _valuation(expr: sp.Expr, t: sp.Symbol) -> sp.Rational:
    try:
        leading = sp.simplify(expr.as_leading_term(t))
        exponent = sp.simplify(leading.as_powers_dict().get(t, sp.Integer(0)))
    except (NotImplementedError, ValueError, TypeError) as exc:
        raise SemanticFailure(FailureCode.NORMAL_FORM, f"cannot determine t-valuation of {expr}") from exc
    if not exponent.is_Rational:
        raise SemanticFailure(FailureCode.NORMAL_FORM, f"nonrational t-valuation {exponent}")
    return sp.Rational(exponent)


def _rewrite(
    expr: sp.Expr,
    parameter: sp.Symbol,
    t: sp.Symbol,
    q: int,
    counter: list[int],
) -> sp.Expr:
    counter[0] += 1
    if expr == parameter:
        raise SemanticFailure(
            FailureCode.FREE_PARAMETER,
            "the asymptotic parameter occurs outside an admissible exponential rate",
        )
    if expr.is_Atom:
        return expr
    if expr.func is sp.exp:
        rate, residual = _direct_rate(expr.args[0], parameter)
        rewritten_residual = _rewrite(residual, parameter, t, q, counter)
        if rate == 0 and _valuation(rewritten_residual, t) < 0:
            raise SemanticFailure(
                FailureCode.NESTED_SCALE,
                "an outer exponential receives an unbounded negative-valuation argument",
            )
        exponent = -sp.Rational(rate) * q
        if not exponent.is_Integer:
            raise SemanticFailure(FailureCode.NORMAL_FORM, "derived chart did not integerize an exponential rate")
        return sp.simplify(t ** int(exponent) * sp.exp(rewritten_residual))
    rewritten_args = tuple(_rewrite(item, parameter, t, q, counter) for item in expr.args)
    try:
        return expr.func(*rewritten_args)
    except (TypeError, ValueError) as exc:
        raise SemanticFailure(FailureCode.NORMAL_FORM, f"cannot rebuild {expr.func}") from exc


def _max_cancellation_jump(expr: sp.Expr, t: sp.Symbol) -> int:
    best = 0
    for node in sp.preorder_traversal(expr):
        if isinstance(node, sp.Add):
            child_values = [_valuation(item, t) for item in node.args]
            sum_value = _valuation(node, t)
            jump = sum_value - min(child_values)
            if jump.is_Integer and jump > best:
                best = int(jump)
    return best


def _failure_certificate(
    source: Mapping[str, Any],
    context: Mapping[str, Any],
    observer: Mapping[str, Any],
    failure: SemanticFailure,
    *,
    nodes: int = 0,
) -> LESemanticCertificate:
    status = Status.RESOURCE_EXCEEDED if failure.resource else Status.UNSUPPORTED
    cost = CostLedger(nodes, 0, 0, 0, 0, 0, 0, 2, 1)
    base = LESemanticCertificate(
        SCHEMA, status, digest(source), digest(context), digest(observer), None, (), None,
        None, None, None, None, None, (), (), CLAIM_SCOPE,
        ({"code": failure.code.value, "message": failure.message},), cost, "",
    )
    size = 0
    for _ in range(4):
        sized = replace(base, cost=replace(cost, certificate_bytes=size), certificate_digest="0" * 64)
        new_size = len(canonical_json(sized.to_data()).encode("utf-8"))
        if size == new_size:
            break
        size = new_size
    base = replace(base, cost=replace(cost, certificate_bytes=size))
    return replace(base, certificate_digest=digest(base.payload()))


def evaluate(
    source: Mapping[str, Any],
    context: Mapping[str, Any],
    observer: Mapping[str, Any],
    budget: EvaluatorBudget | None = None,
) -> LESemanticCertificate:
    budget = budget or EvaluatorBudget()
    nodes = 0
    try:
        if context.get("direction") != "+infinity" or context.get("branch_policy") != "real-positive-log":
            raise SemanticFailure(FailureCode.OUTSIDE_GRAMMAR, "context is outside the frozen real positive-infinity regime")
        if observer.get("kind") != "exact-limit":
            raise SemanticFailure(FailureCode.OUTSIDE_GRAMMAR, "only the exact-limit observer is implemented")
        retained_order = max(2, int(observer.get("residual_order", 1)) + 1)
        if retained_order > budget.max_series_order:
            raise SemanticFailure(FailureCode.ORDER_BUDGET, "requested residual order exceeds the series budget", resource=True)

        expr, domain_witnesses, nodes = decode_expression(source, context.get("assumptions", {}))
        if nodes > budget.max_nodes:
            raise SemanticFailure(FailureCode.NODE_BUDGET, "source exceeds the node budget", resource=True)
        parameter = next(item for item in expr.free_symbols if item.name == context.get("parameter", "N"))
        t = sp.Symbol("t", positive=True)
        rates = _collect_rates(expr, parameter)
        q = _chart_denominator(rates)
        if q > budget.max_q:
            raise SemanticFailure(FailureCode.Q_BUDGET, f"derived q={q} exceeds the chart budget", resource=True)

        rewrite_counter = [0]
        rewritten = _rewrite(expr, parameter, t, q, rewrite_counter)
        if rewritten.has(parameter):
            raise SemanticFailure(FailureCode.FREE_PARAMETER, "parameter remains after chart rewriting")
        cancellation = _max_cancellation_jump(rewritten, t)
        try:
            normal = sp.series(rewritten, t, 0, retained_order)
            leading = sp.simplify(rewritten.as_leading_term(t))
        except (NotImplementedError, ValueError, TypeError, PoleError) as exc:
            raise SemanticFailure(FailureCode.NORMAL_FORM, "SymPy could not construct the finite Laurent/Taylor band") from exc
        valuation = _valuation(rewritten, t)
        if valuation < 0:
            raise SemanticFailure(FailureCode.NONFINITE_LIMIT, "the exact-limit observer sees a divergent leading valuation")
        limit_value = sp.Integer(0) if valuation > 0 else sp.simplify(leading)
        if limit_value.has(t) or limit_value.has(parameter) or limit_value in {sp.oo, -sp.oo, sp.zoo, sp.nan}:
            raise SemanticFailure(FailureCode.NONFINITE_LIMIT, "no exact finite parameter-free limit was certified")

        normal_without_order = normal.removeO()
        normal_terms = len(sp.Add.make_args(sp.expand(normal_without_order)))
        residual = f"O(t**{retained_order})"
        provisional = CostLedger(
            nodes, len(tuple(sp.preorder_traversal(expr))), rewrite_counter[0], retained_order,
            normal_terms, 2 + len(rates), 0, 4 + nodes + rewrite_counter[0], 0,
        )
        certificate = LESemanticCertificate(
            SCHEMA,
            Status.EVALUATED,
            digest(source),
            digest(context),
            digest(observer),
            q,
            tuple(sorted(str(item) for item in rates)),
            f"t=exp(-{context.get('parameter', 'N')}/{q})->0+",
            str(normal),
            str(limit_value),
            retained_order,
            cancellation,
            residual,
            domain_witnesses,
            DISCHARGED,
            CLAIM_SCOPE,
            (),
            provisional,
            "",
        )
        size = 0
        for _ in range(4):
            sized = replace(certificate, cost=replace(provisional, certificate_bytes=size), certificate_digest="0" * 64)
            new_size = len(canonical_json(sized.to_data()).encode("utf-8"))
            if size == new_size:
                break
            size = new_size
        certificate = replace(certificate, cost=replace(provisional, certificate_bytes=size))
        certificate = replace(certificate, certificate_digest=digest(certificate.payload()))
        if len(canonical_json(certificate.to_data()).encode("utf-8")) > budget.max_certificate_bytes:
            raise SemanticFailure(FailureCode.CERTIFICATE_BUDGET, "certificate exceeds the byte budget", resource=True)
        return certificate
    except StopIteration:
        failure = SemanticFailure(FailureCode.FREE_PARAMETER, "declared parameter is absent from the decoded expression")
        return _failure_certificate(source, context, observer, failure, nodes=nodes)
    except SemanticFailure as failure:
        return _failure_certificate(source, context, observer, failure, nodes=nodes)
