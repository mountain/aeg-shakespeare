# Theory Map governance

**Status:** repository policy for developing and promoting mathematical theory.

**Required prior reading:** [`MATHEMATICAL_CORE.md`](MATHEMATICAL_CORE.md), then
[`ENGINEERING_ARCHITECTURE.md`](ENGINEERING_ARCHITECTURE.md). The Mathematical
Core carries the present objects, constructions, laws, and boundaries; the
Engineering Architecture carries the problem-to-solver technical decisions;
the Theory Map and this policy locate, grade, and govern the theory.

Process Geometry needs two different kinds of freedom at the same time:

- research must be free to propose beautiful, incompatible, and even wrong theories;
- the stable theory map must be conservative enough that explanatory enthusiasm does not silently become ontology.

This document governs the second problem. It complements [`GOVERNANCE.md`](GOVERNANCE.md), which governs the path from problem-driven research to Experimental and Public API commitments.

The governing principle is:

> **Ideas may move quickly. The stable theory map moves slowly.**

Or, more operationally:

```text
free exploration
    -> mathematical reconstruction
    -> precise claim
    -> cross-problem calibration
    -> structural law
    -> core theory
```

A theory may run far ahead of implementation. Implementation, especially Public API, should normally lag behind theory promotion.

---

## 1. Eight standing principles

Theory-map review is governed by eight rules.

### G1 — Mathematical content before map placement

The Theory Map is an index, not the carrier of the full mathematics. Before a
substantial node or arrow is proposed, its primitive data, construction,
law/obstruction, information contract, covariance and unit semantics where
relevant, scope, reconstruction boundary, and evidence must be recoverable in
the Mathematical Core or a linked theory record.

A new noun or an untyped arrow is not yet a mathematical contribution to the
stable map.

When the claim is computational, its algorithm, evaluator, certificate,
error/failure semantics, units, decoder, baseline, and budget must also be
recoverable under the Engineering Architecture. An abstract existence claim
and a feasible solver claim are different maturities.

### G2 — Free proposal, conservative promotion

Research notes and Sonnets may contain speculative, competing, or mutually incompatible explanations. Entry into the stable theory map is a separate act requiring explicit evidence and scope.

### G3 — Nodes may be suggestive; edges must be audited

A map of attractive nouns is not a theory. The principal unit of review is an arrow

\[
A \longrightarrow B,
\]

because the arrow carries assumptions, information loss, invariants, reconstruction obligations, and the sense in which a construction is claimed to be canonical.

### G4 — Strong words create proof obligations

Words such as **canonical**, **universal**, **intrinsic**, **natural**, **forced**, **minimal**, **complete**, and **fundamental** must be qualified by a mathematical meaning. A strong name is not a substitute for a uniqueness theorem, universal property, invariance statement, or stated optimization criterion.

### G5 — New primitives require a forced distinction

A new foundational object is justified only when existing theory cannot express a distinction that is repeatedly forced by mathematics or independent calibrations.

Beautiful abstraction is not sufficient pressure.

### G6 — Every substantial claim has a falsification interface

A theory record must state what observation, counterexample, degeneration, or incompatibility would kill or materially weaken the claim.

### G7 — Mature theory should compress the map

Promotion is justified when a theory removes accidental distinctions, replaces several local explanations by a smaller structural account, or exposes a reusable obstruction/completion principle.

A theory that mainly enlarges the vocabulary is presumed immature.

### G8 — Analysis claims must remain effectively calculable

Process Geometry must not gain generality by abandoning the operational
strength of calculus.  When a node or edge claims an analysis language, it must
state how symbolic operations and/or numerical evaluation are actually
performed, certified, bounded, and costed.

This rule is conditional rather than universal.  A discrete semantic quotient
may legitimately make no differential claim.  An abstract differential,
integral, variational, or closure object does not by itself justify the words
`analysis`, `computable`, `stable`, or `efficient`.

---

## 2. Two orthogonal labels

Every substantial theory-map entry should carry two independent labels.

### 2.1 Epistemic maturity

| Level | Name | Meaning |
| --- | --- | --- |
| **T0** | Sketch / Playground | Suggestive observation, analogy, or incomplete construction. Contradictions are allowed. |
| **T1** | Precise Conjecture | Inputs, outputs, scope, equivalence notion, and falsification conditions can be stated precisely. |
| **T2** | Calibrated Structure | The same structural claim survives multiple meaningful calibrations, including a negative, adversarial, or degenerate case. |
| **T3** | Structural Law | The claim is supported by an abstract theorem, universal property, classification, functorial statement, or obstruction result that no longer depends on the motivating example. |
| **T4** | Core Theory | Stable foundational structure with clear definitions, nontrivial theorem-level support, cross-domain evidence, explicit failure domain, and demonstrated value as a dependency for other theory. |

Promotion is not monotone by prestige. A theorem about a problem-local object may remain local; a foundationally important conjecture may remain T1 for a long time.

### 2.2 Structural role

Independently record one of:

- **local** — explains one problem family or one constrained setting;
- **reusable** — has a stable role across independent settings;
- **foundational** — proposed as part of the framework's mother structure.

For example, a claim can be `T1 / foundational candidate` or `T3 / local`. These are not contradictions.

### 2.3 Evidence provenance is separate again

The existing vocabulary in [`THEORY_MAP.md`](THEORY_MAP.md)—for example `classical anchor`, `implemented concrete`, `calibrated candidate`, `experimental abstraction`, `public commitment`, `research hypothesis`, and `open conjecture`—describes evidence provenance or theory-to-code state.

Do not collapse that vocabulary into T0–T4.

A useful theory record may therefore say:

```text
Epistemic maturity: T2
Role: reusable
Evidence: classical anchors + implemented concrete calibrations
Code status: research-local
```

---

## 3. Promotion gates

Promotion is explicit. Mere age, repetition, implementation, or popularity does not promote a theory.

### T0 -> T1: precision gate

A sketch may become a precise conjecture only when it states:

1. input objects and required structure;
2. output objects;
3. scope/domain of validity;
4. equivalence notion;
5. preserved information or invariants;
6. forgotten information;
7. at least one kill condition.
8. if analysis or computational advantage is claimed, the applicable symbolic,
   numerical, certification, unit, and cost contract.
9. its relation to the Mathematical Core: reused or changed objects,
   construction, law/obstruction, information contract, and boundary.
10. if the claim is computational, its Engineering Architecture relation:
    algorithm, evaluator, certificate, failure/error semantics, units,
    decoder, baseline, budget, dependency, and cost.

### T1 -> T2: calibration gate

Default requirement:

- at least two genuinely informative positive calibrations; and
- at least one negative control, adversarial case, degeneration, or nearby example where the stronger claim must fail or change form.

The useful heuristic is:

> **One example creates a conjecture. Two examples create a pattern. Positive evidence plus a boundary creates structure.**

Several parameter choices inside one solver ontology do not count as independent evidence.

For an effective-analysis claim, the calibration gate is also claim-relative:

- symbolic claims require exact relations, closure/controlled-extension
  evidence, or independently checkable residuals;
- numerical claims require a stated domain, scale-aware error or convergence
  evidence, and a failure case;
- efficiency claims require a declared workload, baseline, and accounting for
  discovery/compilation, storage, dictionary, residual, and decoding costs;
- covariance or rank-closure claims require a transport/round-trip red team.

### T2 -> T3: abstraction gate

At least one result must cease to depend on the motivating examples. Normal forms include:

- theorem;
- universal property;
- classification result;
- functorial or naturality statement;
- uniqueness result under declared equivalence;
- precise obstruction theorem.

### T3 -> T4: foundation gate

Core promotion is exceptional. It normally requires:

- stable definitions;
- at least one nontrivial theorem-level result;
- independent pressure from more than one mathematical domain;
- explicit failure domain;
- compatibility with neighboring core claims;
- evidence that other theory becomes smaller or clearer by depending on it.

**Default rule:** a new concept does not enter Core merely because it is elegant or broadly worded.

### Demotion

T-status can move downward. A counterexample, better equivalence notion, or revised dependency graph may demote, split, or retire a theory node. Demotion is a normal research outcome and should leave an auditable record.

---

## 4. Theory Node Contract

Every material node added to the stable theory map should answer the following fields, directly or by reference to a theory record.

```text
Name:
Epistemic maturity: T0 | T1 | T2 | T3 | T4
Role: local | reusable | foundational

Mathematical Core relation:
Primitive data:
Construction(s):
Law / obstruction:
Engineering Architecture relation, if computational:

Definition / claim:
Dependencies:
Scope:
Equivalence notion:

Preserves:
Forgets:

Positive calibrations:
Negative controls:
Adversarial cases:
Degenerations:
Known counterexamples:

Claim classes:
  theorem:
  conjecture:
  interpretation:

Open obligations:
Kill conditions:
Promotion criteria:
Code/API status:

Effective-analysis contract, if claimed:
  symbolic mode / closure:
  numerical mode / error and failure semantics:
  units / ruler:
  certificates:
  baseline / cost boundary:
  lift / lowering compatibility:
```

A node that cannot distinguish theorem, conjecture, and interpretation is not ready for stable-map promotion.

---

## 5. Theory Edge Contract

The stable theory map treats arrows as first-class mathematical commitments.

For an arrow

\[
A \xrightarrow{F} B,
\]

record:

```text
Source:
Target:
Operation / construction:
Required structure:

Information forgotten:
Invariant or semantics preserved:
Canonicality claim:
Equivalence notion:

Decoder / reconstruction:
Local or global:
Obstruction to globalization:

Evidence:
Failure cases:
Kill conditions:

Effective-analysis transport, if claimed:
Symbolic evaluator / certificate:
Numerical evaluator / error semantics:
Unit / scale transport:
Cost transport:
```

In particular, a map arrow must not silently identify the following distinct situations:

- quotient versus choice of representative;
- local coordinate versus global coordinate;
- algebraic image versus task-semantic quotient;
- representation refinement versus forced completion;
- state reconstruction versus history reconstruction;
- existence versus uniqueness;
- uniqueness versus uniqueness only up to an equivalence relation.

The pendulum and observer-quotient work already show why these distinctions matter: an algebraically correct quotient may forget a discrete state branch, while an Abelian clock may exist locally but acquire a period obstruction globally.

---

## 6. Controlled theoretical vocabulary

The following words are **controlled vocabulary** in foundational theory and promotion records.

| Word | Minimum required qualifier or evidence |
| --- | --- |
| `canonical` | relative to what data, and unique in what sense? |
| `universal` | a stated universal property, quantified universality claim, or clearly marked conjecture |
| `intrinsic` | invariant under which presentation/coordinate/gauge changes? |
| `natural` | natural with respect to which morphisms or transformations? |
| `forced` | what failure, obstruction, or minimality argument excludes alternatives? |
| `minimal` | minimal under which preorder, cost, dimension, information criterion, or universal property? |
| `complete` | complete for which task/semantics/category of inputs? |
| `fundamental` | a role earned by dependencies and compression of the map, not rhetorical importance |
| `computable` | an algorithm and quantified input domain; distinguish decidable, executable, and tractable |
| `exact` | the equality/semantics and arithmetic domain in which exactness holds |
| `stable` | a perturbation/error model, scale, domain, and bound or convergence evidence |
| `efficient` | a declared baseline, workload, cost model, and asymptotic or measured scope |

Preferred forms include:

```text
canonical relative to the declared observer grammar
canonical up to birational equivalence
locally canonical
canonical by a stated universal property
minimal under PresentationCost
forced by failure of closure in the restricted language
```

Unqualified use is acceptable in informal T0 notes, but not in T2–T4 map commitments unless the meaning is already fixed locally and unambiguous.

---

## 7. Conservative extension and theory compatibility

A new theory should extend the map before it rewrites the map.

The default sequence is:

```text
existing node
    |
    +---- candidate bridge ----> new hypothesis
```

not:

```text
new beautiful theory
    -> retroactively rename every older result as a special case
```

A new theory may eventually subsume older structures, but the bridge must be established explicitly.

### 7.1 Existing results retain their original semantics

If a later theory reinterprets an older result, the original theorem or calibration remains valid under its original assumptions and terminology unless a correction record says otherwise.

### 7.2 Competing hypotheses are allowed

The Theory Map is a graph, not a single rooted tree. Two or more explanations may coexist while their distinguishing experiments are unresolved.

### 7.3 Theory migration is explicit

A merge, split, rename, reinterpretation, or retirement of a stable map node should record:

- old claim;
- new claim;
- mathematical reason for the change;
- affected edges;
- code/API implications, if any.

This is theoretical backward compatibility: not preservation of wrong ontology, but preservation of an auditable path from old semantics to new semantics.

---

## 8. Minimum ontology rule

Do not create a generic foundational object merely because several files can share a class name.

A new primitive should normally require all of:

1. a distinction not expressible cleanly by existing nodes/edges;
2. repeated mathematical pressure for that distinction;
3. at least one operation, law, obstruction, or invariant that depends on preserving it;
4. a negative control showing that the concept is not vacuous;
5. a smaller contract than the motivating examples.

Examples of insufficient pressure by themselves include:

- having computed a period;
- having observed a holonomy-like residual;
- finding a new coefficient field;
- using the same helper function in two tests;
- discovering a named classical construction in one calibration.

The repository should prefer a precise local statement over a premature generic object.

---

## 9. Falsification and red-team obligations

Every T1+ theory record must contain a **Kill conditions** section.

Useful kill conditions include:

- two equally admissible constructions produce outputs with no declared equivalence;
- a claimed invariant changes under an allowed presentation transformation;
- a proposed completion loses information required by the declared task;
- a negative control is classified as a positive instance;
- a degeneration fails to land in the proposed boundary theory;
- an allegedly minimal representation is dominated by a competing adequate representation;
- a local construction cannot be globalized and the theory has no place to record the obstruction.
- a claimed symbolic language is not closed and has no controlled-extension
  rule;
- a claimed numerical calculus is unstable, branch-ambiguous, or
  nonreproducible on its declared domain;
- an alleged computational gain disappears when compilation, storage,
  dictionary, residual, or lowering costs are charged;
- quotienting or lowering erases payload required by a declared future
  calculation.

Red-team work is allowed to strengthen a theory by narrowing it. A failed universal claim may become a valuable local theorem.

---

## 10. Relation to software governance

Theory and software use asymmetric promotion rules.

| Theory maturity | Default software consequence |
| --- | --- |
| **T0** | research notes / Sonnet only; no API pressure |
| **T1** | research-local experiments; may motivate prototypes, but not Public API ontology |
| **T2** | may justify `process_geometry.experimental` if the software contract is independently useful |
| **T3** | may justify reusable abstractions; Public API still requires the independent gates in `GOVERNANCE.md` |
| **T4** | may shape package ontology and long-lived vocabulary, subject to ordinary API/release governance |

Effective-analysis evidence does not bypass this table.  A powerful solver in
one model organism can remain T1/T2 and research-local; conversely, a stable
record/container API must not inherit calculation claims its implementation
does not make.

Two prohibitions follow:

```text
implemented class != mathematical promotion
mathematical promotion != automatic Public API promotion
```

The normal order is deliberately conservative:

```text
theory evidence
    -> theory promotion
    -> experimental software pressure
    -> cross-domain API evidence
    -> public semantic commitment
```

A Public API should not be used to make a speculative theory harder to revise.

---

## 11. Theory Map change operations

A substantial result should describe its effect on the current map using one or more of:

- **support** — new evidence for an existing node or edge;
- **refine** — narrow assumptions, equivalence, scope, or semantics;
- **split** — one node/edge was hiding materially different structures;
- **connect** — establish a previously hypothetical edge;
- **contradict** — produce evidence against a claim;
- **merge** — prove that previously separate nodes are equivalent under a stated notion;
- **deprecate** — retain history but stop using a node as current theory;
- **unchanged** — result is important locally but does not alter the map.

A map change is not required for every research result. Most results should leave the stable map unchanged.

---

## 12. Pull-request discipline

A PR that materially changes a T1–T4 theory node or edge should include a **Theory Map Change** section answering:

1. Which node or edge changes?
2. What is its old and proposed T-status?
3. Is the role local, reusable, or foundational?
4. Is the operation support, refine, split, connect, contradict, merge, deprecate, or unchanged?
5. What structure is preserved and forgotten?
6. What is the strongest controlled word used, and what justifies it?
7. What negative control or kill condition protects the claim?
8. Does this create pressure on Experimental/Public API? If so, why is the software response not stronger than the theory evidence?
9. If analysis, computation, stability, or efficiency is claimed, which
   Effective Analysis gates apply and where are the executable evidence,
   baseline, units, error/failure semantics, and cost boundary recorded?
10. What changes in the Mathematical Core: objects, construction,
    law/obstruction, information contract, covariance/units, or boundary?
11. What changes in the Engineering Architecture: solver stage, algorithm,
    backend/dependency, evaluator, certificate, error/failure contract,
    decoder, budget, baseline, or cost?

Purely local research may answer:

> `Theory Map Change: none; this is T0/T1 exploration and does not modify the stable map.`

Mechanical PRs may mark the section not applicable.

---

## 13. First governed application: canonical-completion hypothesis

The current pendulum / Abelian-history line suggests a possible larger chain of the form

\[
\text{process quotient}
\to (C,D,\omega)
\to \text{global period data}
\to \text{group/completion layer}
\to \text{uniformizing process functions}.
\]

This is theoretically important, but under this governance it is **not** Core Theory.

Current classification:

```text
Epistemic maturity: T1 — Precise Conjecture
Role: foundational candidate
Code/API status: no generic completion API
Map effect: candidate connection inside H4 / global analysis
```

The existing executable evidence around algebraic observable quotients, Abelian differentials, periods, and the genus hierarchy is meaningful, but it does not yet prove that a unique or universal completion is forced by Process Geometry.

Before T2 promotion, the line should survive deliberately different calibrations and boundaries—for example genus-zero/additive or multiplicative cases, pendulum/elliptic cases, higher-genus cases, degeneration, and a nonintegrable or nonconservative negative control. It must also state precisely what information is lost when noncommutative process history is replaced by a commutative/global analytic shadow.

This classification is intentionally conservative: a promising foundational idea is allowed to remain a T1 hypothesis for as long as necessary.

---

## 14. Repository artifacts

Use the following artifacts for theory governance:

- [`MATHEMATICAL_CORE.md`](MATHEMATICAL_CORE.md) — required mathematical
  synthesis: objects, constructions, laws, information contracts, and current
  boundaries;
- [`ENGINEERING_ARCHITECTURE.md`](ENGINEERING_ARCHITECTURE.md) — required
  problem-to-solver architecture, technical decisions, evidence, errors,
  dependencies, and cost boundaries;
- [`THEORY_MAP.md`](THEORY_MAP.md) — compact current map;
- this file — promotion and review policy;
- [`THEORY_RECORD_TEMPLATE.md`](THEORY_RECORD_TEMPLATE.md) — node/edge record template;
- [`65-effective-analysis-principle.md`](65-effective-analysis-principle.md) —
  cross-cutting research and engineering contract for symbolic/numerical
  analysis claims;
- research notes / Sonnets — unconstrained exploration and detailed evidence;
- `GOVERNANCE.md` — theory-to-software/API promotion;
- PR **Theory Map Change** section — auditable map mutations.

The intended information flow is:

```text
research note / Sonnet
    -> Mathematical Core relation or proposed correction
    -> Engineering Architecture relation when computational
    -> theory record
    -> Theory Map promotion
    -> optional Experimental software
    -> API governance
```

Most ideas should stop before the end of this chain.

---

## 15. Compact policy

If only one paragraph is retained, use this one:

> **Explore freely; promote conservatively. Treat theory as a graph of auditable nodes and edges. Every stable claim states its maturity, scope, equivalence, preserved and forgotten information, and falsification conditions. Strong words create proof obligations. New ontology must be forced by repeated distinctions. Stable theory should compress the map. Analysis claims must expose effective symbolic/numerical evaluation, certificates, failure semantics, and cost boundaries. Software may trail theory, but must not run ahead of it.**

In even shorter form: **read and reconstruct the Mathematical Core before
placing a claim in the Theory Map, and read the Engineering Architecture before
claiming that it is feasibly computable or naming it in software.**
