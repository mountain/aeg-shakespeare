# Public API map

Process Geometry exposes a semantic API hierarchy rather than a flat symbol catalog.
The four public namespaces are:

```text
Process  ->  Presentation  ->  Discovery  ->  Analysis
```

The arrows describe the intended conceptual dependency: a process exists before
one chooses a finite presentation; discovery searches alternative presentations;
analysis consumes successful presentations to build adequate function/geometric
languages.

The canonical Python package is `process_geometry`. The historical
`aeg_shakespeare` package is a deprecated compatibility alias only; it is not a
second implementation owner.

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

This namespace deliberately does not imply a universal group, topology,
measure, representation, or cohomology hierarchy.

### `process.local`

Local/infinitesimal realizations:

- `ProcessSystem`
- `ProcessFrame`

A finite process family and a local generator may be related in a mathematical
vignette, but Process Geometry does not yet impose a universal finite-to-infinitesimal
bridge.

## 2. `process_geometry.presentation`

A presentation records how process/history information is objectified,
quotiented, reconstructed, transformed, and costed.

### `presentation.history`

- `WordRewriteRule`, `rewrite_once`, `normalize_word`
- `RewriteStep`, `RewriteResult`
- `ProcessJetSignature`, `process_jet_signature`
- `history_process_jet_signature`, `histories_task_equivalent`
- `history_depth`, `boundary_profile`
- `BoundaryProfile`, `PrefixCode`, `PrefixCodeMetrics`, `huffman_prefix_code`

### `presentation.construction`

- `SymbolicOperation`
- `PrimitiveConstruction`
- `PrimitiveProposal`, `PrimitiveProposalResult`, `RejectedPrimitiveProposal`
- `generate_primitive_proposals`

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

`PresentationMorphism` is the minimal task-relative record promoted after three
independent calibrations: KdV tau/rewrite presentations, resistor-network
Schur/Y-Delta transformations, and braid/Markov moves. It binds a source
presentation, target presentation, declared task semantics, caller-defined
certificate, and optional construction witness.

The public object deliberately does **not** define a universal verifier,
composition law, inverse, normal-form relation, category/groupoid structure, or
same-type requirement for source and target. In particular, a morphism may connect
presentations with different carrier dimensions when the declared task semantics
provides the comparison.

### `presentation.search`

- `SearchBudget`
- `PresentationCost`
- `PresentationCandidate`, `PresentationSearchResult`
- `pareto_frontier`
- exact reconstruction / primitive-proposal search entry points

## 3. `process_geometry.discovery`

Discovery contains bounded algorithms for proposing or selecting alternative
representations. It is not process ontology.

Current implementation families include:

- polynomial observer bases, invariants, and quotient elimination;
- structured pairing observers;
- first-order observer quotient selection;
- explicit coefficient-language extension experiments.

The package already has internal modules (`polynomial`, `structured`,
`selection`, `coefficient_extension`). Their existence does not promote every
backend object into a stable public abstraction.

## 4. `process_geometry.analysis`

Analysis contains mathematical languages supported by successful process
presentations.

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

These objects are intentionally not re-exported from the package root.

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

remain available lazily and emit `DeprecationWarning`. They exist only as a
transition bridge from the earliest flat API and are not part of the declared
root contract.

Separately, the historical namespace remains temporarily importable:

```python
import aeg_shakespeare
from aeg_shakespeare.process.history import ProcessWord
```

Importing `aeg_shakespeare` emits `DeprecationWarning`. The compatibility layer
aliases canonical modules rather than owning implementations, so representative
deep imports must preserve object identity:

```python
from process_geometry.process.history import ProcessWord as NewProcessWord
from aeg_shakespeare.process.history import ProcessWord as OldProcessWord

assert NewProcessWord is OldProcessWord
```

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
- `presentation` may consume process objects but must not require optional
  function theories;
- `discovery` may consume process/presentation machinery to search alternatives;
- `analysis` may consume process/presentation outputs, but core process ontology
  must not know about Abelian periods, Fourier transforms, or other downstream
  languages.

The namespace migration adds a second, orthogonal ownership invariant:

```text
process_geometry  <-  aeg_shakespeare compatibility alias
```

Canonical implementation code under `src/process_geometry/**` must never import
or depend on `aeg_shakespeare`. The reverse dependency is the entire purpose of
the compatibility alias.

## 7. Research concepts are not automatically API concepts

The Process Geometry foundation now discusses distinguishability topology,
semantic compression, objectification, rank lowering, and analytic closure.
Those research concepts do **not** become public classes merely because the
software namespace now matches the project name. Any generic abstraction must
still pass the lifecycle in `GOVERNANCE.md`: Sonnet -> extraction candidate ->
Experimental -> maturing -> Public API.
