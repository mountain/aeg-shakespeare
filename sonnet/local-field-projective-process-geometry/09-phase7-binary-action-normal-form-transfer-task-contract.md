# Phase 7 task contract — binary action normal form and transfer audit

**Status:** frozen before Phase 7 execution and now discharged without
amendment by
[the Phase 7 result](10-phase7-binary-action-normal-form-transfer-results.md).
This file remains the pre-result audit contract rather than being rewritten as
evidence.

**Executable owner:**
`tests/research/test_padic_selector_structural_law.py`.

**Result owner:**
`10-phase7-binary-action-normal-form-transfer-results.md`.

## 1. Purpose

Phase 6 solved one exact finite selector-policy task and exposed two separate
compressions:

1. as many as 2,197 raw coefficient tuples collapsed to at most two distinct
   rational actions at one state;
2. the depth-four stopping surface collapsed a nominal sixteen-step search to
   at most three selected digits on the frozen corpus.

The first compression looked structural; the second may be an artifact of the
chosen precision and corpus.  Phase 7 must separate them before any larger
selector or framework claim is considered.

The task is therefore:

> Prove or refute an exact closed normal form for the Phase 6 action grammar,
> encode every legal action by a binary lift choice when possible, determine
> whether scalar-optimal first choices descend through smaller task-native
> signatures, and red-team the result at greater precision, new primes, and
> held-out rational inputs.

The goal is not to fit an arbitrary classifier to a finite policy table.  A
candidate compression is acceptable only when its signature has declared
semantics, exact witnesses, explicit collisions, and an out-of-sample audit.

## 2. Primitive data and forbidden imports

Retain the Phase 6 primitive arithmetic:

- one odd prime \(p\);
- one nonzero rational complete quotient \(\alpha\);
- reciprocal continuation \(\alpha'=(\alpha-a)^{-1}\);
- the chronological digit matrix
  \[
  M(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix};
  \]
- the standard lattice frame and normalized ruler \(v_p(p)=1\);
- the exact state, transition precedence, terminal decoders, and four cost
  axes from Phase 6.

The following must not be imported as an answer:

- a preselected Ruban/Browkin winner;
- a machine-learning classifier whose features or capacity are enlarged
  until the frozen table is memorized;
- floating-point thresholds or approximate equality;
- a source-independent scalar objective;
- a general \(p\)-adic convergence, periodicity, entropy, or Lagrange law;
- a generic Bellman, decision-tree, continued-fraction, or projective API.

Ruban may be used as an exact reference representative of the already frozen
contact fibre.  That does not make it the selected policy.

## 3. Candidate action normal form, frozen before execution

For \(\alpha\ne0\), define

\[
k=\min(v_p(\alpha),0),
\qquad
B=p-p^k,
\qquad
r=\lfloor\alpha\rfloor_{p,\mathrm{Ruban}}.
\]

Phase 7 tests the following exact candidate theorem.

### Candidate theorem A — raw grammar image

The image of the coefficient box

\[
c_j\in\{-(p-1),\ldots,p-1\},
\qquad k\le j\le0,
\]

is the complete rational grid

\[
p^k\mathbb Z\cap[-B,B].
\]

This is stronger than the Phase 6 interval bound: it asserts there are no
holes after syntactic coefficient collisions are quotiented.

### Candidate theorem B — binary contact fibre

The distinct admissible action set is

\[
A_p(\alpha)
=
\{r\}
\cup
\begin{cases}
\{r-p\}, & r\ge p^k,\\
\varnothing, & r<p^k.
\end{cases}
\]

For \(\alpha=0\), retain \(A_p(0)=\{0\}\).

If certified, every action has a canonical bit label

\[
a=r-\varepsilon p,
\qquad \varepsilon\in\{0,1\},
\]

with \(\varepsilon=1\) admitted exactly when \(r\ge p^k\).  This is an
action-alphabet normal form, not yet a policy rule.

### Proof obligations

The executable and note must separately certify:

1. the coefficient image is a contiguous \(p^k\)-grid;
2. Ruban's truncation belongs to the grid, obeys \(0\le r\le B\), and has the
   same contact as \(\alpha\);
3. every admissible action is congruent to \(r\) modulo \(p\);
4. the interval contains no third member of that congruence class;
5. the lower member \(r-p\) lies in the grid exactly at the stated threshold;
6. the closed evaluator agrees with exhaustive tuple enumeration wherever the
   latter is run;
7. both baseline actions still belong to the closed action set on every
   audited reachable state.

A finite test census supports but does not replace the general arithmetic
argument.

## 4. Controller-signature audit

For each successful Pareto frontier, retain the Phase 6 deterministic scalar
tie-breaking and inspect two named scalar tasks:

```text
digit policy    minimize digit_steps
decoder policy  minimize decoder_bits
```

Every selected first action is recorded by its canonical lift bit
\(\varepsilon\).  The following signatures are tested in increasing order.

### S0 — contact signature

\[
\sigma_0=(p,k,r,\operatorname{sign}\alpha,
          [\alpha=r],\text{remaining horizon}).
\]

### S1 — evaluated geometry signature

Add the current lattice vertex and, for each admitted bit, the exact next
lattice vertex, tree-edge increment, and transition outcome class.

### S2 — local cost/decoder signature

Add the four exact one-stage or terminal cost increments available before
recursive continuation, including the declared decoder layout on immediately
successful edges.

A signature is sufficient for one scalar task on one declared workload only
if all states with equal signatures have the same set of scalar-optimal first
bits.  A collision with different optimal bit sets is an exact obstruction and
must be retained with both replayable states and suffix witnesses.

No signature may be repaired after a collision by adding the complete matrix,
complete quotient, visited set, or an opaque state identifier.  Those fields
would simply reconstruct the Phase 6 table rather than explain it.  A richer
signature requires a separately frozen later phase.

## 5. Frozen workloads

Define

\[
X_m=\left\{
\frac ab:
1\le b\le m,\quad
-m\le a\le m,\quad
a\ne0,\quad
\gcd(|a|,b)=1
\right\}.
\]

Run the following workloads separately; do not average prime, precision, or
corpus tasks by default.

### Regression workload R

```text
p in {3, 5, 7}
inputs X_12, |X_12| = 182
precision d = 4
horizon H = 16
```

This must reproduce every Phase 6 graph, frontier, baseline, and decoder
result while replacing raw action search by the certified closed form.

### Precision-transfer workload D

```text
p in {3, 5, 7}
inputs X_12
precision d in {6, 8}
horizon H = 24
```

This tests whether the earlier stopping compression survives when the visible
frontier is moved outward.

### Prime-transfer workload P

```text
p in {11, 13}
inputs X_12
precision d in {4, 6}
horizon H = 24
```

These primes are holdouts for the Phase 6 census.  Raw tuple enumeration is
used only on a bounded adversarial sample; the complete run uses the closed
action evaluator after Gate 7A passes.

### Input-transfer workload I

```text
p in {3, 5, 7}
inputs X_18 minus X_12
precision d = 6
horizon H = 24
```

These inputs are excluded from signature discovery on R and used only for
transfer reporting.

## 6. Cost, storage, and comparison contract

Keep all Phase 6 online axes separate.  Add two engineering ledgers:

1. raw coefficient candidates avoided by the closed evaluator;
2. action payload storage under exact rational serialization versus the
   canonical zero/one-bit lift label.

A one-action state needs no action-choice bit.  A two-action state needs one
bit only after \((p,k,r)\) and the normal-form decoder are available.  Do not
count the reference representative or state key as free.  Report separately:

- state-key storage;
- rational-action payload storage;
- normal-form metadata;
- lift-choice bits;
- compilation time;
- repeated evaluation time.

No reduction in action payload is called a reduction in total controller size
unless the complete ledger is smaller.

## 7. Failure semantics and kill conditions

Distinguish:

```text
normal_form_certified
normal_form_false
signature_sufficient_on_declared_workload
signature_collision
success_exact
success_precision
cycle
horizon
invalid_task_parameter
arithmetic_or_decoder_failure
inconclusive_within_resource_budget
```

The phase stops without a transfer or compression claim if:

1. either candidate theorem has an exact counterexample;
2. closed and exhaustive action evaluators disagree;
3. a baseline action falls outside the closed grammar;
4. Phase 6 regression counts or witnesses change;
5. a terminal decoder or policy witness fails replay;
6. a signature collision is hidden by deterministic tie-breaking;
7. a stress workload crosses its declared budget;
8. a failed or unexecuted holdout is reported as successful transfer;
9. action-bit savings are reported as total-table savings without charging
   the normal-form decoder and state keys.

Per input, freeze budgets at 50,000 live states and 100,000 transitions.  Raw
coefficient comparison is limited to 250,000 tuples per audited state.  A
budget crossing is `inconclusive_within_resource_budget`, never a theorem that
the task has no successful or compressed controller.

## 8. Execution gates

1. **Gate 7A — arithmetic normal form:** prove the two candidate theorems,
   implement the closed evaluator, and compare it with exhaustive enumeration
   on R plus bounded adversarial valuation cases.
2. **Gate 7B — Phase 6 equivalence:** reproduce the complete Phase 6 workload,
   witnesses, decoders, baselines, and cost vectors with the closed evaluator.
3. **Gate 7C — signature discovery:** evaluate S0--S2 on R, retaining the
   first exact collision or a complete sufficiency certificate for each scalar
   task.
4. **Gate 7D — transfer red teams:** freeze the discovered conclusion, then
   run D, P, and I without changing the signatures or tie-breaking.
5. **Gate 7E — cost and interpretation:** report total storage, enumeration
   savings, runtime, Mathematical Core, Engineering Architecture, and Theory
   Map effects.

No later gate may revise an earlier theorem, signature, workload, or cost
layout after seeing holdout results.

## 9. Solver plan

```text
Problem and task:
  exact normal form for a finite contact-lift grammar; task-local scalar-policy
  signature and transfer audit

Primitive process / constraints:
  rational reciprocal continuation, bounded Laurent digits, chronological
  projective matrices, standard-root lattice evaluation

Parameter regime and units:
  Sections 5 and 6; digit, tree edge, serialization bit, decoder bit, table
  bit, compilation, and evaluation ledgers remain separate

Mathematical Core relation:
  test whether one local history alphabet admits a lossless normal form before
  continuation; do not identify action compression with task-state quotient

Required lift and residuals:
  retain the complete Phase 6 state and decoders; the candidate bit replaces
  only the rational action payload

Candidate presentations:
  exhaustive coefficient tuples; distinct rational actions; Ruban-reference
  plus lift bit; S0--S2 policy signatures

Adequacy certificates:
  arithmetic proof, exhaustive equivalence, exact transitions, decoder round
  trips, Bellman witness replay, signature collision/sufficiency census

Chosen algorithms:
  closed exact action evaluation, bounded graph enumeration, set-valued
  Bellman recursion, exact signature partition audit

Symbolic evaluator:
  Python integers and Fraction

Numerical evaluator:
  not applicable

Independent baseline:
  Phase 6 exhaustive grammar and frozen results; Ruban and Browkin policies

Red team / degeneration:
  boundary values r=0 and r=p^k, negative valuations, new primes, deeper
  stopping surfaces, held-out rationals, signature collisions

Current software layer:
  Sonnet research-local only

Engineering Architecture effect:
  pending; no API or dependency pressure is assumed

Theory Map effect:
  pending; no maturity promotion is assumed

API pressure / explicit non-pressure:
  none
```

## 10. Completion and claim boundary

Phase 7 is complete only when it supplies:

- a written arithmetic proof or an exact counterexample for both candidate
  theorems;
- an executable closed evaluator and Phase 6 equivalence certificate;
- exact S0--S2 collision or sufficiency records for both scalar tasks;
- D, P, and I transfer outcomes or explicit inconclusive records;
- replayable terminal and policy witnesses;
- full online, compilation, storage, and decoder ledgers;
- a claim ledger and postmortem, including negative results.

Even a successful phase proves only a normal form for this declared action
grammar and finite transfer results for the frozen workloads.  It proves no
preferred \(p\)-adic continued fraction, task-free policy, asymptotic
convergence or periodicity theorem, infinite-boundary measure, entropy rate,
general controller compression theorem, or Experimental/Public API.
