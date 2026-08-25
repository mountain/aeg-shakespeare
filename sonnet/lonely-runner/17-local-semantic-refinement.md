# Phase 7h — contact-depth refinement is semantically local

**Status:** exact corollary of the center-2 -> center-3 pair-difference census, plus a local detector that does not require enumerating the full center-3 geometry; still Gate A.

Phase 7g showed that raw pair syntax grows much faster than the exact task presentation when the contact alphabet is refined.  The next question is algorithmic:

> when center-3 contacts are introduced, which already-frozen center-2 task-safe states actually need to be reopened?

The answer is under one percent.

## 1. Center-3 task geometry is a refinement of center-2

All 21 wall coordinates that are task-relevant at center `<=2` remain relevant at center `<=3`.

Only five genuinely new wall coordinates survive the complete post-hoc task quotient:

\[
\boxed{
\begin{aligned}
\frac{u_4}{u_2}&\ ?\ \frac73,\\
\frac{u_4}{u_2}&\ ?\ \frac83,\\
\frac{u_4}{u_3}&\ ?\ \frac{14}{11},\\
\frac{u_4}{u_3}&\ ?\ \frac{14}{9},\\
\frac{u_4}{u_3}&\ ?\ \frac{16}{9}.
\end{aligned}}
\]

Thus the center-3 presentation is not a replacement by unrelated coordinates.  It is a local refinement of the old pair-difference sign graph.

## 2. Geometric refinement is sparse

Project every one of the 1,953 center-3 task-safe sign strata onto the old 21-sign key.  Every old center-2 task-safe state is reached, so there are exactly 849 parents.

Their center-3 child-count distribution is:

| center-3 sign children | center-2 parents |
| ---: | ---: |
| 1 | 550 |
| 3 | 136 |
| 5 | 133 |
| 7 | 7 |
| 11 | 9 |
| 13 | 14 |

Therefore

\[
\boxed{550/849\approx64.8\%}
\]

of the old exact sign states do not split geometrically at all.  Only 299 need any finer sign geometry.

## 3. Task semantics is much more stable than sign geometry

There are two distinct ways an old task-safe state can be affected by the new contact layer:

1. **split:** different center-3 refinements acquire different first-witness semantics;
2. **uniform replacement:** all refinements still agree with one another, but the common first witness changes because a new contact is forced into the old causal prefix.

The exact center-3 census gives:

```text
841 parents   witness semantics unchanged
  6 parents   split into several new witness semantics
  2 parents   one common new witness replaces the old one
```

Hence only

\[
\boxed{8/849\approx0.94\%}
\]

of old task-safe states need any semantic recomputation at all.

Equivalently,

\[
\boxed{841/849\approx99.06\%}
\]

of the old first-witness semantics can be inherited unchanged across the contact-depth refinement.

For the six splitting parents, the numbers of distinct new witness semantics are

```text
3, 3, 5, 5, 5, 7.
```

The two uniformly replaced parents each retain one semantic child, but their witness event index is pushed later by a center-3 contact that is already forced by the old geometry.

## 4. A local detector finds all eight affected parents without center-3 census

The post-hoc `8/849` answer can be rediscovered from the **old center-2 process states only**.

Each center-2 task-safe state already carries a certified first-witness contact prefix.  Introduce the two new center-3 events on each runner:

\[
\alpha_{3,-}=3-\frac15=\frac{14}{5},
\qquad
\alpha_{3,+}=3+\frac15=\frac{16}{5}.
\]

An old parent needs reopening if either of two local conditions holds.

### A. Forced earlier insertion

Using only the old pair-difference constraints, a new center-3 event is provably at or before the old witness event.

Then the old witness prefix is no longer the actual process prefix even if no old sign cell splits.  This detects the two uniform replacements and one of the six splitting parents.

### B. Effective unresolved crossing in the old causal prefix

A new center-3 event can exchange order with an event already present before the old witness, and the old pair stratum does not decide which side of the new collision ratio it lies on.

One crossing can be discarded without refinement:

> an unresolved **enter-enter** swap cannot create the first safe time.

Immediately before the first enter both involved runners are at least as safe as at their simultaneous contact; if all other runners were already safe, a witness would have existed before that swap.  Thus pure enter-enter ordering is causally irrelevant to first-witness creation.

After this process-semantic filter, condition B detects six parents.

The union

\[
A\cup B
\]

contains exactly

\[
\boxed{8}
\]

parents: **8 true positives, 0 false positives, 0 false negatives** against the complete center-3 census.

So the affected subset can be identified before the 72,241 refined sign systems are generated.

## 5. Local refinement shrinks 72,241 systems to 298 children

The eight affected task-safe parents contain only

\[
\boxed{26}
\]

of the 5,823 complete center-2 realizable sign systems.

Refine only those 26 full systems by the new center-3 pair strata and apply the same exact cycle closure.  They generate only

\[
\boxed{298}
\]

center-3 realizable children.

Evaluating first-witness semantics on those 298 children reproduces **exactly** the complete post-hoc center-3 task sets of all eight affected parents.

Thus the semantic refinement step can be changed from

\[
72{,}241\text{ full center-3 states}
\]

to

\[
\boxed{298\text{ locally required refined states}}
\]

once the old task quotient is available—a reduction of roughly

\[
\boxed{242\times}
\]

in the number of refined full sign systems whose new semantics must actually be evaluated.

The other 841 task-safe parents are inherited as stable objects.

## 6. This is the process-objectification mechanism we were looking for

A census-style algorithm does

```text
new contact alphabet
    -> rebuild all realizable geometry
    -> recompute every task state
    -> quotient again
```

The local process algorithm can instead do

```text
persistent old task-safe state S
    -> keep its certified witness/contact prefix
    -> introduce the next contact layer
    -> local causal detector
         unaffected -> reuse S unchanged
         affected   -> refine only S
    -> cycle-close only the affected residual geometry
    -> update task DAG locally
```

This is a much stronger form of compression than a smaller static state count.  The **objectified state survives future process depth** and is reopened only when a new observation can actually distinguish its future.

That is very close to the intended Shakespeare/AEG idea of history residual becoming a stable object.

## 7. Consequence for the Huffman structure: use a persistent DAG

If 841 of 849 old task nodes survive unchanged, rebuilding an entirely new decision tree at center 3 wastes almost all stable history structure.

The natural next representation is therefore a **persistent decision DAG**:

- old unaffected states are shared verbatim across contact depths;
- only eight old semantic states acquire refinement edges;
- only the six splitting states branch semantically;
- two states are retargeted to a new common witness;
- Huffman/history cost measures the incremental space/time growth of the shared DAG.

This separates three quantities that a fresh tree conflates:

1. total representation size;
2. new space allocated by one calculus refinement;
3. extra decision depth paid only on affected histories.

The right optimization target is therefore no longer merely `best tree at depth m`, but

\[
\boxed{\text{minimum incremental space-time cost of }D_m\to D_{m+1}.}
\]

## 8. Next executable step

The immediate implementation target is now precise:

```text
old task-safe DAG
    + new contact events
    -> detect 8 affected parents
    -> refine 26 old full sign systems
    -> construct 298 center-3 children
    -> recover the exact new task semantics
    -> patch the DAG locally
```

The full center-3 census remains the frozen oracle/red team, not the algorithm.

If this local update reproduces the same 75 final witness semantics and Huffman decision behavior without visiting the other 71,943 center-3 full states, then contact-depth refinement has become genuinely incremental.

## Claim boundary

The `8/849` locality and `26 -> 298` local refinement counts are bounded four-speed first-witness results.  They are not yet a theorem for arbitrary runner count or contact depth.

Their significance for Shakespeare is direct:

\[
\boxed{\text{most objectified task states remain stable when the process language is deepened.}}
\]

This is the strongest evidence so far in Sonnet 001 that process objectification can control not only a fixed search space, but the *growth of the representation itself*.
