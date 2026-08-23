# Changelog

## Unreleased

- namespace migration from `aeg_shakespeare` to a Process Geometry-native import path remains intentionally deferred; the `0.0.3` release changes distribution identity first.

## 0.0.3 — Process Geometry release identity

First pre-alpha release under the **Process Geometry** distribution identity.

Highlights:

- renames the PyPI distribution from `aeg-shakespeare` to `process-geometry` while preserving the existing `aeg_shakespeare` import namespace for this transition release;
- moves the repository identity to `mountain/process-geometry` and updates package, citation, CI, and publish metadata accordingly;
- retains the semantic public pipeline `Process -> Presentation -> Discovery -> Analysis`;
- adds the minimal public `presentation.morphism.PresentationMorphism` record after independent KdV, resistor-network, and braid/Markov calibrations;
- keeps morphism validity explicitly task-relative through caller-defined semantics and certificates, allows heterogeneous source/target presentation types, and deliberately postpones universal verification, composition, inverses, normal forms, and category/groupoid structure;
- adds the first-principles Process Geometry foundation: exact distinguishability quotients, the Myhill–Nerode minimal-presentation calibration, and the topological threshold;
- adds the vertical objectification program: semantic compression, new primitives, free higher-rank composition, and compositional rank lowering;
- records the lineage against algebraic theories, operads, Baez–Dolan slicing, polygraphs/computads, definitional extension, abstract interpretation, and sheaf-style locality;
- distinguishes semantic, topological, and analytic cross-rank closure, with AEG retained as the first model organism rather than as a package-wide arithmetic restriction;
- keeps Shakespeare/Sonnet as the problem-driven research program rather than the software distribution identity.

Historical releases `0.0.1` and `0.0.2` were published under the PyPI distribution name `aeg-shakespeare`. The new `process-geometry` distribution should not be installed side-by-side with the historical distribution because both currently provide the same transitional `aeg_shakespeare` import package.

`0.0.x` APIs remain experimental and may change without compatibility guarantees.

## 0.0.2 — semantic API and discovery expansion

Second pre-alpha research release of AEG Shakespeare.

Highlights:

- reorganizes the public API into the semantic pipeline `Process -> Presentation -> Discovery -> Analysis`;
- contracts the package root to namespace navigation while retaining lazy `0.0.x` compatibility shims;
- physically consolidates finite process families, characters, actions, and process cocycles under `process.finite`;
- moves literal histories and local process realizations to canonical `process.history` / `process.local` ownership and moves search budgets to `presentation`;
- adds bounded polynomial invariant and observable-quotient discovery;
- adds structured pairing-based observer proposals and Pareto selection of first-order algebraic quotients;
- adds explicit coefficient-language extension for discovered process relations, with oscillator red-team tests showing that finer splitting is not universally cheaper;
- adds finite `ProcessFamily`, `ProcessCharacter`, `FamilyAction`, and `ProcessCocycle` calibrations through translation, dilation, A/M, Galilean mechanics, and magnetic translations;
- extends the global Abelian-history line through lifted cycles, period matrices, intersection structure, and normalized Abel–Jacobi history quotients;
- adds repository-level AST import-hygiene and physical-ownership checks so compatibility modules cannot silently become architectural dependencies;
- supports and tests CPython 3.10, 3.11, 3.12, 3.13, and 3.14.

`0.0.x` APIs remain experimental and may change without compatibility guarantees.

## 0.0.1 — research preview

First installable pre-alpha release of AEG Shakespeare.

Highlights:

- ordered `ProcessWord` histories and explicit noncommutative rewriting;
- bounded task-sufficient process signatures;
- history depth/boundary observables and Huffman prefix strategy;
- construction-history-preserving primitive proposals;
- generated finite process grammars and exact return-relation decomposition;
- algebraic constraint quotients and prolongation;
- multi-axis presentation cost and Pareto search;
- generic `ProcessFrame` and `ProcessFunctionModule` abstractions;
- Addition/Multiplication (A/M) function-theory prototype with resonance and path-flow structure;
- classical/research calibration program including constrained pendulum and genus-hierarchy probes;
- public-domain dedication and literate-programming/citation discipline.

`0.0.x` APIs are experimental and may change without compatibility guarantees.
