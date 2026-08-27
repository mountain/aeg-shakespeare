from __future__ import annotations

from pathlib import Path
import sys


WORKSTREAM = Path(__file__).resolve().parents[1] / "workstreams" / "am_weight_compiler"
sys.path.insert(0, str(WORKSTREAM))

from am_weight_compiler.corpus import run_corpus  # noqa: E402


def test_am_weight_compiler_public_gate() -> None:
    result = run_corpus(
        WORKSTREAM / "PUBLIC_CORPUS.json",
        WORKSTREAM / "FROZEN_CONTRACT.json",
    )
    assert result["passed"] is True
    assert result["pass_count"] == result["case_count"] == 12
