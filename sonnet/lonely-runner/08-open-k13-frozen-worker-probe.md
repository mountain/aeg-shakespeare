# Phase 6 — first frozen-rule probe on the open `K=13` case

**Status:** worker 0 complete and positive; adjacent workers are used only as a transfer/imbalance check.  
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
worker index       0
pruning rule       unchanged Phase-5 exact two-slot certificate
per-variant bound  300 s
```

No threshold, representation, branch ordering, lookahead depth, or heuristic is
allowed to change in response to `K=13` data.

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

Thus worker 0 is the unselected first branch with literal construction prefix

```text
(1,2)
```

rather than an easy worker chosen after inspecting runtimes.

## 3. Worker 0 result

The dedicated GitHub Actions run compiles the harness twice against the actual
pinned upstream source, once untouched and once with the already-frozen two-slot
patch.

Both variants finish within the predeclared 300-second bound.

### Exact output

Each worker returns

```text
1,235,622 canonical classes
```

The complete sets are serialized, sorted, and compared byte-for-byte.  They are
identical.

Stable SHA-256 of the complete worker output:

```text
dcc33044a2ce577df5e13deef9082624fb5ab6050ad8f3dbe15994d5fa069e45
```

This is the first exact Shakespeare calibration performed inside a real search
branch of the open `LRC(13)` case.

### Solve time

On the same 4-core GitHub-hosted runner (`g++ 13.3.0`, `-O3 -std=c++23 -pthread
-march=native`), the single-threaded `Dfs` worker solve times are:

```text
baseline   184,914.199 ms
patched    165,732.075 ms
```

Therefore

\[
\text{speedup}\approx1.116\times,
\]

or approximately

\[
\boxed{10.4\%}
\]

less worker solve time.

The serialization/sorting time is not included in those solve times and does not
enter the baseline/patched comparison.

## 4. What this establishes

The representation-development chain has now crossed the solved/open boundary:

```text
small exact ProcessJet future languages
    -> requirement antichain
    -> transversal semantics
    -> cost-selected two-slot certificate
    -> frozen transfer K=8..12
    -> actual upstream open K=13 worker
```

The important experimental fact is not the 10.4% number by itself.  It is that the
rule was fixed entirely on solved cases and then produced a positive net result on
the first predeclared open-case worker while preserving its complete canonical
output.

That rules out several weaker explanations:

- the advantage is not restricted to toy examples;
- it is not restricted to Python;
- it is not restricted to our C++ reconstruction;
- it does not disappear immediately at the open `K=13` scale;
- it was not selected by inspecting `K=13` performance first.

## 5. What this does **not** establish

This result does not prove `LRC(13)` and does not yet show that the full open-case
verification is feasible.

In particular:

- one worker is not the full `p=199` initial sieve;
- the 14 workers can have strongly unequal cost;
- canonical solution sets from different workers can overlap after global unit
  normalization, so their counts cannot simply be summed;
- the current `K=13` program uses many primes, not only `p=199`;
- later lifting/projection stages remain outside this benchmark;
- a 10% local gain may be scientifically real while still being computationally
  insufficient to close the open case.

## 6. Immediate red team — adjacent workers

The protocol permits a small expansion only because worker 0 finished inside its
predeclared bound.

Workers 1 and 2, corresponding to second speeds `4` and `6`, are therefore run in
parallel under exactly the same 300-second-per-variant rule.  Their purposes are:

1. test whether the worker-0 gain is an isolated branch accident;
2. expose top-level worker imbalance before any full-sieve extrapolation;
3. obtain additional exact canonical-set equality checks without altering the
   certificate.

No further rule development should use these open-case results as a tuning set.
If a stronger presentation is sought later, it must again be developed/frozen on
solved instances before transfer to `K=13`.

## 7. Claim level

Under the Sonnet rubric, Phase 6 remains Level 3 rather than Level 4:

- **compression:** now demonstrated on one real open-case worker;
- **structural discovery:** the same solved-case representation continues to have
  operational value beyond the known theorem frontier;
- **new mathematics:** not achieved; no new Lonely Runner case has been proved.

The strongest defensible statement is:

> **A process-future representation discovered entirely on solved instances yields
> a frozen exact pruning certificate that preserves the complete output of the
> first real `K=13,p=199` upstream worker and reduces its solve time by about 10%.**
