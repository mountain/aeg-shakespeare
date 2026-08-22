# Semantic public API refactor: Phase A.2

**Status:** repository-internal import migration; no implementation relocation and no new mathematics.

## 1. Goal

Phase A.1 introduced the semantic public hierarchy

```text
Process -> Presentation -> Discovery -> Analysis
```

and retained a lazy legacy root-import bridge for external `0.0.x` users. Phase
A.2 makes the repository itself stop depending on that bridge.

The reason is architectural: if Shakespeare's own tests continue to import
symbols from the root, a broken or incomplete facade can remain invisible
because compatibility re-exports silently repair it.

## 2. Migration rule

Internal tests now import according to semantic ownership:

- process histories/families/local generators from `aeg_shakespeare.process.*`;
- rewriting, constraints, grammars, relations, construction, and cost/search
  from `aeg_shakespeare.presentation.*`;
- invariant/observer/quotient/language search from `aeg_shakespeare.discovery`;
- A/M, algebraic quotient, and Abelian/global machinery from
  `aeg_shakespeare.analysis.*`.

Calibration problems such as pendulum, oscillator, Galilean mechanics, and
magnetic translations do not receive public namespaces. Their tests compose the
shared semantic layers directly.

## 3. Backend distinction

Not every callable implementation helper is promoted into the public ontology.
For example, the Krylov calibration and fixed-degree monomial helper remain
explicit backend/internal imports in the benchmark test. This is intentional:

```text
callable implementation surface != public mathematical ontology
```

## 4. Hygiene gate

`tests/test_namespace_hygiene.py` parses every Python test with `ast` and rejects
any direct

```python
from aeg_shakespeare import ...
```

statement, except the dedicated public-API smoke test that intentionally checks
the temporary compatibility bridge.

The gate is syntax-aware rather than string-based, so comments/docstrings do not
produce false positives.

## 5. Completion criterion

Phase A.2 is complete only when:

1. the hygiene gate reports no internal dependency on legacy root symbols;
2. the full historical classical/research suite remains green;
3. the semantic facades require no new convenience exports merely to make old
   tests pass;
4. quickstarts and isolated-wheel smoke remain green;
5. `_legacy_api.py` remains only as an external migration bridge.

Physical relocation of implementation files is still deferred. The next
refactor decision should be based on the now-clean import graph rather than on
root-level compatibility pressure.
