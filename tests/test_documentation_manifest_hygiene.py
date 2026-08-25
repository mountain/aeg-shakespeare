"""Mechanical hygiene for documentation and Sonnet navigation.

The filename numbers are historical chronology markers, not unique theory IDs.
This test preserves existing citation paths, prevents new collisions, and makes
the two repository entry ledgers fail closed when a new document or Sonnet is
added without an index entry. It makes no mathematical or maturity claim.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re


_REPO = Path(__file__).parents[1]
_DOCS = _REPO / "docs"
_DOCS_INDEX = _DOCS / "README.md"
_SONNET = _REPO / "sonnet"
_SONNET_INDEX = _SONNET / "README.md"

_LEGACY_DUPLICATE_DOC_PREFIXES = {
    "27": {
        "27-finite-family-calibration-map.md",
        "27-galilean-central-residual.md",
    },
    "28": {
        "28-do-not-extend-this-api-yet.md",
        "28-magnetic-translation-central-residual.md",
    },
    "35": {
        "35-canonical-observer-vertical-slice.md",
        "35-killer-calibrations-and-dominance-target.md",
    },
    "36": {
        "36-classical-reexpression-audit.md",
        "36-kdv-soliton-rewrite-confluence.md",
    },
    "37": {
        "37-canonical-observer-claim-ledger.md",
        "37-kdv-tau-rewrite-cross-presentation.md",
    },
    "38": {
        "38-canonicalization-mainline.md",
        "38-resistor-network-presentation-morphism.md",
    },
    "39": {
        "39-braid-markov-presentation-morphism.md",
        "39-canonicalization-mechanism-closure.md",
    },
    "54": {
        "54-pendulum-canonical-history-cost.md",
        "54-pendulum-elliptic-group-rank-lowering.md",
    },
    "55": {
        "55-cross-problem-canonical-history-correspondence.md",
        "55-pendulum-lifted-clock-global-quotient.md",
    },
}


def test_every_top_level_document_is_named_by_the_documentation_map():
    index = _DOCS_INDEX.read_text(encoding="utf-8")
    expected = sorted(
        path.name
        for path in _DOCS.iterdir()
        if path.is_file()
        and path.name != "README.md"
        and (path.suffix == ".md" or path.name.endswith(".py.txt"))
    )
    missing = [name for name in expected if f"`{name}`" not in index]
    assert not missing, (
        "docs/README.md must name every top-level documentation artifact: "
        + ", ".join(missing)
    )


def test_every_sonnet_study_is_named_by_the_study_ledger():
    index = _SONNET_INDEX.read_text(encoding="utf-8")
    studies = sorted(
        path.name
        for path in _SONNET.iterdir()
        if path.is_dir() and (path / "README.md").is_file()
    )
    missing = [name for name in studies if f"`{name}/`" not in index]
    assert not missing, (
        "sonnet/README.md must name every study directory with a README: "
        + ", ".join(missing)
    )


def test_no_new_top_level_document_prefix_collision_is_introduced():
    grouped: dict[str, set[str]] = defaultdict(set)
    for path in _DOCS.iterdir():
        if not path.is_file():
            continue
        match = re.match(r"(\d+)-", path.name)
        if match:
            grouped[match.group(1)].add(path.name)

    duplicates = {key: names for key, names in grouped.items() if len(names) > 1}
    assert duplicates == _LEGACY_DUPLICATE_DOC_PREFIXES, (
        "numeric prefixes are frozen historical chronology markers; "
        "do not add or silently remove collisions without an explicit migration: "
        f"{duplicates}"
    )
