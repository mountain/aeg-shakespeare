# Quickstart examples

These files are intentionally small, runnable entry points into the semantic public API. They are not substitutes for the complete mathematical essays in `tests/classical/` and `tests/research/`.

All public examples use the canonical namespaced API:

```text
process_geometry.process
process_geometry.presentation
process_geometry.discovery
process_geometry.analysis
```

The deprecated `aeg_shakespeare` namespace is tested only as a compatibility alias and should not appear in new examples.

- `quickstart.py` — literal process history, explicit presentation rewriting, and A/M (Addition/Multiplication) analysis.
- `constraint_quickstart.py` — exact equality modulo an algebraic presentation constraint ideal.
- `grammar_quickstart.py` — a local process realization feeding generated-grammar presentation discovery.

For mathematical lineage and citations, follow the corresponding docs and tests rather than treating an example script as a proof.
