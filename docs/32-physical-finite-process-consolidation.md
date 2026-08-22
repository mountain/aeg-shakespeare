# Physical API consolidation B.1: finite process structure

**Status:** first implementation relocation after the semantic namespace and import-graph refactors.

## 1. Why finite process comes first

Phase A established the public hierarchy

```text
Process -> Presentation -> Discovery -> Analysis
```

without moving implementation files. Phase A.2 then made the repository itself
consume that hierarchy directly.

The finite-process cluster is the cleanest place to begin physical
consolidation because its public boundary is already stable and its implementation
has very little inward coupling:

- process families and scalar characters;
- family actions and character transport;
- additive process cocycles and their exact certificates.

By contrast, the old `core.py` still mixes literal histories, local process
realizations, search budgets, and a polynomial backend helper. It is therefore a
poor first target for mechanical relocation.

## 2. Physical move

The canonical implementation now lives at

```text
aeg_shakespeare/process/finite/
    __init__.py
    families.py
    cocycle.py
```

The public import remains

```python
from aeg_shakespeare.process.finite import ProcessFamily, ProcessCocycle
```

so Phase B changes physical ownership without changing the semantic facade.

The old implementation paths

```text
aeg_shakespeare/families.py
aeg_shakespeare/central.py
```

are retained as thin identity-preserving compatibility shims. They contain no
independent implementation.

## 3. Executable ownership certificate

`tests/test_physical_api_layout.py` requires

```text
ProcessFamily.__module__ == aeg_shakespeare.process.finite.families
ProcessCocycle.__module__ == aeg_shakespeare.process.finite.cocycle
```

and also requires the old module-path imports to resolve to the exact same class
objects. This prevents a compatibility shim from silently becoming a forked
second implementation.

## 4. Boundary

This phase does not move:

- `core.py` / `frame.py`;
- presentation implementations such as grammar, relations, or search;
- discovery implementations;
- the existing `function_theory/` package.

Those moves should be staged independently. In particular, mixed modules should
first be split by semantic ownership rather than copied wholesale into a new
directory.

The next physical-refactor candidate should be selected from the clean import
graph established by A.2, with the same rule: one coherent semantic cluster per
PR and compatibility shims at old implementation paths where useful.
