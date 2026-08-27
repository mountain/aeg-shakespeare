"""Same-information SymPy baseline; deliberately separate from compiler semantics."""

from __future__ import annotations

import json
from pathlib import Path
from time import perf_counter_ns

import sympy as sp

from finite_le_semantics.ast import decode_expression


ROOT = Path(__file__).resolve().parent


def main() -> None:
    corpus = json.loads((ROOT / "PUBLIC_CORPUS.json").read_text())
    context = corpus["context"]
    rows = []
    for case in corpus["cases"]:
        if "limit" not in case["expected"]:
            continue
        expression, _, nodes = decode_expression(case["expression"], context["assumptions"])
        parameter = next(item for item in expression.free_symbols if item.name == context["parameter"])
        started = perf_counter_ns()
        result = sp.limit(expression, parameter, sp.oo)
        elapsed = perf_counter_ns() - started
        rows.append({
            "id": case["id"],
            "backend": f"SymPy {sp.__version__}",
            "same_source_nodes": nodes,
            "result": str(result),
            "matches_frozen_expected": str(result) == case["expected"]["limit"],
            "elapsed_ns": elapsed,
            "semantic_authority": False,
            "certificate": None,
        })
    print(json.dumps({
        "schema": "process-geometry/finite-le-baseline-result/v0",
        "claim_boundary": "The baseline receives the same AST and assumptions, but its generic limit call supplies no compiler certificate or replay credit.",
        "cases": rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
