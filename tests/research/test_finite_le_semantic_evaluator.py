"""Default-CI bridge for issue #144's research-local semantic evaluator."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
WORKSTREAM = ROOT / "workstreams" / "finite_le_semantics"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=WORKSTREAM,
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_finite_le_semantic_suite_and_manifest_pass() -> None:
    suite = _run("-m", "pytest", "-q")
    manifest = _run("verify_manifest.py")
    assert "[100%]" in suite.stdout
    assert "manifest ok" in manifest.stdout


def test_public_controls_are_compiler_results_not_limit_oracles() -> None:
    source = (WORKSTREAM / "finite_le_semantics" / "evaluator.py").read_text()
    replay = (WORKSTREAM / "finite_le_semantics" / "replay.py").read_text()
    assert ".limit(" not in source + replay
    result = _run("run_corpus.py", "PUBLIC_CORPUS.json").stdout
    assert '"limit": "exp(2)"' in result
    assert '"limit": "1/3"' in result
    assert '"q": 6' in result
