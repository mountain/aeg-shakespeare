# Phase 6 — frozen-rule probes on the open `K=13` case

**Status:** first three predeclared top-level workers complete; all preserve exact output and all benefit from the frozen solved-case rule.  
**Open target:** `LRC(13)`, i.e. 14 total runners.

## 1. Why the experiment is deliberately worker-sized

Phase 5c closed the solved-case transfer gate: the same two-slot certificate,
without retuning, preserved complete canonical `find_cover` outputs and produced a
net speedup on the actual pinned upstream source from `K=8` through `K=12`.

That permits an open-case experiment, but not an uncontrolled full search.

The first `K=13` experiment therefore freezes all choices *before* observing any
open-case result:

```text
upstream SHA       755b116b2e6090cd4a83187a696f863388b7d746
K                  13
p                  199   (first prime in the current K=13 configuration)
first worker        0
pruning rule       unchanged Phase-5 exact two-slot certificate
per-variant bound  300 s
```

No threshold, representation, branch ordering, lookahead depth, or heuristic is
allowed to change in response to `K=13` data.

After worker 0 completed inside the bound, the protocol allowed the next two
workers, in index order, solely as a transfer/imbalance red team.  The rule remained
frozen.

## 2. Exact upstream worker decomposition

The Phase-6 harness reconstructs the top-level decomposition literally from
`find_all_covers_parallel<P,K>()`:

1. fix the first speed at `1`;
2. compute the upstream MRV time position;
3. form the same `coord2_candidates`;
4. precompute the same `AvailableChoice` states after earlier sibling eliminations;
5. instantiate the actual upstream `Dfs<P,K>` for exactly one candidate.

For `K=13,p=199`, there are 14 workers:

```text
second speed = 2,4,6,8,10,12,14,16,18,20,22,24,26,28
```

Thus the first three probes are fixed prefixes

```text
worker 0  -> (1,2)
worker 1  -> (1,4)
worker 2  -> (1,6)
```

rather than workers selected after inspecting runtimes.

## 3. Exact open-case results

Each worker is compiled and run twice against the actual pinned upstream source:

```text
baseline  = untouched find_cover.h
patched   = same source + frozen Phase-5 two-slot certificate
```

For every completed worker, the entire canonical solution set is serialized,
sorted, and compared byte-for-byte before a performance claim is accepted.

All three comparisons pass.

| worker | prefix | canonical classes | baseline | patched | speedup | reduction | exact-set SHA-256 |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 0 | `(1,2)` | 1,235,622 | 184.914 s | 165.732 s | **1.116x** | 10.4% | `dcc33044a2ce577df5e13deef9082624fb5ab6050ad8f3dbe15994d5fa069e45` |
| 1 | `(1,4)` | 3,020,996 | 260.647 s | 216.269 s | **1.205x** | 17.0% | `19b58483bfa4bf5bafa3042f46c3b64f57c430286a93a9ccac54c4b5fbe6e841` |
| 2 | `(1,6)` | 3,463,105 | 204.395 s | 195.240 s | **1.047x** | 4.5% | `f4ff7e2f7d0d4dc52a0930c09d43243c457b6bec4f7bd715d6b46a905b77eeba` |

All runs use GitHub-hosted Ubuntu 24.04 runners with `g++ 13.3.0` and

```text
-O3 -std=c++23 -pthread -march=native
```

within each baseline/patched pair.  Workers 1 and 2 ran on separate hosted runners,
so their absolute times should not be aggregated into a synthetic full-sieve wall
time.  The within-worker ratios are the robust measurements.

## 4. What the three-worker red team says

The transfer signal survives three consecutive, non-cherry-picked workers:

```text
worker 0: +10.4%
worker 1: +17.0%
worker 2:  +4.5%
```

So worker 0 was not an isolated branch accident.

At the same time, the variation is substantial.  The certificate's value depends
on the residual requirement geometry of each top-level branch, which is exactly
what one should expect from a task-relative representation rather than a uniform
micro-optimization.

The canonical output volume also varies strongly:

```text
1.24M -> 3.02M -> 3.46M classes
```

which warns against extrapolating the full `p=199` cost from a single worker.

## 5. What this establishes

The representation-development chain has now crossed the solved/open boundary in a
nontrivial way:

```text
small exact ProcessJet future languages
    -> requirement antichain
    -> transversal semantics
    -> cost-selected two-slot certificate
    -> frozen transfer K=8..12
    -> three consecutive actual-upstream K=13 workers
```

The important result is not any single percentage.  It is the experimental
protocol:

```text
discover and select the representation only on solved cases
freeze it
move across the theorem frontier
preserve complete open-case worker outputs
observe a positive net gain without retuning
```

This rules out several weaker explanations:

- the advantage is not restricted to toy examples;
- it is not restricted to Python;
- it is not restricted to our C++ reconstruction;
- it does not disappear immediately at the open `K=13` scale;
- it is not specific to one preselected open-case worker;
- it was not selected by inspecting `K=13` performance first.

## 6. What this does **not** establish

Phase 6 does not prove `LRC(13)` and does not show that the complete open-case
verification is feasible.

In particular:

- three workers are not the full 14-worker `p=199` initial sieve;
- the remaining workers may be substantially heavier;
- canonical solution sets from different workers can overlap after global unit
  normalization, so their counts cannot simply be summed;
- the current `K=13` program uses many primes, not only `p=199`;
- later lifting/projection stages remain outside this benchmark;
- gains between roughly 5% and 17% are scientifically real but far from the
  orders-of-magnitude improvement one would want before claiming that the open
  computation itself has become easy.

## 7. Research discipline after touching the open case

The `K=13` workers must now be treated as a **holdout**, not as a tuning set.

A stronger Shakespeare presentation should not be invented by inspecting which
`K=13` branches remain expensive.  Instead the next discovery cycle should return
to solved instances (`K<=12`), develop and red-team any stronger quotient or
certificate there, freeze it, and only then transfer it across the frontier again.

Likewise, launching all 14 `p=199` workers now would mostly measure brute-force
scale.  It may be useful later for end-to-end accounting, but it is not the next
best test of the representation hypothesis.

## 8. Claim level

Under the Sonnet rubric, Phase 6 remains Level 3 rather than Level 4:

- **compression:** demonstrated on three real open-case workers;
- **structural discovery:** the same solved-case future-requirement representation
  continues to have operational value beyond the known theorem frontier;
- **new mathematics:** not achieved; no new Lonely Runner case has been proved.

The strongest defensible statement is:

> **A process-future representation discovered and selected entirely on solved
> instances yields a frozen exact pruning certificate that preserves the complete
> outputs of the first three real `K=13,p=199` upstream workers and reduces each
> worker's solve time, by about 4.5% to 17% in these measurements.**
