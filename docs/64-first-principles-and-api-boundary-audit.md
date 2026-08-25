# First-principles and API-boundary audit

**Date:** 2026-08-25  
**Status:** repository audit and conservative refactor record; no theory-maturity
promotion and no new Public API.  
**Baseline:** `main@58c3057`, 448 tests passed and 25 skipped before the
refactor.

## 1. Verdict

The repository has established a clear first-principles **spine**, but not a
closed first-principles theory.

The stable spine consists of two independently meaningful axes:

1. **horizontal distinguishability geometry** — a process supplies histories
   and continuations; a declared observer/task determines which distinctions
   survive; exact continuation semantics can force a quotient, while coherent
   finite-resolution semantics can later force topology, complexity, metric,
   and differential structure;
2. **vertical ontology growth** — stable lower-rank semantics may become a new
   primitive only when it opens a genuine higher-rank composition language and
   every legal composite retains a coherent lower-rank interpretation.

These axes explain why the project is called Process Geometry without assuming
that every process is a manifold or that Arithmetic Universality is already
true.  They also give a principled place to the existing software pipeline:

```text
Process -> Presentation -> Discovery -> Analysis
```

The pipeline is an engineering decomposition that serves the two axes; it is
not itself the ontology.

The theory is not closed because the recent history-cost, Bellman, Noether,
coarea, thermodynamic, and holonomy work has forced an additional transversal
question that has not yet earned a Core node:

```text
lifted history
  -> transported composable payload
  -> task evaluation / resource order
  -> stopping, coding, partition, or variational objective
```

This is provisionally a **task-covariant evaluation layer**.  It cuts across
both axes: it determines what quotienting may forget, what objectification must
charge, how history residuals create memory, and how Bellman/Huffman or
partition constructions evaluate a presentation.  The evidence is substantial
but heterogeneous and remains T0/T1.  It must not yet become a generic API.

The correct high-level judgment is therefore:

> The repository now has a coherent first-principles grammar and a disciplined
> theory map.  It does not yet have a theorem-level mother object joining
> distinguishability, rank change, transported history payloads, and analysis.

## 2. What is genuinely established

### 2.1 Process and literal history are prior to representation

`ProcessWord`, finite families, local frames, and explicit interpretation keep
ordered generation separate from quotienting.  This is one of the strongest
theory/code alignments in the repository.

### 2.2 Exact task semantics can force a minimal finite quotient

Myhill--Nerode/Moore minimization supplies a theorem-level classical anchor.
`process_geometry.experimental.FiniteTaskQuotient` now realizes the exact
finite deterministic slice:

- stable partition refinement has no continuation-depth cutoff;
- task observation and deterministic transition descend to the quotient;
- every distinct class pair carries a distinguishing continuation;
- the result is a minimal task-sufficient deterministic presentation, with
  class numbering canonical only up to quotient isomorphism.

This is a narrow exact implementation, not a generic task quotient.

### 2.3 Topology has a precise threshold and is correctly absent

The repository distinguishes exact equivalence from locality.  No generic
observer topology is implemented because no common neighborhood/refinement and
process-continuity contract has yet survived a concrete calibration.  This
absence is evidence of discipline, not missing boilerplate.

### 2.4 One complete arithmetic V1--V4 cycle is executable

Signed unit histories compress to translation semantics, translations become
reusable primitives, unseen higher-rank words compose, and arbitrary legal
composites lower coherently.  The Addition-to-Multiplication continuation
sharpens the lowering target to endomorphisms and the positive affine monoid,
including the noncommutative cross relation.

This establishes concrete model organisms.  It does not yet identify the
generic domain of objectification or justify `Objectification`, `ProcessRank`,
or `RankLowering` as framework classes.

### 2.5 Presentation morphisms have earned a small public contract

KdV, resistor-network, and braid/Markov calibrations forced a common record for
task-relative transformation evidence.  The public object remains deliberately
smaller than a category: it has no universal verifier, composition, inverse, or
normal-form claim.

### 2.6 Several exact results constrain the evaluation layer

Recent research-local work establishes, in its declared finite or classical
scope:

- clock-measured pendulum stopping policies are invariant under the tested
  nonlinear observable reparameterization, while coordinate-spaced controls
  fail;
- covariant Bellman transport is required when local units differ;
- expected stopping cost equals probability-weighted frontier volume on a
  finite costed task tree;
- task-visible holonomy gives a Myhill--Nerode-style finite memory lower bound;
- a local clock distribution need not admit global stopping slices;
- same-scale log-sum-exp nesting is only finite mass pushforward when reference
  measure is transported coherently;
- plethystic assembly and twisted cycle characters retain different payloads
  and have different flattening boundaries.

These results constrain future theory sharply.  They do not yet select one
universal payload, resource, connection, or scalar complexity object.

## 3. The remaining first-principles gaps

### 3.1 The two axes are not yet unified

Horizontal quotienting and vertical objectification interact, but the project
does not yet possess an abstract theorem explaining when a task-stable quotient
class or action is exactly the kind of object that may generate a new rank.

### 3.2 The task-covariant evaluation layer has no settled carrier

The evidence requires at least some of:

- lifted histories before task quotienting;
- residual/deck/holonomy composition;
- additive, max-like, group-valued, or phase-valued payloads;
- connection or unit transport;
- task evaluation into an ordered resource;
- workload-dependent accounting for objectified shortcuts;
- a stopping section, ensemble, or variational boundary.

It is not yet known whether the correct abstraction is a bundle, groupoid,
enriched history category, cocycle family, fibration, or a smaller family of
problem-specific structures.  A generic `HistoryPayload`, `ResourceBundle`, or
`TaskCovariantComplexity` API would therefore freeze the choice too early.

### 3.3 Canonicalization remains relative and layered

The executable local equation backend proves only:

```text
declared constraints + declared base rates
  -> unique local observer rates, when a unique symbolic solution exists.
```

It does not prove a global canonical lift, task-independent sufficient quotient,
unique scalar ruler, branch/holonomy erasure, or history reconstruction.  The
pendulum, Abelian, centered-quadratic, and PCR3BP lines all show why those
obligations must stay separate.

### 3.4 H2 and V5 remain the two decisive theory gates

The next foundational advances should not be more vocabulary.  They are:

1. a legitimate observer-neighborhood/process-continuity calibration for H2;
2. a nontrivial analytic-closure square across an explicit rank-lowering map,
   including a red team where naive derivative commutation fails.

### 3.5 Universality claims remain strictly downstream

Free-object universality, classical universal covers, objectification
universality, and arithmetic geometric universality are distinct.  The finite
partition and cycle work strengthens the classification questions but does not
collapse these meanings.

## 4. API audit

### 4.1 Public surface that remains justified

The four namespace router remains appropriate:

```text
process_geometry.process
process_geometry.presentation
process_geometry.discovery
process_geometry.analysis
```

The public surface is strongest where names are qualified by implemented
semantics: literal histories, finite families, concrete presentations,
observable algebraic quotients, bounded task-continuation signatures,
presentation morphisms, and named A/M/algebraic/Abelian analysis languages.

### 4.2 Exact finite quotient remains Experimental

`FiniteTaskQuotient` has earned its strong name only inside the finite,
deterministic, finite-alphabet, hashable-observation class.  It therefore stays
under `process_geometry.experimental`.  This audit adds only executable helper
methods and makes its state-to-class certificate read-only; it does not broaden
the quantified domain.

### 4.3 Local canonical-observer records were in the wrong ownership layer

Before this audit, three explicitly experimental records were exposed through
the declared Public namespaces:

```text
presentation.canonicalization.ConstraintCanonicalization
analysis.connection.ObserverConnection
analysis.decomposition.CanonicalDecomposition
```

Their names are qualified, but their namespace ownership still suggested more
theory maturity than the map grants.  The implementation now lives at:

```text
process_geometry.experimental.ConstraintCanonicalization
process_geometry.experimental.ObserverConnection
process_geometry.experimental.CanonicalDecomposition
```

The historical module paths remain one-way 0.0.x compatibility shims and are
removed from `presentation.__all__` / `analysis.__all__`.  Stable source is
tested not to depend on Experimental ontology.

### 4.4 APIs deliberately not introduced

This audit rejects immediate classes named:

```text
ProcessGeometry
ObserverTopology
CanonicalHistoryLift
HistoryPayload
TaskCovariantComplexity
Objectification
ProcessRank
RankLowering
PartitionTower
ThermodynamicObjectification
```

Each would commit to a carrier or equivalence notion that the current evidence
has not uniquely selected.

## 5. Progress map after the audit

| Theory element | Current evidence | Code status | Judgment |
| --- | --- | --- | --- |
| H0 process/history | several exact concrete carriers | Public qualified APIs | healthy |
| H1 bounded distinction | exact bounded enumeration | Public qualified API | healthy |
| H1/V1 exact finite quotient | theorem anchor + exact refinement/witnesses | Experimental | correct boundary |
| H2 topology | precise threshold, no executable carrier | absent | intentionally deferred |
| H3 coding/frontier | exact finite shadows and lower bounds | Public concrete + research | do not call generic entropy |
| H4 analysis | strong A/M and Abelian model organisms | Public domain-specific APIs | generic foundation open |
| V0 free generation | several concrete grammars | Public concrete APIs | healthy |
| V2--V4 rank transition | two arithmetic calibrations + geometric pressures | research-local | generic API premature |
| V5 analytic closure | finite/infinitesimal A/M bridge only | absent generically | next major vertical gate |
| task-covariant evaluation | T0/T1 cross-problem evidence and exact local identities | research-local | candidate transversal, not Core |

## 6. Theory Impact

**Theory position:** H1/V1 exact finite slice and H4 local canonical-observer
calibrations; the audit also records a candidate transversal evaluation layer
across H3/H4 and V2/V5.

**Maturity:** unchanged.  No T-status or structural role is promoted.

**Semantic claim:** namespace ownership now matches the existing Theory Map:
only the exact finite quotient uses the strong task-quotient name, and unsettled
canonical-observer records are visibly Experimental.

**Non-claim:** the refactor does not establish a generic observer connection,
canonicalization theory, canonical decomposition, resource bundle, history
payload, topology, objectification, or rank-lowering framework.

**Evidence:** foundation notes 42--45; naming/alignment audits 48--49; exact
finite quotient implementation; arithmetic V1--V4 calibrations; pendulum,
stochastic, Noether, coarea, thermodynamic, and holonomy red teams through note
63.

**Map effect:** clarify and connect only.  The two-axis mother picture remains;
the task-covariant evaluation layer is recorded as an emerging transversal and
not inserted as a stable node.

**Migration risk:** low.  Historical import paths remain identity-preserving
shims during 0.0.x, while new repository code uses the Experimental owner.

## 7. Recommended research order

1. Complete the frozen PCR3BP return--partition--holonomy contract and test
   presentation covariance under both gate systems.
2. Extract from it the smallest typed history-payload/evaluation diagram that
   survives scalar and twisted tasks; keep it research-local until an
   independent system agrees.
3. Run one genuine H2 observer-neighborhood calibration with a continuity red
   team.
4. Return to V5 only with an explicit rank pair, lowering map, variation
   objects, and a corrected commutation law.
5. Consider a new Experimental abstraction only when one of these tests forces
   a repeated interface that cannot be expressed by existing concrete APIs.

This order preserves the first-principles picture while allowing engineering
to follow evidence rather than lead it.

## 8. Effective-analysis correction

The audit's two-axis verdict remains valid, but it underweighted a defining
selection pressure: Process Geometry is intended to preserve the symbolic and
numerical effectiveness that makes classical calculus useful in science and
engineering.

This does not add a third ontology axis.  It adds a cross-cutting admissibility
condition:

```text
analysis-bearing presentation
  = task-semantic adequacy
  + symbolic effectiveness
  + numerical effectiveness where claimed
  + explicit certificates and failure semantics
  + task-relative cost accounting
  + compatible lift / quotient / lowering transport
```

The correction strengthens rather than weakens the conservative API judgment.
It does not imply that every process has a differential calculus or that one
generic analysis carrier has been found.  Instead it prevents abstract
existence, one-backend simplification, one-point numerical agreement, or free
accounting of an objectified primitive from being mistaken for a mature
analysis claim.

Canonicalization remains local and observer/task-relative; effective analysis
supplies another selection criterion, not a global representative theorem.
Lift-first now protects computational payload such as derivatives, adjoints,
phase, branch, error, and holonomy as well as topological information.  The
unit/ruler is part of numerical tolerance and cost semantics.  V5 analytic
closure is correspondingly stratified into formal, certified, and effective
levels.

The governing contract and engineering gates are recorded in
`65-effective-analysis-principle.md`.  This addendum refines the research
program and review policy without changing the T-status or runtime API audited
above.
