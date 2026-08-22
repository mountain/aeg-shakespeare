# Phase 5b — C++ semantic mirror and minimal upstream patch

**Status:** standalone C++ mirror compiled and benchmarked; minimal upstream patch prepared but not yet executed against the upstream repository.

## 1. Why a second implementation matters

Phase 5 first established the two-slot certificate in an exact Python semantic
mirror.  That was enough for deterministic node-count and solution-set claims, but
not enough to answer the engineering objection that Python overhead might distort
the cost/benefit ordering.

We therefore wrote a standalone C++23 mirror of the same finite process:

```text
sonnet/lonely-runner/cpp/phase5_two_slot_bench.cpp
```

It preserves the relevant upstream semantics:

- the same folded speed universe;
- the same `P/2` bad-time bit ordering;
- `AvailableChoice`-style elimination and remaining counts;
- the same MRV tie-breaking;
- the same optimistic `early_return_bound()`;
- elimination of a chosen speed only after its child returns;
- the same serialized top-level worker initialization.

The enhanced version differs at exactly one point:

```text
if remaining_slots == 2:
    prune unless some two available speed covers jointly cover all uncovered bits
```

## 2. Deterministic cross-language calibration

The C++ mirror reproduces the Python node/leaf counts exactly.

### Whole searches

```text
k=8,p=79
baseline  nodes=39,813   accepted=3,529
two-slot  nodes=28,828   accepted=3,529   new prunes=2,276

k=9,p=89
baseline  nodes=161,820  accepted=12,436
two-slot  nodes=112,951  accepted=12,436  new prunes=10,113
```

### `k=10,p=127`, first five workers

The C++ mirror again reproduces the deterministic table from Phase 5:

```text
second 2:   376,376 -> 264,486   accepted 2,822
second 4:   505,777 -> 322,126   accepted 8,041
second 6:   543,301 -> 345,043   accepted 19,176
second 8:   394,315 -> 244,797   accepted 8,841
second 10:  316,729 -> 201,286   accepted 7,454
```

Thus the representation result is not an artifact of the Python traversal.

## 3. Standalone C++ timing signal

On one local build using

```text
g++ 14.2.0
-O3 -std=c++23 -march=native
```

the standalone mirror produced representative timings:

```text
k=8,p=79     10.18 ms ->  8.73 ms
k=9,p=89     45.50 ms -> 33.26 ms
```

For the first five `k=10,p=127` workers:

```text
second 2:   171.6 ms -> 153.5 ms
second 4:   212.1 ms -> 162.5 ms
second 6:   219.6 ms -> 159.1 ms
second 8:   161.5 ms -> 111.3 ms
second 10:  128.7 ms ->  93.5 ms
```

All five workers improved in this implementation.  The aggregate local timing for
those five workers is roughly

\[
893.5\text{ ms}\to679.8\text{ ms},
\]

or about a `1.31x` speedup.

These are **diagnostic timings, not upstream performance claims**.  The standalone
mirror uses the same mathematical/search semantics but is not the upstream source
layout, compiler invocation, threading environment, or full proof pipeline.

The important result is narrower: the two-slot certificate is cheap enough to
remain a net win in a C++/`std::bitset` realization.

## 4. Minimal upstream patch

A source-level patch against the current upstream `src/find_cover.h` is stored at

```text
sonnet/lonely-runner/patches/phase5-two-slot-find-cover.patch
```

The intended change is deliberately small.  Add one predicate inside `Dfs<P,K>`:

```cpp
bool two_slot_completion_impossible() const
```

which is active only when

```text
state.elems.size() == K - 2.
```

It reuses:

- `state.covered`;
- `state.choice.isEliminated(i)`;
- `state.choice.get_next_to_cover(...)`;
- `context<P,K>.cover(i)`.

No new persistent search state is introduced.

Then `Dfs::run()` gains one line after the existing optimistic bound:

```cpp
if (two_slot_completion_impossible()) return;
```

This is important experimentally: if a real upstream benchmark changes, the cause
can be attributed to one exact lookahead rule rather than to a large refactor.

## 5. Safety argument in upstream terms

Let

\[
U=\neg\texttt{state.covered}
\]

within the `P/2`-bit `CoveredBitset`, and let `A` be the currently non-eliminated
speed choices.

With exactly two slots remaining, an accepting descendant exists iff

\[
\exists i,j\in A:
U\subseteq C_i\cup C_j.
\]

The forward implication is immediate from any accepting two-step descendant.

For the reverse implication, let `a` be the same MRV uncovered position chosen by
upstream.  Any covering pair contains at least one speed covering `a`; choose it as
the first child.  Upstream does not eliminate that speed (or any other currently
available speed) inside the child; elimination happens only after the child returns
for later siblings.  Therefore the second member of the pair remains selectable in
the child and completes the cover.

Repeated residues are also handled correctly: `i=j` is allowed, matching upstream
child semantics.

Thus the predicate prunes exactly those two-slot states with no accepting
descendant in the `I(k,p,1)` search.

## 6. What remains to establish

The remaining uncertainty is now almost entirely implementation-level:

1. apply the patch to a checkout of the exact upstream revision;
2. compile with the upstream command/configuration;
3. run selected solved configurations before/after;
4. compare `find_cover` output sets or stable hashes, not only `S.size()`;
5. compare wall time under the same thread count;
6. verify that savings in `find_cover` are not irrelevant to total time after
   lifting for the selected configurations.

If this passes, the two-slot rule becomes the first Shakespeare-derived change that
has crossed the full chain

```text
future semantics
 -> structural quotient
 -> exact certificate
 -> configured solved parameters
 -> C++ cost survival
 -> actual frontier implementation
```

The last arrow is the only one not yet completed.
