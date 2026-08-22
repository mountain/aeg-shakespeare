"""Repository-internal import hygiene for the semantic public API.

The package keeps a lazy 0.0.x root compatibility bridge for external users,
but Shakespeare's own tests must not depend on that bridge. Otherwise facade
mistakes can be hidden indefinitely by compatibility behavior.
"""

import ast
from pathlib import Path


_ALLOWED_LEGACY_ROOT_IMPORT = Path(__file__).with_name("test_public_api_smoke.py")


def _uses_legacy_root_symbol_import(path: Path) -> bool:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return any(
        isinstance(node, ast.ImportFrom) and node.module == "aeg_shakespeare"
        for node in ast.walk(tree)
    )


def test_internal_tests_do_not_use_legacy_root_symbol_imports():
    tests_root = Path(__file__).parent
    offenders = []
    for path in sorted(tests_root.rglob("*.py")):
        if path == _ALLOWED_LEGACY_ROOT_IMPORT:
            continue
        if _uses_legacy_root_symbol_import(path):
            offenders.append(str(path.relative_to(tests_root.parent)))

    assert not offenders, (
        "internal tests must use process/presentation/discovery/analysis "
        f"namespaces instead of the legacy root bridge: {offenders}"
    )
