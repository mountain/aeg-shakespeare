# Phase 7 — AM-first discovery from problem-native contact geometry

**Status:** active.  This phase deliberately restarts Sonnet 001 from the problem's arithmetic process structure rather than from the upstream `find_cover` search state.

## 1. Why restart

Phases 0–6 were productive: Shakespeare discovered a future-requirement/transversal certificate that transferred across the solved/open frontier.  But that line entered through the ontology of the existing solver: folded cover bitsets, MRV choice, sibling elimination, and set-cover completion.

That representation discards a stronger structure already present in the Lonely Runner problem itself.

Before reduction to bitsets, one runner contributes a periodic additive contact pattern and its speed acts multiplicatively on time.  In the finite mod-`p` shadow this is exactly

\[
A_p=(\mathbf F_p,+),\qquad
M_p=(\mathbf F_p^\times,\cdot),\qquad
M_s:a\mapsto sa.
\]

For the primitive folded bad window `B`, every speed cover is

\[
C_s=s^{-1}B.
\]

The family `C_s` is therefore not a generic collection of sets.  It is one additive observer transported by the multiplicative process family.

Phase 7 asks whether Shakespeare can discover a cheaper task presentation **inside this A/M language before any unrestricted representation search is allowed**.

## 2. Two-gate protocol

The experiment is intentionally staged.

### Gate A — AM-constrained discovery

Allowed primitives and constructors are limited to structures native to Addition/Multiplication:

- finite A and M process families;
- M composition and inverse;
- M action on A/contact coordinates;
- finite quotients forced by explicit A/M symmetries;
- tuple/set composition only when needed to represent the task.

Forbidden in this gate:

- Fourier or spectral transforms;
- vector-space embeddings introduced solely for convenience;
- generic linearization;
- hand-supplied ratio coordinates;
- requirement-antichain features from the earlier solver-first line;
- K=13 holdout data for tuning.

The task oracle comes from contact geometry, not from a hidden target formula.

### Gate B — unrestricted presentation search

Only after Gate A is frozen do we restore competing grammars: raw cover state, requirement antichains, history quotients, AM constructions, or other Shakespeare-generated presentations.  The final question is then whether the AM result remains on the global Pareto frontier.

This separation answers two different questions:

1. how far can the arithmetic process language itself compress the problem?;
2. after all representations are allowed, is that language still selected by the task/cost objective?

## 3. First exact task: two-speed contact shape

For a folded speed pair `(s,t)`, define its problem-native task signature by:

1. form `C_s union C_t` from the primitive bad window;
2. quotient the resulting contact set by simultaneous global M action.

This signature says what two runners look like to the contact task after removing absolute multiplicative scale.  It does **not** mention a ratio coordinate.

The bounded AM construction search starts only from atoms `s,t` and the operations

```text
inv(x)       M inverse
mul(x,y)     M composition
orbit(x)     quotient x ~ x^{-1}
```

The last quotient is the intrinsic M involution induced by exchanging the two runners; it does not encode a particular formula relating `s` and `t`.

Executable calibration:

```text
tests/research/test_lonely_runner_am_discovery.py
```

## 4. Discovery result on training worlds

Training worlds:

```text
(k,p) = (5,17), (5,29)
```

The contact-task partitions have respectively

```text
5 classes
8 classes
```

The AM search produces two relevant Pareto points.

First:

```text
mul(inv(s), t)
```

This is task-sufficient, but it over-refines the contact task because it keeps the orientation of the relative M displacement.  Its feature-class counts are

```text
8 classes at p=17
14 classes at p=29
```

Second:

```text
orbit(mul(inv(s), t))
```

The extra intrinsic quotient collapses the two orientations and reaches

```text
5 classes at p=17
8 classes at p=29
```

exactly matching the contact-task partition in both training worlds.

The important point is methodological: the search was not supplied with `t/s`.  Relative multiplicative position appeared because inverse + composition is cheaper, under the task oracle, than retaining two absolute M coordinates.

## 5. Frozen solved-world transfer

The exact AM presentation selected above is frozen and transferred to

```text
(k,p) = (8,79)
```

which is not used in proposal generation or selection.

There are

\[
\binom{39+1}{2}=780
\]

literal unordered folded speed pairs.  The held-out contact task has exactly

```text
20 classes
```

and the frozen AM presentation also has exactly `20` classes with the same partition.

Thus the first AM-first result is an exact representation compression

\[
780\longrightarrow 20
\]

on a held-out solved parameter set, about `39x` in class count for unordered pairs.  If ordered literal pairs are counted before quotienting exchange symmetry, the corresponding raw count is `39^2=1521` against the same 20 shapes.

This is a presentation result, not yet a runtime claim.

## 6. What is and is not established

Established:

- the finite Lonely Runner contact family is exactly an M orbit of one additive bad window;
- bounded AM-only construction search can rediscover a relative multiplicative coordinate from the contact-task oracle;
- one further intrinsic M quotient reaches the exact two-speed task partition;
- the selected presentation transfers unchanged to held-out `k=8,p=79`.

Not established:

- that pairwise relative coordinates are sufficient for the full `k`-runner future task;
- that the resulting orbit grammar dominates the earlier requirement-antichain presentation;
- that an upstream implementation is faster;
- that `LRC(13)` is easier after this change.

Those are later gates.

## 7. Next experiment

Remain inside AM.

The next target is depth `d>2`: start from a speed multiset/contact history and let the AM grammar search for a small collection of relative M coordinates or orbit invariants that preserves the complete bounded future contact language.

The correct comparison is

```text
literal absolute M history
    -> AM-generated candidate presentation
    -> exact future-task certificate
    -> state/class count + update cost
```

No unrestricted representation family should be introduced until this AM-only line reaches a stable Pareto frontier on solved worlds.
