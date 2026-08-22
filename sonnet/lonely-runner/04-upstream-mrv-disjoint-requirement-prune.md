# Phase 4 note — a strictly stronger certificate on the upstream MRV search

**Status:** first direct test against the actual `find_cover` state semantics.  A requirement-disjointness certificate prunes states that the current upstream `early_return_bound()` does not.  The measured gain is small; this is a strictness result, not yet a performance result.

## 1. Why return to the upstream search now

Phases 1–3 deliberately separated a clean canonical grammar from the C++ implementation.  That separation produced an exact process quotient, but it left the main practical question unanswered:

> Does the future-requirement representation reveal anything that the real `find_cover` MRV search does not already know?

To answer this, the Phase-4 executable test transliterates the relevant upstream logic literally:

```text
Context::cover
Dfs::State.covered
AvailableChoice.eliminated / remaining
get_next_to_cover
Dfs::early_return_bound
Dfs::run
find_all_covers_parallel initialization, serialized
```

The bit ordering is preserved as well: upstream stores rational time `t` at bit position `P/2 - t`.  This matters because `get_next_to_cover` resolves ties by the first bit position.

The Python calibration is not proposed as a replacement implementation.  It is an instrumented semantic mirror for small `(k,p)` worlds.

## 2. The upstream optimistic bound

At a partial state, upstream selects the most constrained uncovered time `u`.  With `r` slots remaining it computes roughly

- `bestCovering_next`: the largest number of uncovered positions one available speed can cover while also covering `u`;
- `bestCovering`: the largest number of the other uncovered positions one available speed can cover.

It prunes when

\[
N_{\rm uncovered}
>
B_{\rm next}+(r-1)B.
\]

This is a sound optimistic cardinality bound.  It treats future speed choices independently, however, and therefore does not see incompatibility between *which* speeds can satisfy different outstanding requirements.

## 3. Requirement sets on the real `AvailableChoice` state

For each uncovered time position `a`, define

\[
R(a)=\{s:\ s\text{ is currently available and }C_s\ni a\}.
\]

As in Phase 3, delete duplicate requirement sets and strict supersets, leaving the inclusion-minimal antichain.

Now observe a very cheap family of lower-bound certificates:

> If there are `q` pairwise-disjoint requirement sets, then at least `q` future speed choices are necessary.

Indeed, no one speed token can hit two disjoint requirement sets.  Therefore

\[
q>r
\quad\Longrightarrow\quad
\text{the state is impossible to complete.}
\]

This is a dual obstruction: the upstream bound asks how many uncovered positions a speed *can cover*; requirement disjointness asks how many mutually incompatible future operations are *forced*.

## 4. A strict counterexample to the existing bound: `k=5,p=29`

The exact upstream traversal reaches the state

```text
chosen history:     (1, 2, 7)
eliminated choices: {5}
remaining slots:    2
uncovered times:    {5, 6, 7, 9, 10, 11}
```

The minimal future requirements include

\[
\{6,11,12\},
\qquad
\{3,8,13\},
\qquad
\{9,10,14\}.
\]

These three sets are pairwise disjoint.  Consequently every completion needs at least three future speed choices, but only two slots remain:

\[
\boxed{3>2.}
\]

So the branch is impossible.

The current upstream optimistic bound does **not** prune it.  At this state:

```text
uncovered positions       = 6
bestCovering_next          = 3
bestCovering               = 3
remaining slots            = 2
```

and therefore

\[
6>3+3(2-1)
\]

is false exactly at equality.

This is the first direct evidence that the requirement representation contains pruning information not captured by the current upstream bound.

## 5. Whole-search calibration

The executable test runs both versions from the exact serialized equivalent of upstream initialization.

For `k=5,p=29`:

| metric | upstream bound only | + disjoint-requirement certificate |
|---|---:|---:|
| DFS calls | 113 | 110 |
| new disjoint prunes | 0 | 1 |
| canonical solution classes | 7 | 7 |

For an independent larger calibration `k=7,p=37`:

| metric | upstream bound only | + disjoint-requirement certificate |
|---|---:|---:|
| DFS calls | 1752 | 1743 |
| new disjoint prunes | 0 | 3 |
| canonical solution classes | 177 | 177 |

The solution sets are compared exactly, not just their cardinalities.

The reduction is small.  That is useful information: **we have proved strictness, not practical dominance.**  A one-branch improvement at `k=5,p=29` is not evidence that the same certificate will materially change the `k=13` computation.

## 6. Why this still matters

The open `k=13` bottleneck is explicitly the initial `I(k,p,1)` sieve and the need for stronger pruning of no-witness tuples.  Phase 4 now gives the Sonnet line its first end-to-end chain:

```text
LRC no-witness tuple
    -> set-cover process
    -> future requirement presentation
    -> exact task quotient
    -> cheap structural obstruction
    -> branch rejected where current upstream bound survives
```

The new obstruction is elementary once stated.  The value of Shakespeare here is not that disjoint set families are novel mathematics; it is that the process-first representation led systematically from semantic equivalence to the dual requirement object where this certificate becomes obvious.

That is the level of claim appropriate at this stage.

## 7. What should be tried next

Pairwise-disjoint packing uses only a small part of the requirement hypergraph.  The natural ladder is:

1. **singleton / forced-speed propagation**;
2. **disjoint requirement packing**;
3. **small exact transversal lower bound** up to `r+1` choices;
4. **memoization by reduced requirement presentation**;
5. compare each against upstream node counts on the actual primes used for solved `k` runs.

The important experimental discipline is incremental: every stronger certificate must report

```text
additional prunes
certificate cost
visited-node reduction
unchanged canonical solution set
```

and should be removed if its overhead dominates its pruning value.

## 8. Claim boundary

Phase 4 does not improve the published `LRC(k)` frontier and does not establish a wall-clock speedup.  The Python mirror is used only for small exact calibration, and the disjointness search itself has not yet been engineered for the large-prime `k=13` regime.

What is established is narrower but concrete:

\[
\boxed{
\text{the Shakespeare-derived future-requirement view yields a sound pruning certificate strictly stronger than the current upstream optimistic bound on reachable MRV states.}
}
\]
