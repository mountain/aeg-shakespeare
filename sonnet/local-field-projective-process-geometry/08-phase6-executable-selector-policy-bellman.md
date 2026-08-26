# Phase 6 — executable finite selector-policy Bellman comparison

**Status:** Gates 6A--6F complete for the frozen finite task; exact action
grammar, state, transition, decoders, reachable graphs, Pareto Bellman values,
fixed baselines, witnesses, red teams, and cost ledgers certified.  This is a
task-local finite control result, not a preferred \(p\)-adic continued
fraction or a framework API.

**Owner:**
[test_padic_selector_policy_bellman.py](../../tests/research/test_padic_selector_policy_bellman.py)

## 1. Verdict

The Phase 6 task contract is executable without amendment.  No kill condition
fires on the frozen source

\[
p\in\{3,5,7\},\qquad |X|=182,\qquad d=4,\qquad H=16.
\]

The exact result is more informative than a comparison of Ruban and Browkin
as two indivisible algorithms.

1. The coefficient grammar supplies one or two semantic actions at every
   state.  When Ruban and Browkin agree, a second lift can still exist; hence
   the control problem is not merely a switch between two named policies.
2. The frozen depth-four stopping surface makes every reachable graph tiny:
   at most seven live states and fourteen enumerated actions per input, with no
   live state beyond step two.
3. Exact Pareto Bellman recursion returns a successful replayable value for
   every input.  At \(p=5,7\) the initial frontier is a unique exact-terminal
   value for all 182 inputs.  At \(p=3\), fixed-precision values survive on 16
   frontier records and four inputs have three-point frontiers.
4. Browkin is successful on every frozen task, but is Pareto-dominated on 56,
   38, and 38 inputs for \(p=3,5,7\).  Ruban retains 4, 6, and 8 cycle outcomes
   and is dominated on most remaining inputs, while still matching the
   frontier on its cheapest exact cases.
5. A changed source reverses conditional expected digit/edge rankings, and
   two legitimate scalar cost choices select different controllers on twelve
   \(p=3\) inputs.  Geometry fixes the projective evaluation and ruler; it
   does not choose source weights or scalar priorities.

This is a genuine adaptive-control result.  Of the initial Pareto values, 43
at \(p=3\), 28 at \(p=5\), and 24 at \(p=7\) use at least one local action
chosen by neither Ruban nor Browkin at that complete quotient.

## 2. Frozen task and claim mode

The execution changes none of the task data in
[the Phase 6 contract](07-phase6-selector-policy-bellman-task-contract.md):

- exact rational inputs and `Fraction` arithmetic;
- the 182-element reduced rational corpus, reported separately for each prime;
- projective precision four and horizon sixteen;
- the declared coefficient grammar \(A_p(\alpha)\);
- the pre-action state
  \(s_n=(n,\alpha_n,G_{n-1},V_{n-1},R_n)\);
- exact termination before precision success, precision before cycle, and
  cycle before horizon;
- the policy-independent exact and fixed-cylinder decoders;
- four separate online costs: digit, tree edge, digit serialization, and
  decoder payload;
- Pareto comparison before any named scalar audit;
- Ruban and Browkin I only as fixed baselines.

The claim mode is **exact finite**.  Runtime is measured engineering evidence,
not an asymptotic theorem.  There is no numerical or stochastic evaluator.

## 3. Gate 6A — action grammar and state contract

### 3.1 The action grammar is semantically binary

For \(\alpha\ne0\), let \(k=\min(v_p(\alpha),0)\).  Every raw coefficient
tuple produces an action in the real interval

\[
-(p-p^k)\le a\le p-p^k.
\]

Any two admissible actions differ by an element of \(p\mathbb Z_p\).  Since
their denominators divide \(p^{-k}\), that difference is an ordinary integer
multiple of \(p\).  The displayed interval has width strictly below \(2p\),
so it contains at most two points in one such residue class.  Therefore

\[
\boxed{|A_p(\alpha)|\le2.}
\]

For \(v_p(\alpha)>0\), only zero is admitted.  For \(\alpha=0\), the contract
separately declares \(A_p(0)=\{0\}\).

This is a theorem about the frozen grammar, not about all interesting
\(p\)-adic sections.  Syntactic coefficient tuples can collide.  At
\(p=3,\alpha=-1/9\), four admissible tuples collapse to the two rational
actions

\[
-\frac19,\qquad \frac{26}{9}.
\]

The executable owner removes those duplicates before any transition or cost
is evaluated.

### 3.2 Baseline inclusion and nonbaseline actions

Gate 6A first certifies both named selectors on a tiny reachable corpus.  Gate
6C then certifies inclusion on the complete reachable graph.  The full state
census is:

| \(p\) | one-action states | two-action states | states with an action outside both named baselines |
| ---: | ---: | ---: | ---: |
| 3 | 48 | 634 | 317 |
| 5 | 30 | 808 | 404 |
| 7 | 22 | 858 | 429 |

Thus the grammar is small, but not vacuous.  When the two classical selectors
choose different lifts, they exhaust the two actions.  When they coincide,
the grammar may retain a second task-admissible lift not selected by either
whole rule.

### 3.3 Exact state key

The implementation keys all five frozen state fields.  `Fraction`, matrix
entries, the normalized lattice class, and the visited set are immutable and
hashable.  Set order is intentionally irrelevant; changing any semantic field
changes the key.

Two derivability facts are now certified:

\[
V_{n-1}=[G_{n-1}\mathbb Z_p^2]
\]

is exactly recomputable from \(G_{n-1}\), and within one fixed episode

\[
\alpha_n=G_{n-1}^{-1}\cdot\alpha_0
\]

is exactly recoverable whenever the rational chart is finite.  They may
therefore be cached fields rather than mathematically independent data.  The
executable state nevertheless retains them because the frozen contract did
not authorize a state quotient.  In particular, this phase proves no minimal
state theorem.

The stronger deletions fail.  Two matrices can stabilize the same complete
quotient and evaluate to the same lattice class while producing different
fixed-precision decoder payload costs.  Removing \(G\) therefore erases a
declared cost distinction.  Two otherwise equal records with different
visited sets can send the same next quotient to `cycle` or `live`; removing
\(R\) changes outcome semantics.

## 4. Gate 6B — transitions and shared decoders

Every selected action passes the same exact sequence:

\[
G_n=G_{n-1}M(a_n),\qquad
V_n=[G_n\mathbb Z_p^2],\qquad
r_n=\alpha_n-a_n.
\]

The executable precedence is exactly the contract order:

```text
success_exact
  -> success_precision
  -> cycle
  -> horizon
  -> live
```

The exact decoder checks the first-column ratio.  The precision decoder checks
the unique depth-four ancestor and the round trip

\[
\alpha_0=G_n\cdot\alpha_{n+1}.
\]

Tampered first columns, cylinders, and complete-quotient residuals are all
rejected.  At \(p=5,\alpha_0=-1\), a depth-two regression confirms that
precision success precedes the otherwise repeated complete quotient; under
the frozen depth four the same history remains a cycle.  A forced one-step
horizon remains `horizon` rather than becoming a nontermination claim.

## 5. Gate 6C — complete finite graph census

The solver exhausts live states by exact keys and records every admissible
action before Bellman recursion.  The terminal counts below count graph edges,
not input-level policy outcomes.

| \(p\) | inputs | live states | action edges | exact terminal edges | precision terminal edges | cycle edges | horizon edges | max raw tuples at one state |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 182 | 682 | 1,316 | 370 | 434 | 12 | 0 | 625 |
| 5 | 182 | 838 | 1,646 | 448 | 522 | 20 | 0 | 729 |
| 7 | 182 | 880 | 1,738 | 450 | 564 | 26 | 0 | 2,197 |

For every input:

```text
maximum live states       = 7
maximum enumerated actions = 14
maximum live-state step    = 2
```

The nominal horizon \(H=16\) is therefore inactive on the frozen workload.
The small graph is caused by the combination of a one/two-action grammar and
the depth-four success section, not by a generic property of \(p\)-adic
continued fractions.

State, transition, and raw coefficient-enumeration budgets are explicit.
Crossing one returns `inconclusive_within_resource_budget`; it is not reported
as absence of a better policy.

## 6. Gate 6D — Pareto Bellman values

Backward recursion stores every nondominated successful cost vector together
with a deterministic action witness.  Equal cost vectors with different
success modes remain distinct records.  Every returned witness is replayed
through the independent transition and decoder path.

| \(p\) | initial frontier records | max frontier per input | solved states | stored nondominated state-values | candidate state-values | exact records | precision records | records using a nonbaseline action |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 202 | 3 | 682 | 758 | 1,360 | 186 | 16 | 43 |
| 5 | 182 | 1 | 838 | 850 | 1,638 | 182 | 0 | 28 |
| 7 | 182 | 1 | 880 | 882 | 1,714 | 182 | 0 | 24 |

The hand-checkable \(p=5,\alpha_0=-1\) frontier contains only

\[
a_0=-1,qquad c=(1,0,2,4),
\]

which terminates exactly.  The alternative Ruban lift enters the known cycle.

At \(p=3,\alpha_0=-10/11\), the three-point frontier is:

| outcome | actions | \((c_{digit},c_{edge},c_{digit\ bits},c_{decoder\ bits})\) |
| --- | --- | --- |
| precision | \((1,1/3,1/3)\) | \((3,4,8,35)\) |
| precision | \((1,1/3,-8/3)\) | \((3,4,11,33)\) |
| exact | \((-2,5/3,-4/3)\) | \((3,4,13,16)\) |

Exact termination is semantically stronger reconstruction, but it does not
dominate the precision records on digit serialization.  This is why success
mode and cost vector must remain separate.

## 7. Gate 6E — fixed baselines

### 7.1 Shared outcomes

Both named policies use the same action-admissibility check, transition order,
decoders, and cost rulers.

| \(p\) | policy | exact | precision | cycle | horizon |
| ---: | --- | ---: | ---: | ---: | ---: |
| 3 | Ruban | 48 | 130 | 4 | 0 |
| 3 | Browkin | 168 | 14 | 0 | 0 |
| 5 | Ruban | 36 | 140 | 6 | 0 |
| 5 | Browkin | 180 | 2 | 0 | 0 |
| 7 | Ruban | 38 | 136 | 8 | 0 |
| 7 | Browkin | 176 | 6 | 0 | 0 |

Precision success legitimately stops many Ruban paths before the exact cycles
seen in Phase 3.  The remaining cycles occur before depth four and are not
penalized into finite costs.

### 7.2 Relation to the Bellman frontier

| \(p\) | policy | equal to a frontier value | Pareto-dominated | failure | incomparable |
| ---: | --- | ---: | ---: | ---: | ---: |
| 3 | Ruban | 54 | 124 | 4 | 0 |
| 3 | Browkin | 126 | 56 | 0 | 0 |
| 5 | Ruban | 36 | 140 | 6 | 0 |
| 5 | Browkin | 144 | 38 | 0 | 0 |
| 7 | Ruban | 38 | 136 | 8 | 0 |
| 7 | Browkin | 144 | 38 | 0 | 0 |

At \(p=5,\alpha_0=3\), the earlier economy reversal survives the complete
ledger:

\[
c_R=(1,0,3,5),\qquad c_B=(2,2,7,9).
\]

Ruban strictly dominates Browkin on all four axes there.  At \(-1\), Browkin
terminates at \((1,0,2,4)\) while Ruban cycles.  No task-free selector order
survives both witnesses.

### 7.3 Conditional costs by success mode

The following expectations use the frozen uniform source and condition on the
reported success mode.  Axis order is digit, edge, digit bits, decoder bits.

| \(p\) | policy | mode | count | conditional expected cost |
| ---: | --- | --- | ---: | --- |
| 3 | Ruban | exact | 48 | \((83/48,71/24,331/48,215/24)\) |
| 3 | Ruban | precision | 130 | \((321/130,57/13,781/65,4611/130)\) |
| 3 | Browkin | exact | 168 | \((47/21,79/21,709/84,929/84)\) |
| 3 | Browkin | precision | 14 | \((19/7,4,10,241/7)\) |
| 5 | Ruban | exact | 36 | \((29/18,16/9,121/18,80/9)\) |
| 5 | Ruban | precision | 140 | \((96/35,283/70,120/7,1067/20)\) |
| 5 | Browkin | exact | 180 | \((20/9,26/9,929/90,37/3)\) |
| 5 | Browkin | precision | 2 | \((3,4,16,55)\) |
| 7 | Ruban | exact | 38 | \((59/38,32/19,125/19,327/38)\) |
| 7 | Ruban | precision | 136 | \((387/136,273/68,2711/136,8969/136)\) |
| 7 | Browkin | exact | 176 | \((24/11,115/44,901/88,1125/88)\) |
| 7 | Browkin | precision | 6 | \((3,4,19,199/3)\) |

## 8. Source and scalar red teams

At \(p=5\), the uniform source gives successful mass \(88/91\) to Ruban and
one to Browkin.  Conditional on success, their combined expected costs are

\[
\begin{aligned}
E_R^{uniform}&=(221/88,315/88,1321/88,7789/176),\\
E_B^{uniform}&=(29/13,264/91,135/13,1165/91).
\end{aligned}
\]

Now assign mass \(1/2\) to input \(3\) and share the other half uniformly
among the remaining 181 inputs.  The successful masses become \(178/181\) and
one, while conditional costs become

\[
\begin{aligned}
E_R^{skew}&=(311/178,315/178,1591/178,8689/356),\\
E_B^{skew}&=(383/181,444/181,1575/181,1975/181).
\end{aligned}
\]

Under the uniform source Browkin has lower conditional digit and edge cost;
under the skewed source Ruban does.  This is not an overall Ruban victory,
because its success mass remains smaller.  It is the required exact witness
that expected-cost ranking depends on the source task rather than the
projective geometry alone.

At \(p=3\), scalar minimization of `digit_steps` and `decoder_bits` selects
different Pareto witnesses on twelve inputs.  Compiling one deterministic
corpus controller for each ruler gives:

| scalar ruler | table entries | declared serialized-state/action bits | exact terminals | precision terminals |
| --- | ---: | ---: | ---: | ---: |
| digit steps | 364 | 13,264 | 174 | 8 |
| decoder bits | 372 | 13,611 | 182 | 0 |

For \(p=5\), both named scalarizations select the same 372-entry, 14,870-bit
table.  For \(p=7\), both select the same 366-entry, 15,026-bit table.  The
table layout serializes every retained state field and action by a declared
exact rational ruler.  It is a reproducible storage proxy, not a universal
machine-code size.

Ruban and Browkin require no corpus lookup table.  Their table-entry count is
therefore zero, but their independently supplied rule descriptions are not
declared to have zero description complexity.  Compilation/storage and online
cost remain separate ledgers.

## 9. Remaining red teams and failure semantics

All contract red teams are executable:

- same contact, different lift: \(-1\) admits \(-1\) and \(4\) at \(p=5\);
  one terminates and the other continues to \(-1/5\);
- dropping the matrix payload changes precision-decoder storage cost even
  when complete quotient and lattice class agree;
- dropping the visited set changes one transition from `cycle` to `live`;
- a one-step horizon remains distinct from both cycle and nontermination;
- a synthetic root--left--sibling path has traveled distance four, net
  distance two, and one backtracked edge, so the metric still detects
  cancelled travel;
- malformed states, inadmissible actions, decoder tampering, invalid task
  parameters, and exhausted state/action/raw-enumeration budgets have distinct
  exceptions and do not become optimization results.

## 10. Cost and runtime ledger

Online policy costs contain only the four frozen axes.  Separately, the
executable records:

- reachable live states and enumerated action edges;
- raw coefficient tuples before semantic deduplication;
- stored Bellman values and candidates considered;
- scalar policy-table entries and the declared serialization proxy;
- graph/Bellman compilation time and fixed-policy evaluation time.

On the reference development run, all fourteen Phase 6 regressions—including
the full 546-input graph and Bellman censuses, both complete baselines, source
and scalar red teams, and witness replays—complete in about sixteen seconds.
The exact counts and witnesses are the reproducible evidence; wall time is an
environment-dependent engineering observation and no asymptotic speed claim
is made.

## 11. Claim ledger

### Exact finite theorem-level statements for the declared task

1. The frozen action grammar has at most two distinct rational values per
   state and contains both baseline actions on the complete reachable graph.
2. The transition and both decoders commute exactly on every successful edge.
3. Every frozen reachable graph is exhaustible within the recorded budgets.
4. Backward set-valued recursion returns exactly the recorded Pareto values,
   and every stored initial witness replays to its reported outcome and cost.
5. The fixed-policy counts, frontier relations, conditional expectations,
   changed-source comparison, scalar controllers, and storage ledgers are the
   exact values displayed above.

### Corpus statistics, not general theorems

- at most seven live states and depth-two live histories;
- unique exact frontiers at \(p=5,7\);
- the counts of dominated baseline inputs and nonbaseline optimal actions;
- the source-specific and scalar-specific policy rankings.

### Process Geometry interpretation

The experiment realizes one full finite chain:

```text
literal local action history
    -> chronological matrix payload
    -> standard-frame lattice evaluation
    -> depth-four task cylinder + retained residual
    -> policy-independent decoder
    -> Pareto Bellman selection under declared rulers
```

It supports the emerging task-covariant history-evaluation transversal.  It
also sharpens it: geometric route optimality was already exhausted in Phase
4, while policy optimality appears only after source, action, stopping,
decoder, and cost data are added.  The matrix payload and visited witness are
operationally necessary; cached lattice and complete-quotient fields are
exactly derivable under this fixed finite episode.

### Explicit nonclaims

The result proves no preferred section on \(\mathbb Q_p\), no convergence,
periodicity, entropy-rate, Lagrange, infinite-boundary, general ray, or
continuous/discrete complexity theorem.  A scalar corpus policy is not a new
continued-fraction algorithm, and a table lookup is not a new arithmetic
primitive.

## 12. Core, architecture, and map effects

### Mathematical Core — refine

The previously open finite selector-policy contract is now realized in one
declared task.  The phase supports the history--payload--evaluation--task
quotient--residual--decoder order and adds exact evidence that cost can require
payload distinctions invisible to the task cylinder.  It does not select a
generic payload carrier or a minimal general state.

### Engineering Architecture — support and refine

The result supports the exact-finite architecture: semantic adequacy before
optimization, bounded graph enumeration, set-valued Bellman recursion,
policy-independent decoding, explicit inconclusive outcomes, and separate
online/compilation/storage ledgers.  The complete solver remains Sonnet-local;
no dependency or reusable API is added.

### Theory Map — refine without promotion

The result gives H3 and the emerging history-evaluation transversal a complete
finite control calibration.  Changed sources and scalar rulers block an
intrinsic selector interpretation.  Maturity remains local T1/T2 evidence for
the declared finite structure, not a stable generic node, and all API levels
remain unchanged.

## 13. Postmortem and next boundary

The original intuition survives, but in a narrower form.  Projective geometry
does not supply a hidden shorter route: Phase 4 already showed both classical
histories moving on one ray.  Its role is to provide a composable evaluation,
an exact stopping frontier, and a ruler.  Bellman becomes meaningful only
after the task adds local lift actions, residuals, decoders, source law, and
cost axes.

The crucial technical fact is the interaction of two compressions: the raw
coefficient grammar collapses to a binary semantic action set, and the
depth-four stopping surface collapses the nominal sixteen-step search to at
most three selected actions.  That makes exact policy search feasible and
auditable.

The next responsible question is not a larger API.  It is whether this result
survives a deliberately harder task in which at least one of these two
compressions is relaxed—for example greater projective precision, a wider
lift grammar, or finite-precision nonrational inputs—while retaining the same
decoder and failure discipline.  Such a task must be frozen separately before
execution.
