# Phase 8 task contract — continuation-value fibres and the objectification threshold

**Status:** frozen before Phase 8 execution and discharged without amendment by
`12-phase8-continuation-value-fiber-objectification-results.md`.  This file is
the pre-result audit contract and must not be rewritten to fit the observed
quotient.

**Executable owner:**
`tests/research/test_padic_continuation_value_fiber.py`.

**Planned result owner:**
`12-phase8-continuation-value-fiber-objectification-results.md`.

## 1. Purpose

Phase 7 proved an exact binary normal form for the declared p-adic action
grammar, then found exact states with the same strongest local signature S2
but disjoint scalar-optimal lift bits.  That proves a nontrivial future-value
fibre over the local evaluation.  It does not decide what kind of mathematical
object the fibre is.

Four claims must remain separate:

1. **residual existence** — local evaluation forgets information used by a
   declared future task;
2. **task-state extension** — adjoining a finite residual makes the task value
   descend;
3. **transported extension** — the existing lift actions descend to a stable
   partial composition law on the extended state;
4. **vertical objectification** — the residual becomes a task-independent new
   primitive with free higher-rank composition and coherent lowering.

Phase 7 establishes the first item on finite workloads.  Phase 8 tests the
second and third exactly and red-teams the fourth.  It must not call a finite
residual bit a new geometric dimension merely because it is nonzero.

The task is therefore:

> Compute the coarsest finite stable extensions of the Phase 7 local
> signatures that preserve declared policy, value, or full continuation
> semantics; certify the resulting fibre sizes and distinguishing suffixes;
> and decide whether the induced lift-bit transport is uniform, invertible,
> and stable enough to justify any objectification claim.

## 2. Primitive process and forbidden imports

Retain the exact Phase 6/7 process:

- one odd prime \(p\);
- one rational episode input \(x\) and complete quotient \(\alpha\);
- the exact binary action alphabet
  \[
  a=r-\varepsilon p,
  \qquad \varepsilon\in\{0,1\},
  \]
  with bit one admitted exactly when \(r\ge p^k\);
- reciprocal continuation \(\alpha'=(\alpha-a)^{-1}\);
- chronological prefix matrices, standard-root lattice evaluation, visited
  complete quotients, stopping precision, horizon, exact terminal decoders,
  and the four frozen cost axes;
- the exact Phase 7 signatures S0, S1, and S2.

The following must not be imported as answers:

- a hand-named hidden coordinate chosen from the episode input or matrix;
- a classifier enlarged until it memorizes the policy table;
- floating-point clustering, tolerances, or approximate equality;
- a claim that one residual bit is one manifold dimension;
- a group, groupoid, vector bundle, covering, or process-rank vocabulary
  before its required laws are checked;
- a generic task-quotient, controller, objectification, or rank API;
- an infinite-boundary, convergence, periodicity, entropy, or Lagrange claim.

The experiment may use finite partition refinement and canonical structural
hashing because these construct the declared quotient rather than supplying a
preferred arithmetic selector.

## 3. Frozen workload

Let

\[
X_B=\left\{\frac mn:
1\le n\le B,\;0<|m|\le B,\;\gcd(|m|,n)=1\right\}.
\]

Use the following tagged task families:

| label | primes | inputs | precision | horizon | role |
| --- | --- | --- | ---: | ---: | --- |
| R | \(3,5,7\) | \(X_{12}\) | 4 | 16 | Phase 7 regression |
| D6 | 3 | \(X_{12}\) | 6 | 24 | stopping-depth transfer |
| D8 | 3 | \(X_{12}\) | 8 | 24 | deeper stopping red team |
| P4 | 11 | \(X_{12}\) | 4 | 24 | unseen-prime transfer |
| P6 | 11 | \(X_{12}\) | 6 | 24 | prime/depth interaction |
| I | 3 | \(X_{18}\setminus X_{12}\) | 6 | 24 | held-out inputs |

Every state is tagged by its task family, prime, episode input, precision,
horizon, and exact control-state key.  Equal internal tuples from different
tasks are not silently identified before task semantics are compared.

Frozen limits per task are 50,000 live states and 100,000 action edges.  A
task that reaches a limit is `inconclusive_within_budget`; it is not silently
discarded.  All arithmetic is `Fraction`-exact.

## 4. Exact finite response system

Use the common bit alphabet

\[
\mathcal A=\{0,1\}.
\]

For a tagged live state \(s\) and bit \(\varepsilon\), the exact edge response
is one of:

```text
invalid
live(stage_cost, next_state)
success_exact(stage_cost + decoder_cost)
success_precision(stage_cost + decoder_cost)
cycle(stage_cost)
horizon(stage_cost)
```

The full four-axis cost vector is retained.  `invalid`, `cycle`, and `horizon`
remain observable task outcomes even though Bellman optimization excludes
them from successful frontiers.

For a bit word \(w\), recursively compose these edge responses until the word
ends, becomes invalid, or reaches a terminal.  Equality of full continuation
semantics means equality of the exact response for every word admitted by the
common binary interface through the declared finite horizon.

## 5. Three semantic obligations

Phase 8 computes separate quotients because selecting an action, preserving a
value, and preserving every continuation are different tasks.

### 5.1 Policy semantics

For scalar axis

\[
q\in\{\texttt{digit_steps},\texttt{decoder_bits}\},
\]

let \(P_q(s)\subseteq\{0,1\}\) be the exact set of first bits occurring in
successful scalar-minimal Bellman witnesses.  Empty successful frontiers have
the distinguished output `no_success`.

The policy quotient must preserve \(P_q\), not one arbitrary tie-broken bit.

### 5.2 Scalar-value semantics

Let \(V_q(s)\) retain:

- the minimum remaining scalar cost on axis \(q\);
- every optimal terminal outcome;
- every optimal bit word after rational actions are decoded through the Phase
  7 normal form.

This is stronger than policy semantics and remains exact and replayable.

### 5.3 Full finite continuation semantics

Let \(F(s)\) be the complete finite binary response tree of Section 4,
including suboptimal edges, failures, full cost vectors, terminal decoders,
and live successors.  Equality of \(F\) is the strongest Phase 8 task
equivalence.  It is still finite-task relative and is not an infinite
continued-fraction equivalence.

## 6. Stable extension over a local interface

For each local interface \(S_i\), \(i\in\{0,1,2\}\), and each semantic output
\(O\in\{P_q,V_q,F\}\), begin with the kernel partition

\[
\Pi_0=\ker(S_i,O).
\]

Refine synchronously by the two exact edge responses:

\[
\Pi_{n+1}(s)=
\left(
  \Pi_n(s),
  E_0^{\Pi_n}(s),
  E_1^{\Pi_n}(s)
\right),
\]

where a live edge records its exact edge label and the \(\Pi_n\)-class of its
successor, while a terminal or invalid edge records its complete exact label.
Canonicalize block labels after every round and stop at the first fixed point.

Because the state carrier is finite, stabilization is guaranteed.  The
executable must additionally certify that the fixed partition is:

1. a refinement of the declared local interface and semantic output;
2. stable under both lift bits;
3. idempotent under one additional refinement round;
4. the coarsest stable refinement of the frozen initial partition;
5. accompanied by a distinguishing bit suffix for every pair split inside a
   formerly common local fibre.

The fourth item may use the standard finite partition-refinement induction; it
must not be inferred from one implementation's block numbering.

For full continuation semantics, the result must also agree with an
independently computed bottom-up canonical response-tree hash.

## 7. Fibre and information ledger

Let

\[
\rho_{i,O}:\mathcal S_{\mathrm{full}}longrightarrow Z_{i,O}
\]

be the stable quotient and let

\[
\beta_i:Z_{i,O}\longrightarrow S_i
\]

forget the residual block refinement.  For every observed base signature
\(z\in S_i\), record

\[
N_{i,O}(z)=|\beta_i^{-1}(z)|,
\qquad
b_{i,O}(z)=\lceil\log_2N_{i,O}(z)\rceil.

The ledger must report:

- full live state records;
- local-interface classes;
- stable quotient classes;
- number and fraction of nontrivial fibres;
- maximum and distribution of fibre cardinality;
- maximum residual-bit lower bound;
- refinement rounds and shortest/longest distinguishing suffixes;
- task-family and scalar-axis breakdowns.

Two monotonicities must not be conflated:

1. refining the declared interface cannot reduce the total number of stable
   quotient classes;
2. refining the interface may reduce the hidden fibre cardinality above one
   base point because more information has moved into the base.

Phase 8 must prove the first finite statement and measure, not assume, the
second.  Total quotient information and hidden residual information are
different ledgers.

## 8. Transport and objectification red team

At a stable quotient, each legal bit induces a partial map

\[
T_\varepsilon:Z_{i,O}\dashrightarrow
Z_{i,O}\sqcup\mathcal T,

\]

where \(\mathcal T\) is the exact terminal/failure response set.  Certify
well-definedness directly: representatives of one block must have identical
edge labels and, on live edges, land in one successor block.

Then audit the properties that stronger geometric language would require:

### 8.1 Uniformity

- Is fibre cardinality locally or globally constant on any declared base?
- Is one fixed residual alphabet sufficient, or are most fibres singleton
  with irregular exceptional fibres?
- Do the same residual response types recur across R, D6/D8, P4/P6, and I?

### 8.2 Invertibility

- Are the partial maps \(T_0,T_1\) injective on live quotient classes?
- Do distinct classes merge under one bit?
- Do terminal and failure edges prevent inverses?

Failure of invertibility forbids a group or covering-action interpretation;
it does not invalidate a directed finite automaton or category.

### 8.3 Task and ruler stability

- Compare digit and decoder policy/value quotients on the same states.
- Compare depth four with depths six/eight.
- compare regression with new-prime and held-out families.
- record shared response types, task-specific types, and exact witnesses for
  any split caused by changed stopping or decoder semantics.

### 8.4 Composition and lowering

Stable transition descent supplies composition of already declared bit words.
It is only a **horizontal task-state composition certificate**.  A vertical V2
objectification claim would additionally require:

1. residual classes with semantics not tied to one frozen task;
2. a new primitive grammar whose legal composites extend beyond the enumerated
   state graph;
3. coherent lowering of arbitrary generated composites to the original
   continuation process and decoder;
4. relations or invariants that depend on preserving the new primitive;
5. independent-domain pressure.

Phase 8 records which of these obligations remain open.  It must not promote
the finite stable quotient to `Objectification`, `ProcessRank`, a bundle, or a
groupoid API.

## 9. Gates

### Gate 8A — graph and response reconstruction

- reproduce the selected Phase 7 workload censuses through the closed binary
  evaluator;
- construct every tagged live state and exact bit edge once;
- replay every successful scalar/Pareto witness after bit encoding;
- preserve invalid, cycle, horizon, exact, and precision outcomes.

### Gate 8B — quotient construction

- compute policy, scalar-value, and full-continuation stable extensions over
  S0, S1, and S2;
- certify fixed-point stability, coarseness, and bottom-up agreement for full
  continuation semantics;
- retain exact block representatives and provenance.

### Gate 8C — fibre and witness census

- compute every \(N_{i,O}(z)\) and \(b_{i,O}(z)\);
- retain the Phase 7 S2 collision as a mandatory positive witness;
- emit a shortest distinguishing suffix for each nontrivial split type;
- prove total-class monotonicity under S0 \(\preceq\) S1 \(\preceq\) S2.

### Gate 8D — transport audit

- certify descended bit transport;
- count injective, merging, and terminal maps;
- test fibre uniformity and residual-type recurrence;
- compare axes and task families without changing the frozen workload.

### Gate 8E — cost and interpretation

- report quotient compilation time, refinement rounds, state/block storage,
  residual bits, and decoder dependence separately;
- classify the result as horizontal task-state lift, transported finite
  extension, objectification candidate, or exact obstruction;
- update the Mathematical Core, Engineering Architecture, and Theory Map only
  to the strength earned by the certificates.

## 10. Failure semantics and kill conditions

Use the following outcomes:

```text
success_exact
inconclusive_within_budget
invalid_task_contract
arithmetic_or_state_failure
quotient_certificate_failure
objectification_obstruction
```

The following observations kill or weaken the stronger hypotheses:

1. If every S2 fibre is trivial after exact reconstruction, Phase 7's residual
   does not survive as a stable state distinction.
2. If partition transport depends on the chosen representative, the proposed
   residual is not compositional even for the frozen finite task.
3. If policy classes compose only after refinement to full continuation trees,
   the policy residual is not itself a sufficient transported object.
4. If fibre cardinality is irregular, task/ruler changes split the classes,
   or response types fail to recur, a fixed new dimension is unsupported.
5. If bit transport is noninjective or terminates, group, covering, and
   groupoid interpretations are unsupported without additional structure.
6. Even a uniform finite transported quotient does not establish vertical
   objectification without free new composition and compositional lowering.

Positive evidence is also falsifiable: an exact quotient certificate fails if
one pair in a block has different semantic output, edge label, successor
block, or replayed decoder result.

## 11. Solver-plan record

```text
Problem and task:
  minimal stable continuation residual over Phase 7 local signatures

Primitive process / constraints:
  exact rational binary p-adic lift process and frozen finite tasks

Parameter regime and units:
  odd primes and finite rational corpora in Section 3; v_p(p)=1

Mathematical Core relation:
  tests the open minimal-continuation-residual and objectification-threshold
  questions; no dimension or rank is assumed

Required lift and residuals:
  full tagged control state during construction; quotient residual only after
  exact stability certification

Candidate presentations:
  S0/S1/S2 plus policy, scalar-value, or full-continuation stable block

Adequacy certificates:
  exact partition stability, bottom-up response hash, replay, distinguishing
  suffixes, and terminal decoder preservation

Selection cost / Pareto axes:
  digit and decoder scalar views are separate; full four-axis response is
  retained for the strongest quotient

Chosen algorithms:
  finite graph exhaustion, Bellman replay, synchronous partition refinement,
  bottom-up structural hashing, and exact witness extraction

Symbolic evaluator:
  Python integers and Fraction

Numerical evaluator:
  not applicable

Decoder / reconstruction:
  frozen exact/precision terminal decoders and quotient distinguishing suffixes

Error and failure semantics:
  explicit outcomes in Section 10

Independent baseline:
  Phase 7 graph/frontier censuses and independent response-tree hashing

Red team / degeneration:
  S2 witness, changed scalar ruler, changed stopping depth, new prime,
  held-out inputs, noninvertible transport, and nonuniform fibres

Search and runtime budgets:
  finite workload and per-task graph limits in Section 3; routine test module
  must remain seconds-scale rather than become an open sweep

Reproducibility data:
  every workload, state tag, block key, suffix witness, and exact count frozen

Current software layer:
  Sonnet-local research test only

Engineering Architecture effect:
  expected refine/support or explicit obstruction; no dependency/API change

Theory Map effect:
  pending; no maturity promotion is assumed

API pressure / explicit non-pressure:
  none
```

## 12. Completion boundary

Phase 8 is complete only when it supplies:

- exact quotient definitions and the coarsest-stable-refinement argument;
- reproducible policy, value, and full-continuation fibre ledgers;
- replayable distinguishing suffixes and transport certificates;
- uniformity, invertibility, task/ruler-stability, and cost red teams;
- a claim ledger separating finite theorem, corpus statistic, interpretation,
  and nonclaim;
- an explicit verdict on horizontal lift versus vertical objectification.

Even a successful phase proves only a finite task-relative result for the
declared p-adic process.  It proves no new manifold dimension, universal
residual, generic groupoid, process-rank promotion, preferred continued
fraction, asymptotic theorem, or Experimental/Public API.
