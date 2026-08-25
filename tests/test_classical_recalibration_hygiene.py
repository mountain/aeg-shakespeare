"""Mechanical coverage for the Mathematical-Core recalibration ledger.

This test makes the documentation audit fail closed when a new executable essay
is added under ``tests/classical``. It certifies file coverage and required
governance links only; it makes no mathematical, maturity, or API claim.
"""

from __future__ import annotations

from pathlib import Path


_ROOT = Path(__file__).parents[1]
_CLASSICAL = _ROOT / "tests" / "classical"
_AUDIT = _ROOT / "docs" / "36-classical-reexpression-audit.md"


def test_every_classical_essay_is_named_by_the_core_recalibration_ledger():
    audit = _AUDIT.read_text(encoding="utf-8")
    essays = sorted(path.name for path in _CLASSICAL.glob("test_*.py"))
    missing = [name for name in essays if f"`{name}`" not in audit]

    assert not missing, (
        "docs/36-classical-reexpression-audit.md must classify every "
        "tests/classical executable essay: " + ", ".join(missing)
    )


def test_recalibration_ledger_names_its_governing_contracts_and_non_promotions():
    audit = _AUDIT.read_text(encoding="utf-8")
    required = (
        "MATHEMATICAL_CORE.md",
        "ENGINEERING_ARCHITECTURE.md",
        "Theory Map",
        "API pressure",
        "Kill conditions",
    )

    missing = [term for term in required if term not in audit]
    assert not missing, "recalibration ledger is missing: " + ", ".join(missing)
