"""Mechanical hygiene for the multi-file pendulum vignette family.

This is a plumbing test, not a mathematical claim.  It protects only the
family-level knowledge contract: one stable entry guide, explicit stage
coverage, independent essay boundaries, and evidence/reconstruction labels.
The mathematical identities remain certified by the pendulum essays themselves.
"""

from __future__ import annotations

import ast
from pathlib import Path


_ROOT = Path(__file__).parent
_REPO = _ROOT.parent
_GUIDE = _REPO / "docs" / "vignettes" / "simple-pendulum.md"
_CLASSICAL_README = _ROOT / "classical" / "README.md"

_PENDULUM_ESSAYS = (
    _ROOT / "classical" / "test_pendulum_process_geometry.py",
    _ROOT / "classical" / "test_pendulum_discovery_layer.py",
    _ROOT / "classical" / "test_pendulum_observer_selection.py",
    _ROOT / "classical" / "test_pendulum_structured_observers.py",
    _ROOT / "classical" / "test_pendulum_observable_quotient_fiber.py",
    _ROOT / "classical" / "test_pendulum_period_history.py",
    _ROOT / "classical" / "test_pendulum_period_contour.py",
    _ROOT / "classical" / "test_pendulum_period_matrix.py",
    _ROOT / "classical" / "test_pendulum_cycle_intersection.py",
)


def _docstring(path: Path) -> str:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    doc = ast.get_docstring(tree, clean=False)
    assert doc is not None, f"pendulum essay has no module docstring: {path}"
    return doc


def test_every_pendulum_proof_step_is_a_self_identifying_mathematical_essay():
    failures: list[str] = []
    for path in _PENDULUM_ESSAYS:
        if not path.exists():
            failures.append(f"missing pendulum essay: {path.name}")
            continue
        doc = _docstring(path)
        if not (
            "Question\n--------" in doc
            or "Problem statement\n-----------------" in doc
        ):
            failures.append(f"{path.name}: missing independent problem/question section")
        for required in ("Primitive data", "Calibration statement", "Proof map"):
            if required not in doc:
                failures.append(f"{path.name}: missing {required!r}")
        if "Boundary" not in doc:
            failures.append(f"{path.name}: missing claim/reconstruction boundary")
        if "References" not in doc:
            failures.append(f"{path.name}: missing references/onward links")
    assert not failures, "pendulum vignette essay hygiene failures: " + "; ".join(failures)


def test_family_guide_names_every_executable_stage_and_evidence_boundary():
    guide = _GUIDE.read_text(encoding="utf-8")

    for path in _PENDULUM_ESSAYS:
        assert path.name in guide, f"family guide omits {path.name}"

    for stage in range(10):
        assert f"**P{stage}**" in guide, f"family guide omits stage P{stage}"

    for required_phrase in (
        "exact symbolic",
        "sampled numerical",
        "Z2",
        "reconstruction",
        "A/M lift canonicalization",
        "Representation-invariant elliptic object",
        "Canonical completion theory",
    ):
        assert required_phrase in guide, f"family guide omits boundary {required_phrase!r}"


def test_classical_directory_exposes_the_family_level_start_here_guide():
    readme = _CLASSICAL_README.read_text(encoding="utf-8")
    assert "docs/vignettes/simple-pendulum.md" in readme
