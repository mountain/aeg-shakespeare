# Theory record template

Use this template when a research result proposes, materially changes, or promotes a Theory Map node or edge. It is deliberately stricter than an ordinary research note.

A theory record is not required for every local result. It is appropriate when the result is intended to change the stable map, create a reusable theoretical dependency, or justify stronger terminology.

---

## Node record

```text
Theory record: TR-NNNN
Name:
Date:
Authors / origin:
Related notes / Sonnets / tests:

Epistemic maturity: T0 | T1 | T2 | T3 | T4
Role: local | reusable | foundational
Evidence provenance:
Code/API status:

## Claim

Definition / claim:

Input objects:
Required structure:
Output objects:
Scope / domain:
Equivalence notion:

## Information contract

Preserves:
Forgets:
Task semantics, if any:
Decoder / reconstruction status:

## Effective analysis contract, if claimed

Claim mode: exact-symbolic | certified-approximate | numerical | search-only | record-only | not-applicable
Function / observable language:
Operators / process actions:
Closure / controlled extension:
Symbolic evaluator / certificates:
Numerical evaluator:
Domain / units / ruler:
Error / tolerance / failure semantics:
Conventional or competing baseline:
Workload / cost boundary:
Lift / quotient / lowering compatibility:

## Claim classes

Theorems:
Conjectures:
Interpretations:
Classical anchors:

## Evidence

Positive calibrations:
Independent domains:
Negative controls:
Adversarial cases:
Degenerations:
Known counterexamples:

## Controlled vocabulary

Strong terms used:
Meaning / evidence for each:

## Kill conditions

- ...

## Open obligations

- ...

## Promotion criteria

To T(next):
- ...

## Theory Map effect

support | refine | split | connect | contradict | merge | deprecate | unchanged

Affected nodes:
Affected edges:
Migration note:

## Software pressure

Experimental/API pressure:
Explicit non-pressure:
```

---

## Edge record

For a proposed arrow

\[
A \xrightarrow{F} B,
\]

use:

```text
Theory edge: TE-NNNN
Source:
Target:
Operation / construction:

Epistemic maturity: T0 | T1 | T2 | T3 | T4
Role: local | reusable | foundational

Required source structure:
Additional choices / gauge / observer data:

Information forgotten:
Invariant / semantics preserved:

Canonicality claim:
Equivalence notion:
Existence status:
Uniqueness status:

Local or global:
Globalization obstruction:
Decoder / reconstruction:

Effective-analysis transport, if claimed:
Claim mode:
Symbolic evaluator / certificate:
Numerical evaluator / error semantics:
Unit / scale transport:
Baseline / cost transport:

Positive evidence:
Negative control:
Degeneration:
Known failure:

Kill conditions:
- ...

Promotion criteria:
- ...
```

---

## Minimal T1 example

A useful T1 record is already precise enough to be killed.

Bad:

> Elliptic functions are the natural language of the pendulum.

Better:

> On a specified nondegenerate energy leaf and for a declared observable construction, the first-order algebraic process image carries a differential \(\omega\) satisfying \(\omega(D)=1\). The conjectural stronger edge is that an admissible class of such marked carriers has a canonical global completion, under a stated equivalence, whose period obstruction controls the required uniformizing process functions.

The second statement is still a conjecture, but its scope, missing uniqueness theorem, and possible counterexamples can be audited.

---

## Review checklist

Before promoting a record, check:

- [ ] theorem, conjecture, and interpretation are separated;
- [ ] inputs and required extra structure are explicit;
- [ ] equivalence notion is explicit;
- [ ] preserved and forgotten information are explicit;
- [ ] at least one kill condition is stated;
- [ ] negative/adversarial/degenerate evidence is present at T2+;
- [ ] controlled vocabulary is justified;
- [ ] map effect is explicit;
- [ ] code/API status does not exceed theory evidence;
- [ ] the new theory compresses or clarifies the map rather than only adding names.
- [ ] analysis/computation claims state their mode, evaluator, certificates,
      domain, units, error/failure semantics, baseline, and cost boundary;
- [ ] symbolic closure, numerical stability, and computational economy are not
      inferred from one another;
- [ ] `not applicable` is justified where an Effective Analysis field is
      intentionally absent.
