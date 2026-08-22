# Phase 3 note — requirement antichain as a cheap exact quotient

**Status:** first analytically justified quotient discovered from the Phase-2 task classes.  Exact for the canonical nondecreasing presentation; not yet transported to upstream MRV.

## 1. The problem left by Phase 2

`ProcessJetSignature` exposed large exact semantic classes:

```text
k=4, p=13: 28 literal partial histories -> 11 task classes
k=5, p=17: 165 literal partial histories -> 19 task classes
```

But computing a full future signature enumerates the continuation tree.  It is therefore an oracle for *what may be merged*, not yet a useful representation for a large search.

The next question is the Shakespeare discovery question:

> Can we explain a substantial part of those semantic collisions by an invariant computable from the current state, without enumerating its future?

For the canonical set-cover grammar, the answer is yes.

## 2. Future requirements rather than present coverage

Fix `(k,p)` and write

\[
M=(p-1)/2,
\qquad
U_p=\{1,\ldots,M\}.
\]

Let a valid nondecreasing partial history be

\[
h=(s_1,\ldots,s_d),
\]

with current cover `C(h)`, last speed

\[
m=s_d,
\]

and remaining slots

\[
r=k-d.
\]

The uncovered time positions are

\[
U(h)=U_p\setminus C(h).
\]

For each uncovered time `a`, ask a future-facing question:

\[
R_h(a)
=
\{s\in\{m,m+1,\ldots,M\}:a\in C_s\}.
\]

`R_h(a)` is the set of still-admissible speed tokens capable of satisfying that one outstanding cover requirement.

The entire current bitset `C(h)` is not intrinsically important.  What matters for the future is the family

\[
\mathcal R(h)=\{R_h(a):a\in U(h)\}.
\]

## 3. Remove logically redundant requirements

Suppose two outstanding requirements satisfy

\[
R_1\subseteq R_2.
\]

Any future speed set that hits `R_1` automatically hits `R_2`.  Therefore the second constraint adds no information to future acceptance.

Define the **requirement antichain**

\[
\mathcal A(h)
=
\min_{\subseteq}\mathcal R(h),
\]

the unique set of distinct inclusion-minimal requirement sets.

Special cases behave correctly:

- if some uncovered time has `R_h(a)=emptyset`, then `emptyset` is the unique minimal obstruction and no completion exists;
- if nothing is uncovered, `A(h)` is empty and the only remaining condition is canonical admissibility of filler speeds.

This operation is cheap relative to full future enumeration: build an incidence row for every uncovered time against the at most `(p-1)/2` folded speeds, deduplicate rows, then delete strict supersets.

## 4. Exact sufficiency theorem for the canonical grammar

Define

\[
S(h)=\bigl(r,m,\mathcal A(h)\bigr).
\]

### Proposition

For the canonical nondecreasing completion presentation, if

\[
S(h_1)=S(h_2),
\]

then the complete Shakespeare task signatures of `h_1` and `h_2` are equal.

### Proof

Take any literal continuation word

\[
c=(x_1,\ldots,x_q),
\qquad q\le r.
\]

The terminal-cover observer can be true only when `q=r`.

For `q=r`, the continuation is valid exactly when

\[
m\le x_1\le x_2\le\cdots\le x_r.
\]

Because `m` and `r` are included in `S`, this admissibility condition is identical for the two states.

For a valid continuation, an uncovered time `a` becomes covered exactly when the support of `c` intersects `R_h(a)`. Hence the final cover succeeds iff

\[
\operatorname{supp}(c)\cap R\ne\varnothing
\qquad
\text{for every }R\in\mathcal R(h).
\]

Every nonminimal member of `R(h)` contains a minimal member, so this is equivalent to hitting every member of `A(h)`. Thus acceptance of every literal continuation depends only on

\[
(r,m,\mathcal A(h)).
\]

Therefore equal `S` implies equal complete `ProcessJetSignature`. QED.

This is a **sufficient** quotient, not necessarily the minimal task quotient.  Phase 2 already exhibited equal task signatures with different last speeds, so `S` can still split states that the exact Nerode-like quotient merges.

## 5. A concrete nontrivial merge

At `k=5,p=17`, compare the depth-four prefixes

\[
h_1=(1,3,4,6),
\qquad
h_2=(1,4,5,6).
\]

Their current cover sets differ:

\[
C(h_1)=\{1,2,3,4,5,6,8\},
\]

\[
C(h_2)=\{1,2,3,4,6,7,8\}.
\]

Yet both have

\[
r=1,\qquad m=6,\qquad
\mathcal A(h)=\{\{7\}\}.
\]

So the structural quotient certifies their merger immediately, without exploring a future tree.  In both cases the unique accepting continuation is speed `7`.

The reason is illuminating: the two states are missing *different time positions*, but those positions impose the **same future process requirement**.

This is exactly the kind of representation change Shakespeare is intended to surface:

```text
where the deficit is
        -> quotient ->
what future operation can repair it
```

## 6. Compression ladder

The executable experiment compares four representations at each depth:

1. literal canonical prefix;
2. present state `(remaining slots, last speed, current cover)`;
3. structural state `(remaining slots, last speed, requirement antichain)`;
4. exact `ProcessJetSignature` task class.

For `k=4,p=13`, totals across partial depths are:

| representation | states/classes |
|---|---:|
| literal histories | 28 |
| current-cover state | 21 |
| requirement-antichain state | 16 |
| exact task class | 11 |

For `k=5,p=17`:

| representation | states/classes |
|---|---:|
| literal histories | 165 |
| current-cover state | 85 |
| requirement-antichain state | 41 |
| exact task class | 19 |

Thus the requirement antichain removes about half of the remaining current-cover states in the second calibration:

\[
85\to41,
\]

while remaining conservative relative to the semantic optimum

\[
19.
\]

Again, these are state counts, not runtime speedups.

## 7. Why this may matter for the actual `I(k,p,1)` bottleneck

The 2026 LRC computation asks for stronger pruning of no-witness speed tuples.  The requirement picture supplies an exact dual view of a partial candidate:

```text
current covered times
        ->
outstanding time constraints
        ->
future speed sets that can satisfy each constraint
        ->
minimal requirement antichain
```

Several pruning certificates become natural downstream of this representation:

- an empty requirement set gives immediate impossibility;
- if the requirement hypergraph needs more than `r` hitting speeds, the branch is impossible;
- pairwise-disjoint or otherwise certified lower bounds on its transversal number give cheap sufficient pruning conditions;
- equivalent antichains can be memoized even when current cover bitsets differ.

The first bullet is close to upstream `canBeCovered`; the interesting question is whether higher-order antichain structure produces pruning or memoization not already captured by upstream's MRV and optimistic coverage bound.

That must be measured rather than assumed.

## 8. Next phase: cross-presentation benchmark

Phase 4 should now leave the toy canonical grammar and reconstruct enough of upstream `find_cover` to answer three concrete questions:

1. Can the requirement antichain be computed on the actual `covered + AvailableChoice` MRV state?
2. Does antichain/transversal pruning reject branches that survive the current upstream `early_return_bound()`?
3. Does memoization by a task-safe requirement presentation reduce visited states on solved `(k,p)` instances without changing the canonical solution set?

The baseline should be the upstream code's exact node counts and solution sets, not wall-clock comparisons between Python and C++.

If the answer is negative, this Phase-3 quotient remains a clean conceptual result but not an LRC breakthrough.  If the answer is positive and transfers across solved `k`, we will have the first plausible Shakespeare-derived attack on the bottleneck the LRC authors themselves identify.
