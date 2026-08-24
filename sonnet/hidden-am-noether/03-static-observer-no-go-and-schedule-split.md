# Phase 2 preflight — static observer no-go

**Status:** the originally frozen static-observer S2 search is closed by a
no-go theorem; no moving-observer search has been authorized.

## 1. Why the raw 166 x 85 search should not run

The 85 frozen observer words are built from the same product-affine A/M group
whose Lie algebra supplied the S1 generators. For a static invertible observer
(g) and expression (F),

\[
\operatorname{Stab}(g\cdot F)
=\operatorname{Ad}_g\operatorname{Stab}(F).
\]

The adjoint action is invertible, hence

\[
\dim\operatorname{Stab}(g\cdot F)
=\dim\operatorname{Stab}(F).
\]

All 166 legal S2 inputs have zero stabilizer in the complete constant linear
A/M algebra. No static word in the same group can expose a nonzero one.
Enumerating the 85 words would spend computation confirming a group-theoretic
tautology and could encourage accidental use of noninvertible transformations.

## 2. Executable certificate

The test realizes three independent invertible product-affine observers,
including translations, positive/negative dilations, and independently changed
axes. Across all 166 frontier expressions it checks exact polynomial rank
before and after observation:

```text
expressions                  166
observer controls              3
rank comparisons             498
dimension-changing failures    0
```

A visibly symmetric expression is retained as a positive control, and a
zero-scale noninvertible map is rejected rather than allowed to manufacture a
symmetry by information loss.

The finite controls illustrate the general conjugacy proof; they are not the
basis of the theorem.

## 3. Result for the original open question

Within the originally frozen semantics — static observer words drawn from the
same A/M group and symmetry tested in its full constant Lie algebra — the S2
answer is **no**. This is a bounded negative result, not evidence against moving
canonical observers.

## 4. Required schedule split

Continuing requires choosing one genuinely stronger problem:

1. **moving observer:** observer parameters depend on process state/history and
   maintaining a normalization derives an observer ODE;
2. **task quotient:** symmetry appears only after a declared task equivalence,
   with reconstruction obligations retained;
3. **larger ambient algebra:** observer conjugation moves the process into a
   completion not contained in the original product A/M algebra;
4. **higher AM jet:** the relevant action lives on acceleration/variation data,
   not the first process-jet atoms supplied here.

These are mathematically different hypotheses and must not be merged by merely
enlarging the word list. The closest continuation to the canonical-observer
programme is option 1, but it requires the missing `AMJet`/normalization
mechanism identified in note 60.

## 5. Framework lesson

Canonicalization by an invertible static change of frame cannot create a
symmetry absent from the full conjugation-closed generator algebra. A meaningful
"hidden symmetry" claim must specify what changes: locality of the observer,
task equivalence, ambient algebra, or jet order.

This sharpens the API requirement from generic observer search to a narrower
object:

```text
state/history-dependent normalization
  -> derived observer motion
  -> transported process residual
  -> reconstruction certificate
```

