"""JSON corpus runner with deterministic results and replay."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .certificate import replay_certificate
from .compiler import CarrierCompiler, CompilerBudget
from .ir import expr_from_data
from .model import Carrier


def run_corpus(path: str | Path) -> dict[str, Any]:
    source = json.loads(Path(path).read_text(encoding="utf-8"))
    budget = CompilerBudget(**source["budget"])
    compiler = CarrierCompiler(budget)
    rows = []
    for case in source["cases"]:
        expr = expr_from_data(case["expression"])
        requested = Carrier(case["requested_carrier"]) if case.get("requested_carrier") else None
        certificate = compiler.compile(expr, requested).to_data()
        replay = replay_certificate(case["expression"], certificate)
        rows.append({
            "id": case["id"],
            "certificate": certificate,
            "replay": {"valid": replay.valid, "steps": replay.steps, "failures": list(replay.failures)},
        })
    return {"schema": "process-geometry/carrier-corpus-result/v0", "cases": rows}
