# Effective Analysis Principle

**Date:** 2026-08-25
**Status:** research-program constraint and engineering policy; this note does
not claim that every process admits a calculus-bearing presentation, does not
promote H4 or V5, and does not propose a generic API.

**Operationalization:** `MATHEMATICAL_CORE.md` carries the current mathematical
meaning, while `ENGINEERING_ARCHITECTURE.md` turns this principle into concrete
problem contracts, algorithm/backend decisions, evidence, error/failure
semantics, dependency policy, CI tiers, and solver-plan governance.

## 0. Purpose

Process Geometry starts before coordinates, function spaces, differential
operators, or named special functions.  That origin creates an important
obligation.  The framework must not gain generality by abandoning the feature
that makes classical calculus scientifically powerful: after an adequate
language has been found, one can perform symbolic operations, evaluate it
numerically, control error, and compare the cost of competing representations.

This note makes that obligation explicit.

The current mother picture remains two-axis:

- horizontal distinguishability and task-sufficient presentation;
- vertical semantic compression, objectification, higher-rank composition,
  and compositional lowering.

The new statement is a constraint across both axes rather than a third
ontological axis:

> **Effective Analysis Principle.**  When Process Geometry claims that a
> presentation supports analysis, that claim must include an effective path
> from declared process and task data to symbolic operations and/or numerical
> evaluation, together with explicit certificates, error or failure semantics,
> and cost accounting appropriate to the claim.

A semantically sufficient presentation may legitimately stop before analysis.
It must then say so.  What is prohibited is calling a presentation analytically
successful merely because an abstract differential, integral, quotient, or
comparison object exists.

---

## 1. What is being preserved from classical calculus

The relevant inheritance is not a fixed coordinate system or the ordinary
derivative.  It is the conjunction of several operational properties:

1. **symbolic action** — important operators act by explicit rules on a stated
   function language;
2. **closure or controlled extension** — the action remains in the language,
   or a resonance/singularity forces a documented extension;
3. **numerical evaluation** — expressions, paths, or observables can be
   evaluated with stated domains, tolerances, and failure conditions;
4. **certification** — exact identities, residuals, commutators, round trips,
   or error bounds make the claim independently auditable;
5. **computational economy** — the chosen presentation is compared with a
   declared baseline under an explicit task ruler and cost model.

Traditional calculus is valuable because geometry, symbolic manipulation, and
numerical approximation reinforce one another.  Process Geometry should seek
process-adapted versions of that conjunction, not merely retain familiar
notation.

The A/M model organism already exhibits a narrow concrete slice:

```text
Addition / Multiplication histories
    -> finite noncommutative relation
    -> ordered differential algebra
    -> power-weight modules and resonant extensions
    -> exact residual certificates and explicit path flow
```

The Abelian and classical calibrations exhibit different slices.  None of
these examples establishes a universal calculus.

---

## 2. A claim contract, not a new universal object

For review purposes, an analysis-bearing presentation should state the
following fields.  They are a checklist, not a proposed class or mother object:

```text
process and task:
presentation and declared equivalence:
unit / ruler / scale data:
function or observable language:
operators / process actions:
closure or controlled-extension rule:
symbolic evaluator and certificates:
numerical evaluator and error/failure semantics:
baseline and cost model:
lift / quotient / reconstruction boundary:
cross-rank comparison, if claimed:
```

The fields are claim-relative.  A finite exact quotient may mark differential
and numerical fields `not applicable`, while still providing an executable
transition, observation, and distinguishing-continuation certificate.  A
continuous scientific model that claims a process calculus may not mark all of
symbolic closure, numerical evaluation, and error semantics absent.

This prevents two opposite mistakes:

- forcing manifold-style calculus onto discrete processes that do not need it;
- allowing abstract existence or a successful symbolic prototype to stand in
  for an effective analytic language.

---

## 3. Five effective-analysis gates

### E1 — Semantic adequacy

The task, process carrier, equivalence notion, and preserved/forgotten
information must be explicit.  Calculation on the wrong quotient is not a
successful analysis.

Questions:

- Which future observations or variations must remain distinguishable?
- Which histories, branches, residuals, or holonomies may be forgotten?
- Is the presentation exact, approximate, local, or resource-bounded?
- What decoder or reconstruction obligation remains?

### E2 — Symbolic effectiveness

State the operator language and show what happens under its action.

Acceptable evidence includes:

- a finite process-action table;
- exact finite relations and commutator/PBW certificates;
- a normal-form or rewrite certificate under declared constraints;
- a controlled extension forced at resonance or a singular locus;
- an exact lowering or round-trip identity.

Calling `sympy.simplify()` is an implementation technique, not a semantic
definition of process equality and not by itself a closure theorem.

### E3 — Numerical effectiveness

When numerical use is claimed, provide an executable evaluator with declared:

- domain and parameter regime;
- units and nondimensionalization choices;
- tolerance or error estimator;
- singular, branch, and nonconvergence behavior;
- reproducibility conditions;
- comparison with an independent reference, conserved quantity, exact limit,
  or convergence study.

Agreement at one sample point is a smoke test, not numerical validation.

### E4 — Computational economy

An economical presentation is relative to a task, unit, workload, and cost
model.  At minimum distinguish:

- execution/evaluation cost;
- storage and live-state cost;
- compilation or discovery cost;
- dictionary/new-primitive cost;
- decoder/lowering cost;
- residual, branch, or holonomy memory.

Objectification does not make a long history one free step.  Its amortized
benefit must be compared with the cost of introducing and maintaining the new
primitive.  Bellman/Huffman conclusions are valid only after the task quotient
and ruler have been declared; moving units require covariant transport rather
than silent scalar comparison.

### E5 — Certified transport and closure

The calculation must remain meaningful under every transformation that the
claim treats as semantic:

- literal history to task presentation;
- local observer change;
- lifted history to quotient;
- one presentation to another;
- objectification and compositional rank lowering;
- higher-rank to lower-rank variation, when V5 is claimed.

The strongest version asks not only for a commuting diagram of formal
derivatives, but also for compatible evaluators, certificates, errors, units,
and costs.  That stronger **effective analytic closure** is a research target,
not a current theorem.

---

## 4. Consequences for the first-principles program

### 4.1 Presentation

Task sufficiency and analytic usefulness are distinct judgments.  A search may
therefore produce two Pareto frontiers:

```text
semantic adequacy frontier
effective-analysis frontier among adequate presentations
```

An analytically preferable presentation may be the one with sparse operator
action, stable evaluation, or a smaller certified function module, even when
another presentation has the same observable quotient.

### 4.2 Canonicalization

Canonicalization remains local and relative to declared task, observer grammar,
constraints, and equivalence.  Effective analysis adds selection pressure but
does not create a global canonical representative.

A canonicalization claim should report:

- the admissible family and optimization or uniqueness criterion;
- the local regularity and singular locus;
- the symbolic/numerical advantage obtained;
- the information and conditioning sacrificed;
- the allowed transformation under which the result is invariant.

### 4.3 Lift first, quotient second

Calculation may require payload not visible in the terminal observable:
derivatives, adjoints, accumulated action, phase, deck data, branch choices,
peak memory, or error history.  The lift-first discipline therefore protects
computational semantics as well as topology.

Quotienting is justified only after the task declares which of these payloads
future calculations may observe.  Observable equality alone does not license
their erasure.

### 4.4 Unit one and task-covariant cost

The local unit/ruler is part of the computation contract.  It determines
discretization, stopping, tolerances, and the comparison of time, space, and
stored history.  A fixed unit may reduce a costed tree to a Huffman calibration;
a moving unit requires transport and may expose holonomy or global
integrability obstructions.

### 4.5 Objectification and rank change

Objectification earns its role when it creates both new compositional freedom
and a more effective analytic language.  Mere abbreviation is insufficient.
At a minimum, a rank-raising claim should measure whether the new primitive:

- shortens repeated execution under a declared workload;
- supports explicit operator action or variation;
- lowers compositionally with certificates;
- preserves task-required errors, units, and residuals;
- remains beneficial after compilation, storage, and decoding are charged.

### 4.6 Analytic closure

V5 should be tested at three increasingly strong levels:

1. **formal closure** — a variation object and comparison map can be written;
2. **certified closure** — the comparison law has exact residual or error
   evidence and survives a red team;
3. **effective closure** — symbolic and numerical computations performed at
   the higher rank lower coherently, with controlled errors and accounted cost.

The repository currently has an explicit A/M rank pair and a finite/
infinitesimal bridge.  It has not yet passed levels 2 or 3 generically.

---

## 5. Research standards

Every substantial Sonnet, classical calibration, or research vignette that
claims a new analysis language should answer:

1. What is the primitive process and declared task?
2. What conventional symbolic/numerical baseline is being reconstructed or
   challenged?
3. Which presentation is proposed, and why is it task-sufficient?
4. Which function/observable language and operators are generated?
5. What closes exactly, what requires extension, and where does it fail?
6. What is numerically evaluable, over which domain, with what error semantics?
7. Which assertions, residuals, invariants, or convergence checks certify it?
8. What unit/ruler and cost components are used?
9. What information is retained on the lift and forgotten by the quotient?
10. Does objectification or rank change improve computation after all costs are
    charged?
11. Which independent domain or adversarial example could falsify the proposed
    generality?
12. What changes, if anything, in the Theory Map or software layers?

The default calibration family for a broad effective-analysis claim should
contain:

- one exact finite/discrete example;
- one continuous integrable or otherwise independently checkable example;
- one nonintegrable, stiff, branched, singular, or nonconservative red team;
- one cross-presentation or cross-rank transport test when covariance or
  analytic closure is claimed.

These are defaults, not a requirement that every local essay solve all four
classes.  The breadth of the evidence must match the breadth of the claim.

---

## 6. Engineering standards by maturity layer

| Layer | Minimum effective-analysis obligation |
| --- | --- |
| **Sonnet / research-local** | State the intended calculation, baseline, claim boundary, and at least one executable or falsifiable check; failures may remain open and are valuable evidence. |
| **Extraction candidate** | Supply the claim contract in Section 2, identify which gates are applicable, and compare at least one real alternative presentation. |
| **Experimental** | Provide an executable evaluator for every claimed mode, explicit failure semantics, certificate-bearing tests, a red team, and reproducible cost/stability evidence appropriate to the scope. |
| **Maturing** | Survive independent domains that stress different gates; stabilize units, tolerances, round trips, and migration semantics; document known conditioning and complexity boundaries. |
| **Public API** | Make a narrow durable calculation contract, protect it with semantic and numerical tests, distinguish exact from approximate behavior, avoid backend-defined semantics, and retain replacement-independent meaning. |

`not applicable` is valid when justified.  `not measured` is not evidence for a
positive claim.

### 6.1 Symbolic tests

Prefer exact relations, property tests, residual certificates, round trips,
normal-form agreement under declared semantics, and independent evaluators.
Tests should distinguish literal history from its symbolic image.

### 6.2 Numerical tests

Prefer dimensional checks, convergence studies, invariant drift, branch and
singular-locus tests, independent reference methods, and tolerance scaling.
Hard-coded tolerances without scale or conditioning rationale should not
support a general numerical claim.

### 6.3 Cost tests

Report workload and baseline.  Separate discovery/compilation cost from repeat
evaluation cost.  Measure storage and decoder cost when a new primitive or
compressed presentation is introduced.  Do not infer asymptotic improvement
from one small benchmark.

### 6.4 Reproducibility

Record parameter regimes, seeds where relevant, backend/version constraints,
and whether a result is exact, deterministic approximate, or stochastic.
Generated artifacts must be regenerable or accompanied by an independently
checkable certificate.

---

## 7. Promotion and API consequences

Effective analysis is an additional gate, not an automatic promotion path.

```text
beautiful formula
    != symbolic closure
symbolic closure
    != numerical stability
numerical agreement
    != computational advantage
computational advantage in one model organism
    != generic Process Geometry API
```

An API name that promises calculation must state its mode:

- exact symbolic;
- certified approximate;
- numerical with error/failure semantics;
- search/proposal only;
- record/container only.

Generic names such as `Calculus`, `Integrator`, `CanonicalSolver`,
`AnalyticClosure`, or `ComputablePresentation` remain unclaimed until their
contracts survive independent process classes and negative controls.

---

## 8. Failure patterns to red-team

The following are explicit anti-patterns:

1. a semantically sufficient quotient erases future derivative, adjoint,
   branch, phase, or history payload;
2. a symbolic identity is defined by one computer-algebra simplifier;
3. a numerical path matches one reference value but lacks convergence or
   singular-domain analysis;
4. a new primitive is counted as one free step while compilation, dictionary,
   storage, and lowering are ignored;
5. a local observer equation is described as a global canonicalization;
6. a formal derivative diagram is called analytic closure without executable
   comparison or a failure case;
7. a process-adapted language reproduces a classical formula but is less stable
   or more expensive than the baseline and the difference is not reported;
8. an API exposes a calculation-sounding name while providing only data
   storage or proposal generation.

Each failure can narrow and improve a claim.  None is grounds for hiding a
negative result.

---

## 9. Current evidence and boundary

What is visible now:

- A/M finite relations, commutators, PBW identities, resonant primitives,
  finite modules, and path-flow decomposition are symbolically executable;
- finite process quotients and several coding/frontier results carry exact
  finite certificates;
- pendulum and Abelian calibrations connect process-first reconstruction to
  explicit integrals, periods, and classical numerical shadows;
- local canonical-observer experiments expose symbolic equation solving and
  transported decomposition in bounded domains;
- task-covariant cost experiments show that units, holonomy, and history
  payload materially change computation.

What is not established:

- every task-sufficient presentation admits a low-complexity analysis;
- symbolic closure implies useful numerical stability;
- one generic process calculus covers discrete, continuous, stochastic, and
  higher-rank systems;
- canonicalization selects a globally unique computational language;
- effective analytic closure holds across general rank lowering;
- Arithmetic Geometric Universality follows from the success of A/M.

The strongest responsible claim is therefore:

> Process Geometry treats effective symbolic and numerical analysis as a
> first-class success condition for analysis-bearing presentations, and its
> current model organisms demonstrate important local instances.  General
> existence, stability, complexity, and cross-rank closure remain research
> questions.

---

## 10. Theory Impact

**Theory position:** cross-cutting constraint on Presentation, H4 analysis,
task-covariant evaluation, and V5 analytic closure.

**Maturity:** no T-status promotion.  The principle is adopted as research and
engineering discipline; the corresponding general existence and closure
claims remain open.

**Semantic claim:** an analysis claim must expose how calculation is actually
performed and audited.  Abstract structure alone is insufficient evidence of
effective analysis.

**Non-claim:** no universal calculus-bearing presentation, global canonical
solver, generic effective-analysis carrier, or Public API is asserted.

**Evidence:** A/M exact symbolic calibrations, finite task/coding certificates,
classical and Abelian computation, canonical-observer experiments, and the
unit/holonomy/cost red teams through note 64.

**Map effect:** refine the mother picture from “two axes” to “two axes governed
by a cross-cutting effective-analysis admissibility principle”; connect H4,
task-covariant evaluation, and V5 without merging them.

**Migration risk:** low.  This change strengthens review obligations and claim
boundaries; it introduces no package symbol and changes no runtime semantics.
