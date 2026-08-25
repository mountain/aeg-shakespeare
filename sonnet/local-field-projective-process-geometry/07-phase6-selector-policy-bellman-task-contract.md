# Phase 6 task contract — finite selector-policy Bellman comparison

**Status:** frozen task statement only; research inactive; no evaluator,
dynamic program, certificate, optimum, or preferred selector is claimed.

**Specification owner:** this note.  A future executable owner must be created
only when the phase is explicitly reactivated.

## 1. Purpose of this record

Phases 3--5 established the exact boundary of the next question.

- Ruban and Browkin I choose different rational lifts of the same finite
  projective contact.
- Reciprocal continuation can distinguish those lifts.
- On the bounded rational audit, both fixed selectors materialize
  nondecreasing segments of one input-directed Bruhat--Tits ray, so route
  geometry supplies no unspent shortest-path problem.
- Fixed-depth projective cylinders support an exact source and Huffman task,
  but that coding tree is separate from selector histories.

The remaining optimization question is therefore not "which existing
selector takes the shortest geometric route?"  It is:

> Under one finite source, one finite action grammar, one shared stopping and
> decoding contract, and separately declared costs, can local choices of
> projective-contact lifts be compared by an exact finite-horizon Bellman
> recursion?

This note freezes that question without answering it.  It deliberately adds
no experimental evidence and changes no current mathematical claim.

## 2. Task identity and maturity

```text
Name: finite p-adic selector-policy Bellman comparison
Epistemic maturity: T0 task specification
Role: local Sonnet calibration
Claim mode in this PR: record-only
Execution state: not started
Software status: no implementation and no API pressure
```

The eventual result, if executed, will be an exact finite control result for
the declared corpus and budgets below.  It will not define a preferred
continued fraction on \(\mathbb Q_p\).

## 3. Frozen finite workload

Run three independent tasks, one for each

\[
p\in\{3,5,7\}.
\]

For each prime use the Phase 3 rational audit set

\[
X=\left\{
\frac ab:
1\le b\le12,\quad
-12\le a\le12,\quad
a\ne0,\quad
\gcd(|a|,b)=1
\right\},
\qquad |X|=182,
\]

with the explicitly declared audit source

\[
\mu_p(x)=\frac1{182},\qquad x\in X.
\]

This is a finite comparison convention, not a natural, invariant, Haar, or
boundary measure.  A changed source law is a required red team rather than an
allowed silent reinterpretation.

Freeze the remaining workload parameters as

```text
projective precision d = 4 edges from the standard lattice root
control horizon       H = 16 selected digits
arithmetic domain       = exact Fraction values only
prime tasks              = reported separately, never averaged by default
```

Exact rational termination is accepted as a stronger success than reaching
finite projective precision.  This prevents a one-digit exact expansion from
being penalized merely because its terminal prefix lattice stays shallower
than depth four.

## 4. Primitive data and forbidden imports

The primitive data are:

1. an exact rational initial value \(\alpha_0\in X\);
2. one declared odd prime \(p\);
3. reciprocal continuation
   \(\alpha_{n+1}=1/(\alpha_n-a_n)\);
4. the chronological digit matrix
   \[
   M(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix};
   \]
5. the standard lattice frame \(L_0=\mathbb Z_p^2\) and edge ruler
   \(v_p(p)=1\);
6. the exact Phase 1 two-chart finite lattice oracle;
7. the source, precision, horizon, decoder, and costs declared here.

The future phase must not import any of the following as an answer:

- Ruban or Browkin as the only two admissible whole policies;
- a preferred section chosen by historical name or real-place analogy;
- a boundary measure inferred from the finite audit source;
- Bruhat--Tits edges reused as digit, bit, serialization, or computation
  units;
- a universal scalarization of the cost axes;
- a Bellman optimum interpreted as convergence, periodicity, entropy, or a
  Lagrange theorem;
- a generic control, projective-tree, or continued-fraction API.

## 5. Frozen local action grammar

For a nonzero complete quotient \(\alpha\), put

\[
k=\min\{v_p(\alpha),0\},
\qquad
C_p=\{-(p-1),\ldots,p-1\}.
\]

The admissible action values are the distinct rationals

\[
A_p(\alpha)=
\left\{
a=\sum_{j=k}^{0}c_jp^j:
c_j\in C_p,
\quad
\alpha-a=0\ \text{or}\ v_p(\alpha-a)\ge1
\right\}.
\]

For \(\alpha=0\), declare \(A_p(0)=\{0\}\).  Coefficient tuples that denote
the same rational define one action, not several syntactic actions.

This grammar is finite at every state and is stated without naming either
classical selector.  It is intended to admit their digits, but the future
phase must certify, rather than assume, that the Ruban and Browkin action at
every complete quotient reachable in the frozen graph belongs to this
grammar.  Failure of that inclusion is a task-definition failure and stops
the phase before optimization.

The grammar is not claimed to contain every mathematically interesting
\(p\)-adic section.  It is the declared finite control alphabet for this one
task.

## 6. Markov state and information contract

Immediately before selecting \(a_n\), use the state

\[
s_n=(n,\alpha_n,G_{n-1},V_{n-1},R_n),
\]

where

- \(n\) is the number of digits already selected;
- \(\alpha_n\) is the exact next complete quotient;
- \(G_{n-1}=M(a_0)\cdots M(a_{n-1})\), with \(G_{-1}=I\);
- \(V_{n-1}=[G_{n-1}\mathbb Z_p^2]\) is the standard-frame lattice class;
- \(R_n=\{\alpha_0,\ldots,\alpha_n\}\) is the visited complete-quotient set
  needed to distinguish an exact repeated state from horizon exhaustion.

The initial value \(\alpha_0\), prime \(p\), target depth \(d\), and horizon
\(H\) are episode parameters.  Accumulated additive cost is not part of the
semantic state; it is carried by the Bellman ledger.

The state deliberately retains both a composable payload and continuation
residual:

```text
literal chosen actions
    -> prefix matrix G
    -> standard-frame lattice value V
    + complete quotient alpha
    + visited-state witness R
```

The future implementation may cache a field that is exactly derivable from
the others, but it must not quotient the state until a commuting transition
and decoder certificate proves that the omitted information is unnecessary.
In particular, a finite contact or lattice vertex alone is not an admissible
Bellman state.

## 7. Exact transition and outcome precedence

For \(a_n\in A_p(\alpha_n)\), compute

\[
G_n=G_{n-1}M(a_n),
\qquad
V_n=[G_n\mathbb Z_p^2],
\qquad
r_n=\alpha_n-a_n.
\]

Classify the transition in this order:

1. **success_exact:** if \(r_n=0\), stop with an exact terminal certificate;
2. otherwise set \(\alpha_{n+1}=1/r_n\);
3. **success_precision:** if \(\operatorname{depth}(V_n)\ge d\), stop with
   the depth-\(d\) ancestor cylinder and retained reconstruction data;
4. **cycle:** if \(\alpha_{n+1}\in R_n\), stop with the first repeated-state
   witness;
5. **horizon:** if \(n+1=H\), stop without claiming nontermination;
6. otherwise continue at
   \[
   s_{n+1}=(n+1,\alpha_{n+1},G_n,V_n,
   R_n\cup\{\alpha_{n+1}\}).
   \]

Success precedes cycle detection because the declared task ends once its
exact or finite-precision deliverable is available; later continuation is
then outside the task.  Changing this precedence defines a different task.

An inadmissible digit is not a penalized action.  It is absent from the action
set.  Arithmetic invariant failures, singular prefix matrices, or malformed
state records are evaluator failures and invalidate that run.

## 8. Shared terminal decoder

Both success modes must use policy-independent verification.

### Exact termination

The first column of \(G_n\) must reconstruct \(\alpha_0\):

\[
\alpha_0=\frac{(G_n)_{00}}{(G_n)_{10}}.
\]

The denominator must be nonzero and the equality exact.

### Fixed projective precision

Return

\[
(C_d,G_n,\alpha_{n+1}),
\]

where \(C_d\) is the unique depth-\(d\) ancestor of \(V_n\).  Verify both

\[
C_d\preceq V_n,
\qquad
\alpha_0=G_n\cdot\alpha_{n+1}.
\]

The visible task output is the cylinder \(C_d\).  The matrix and next complete
quotient are retained decoder/continuation data, not silently identified with
that cylinder.  A policy whose terminal record cannot pass the same decoder
is unsuccessful regardless of its cost.

## 9. Cost and comparison order

For every successful path record the online cost vector

\[
c=(c_{\mathrm{digit}},c_{\mathrm{edge}},c_{\mathrm{digit\ bits}},
c_{\mathrm{decoder\ bits}}).
\]

Freeze the axes as follows.

1. \(c_{\mathrm{digit}}\): one unit per selected action;
2. \(c_{\mathrm{edge}}\): the sum of exact tree distances
   \(d(V_{i-1},V_i)\), including skipped intermediate vertices;
3. \(c_{\mathrm{digit\ bits}}\): the Phase 3 exact rational ruler
   \[
   b(q)=\max\{1,\operatorname{bitlength}(|\operatorname{num}q|)\}
        +\operatorname{bitlength}(\operatorname{den}q),
   \]
   summed over selected digits;
4. \(c_{\mathrm{decoder\ bits}}\): for `success_exact`, apply the same ruler
   to the two first-column entries used by the decoder; for
   `success_precision`, apply it to all four entries of \(G_n\) and to
   \(\alpha_{n+1}\), then add
   \(\lceil\log_2|\mathbb P^1(\mathbb Z/p^d\mathbb Z)|\rceil\) for the
   cylinder label.  These two terminal layouts are frozen here and used by
   every policy.

No default weighted sum is declared.  The primary Bellman value is the finite
set of Pareto-nondominated successful cost vectors.  Separate scalar Bellman
audits may minimize one named axis at a time; any mixed scalarization must
declare its weights and units as a separate task.

Outcome comparison is lexicographic before cost:

```text
success_exact or success_precision  <  cycle  <  horizon
```

where either success is finite-cost, while cycle and horizon receive distinct
nonfinite sentinels and are never averaged into a finite success cost.  Exact
termination and finite-precision success share feasibility rank but remain
separate reported outcomes.

Computation is a separate engineering ledger, not silently a fifth online
geometry cost.  The future phase must report at least reachable states,
enumerated actions, exact arithmetic operations or a reproducible proxy, peak
stored Bellman records, policy-table size, compilation time, and repeated
evaluation time.  Discovery/compilation cost and online policy cost must not
be merged.

## 10. Bellman problem and baseline policies

For each \((p,\alpha_0)\), exhaust the finite reachable state graph induced by
the frozen grammar and horizon.  Backward recursion returns the
Pareto-nondominated successful costs and at least one action witness for every
retained value.  The source-level report then pushes the per-input results
through \(\mu_p\), while retaining individual failures and witnesses.

The fixed Ruban and Browkin I selectors enter only as deterministic baseline
policies.  They must be replayed through the same:

- state representation;
- action-admissibility check;
- transition and outcome precedence;
- terminal decoder;
- cost rulers;
- source law and workload limits.

Required comparisons are:

1. success, cycle, and horizon counts;
2. per-input outcome differences;
3. conditional expected costs for each success mode and each named axis;
4. Pareto dominance, incomparability, or equality against the Bellman
   frontier;
5. policy-table compilation/storage cost versus the two rule-defined
   baselines.

A corpus-specific lookup policy is not a new \(p\)-adic section.  Any adaptive
policy discovered here must be named as a finite task controller and reported
with its representation cost.

## 11. Required certificates and red teams

The future executable phase is incomplete without all of the following.

### Positive certificates

1. exact action enumeration with duplicate rational values removed;
2. inclusion of every reachable Ruban and Browkin baseline action;
3. exact floor-contact admissibility for every selected action;
4. determinant, matrix chronology, lattice-class, and reconstruction checks;
5. exact terminal-cylinder ancestor and decoder round trips;
6. finite reachable-graph and Bellman-recursion coverage;
7. replay of every returned policy witness to its reported outcome and cost;
8. independent exhaustive comparison on a smaller hand-checkable subproblem.

### Required red teams

- \(\alpha_0=-1\): terminal Browkin versus cyclic Ruban behavior must remain
  visible until the declared precision task legitimately stops earlier;
- \(p=5,\alpha_0=3\): the existing local economy reversal must survive the
  shared cost ledger;
- equal projective contact with different reciprocal continuation must not be
  merged into one Bellman state;
- dropping \(\alpha_n\), \(G_n\), or the visited-state witness must be tested
  for false continuation, decoder, or cycle equivalence;
- at least one nonuniform source on the same corpus must be replayed to show
  that source-dependent expected rankings are not geometry-selected;
- at least two declared scalar cost choices must be replayed to show whether
  their optimal policies differ;
- a forced one-step horizon must remain `horizon`, not become a cycle or
  nontermination claim;
- a synthetic tree sibling-turn must continue to register backtracking even
  if all selected optimal paths happen to be rays.

Negative results are valid.  If no adaptive policy strictly improves either
baseline under a declared ruler, that is a finite result rather than a reason
to change the task after seeing the data.

## 12. Failure semantics and kill conditions

The evaluator must distinguish:

```text
success_exact
success_precision
cycle
horizon
invalid_task_parameter
invalid_action_grammar
arithmetic_or_decoder_failure
inconclusive_within_resource_budget
```

The phase stops without an optimization claim if any of these kill conditions
occurs:

1. the frozen action grammar fails to contain a reachable action of either
   baseline;
2. the proposed state admits two histories with different legal futures,
   outcomes, decoder results, or costs;
3. the policy-independent terminal decoder fails on any successful path;
4. the supposedly finite reachable graph cannot be exhausted under the
   declared horizon and implementation budget;
5. Bellman witnesses cannot be replayed exactly;
6. a comparison changes because one policy used a different stop rule,
   failure penalty, serialization layout, or cost unit;
7. resource exhaustion is silently reported as absence of a better policy.

The task may be revised after such a failure, but the revised contract must be
recorded as a new phase or an explicit amendment before further execution.

## 13. Frozen solver plan

```text
Problem and task:
  finite-horizon adaptive selection of p-adic contact lifts, with exact or
  fixed-cylinder-precision success and a policy-independent decoder

Primitive process / constraints:
  exact rational reciprocal continuation, finite coefficient grammar,
  projective digit matrices, standard-root lattice evaluation

Parameter regime and units:
  p in {3,5,7}; 182-input audit source; d=4; H=16;
  digit, tree edge, rational bit, and decoder bit kept separate

Mathematical Core relation:
  uses the literal history -> composable payload -> observer evaluation ->
  task quotient + retained residual -> decoder chain; changes no core claim

Required lift and residuals:
  complete quotient, prefix matrix, lattice value, and visited-state witness

Candidate presentations:
  exact finite Bellman state above; no generic framework carrier

Adequacy certificates:
  transition congruence, reconstruction, cylinder ancestry, cycle witness

Selection cost / Pareto axes:
  digit, edge, digit serialization, terminal decoder payload

Chosen algorithm:
  exact reachable-graph enumeration and finite-horizon set-valued Bellman
  recursion

Symbolic evaluator:
  Python integers and Fraction, plus the existing research-local matrix and
  lattice normal forms

Numerical evaluator:
  not applicable

Decoder / reconstruction:
  shared exact-terminal or fixed-precision decoder from Section 8

Error and failure semantics:
  Section 12

Independent baseline:
  fixed Ruban and Browkin I policies plus a smaller exhaustive control

Red team / degeneration:
  Section 11

Search and runtime budgets:
  full frozen state graph is attempted only after a small-instance size and
  seconds-scale feasibility audit; larger execution is manually dispatched

Reproducibility data:
  source ordering, action ordering, exact state keys, tie-breaking, terminal
  layout, cost rulers, and environment versions

Current software layer:
  Sonnet research-local only

Engineering Architecture effect:
  unchanged in this specification PR

Theory Map effect:
  unchanged in this specification PR

API pressure / explicit non-pressure:
  none
```

## 14. Execution gates after reactivation

Research must proceed in this order.

1. **Gate 6A -- contract validation:** implement only action enumeration,
   baseline inclusion, state keys, and failure validation on a tiny corpus.
2. **Gate 6B -- transition and decoder:** certify exact transitions and both
   success decoders before adding optimization.
3. **Gate 6C -- finite graph:** measure reachable-state/action growth and
   either certify the frozen workload feasible or return inconclusive.
4. **Gate 6D -- Bellman recursion:** compute and replay Pareto value/action
   witnesses on the validated graph.
5. **Gate 6E -- baselines and red teams:** compare Ruban, Browkin, changed
   sources, and changed cost rulers without changing the frozen primary task.
6. **Gate 6F -- interpretation:** only after the executable evidence, state
   the Mathematical Core, Engineering Architecture, and Theory Map effects.

No later gate may be used to retroactively repair an earlier certificate by
changing its semantics in place.

## 15. Completion criteria for the future phase

Phase 6 is complete only when a later PR supplies:

- an executable owner and seconds-scale semantic regression slice;
- exact records for every frozen input or an explicit
  `inconclusive_within_resource_budget` result;
- all positive certificates and required red teams;
- replayable Bellman and baseline policy witnesses;
- separate online, compilation, storage, and decoder cost reports;
- a claim ledger distinguishing finite theorem, corpus statistic,
  interpretation, and open question;
- an explicit postmortem even if the optimization hypothesis fails.

Until then, this file is a restart point, not evidence that the research has
advanced.

## 16. Present claim boundary

This specification PR makes no new exact mathematical statement beyond
defining a finite task.  It does not run the action grammar, assert that the
state is minimal, establish Bellman optimality, compare any policy, or modify
the Phase 5 results.

It proves no preferred selector, infinite-boundary measure, convergence rate,
entropy rate, periodicity classification, \(p\)-adic Lagrange theorem, general
ray theorem, or continuous/discrete complexity identity.  It changes neither
`MATHEMATICAL_CORE.md`, `ENGINEERING_ARCHITECTURE.md`, nor `THEORY_MAP.md`, and
it creates no Experimental or Public API proposal.
