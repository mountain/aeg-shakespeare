from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def test_reveal_matches_pre_reveal_commitment() -> None:
    reveal = json.loads((ROOT / "HELD_OUT_REVEAL.json").read_text())
    commitment = json.loads((ROOT / "HELD_OUT_COMMITMENT.json").read_text())
    assert sha256(canonical_bytes(reveal)).hexdigest() == commitment["payload_sha256"]


def test_heldout_results_replay_and_obey_firewall() -> None:
    result = json.loads((ROOT / "HELD_OUT_RESULT.json").read_text())
    assert result["freeze"]["commitment_valid"] is True
    assert all(case["compiler_replay_valid"] for case in result["cases"])
    assert all(case["independent_firewall_valid"] for case in result["cases"])
    assert result["forbidden_certificate_fields_present"] == []


def test_finite_height_is_not_promoted_to_symbolic_height() -> None:
    result = json.loads((ROOT / "HELD_OUT_RESULT.json").read_text())
    fixed = next(case for case in result["cases"] if case["id"] == "heldout-l2-fixed-iterate")
    symbolic = next(case for case in result["cases"] if case["id"] == "heldout-l2-symbolic-height")
    assert fixed["construction_height"] == 7
    assert fixed["symbolic_height_credit"] is False
    assert symbolic["compiler_status"] == "unsupported"
    assert symbolic["minimum_declared_carrier"] is None
    assert symbolic["failure_code"] == "symbolic-height-not-finite-unrolling"
    assert symbolic["typed_refusal_valid"] is True


def test_finite_semantic_baselines_execute_without_larger_carrier() -> None:
    result = json.loads((ROOT / "HELD_OUT_RESULT.json").read_text())
    finite = [case for case in result["cases"] if case["id"] != "heldout-l2-symbolic-height"]
    assert all(case["minimum_declared_carrier"] == "C2-finite-height-le" for case in finite)
    assert all(case["semantic_result_valid"] is True for case in finite)
    assert all(case["compiler_semantic_task_pass"] is False for case in finite)
    assert result["disposition"] == "NARROW"


def test_k7_is_retained_only_as_an_out_of_budget_probe() -> None:
    result = json.loads((ROOT / "HELD_OUT_RESULT.json").read_text())
    fixed = next(case for case in result["cases"] if case["id"] == "heldout-l2-fixed-iterate")
    assert fixed["budget_status"] == "outside-redteam-fixed-height-budget"
    assert fixed["outside_contract"] is True
    assert fixed["acceptance_credit"] is False
    assert result["disposition"] == "NARROW"
    assert result["executable_finite_subset_surreal_runtime_disposition"] == "ELIMINATE"
