"""Source-level dependency hygiene after semantic core decomposition."""

import ast
from pathlib import Path


_SRC_ROOT = Path(__file__).parents[1] / "src" / "aeg_shakespeare"
_ALLOWED_COMPATIBILITY = {
    _SRC_ROOT / "core.py",
    _SRC_ROOT / "_legacy_api.py",
}
_SEMANTIC_CORE_NAMES = {
    "ProcessWord",
    "interpret_history",
    "ProcessSystem",
    "SearchBudget",
}


def _imported_names(node: ast.ImportFrom) -> set[str]:
    return {alias.name for alias in node.names}


def test_source_does_not_reintroduce_semantic_dependencies_on_core_or_frame_shims():
    offenders: list[str] = []
    for path in sorted(_SRC_ROOT.rglob("*.py")):
        if path in _ALLOWED_COMPATIBILITY:
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.ImportFrom):
                continue
            names = _imported_names(node)
            if node.module == "core" and names & _SEMANTIC_CORE_NAMES:
                offenders.append(
                    f"{path.relative_to(_SRC_ROOT)} imports {sorted(names & _SEMANTIC_CORE_NAMES)} from core"
                )
            if node.module == "frame" and "ProcessFrame" in names:
                offenders.append(
                    f"{path.relative_to(_SRC_ROOT)} imports ProcessFrame from legacy frame shim"
                )

    assert not offenders, (
        "semantic source dependencies must point to process/presentation owners, "
        f"not compatibility shims: {offenders}"
    )


def test_core_backend_import_is_limited_to_homogeneous_monomials_outside_compatibility():
    unexpected: list[str] = []
    for path in sorted(_SRC_ROOT.rglob("*.py")):
        if path in _ALLOWED_COMPATIBILITY:
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.ImportFrom) or node.module != "core":
                continue
            extra = _imported_names(node) - {"homogeneous_monomials"}
            if extra:
                unexpected.append(
                    f"{path.relative_to(_SRC_ROOT)} imports {sorted(extra)} from core"
                )

    assert not unexpected, (
        "core.py may remain a backend source only for homogeneous_monomials: "
        f"{unexpected}"
    )
