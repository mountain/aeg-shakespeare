"""Mechanical coverage for the Mathematical-Core recalibration records.

This test makes the documentation audit fail closed when a new executable essay
is added under ``tests/classical``.  It also validates the evidence vocabulary
and keeps the three cover notions structurally separate.  It certifies audit
coverage only; it makes no mathematical, maturity, or API claim.
"""

from __future__ import annotations

from pathlib import Path


_ROOT = Path(__file__).parents[1]
_CLASSICAL = _ROOT / "tests" / "classical"
_AUDIT = _ROOT / "docs" / "36-classical-reexpression-audit.md"
_MATRIX = _ROOT / "docs" / "66-classical-process-language-calibration.md"
_BEGIN = "<!-- CLASSICAL_CALIBRATION_MATRIX:BEGIN -->"
_END = "<!-- CLASSICAL_CALIBRATION_MATRIX:END -->"
_EVIDENCE_STATES = {"E", "N", "D", "F", "I", "NA", "OPEN"}


def _calibration_matrix():
    text = _MATRIX.read_text(encoding="utf-8")
    assert text.count(_BEGIN) == 1 and text.count(_END) == 1
    body = text.split(_BEGIN, 1)[1].split(_END, 1)[0]
    table_lines = [line for line in body.splitlines() if line.startswith("|")]
    assert len(table_lines) >= 3

    header = tuple(cell.strip() for cell in table_lines[0].strip("|").split("|"))
    assert header == (
        "File",
        "Family",
        "P",
        "H",
        "T",
        "L",
        "Hinf",
        "Ctop",
        "Can",
        "R",
        "Q",
        "Dec",
        "A",
        "B",
        "Next gate",
    )

    rows = []
    for line in table_lines[2:]:
        cells = tuple(cell.strip() for cell in line.strip("|").split("|"))
        assert len(cells) == len(header), line
        assert cells[0].startswith("`test_") and cells[0].endswith(".py`")
        rows.append(dict(zip(header, cells)))
    return rows


def test_every_classical_essay_is_named_by_the_core_recalibration_ledger():
    audit = _AUDIT.read_text(encoding="utf-8")
    essays = sorted(path.name for path in _CLASSICAL.glob("test_*.py"))
    missing = [name for name in essays if f"`{name}`" not in audit]

    assert not missing, (
        "docs/36-classical-reexpression-audit.md must classify every "
        "tests/classical executable essay: " + ", ".join(missing)
    )


def test_process_language_matrix_covers_every_classical_essay_exactly_once():
    essays = sorted(path.name for path in _CLASSICAL.glob("test_*.py"))
    rows = _calibration_matrix()
    matrix_names = [row["File"].strip("`") for row in rows]

    assert len(matrix_names) == len(
        set(matrix_names)
    ), "matrix contains duplicate files"
    assert sorted(matrix_names) == essays


def test_process_language_matrix_uses_only_governed_evidence_states():
    evidence_columns = (
        "P",
        "H",
        "T",
        "L",
        "Hinf",
        "Ctop",
        "Can",
        "R",
        "Q",
        "Dec",
        "A",
        "B",
    )

    for row in _calibration_matrix():
        invalid = {
            column: row[column]
            for column in evidence_columns
            if row[column] not in _EVIDENCE_STATES
        }
        assert not invalid, f"{row['File']} has invalid evidence states: {invalid}"
        assert row["Next gate"]


def test_history_topological_and_analytic_covers_remain_separate_axes():
    matrix = {row["File"].strip("`"): row for row in _calibration_matrix()}
    oscillator = matrix["test_even_power_oscillator_process_calibration.py"]

    assert oscillator["Hinf"] == "OPEN"
    assert oscillator["Ctop"] == "E"
    assert oscillator["Can"] == "E"

    calibration = _MATRIX.read_text(encoding="utf-8")
    required_separations = (
        "Raw-history unfolding is an open transversal",
        "complex energy carriers",
        "real history-cover",
        "Generic raw-history unfolding",
    )
    missing = [term for term in required_separations if term not in calibration]
    assert not missing, "cover-separation record is missing: " + ", ".join(missing)


def test_recalibration_ledger_names_its_governing_contracts_and_non_promotions():
    audit = _AUDIT.read_text(encoding="utf-8") + _MATRIX.read_text(encoding="utf-8")
    required = (
        "MATHEMATICAL_CORE.md",
        "ENGINEERING_ARCHITECTURE.md",
        "Theory Map",
        "API pressure",
        "Kill conditions",
    )

    missing = [term for term in required if term not in audit]
    assert not missing, "recalibration ledger is missing: " + ", ".join(missing)
