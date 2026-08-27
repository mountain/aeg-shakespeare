"""Frozen corpus runner."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .evaluator import evaluate
from .replay import replay_certificate


def run_corpus(path: str | Path) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    context = payload["context"]
    observer = payload["observer"]
    rows = []
    for case in payload["cases"]:
        certificate = evaluate(case["expression"], context, observer)
        replay = replay_certificate(case["expression"], context, observer, certificate.to_data())
        rows.append({
            "id": case["id"],
            "certificate": certificate.to_data(),
            "replay": {"valid": replay.valid, "failures": list(replay.failures), "steps": replay.steps},
        })
    return {"schema": "process-geometry/finite-le-corpus-result/v0", "cases": rows}
