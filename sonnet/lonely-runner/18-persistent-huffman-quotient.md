# Phase 7i — persistent Huffman quotient: current-task minimality is not the right objective

**Status:** bounded four-speed representation result derived from the center-2/center-3 local refinement experiment; still Gate A.

## 1. Static minimality can destroy future objectification

At contact center `<=2` the representation ladder contains

```text
849 exact task-safe sign states
 -> 60 first-witness semantics.
```

If the only task is the current first witness, collapsing all the way to 60 labels is natural.

But Phase 7h shows that the next contact layer does not affect all members of a witness class equally.  Eight particular center-2 task-safe parents must be reopened when center-3 contacts are introduced.

Therefore the current-task quotient

\[
849\to60
\]

forgets some information that is cheap now but valuable for future refinement.

This makes the representation problem explicitly temporal:

> the cheapest presentation for the current observer need not be the cheapest presentation for a process whose observation language will continue to deepen.

## 2. A one-step persistent quotient needs only 68 labels

Construct a refinement-aware label as follows.

- For every center-2 task-safe state certified stable by the local detector, keep only its current first-witness semantic.
- For each of the eight affected parent states, retain one residual identity in addition to the current witness label.

The resulting quotient has

\[
\boxed{68\text{ persistent labels}}
\]

instead of either extreme:

\[
60\text{ current-only semantics}
\qquad\text{or}\qquad
849\text{ full sign states}.
\]

The extra eight residual identities are not arbitrary provenance.  Each is exactly a state that the next contact layer can distinguish causally.

## 3. Huffman search says the future residual is free in this calibration

Re-run the exact center-2 Huffman decision-tree search, but require leaves to be pure for the 68 persistent labels rather than merely the 60 current witness semantics.

Under the same 55-input usage distribution, the time-first optimum is unchanged:

```text
weighted decision depth   135
boundary volume           328
worst depth                 9
internal decision nodes   109
root wall                  u4/u1 ? 4
```

Thus

\[
\boxed{E[d]=135/55\approx2.455}
\]

exactly as before.

The complete boundary profile is also unchanged:

```text
1, 3, 3, 9, 27, 48, 63, 69, 72, 33.
```

The balanced space-time Pareto point is unchanged as well:

```text
weighted depth      174
boundary volume     328
peak frontier        69
worst depth           9
```

or

\[
E[d]=174/55\approx3.164.
\]

So, on this bounded geometry:

\[
\boxed{
\text{60 current labels}
\to
\text{68 persistent labels}
}
\]

requires **zero extra decision queries, zero extra tree nodes, and zero extra worst depth**.

Only the terminal object carried by a few leaves becomes slightly richer.

## 4. Why zero extra tree cost is possible

The Huffman tree already asks wall questions for other current task distinctions.  Those same paths happen to separate the eight refinement-sensitive parents from the stable states with which they share a current witness label.

Thus the information required for future refinement is already present in the process history; the static 60-label quotient merely discards it at the leaf.

This is an important distinction:

```text
process asks enough questions to know the residual
        ↓
current observer throws the residual away
```

versus

```text
persistent observer objectifies that residual at essentially no extra process cost.
```

The second is the representation we want.

## 5. Persistent DAG update

Combine the 68-label center-2 presentation with the local detector/update from Phase 7h:

```text
center-2 persistent DAG
    68 terminal labels
    ↓ introduce center-3 contacts
local detector
    8 affected parents
    ↓
reopen only 26 / 5,823 full old sign systems
    ↓ cycle-close local refinements
298 center-3 children
    ↓
recover all 75 center-3 witness semantics
```

The other 841 old task-safe parents remain stable objects.

The full 72,241-state center-3 census is now needed only as a red-team oracle, not as the update algorithm.

This suggests the fundamental representation object should be a **persistent decision DAG with refinable terminal residuals**, not a sequence of independently optimized trees.

## 6. A new cost axis: refinement cost

The current `PresentationCost` axes—grammar, relations, history, decoder, task error—are not yet enough for this setting.

Two presentations may have identical current task cost but very different future update cost.

For an evolving process language, a candidate presentation should eventually expose something like

\[
\boxed{
C(P)=
(
\text{current boundary geometry},
\text{current depth},
\text{task error},
\text{residual size},
\text{expected refinement cost}
).
}
\]

At center 2 we have a concrete calibration:

- current-only label count: `60`;
- persistent label count: `68`;
- full sign-state count: `849`;
- extra Huffman tree cost from `60 -> 68`: **zero**;
- next-layer full semantic census: `72,241` refined systems;
- persistent local update: `298` refined systems.

This is a strong example where a slightly richer terminal residual wins overwhelmingly once refinement cost is included.

## 7. Relation to future-task quotients

Conceptually this returns to Shakespeare's earliest task-equivalence idea, but along a new continuation axis.

Earlier Sonnet phases asked whether two partial **runner-choice histories** have the same future completion language.

Here we ask whether two objectified states have the same response to future **contact-depth extensions**.

The corresponding equivalence is roughly

\[
S_1\equiv_{Q,+1}S_2
\]

when they agree on:

1. the current task observer;
2. whether the next contact layer reopens them;
3. the task semantics of every allowed local next-layer refinement.

The 68-label construction is a deliberately minimal first approximation: stable current tasks are merged; the eight causally sensitive states retain residual identity.

A later discovery pass can search automatically for the smallest residual sufficient for multiple future contact layers.

## 8. Next experiment

The next useful experiment is no longer a larger static arrangement.

Build the persistent center-2 -> center-3 DAG explicitly and measure **incremental** Huffman geometry:

```text
new DAG nodes allocated
old DAG nodes reused
extra wall queries paid only on affected paths
incremental boundary volume
incremental expected depth
```

Then repeat center-3 -> center-4 using the same mechanism.

The critical scaling question becomes

\[
\boxed{
\text{incremental representation growth per new process layer},
}
\]

not the size of the fully expanded arrangement at that layer.

If that incremental growth remains sparse, it would be substantially stronger evidence for Shakespeare than any one-shot compression factor.

## Claim boundary

The zero-extra-cost `60 -> 68` persistent quotient is a bounded four-speed result for one contact-depth lookahead.  It does not prove that future residuals remain free at arbitrary depth or runner dimension.

Its significance is methodological:

\[
\boxed{
\text{the representation that is optimal for a continuing process may deliberately retain a tiny, task-invisible residual.}
}

In this calibration that residual costs nothing in current Huffman tree geometry and reduces the next semantic update from a 72,241-state census to a 298-state local refinement.
