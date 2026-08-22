# Lonely Runner — Sonnet 001

**Status:** Phase 5c — frozen two-slot certificate validated on the actual pinned upstream `find_cover` source through the solved `K=12` frontier.  
**Target open case:** `LRC(13)`, i.e. **14 total runners**.

## 1. Problem

For a positive integer relative speed tuple

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

Thus the initial modular sieve is a finite set-cover completion process.

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

Executable calibration:

```text
tests/research/test_lonely_runner_two_slot_transversal.py
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

The strongest useful Pareto point found so far is not full four-slot lookahead but the exact **two-slot** specialization:

\[
\boxed{\exists s,t\in A:\ U\subseteq C_s\cup C_t}
\]

where `U` is the current uncovered-time bitset and `A` the currently available speeds. If no such pair exists, the branch is impossible.

The Python semantic mirror already showed material node reductions, including about 35.5% over the first five `k=10,p=127` top-level workers. Stronger three/four-slot lookahead removes more nodes but can lose on certificate cost, making the two-slot rule the first stable cost/strength Pareto point.

### Phase 5b — independent C++ cost survival

[`06-cpp-semantic-mirror-and-upstream-patch.md`](06-cpp-semantic-mirror-and-upstream-patch.md)

Standalone C++ mirror:

```text
sonnet/lonely-runner/cpp/phase5_two_slot_bench.cpp
```

Prepared minimal patch:

```text
sonnet/lonely-runner/patches/phase5-two-slot-find-cover.patch
```

The independent C++23 / `std::bitset` mirror reproduces the deterministic Python node/leaf counts and shows that the two-slot certificate remains cheap enough to produce a net speedup in C++.

This eliminated the explanation that the Phase-5 advantage was merely an artifact of Python search overhead, but still left one gap: it was our C++ reconstruction rather than the upstream implementation itself.

### Phase 5c — pinned actual-upstream benchmark

[`07-pinned-upstream-find-cover-benchmark.md`](07-pinned-upstream-find-cover-benchmark.md)

Pinned benchmark workflow:

```text
.github/workflows/sonnet-lonely-runner-upstream-bench.yml
```

Harness compiled directly against upstream source:

```text
sonnet/lonely-runner/cpp/upstream_find_cover_harness.cpp
```

The workflow clones the upstream repository and pins exactly

```text
755b116b2e6090cd4a83187a696f863388b7d746
```

before compiling baseline and patched harnesses against the two source trees with the same compiler and flags.

Before any timing result is accepted, the complete canonical solution sets are serialized, sorted, and compared byte-for-byte. Equality holds from `K=8` through the solved `K=12` frontier:

| `K` | `p` | canonical classes | exact-set SHA-256 |
| ---: | ---: | ---: | --- |
| 8 | 79 | 442 | `19e7676dd8b93337528427e34e93eeb676398cf9bf2bf56db7ab0a695ee4cde4` |
| 9 | 89 | 1,382 | `6592161f6521096779a65c851f41e0da254dfb72f1c8b645d2d6dade4b111c5b` |
| 10 | 127 | 8,228 | `7de33735d72cb7ecdc6f6169a77ed6b93bdba18a73d42e25f9c47633151ab328` |
| 11 | 131 | 40,615 | `2c6f57d4ca0d809d68c2f66e3122eee09685cb4856bed1860247aa1719de0fcb` |
| 12 | 139 | 641,960 | `913fb4de316be14928cb09621b9f66fd57adff418e70247651605bbbc3dc8b0e` |

On one successful 4-core GitHub-hosted runner (`g++ 13.3.0`, `-O3 -std=c++23 -pthread -march=native`), median `find_cover` timings were:

| `K,p` | baseline | patched | speedup | reduction |
| --- | ---: | ---: | ---: | ---: |
| `8,79` | 4.842 ms | 4.003 ms | **1.210x** | 17.3% |
| `9,89` | 20.642 ms | 17.604 ms | **1.173x** | 14.7% |
| `10,127` | 450.341 ms | 373.116 ms | **1.207x** | 17.1% |
| `11,131` | 1.630 s | 1.416 s | **1.151x** | 13.2% |
| `12,139` | 18.656 s | 15.527 s | **1.201x** | 16.8% |

The absolute timings are machine-dependent. The important transfer statement is stronger and cleaner:

```text
one frozen rule
one pinned upstream revision
no K-specific retuning
complete canonical output equality
positive median speedup at every tested K = 8..12
```

This closes the solved-case transfer gate that was set before any open-case experiment was attempted.

## 3. What Shakespeare has contributed

The research chain is now:

```text
literal search history
    -> exact future continuation semantics
    -> future repair requirements
    -> requirement antichain
    -> transversal feasibility
    -> cost-selected exact two-slot certificate
    -> deterministic node reduction
    -> C++ cost survival
    -> minimal patch to actual pinned upstream source
    -> byte-identical canonical outputs K=8..12
    -> net upstream find_cover speedups K=8..12
```

This is not merely a new notation for an existing algorithm. The key structure was found by first computing the correct future semantics, then explaining the resulting equivalence classes with a compact representation, and finally lowering that representation into a cheap certificate for the frontier solver.

The cost red team is equally important. Shakespeare should not maximize semantic strength blindly. The operative objective is a Pareto frontier over

\[
\text{semantic strength},\quad
\text{search reduction},\quad
\text{certificate cost},\quad
\text{reconstruction/provenance cost}.
\]

## 4. Claim level

Using the `sonnet/` rubric:

1. **re-expression:** achieved;
2. **compression:** achieved on actual pinned upstream searches across solved configurations;
3. **structural discovery:** achieved — future-requirement/transversal structure yields a new exact pruning certificate and a reproducible implementation gain;
4. **new mathematics:** not achieved — `LRC(13)` remains open.

Nothing through Phase 5c improves the published Lonely Runner mathematical frontier.

## 5. Next threshold — Phase 6 frozen open-case probe

The protocol now permits a carefully bounded experiment on `K=13`.

The rule must remain completely frozen. We will **not** retune the lookahead depth, threshold, presentation, or search heuristic after seeing open-case data.

The first experiment should not launch the entire `K=13` initial sieve. Instead:

1. use the current upstream `K=13` configured prime list unchanged;
2. start at its first configured prime, `p=199`;
3. expose exactly the same top-level worker decomposition used by `find_all_covers_parallel`;
4. replay one worker baseline vs patched;
5. compare complete worker canonical solution sets and wall time;
6. expand to a few workers only if the first probe remains tractable;
7. extrapolate total cost only after measuring worker imbalance.

The first open-case question is therefore deliberately narrow:

\[
\boxed{\text{Does the frozen solved-case representation advantage transfer to one real }K=13\text{ worker?}}
\]

A positive answer would still not prove `LRC(13)`, but it would be the first experiment in this Sonnet to touch the actual open-case search without changing the representation discovered on solved instances.
