"""Repository-wide spelling hygiene for Huffman coding terminology."""

from pathlib import Path


_ROOT = Path(__file__).parents[1]
_MISSPELLING = ("Hauf" + "fman").casefold()
_TEXT_SUFFIXES = {".cff", ".md", ".py", ".toml", ".txt", ".yaml", ".yml"}
_SCAN_ROOTS = (
    _ROOT / ".github",
    _ROOT / "docs",
    _ROOT / "sonnet",
    _ROOT / "src",
    _ROOT / "tests",
)
_ROOT_TEXT_FILES = (_ROOT / "CHANGELOG.md", _ROOT / "README.md")


def _text_paths():
    yield from _ROOT_TEXT_FILES
    for root in _SCAN_ROOTS:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in _TEXT_SUFFIXES:
                yield path


def test_huffman_spelling_is_consistent_in_paths_and_text():
    failures = []
    for path in _text_paths():
        relative_path = path.relative_to(_ROOT).as_posix()
        if _MISSPELLING in relative_path.casefold():
            failures.append(f"path: {relative_path}")

        text = path.read_text(encoding="utf-8")
        if _MISSPELLING in text.casefold():
            failures.append(f"text: {relative_path}")

    assert not failures, "Nonstandard Huffman spelling found:\n" + "\n".join(failures)
