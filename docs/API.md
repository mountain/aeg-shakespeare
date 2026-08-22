# Public API map

Shakespeare exposes a semantic API hierarchy rather than a flat symbol catalog.
The four public namespaces are:

```text
Process  ->  Presentation  ->  Discovery  ->  Analysis
```

The arrows describe the intended conceptual dependency: a process exists before
one chooses a finite presentation; discovery searches alternative presentations;
analysis consumes successful presentations to build adequate function/geometric
languages.

## 1. `aeg_shakespeare.process`

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
vignette, but Shakespeare does not yet impose a universal finite-to-infinitesimal
bridge.

## 2. `aeg_shakespeare.presentation`

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

## 3. `aeg_shakespeare.discovery`

Discovery contains bounded algorithms for proposing or selecting alternative
representations. It is not process ontology.

Current implementation families include:

- polynomial observer bases, invariants, and quotient elimination;
- structured pairing observers;
- first-order observer quotient selection;
- explicit coefficient-language extension experiments.

The package already has internal modules (`polynomial`, `structured`,
`selection`, `coefficient_extension`). A later refactor may narrow the
`discovery.__init__` surface further; Phase A intentionally does not combine
that mechanical change with the root namespace migration.

## 4. `aeg_shakespeare.analysis`

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

The declared root public surface is only:

```python
import aeg_shakespeare as sh

sh.process
sh.presentation
sh.discovery
sh.analysis
sh.__version__
```

`aeg_shakespeare.__all__` contains only those names.

During the `0.0.x` migration, legacy imports such as

```python
from aeg_shakespeare import ProcessWord
```

remain available lazily and emit `DeprecationWarning`. They exist only as a
transition bridge and are not part of the new public root contract.

## 6. Dependency discipline

The desired long-term dependency direction is:

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

The facade packages introduced in Phase A enforce the public ontology first.
Physical source-file relocation is deferred to a later mechanical phase so that
architecture and file movement can be reviewed separately.
