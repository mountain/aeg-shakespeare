# Public API map

Process Geometry exposes a semantic API hierarchy rather than a flat symbol catalog.
The four public namespaces are:

```text
Process  ->  Presentation  ->  Discovery  ->  Analysis
```

The arrows describe the intended conceptual dependency: a process exists before one chooses a finite presentation; discovery searches alternative presentations and observer constructions; analysis consumes successful presentations to build adequate function/geometric languages.

The canonical Python package is `process_geometry`. The historical `aeg_shakespeare` package is a deprecated compatibility alias only; it is not a second implementation owner.

The terminology in this document follows `docs/42–45` and the naming rules in `docs/48-foundation-naming-audit.md`. In particular, **task/process quotient**, **jet**, and **objectification** are reserved for their stronger foundation meanings.

## 1. `process_geometry.process`

### `process.history`

Literal process history and interpretation:

- `ProcessWord`
- `interpret_history`

### `process.finite`

Finite parameterized process structure:

- `ProcessFamily`, `FamilyStep`
- `ProcessCharacter`, `CharacterVerification`, `verify_process_character`
- `FamilyAction`, `FamilyActionVerification`, `verify_family_action`
- `transport_process_character`, `character_invariance_residual`
- `ProcessCocycle`, `CocycleVerification`, `verify_process_cocycle`
- `central_commutator_residual`

This namespace deliberately does not imply a universal group, topology, measure, representation, or cohomology hierarchy.

### `process.local`

Local/infinitesimal realizations:

- `ProcessSystem`
- `ProcessFrame`

A finite process family and a local generator may be related in a mathematical vignette, but Process Geometry does not yet impose a universal finite-to-infinitesimal bridge.

## 2. `process_geometry.presentation`

A presentation records an explicit realization of process/history structure: relations, task-sufficiency evidence, reconstruction, transformation, and cost. A presentation may participate in semantic compression, but the current API does not equate ordinary presentation construction with the stronger `docs/44` notion of objectification.

### `presentation.history`

History rewriting and bounded task distinguishability:

- `WordRewriteRule`, `rewrite_once`, `normalize_word`
- `RewriteStep`, `RewriteResult`
- `TaskContinuationSignature`, `task_continuation_signature`
- `history_task_continuation_signature`, `histories_task_equivalent`
- `history_depth`, `boundary_profile`
- `BoundaryProfile`, `PrefixCode`, `PrefixCodeMetrics`, `huffman_prefix_code`

Historical 0.0.x names `ProcessJetSignature`, `process_jet_signature`, and `history_process_jet_signature` remain compatibility aliases. They are no longer canonical because the implemented object is a bounded continuation signature, not a differential jet.

### `presentation.construction`

Candidate primitive construction with preserved provenance:

- `SymbolicOperation`
- `PrimitiveConstruction`
- `PrimitiveProposal`, `PrimitiveProposalResult`, `RejectedPrimitiveProposal`
- `generate_primitive_proposals`

`PrimitiveProposal` means **candidate primitive**. It has not, merely by being proposed, satisfied semantic-stability, higher-rank composition, or compositional rank-lowering requirements and therefore is not an `ObjectifiedPrimitive`.

### `presentation.constraints`

- `AlgebraicConstraintSet`
- `constraint_prolongation`

### `presentation.grammar`

- `GeneratedGrammar`, `GeneratedPresentation`
- `discover_generated_grammar`
- `discover_generated_presentation`

### `presentation.relations`

- `ProcessPolynomialRelation`
- `ReturnRelation`, `RelationKernel`, `RelationDecomposition`
- `discover_return_relation`, `discover_operator_relation`
- `factor_process_relation`
- `discover_relation_kernel`, `discover_relation_decomposition`
- exact coordinate/decomposition utilities used by finite presentations

### `presentation.morphism`

- `PresentationMorphism`

`PresentationMorphism` is the minimal task-relative record promoted after three independent calibrations: KdV tau/rewrite presentations, resistor-network Schur/Y-Delta transformations, and braid/Markov moves. It binds a source presentation, target presentation, declared task semantics, caller-defined certificate, and optional construction witness.

The public object deliberately does **not** define a universal verifier, composition law, inverse, normal-form relation, category/groupoid structure, or same-type requirement for source and target. In particular, a morphism may connect presentations with different carrier dimensions when the declared task semantics provides the comparison.

### `presentation.search`

- `SearchBudget`
- `PresentationCost`
- `PresentationCandidate`, `PresentationSearchResult`
- `pareto_frontier`
- exact reconstruction / primitive-proposal search entry points

Formal API text uses **presentation cost** rather than `representation cost`: representation remains a broad informal umbrella, while `PresentationCost` evaluates a concrete declared realization.

## 3. `process_geometry.discovery`

Discovery contains bounded algorithms for proposing or selecting alternative presentations, observers, observables, and quotient candidates. It is not process ontology.

Current implementation families include:

- polynomial observable bases and invariant discovery;
- structured pairing observer proposals;
- algebraic elimination of source variables into observable relations;
- first-order observer-presentation selection;
- explicit coefficient-language extension experiments.

The theory-aligned public names for the first-order polynomial path are:

- `ObservableAlgebraicQuotient`
- `discover_first_order_observable_quotient`
- `FirstOrderObservablePresentation`
- `search_first_order_observer_presentations`
- `structural_first_order_observer_presentation_cost`

These names are deliberately qualified. The polynomial backend constructs an algebraic presentation of selected observables; it does **not** construct the history/task quotient

\[
\mathcal H(P)/{\sim_Q}
\]

from `docs/42–43`.

Historical backend names `ObservableQuotient`, `discover_first_order_process_quotient`, `search_first_order_process_quotients`, and `structural_first_order_quotient_cost` remain aliases during the 0.0.x transition.

`Observable` and `Observer` are also not interchangeable: an observable is a quantity read from a process; an observer may be a broader protocol or structured mechanism that determines distinguishability.

## 4. `process_geometry.analysis`

Analysis contains mathematical languages supported by successful process presentations. In the foundation (`docs/45`), its eventual theoretical role is the study of variation on induced process structures, not merely a collection of classical solver backends.

### `analysis.module`

- `ProcessFunctionModule`
- `polynomial_am_module`

### `analysis.am`

- `AMFunctionTheory`
- `AMPrimitive`, `AMPowerWeight`, `AMPathFlow`, `AMState`
- `affine_am_frame`

### `analysis.algebraic`

- `HyperellipticProfile`, `hyperelliptic_profile`
- `WeierstrassCubicProfile`, `weierstrass_cubic_profile`

### `analysis.abelian`

- holomorphic differential and Abelian-integral profiles;
- lifted square-root histories and period integration;
- cycle intersections and real-branch cycle constructions;
- `AbelianCycleSystem`, `AbelianPeriodMatrix`, `compute_period_matrix`;
- Abel-Jacobi history increments and `NormalizedAbelianTorus`.

Local canonical-observer records are not part of the declared Analysis or
Presentation surfaces.  Their canonical ownership is Experimental; see
section 7.  Historical `analysis.connection`, `analysis.decomposition`, and
`presentation.canonicalization` module paths remain 0.0.x compatibility shims.

## 5. Root contract

The declared canonical root public surface is only:

```python
import process_geometry as pg

pg.process
pg.presentation
pg.discovery
pg.analysis
pg.__version__
```

`process_geometry.__all__` contains only those names.

During the `0.0.x` migration, old root-level symbols such as

```python
from process_geometry import ProcessWord
```

remain available lazily and emit `DeprecationWarning`. They exist only as a transition bridge from the earliest flat API and are not part of the declared root contract.

Separately, the historical namespace remains temporarily importable:

```python
import aeg_shakespeare
from aeg_shakespeare.process.history import ProcessWord
```

Importing `aeg_shakespeare` emits `DeprecationWarning`. The compatibility layer aliases canonical modules rather than owning implementations, so representative deep imports preserve object identity.

New code should not use the historical namespace.

## 6. Dependency discipline

The desired conceptual dependency direction is:

```text
process <- presentation <- discovery
    ^           ^
    |           |
    +-------- analysis
```

More precisely:

- `process` must not depend on presentation-search or analysis concepts;
- `presentation` may consume process objects but must not require optional function theories;
- `discovery` may consume process/presentation machinery to search alternatives;
- `analysis` may consume process/presentation outputs, but core process ontology must not know about Abelian periods, Fourier transforms, or other downstream languages.

The foundation adds a second discipline: **large theory words are not API rewards**. Names such as `ProcessGeometry`, `Objectification`, `ProcessRank`, `RankLowering`, `ObserverTopology`, and `AnalyticClosure` remain unclaimed until independent executable structures and red teams justify them.

### 6.1 Effective-analysis discipline

An API under `analysis` does not acquire a generic calculus claim merely from
its namespace.  Each concrete family should document which mode it provides:

```text
exact-symbolic
certified-approximate
numerical
search-only
record-only
```

Where applicable, the durable contract includes the function/observable
language, process operators, closure or controlled extension, evaluator,
certificates, numerical domain, units/scale, error and failure semantics,
baseline, and cost boundary.  Exact, stable, and efficient are separate claims.
One computer-algebra backend does not define process equality; one numerical
match does not establish stability; shortened syntax does not establish lower
cost after compilation, storage, residual, and decoding are charged.

This standard strengthens evidence requirements without promoting a generic
`Calculus`, `ComputablePresentation`, `CanonicalSolver`, or `AnalyticClosure`
object.  See `docs/65-effective-analysis-principle.md`.

## 7. `process_geometry.experimental`

Experimental is not a fifth stable layer in the public pipeline. It is an explicitly unstable incubation namespace governed by `docs/GOVERNANCE.md` and reviewed against `docs/THEORY_MAP.md`.

The first theory-to-code alignment probe is:

- `FiniteTaskQuotient`
- `DistinguishingContinuation`
- `minimize_finite_task_process`

For a **finite deterministic** state carrier, finite step alphabet, total closed transition rule, and hashable task observation, this experiment computes the exact coarsest continuation-stable task quotient. It also constructs the induced quotient transition and supplies a future continuation distinguishing every pair of distinct quotient classes.

This is intentionally stronger than bounded `TaskContinuationSignature`: there is no continuation-depth cutoff in the declared finite class. It is also intentionally narrower than a generic Process Geometry task quotient: no claims are made about infinite, nondeterministic, probabilistic, continuous, approximate, or resource-bounded processes.

Example:

```python
from process_geometry.experimental import minimize_finite_task_process

quotient = minimize_finite_task_process(
    states,
    steps,
    transition,
    observe,
)
```

The exact finite quotient certificate is executable: `run_class` applies a
continuation on the induced quotient process, `observe_after` evaluates the task
after it, and `witness_between` returns a continuation separating any two
distinct quotient classes.  `state_to_class` is read-only.  Numeric class
indices are presentation artifacts determined by caller state order; the
minimal quotient is canonical only up to isomorphism.

The second Experimental family contains local canonical-observer evidence
records:

- `ConstraintCanonicalization`;
- `ObserverConnection`;
- `CanonicalDecomposition`.

Use:

```python
from process_geometry.experimental import (
    CanonicalDecomposition,
    ConstraintCanonicalization,
    ObserverConnection,
)
```

These records implement a qualified local equation/transport/decomposition
slice.  They do **not** assert a generic observer topology, global canonical
lift, unique task ruler, universal connection, or canonical decomposition
theorem.  Their former module paths preserve object identity temporarily but
are excluded from `presentation.__all__` and `analysis.__all__`.

Experimental symbols are not re-exported from `process_geometry` root and carry no compatibility promise. Their purpose is to test whether a Theory Map node has acquired enough executable semantics to survive broader calibrations.
