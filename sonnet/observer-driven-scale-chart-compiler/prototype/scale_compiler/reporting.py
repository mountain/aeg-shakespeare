"""Stable JSON-compatible summaries for replay and cross-workstream comparison."""

from __future__ import annotations

from dataclasses import asdict

from .balance import BalanceResult
from .compiler import CompilationReport


def _scale(scale) -> str | None:
    return None if scale is None else str(scale)


def compilation_summary(report: CompilationReport) -> dict[str, object]:
    result_terms = []
    if report.result is not None:
        result_terms = [
            {"scale": str(scale), "coefficient": str(coefficient)}
            for scale, coefficient in report.result.ordered_terms()
        ]
    return {
        "status": report.status,
        "certified": report.certified,
        "result_terms": result_terms,
        "remainder": _scale(report.result.remainder if report.result else None),
        "residuals": [
            {
                "source": residual.source,
                "order": str(residual.order),
                "visible": residual.visible,
                "reason": residual.reason,
            }
            for residual in report.residuals
        ],
        "visibility_events": [
            {
                "source": event.source,
                "hidden_input": str(event.hidden_input),
                "amplifier": str(event.amplifier),
                "output_effect": str(event.output_effect),
                "rescued": event.rescued,
                "explanation": event.explanation,
            }
            for event in report.visibility_events
        ],
        "obligations": [
            {
                "path": obligation.path,
                "operator": obligation.operator,
                "child": obligation.child,
                "parent_required": str(obligation.parent_required),
                "child_required": str(obligation.child_required),
                "rule": obligation.rule,
            }
            for obligation in report.obligations
        ],
        "decisions": list(report.decisions),
        "failures": [asdict(failure) for failure in report.failures],
        "cost": asdict(report.cost),
    }


def balance_summary(result: BalanceResult) -> dict[str, object]:
    return {
        "status": result.status,
        "certified": result.certified,
        "scales": {name: str(scale) for name, scale in result.scales.items()},
        "equations": [
            {
                "term_coefficient": str(equation.term.coefficient),
                "term_powers": dict(equation.term.powers),
                "coefficients": [str(value) for value in equation.coefficients],
                "right_hand_side": str(equation.right_hand_side),
            }
            for equation in result.equations
        ],
        "term_orders": [str(order) for order in result.term_orders],
        "normalized_phase": str(result.normalized_phase),
        "scope": result.scope,
        "certificate_checks": list(result.certificate_checks),
        "cost": {
            "expanded_terms": result.input_term_count,
            "solve_rank": result.solve_rank,
        },
    }
