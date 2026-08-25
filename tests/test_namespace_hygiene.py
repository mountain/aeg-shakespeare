"""Namespace ownership and repository-internal import hygiene.

`process_geometry` is the single implementation owner. The historical
`aeg_shakespeare` package may depend on it as a compatibility alias, but the
canonical source tree and public examples must never depend in the reverse
direction.
"""

import ast
from pathlib import Path


_REPO_ROOT = Path(__file__).parents[1]
_CANONICAL_SRC = _REPO_ROOT / "src" / "process_geometry"
_LEGACY_SRC = _REPO_ROOT / "src" / "aeg_shakespeare"
_EXAMPLES_ROOT = _REPO_ROOT / "examples"
_ALLOWED_LEGACY_TEST = Path(__file__).with_name("test_public_api_smoke.py")
_EXPERIMENTAL_COMPATIBILITY_SHIMS = {
    _CANONICAL_SRC / "presentation" / "canonicalization.py",
    _CANONICAL_SRC / "analysis" / "connection.py",
    _CANONICAL_SRC / "analysis" / "decomposition.py",
}


def _imports_legacy_namespace(path: Path) -> bool:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any(
                alias.name == "aeg_shakespeare"
                or alias.name.startswith("aeg_shakespeare.")
                for alias in node.names
            ):
                return True
        if isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if module == "aeg_shakespeare" or module.startswith("aeg_shakespeare."):
                return True
    return False


def _uses_legacy_root_symbol_import(path: Path) -> bool:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return any(
        isinstance(node, ast.ImportFrom) and node.module == "aeg_shakespeare"
        for node in ast.walk(tree)
    )


def test_canonical_source_never_depends_on_legacy_namespace():
    offenders = [
        str(path.relative_to(_REPO_ROOT))
        for path in sorted(_CANONICAL_SRC.rglob("*.py"))
        if _imports_legacy_namespace(path)
    ]
    assert not offenders, (
        "canonical source must not depend on deprecated aeg_shakespeare namespace: "
        f"{offenders}"
    )


def test_public_examples_use_canonical_namespace():
    offenders = [
        str(path.relative_to(_REPO_ROOT))
        for path in sorted(_EXAMPLES_ROOT.glob("*.py"))
        if _imports_legacy_namespace(path)
    ]
    assert not offenders, (
        "public examples must demonstrate process_geometry, not the compatibility alias: "
        f"{offenders}"
    )


def test_legacy_package_contains_only_the_alias_owner():
    python_files = sorted(
        str(path.relative_to(_LEGACY_SRC)) for path in _LEGACY_SRC.rglob("*.py")
    )
    assert python_files == ["__init__.py"], (
        "aeg_shakespeare must remain a thin alias, not regrow a second implementation tree: "
        f"{python_files}"
    )


def test_internal_tests_do_not_use_legacy_root_symbol_imports():
    """Keep the earlier flat-root bridge out of ordinary repository tests.

    Existing deep `aeg_shakespeare.*` imports remain valid compatibility coverage
    during the staged 0.0.4 migration, but no test except the explicit smoke test
    may depend on the even older flat-root symbol facade.
    """

    tests_root = Path(__file__).parent
    offenders = []
    for path in sorted(tests_root.rglob("*.py")):
        if path == _ALLOWED_LEGACY_TEST:
            continue
        if _uses_legacy_root_symbol_import(path):
            offenders.append(str(path.relative_to(_REPO_ROOT)))

    assert not offenders, (
        "internal tests must use namespaced APIs instead of the legacy flat-root bridge: "
        f"{offenders}"
    )


def test_stable_source_does_not_depend_on_experimental_ontology():
    """Experimental may depend inward; stable layers must not depend outward.

    The three listed modules are one-way 0.0.x compatibility paths.  They own
    no implementation and may disappear after the migration window.
    """

    offenders: list[str] = []
    experimental_root = _CANONICAL_SRC / "experimental"
    for path in sorted(_CANONICAL_SRC.rglob("*.py")):
        if path.is_relative_to(experimental_root):
            continue
        if path in _EXPERIMENTAL_COMPATIBILITY_SHIMS:
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.ImportFrom):
                continue
            module = node.module or ""
            if (
                module == "experimental"
                or module.startswith("experimental.")
                or module == "process_geometry.experimental"
                or module.startswith("process_geometry.experimental.")
            ):
                offenders.append(str(path.relative_to(_REPO_ROOT)))

    assert not offenders, (
        "stable source must not depend on experimental ontology: "
        f"{offenders}"
    )
