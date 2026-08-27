from __future__ import annotations

import json
from pathlib import Path

from audit_candidate_certificate import audit


ROOT = Path(__file__).resolve().parent


def test_freeze_is_machine_readable_and_commitment_is_assigned() -> None:
    contract = json.loads((ROOT / "FROZEN_REDTEAM_CONTRACT.json").read_text())
    commitment = json.loads((ROOT / "HELD_OUT_COMMITMENT.json").read_text())
    assert contract["frozen_against"]["issue"] == 142
    assert len(commitment["payload_sha256"]) == 64
    assert "PLACEHOLDER" not in commitment["payload_sha256"]


def test_accepts_minimal_c0_certificate() -> None:
    cert = {
        "selected_carrier": "C0",
        "passed_carriers": ["C0", "C1", "C2", "C3", "C4"],
        "evidence": {"kind": "exact_balance"},
    }
    assert audit(cert) == []


def test_detects_overpromotion() -> None:
    cert = {
        "selected_carrier": "C4",
        "passed_carriers": ["C0", "C4"],
        "smaller_carrier_obstruction": {"C0-C3": "claimed but contradicted"},
        "evidence": {"kind": "effective_algorithm"},
    }
    assert "overpromotion-smaller-carrier-already-passed" in audit(cert)


def test_detects_fixed_height_masquerading_as_symbolic_height() -> None:
    cert = {
        "selected_carrier": "C2",
        "passed_carriers": ["C2"],
        "symbolic_height_credit": True,
        "evidence": {"mode": "fixed_unrolling", "unrolled_height": 64},
    }
    failures = audit(cert)
    assert "fixed-height-masquerades-as-symbolic-height" in failures
    assert "symbolic-height-certificate-contains-unrolling-bound" in failures


def test_detects_embedding_masquerading_as_algorithm() -> None:
    cert = {
        "selected_carrier": "C4",
        "passed_carriers": ["C4"],
        "smaller_carrier_obstruction": {"C0-C3": "opaque"},
        "evidence": {"kind": "embedding"},
    }
    assert "embedding-or-existence-masquerades-as-algorithm" in audit(cert)


def test_detects_certificate_that_stores_full_trace() -> None:
    cert = {
        "selected_carrier": "C2",
        "passed_carriers": ["C2"],
        "evidence": {"kind": "exact_lowering"},
        "full_trace": ["exp", "exp", "log"],
        "compression_claim": True,
        "certificate_bytes": 960,
        "source_plus_full_trace_bytes": 1000,
    }
    failures = audit(cert)
    assert "certificate-stores-forbidden-trace-or-answer" in failures
    assert "certificate-does-not-compress-source-plus-trace" in failures
