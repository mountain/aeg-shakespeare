# Phase 5c — pinned upstream `find_cover` benchmark

**Status:** exact upstream-source transfer achieved through the solved `K=12` frontier; `K=13` remains untouched in this phase.

## 1. Purpose

Phases 5 and 5b left one implementation-level ambiguity.

The exact two-slot certificate had already shown:

1. soundness in the Python semantic mirror;
2. substantial deterministic node reductions on configured solved parameters;
3. net speedups in an independent C++23 / `std::bitset` reconstruction.

But the C++ reconstruction was still *our* implementation of the upstream semantics.
The remaining question was:

> Does the same frozen certificate preserve exact outputs and remain a net win when
> compiled directly against the current upstream `find_cover.h` source?

Phase 5c answers that question with a pinned, reproducible GitHub Actions benchmark.

## 2. Pinned source and build

The dedicated workflow

```text
.github/workflows/sonnet-lonely-runner-upstream-bench.yml
```

clones

```text
https://github.com/vzsky/13-lonely-runners
```

and checks out exactly

```text
755b116b2e6090cd4a83187a696f863388b7d746
```

before making two copies:

```text
upstream-baseline/   untouched
upstream-patched/    phase5-two-slot-find-cover.patch applied
```

The benchmark harness is then compiled twice against those two upstream source
trees.  The successful reference run used:

```text
Ubuntu 24.04 hosted runner
4 logical CPUs
g++ 13.3.0
-O3 -std=c++23 -pthread -march=native
```

No source other than `src/find_cover.h` is changed in the patched checkout.

## 3. Exact canonical-set equality

Before timing is accepted, the workflow serializes every canonical solution returned
by `find_all_covers_parallel<P,K>()`, sorts the serialized tuples, and compares the
baseline and patched files byte-for-byte.

The equality check passes from `K=8` through the current solved frontier `K=12`:

| `K` | `p` | canonical classes | SHA-256 of sorted exact set |
| ---: | ---: | ---: | --- |
| 8 | 79 | 442 | `19e7676dd8b93337528427e34e93eeb676398cf9bf2bf56db7ab0a695ee4cde4` |
| 9 | 89 | 1,382 | `6592161f6521096779a65c851f41e0da254dfb72f1c8b645d2d6dade4b111c5b` |
| 10 | 127 | 8,228 | `7de33735d72cb7ecdc6f6169a77ed6b93bdba18a73d42e25f9c47633151ab328` |
| 11 | 131 | 40,615 | `2c6f57d4ca0d809d68c2f66e3122eee09685cb4856bed1860247aa1719de0fcb` |
| 12 | 139 | 641,960 | `913fb4de316be14928cb09621b9f66fd57adff418e70247651605bbbc3dc8b0e` |

The larger `K=11,12` files are deleted after comparison to avoid unnecessary
artifact storage, but their counts and hashes remain in the workflow log.

This is stronger than comparing only `S.size()`.

### Legacy-count correction

Historical upstream result logs sometimes report much larger `Step1` set sizes,
for example millions of tuples at `K=11,12`.  Those logs come from earlier stages /
formats and must not be used as expected values for the current pinned source.

The current `find_cover` inserts

```text
state.elems.get_canonical_representation(P)
```

into its solution set.  Phase 5c therefore treats the current source itself as the
semantic baseline and verifies its complete canonical output directly.

## 4. Repeated timing results

The successful reference workflow uses three warmups and fifteen timed repetitions
for `K=8..10`.  For the larger frontier transfer it uses one warmup plus five
repetitions at `K=11`, and one warmup plus three repetitions at `K=12`.

Median timings on the same runner:

| `K,p` | baseline | two-slot patch | median speedup | time reduction |
| --- | ---: | ---: | ---: | ---: |
| `8,79` | 4.842 ms | 4.003 ms | **1.210x** | 17.3% |
| `9,89` | 20.642 ms | 17.604 ms | **1.173x** | 14.7% |
| `10,127` | 450.341 ms | 373.116 ms | **1.207x** | 17.1% |
| `11,131` | 1.630 s | 1.416 s | **1.151x** | 13.2% |
| `12,139` | 18.656 s | 15.527 s | **1.201x** | 16.8% |

The individual numbers are machine-dependent.  The robust signal is the transfer
pattern:

```text
same unretuned rule
same upstream source revision
same runner and compiler per comparison
complete output equality
positive median speedup at every tested K = 8..12
```

The gain does not collapse as the search reaches the solved frontier.

## 5. Why this closes the Phase-5 transfer gate

The experimental chain is now

```text
ProcessJetSignature future-language oracle
    -> requirement antichain
    -> transversal semantics
    -> exact two-slot shadow selected by cost
    -> deterministic node reductions
    -> independent C++ cost survival
    -> pinned upstream source patch
    -> byte-identical canonical outputs K=8..12
    -> net upstream find_cover speedups K=8..12
```

No parameter, rule, threshold, or lookahead depth was retuned when moving from
`K=8` to `K=12`.

That matters more than the absolute 13–20% wall-time gain.  It establishes that the
representation-derived certificate is not fitted to one calibration world.

## 6. Claim boundary

Phase 5c still does **not**:

- prove `LRC(13)`;
- improve the published mathematical frontier;
- benchmark the complete lifting/projection proof pipeline;
- show that a 13–20% `find_cover` gain is enough to make the open `K=13` case
  computationally feasible;
- justify changing the public Shakespeare API.

The result is narrower:

> **The frozen Shakespeare-derived two-slot completion certificate is sound on the
> actual pinned upstream `find_cover` source, preserves complete canonical outputs,
> and produces a reproducible net speedup across configured solved probes from
> `K=8` through `K=12`.**

## 7. Next experiment: frozen-rule probe at open `K=13`

The transfer protocol now permits one carefully bounded open-case experiment.

We should not immediately launch the entire `K=13` sieve.  Instead:

1. use the current upstream `K=13` prime list without changing the rule;
2. expose the same serialized top-level worker decomposition used by
   `find_all_covers_parallel`;
3. replay one or a few workers at the first configured prime (`p=199`);
4. compare baseline and patched worker output sets and traversal/wall cost;
5. extrapolate only after measuring worker imbalance and total candidate volume.

This keeps the first open-case probe auditable and prevents a large computation
from hiding whether the representation advantage itself transferred.
