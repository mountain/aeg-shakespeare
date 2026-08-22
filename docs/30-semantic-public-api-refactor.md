# Semantic public API refactor: Phase A.1

**Status:** public-ontology refactor; implementation files deliberately remain in place.

## 1. Problem

The early `0.0.x` package root accumulated every successful research abstraction as
a direct re-export.  This made the declared public API look like one flat list
containing process histories, finite families, rewriting, task quotients,
construction proposals, generated grammars, relation kernels, observer search,
A/M calculus, hyperelliptic profiles, Abelian periods, and calibration backends.

The mathematical work had not actually collapsed into one layer; the package
root had simply stopped representing the conceptual hierarchy.

## 2. New public ontology

The declared root surface is now the four-stage pipeline

```text
Process  ->  Presentation  ->  Discovery  ->  Analysis
```

implemented as

```text
aeg_shakespeare.process
aeg_shakespeare.presentation
aeg_shakespeare.discovery
aeg_shakespeare.analysis
```

The root `__all__` contains only those namespaces plus `__version__`.

### Process

What the process is:

- literal history;
- finite parameterized families;
- scalar responses and family actions;
- additive process cocycles;
- local/infinitesimal realizations.

### Presentation

How process information is finitely objectified and compared:

- rewriting and task signatures;
- history geometry;
- construction histories;
- algebraic constraints;
- generated grammars;
- exact relations/decompositions;
- budgets, costs, and Pareto search.

### Discovery

Algorithms that search alternative presentations:

- invariant/observer proposals;
- quotient selection;
- coefficient-language experiments.

### Analysis

Mathematical languages supported by successful presentations:

- process-function modules;
- A/M calculus;
- algebraic quotient profiles;
- Abelian integrals, cycles, periods, and normalized history quotients.

## 3. Why facade packages come before file movement

Phase A.1 changes only the public semantic facade. Existing implementation files
such as `families.py`, `central.py`, `grammar.py`, `relations.py`, and the
`function_theory/` package remain in place.

This separation is deliberate. Moving thousands of lines while simultaneously
changing the public ontology would make review ambiguous: an import failure could
come from architecture, file relocation, or both.  The facade packages let CI
validate the new conceptual shape first.

A later physical-consolidation phase may move implementation files under the
semantic packages once the namespace design has survived additional vignettes.

## 4. Root contraction and compatibility

Legacy research-preview imports such as

```python
from aeg_shakespeare import ProcessWord
```

remain available lazily through a private compatibility module during the
`0.0.x` transition. Access emits `DeprecationWarning` and the legacy names do not
appear in the declared root `__all__` or `dir(aeg_shakespeare)` surface.

New examples and new public-API tests use semantic imports instead:

```python
from aeg_shakespeare.process.history import ProcessWord
from aeg_shakespeare.presentation.grammar import discover_generated_presentation
from aeg_shakespeare.analysis.am import AMFunctionTheory
```

This keeps existing research tests operational while the internal test suite is
migrated in a separate mechanical pass.

## 5. Why discovery is not physically refactored in this phase

`discovery/` already exists as a package and has useful internal modules:
`polynomial`, `structured`, `selection`, and `coefficient_extension`.

Its `__init__` still re-exports many symbols. Phase A.1 intentionally leaves that
implementation surface unchanged. The important immediate correction is that
discovery is now a *namespace in the four-stage ontology*, rather than a group
of symbols flattened beside process and analysis objects at package root.

A later cleanup can narrow `discovery.__init__` without coupling that work to the
root migration.

## 6. Freeze criterion

Phase A.1 is acceptable only if:

1. the root public contract is exactly the four namespaces plus version;
2. the three public quickstarts run using namespaced imports;
3. representative process, presentation, discovery, and analysis imports work
   from an installed wheel outside the source tree;
4. the full historical test suite still passes through the temporary lazy
   compatibility bridge;
5. no mathematical implementation behavior changes.

The next API-refactor pass should migrate repository-internal tests away from the
legacy root bridge. Only after that should physical source-file relocation be
considered.
