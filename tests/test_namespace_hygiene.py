"""Repository-internal import hygiene for the semantic public API.

The package keeps a lazy 0.0.x root compatibility bridge for external users,
but Shakespeare's own tests must not depend on that bridge.  Otherwise facade
mistakes can be hidden indefinitely by compatibility behavior.
"""

from pathlib import Path


_ALLOWED_LEGACY_ROOT_IMPORT = Path(__file__).with_name("test_public_api_smoke.py")


def test_internal_tests_do_not_use_legacy_root_symbol_imports():
    tests_root = Path(__file__).parent
    offenders = []
    for path in sorted(tests_root.rglob("*.py")):
        if path == _ALLOWED_LEGACY_ROOT_IMPORT:
            continue
        text = path.read_text(encoding="utf-8")
        if "from aeg_shakespeare import" in text:
            offenders.append(str(path.relative_to(tests_root.parent)))

    assert not offenders, (
        "internal tests must use process/presentation/discovery/analysis "
        f"namespaces instead of the legacy root bridge: {offenders}"
    )
