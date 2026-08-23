"""Mechanical hygiene for the new canonical-observer mathematical essays.

This is a plumbing test, not a mathematical vignette.  It enforces only the
parts of the repository literate-programming policy that can be checked
mechanically; mathematical correctness remains the responsibility of each
essay's executable assertions and cited argument.
"""

from __future__ import annotations

import ast
from pathlib import Path
import re


_ROOT = Path(__file__).parent
_ESSAYS = (
    _ROOT / "classical" / "test_restricted_riccati_canonical_observer.py",
    _ROOT / "classical" / "test_riccati_canonical_horizontal_lift.py",
    _ROOT / "classical" / "test_coupled_scalar_canonical_observer.py",
    _ROOT / "classical" / "test_coupled_diagonal_canonical_horizontal_lift.py",
    _ROOT / "classical" / "test_restricted_kepler_canonical_decomposition.py",
    _ROOT / "classical" / "test_kepler_radial_canonical_horizontal_lift.py",
    _ROOT / "classical" / "test_am_process_direction.py",
    _ROOT / "research" / "test_lonely_runner_canonical_observer_decomposition.py",
    _ROOT / "research" / "test_lonely_runner_minimal_completion_residuals.py",
    _ROOT / "research" / "test_lonely_runner_residual_objectification.py",
    _ROOT / "research" / "test_lonely_runner_persistent_dag_increment.py",
    _ROOT / "research" / "test_lonely_runner_refinement_aware_huffman.py",
    _ROOT / "research" / "test_lonely_runner_activation_geometry.py",
    _ROOT / "research" / "test_lonely_runner_controlled_interleaving.py",
    _ROOT / "research" / "test_lonely_runner_center4_constraint_cells.py",
    _ROOT / "research" / "test_lonely_runner_center4_semantic_redteam.py",
    _ROOT / "research" / "test_lonely_runner_center4_minimal_completion.py",
    _ROOT / "research" / "test_lonely_runner_center4_persistent_update.py",
    _ROOT / "research" / "test_lonely_runner_infinite_contact_tail_closure.py",
)
_REQUIRED_SECTIONS = (
    "Question\n--------",
    "Primitive data\n--------------",
    "Classical lineage\n-----------------",
    "Shakespeare reconstruction\n---------------------------",
    "Calibration statement\n---------------------",
    "Proof map\n---------",
    "Boundary\n--------",
    "References\n----------",
)
_CITATION_KEY = re.compile(r"\[([A-Z][A-Za-z0-9.-]*-\d{4}|DLMF-[0-9.]+)\]")
_REFERENCE_ENTRY = re.compile(
    r"^\[([A-Z][A-Za-z0-9.-]*-\d{4}|DLMF-[0-9.]+)\]\s+",
    re.MULTILINE,
)
_PROOF_TEST = re.compile(r"``(test_[A-Za-z0-9_]+)``")


def _module(path: Path) -> tuple[ast.Module, str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    doc = ast.get_docstring(tree, clean=False)
    assert doc is not None, f"mathematical essay has no module docstring: {path}"
    return tree, doc


def test_new_mathematical_essays_follow_the_repository_template():
    failures: list[str] = []
    for path in _ESSAYS:
        _, doc = _module(path)
        for section in _REQUIRED_SECTIONS:
            if section not in doc:
                failures.append(f"{path.name}: missing {section.splitlines()[0]!r}")
    assert not failures, "incomplete executable mathematical essays: " + "; ".join(failures)


def test_every_citation_key_resolves_to_a_full_reference_entry():
    failures: list[str] = []
    for path in _ESSAYS:
        _, doc = _module(path)
        body, references = doc.split("References\n----------", 1)
        cited = set(_CITATION_KEY.findall(body))
        entries = set(_REFERENCE_ENTRY.findall(references))
        missing = sorted(cited - entries)
        if missing:
            failures.append(f"{path.name}: unresolved citation keys {missing}")
        if not entries:
            failures.append(f"{path.name}: empty References section")

        chunks = re.split(r"(?m)^\[(?=[A-Z])", references)
        for chunk in chunks:
            if not chunk.strip():
                continue
            if not any(
                locator in chunk
                for locator in ("DOI", "https://", "ISBN", "Chapter", "pp.", "§")
            ):
                failures.append(
                    f"{path.name}: reference entry lacks a useful locator: {chunk.splitlines()[0]!r}"
                )
    assert not failures, "reference hygiene failures: " + "; ".join(failures)


def test_proof_map_names_real_executable_checks():
    failures: list[str] = []
    for path in _ESSAYS:
        tree, doc = _module(path)
        proof_text = doc.split("Proof map\n---------", 1)[1].split("Boundary\n--------", 1)[0]
        named = set(_PROOF_TEST.findall(proof_text))
        actual = {
            node.name
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name.startswith("test_")
        }
        if not named:
            failures.append(f"{path.name}: Proof map names no test functions")
        missing = sorted(named - actual)
        untracked = sorted(actual - named)
        if missing:
            failures.append(f"{path.name}: Proof map names missing tests {missing}")
        if untracked:
            failures.append(f"{path.name}: executable tests absent from Proof map {untracked}")
    assert not failures, "proof-map hygiene failures: " + "; ".join(failures)
