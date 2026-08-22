# Physical API consolidation B.2: semantic core decomposition

**Status:** split the old mixed `core.py` by semantic ownership; retain only a backend helper and compatibility re-exports in `core.py`.

## 1. Why `core.py` could not be moved wholesale

The original research-preview `core.py` contained four different kinds of object:

- literal history (`ProcessWord`, `interpret_history`);
- local process realization (`ProcessSystem`);
- presentation-search policy (`SearchBudget`);
- one SymPy polynomial helper (`homogeneous_monomials`).

After the public namespace refactor, moving that file intact under any one
semantic package would preserve the wrong architecture. B.2 therefore decomposes
it instead of renaming it.

## 2. Canonical ownership

The implementations now live at:

```text
process/history.py
    ProcessWord
    interpret_history

process/local/
    system.py     -> ProcessSystem
    frame.py      -> ProcessFrame

presentation/budget.py
    SearchBudget
```

`ProcessFrame` is moved together with `ProcessSystem` because both are local /
infinitesimal process realizations. The old top-level `frame.py` is now only an
identity-preserving compatibility shim.

## 3. What remains in `core.py`

`core.py` is no longer a semantic owner. It retains:

1. identity-preserving compatibility imports for the old internal paths;
2. `homogeneous_monomials`, explicitly documented as a SymPy backend helper.

The polynomial discovery backend may still import that helper. No public
ontology claim is attached to it.

## 4. Dependency cleanup

Implementation modules now depend directly on semantic owners:

- rewrite/signature/history geometry -> `process.history`;
- grammar/relations/search/discovery -> `process.local` and
  `presentation.budget` where appropriate;
- A/M and finite function modules -> `process.local.ProcessFrame`.

`tests/test_source_semantic_hygiene.py` parses the source tree and prevents
semantic objects from being re-imported through `core.py` or the old `frame.py`
shim. Outside compatibility modules, the only permitted `core` import is
`homogeneous_monomials`.

## 5. Physical ownership certificates

The physical-layout tests require:

```text
ProcessWord.__module__   == aeg_shakespeare.process.history
ProcessSystem.__module__ == aeg_shakespeare.process.local.system
ProcessFrame.__module__  == aeg_shakespeare.process.local.frame
SearchBudget.__module__  == aeg_shakespeare.presentation.budget
```

Old `core` / `frame` paths must resolve to the exact same class objects.

## 6. Boundary

B.2 does not yet physically relocate grammar, relation, cost/search, discovery,
or analysis implementation modules. The important result is that those modules
no longer need the old mixed semantic core.

This creates a much cleaner basis for later physical moves: presentation modules
can now be consolidated without dragging local process ownership or search
budget policy through `core.py`.
