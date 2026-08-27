from __future__ import annotations

from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).parent
MANIFEST = ROOT / "MANIFEST.sha256"


def verify() -> list[str]:
    failures: list[str] = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        actual = sha256((ROOT / relative).read_bytes()).hexdigest()
        if actual != expected:
            failures.append(relative)
    return failures


if __name__ == "__main__":
    failures = verify()
    if failures:
        raise SystemExit("manifest mismatch: " + ", ".join(failures))
    print("manifest ok")
