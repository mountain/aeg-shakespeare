# Quickstart examples

These files are intentionally small, runnable entry points into the semantic public API. They are not substitutes for the complete mathematical essays in `tests/classical/` and `tests/research/`.

All examples use the namespaced API rather than legacy root-level imports:

```text
aeg_shakespeare.process
aeg_shakespeare.presentation
aeg_shakespeare.discovery
aeg_shakespeare.analysis
```

- `quickstart.py` — literal process history, explicit presentation rewriting, and A/M (Addition/Multiplication) analysis.
- `constraint_quickstart.py` — exact equality modulo an algebraic presentation constraint ideal.
- `grammar_quickstart.py` — a local process realization feeding generated-grammar presentation discovery.

For mathematical lineage and citations, follow the corresponding docs and tests rather than treating an example script as a proof.
