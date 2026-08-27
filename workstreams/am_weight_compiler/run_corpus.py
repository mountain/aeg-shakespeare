from __future__ import annotations

import json
from pathlib import Path

from am_weight_compiler.corpus import run_corpus


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    result = run_corpus(root / "PUBLIC_CORPUS.json", root / "FROZEN_CONTRACT.json")
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["passed"] else 1)
