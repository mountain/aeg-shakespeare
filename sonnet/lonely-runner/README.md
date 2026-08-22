# Lonely Runner — Sonnet 001

**Status:** Phase 5b — bounded transversal transferred to configured solved primes, C++ semantic mirror validated, minimal upstream patch prepared.  
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

The same work identifies efficient computation of the initial improper set

\[
I(k,p,1)
\]

as the primary bottleneck for extending the proof to `k=13`, and explicitly points toward stronger pruning of no-witness speed tuples.

This is therefore a direct representation/search-state problem rather than a decorative application of Shakespeare.

## 2. Research chain

### Phase 0 — exact ground truth

[`00-problem-frontier.md`](00-problem-frontier.md)

Executable calibration:

```text
tests/research/test_lonely_runner_phase0.py
```

Freezes the exact continuous oracle, finite `(k,p,l)` properness semantics, the known modulo-`p` quotient, tight-threshold red teams, and a first lift-future separation.

### Phase 1 — `I(k,p,1)` as fixed-cardinality set cover

[`01-initial-sieve-as-set-cover.md`](01-initial-sieve-as-set-cover.md)

Executable calibration:

```text
tests/research/test_lonely_runner_initial_sieve.py
```

For the half-circle time set

\[
U_p=\{1,\ldots,(p-1)/2\},
\]

each folded speed `s` defines

\[
C_s=\left\{a\in U_p:\left\|\frac{as}{p}\right\|<\frac1{k+1}\right\}.
\]

Then exactly

\[
(s_1,\ldots,s_k)\in I(k,p,1)
\iff
C_{s_1}\cup\cdots\cup C_{s_k}=U_p.
\]

The initial modular sieve is therefore a finite set-cover completion process.

### Phase 2 — exact task quotient with Shakespeare

[`02-process-jet-quotient.md`](02-process-jet-quotient.md)

Executable calibration:

```text
tests/research/test_lonely_runner_process_jet_quotient.py
```

`ProcessJetSignature` is used as an exhaustive finite oracle for the complete future task language. It both rejects unsafe state merges and certifies nontrivial safe merges.

Representative class compression:

```text
k=4,p=13:  28 literal partial histories -> 11 task classes
k=5,p=17: 165 literal partial histories -> 19 task classes
```

### Phase 3 — requirement antichain

[`03-requirement-antichain-quotient.md`](03-requirement-antichain-quotient.md)

Executable calibration:

```text
tests/research/test_lonely_runner_requirement_antichain.py
```

For each uncovered time `a`, define the available future repairs

\[
R_h(a)=\{s:\text{future speed }s\text{ covers }a\}.
\]

Delete duplicate requirements and strict supersets, retaining the inclusion-minimal antichain

\[
\mathcal A(h).
\]

For the canonical grammar,

\[
(\text{remaining slots},\text{last speed},\mathcal A(h))
\]

is sufficient to determine the complete future task language.

### Phase 4 — return to the real upstream MRV state

[`04-upstream-mrv-disjoint-requirement-prune.md`](04-upstream-mrv-disjoint-requirement-prune.md)

Executable calibration:

```text
tests/research/test_lonely_runner_upstream_requirement_prune.py
```

This phase transliterates the relevant upstream `find_cover` semantics, including bit ordering, `AvailableChoice`, MRV tie-breaking, optimistic `early_return_bound()`, sibling elimination, and top-level worker initialization.

The requirement representation yields the first reachable state pruned by Shakespeare-derived information but not by the existing upstream optimistic bound. Small-world whole-search gains are intentionally modest; Phase 4 establishes strictness, not practical dominance.

### Phase 5 — bounded transversal as a cost-selected exact certificate

[`05-bounded-transversal-prune.md`](05-bounded-transversal-prune.md)

Executable CI calibration:

```text
tests/research/test_lonely_runner_two_slot_transversal.py
```

Manual configured-worker benchmark:

```text
python sonnet/lonely-runner/bench_phase5_two_slot.py
```

The requirement hypergraph has transversal number

\[
\tau(\mathcal A)=\min\{|H|:H\cap R\ne\varnothing\text{ for every }R\in\mathcal A\}.
\]

With `r` slots remaining,

\[
\tau(\mathcal A)>r
\]

is an exact impossibility certificate for the remaining `I(k,p,1)` set-cover task.

The first useful Pareto point is not full four-slot lookahead but the exact **two-slot** specialization:

\[
\boxed{\exists s,t\in A:\ U\subseteq C_s\cup C_t}
\]

where `U` is the current uncovered-time bitset and `A` the currently available speeds. If no such pair exists, the branch is impossible.

Complete configured-prime mirrors give:

```text
k=8,p=79:   39,813 -> 28,828 nodes   (-27.6%)
k=8,p=83:  113,488 -> 91,335 nodes   (-19.5%)
k=9,p=89:  161,820 -> 112,951 nodes  (-30.2%)
```

For `k=8,p=79` and `k=9,p=89`, the complete accepted raw history sets are compared directly and are identical before and after pruning.

For current-config `k=10,p=127`, the first five serialized top-level workers give:

| second speed | baseline | + 2-slot | reduction | new prunes | accepted leaves |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2  | 376,376 | 264,486 | 29.7% | 17,022 | 2,822 |
| 4  | 505,777 | 322,126 | 36.3% | 28,063 | 8,041 |
| 6  | 543,301 | 345,043 | 36.5% | 30,261 | 19,176 |
| 8  | 394,315 | 244,797 | 37.9% | 22,958 | 8,841 |
| 10 | 316,729 | 201,286 | 36.5% | 18,319 | 7,454 |

Aggregate:

\[
2,136,498\to1,377,738
\]

or about **35.5% fewer nodes**.

A key red-team result is that stronger 3/4-slot exact lookahead removes still more nodes but can lose on certificate cost. The two-slot rule is presently the best stable representation/certificate Pareto point in the Python semantic mirror.

### Phase 5b — C++ semantic mirror and minimal upstream bridge

[`06-cpp-semantic-mirror-and-upstream-patch.md`](06-cpp-semantic-mirror-and-upstream-patch.md)

Standalone C++ benchmark:

```text
sonnet/lonely-runner/cpp/phase5_two_slot_bench.cpp
```

Prepared source patch:

```text
sonnet/lonely-runner/patches/phase5-two-slot-find-cover.patch
```

The C++23 / `std::bitset` mirror reproduces the Python deterministic node and accepted-leaf counts exactly. In one local `g++ 14.2 -O3 -march=native` diagnostic run, the two-slot rule remained a net win:

```text
k=8,p=79:  about 10.2 ms -> 8.7 ms
k=9,p=89:  about 45.5 ms -> 33.3 ms
```

All first five `k=10,p=127` workers also improved in that standalone C++ realization, individually by roughly `1.1x–1.45x`.

This is **not yet an upstream benchmark**. Its purpose is to eliminate a major alternative explanation: the certificate is not useful only because of Python-specific search costs. The remaining implementation uncertainty is now the exact upstream source/build/threading environment.

## 3. What Shakespeare has contributed

The chain is now:

```text
literal search history
    -> exact future continuation semantics
    -> future repair requirements
    -> requirement antichain
    -> transversal feasibility
    -> cost-selected two-slot certificate
    -> configured solved-prime node reduction
    -> C++ bitset cost survival
    -> prepared minimal upstream patch
```

This is stronger than translating an existing algorithm into new notation. The key structure was discovered by first computing exact future semantics, then explaining the resulting equivalence classes, then lowering that explanation back into a cheap certificate for the frontier solver.

The cost red team is equally important: Shakespeare should not maximize semantic strength blindly. The operative objective is a Pareto frontier over

\[
\text{semantic strength},\quad
\text{search reduction},\quad
\text{certificate cost},\quad
\text{reconstruction/provenance cost}.
\]

## 4. Claim level

Using the `sonnet/` rubric:

1. **re-expression:** achieved;
2. **compression:** achieved in exact state/node counts on configured solved parameters;
3. **structural discovery:** achieved — future-requirement/transversal structure produces pruning not present in the upstream bound and survives a C++ realization;
4. **new mathematics:** not achieved — `LRC(13)` remains open.

Phase 5b still does **not** improve the published Lonely Runner frontier.

## 5. Next threshold

The next step is now extremely specific:

1. apply the prepared patch to the exact upstream `find_cover.h` revision;
2. compile with the upstream command and threading setup;
3. verify output identity or stable hashes over solved `K=8..10` primes;
4. measure `find_cover` wall time and total proof-pipeline time;
5. if the net gain survives, freeze the rule and extend to configured `K=11,12` primes;
6. only after that transfer should the frozen rule be tried on exploratory `K=13` parameters.

The decisive question has narrowed from mathematics to implementation: does the cheapest exact shadow discovered by Shakespeare remain a net win **inside the actual solver that defines the current frontier**?
