from __future__ import annotations

import json
from pathlib import Path
import sys

from finite_le_semantics import run_corpus


if __name__ == "__main__":
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "PUBLIC_CORPUS.json")
    print(json.dumps(run_corpus(path), indent=2, sort_keys=True))
