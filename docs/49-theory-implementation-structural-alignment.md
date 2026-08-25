# Theory–Implementation Structural Alignment

**Status:** structural audit against `docs/THEORY_MAP.md`; this note distinguishes exact implementations from calibrated shadows and missing semantics. It does not promote new Public API.

## 0. Purpose

The naming audit in `48-foundation-naming-audit.md` established a vocabulary discipline. The next question is deeper:

> Which parts of the current Process Geometry theory are actually implemented, which are only approximated by existing code, and which do not yet exist in executable form?

This note uses the living Theory Map as the sole organizing frame. It deliberately avoids the reverse mistake of treating the existing package layout as ontology.

The status vocabulary is:

- **implemented concrete** — executable semantics match the local theory claim;
- **calibrated shadow** — code exhibits an important projection of the theory but does not satisfy the full definition;
- **partial** — some required semantics are executable, but a defining condition is missing;
- **absent** — no current code object has the required semantics;
- **deferred by design** — intentionally absent pending more cross-domain evidence.

The original audit found strong literal process generation and domain-specific
analysis, with a gap in the middle and on the vertical bridge.  The first narrow
part of that gap has since closed: exact finite deterministic task quotienting
now exists under Experimental.  Topology, generic objectification, and
rank-lowering remain absent:

```text
strong            exact finite slice        strong
Process/history -> task quotient -> H2/... -> Analysis
                         Experimental   ^
                                        |
                                  current gap

Vertical:
free generation -> semantic compression -> objectification -> higher rank -> lowering
      strong        exact finite slice          absent           absent        absent
                         + partial shadows
```

This shape explains why recent Sonnets repeatedly discover good local representations but still need problem-specific glue to turn those discoveries into a general ontology-growth mechanism.

---

## 1. Alignment matrix

| Theory node | Current implementation | Status | Missing defining semantics |
| --- | --- | --- | --- |
| **H0 Process/history** | `ProcessWord`, `interpret_history`, `ProcessFamily`, `ProcessSystem`, `ProcessFrame` | **implemented concrete** | no universal Process protocol, intentionally |
| **H1 exact task/future distinguishability** | bounded `TaskContinuationSignature`; exact finite `FiniteTaskQuotient` | **implemented concrete in the finite deterministic class** | no exact framework for infinite, nondeterministic, probabilistic, continuous, approximate, or resource-bounded processes |
| **H1 task/process quotient** | `process_geometry.experimental.FiniteTaskQuotient` | **exact narrow Experimental slice; absent generically** | broader process classes, topology, and a cross-class quotient protocol remain open |
| **H2 topology/locality** | none in generic package | **absent** | observer neighborhoods, refinement law, process continuity |
| **H3 entropy/intrinsic complexity** | `BoundaryProfile`, `PrefixCodeMetrics`, Huffman code | **calibrated shadow** | no dynamical open-cover/separated-set entropy; no intrinsic lower-bound object tied to task quotient |
| **H4 analysis of variation** | `ProcessSystem`, `ProcessFrame`, A/M calculus, Abelian history/period layers; Experimental canonical-observer records | **strong domain-specific / partial general** | no generic locality/tangent/jet foundation; no observer-induced differential structure |
| **V0 free generation** | `ProcessWord`, continuation enumeration, `PrimitiveConstruction`, generated grammar search | **implemented concrete in several forms** | no single generic free-construction abstraction, intentionally |
| **V1 semantic compression** | exact finite task quotient plus rewrite relations, bounded signatures, and problem-local quotients | **implemented concrete in one narrow class; partial otherwise** | no generic semantics object or quotient across process classes |
| **V2 objectification** | `PrimitiveProposal`, relation decomposition primitives | **calibrated shadows only** | no objectification gate, no new process rank, no proof of semantic stability + reuse |
| **V3 higher-rank free composition** | symbolic construction trees compose caller operations | **shadow, not rank semantics** | no explicit rank boundary or grammar whose generators are objectified lower-rank semantics |
| **V4 compositional rank lowering** | `PairingSpec.lower` and backend decoders are local lowering-like mechanisms | **absent at theory level** | interpretation defined on every legal higher-rank composite and relation-soundness certificate |
| **V5 cross-rank closure** | A/M suggests analytic compatibility; no generic structure | **research hypothesis** | semantic/topological/analytic comparison across explicit ranks |
| **Presentation bridge** | `PresentationMorphism` | **public calibrated tool** | no composition/identity; not yet an inter-rank semantic interpretation |

---

## 2. H0 — process and history are genuinely implemented

`process.history.ProcessWord` is one of the cleanest theory/code correspondences in the repository.

It stores ordered steps without prematurely interpreting them. Composition is literal concatenation, while `interpret_history` supplies semantics separately. This respects the foundational order

\[
\text{free/literal history first} \to \text{interpretation later}.
\]

`process.finite` and `process.local` add two concrete process realizations:

- finite parameterized actions and cocycles;
- local differential generators and frames.

These are not one universal `Process` object, and that absence is currently healthy. The theory does not yet justify one protocol that would cover words, finite actions, rewrite systems, ODE flows, and higher-rank languages without erasing important differences.

**Alignment judgment:** no generic H0 refactor is needed now.

---

## 3. H1 — bounded and exact-finite distinguishability are now separated

`TaskContinuationSignature` computes

\[
S_Q^k(h)=\bigl(Q(hw)\bigr)_{w\in\Sigma^{\le k}}
\]

for every allowed continuation through a finite depth. `histories_task_equivalent` therefore implements a genuine bounded future-distinguishability predicate.

This is stronger than current-state equality, but weaker than the exact relation

\[
h_1\sim_Q h_2
\iff
\forall w\in\Sigma^*,\;Q(h_1w)=Q(h_2w).
\]

The Experimental `FiniteTaskQuotient` now closes the finite deterministic
version of the earlier gap.  Stable partition refinement:

1. computes the coarsest continuation-stable equivalence;
2. constructs the quotient state/process space;
3. records the induced task observation and deterministic transition;
4. returns a future continuation distinguishing every distinct class pair;
5. thereby certifies minimality in the Myhill–Nerode/Moore-machine sense.

The certificate is immutable at its public boundary, executable on arbitrary
finite continuations, and canonical only up to quotient isomorphism; numeric
class indices remain caller-order presentation artifacts.

The strong word `TaskQuotient` remains confined to this quantified class.  No
claim is made about topology or a universal quotient protocol.

**Alignment judgment:** the narrow H1 implementation gap is closed correctly
under Experimental; broader H1 and all of H2 remain open.

---

## 4. H2 — topology is genuinely absent, which is preferable to a fake API

A repository search finds no generic topology/neighborhood implementation corresponding to the topological threshold in `42–43`.

That is the correct status. Existing code has:

- exact/bounded observations;
- algebraic constraints;
- history prefix geometry;
- observer-selection mechanisms;
- continuous local systems.

But none of these alone supplies the required topological data:

\[
\mathcal N_O(x),
\]

with neighborhood refinement/local inheritance and compatibility with process evolution.

`ConstraintCanonicalization` and `ObserverConnection` are downstream local differential objects; they should not be retroactively interpreted as evidence that an observer topology already exists.

**Alignment judgment:** keep H2 absent until a concrete problem supplies a natural resource-indexed observer-neighborhood family.

---

## 5. H3 — history geometry is a useful entropy shadow, not topological entropy

`history_geometry.py` contains two important concrete structures.

### 5.1 Boundary growth

`BoundaryProfile` records frontier width by history depth and exposes

\[
\frac{\log N(d)}{d}.
\]

This is structurally close to distinguishability-growth ideas. But `boundary_profile` accepts an arbitrary `quotient_key`; it does not itself derive a task quotient or a topology, and it does not implement the orbit-cover definition of topological entropy.

### 5.2 Prefix coding

`PrefixCodeMetrics` computes Shannon entropy and Huffman redundancy for a finite weighted source. This is an exact coding-theory calibration of materialization cost.

The crucial theory gap is the bridge:

\[
\text{intrinsic task distinguishability}
\to
\text{lower bound on every sufficient presentation}
\to
\text{realization overhead}.
\]

The current `PresentationCost` is an explicit engineering multi-axis cost; it is not claimed to be intrinsic complexity.

**Alignment judgment:** H3 has strong classical shadows but no Process Geometry entropy object yet.

---

## 6. H4 — analysis is much stronger than the middle layers

The analysis side is already substantial.

### 6.1 Local process calculus

`ProcessSystem` / `ProcessFrame` support derivatives, iterated generators, and commutators.

### 6.2 A/M function theory

`AMFunctionTheory` realizes a nontrivial process-native calculus generated by Addition and Multiplication:

\[
A=\partial_a,
\qquad
M=\partial_v+a\partial_a,
\qquad
[A,M]=A.
\]

It includes finite process relations, resonant primitive construction, PBW-style identities, and path flows.

This is important evidence for the theory claim that a process-native ontology can naturally carry analysis rather than requiring an externally chosen linear/Fourier language.

### 6.3 Global Abelian/history analysis

The Abelian layer implements lifted histories, cycles, periods, period matrices, and normalized history quotients for calibrated algebraic processes.

### 6.4 Observer connection slice

`ConstraintCanonicalization -> ObserverConnection` implements a concrete local transport mechanism by differentiating a maintained observer condition.

But the general H4 theory remains incomplete because these layers are not derived from a generic observer-induced topology/locality structure. In particular, the package has no general tangent object, differential jet abstraction, or proof that a chosen observer topology induces the implemented calculus.

**Alignment judgment:** H4 is a strong family of model organisms, not a generic completed layer.

---

## 7. V0 — several good free-generation mechanisms already exist

The vertical tower starts from free or weakly free generation. The package already has several domain-appropriate realizations:

- `ProcessWord`: free ordered word composition;
- continuation enumeration: bounded free future tree;
- `PrimitiveConstruction`: free construction trees under caller-declared operations, with only explicit commutative quotienting;
- generated grammar search: closure under a concrete process generator;
- rewrite machinery: free words plus explicitly declared relations.

There is no need to force these into one generic `FreeProcess` API yet. Their differences are mathematically meaningful.

**Alignment judgment:** V0 is well represented concretely.

---

## 8. V1 — exact finite semantic compression has an owner

The repository contains many ways to reduce a representation:

- rewrite normalization;
- algebraic constraint reduction;
- generated finite spans;
- task-continuation signatures;
- observable elimination;
- presentation search and Pareto filtering;
- problem-local future-requirement antichains in Sonnets.

Only some are semantic compression in the theory sense.

A rewrite rule may be caller-declared without being task-derived. Algebraic elimination may preserve selected observables without establishing future task equivalence. Huffman coding may compress already-distinguished symbols but does not decide which histories may be merged.

Therefore most reduction mechanisms still must not be called semantic
compression.  The one exact generic owner in a declared class is
`FiniteTaskQuotient`, which realizes

\[
X\to X/{\sim_Q}
\]

for finite deterministic state carriers.  It does not absorb rewrite,
observable-elimination, approximate, continuous, or probabilistic compression
into one interface.

**Alignment judgment:** V1 is implemented concretely in one narrow class and
remains partial as a general theory.

---

## 9. V2 — `PrimitiveProposal` is deliberately below objectification

`PrimitiveConstruction` and `PrimitiveProposal` preserve construction provenance and allow bounded generation of candidate expressions. This is useful infrastructure for objectification discovery.

But a proposal currently lacks the defining gates of `docs/44`:

- stable task-relative semantics;
- continuation compatibility;
- promotion into a new primitive vocabulary;
- generative novelty at the next rank;
- compositional rank lowering;
- relation soundness.

Likewise relation decomposition can identify useful primitive components of a finite span, but this does not create a new semantic rank.

**Alignment judgment:** do not create an `Objectification` class by wrapping `PrimitiveProposal`. The gap is semantic, not nominal.

---

## 10. V3 — current construction trees are not yet higher-rank languages

`PrimitiveConstruction` already supports free recursive composition of caller-declared `SymbolicOperation`s. Superficially this resembles V3.

The essential missing fact is where those operations came from.

In V3, the generators of the new grammar must be objectified semantic processes from rank \(r\). The current construction grammar begins with caller-supplied operations and does not encode an explicit rank transition.

Therefore it is better classified as **free-construction infrastructure** that may later host V3, not as V3 itself.

---

## 11. V4 — local lowering-like functions exist, compositional lowering does not

The strongest near-miss is `PairingSpec.lower`: a structured observer construction is lowered to a scalar backend expression. Similar local decoder/interpretation functions appear elsewhere.

These are valuable precedents because they preserve a distinction between semantic construction and backend realization.

However V4 requires one map

\[
\llbracket-\rrbracket_{r+1\downarrow r}
\]

that is defined for **every legal higher-rank composite**, preserves the higher-rank composition semantics, and sends high-rank relations to valid lower-rank relations.

No current package object has this contract.

`PresentationMorphism` also cannot yet fill this role: it records one evidence-bearing transformation but deliberately has no composition law and does not interpret a whole higher-rank grammar.

**Alignment judgment:** V4 is absent, not merely hidden behind existing names.

---

## 12. V5 — A/M is the best candidate model organism for analytic closure

The repository already contains the right kind of evidence to formulate a first V5 calibration, but not enough to declare V5 implemented.

A/M supplies:

- finite process operations;
- infinitesimal generators;
- a noncommutative relation;
- a function language adapted to those generators;
- integration/resonance phenomena;
- path-flow evolution.

What is missing is an explicit **rank pair** plus a compositional lowering map between them. Without V4, one cannot yet ask rigorously whether differentiation/flow commutes with lowering across ranks.

Thus the next analytic-closure experiment should follow, not precede, a genuine rank-lowering calibration.

---

## 13. Cross-axis role of `PresentationMorphism`

`PresentationMorphism` is one of the strongest existing generic abstractions because it survived independent domains and explicitly records task-relative semantic evidence.

Its current semantics are nevertheless orthogonal to several Theory Map arrows.

It is **not yet**:

- a semantic quotient map;
- a topological continuous map;
- a rank-lowering interpretation;
- a functor between process ranks.

The class may later become part of those structures, but the current deliberate absence of composition is an important boundary.

A future inter-rank calibration should test whether rank lowering is best modeled as a specialized `PresentationMorphism`, a compositional family of morphisms, or a different interpretation object entirely.

---

## 14. Priority order after the audit

The audit changes the implementation priority.

### Completed foundation target — exact finite task quotient

Why first:

- exact classical theorem anchor;
- fills a real H1/V1 gap;
- sharpens the meaning of the reserved word `TaskQuotient`;
- produces a true minimal presentation in a finite class;
- supplies a baseline against which bounded `TaskContinuationSignature` can be measured.

Canonical home: `process_geometry.experimental`.

### Priority 1 — objectification + rank-lowering calibration in an independent domain

Do **not** first design a generic objectification API. Choose one domain in which:

1. a lower-rank semantic class can be promoted;
2. the promoted objects generate unseen composites;
3. every composite lowers compositionally;
4. relations lower soundly.

AEG arithmetic has now supplied two consecutive model-organism calibrations.
The next promotion pressure must come from an independent domain and remain
small enough that the entire lowering law can be checked.

### Priority 2 — topological threshold calibration

Choose a process/observer pair with a natural directed resource parameter and build the smallest neighborhood-basis experiment. The goal is not a generic `Topology` class; it is to verify the extra conditions that distinguish a topology from arbitrary tolerance relations.

### Priority 3 — intrinsic complexity versus realization overhead

Now that the exact finite task quotient exists, connect
`BoundaryProfile`/Huffman/Pareto cost to a true intrinsic state/distinction
lower bound in that same declared class before generalizing.

### Priority 4 — task-covariant evaluation carrier

Recent clock/resource/holonomy/coarea/partition work suggests a transversal
history-evaluation layer.  Determine the smallest carrier and information
contract through PCR3BP and an independent red team before any Experimental
API.

### Priority 5 — analytic closure

After a genuine rank-lowering example exists, test whether variation is compatible across ranks. A/M is currently the best candidate.

---

## 15. First executable alignment target — completed

The first alignment phase delivered one narrow experimental implementation:

> **Exact finite deterministic task quotient.**

Given a finite deterministic process

\[
(X,\Sigma,\delta,Q),
\]

compute the coarsest equivalence relation satisfying

\[
x\sim y
\iff
Q(\delta(x,w))=Q(\delta(y,w))
\quad\forall w\in\Sigma^*.
\]

The implementation returns:

- the equivalence classes;
- the induced quotient transition;
- the task observation of each class;
- an exact continuation witness distinguishing every pair of distinct classes;
- a refinement/fixed-point certificate sufficient to justify minimality in the finite deterministic setting.

This is the first case in which the package intentionally uses the strong term
**TaskQuotient**, because the executable object satisfies the Theory Map
definition in its declared finite class.

It remains Experimental because one exact finite class does not establish the
generic Process Geometry quotient abstraction.  The next conservative software
change is not another theory noun: it is keeping unsettled local
canonical-observer records under Experimental ownership.

---

## 16. Theory Impact

**Theory position:** H1 exact task/future distinguishability and V1 semantic compression.

**Maturity before this phase:** classical anchor plus bounded concrete witness.

**Semantic claim:** the proposed finite deterministic experimental object computes an actual continuation-stable semantic quotient, not a finite-depth approximation.

**Non-claim:** it is not a universal task quotient for infinite, nondeterministic, continuous, probabilistic, or resource-bounded processes; it does not imply topology.

**Evidence:** Myhill–Nerode/Moore minimization provides the exact external anchor; current `TaskContinuationSignature` supplies the bounded comparison case.

**Map effect:** H1 is refined from “bounded implementation only” to “bounded public machinery plus an exact finite Experimental slice.”

**Migration risk:** low because the implementation is explicitly finite/deterministic and lives under Experimental rather than occupying a universal root concept.
