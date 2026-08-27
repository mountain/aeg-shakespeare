from __future__ import annotations

import json
from pathlib import Path

from finite_le_semantics import run_corpus


def test_public_corpus_matches_frozen_expectations() -> None:
    root = Path(__file__).parents[1]
    corpus = json.loads((root / "PUBLIC_CORPUS.json").read_text())
    expected = {case["id"]: case["expected"] for case in corpus["cases"]}
    result = run_corpus(root / "PUBLIC_CORPUS.json")
    rows = {row["id"]: row for row in result["cases"]}
    for case_id, wanted in expected.items():
        certificate = rows[case_id]["certificate"]
        assert certificate["status"] == wanted["status"]
        if "q" in wanted:
            assert certificate["q"] == wanted["q"]
        if "limit" in wanted:
            assert certificate["limit"] == wanted["limit"]
        if "failure" in wanted:
            assert certificate["failures"][0]["code"] == wanted["failure"]
        if "minimum_cancellation_jump" in wanted:
            assert certificate["cancellation_jump"] >= wanted["minimum_cancellation_jump"]
        assert rows[case_id]["replay"]["valid"] is True


def test_recorded_public_result_matches_deterministic_replay() -> None:
    root = Path(__file__).parents[1]
    recorded = json.loads((root / "PUBLIC_RESULT.json").read_text())
    rerun = run_corpus(root / "PUBLIC_CORPUS.json")
    actual = []
    for row in rerun["cases"]:
        certificate = row["certificate"]
        actual.append({
            "id": row["id"],
            "status": certificate["status"],
            "q": certificate["q"],
            "limit": certificate["limit"],
            "cancellation_jump": certificate["cancellation_jump"],
            "residual": certificate["residual"],
            "certificate_digest": certificate["certificate_digest"],
            "certificate_bytes": certificate["cost"]["certificate_bytes"],
            "replay_valid": row["replay"]["valid"],
            "failure": certificate["failures"][0]["code"] if certificate["failures"] else None,
        })
    assert recorded["cases"] == actual


def test_baseline_is_labeled_as_non_authoritative_and_certificate_free() -> None:
    root = Path(__file__).parents[1]
    baseline = json.loads((root / "BASELINE_RESULTS.json").read_text())
    assert all(case["matches_frozen_expected"] for case in baseline["cases"])
    assert all(case["semantic_authority"] is False for case in baseline["cases"])
    assert all(case["certificate"] is None for case in baseline["cases"])
