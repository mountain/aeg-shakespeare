# Changelog

## Unreleased

- adds `docs/55-pendulum-lifted-clock-global-quotient.md` and a research executable essay globalizing the lifted-clock/geometric-phase chain of `docs/54` (PR #79) on the lemniscatic leaf;
- certifies the exact sigma symmetry `sigma(U,Y)=(-U,iY)` with `sigma*omega = i omega` (hence `tau = i`), the complex-flow carrier ODE `dU/dz = Y`, and the square period lattice `Lambda = Z T_p + Z i T_p` with the Jacobi identities `K(i) = varpi/2` and `T_p = 4 sqrt(2) K(i)`;
- certifies the branch-locus degeneration: the local decoder chart fails exactly at `U = +/-1`, the Z2 mark flips across each turning point (mark monodromy -1 around each branch point), and the real period loop lifts to a closed marked loop;
- reads off the clock-chain information contract: `R -> R/T_p Z` forgets winding, and the real phase embeds in `C/Lambda` because `R cap Lambda = T_p Z` — the third arrow is a complexification, not a further quotient;
- keeps the result research-local: no Theory Map node/edge change, no public or experimental API pressure, and no promotion of TR-0001; the E = 0 leaf is the declared scope, other energy leaves remain open;
- adds `docs/51-aeg-addition-multiplication-rank-transition.md` and a research executable essay for the second arithmetic rank transition: Multiplication objectifies a uniform repeated-Addition endomorphism on Translation objects rather than one fixed additive composite;
- lowers pure multiplicative words to Translation endomorphisms and arbitrary mixed Translation/Dilation words to the positive affine monoid, with exact relation soundness for `T_a T_b = T_(a+b)`, `D_k D_l = D_(kl)`, and the AEG cross relation `D_k T_a = T_(ka) D_k`;
- records two second-rank red teams: one fixed additive result cannot identify the multiplicative process schema, and a nontrivial dilation cannot lower to any single Translation object; connects the finite cross relation to the existing A/M finite law and `[A, M] = A` without claiming V5 analytic closure;
- adds `docs/50-aeg-translation-objectification-rank-lowering.md` and a research executable essay providing the first complete concrete V1→V4 calibration: continuation-stable semantic compression, objectification into reusable Addition/translation primitives, free higher-rank composition, compositional lowering, and relation soundness;
- adds an adversarial absolute-displacement compression showing that terminal equality is insufficient when continuation can recover a discarded distinction;
- refines `docs/THEORY_MAP.md` so V2–V4 now record one complete AEG/Addition research calibration while generic objectification, rank, and lowering abstractions remain intentionally unpromoted;
- adds `docs/49-theory-implementation-structural-alignment.md`, mapping H0–H4 and V0–V5 in the living Theory Map to current executable implementations, calibrated shadows, and missing semantics;
- adds an explicit `process_geometry.experimental` incubation namespace without changing the stable root API;
- adds `FiniteTaskQuotient` / `minimize_finite_task_process`, an exact finite deterministic H1/V1 calibration using stable partition refinement and future distinguishing continuations, deliberately narrower than a generic Process Geometry task quotient;
- refines `docs/THEORY_MAP.md` so H1/V1 distinguish bounded public task-continuation evidence from the exact finite Experimental quotient slice;
- aligns current program vocabulary with the Process Geometry foundation in `docs/42–45` and records the mapping in `docs/48-foundation-naming-audit.md`;
- makes `TaskContinuationSignature`, `task_continuation_signature`, and `history_task_continuation_signature` the canonical names for the bounded future-task signature, retaining the historical `ProcessJet*` names as 0.0.x aliases so `jet` remains available for genuinely differential/local structure;
- exposes qualified discovery names `ObservableAlgebraicQuotient`, `discover_first_order_observable_quotient`, `search_first_order_observer_presentations`, and `structural_first_order_observer_presentation_cost`, while retaining historical backend aliases;
- reserves strong theory words such as task/process quotient, objectification, process rank, rank lowering, and analytic closure until their full semantics are implemented rather than promoting new classes by nomenclature alone;
- further migration of repository-owned historical tests/docs from `aeg_shakespeare` remains follow-up work; no new implementation may depend on the deprecated namespace.

## 0.0.4 — canonical `process_geometry` namespace

Second identity-migration release of Process Geometry.

Highlights:

- makes `process_geometry` the canonical Python import namespace;
- moves the complete implementation tree under `src/process_geometry`;
- reduces `src/aeg_shakespeare` to a temporary compatibility alias rather than keeping a second implementation copy;
- preserves deep Python object identity between representative legacy and canonical imports;
- changes public quickstarts, wheel smoke tests, and publish smoke tests to use `process_geometry` as the primary namespace;
- retains `aeg_shakespeare` only as a deprecated compatibility path for code written against `0.0.1`–`0.0.3`;
- establishes the dependency direction `process_geometry <- aeg_shakespeare alias` and adds release/hygiene requirements preventing canonical implementation code from depending on the historical namespace;
- leaves the semantic public pipeline `Process -> Presentation -> Discovery -> Analysis` unchanged and promotes no new Process Geometry research abstractions solely because of the namespace migration.

Historical PyPI distributions named `aeg-shakespeare` should not be installed alongside current `process-geometry` releases because they ship their own `aeg_shakespeare` package and may shadow the compatibility alias.

`0.0.x` APIs remain experimental and may change without compatibility guarantees.

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
