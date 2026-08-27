from __future__ import annotations

import json
from pathlib import Path
import sys

from carrier_compiler.corpus import run_corpus


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python run_corpus.py CORPUS.json")
    print(json.dumps(run_corpus(Path(sys.argv[1])), indent=2, sort_keys=True))
