# AEG Shakespeare 0.0.2

**Release date:** 2026-08-22  
**Status:** pre-alpha research preview

`0.0.2` is the second installable research release of AEG Shakespeare. It is primarily a consolidation release: the project now has a clearer semantic public API, a larger executable discovery/calibration surface, and explicit architectural hygiene checks that keep compatibility paths from becoming hidden dependencies.

`0.0.x` APIs remain experimental and are not covered by backward-compatibility guarantees.

## Public API shape

The declared public surface is organized as

```text
Process -> Presentation -> Discovery -> Analysis
```

The package root is intentionally a namespace router rather than a flat catalog. Legacy root-level symbol imports from the early research-preview API remain available lazily for migration and emit `DeprecationWarning`.

Canonical ownership now includes:

- `process.history` for literal histories and caller-supplied semantics;
- `process.finite` for finite process families, scalar characters, family actions, and additive process cocycles;
- `process.local` for `ProcessSystem` and `ProcessFrame`;
- `presentation` for budgets, rewriting, constraints, generated grammars, relations, construction histories, cost, and Pareto search;
- `discovery` for bounded invariant/observer/quotient/language search;
- `analysis` for A/M, algebraic, and Abelian/global function-theory layers.

Repository tests include AST dependency-hygiene checks and physical-ownership checks so old compatibility modules cannot silently become canonical implementation owners again.

## Discovery and calibration additions

Since `0.0.1`, Shakespeare has added:

- bounded polynomial observer grammars and exact first-integral discovery;
- exact observable-quotient elimination with pullback certificates;
- structured pairing-based observer proposals;
- Pareto selection of first-order algebraic observer quotients;
- explicit coefficient-language extension and relation-factor refinement;
- oscillator red-team calibrations showing that finer decomposition is not automatically a cheaper presentation;
- finite-family/character/action calibrations for translation, dilation, A/M, and Galilean mechanics;
- a minimal `ProcessCocycle` abstraction forced independently by Bargmann mass and magnetic-translation flux residuals;
- extended Abelian-history machinery through lifted paths, cycle/intersection structure, period matrices, and normalized Abel–Jacobi history quotients.

These are deliberately bounded research abstractions. Shakespeare still does not expose a universal `Group`, `Representation`, `Spectrum`, `FourierTransform`, cohomology hierarchy, projective-representation framework, or automatic finite-to-infinitesimal bridge.

## Python support

`0.0.2` declares and continuously tests CPython:

```text
3.10, 3.11, 3.12, 3.13, 3.14
```

Every supported version runs the same release gate:

1. editable install with development dependencies;
2. full pytest suite;
3. public quickstarts;
4. sdist/wheel build;
5. `twine check`;
6. isolated wheel installation outside the source tree;
7. semantic public-API smoke imports.

## Packaging and publication

Package metadata and `aeg_shakespeare.__version__` are both `0.0.2`.

Publishing uses the repository's GitHub Actions PyPI Trusted Publisher workflow. No PyPI password or API token is stored in the repository.

## Research boundary

This release should be read as a checkpoint in a research program, not as a stable end-user numerical library. Exact certificates, explicit failure modes, process-history preservation, and conceptual layer separation continue to take priority over API stability and breadth during the `0.0.x` series.
