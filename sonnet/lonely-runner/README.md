# Lonely Runner — Sonnet 001

**Status:** Phase 4 — exact semantics, task quotient, structural quotient, and first upstream-strict pruning certificate.  
**Target open case:** `LRC(13)`, i.e. **14 runners**.

## 1. Problem

For a positive integer speed tuple

\[
\mathbf u=(u_1,\ldots,u_k),
\]

`LRC(k)` asks whether some real time `t` satisfies

\[
\|t u_i\|\ge \frac1{k+1}\qquad(i=1,\ldots,k).
\]

This is the usual Lonely Runner Conjecture for `k+1` total runners after passing to speeds relative to one runner.

The 2026 computer-assisted frontier proves

\[
LRC(k)\quad\text{for }k\le 12,
\]

so the next fixed-dimensional open case is

\[
\boxed{LRC(13)\text{ — 14 total runners}.}
\]

The same work explicitly identifies efficient computation of the initial improper set

\[
I(k,p,1)
\]

as the primary bottleneck for extending the proof to `k=13`, and points to stronger pruning of no-witness speed tuples as the needed direction.

That makes this a particularly clean Shakespeare problem: the accepted frontier is already blocked by a representation/search-state issue rather than by lack of a numerical integrator.

## 2. Current research chain

The Sonnet is organized as a sequence of increasingly less naive representations.

### Phase 0 — exact ground truth

[`00-problem-frontier.md`](00-problem-frontier.md)

Executable calibration:

```text
tests/research/test_lonely_runner_phase0.py
```

This phase freezes:

- an exact rational continuous oracle for small integer speed tuples;
- the exact finite `(k,p,l)` ansatz proper/improper predicate;
- the known modulo-`p` quotient by permutation, independent sign flips, and global units;
- tight-threshold red teams;
- a first future-behavior separation: two states can both be improper at `l=1` but differ after all `c=2` lifts.

### Phase 1 — `I(k,p,1)` is fixed-cardinality set cover

[`01-initial-sieve-as-set-cover.md`](01-initial-sieve-as-set-cover.md)

Executable calibration:

```text
tests/research/test_lonely_runner_initial_sieve.py
```

For the half-circle time set

\[
U_p=\{1,\ldots,(p-1)/2\},
\]

each folded speed `s` defines its bad-time subset

\[
C_s=\left\{a\in U_p:\left\|\frac{as}{p}\right\|<\frac1{k+1}\right\}.
\]

Then

\[
(s_1,\ldots,s_k)\in I(k,p,1)
\iff
C_{s_1}\cup\cdots\cup C_{s_k}=U_p.
\]

At `k=3,p=13`, direct rational-grid semantics and this set-cover semantics agree on all 56 folded multisets, giving 14 improper tuples and 3 unit-orbit canonical classes.

A red team also shows that `current cover + depth` is not a sufficient state once a construction grammar constrains which future choices remain admissible.

### Phase 2 — exact task quotient with Shakespeare

[`02-process-jet-quotient.md`](02-process-jet-quotient.md)

Executable calibration:

```text
tests/research/test_lonely_runner_process_jet_quotient.py
```

Using a deliberately simple canonical nondecreasing multiset grammar, Shakespeare's existing `ProcessJetSignature` computes the **entire remaining future task language** on finite worlds.

It does both sides of the job:

- rejects unsound merges such as `(1,4)` / `(1,6)` at `k=3,p=13`;
- certifies safe merges even when current cover sets differ.

Example:

\[
(1,1,4)\equiv_Q(1,4,5)
\qquad(k=5,p=17),
\]

because both have exactly the same accepting two-step continuation `(6,7)`.

Exact class counts:

```text
k=4,p=13:  28 literal partial histories -> 11 task classes
k=5,p=17: 165 literal partial histories -> 19 task classes
```

These are semantic class counts, not runtime speedups.

### Phase 3 — requirement antichain

[`03-requirement-antichain-quotient.md`](03-requirement-antichain-quotient.md)

Executable calibration:

```text
tests/research/test_lonely_runner_requirement_antichain.py
```

For every uncovered time `a`, record the still-admissible future speeds that can repair it:

\[
R_h(a)=\{s:\text{future speed }s\text{ covers }a\}.
\]

Delete duplicates and strict supersets, retaining the inclusion-minimal requirement antichain

\[
\mathcal A(h).
\]

For the canonical grammar, the structural state

\[
\boxed{S(h)=(\text{remaining slots},\text{last speed},\mathcal A(h))}
\]

is proved sufficient to determine the complete future task language.

Compression ladder:

```text
k=4,p=13:
  literal histories       28
  current-cover states    21
  requirement states      16
  exact task classes      11

k=5,p=17:
  literal histories      165
  current-cover states    85
  requirement states      41
  exact task classes      19
```

Thus a substantial part of the semantic quotient has a cheap, intelligible structural explanation.

### Phase 4 — return to the real upstream MRV state

[`04-upstream-mrv-disjoint-requirement-prune.md`](04-upstream-mrv-disjoint-requirement-prune.md)

Executable calibration:

```text
tests/research/test_lonely_runner_upstream_requirement_prune.py
```

This phase transliterates the relevant `vzsky/13-lonely-runners` `find_cover` semantics, including the exact bit ordering, `AvailableChoice` elimination, MRV tie-breaking, optimistic `early_return_bound()`, and top-level worker initialization.

The first strictly stronger pruning certificate appears at `k=5,p=29` in the reachable state

```text
chosen history     (1, 2, 7)
eliminated speed   {5}
remaining slots    2
```

Among its minimal future requirements are the three pairwise-disjoint sets

\[
\{6,11,12\},
\qquad
\{3,8,13\},
\qquad
\{9,10,14\}.
\]

Therefore at least three future choices are necessary, while only two slots remain.  The branch is impossible.

The current upstream optimistic bound does not reject this state: it sees six uncovered positions and obtains

\[
6 = 3 + 3(2-1),
\]

so its strict pruning inequality fails exactly at equality.

Whole-search small-world checks preserve the exact canonical solution sets:

```text
k=5,p=29:  113 -> 110 DFS calls, 1 new prune, 7 solution classes unchanged
k=7,p=37: 1752 -> 1743 DFS calls, 3 new prunes, 177 solution classes unchanged
```

The gains are small.  What Phase 4 establishes is **strictly stronger information**, not practical dominance.

## 3. What Shakespeare has contributed so far

The useful conceptual move was not “rewrite Lonely Runner in new notation.”  It was the representation sequence

```text
current tuple / covered times
        ->
exact future continuation language
        ->
future repair requirements
        ->
minimal requirement antichain
        ->
new exact obstruction on the actual upstream search
```

The difference is important.  Phase 2 first used exhaustive future semantics as an oracle for the correct quotient; Phase 3 then searched backward for a compact invariant explaining part of that quotient; Phase 4 transported the resulting object to the real computational bottleneck.

That is the intended Shakespeare workflow.

## 4. Claim level

Using the `sonnet/` four-level rubric:

1. **re-expression:** achieved;
2. **compression:** achieved on finite state counts, but not yet as a meaningful wall-clock result;
3. **structural discovery:** achieved at calibration level — the requirement-antichain presentation is exact for the canonical grammar and yields a strictly stronger reachable-state prune upstream;
4. **new mathematics:** not achieved — `LRC(13)` remains open.

No claim here improves the published LRC frontier.

## 5. Next phase

The next work should stay close to the actual `I(k,p,1)` bottleneck rather than return to abstract API design.

Priority order:

1. reconstruct the exact primes / parameter sets used in solved upstream `k=8..12` runs and collect node-count baselines;
2. add forced-speed propagation and bounded transversal lower bounds on the requirement antichain;
3. measure **additional prunes versus certificate cost** under identical solution semantics;
4. investigate memoization by reduced requirement presentations while retaining construction provenance needed to reconstruct every candidate tuple;
5. only after a method transfers across solved `k`, freeze it and test `k=13` without retuning the representation grammar.

The next decisive threshold is therefore not another attractive toy merge.  It is a reproducible improvement on solved large instances of the same initial sieve that blocks `LRC(13)`.
