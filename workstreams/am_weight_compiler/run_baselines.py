from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
from statistics import median
from time import perf_counter_ns
from typing import Any, Mapping

import sympy as sp

from am_weight_compiler.evaluator import evaluate_case
from am_weight_compiler.model import Budgets
from am_weight_compiler.replay import replay_certificate


x = sp.Symbol("x", positive=True)


def rational(value: object) -> sp.Rational:
    parsed = Fraction(str(value))
    return sp.Rational(parsed.numerator, parsed.denominator)


def to_sympy(node: Mapping[str, Any]) -> sp.Expr:
    op = node["op"]
    if op == "finite":
        return sum(
            (
                rational(term["coefficient"]) * x ** rational(term["weight"])
                for term in node["terms"]
            ),
            sp.S.Zero,
        )
    if op == "add":
        return sum((to_sympy(argument) for argument in node["arguments"]), sp.S.Zero)
    if op == "multiply":
        return sp.prod(to_sympy(argument) for argument in node["arguments"])
    if op == "scale":
        return rational(node["coefficient"]) * to_sympy(node["argument"])
    if op == "shift":
        return x ** rational(node["by"]) * to_sympy(node["argument"])
    if op == "exp":
        return sp.exp(to_sympy(node["argument"]))
    if op == "log1p":
        return sp.log(1 + to_sympy(node["argument"]))
    raise ValueError(f"baseline does not support {op}")


def source_horizon(node: Mapping[str, Any], target: int) -> int:
    op = node["op"]
    if op == "shift":
        shift = Fraction(str(node["by"]))
        if shift.denominator != 1:
            raise ValueError("baseline window only reports integer weights")
        return source_horizon(node["argument"], target - shift.numerator)
    if op in {"add", "multiply"}:
        return max(source_horizon(argument, target) for argument in node["arguments"])
    if op in {"scale", "exp", "log1p"}:
        return source_horizon(node["argument"], target)
    return target


def source_measure(node: Mapping[str, Any]) -> tuple[int, int]:
    op = node["op"]
    if op == "finite":
        return 1, len(node["terms"])
    if op in {"add", "multiply"}:
        children = [source_measure(argument) for argument in node["arguments"]]
        return 1 + sum(item[0] for item in children), sum(item[1] for item in children)
    if op in {"scale", "shift", "exp", "log1p"}:
        nodes, terms = source_measure(node["argument"])
        return nodes + 1, terms
    raise ValueError(f"baseline does not support {op}")


def benchmark_case(case: Mapping[str, Any], repetitions: int = 3) -> dict[str, object]:
    target = Fraction(str(case["target_weight"]))
    if target.denominator != 1:
        raise ValueError("baseline benchmark cases use integer target weights")
    expression = to_sympy(case["expression"])
    target_int = target.numerator
    samples: list[float] = []
    coefficient = None
    expanded = None
    for _ in range(repetitions):
        started = perf_counter_ns()
        expanded = sp.series(expression, x, 0, target_int + 1).removeO().expand()
        coefficient = expanded.coeff(x, target_int)
        samples.append((perf_counter_ns() - started) / 1_000_000)
    assert coefficient is not None and expanded is not None
    nodes, finite_terms = source_measure(case["expression"])
    horizon = source_horizon(case["expression"], target_int)
    return {
        "case_id": case["id"],
        "status": "evaluated",
        "coefficient": str(coefficient),
        "method": "same-information-truncated-series-window",
        "source": {"nodes": nodes, "finite_terms": finite_terms},
        "materialized_window": {
            "minimum_weight": 0,
            "maximum_source_weight": horizon,
            "weight_count": horizon + 1,
        },
        "expanded_term_count": len(sp.Add.make_args(expanded)),
        "wall_time_ms": {
            "samples": [round(value, 6) for value in samples],
            "median": round(median(samples), 6),
            "authority": "non-authoritative",
        },
        "semantic_or_certificate_credit": False,
    }


def benchmark_candidate(
    case: Mapping[str, Any],
    context: Mapping[str, object],
    budgets: Budgets,
    repetitions: int = 5,
) -> dict[str, object]:
    evaluation_samples: list[float] = []
    replay_samples: list[float] = []
    certificate = None
    replay = None
    for _ in range(repetitions):
        started = perf_counter_ns()
        certificate = evaluate_case(case, context, budgets)
        evaluation_samples.append((perf_counter_ns() - started) / 1_000_000)
        started = perf_counter_ns()
        replay = replay_certificate(case, context, budgets, certificate)
        replay_samples.append((perf_counter_ns() - started) / 1_000_000)
    assert certificate is not None and replay is not None
    return {
        "status": certificate["status"],
        "coefficient": certificate["result"].get("coefficient"),
        "dependencies": certificate["dependencies"],
        "costs": certificate["costs"],
        "certificate_digest": certificate["certificate_digest"],
        "replay_status": replay["status"],
        "wall_time_ms": {
            "evaluation_samples": [round(value, 6) for value in evaluation_samples],
            "evaluation_median": round(median(evaluation_samples), 6),
            "replay_samples": [round(value, 6) for value in replay_samples],
            "replay_median": round(median(replay_samples), 6),
            "authority": "non-authoritative",
        },
    }


def load_cases(root: Path) -> list[Mapping[str, Any]]:
    public = json.loads((root / "PUBLIC_CORPUS.json").read_text(encoding="utf-8"))
    reveal = json.loads((root / "HELD_OUT_REVEAL.json").read_text(encoding="utf-8"))
    selected = [
        case
        for case in public["cases"]
        if case["id"] in {"p2-weight32-log-cancellation", "p3-completed-exp-composition"}
    ]
    return [*selected, reveal["executable_case"]]


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    contract_data = json.loads((root / "FROZEN_CONTRACT.json").read_text(encoding="utf-8"))
    public_data = json.loads((root / "PUBLIC_CORPUS.json").read_text(encoding="utf-8"))
    budgets = Budgets.from_mapping(contract_data["budgets"])
    cases = load_cases(root)
    rows = []
    for case in cases:
        row = benchmark_case(case)
        row["candidate"] = benchmark_candidate(case, public_data["context"], budgets)
        rows.append(row)
    result = {
        "schema": "process-geometry/am-weight-observed-baselines/v0",
        "engine": f"SymPy {sp.__version__}",
        "contract": "BASELINE_CONTRACT.json",
        "cases": rows,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
