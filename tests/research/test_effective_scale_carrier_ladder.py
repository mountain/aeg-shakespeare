"""CI bridge for the research-local effective carrier gate (issue #142)."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
WORKSTREAM = ROOT / "workstreams" / "carrier_ladder"
COMPILER = WORKSTREAM / "compiler"
REDTEAM = WORKSTREAM / "redteam"


def _run(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_frozen_compiler_and_reveal_suites_pass() -> None:
    compiler = _run("-m", "pytest", "-q", cwd=COMPILER)
    redteam = _run("-m", "pytest", "-q", cwd=REDTEAM)
    assert "[100%]" in compiler.stdout
    assert "[100%]" in redteam.stdout


def test_manifests_and_reveal_runner_reproduce_the_narrow_result() -> None:
    assert "manifest ok" in _run("verify_manifest.py", cwd=COMPILER).stdout

    post_reveal = subprocess.run(
        ["sha256sum", "-c", "POST_REVEAL_MANIFEST.sha256"],
        cwd=REDTEAM,
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert "FAILED" not in post_reveal.stdout

    replay = json.loads(_run("run_heldout_and_audit.py", cwd=REDTEAM).stdout)
    assert replay["freeze"]["commitment_valid"] is True
    assert replay["typed_symbolic_height_refusal_valid"] is True
    assert replay["disposition"] == "NARROW"
    assert "carrier-decision pass only" in replay["acceptance_corrections"]["heldout-l1-mixed-nesting"]
    assert "outside-redteam-fixed-height-budget" in replay["acceptance_corrections"]["heldout-l2-fixed-iterate"]
