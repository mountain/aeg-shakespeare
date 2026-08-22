# Phase 7h — contact-depth refinement is semantically local

**Status:** exact corollary of the center-2 -> center-3 pair-difference census; still Gate A.

Phase 7g showed that raw pair syntax grows much faster than the exact task presentation when the contact alphabet is refined.  A finer question is even more important for an incremental algorithm:

> when center-3 contacts are introduced, how many of the already-frozen center-2 task-safe states actually need their task semantics recomputed?

The answer in the four-speed `u4/u1<8` calibration is unexpectedly small.

## 1. Center-3 task geometry is a pure refinement of center-2

All 21 wall coordinates that were task-relevant at center `<=2` remain relevant at center `<=3`.

Only five genuinely new task-relevant wall coordinates appear:

\[
\boxed{
\begin{aligned}
\frac{u_4}{u_2}&\ ?\ \frac73,\\
\frac{u_4}{u_2}&\ ?\ \frac83,\\
\frac{u_4}{u_3}&\ ?\ \frac{14}{11},\\
\frac{u_4}{u_3}&\ ?\ \frac{14}{9},\\
\frac{u_4}{u_3}&\ ?\ \frac{16}{9}.
\end{aligned}
}
\]

Thus the center-3 exact task-safe sign geometry is literally a refinement of the old 21-sign presentation, not a replacement by unrelated coordinates.

## 2. Geometric refinement is already sparse

Project every one of the 1,953 center-3 task-safe sign strata onto the old 21-sign key.

Every old center-2 task-safe stratum is reached, so the projection has exactly

\[
849
\]

parent states.

Their child-count distribution is:

| center-3 child strata per old parent | number of old parents |
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

of the old exact sign states do not split at all when the contact alphabet is enlarged.

Only 299 old sign states require any geometric refinement.

## 3. Semantic refinement is dramatically sparser

Now forget the refined sign identities and ask only whether the first-witness semantics of a parent changes across any of its center-3 children.

The distribution becomes:

| distinct center-3 witness semantics inside one old parent | old parents |
| ---: | ---: |
| 1 | 843 |
| 3 | 2 |
| 5 | 3 |
| 7 | 1 |

Hence only

\[
\boxed{6/849\approx0.7\%}
\]

of the old task-safe states actually split semantically.

Equivalently,

\[
\boxed{843/849\approx99.3\%}
\]

of the old state semantics can be inherited unchanged across this calculus-depth refinement.

This is much stronger than the global count `849 -> 1,953` suggests.  Most new geometric distinctions are irrelevant to the actual first-witness observer.

## 4. Where the five new walls act

Even the five new task-relevant wall coordinates are highly local.  Counting old parent states on which each sign can actually vary gives:

| new wall | old parent states with nontrivial variation |
| --- | ---: |
| `u4/u2 ? 7/3` | 85 |
| `u4/u2 ? 8/3` | 81 |
| `u4/u3 ? 14/11` | 161 |
| `u4/u3 ? 14/9` | 101 |
| `u4/u3 ? 16/9` | 101 |

For every other old parent the sign of that new wall is already forced by the old pair-difference cycle closure.

So contact-depth refinement has two successive local filters:

```text
new primitive contact ratios
    -> cycle closure says where a new sign is even variable
    -> old task observer says where that variation can change the witness
```

The second filter is far stronger in this calibration.

## 5. Algorithmic consequence

A naive center-depth implementation would do

```text
refine every realizable sign system
    -> recompute contact history
    -> rebuild task quotient
```

The observed locality suggests a different algorithm:

```text
old task-safe state S
    -> retain its certified witness/history boundary
    -> introduce one new contact layer
    -> ask whether any new contact can enter the causally relevant prefix of S
        no  -> inherit S unchanged
        yes -> locally refine only S
    -> run cycle closure only inside the affected residual region
```

In other words, the correct object may be a **persistent task quotient with local contact refinements**, not a sequence of complete rebuilt arrangements.

This is closely aligned with Shakespeare's process-objectification goal: once a history region has been quotiented into a stable object, later process depth should reopen it only when new observations can distinguish its futures.

## 6. Relation to the Hauffman structure

This locality also changes how the history tree should be represented.

If 843 of 849 old task states retain their semantics, rebuilding a new decision tree from scratch wastes stable history structure.  The natural next representation is a **persistent decision DAG**:

- unchanged task nodes are shared across contact depths;
- only the six semantically split residual states acquire new descendants;
- Hauffman/history cost is measured on the resulting shared DAG, not on a fresh tree.

This should reduce both:

1. **space growth** — stable subtrees are stored once;
2. **time growth** — old decisions leading to unaffected states need no extra query.

Thus the next optimization target is no longer merely a better tree at one fixed contact depth.  It is the growth of a persistent space-time DAG under calculus refinement.

## 7. Next executable experiment

The immediate experiment should test whether the six semantic split states can be detected **without first generating all 72,241 center-3 realizable systems**.

A sufficient local certificate would inspect the old state's contact/witness prefix and ask whether a newly introduced center-3 event can cross any event that is causally prior to the old witness.

The target is:

```text
849 old task-safe states
    -> local refinement detector
    -> predicted affected subset
```

with the exact post-hoc answer

```text
6 semantically affected parents
```

held out as the oracle.

If this succeeds, contact-center refinement becomes an incremental algorithm rather than a census.

## Claim boundary

The `6/849` result is a bounded four-speed first-witness fact.  It is not yet a general theorem about contact depth or higher runner number.

Its significance is structural:

\[
\boxed{
\text{new calculus syntax can grow substantially while the old task quotient remains almost entirely stable.}
}

That is precisely the kind of persistence Shakespeare needs if process objectification is to control higher-dimensional search.
