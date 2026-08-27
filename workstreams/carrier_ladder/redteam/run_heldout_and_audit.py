"""Reveal-time runner for the strict issue #142 held-out corpus."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import sympy as sp


HERE = Path(__file__).resolve().parent
COMPILER_ROOT = HERE.parent / "compiler"
sys.path.insert(0, str(COMPILER_ROOT))

from carrier_compiler.corpus import run_corpus  # noqa: E402

from audit_candidate_certificate import audit  # noqa: E402


EXPECTED_COMMITMENT = "40103ae7cdfc5d32bf0917fe98b28c2f427ef6fde7b829535da7a4447376ecd3"


def canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def independent_audit(row: dict[str, object]) -> dict[str, object]:
    cert = row["certificate"]
    minimum = cert["minimum_declared_carrier"]
    adapter = {
        "selected_carrier": None if minimum is None else minimum.split("-", 1)[0],
        "passed_carriers": [] if minimum is None else [minimum.split("-", 1)[0]],
        "symbolic_height_credit": False,
        "evidence": {
            "kind": "exact_lowering" if minimum else "typed_refusal",
            "mode": "finite_dag" if minimum else "symbolic_height",
        },
        "certificate_bytes": cert["cost"]["certificate_bytes"],
    }
    firewall_failures = audit(adapter) if minimum is not None else []
    forbidden = {"full_trace", "source_expr", "heldout_expected_answer"}
    forbidden_present = sorted(forbidden.intersection(cert))
    return {
        "firewall_valid": not firewall_failures and not forbidden_present,
        "firewall_failures": firewall_failures,
        "forbidden_certificate_fields": forbidden_present,
    }


def fixed_iterate_limit(k: int) -> sp.Expr:
    N = sp.Symbol("N", positive=True)
    value: sp.Expr = -N
    for _ in range(k):
        value = sp.exp(value)
    return sp.limit(value, N, sp.oo)


def main() -> None:
    reveal = json.loads((HERE / "HELD_OUT_REVEAL.json").read_text())
    actual_commitment = sha256(canonical_bytes(reveal)).hexdigest()
    if actual_commitment != EXPECTED_COMMITMENT:
        raise SystemExit(
            f"held-out commitment mismatch: {actual_commitment} != {EXPECTED_COMMITMENT}"
        )

    compiler_result = run_corpus(HERE / "HELD_OUT_COMPILER_CORPUS.json")
    audits = {
        row["id"]: independent_audit(row) for row in compiler_result["cases"]
    }
    N = sp.Symbol("N", positive=True)
    mixed = sp.exp(sp.exp(N + 2 * sp.exp(-N)) - sp.exp(N))
    semantic_baselines = {
        "heldout-l1-mixed-nesting": {
            "backend": f"SymPy {sp.__version__}",
            "result": str(sp.limit(mixed, N, sp.oo)),
            "expected": "exp(2)",
            "valid": sp.limit(mixed, N, sp.oo) == sp.exp(2),
        },
        "heldout-l2-fixed-iterate": {
            "backend": f"SymPy {sp.__version__}",
            "result": str(fixed_iterate_limit(7)),
            "expected": "exp(exp(exp(exp(E))))",
            "valid": fixed_iterate_limit(7) == sp.exp(sp.exp(sp.exp(sp.exp(sp.E)))),
            "symbolic_height_credit": False,
        },
        "heldout-l2-symbolic-height": {
            "backend": f"SymPy {sp.__version__}",
            "result": "unsupported by frozen executable baseline",
            "valid_refusal": True,
        },
    }

    symbolic = next(
        row for row in compiler_result["cases"]
        if row["id"] == "heldout-l2-symbolic-height"
    )
    symbolic_cert = symbolic["certificate"]
    typed_refusal_valid = (
        symbolic_cert["status"] == "unsupported"
        and symbolic_cert["minimum_declared_carrier"] is None
        and any(
            item.get("code") == "symbolic-height-not-finite-unrolling"
            for item in symbolic_cert["failures"]
        )
        and symbolic["replay"]["valid"]
    )

    out = {
        "schema": "process-geometry/carrier-heldout-result/v0",
        "freeze": {
            "compiler_commit": "d52289952021f6bf6ee7518a7e79816ff2de3924",
            "commitment_expected": EXPECTED_COMMITMENT,
            "commitment_actual": actual_commitment,
            "commitment_valid": True,
        },
        "compiler_result": compiler_result,
        "independent_audits": audits,
        "semantic_baselines": semantic_baselines,
        "typed_symbolic_height_refusal_valid": typed_refusal_valid,
        "claim_boundary": (
            "The compiler certifies only frozen syntax-directed carrier choice. "
            "The separate SymPy rows execute the two finite readout tasks. "
            "Neither supplies symbolic-height, C3, or C4 construction credit."
        ),
        "acceptance_corrections": {
            "heldout-l1-mixed-nesting": (
                "carrier-decision pass only; compiler semantic-task pass is false; "
                "SymPy supplies the separate exact readout"
            ),
            "heldout-l2-fixed-iterate": (
                "outside-redteam-fixed-height-budget because the frozen maximum is 6; "
                "retain as extrapolation with zero acceptance credit"
            ),
        },
        "disposition": "NARROW",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
