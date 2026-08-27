from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path

from am_weight_compiler.coefficients import WeightEvaluator
from am_weight_compiler.evaluator import evaluate_case
from am_weight_compiler.model import Budgets, ExpQCoefficient
from am_weight_compiler.replay import replay_certificate


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = json.loads((ROOT / "FROZEN_CONTRACT.json").read_text(encoding="utf-8"))
CORPUS = json.loads((ROOT / "PUBLIC_CORPUS.json").read_text(encoding="utf-8"))
BUDGETS = Budgets.from_mapping(CONTRACT["budgets"])
CONTEXT = CORPUS["context"]


def finite(*terms: tuple[str, str]) -> dict[str, object]:
    return {
        "op": "finite",
        "terms": [
            {"weight": weight, "coefficient": coefficient}
            for weight, coefficient in terms
        ],
    }


def test_exp_q_coefficient_is_exact_group_algebra() -> None:
    left = ExpQCoefficient.exp_atom(Fraction(2, 3)).scale_rational(3)
    right = ExpQCoefficient.exp_atom(Fraction(1, 3)).scale_rational(2)
    assert (left * right).to_text() == "6*exp(1)"
    assert (left + (-left)).to_text() == "0"


def test_generic_exp_log_recurrence_uses_only_requested_weight() -> None:
    expression = {
        "op": "exp",
        "argument": {
            "op": "add",
            "arguments": [
                {"op": "log1p", "argument": finite(("1", "1"))},
                finite(("2", "1")),
            ],
        },
    }
    evaluator = WeightEvaluator(expression, Fraction(5), CONTEXT, BUDGETS)
    assert evaluator.coefficient().to_text() == "1/2"
    assert evaluator.meter.coefficient_operations < 100


def test_rational_lattice_and_multiplication() -> None:
    expression = {
        "op": "multiply",
        "arguments": [
            {"op": "exp", "argument": finite(("1/2", "2"))},
            finite(("1/2", "3")),
        ],
    }
    evaluator = WeightEvaluator(expression, Fraction(3, 2), CONTEXT, BUDGETS)
    assert evaluator.lattice_denominator == 2
    assert evaluator.coefficient().to_text() == "6"


def test_replay_rejects_certificate_tampering() -> None:
    case = next(case for case in CORPUS["cases"] if case["id"] == "p3-completed-exp-composition")
    certificate = evaluate_case(case, CONTEXT, BUDGETS)
    tampered = deepcopy(certificate)
    tampered["result"]["coefficient"] = "exp(3)"
    assert replay_certificate(case, CONTEXT, BUDGETS, certificate)["status"] == "verified"
    assert replay_certificate(case, CONTEXT, BUDGETS, tampered)["status"] == "rejected"


def test_expected_field_has_no_semantic_effect() -> None:
    case = deepcopy(next(case for case in CORPUS["cases"] if case["id"] == "p2-weight32-log-cancellation"))
    first = evaluate_case(case, CONTEXT, BUDGETS)
    case["expected"]["coefficient"] = "999"
    second = evaluate_case(case, CONTEXT, BUDGETS)
    assert first == second


def test_source_firewall_excludes_generic_oracles() -> None:
    source = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (ROOT / "am_weight_compiler").glob("*.py")
    )
    assert ".series(" not in source
    assert ".limit(" not in source
