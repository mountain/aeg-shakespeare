# Phase 5 — bounded transversal pruning on solved upstream parameters

**Status:** first transfer beyond tiny calibration worlds; exact search-state certificate, not yet an upstream C++ benchmark.

## 1. Why Phase 4 was only the first shadow

Phase 4 used the requirement antichain

\[
\mathcal A(h)=\min_{\subseteq}\{R_h(a):a\text{ uncovered}\}
\]

and obtained a safe lower bound from pairwise-disjoint requirements.  If more than
`r` requirements are pairwise disjoint while only `r` speed slots remain, no
completion is possible.

That certificate is exact when it fires, but it ignores the dominant case in which
requirements overlap without admitting a small common transversal.

The natural invariant is therefore not the packing number of the requirement
hypergraph but its transversal number

\[
\tau(\mathcal A)=\min\{|H|: H\cap R\ne\varnothing\text{ for every }R\in\mathcal A\}.
\]

For an upstream `find_cover` state with `r` slots left,

\[
\boxed{\tau(\mathcal A)>r\Longrightarrow\text{the branch is impossible}.}
\]

In fact, for the pure `I(k,p,1)` set-cover stage this is stronger than a one-way
bound: a set of at most `r` currently available speeds hits every requirement iff
those speeds cover every still-uncovered rational time position.  Thus bounded
transversal feasibility is exactly the remaining set-cover task semantics, before
provenance/canonicalization of successful completions is considered.

## 2. Why this can be computationally reasonable

A generic hitting-set computation would be the wrong replacement: it would merely
embed another exponential search inside `find_cover`.

The existing upstream code already changes regime near the leaves.  Its optimistic
`early_return_bound()` only activates once the search depth reaches `k-4`.  Thus the
new certificate can be restricted to at most four remaining choices.

A bounded decision procedure is then shallow:

```text
can_cover(U, A, r):
    if U is empty: accept
    if r == 0: reject
    choose an uncovered time with the fewest available covering speeds
    branch on those covering speeds
    remove all times covered by the chosen speed
    recurse with r - 1
```

Here `U` is the uncovered-time bitset and `A` is the current upstream
`AvailableChoice` set.  This is the same future semantics exposed by the Phase-2
`ProcessJetSignature`, but lowered to the structural bitset presentation discovered
in Phases 3–4.

## 3. The two-slot specialization is the first practical Pareto point

The full four-slot lookahead reduces more nodes, but a Python semantic mirror shows
that its certificate cost can erase the traversal savings.  The first useful
cost/strength point is much simpler: invoke exact feasibility only when two slots
remain.

With uncovered set `U` and available speeds `A`, the branch survives iff

\[
\exists s,t\in A\quad U\subseteq C_s\cup C_t.
\]

This can be checked with bitsets without constructing a generic hypergraph solver.
Choose the most constrained uncovered time `a`; every valid pair contains some
`s` covering `a`.  For each such `s`, form

\[
U_s=U\setminus C_s
\]

and ask whether any available `t` covers `U_s` completely.

The certificate therefore has a very small and auditable contract:

```text
remaining slots == 2
no available pair covers all remaining time bits
    -> prune
```

It is strictly stronger than the current optimistic cardinality bound because it
retains overlap geometry between the candidate cover sets.

## 4. Transfer to primes already present in the upstream solved configuration

The current upstream `main.cpp` lists, among others, the primes `79,83` for `K=8`,
`89` for `K=9`, and `127` for `K=10`.  The Phase-5 executable mirror uses the same
`find_cover` semantics fixed in Phase 4: bit ordering, `AvailableChoice`, MRV
selection, sibling elimination order, and the existing optimistic bound.

### Whole-search calibrations

Two complete configured-prime searches give:

| `(k,p)` | baseline nodes | + exact 2-slot check | reduction | new prunes | accepted raw histories |
| --- | ---: | ---: | ---: | ---: | ---: |
| `(8,79)` | 39,813 | 28,828 | 27.6% | 2,276 | 3,529 |
| `(9,89)` | 161,820 | 112,951 | 30.2% | 10,113 | 12,436 |

For both cases the **entire accepted raw history set is identical** before and after
the new pruning rule, not merely its cardinality.

A second `K=8` configured prime, `p=83`, gives

```text
113,488 -> 91,335 nodes   (-19.5%)
4,283 new exact prunes
17,882 accepted raw histories unchanged in count
```

and is retained in the benchmark script as an independent transfer point.

### `k=10,p=127`: first five real top-level workers

The full Python mirror is intentionally not used as a replacement for the C++
solver.  Instead we replay the first five serialized equivalents of the upstream
parallel top-level workers.  Their fixed second-coordinate choices are
`2,4,6,8,10`.

| second speed | baseline nodes | + 2-slot | reduction | new prunes | accepted leaves |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2  | 376,376 | 264,486 | 29.7% | 17,022 | 2,822 |
| 4  | 505,777 | 322,126 | 36.3% | 28,063 | 8,041 |
| 6  | 543,301 | 345,043 | 36.5% | 30,261 | 19,176 |
| 8  | 394,315 | 244,797 | 37.9% | 22,958 | 8,841 |
| 10 | 316,729 | 201,286 | 36.5% | 18,319 | 7,454 |

Aggregate over these five workers:

\[
2,136,498\longrightarrow1,377,738
\]

nodes, a reduction of about

\[
\boxed{35.5\%}.
\]

The accepted leaves of the first worker were compared as complete literal history
sets and are exactly identical (`2,822` histories on both sides).  The remaining
worker rows report the same accepted-leaf counts under baseline/enhanced traversal;
they are benchmark evidence, not a substitute for the general safety proof above.

## 5. Why exact transversal is much stronger than the Phase-4 disjoint test

The `k=10,p=127`, second-speed `2` worker produces `11,932` extra prunes when the
full bounded-transversal test is allowed in the final four slots.  Only `136` of
those states also possess a `(r+1)`-sized pairwise-disjoint requirement family.

Thus roughly 99% of these strict obstructions arise from **overlapping**
requirements.  A typical two-slot failure has six or seven minimal requirements,
each admitting around 9–11 future speeds, yet no pair of speeds hits them all.

This explains the scale transition from Phase 4:

```text
disjoint packing lower bound
    -> catches rare visibly separated obstructions

bounded transversal feasibility
    -> detects global incompatibility among heavily overlapping requirements
```

The representation, not merely the implementation, is doing more work.

## 6. Cost red team: stronger is not automatically better

The semantic hierarchy is

\[
\text{upstream optimistic bound}
<
\text{disjoint-requirement bound}
<
\text{2-slot exact transversal}
<
\text{3/4-slot exact transversal}.
\]

But presentation cost does **not** follow the same order.

In the Python mirror, extending the exact lookahead to three and four slots removes
many more DFS nodes but often spends more time certifying them.  The two-slot rule
is currently the most stable Pareto point across the tested configured primes.

Local Python timings are recorded only as engineering diagnostics because they are
not C++ benchmarks.  Representative runs nevertheless show the intended effect:

```text
k=8,p=79       about 1.3x faster in the Python mirror
k=9,p=89       about 1.25x faster
k=10,p=127     first several workers about 1.3x faster
```

These numbers must **not** be transferred to the upstream C++ implementation
without an actual port and benchmark.

## 7. Shakespeare interpretation

This phase closes the loop started by `ProcessJetSignature`:

```text
literal history
    -> exact future task language
    -> repair-requirement hypergraph
    -> transversal number
    -> shallow exact certificate at a cost-selected horizon
    -> fewer states in the real upstream search
```

The important point is the final cost selection.  Shakespeare is not proposing
"compute the strongest semantic quotient available."  It is searching for a
presentation/certificate pair on a Pareto frontier:

\[
\text{semantic strength}
\quad\text{vs}\quad
\text{certificate cost}.
\]

The two-slot transversal is the first candidate that is both structurally derived
and large enough to matter on parameters already used by the accepted proof code.

## 8. Claim boundary

Phase 5 does **not**:

- prove `LRC(13)`;
- benchmark a modified upstream C++ binary;
- establish a speedup for the full `k=10`, `k=11`, or `k=12` proof pipeline;
- address lift-stage cost after `I(k,p,1)` is generated;
- justify promoting a generic transversal/hitting-set API into Shakespeare.

It establishes a narrower but materially stronger result:

> **A representation discovered from Shakespeare future-task semantics yields an
> exact two-slot completion certificate that preserves the accepted search result
> and cuts roughly 20–38% of DFS nodes on several configured solved-prime searches,
> including about 35.5% over the first five `k=10,p=127` top-level workers.**

## 9. Next threshold

The next step should be engineering-conservative:

1. port only the two-slot certificate to a tiny C++ patch against upstream
   `find_cover.h`;
2. benchmark compilation time, `find_cover` wall time, node counts, and output hashes
   on several solved `K=8..10` primes;
3. keep 3/4-slot lookahead as a red team unless C++ bitset performance makes it
   competitive;
4. if the two-slot rule survives, extend the same frozen patch to the larger
   `K=11,12` configured primes;
5. only then consider the exploratory `K=13` configuration.

The decisive next question is no longer whether the representation contains new
information.  It is whether the cheapest exact shadow of that information remains
a net win in the solver that defines the current frontier.
