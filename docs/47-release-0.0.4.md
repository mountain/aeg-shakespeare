# Release 0.0.4 — Canonical `process_geometry` namespace

**Status:** release contract for the first Process Geometry release whose canonical Python import namespace matches the distribution identity.

## 1. Release purpose

Version `0.0.4` completes the second stage of the project-identity migration:

```text
PyPI distribution:     process-geometry
GitHub repository:     mountain/process-geometry
Python import package: process_geometry
```

Version `0.0.3` deliberately changed the distribution identity first while retaining `aeg_shakespeare` as the canonical import package. Version `0.0.4` makes `process_geometry` the single implementation owner.

## 2. Single-owner rule

There is exactly one implementation tree:

```text
src/process_geometry/
```

The historical package

```text
src/aeg_shakespeare/
```

is a compatibility alias only. It must not contain a forked copy of implementation modules.

The compatibility layer aliases the canonical module tree so deep imports preserve object identity. In particular,

```python
from process_geometry.process.history import ProcessWord as NewProcessWord
from aeg_shakespeare.process.history import ProcessWord as OldProcessWord

assert NewProcessWord is OldProcessWord
```

must hold.

This is stronger than source-level similarity: the old and new import paths must denote the same Python objects.

## 3. Canonical public API

New code should import:

```python
import process_geometry as pg

from process_geometry.process.history import ProcessWord
from process_geometry.presentation.morphism import PresentationMorphism
from process_geometry.discovery import discover_polynomial_invariants
from process_geometry.analysis.am import AMFunctionTheory
```

The semantic public pipeline remains unchanged:

```text
Process -> Presentation -> Discovery -> Analysis
```

This release is a namespace migration, not a theory/API promotion event.

## 4. Compatibility boundary

`aeg_shakespeare` remains importable for a transition period and emits `DeprecationWarning` on import. Its purpose is to support migration of code written against `0.0.1`–`0.0.3`.

The alias is not a second public design surface. New documentation, examples, tests, and implementation code must use `process_geometry` unless they are explicitly testing compatibility behavior or documenting historical releases.

Historical PyPI distributions named `aeg-shakespeare` should not be installed alongside current `process-geometry` releases because those old distributions ship their own `aeg_shakespeare` tree and can shadow the alias package.

## 5. Import-hygiene rule

The repository should enforce the dependency direction:

```text
process_geometry  <-  aeg_shakespeare compatibility alias
```

and forbid the reverse direction.

In particular:

- `src/process_geometry/**` must not import `aeg_shakespeare`;
- public quickstarts must use `process_geometry`;
- release smoke tests must treat `process_geometry` as primary and `aeg_shakespeare` only as a compatibility check;
- future repository-owned code should not create new dependencies on the historical namespace.

## 6. Release gates

Before tagging `v0.0.4`:

1. CPython 3.10–3.14 CI passes;
2. wheel and sdist metadata report `process-geometry==0.0.4`;
3. `twine check dist/*` passes;
4. the built wheel installs outside the source tree and imports `process_geometry`;
5. representative Process / Presentation / Discovery / Analysis imports succeed from the canonical namespace;
6. the legacy namespace imports successfully and representative deep symbols are identical to their canonical counterparts;
7. source/import hygiene checks prove that canonical implementation code does not depend on `aeg_shakespeare`;
8. quickstarts run using `process_geometry` only.

## 7. Non-goals

Release `0.0.4` does **not**:

- remove the `aeg_shakespeare` compatibility namespace;
- change the four-layer semantic API organization;
- promote `ProcessGeometry`, objectification, rank lowering, observer topology, or analytic-closure research concepts into public classes;
- claim Arithmetic Universality;
- promise backward compatibility for the broader `0.0.x` API.

The release establishes namespace ownership so later API evolution has one unambiguous software home.
