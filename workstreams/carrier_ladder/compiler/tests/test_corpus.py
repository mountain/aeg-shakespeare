from pathlib import Path

from carrier_compiler.corpus import run_corpus


def test_frozen_corpus_matches_expected_statuses():
    root = Path(__file__).parents[1]
    result = run_corpus(root / "FROZEN_CORPUS.json")
    by_id = {row["id"]: row for row in result["cases"]}
    assert by_id["l0-bessel-local-germ"]["certificate"]["minimum_declared_carrier"] == "C0-rational-newton"
    assert by_id["l1-finite-generalized-polynomial"]["certificate"]["minimum_declared_carrier"] == "C1f-finite-generalized-polynomial"
    assert by_id["l1-finite-nested-exp-log"]["certificate"]["minimum_declared_carrier"] == "C2-finite-height-le"
    assert by_id["l2-symbolic-exp-height"]["certificate"]["status"] == "unsupported"
    assert by_id["l2-abel-without-normalization"]["certificate"]["status"] == "unsupported"
    assert all(row["replay"]["valid"] for row in by_id.values())


def test_public_sanity_identity_and_replay():
    import hashlib
    import json

    root = Path(__file__).parents[1]
    preimage_bytes = (root / "PUBLIC_SANITY_CASE.json").read_bytes()
    commitment = json.loads((root / "PUBLIC_SANITY_IDENTITY.json").read_text())
    assert hashlib.sha256(preimage_bytes).hexdigest() == commitment["sha256"]
    result = run_corpus(root / "PUBLIC_SANITY_CASE.json")
    row = result["cases"][0]
    recorded = json.loads((root / "PUBLIC_SANITY_RESULT.json").read_text())
    assert row["certificate"]["minimum_declared_carrier"] == "C2-finite-height-le"
    assert row["certificate"]["construction_height"] == 4
    assert row["certificate"]["certificate_digest"] == recorded["certificate_digest"]
    assert row["certificate"]["cost"]["certificate_bytes"] == recorded["certificate_bytes"]
    assert row["certificate"]["cost"]["compilation_steps"] == recorded["compilation_steps"]
    assert row["replay"]["steps"] == recorded["replay_steps"]
    assert row["replay"]["valid"]
