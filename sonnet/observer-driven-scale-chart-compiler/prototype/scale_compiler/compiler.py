"""Observer-driven evaluation and delayed truncation.

The key discipline is simple: intermediate terms are never dropped merely
because the final observer cannot currently see them.  The compiler first
propagates them through the entire expression, including ``pow -> log; mul;
exp``, and truncates only at the output boundary.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from math import factorial
from typing import Mapping

import sympy as sp

from .ir import Add, Const, Exp, Expr, Log, Mul, Pow, Var, walk
from .scale import Obligation, Observer, Residual, Scale, Series, VisibilityEvent


class CompilationError(Exception):
    """Typed research failure; callers receive it in a report."""

    code = "compilation-error"


class MissingBindingError(CompilationError):
    code = "missing-binding"


class UnsupportedScaleError(CompilationError):
    code = "unsupported-scale"


class DomainError(CompilationError):
    code = "domain-error"


class ResourceBudgetError(CompilationError):
    code = "resource-budget-exceeded"


@dataclass
class CostStats:
    input_nodes: int = 0
    evaluations: int = 0
    additions: int = 0
    multiplications: int = 0
    taylor_terms: int = 0
    peak_terms: int = 0
    retries: int = 0
    backward_obligations: int = 0
    retained_terms: int = 0
    residual_records: int = 0
    branch_cases: int = 0
    decoder_operations: int = 0


@dataclass(frozen=True)
class Failure:
    code: str
    message: str


@dataclass(frozen=True)
class CompilationReport:
    status: str
    expression: Expr
    observer: Observer
    result: Series | None
    residuals: tuple[Residual, ...]
    visibility_events: tuple[VisibilityEvent, ...]
    obligations: tuple[Obligation, ...]
    decisions: tuple[str, ...]
    failures: tuple[Failure, ...]
    cost: CostStats

    @property
    def certified(self) -> bool:
        return self.status == "ok" and not any(r.visible for r in self.residuals)


@dataclass
class _State:
    observer: Observer
    taylor_order: int
    cost: CostStats
    events: list[VisibilityEvent] = field(default_factory=list)
    decisions: list[str] = field(default_factory=list)
    values: dict[int, Series] = field(default_factory=dict)

    def observe_series(self, series: Series) -> Series:
        if series.term_count > self.observer.max_live_terms:
            raise ResourceBudgetError("live series exceeded the declared term budget")
        self.cost.peak_terms = max(self.cost.peak_terms, series.term_count)
        return series


def compile_expression(
    expression: Expr,
    bindings: Mapping[str, Series],
    observer: Observer | None = None,
) -> CompilationReport:
    """Compile a finite expression against an explicit observation contract.

    Taylor depth is increased until the declared remainder threshold is met or
    the observer's finite budget is exhausted.  Failures are data, not silent
    fallbacks.
    """

    observer = observer or Observer()
    cost = CostStats(input_nodes=len({id(node) for node in walk(expression)}))
    if cost.input_nodes > observer.max_input_nodes:
        return CompilationReport(
            status="failed",
            expression=expression,
            observer=observer,
            result=None,
            residuals=(),
            visibility_events=(),
            obligations=(),
            decisions=(),
            failures=(Failure("resource-budget-exceeded", "expression DAG exceeds the node budget"),),
            cost=cost,
        )
    order = observer.initial_taylor_order
    last_series: Series | None = None
    last_events: list[VisibilityEvent] = []
    last_decisions: list[str] = []
    last_obligations: list[Obligation] = []

    while order <= observer.max_taylor_order:
        state = _State(observer, order, cost)
        cost.evaluations += 1
        try:
            series = _evaluate(expression, bindings, state)
        except CompilationError as error:
            return CompilationReport(
                status="failed",
                expression=expression,
                observer=observer,
                result=None,
                residuals=(),
                visibility_events=tuple(state.events),
                obligations=(),
                decisions=tuple(state.decisions),
                failures=(Failure(error.code, str(error)),),
                cost=cost,
            )

        last_series = series
        last_events = state.events
        last_decisions = state.decisions
        obligations = _derive_obligations(
            expression,
            observer.visible_at_or_above,
            state,
        )
        last_obligations = obligations
        cost.backward_obligations = len(obligations)
        if series.remainder is None or series.remainder < observer.require_remainder_below:
            output, dropped = series.truncate_below(observer.require_remainder_below)
            residuals = _residuals(output, observer, dropped)
            cost.retained_terms = output.term_count
            cost.residual_records = len(residuals)
            return CompilationReport(
                status="ok",
                expression=expression,
                observer=observer,
                result=output,
                residuals=residuals,
                visibility_events=tuple(state.events),
                obligations=tuple(obligations),
                decisions=tuple(state.decisions),
                failures=(),
                cost=cost,
            )

        if order == observer.max_taylor_order:
            break
        next_order = min(observer.max_taylor_order, order * 2)
        if next_order == order:
            break
        cost.retries += 1
        order = next_order

    assert last_series is not None
    residuals = _residuals(last_series, observer, None)
    cost.retained_terms = last_series.term_count
    cost.residual_records = len(residuals)
    return CompilationReport(
        status="unsafe",
        expression=expression,
        observer=observer,
        result=last_series,
        residuals=residuals,
        visibility_events=tuple(last_events),
        obligations=tuple(last_obligations),
        decisions=tuple(last_decisions),
        failures=(
            Failure(
                "budget-exhausted",
                "finite Taylor budget could not place the remainder below the declared threshold",
            ),
        ),
        cost=cost,
    )


def _residuals(
    series: Series, observer: Observer, dropped: Scale | None
) -> tuple[Residual, ...]:
    residuals: list[Residual] = []
    if series.remainder is not None:
        residuals.append(
            Residual(
                "series",
                series.remainder,
                observer.is_visible(series.remainder),
                "propagated analytic or truncation remainder",
            )
        )
    if dropped is not None:
        residuals.append(
            Residual(
                "output-boundary",
                dropped,
                observer.is_visible(dropped),
                "terms dropped only after whole-expression propagation",
            )
        )
    return tuple(residuals)


def _evaluate(expression: Expr, bindings: Mapping[str, Series], state: _State) -> Series:
    cached = state.values.get(id(expression))
    if cached is not None:
        return cached
    result = _evaluate_uncached(expression, bindings, state)
    state.values[id(expression)] = result
    return result


def _evaluate_uncached(expression: Expr, bindings: Mapping[str, Series], state: _State) -> Series:
    if isinstance(expression, Const):
        return state.observe_series(Series.constant(expression.value))
    if isinstance(expression, Var):
        if expression.name not in bindings:
            raise MissingBindingError(f"no scale binding for variable {expression.name!r}")
        return state.observe_series(bindings[expression.name])
    if isinstance(expression, Add):
        result = Series.constant(0)
        for term in expression.terms:
            result = result.add(_evaluate(term, bindings, state))
            state.cost.additions += 1
        return state.observe_series(result)
    if isinstance(expression, Mul):
        result = Series.constant(1)
        for factor in expression.factors:
            right = _evaluate(factor, bindings, state)
            state.cost.multiplications += result.term_count * right.term_count
            result = result.mul(right)
        return state.observe_series(result)
    if isinstance(expression, Log):
        return state.observe_series(_log_series(_evaluate(expression.argument, bindings, state), state))
    if isinstance(expression, Exp):
        return state.observe_series(_exp_series(_evaluate(expression.argument, bindings, state), state))
    if isinstance(expression, Pow):
        base = _evaluate(expression.base, bindings, state)
        exponent = _evaluate(expression.exponent, bindings, state)
        integer = _constant_integer(exponent)
        if integer is not None:
            return state.observe_series(_integer_power(base, integer, state))

        delta = base.nonconstant()
        delta_lead = delta.leading_scale
        exponent_lead = exponent.leading_scale
        if base.constant_coefficient == 1 and delta_lead is not None and exponent_lead is not None:
            output_effect = delta_lead + exponent_lead
            rescued = (
                not state.observer.is_visible(delta_lead)
                and state.observer.is_visible(output_effect)
            )
            state.events.append(
                VisibilityEvent(
                    "pow",
                    delta_lead,
                    exponent_lead,
                    output_effect,
                    rescued,
                    "a base perturbation is propagated through exponent*log(base) before truncation",
                )
            )
        state.decisions.append("lowered non-integer pow(base, exponent) to exp(exponent * log(base))")
        logarithm = _log_series(base, state)
        state.cost.multiplications += logarithm.term_count * exponent.term_count
        argument = exponent.mul(logarithm)
        return state.observe_series(_exp_series(argument, state))
    raise UnsupportedScaleError(f"unsupported IR node {type(expression).__name__}")


def _derive_obligations(
    expression: Expr,
    required: Scale,
    state: _State,
    path: str = "root",
) -> list[Obligation]:
    """Run a backward observer pass, separately from forward evaluation."""

    obligations: list[Obligation] = []

    def descend(
        child: Expr,
        child_required: Scale,
        child_label: str,
        rule: str,
        child_path: str,
    ) -> None:
        obligations.append(
            Obligation(
                path,
                type(expression).__name__,
                child_label,
                required,
                child_required,
                rule,
            )
        )
        obligations.extend(_derive_obligations(child, child_required, state, child_path))

    if isinstance(expression, Add):
        for index, child in enumerate(expression.terms):
            descend(
                child,
                required,
                f"term[{index}]",
                "addition may expose exact ties or cancellation, so each child inherits the parent band",
                f"{path}.term[{index}]",
            )
    elif isinstance(expression, Mul):
        leads = [state.values[id(child)].leading_scale for child in expression.factors]
        for index, child in enumerate(expression.factors):
            other_leads = [lead for j, lead in enumerate(leads) if j != index]
            if any(lead is None for lead in other_leads):
                continue
            other_order = Scale(
                sum((lead.power for lead in other_leads if lead is not None), Fraction(0))
            )
            descend(
                child,
                required - other_order,
                f"factor[{index}]",
                "product child precision equals parent precision minus the other factors' order",
                f"{path}.factor[{index}]",
            )
    elif isinstance(expression, (Exp, Log)):
        descend(
            expression.argument,
            required,
            "argument",
            "within the implemented bounded germ, exp/log have order-zero local sensitivity",
            f"{path}.argument",
        )
    elif isinstance(expression, Pow):
        base = state.values[id(expression.base)]
        exponent = state.values[id(expression.exponent)]
        exponent_order = exponent.leading_scale
        delta_order = base.nonconstant().leading_scale
        if base.constant_coefficient == 1 and exponent_order is not None:
            descend(
                expression.base,
                required - exponent_order,
                "base",
                "pow=exp(exponent*log(base)); the exponent amplifies near-unit base distinctions",
                f"{path}.base",
            )
        if delta_order is not None:
            descend(
                expression.exponent,
                required - delta_order,
                "exponent",
                "exponent precision is weighted by the leading order of log(base)",
                f"{path}.exponent",
            )
    return obligations


def _constant_integer(series: Series) -> int | None:
    if series.remainder is not None or set(series.terms) - {Fraction(0)}:
        return None
    value = series.constant_coefficient
    if value.is_Integer:
        return int(value)
    return None


def _integer_power(series: Series, exponent: int, state: _State) -> Series:
    if exponent == 0:
        return Series.constant(1)
    if exponent < 0:
        if series.remainder is None and len(series.terms) == 1:
            ((power, coefficient),) = series.terms.items()
            return Series({power * exponent: coefficient ** exponent})
        logarithm = _log_series(series, state)
        return _exp_series(logarithm.scale_by(exponent), state)
    result = Series.constant(1)
    factor = series
    n = exponent
    while n:
        if n & 1:
            state.cost.multiplications += result.term_count * factor.term_count
            result = result.mul(factor)
        n >>= 1
        if n:
            state.cost.multiplications += factor.term_count * factor.term_count
            factor = factor.mul(factor)
    return result


def _small_delta(series: Series, operation: str) -> tuple[sp.Expr, Series]:
    constant = series.constant_coefficient
    delta = series.nonconstant()
    if constant == 0 and operation == "exp":
        constant = sp.S.Zero
    elif operation == "log" and constant != 1:
        raise DomainError("log series currently requires constant term exactly 1")
    lead = delta.leading_scale
    if lead is not None and lead >= Scale(0):
        raise UnsupportedScaleError(
            f"{operation} of a non-small polynomial-scale argument requires a higher log-exp scale backend"
        )
    return constant, delta


def _log_series(series: Series, state: _State) -> Series:
    _, delta = _small_delta(series, "log")
    if not delta.terms and delta.remainder is None:
        return Series.constant(0)
    result = Series.constant(0)
    power = Series.constant(1)
    for k in range(1, state.taylor_order + 1):
        state.cost.multiplications += power.term_count * delta.term_count
        power = power.mul(delta)
        coefficient = sp.Rational((-1) ** (k + 1), k)
        result = result.add(power.scale_by(coefficient))
        state.cost.taylor_terms += 1
    lead = delta.leading_scale
    if lead is not None:
        analytic_remainder = Scale((state.taylor_order + 1) * lead.power)
        remainder = analytic_remainder if result.remainder is None else max(result.remainder, analytic_remainder)
        result = Series(result.terms, remainder)
    state.decisions.append(f"expanded log(1+u) to finite order {state.taylor_order}")
    return result


def _exp_series(series: Series, state: _State) -> Series:
    constant, delta = _small_delta(series, "exp")
    if any(power > 0 for power in series.terms):
        raise UnsupportedScaleError(
            "exp of a positive polynomial order is represented by the IR but not evaluated by this backend"
        )
    result = Series.constant(1)
    power = Series.constant(1)
    for k in range(1, state.taylor_order + 1):
        state.cost.multiplications += power.term_count * delta.term_count
        power = power.mul(delta)
        result = result.add(power.scale_by(sp.Rational(1, factorial(k))))
        state.cost.taylor_terms += 1
    result = result.scale_by(sp.exp(constant))
    lead = delta.leading_scale
    if lead is not None:
        analytic_remainder = Scale((state.taylor_order + 1) * lead.power)
        remainder = analytic_remainder if result.remainder is None else max(result.remainder, analytic_remainder)
        result = Series(result.terms, remainder)
    state.decisions.append(f"expanded exp(c+u) to finite order {state.taylor_order}")
    return result
