from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path

from finite_le_semantics import EvaluatorBudget, c2_semantic_discharge, evaluate, replay_certificate
from finite_le_semantics.model import canonical_json, digest


ROOT = Path(__file__).parents[1]
CORPUS = json.loads((ROOT / "PUBLIC_CORPUS.json").read_text())
CONTEXT = CORPUS["context"]
OBSERVER = CORPUS["observer"]
CASES = {case["id"]: case for case in CORPUS["cases"]}


def compile_case(case_id: str):
    source = CASES[case_id]["expression"]
    cert = evaluate(source, CONTEXT, OBSERVER)
    replay = replay_certificate(source, CONTEXT, OBSERVER, cert.to_data())
    return cert, replay


def test_p1_compiler_computes_exp2_instead_of_delegating_limit() -> None:
    cert, replay = compile_case("p1-mixed-exp-nesting")
    assert cert.status.value == "evaluated"
    assert cert.q == 1
    assert cert.limit == "exp(2)"
    assert cert.normal_form == "exp(2) + 2*t*exp(2) + O(t**2)"
    assert cert.cancellation_jump == 1
    assert replay.valid


def test_p2_retains_logarithmic_cancellation_and_returns_one_third() -> None:
    cert, replay = compile_case("p2-third-order-log-cancellation")
    assert cert.limit == "1/3"
    assert cert.cancellation_jump == 2
    assert len(cert.domain_witnesses) == 1
    assert cert.domain_witnesses[0].path == "root.1.0"
    assert replay.valid


def test_p3_derives_common_rational_rate_chart_q6() -> None:
    cert, replay = compile_case("p3-rational-rate-q6")
    assert cert.q == 6
    assert cert.chart == "t=exp(-N/6)->0+"
    assert cert.rates == ("-1/2", "-1/3", "1/3")
    assert cert.limit == "1"
    assert replay.valid


def test_frozen_negative_controls_fail_with_exact_codes() -> None:
    for case_id in (
        "n1-log-domain-missing",
        "n2-irrational-rate",
        "n3-nested-unbounded-scale",
        "n4-symbolic-height",
    ):
        cert, replay = compile_case(case_id)
        assert cert.status.value == CASES[case_id]["expected"]["status"]
        assert cert.failures[0]["code"] == CASES[case_id]["expected"]["failure"]
        assert cert.discharged_c2_obligations == ()
        assert replay.valid


def test_order_budget_fails_before_semantic_credit() -> None:
    source = CASES["p2-third-order-log-cancellation"]["expression"]
    observer = {"kind": "exact-limit", "residual_order": 3}
    cert = evaluate(source, CONTEXT, observer, EvaluatorBudget(max_series_order=2))
    assert cert.status.value == "resource-exceeded"
    assert cert.failures[0]["code"] == "series-order-budget-exceeded"
    assert cert.limit is None
    assert cert.discharged_c2_obligations == ()


def test_q_budget_is_typed_and_fail_closed() -> None:
    source = {
        "op": "exp",
        "argument": {
            "op": "mul",
            "factors": [
                {"op": "const", "value": "-1/25"},
                {"op": "symbol", "name": "N"},
            ],
        },
    }
    cert = evaluate(source, CONTEXT, OBSERVER)
    assert cert.status.value == "resource-exceeded"
    assert cert.failures[0]["code"] == "exponential-chart-denominator-budget-exceeded"


def test_certificate_size_is_charged_exactly() -> None:
    cert, _ = compile_case("p1-mixed-exp-nesting")
    assert cert.cost.certificate_bytes == len(canonical_json(cert.to_data()).encode("utf-8"))
    assert cert.cost.normal_form_terms > 0
    assert cert.cost.rewrite_visits > 0
    negative, _ = compile_case("n1-log-domain-missing")
    assert negative.cost.certificate_bytes == len(canonical_json(negative.to_data()).encode("utf-8"))


def test_adapter_discharges_only_the_frozen_c2_semantic_scope() -> None:
    positive, _ = compile_case("p2-third-order-log-cancellation")
    negative, _ = compile_case("n1-log-domain-missing")
    accepted = c2_semantic_discharge(positive.to_data())
    refused = c2_semantic_discharge(negative.to_data())
    assert all(item["discharged"] for item in accepted["obligations"])
    assert not any(item["discharged"] for item in refused["obligations"])
    assert accepted["general_le_claim"] is False
    assert accepted["surreal_runtime_used"] is False


def test_replay_rejects_tampered_q_result_residual_branch_and_cost() -> None:
    source = CASES["p2-third-order-log-cancellation"]["expression"]
    cert = evaluate(source, CONTEXT, OBSERVER).to_data()
    mutations = (
        ("q", 2),
        ("limit", "1/2"),
        ("residual", "O(t**9)"),
        ("domain_witnesses", []),
        ("cost", {**cert["cost"], "comparison_steps": 0}),
    )
    for field, value in mutations:
        tampered = {**cert, field: value}
        payload = dict(tampered)
        payload.pop("certificate_digest")
        tampered["certificate_digest"] = digest(payload)
        replay = replay_certificate(source, CONTEXT, OBSERVER, tampered)
        assert not replay.valid
        assert any(item.endswith("-mismatch") for item in replay.failures)


def test_source_context_and_observer_digests_are_bound() -> None:
    source = CASES["p1-mixed-exp-nesting"]["expression"]
    cert = evaluate(source, CONTEXT, OBSERVER).to_data()
    changed_context = {**CONTEXT, "direction": "-infinity"}
    replay = replay_certificate(source, changed_context, OBSERVER, cert)
    assert not replay.valid
    assert "context-digest-mismatch" in replay.failures


def test_compiler_and_replay_source_do_not_call_generic_limit_or_store_expected() -> None:
    source_text = "\n".join(
        (ROOT / "finite_le_semantics" / name).read_text()
        for name in ("evaluator.py", "replay.py")
    )
    assert ".limit(" not in source_text
    assert "sympy.limit" not in source_text
    cert, _ = compile_case("p1-mixed-exp-nesting")
    serialized = canonical_json(cert.to_data())
    assert "expected" not in serialized
    assert "full_trace" not in serialized


def test_real_rational_powers_fail_closed_without_domain_witnesses() -> None:
    source = {
        "op": "pow",
        "base": {"op": "symbol", "name": "x"},
        "exponent": "1/2",
    }
    cert = evaluate(source, CONTEXT, OBSERVER)
    assert cert.status.value == "unsupported"
    assert cert.failures[0]["code"] == "outside-frozen-expression-grammar"
    assert "positive-base witness" in cert.failures[0]["message"]
