# Process Geometry — living theory map

**Status:** evolving research map. This document is a navigation and review aid, **not** a frozen mathematical specification and **not** a public API contract.

## 0. Why this document exists

Process Geometry is developing through mathematics, executable calibrations, Sonnets, and software at the same time. That creates a specific engineering risk: a useful local implementation can acquire a generic name and API shape before the underlying theory has settled, and compatibility pressure can then freeze an accidental ontology.

This document exists to prevent that failure mode.

It records the **current larger theoretical picture** against which implementation and API changes should be interpreted. It is intentionally revisable. A later experiment may split a node, merge two concepts, reject a proposed layer, or show that the current arrows are wrong.

The governing distinction is:

```text
Theory Map        evolving account of what the framework may mean
Public API        durable semantic commitments already earned
Experimental      executable candidates testing parts of the map
Sonnets           problem-driven sources of pressure and counterexamples
```

An API should be reviewed **against** the Theory Map, but the API must never be treated as evidence that an unsettled part of the Theory Map has thereby become true.

The current foundation is developed primarily in:

- `42-process-geometry-from-distinguishability.md`
- `43-myhill-nerode-and-the-topological-threshold.md`
- `44-objectification-semantic-compression-and-rank-lowering.md`
- `45-lineage-objectification-and-analytic-closure.md`
- `48-foundation-naming-audit.md`
- `49-theory-implementation-structural-alignment.md`
- `50-aeg-translation-objectification-rank-lowering.md`

Those notes contain the argument and structural audits. This file is the compact map used for engineering review.

---

## 1. Current mother picture

The theory currently has two complementary axes.

```text
                                VERTICAL
                  ontology growth / process rank

Sigma_r
   |
   v
free process histories H_r
   |
   v
semantic compression under declared semantics
   |
   v
stable semantic classes C_r
   |
   v
objectification
   |
   v
Sigma_(r+1)  -----> free higher-rank composition
   ^                         |
   |                         |
   +---- compositional ------+
         rank lowering


HORIZONTAL at each rank

process/history
   |
   v
observer/task distinguishability
   |
   +-------------------------------+
   |                               |
   v                               v
exact continuation-stable          finite-resolution / local
semantic equivalence               distinguishability
   |                               |
   v                               v
task/process quotient              topology / locality
   |                               |
   v                               +--> continuity / boundary / covering
minimal or task-sufficient         +--> entropy / intrinsic complexity
presentation                       +--> metric/uniform structure when justified
                                   +--> differential/connection structure when justified
```

The map is deliberately not a single mandatory pipeline. A finite discrete process may stop at an exact quotient. A symbolic dynamical system may naturally reach entropy. A continuous process may support differential structure. A higher-rank language is not legitimate merely because a new symbol was introduced: its legal compositions must remain grounded by rank-lowering semantics.

---

## 2. Horizontal axis — distinguishability geometry

### H0 — Process and history

**Question:** What primitive operations, transitions, histories, and continuations exist before a representation is chosen?

Current software has strong concrete support here through `process.history`, `process.finite`, and `process.local`.

**Maturity:** implemented in several concrete forms; no claim of one universal `Process` protocol.

### H1 — Exact task/future distinguishability

**Question:** Which histories or states are indistinguishable under every declared task-relevant continuation?

The canonical exact calibration is Myhill–Nerode:

\[
\text{future distinguishability}
\to
\text{continuation-stable quotient}
\to
\text{minimal DFA presentation}.
\]

The public `TaskContinuationSignature` machinery remains a **bounded finite witness** for this idea: it compares all continuations only through a declared finite depth.

The Experimental namespace contains a narrower but exact finite slice:

```text
process_geometry.experimental.FiniteTaskQuotient
process_geometry.experimental.minimize_finite_task_process
```

For a finite deterministic state carrier with a finite step alphabet and a total task observation, stable partition refinement computes the coarsest equivalence preserving the task under **all** finite continuations. The quotient carries an induced deterministic transition, and every pair of distinct quotient classes is accompanied by an explicit distinguishing continuation.

This exact finite slice does **not** establish a generic quotient/minimization framework for infinite, nondeterministic, probabilistic, continuous, approximate, or resource-bounded processes.

**Maturity:** theorem-level classical anchor; bounded public witness; exact finite Experimental implementation.

### H2 — Topological threshold

**Question:** When do finite-resolution distinctions form stable local neighborhoods, and when is process evolution compatible with them?

Topology is not assumed for every process. It becomes justified only when observer neighborhoods satisfy suitable refinement/locality conditions. Stronger structures such as uniformity, quasi-uniformity, metric structure, or separation axioms may or may not be present.

The exact finite H1 quotient does not by itself provide locality or topology.

**Maturity:** foundational research program; no generic topology API.

### H3 — Entropy and intrinsic complexity

**Question:** How quickly do task-relevant or robust distinctions grow under process continuation, and what lower bounds does that impose on any adequate presentation?

This layer connects topological/metric entropy, coding, history growth, and the proposed distinction between intrinsic complexity and implementation overhead.

Current `BoundaryProfile`/Huffman machinery provides useful finite growth and coding calibrations, but no generic Process Geometry entropy object or intrinsic-complexity lower-bound contract exists.

**Maturity:** classical anchors and concrete coding shadows exist; Process Geometry correspondence remains a research question.

### H4 — Analysis of variation

**Question:** Once locality and suitable regularity exist, how should variation, derivatives, flows, observer paths, connections, and global analytic structure be expressed in the process-native presentation?

AEG is the first major model organism because its arithmetic process structure naturally developed into function theory and analysis rather than remaining a discrete hierarchy.

Current `analysis.*` modules implement important concrete languages; `ObserverConnection` and canonicalization work are experimental slices, not a universal theory.

**Maturity:** strong domain-specific implementation plus developing general theory.

---

## 3. Vertical axis — semantic compression and ontology growth

### V0 — Free generation

Given primitive vocabulary \(\Sigma_r\), legal histories/composites are generated with as little accidental quotienting as the domain permits.

Current history, grammar, rewrite, and construction machinery provide several concrete realizations.

**Maturity:** implemented in multiple bounded/concrete forms.

### V1 — Semantic compression

Histories or states may be identified only relative to declared semantics. This is stronger than syntactic simplification, common-subexpression elimination, or short coding.

`FiniteTaskQuotient` fully realizes this idea in the finite deterministic class. The signed-translation calibration adds a complementary infinite algebraic example: free `S/P` histories are identified by exact net displacement, and this equivalence is stable under every continuation because

\[
q(hk)=q(h)+q(k).
\]

Other repository mechanisms—rewrite normalization, observable elimination, finite coding, and ordinary primitive proposals—remain distinct and should not be called semantic compression unless their declared semantics justify the identification.

**Maturity:** exact finite Experimental implementation plus concrete arithmetic research calibration; no generic semantic-compression abstraction across process classes.

### V2 — Objectification

A stable lower-rank semantic process becomes a new reusable primitive.

This is **not** satisfied by `PrimitiveProposal` alone. A proposal is only a candidate. Objectification matters when the new object participates in a new compositional language.

The first concrete calibration now exists in the Addition/translation model organism. A signed unit-history class with net displacement \(n\) is promoted to a research-local translation primitive

\[
T_n:x\mapsto x+n.
\]

The primitive denotes the lower semantic class, not one particular `S/P` history. The calibration is deliberately research-local and does not establish a generic objectification API.

**Maturity:** first concrete AEG/Addition research calibration; generic V2 theory remains a research program and has no Experimental/Public abstraction.

### V3 — Higher-rank free composition

The objectified primitive opens legal combinations not merely enumerated in the discovery examples.

In the signed-translation calibration, retained primitives such as \(T_2\) and \(T_{-1}\) are placed in a new free `ProcessWord` language. Composites such as

\[
T_2T_2T_{-1}
\]

produce translation by \(+3\) without requiring \(T_3\) to have been supplied as a retained seed.

This is the generative gain that distinguishes ontology growth from memoization. The example is intentionally only the successor-history -> Addition/translation abstraction step; it does not yet realize Addition -> Multiplication.

**Maturity:** first concrete research calibration plus arithmetic/hyperoperation theoretical lineage; no generic higher-rank grammar API.

### V4 — Compositional rank lowering

Every legal higher-rank composite must admit coherent interpretation in an explicitly declared lower-rank semantic domain:

\[
\llbracket A\circ_{r+1}B\rrbracket
\simeq
\llbracket A\rrbracket\star_r\llbracket B\rrbracket.
\]

Generator-by-generator expansion is insufficient. Relations must lower soundly as well.

The signed-translation calibration provides the first concrete executable instance. Each \(T_n\) lowers to a canonical `S/P` word; lowering extends by concatenation to every legal higher-rank word; arbitrary generated terms preserve exact translation semantics; and relations such as

\[
T_mT_n\equiv T_{m+n}
\]

remain valid after lowering to the lower semantic quotient.

A red team using only absolute displacement shows why terminal compression is insufficient: \(S\) and \(P\) appear equal under \(|q|\), but continuation by \(S\) separates them.

**Maturity:** first complete concrete V4 research calibration; no generic Experimental/Public rank-lowering interpretation object.

### V5 — Cross-rank closure

When additional horizontal structure exists, stronger compatibility can be asked:

- **semantic closure** — compositional lowering;
- **topological closure** — continuous lowering between induced geometries;
- **analytic closure** — coherent comparison of local variation across ranks.

The translation calibration establishes only the semantic V4 layer. It does not yet supply a meaningful cross-rank differential comparison.

**Maturity:** research hypotheses / program.

---

## 4. Cross-axis roles of the current software layers

The existing public pipeline remains useful, but it should be read as an engineering decomposition rather than the entire ontology:

```text
Process -> Presentation -> Discovery -> Analysis
```

### Process

Carries concrete primitive dynamics, histories, finite actions, and local realizations.

### Presentation

Carries explicit, auditable realizations: rewriting, constraints, generated grammars, relations, task-sufficiency evidence, morphisms, and costs.

A presentation may realize an exact quotient, a local geometry, an algebraic observable image, a code, or another task-sufficient structure. The word does not imply that all Process Geometry has already been reconstructed.

### Discovery

Searches candidate observables, presentations, languages, quotients, or structures. Discovery algorithms are proposal mechanisms, not ontology.

### Analysis

Provides mathematical languages for variation and global structure supported by successful presentations.

### Experimental

Hosts explicitly unstable theory-to-code probes. Experimental is not a fifth stable ontology layer and is never re-exported from the package root merely because an experiment works.

The exact finite task quotient is the first Experimental probe added specifically to close a Theory Map implementation gap rather than to support one named classical problem. The first V2–V4 calibration remains research-local rather than entering Experimental after only one domain.

---

## 5. AEG and Arithmetic Universality

AEG has two roles that must remain distinct.

First, it is the current **model organism** for Process Geometry:

- the signed-translation calibration now makes one objectification/rank-lowering step executable;
- the arithmetic/hyperoperation tower motivates further rank raising, especially Addition -> Multiplication;
- A/M and related work display a native language of variation and analysis;
- the same lineage therefore pressures both the vertical and horizontal axes.

Second, a stronger conjecture asks whether arithmetic-generated geometries provide universal covers or standard models for a much broader class of process geometries.

That second claim is **not** part of the definition of Process Geometry and is not assumed by the software.

```text
Process Geometry                    general evolving framework
AEG                                 first major model organism
Arithmetic Geometric Universality   stronger open conjecture
```

---

## 6. Maturity vocabulary for theory-to-code review

Every substantial proposed abstraction should be located using one of these states:

| State | Meaning |
| --- | --- |
| **classical anchor** | established external mathematics used as calibration |
| **implemented concrete** | executable structure with deliberately local semantics |
| **calibrated candidate** | implementation has survived meaningful examples/red teams but is not generic |
| **experimental abstraction** | explicitly generalized candidate under repository governance |
| **public commitment** | promoted semantic API contract |
| **research hypothesis** | plausible theoretical structure not yet earned by implementation/evidence |
| **open conjecture** | stronger claim whose truth is not assumed by the framework |

A code symbol and a theory node need not have the same maturity. For example, a concrete `ObserverConnection` class can exist while the general observer-connection theory remains experimental. Likewise `FiniteTaskQuotient` can be exact in its finite deterministic class while the general theory of task quotients remains broader and unsettled. The V2–V4 signed-translation example can be a complete concrete calibration while `Objectification` and `RankLowering` remain intentionally absent as package abstractions.

---

## 7. Mandatory theory-impact questions for API review

Any change that adds, renames, generalizes, promotes, or materially changes an Experimental or Public API should include a short **Theory Impact** section in its PR/AEP/promotion note.

It must answer:

1. **Theory position** — Which node or arrow in this map does the API represent or test?
2. **Maturity** — Is that theory element a classical anchor, concrete implementation, calibrated candidate, experimental abstraction, public commitment, hypothesis, or open conjecture?
3. **Semantic claim** — What mathematical meaning does the API name/signature commit to?
4. **Non-claim** — Which nearby stronger interpretation is explicitly *not* being claimed?
5. **Evidence** — Which independent domains, certificates, or red teams justify this level of generality?
6. **Map effect** — Does the result support, refine, split, contradict, or leave unchanged the current Theory Map?
7. **Migration risk** — If the Theory Map changes later, can this API evolve without forcing the repository to preserve a known-wrong ontology?

For a purely mechanical change, the answer may be one sentence: “No theory position changes; this preserves the existing semantic contract.”

For a new foundational abstraction, absence of a meaningful Theory Impact section is itself evidence that the API is premature.

---

## 8. Review rule: theory may evolve; API claims must stay narrower

The Theory Map is expected to change. Therefore engineering review should enforce the asymmetry

```text
API semantic commitment  <=  evidence-backed portion of the evolving theory
```

and never the reverse.

A useful implementation may be merged without promoting its most ambitious theoretical interpretation. Conversely, a compelling theoretical note does not justify a public class until executable cross-domain evidence and governance gates are satisfied.

When theory and code disagree, record the disagreement explicitly. Do not silently rename one side until the mismatch disappears on paper.

---

## 9. Current high-value structural questions

Two narrow implementation questions have now been answered:

1. bounded `TaskContinuationSignature` can be complemented by an exact/minimized task quotient in the finite deterministic class;
2. a complete V1 -> V4 cycle can be realized concretely for signed unit histories objectified as Addition/translation primitives, including continuation congruence, new free composition, compositional lowering, relation soundness, and a negative control.

The next high-value questions are:

1. can Addition/translation objects themselves be reorganized by a genuinely multiplicative/dilation process so that **Addition -> Multiplication** becomes an explicit second rank transition rather than another translation relation?
2. what is the correct lower semantic target for that multiplicative rank—translation objects, endomorphisms of the translation process, or a richer A/M presentation?
3. can every free higher-rank multiplicative composite lower compositionally, including the noncommutative translation/dilation interaction forced by AEG?
4. only after that, does the existing A/M calculus supply a first convincing V5 **analytic closure** diagram across explicit ranks?
5. independently, what concrete observer-neighborhood object is the smallest legitimate H2 topological-threshold experiment?
6. can exact task quotients plus `BoundaryProfile`/Huffman separate intrinsic distinguishability complexity from realization overhead in a calibration where both are independently known?
7. which current `PresentationMorphism` semantics survive when used between ranks rather than only between presentations at one level?

These are research questions, not a backlog of API classes to create.

---

## 10. Standing interpretation

The current compact statement is:

> **Process Geometry studies how process histories are generated, distinguished, semantically compressed, presented, and—when justified—objectified into new compositional ranks, together with the topological, complexity, and analytic structures induced within and between those ranks.**

This sentence is a working research orientation. Its purpose is to keep engineering choices legible inside the larger mathematical program while leaving the mathematics free to improve.
