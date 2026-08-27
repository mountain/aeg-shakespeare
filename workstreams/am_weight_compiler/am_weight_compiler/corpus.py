from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from .evaluator import evaluate_case
from .model import Budgets
from .replay import replay_certificate


def _expected_matches(expected: Mapping[str, Any], certificate: Mapping[str, Any]) -> bool:
    if certificate["status"] != expected["status"]:
        return False
    result = certificate["result"]
    if "failure" in expected:
        return result.get("failure") == expected["failure"]
    for key, value in expected.items():
        if key in {"status", "maximum_visited_weights"}:
            continue
        if result.get(key) != value:
            return False
    maximum = expected.get("maximum_visited_weights")
    if maximum is not None and certificate["dependencies"]["request_count"] > maximum:
        return False
    return True


def run_corpus(
    corpus_path: Path,
    contract_path: Path,
) -> dict[str, Any]:
    corpus = json.loads(corpus_path.read_text(encoding="utf-8"))
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    budgets = Budgets.from_mapping(contract["budgets"])
    rows = []
    for case in corpus["cases"]:
        certificate = evaluate_case(case, corpus["context"], budgets)
        replay = replay_certificate(case, corpus["context"], budgets, certificate)
        passed = _expected_matches(case["expected"], certificate)
        passed = passed and replay["status"] == "verified"
        rows.append(
            {
                "case_id": case["id"],
                "passed": passed,
                "certificate": certificate,
                "replay": replay,
            }
        )
    return {
        "schema": "process-geometry/am-weight-corpus-result/v0",
        "corpus_schema": corpus["schema"],
        "passed": all(row["passed"] for row in rows),
        "pass_count": sum(bool(row["passed"]) for row in rows),
        "case_count": len(rows),
        "rows": rows,
    }
