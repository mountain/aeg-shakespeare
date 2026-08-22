# Phase 7d — three-speed A/M arrangement and two-axis history optimization

**Status:** exact bounded 2D relative-M calibration; still inside Gate A.

Executable calibration:

```text
tests/research/test_lonely_runner_three_speed_am_huffman.py
```

## 1. Why this is the first serious dimensional test

For three relative speeds

\[
0<u_1<u_2<u_3,
\]

quotient the global multiplicative scale and write

\[
r_2=\frac{u_2}{u_1},\qquad r_3=\frac{u_3}{u_1}.
\]

The parameter space is now genuinely two-dimensional:

\[
1<r_2<r_3.
\]

This is where the AM-first programme could have failed immediately through a
combinatorial explosion of contact histories.

Instead, the contact calculus gives a very restricted arrangement.

## 2. The calculus generates only three wall families

For `k=3` the Lonely Runner threshold is

\[
\delta=\frac14.
\]

Every lifted contact time is

\[
\tau_i=e^{-v_i}\alpha,
\qquad
\alpha=n\pm\frac14.
\]

Equality of two contact times can therefore only produce:

\[
\boxed{
 r_2=c,\qquad
 r_3=c,\qquad
 r_3=c\,r_2,
}
\]

where

\[
c=\beta/\alpha.
\]

So the 2D contact arrangement is not an arbitrary algebraic decomposition.  It
consists of vertical, horizontal, and multiplicative-diagonal line families.
This is the finite geometric shadow of the same A/M contact flow used in the
one-dimensional calibration.

## 3. Exact bounded arrangement

Fix the calibration domain

\[
1<r_2<r_3\le8.
\]

Generate contact constants through center 3.  They yield 17 distinct collision
ratios in the domain, hence

```text
17 ratios x 3 wall families = 51 candidate walls.
```

The test constructs their arrangement using exact rational arithmetic only.  No
floating-point geometry package is used.

Representatives are generated for every 0D, 1D, and 2D stratum by exact line
intersections, edge midpoints, and certified small normal perturbations.

The full arrangement contains

\[
\boxed{1771\text{ geometric strata}.}
\]

An independent first-witness oracle is allowed to inspect contact centers through
12, so the task is not defined by the same center-3 truncation used to propose
walls.  On every exact arrangement stratum the first witness is nevertheless
reached without needing a contact center above 3.

Across the 1771 strata there are

\[
\boxed{44\text{ distinct first-witness semantics}.}
\]

## 4. Task semantics removes most of the calculus geometry

A candidate wall is retained only if deleting its sign coordinate would merge
strata with different first-witness tasks.

The original 51 walls collapse to only 17 task-relevant walls.

Eight are genuinely diagonal relative-M comparisons:

\[
\frac{r_3}{r_2}\in
\left\{
\frac{11}{9},
\frac97,
\frac75,
\frac53,
\frac95,
\frac{11}{5},
\frac73,
\frac{13}{5}
\right\},
\]

and the remaining nine are the vertical/horizontal/diagonal walls at

\[
3,5,7.
\]

After keeping only these signs, the 1771 geometric strata reduce exactly to

\[
\boxed{181\text{ task-relevant sign strata}}
\]

while preserving all 44 witness semantics.

This is an important hierarchy:

```text
literal continuous arrangement      1771 strata
        ↓ task-relative wall removal
task-relevant AM arrangement          181 strata
        ↓ observer quotient
first-witness semantics                 44 classes
```

## 5. Hauffman/history geometry chooses the executable tree

Geometry discovery is kept separate from usage weighting.

Only after the 181 exact task strata are frozen do we introduce the training
measure consisting of all

```text
1 <= u1 < u2 < u3 <= 10,
u3/u1 <= 8,
```

namely 105 literal triples.

Search over ternary decision trees whose internal nodes must be one of the 17
surviving A/M contact walls.  Each query has the intrinsic outcomes

```text
< wall
= wall
> wall.
```

Exact dynamic programming minimizes lexicographically:

1. weighted root-to-task depth;
2. unweighted geometric-stratum depth;
3. internal decision-node count.

The optimum has

```text
weighted path sum      282
unweighted path sum    837
internal wall nodes     43
```

and begins with the horizontal contact wall

\[
\boxed{r_3=3.}
\]

Thus the training-distribution expected decision depth is

\[
\boxed{282/105\approx2.686.}
\]

## 6. The key result is two-axis dominance

This is where the user's Hauffman history geometry becomes essential.  We do not
judge the representation by class count alone.

### Literal event-by-event contact stopping tree

Over the complete 1771-stratum geometry its boundary widths are

```text
1, 1, 3, 9, 20, 28, 31, 34, 29, 25, 15, 10, 1, 1
```

so

\[
W_{\max}=34,
\qquad
\sum_dW(d)=208,
\qquad
d_{\max}=13.
\]

On the 105-triple usage distribution the average stopping depth is

\[
468/105\approx4.457.
\]

### Optimized A/M wall tree

Its complete-geometric boundary widths are

```text
1, 3, 3, 9, 21, 27, 27, 24, 12, 3
```

so

\[
W_{\max}=27,
\qquad
\sum_dW(d)=130,
\qquad
d_{\max}=9.
\]

The usage-weighted expected depth is

\[
282/105\approx2.686.
\]

Therefore the optimized representation improves every recorded history-geometry
axis relative to literal contact evolution:

\[
\boxed{
\begin{aligned}
\text{peak width:}&\quad34\to27,\\
\text{boundary volume:}&\quad208\to130,\\
\text{worst depth:}&\quad13\to9,\\
\text{mean task depth:}&\quad4.457\to2.686.
\end{aligned}
}
\]

This is stronger than a time/space trade-off.  On this calibration the
calculus-generated/Hauffman-selected tree **dominates** the literal contact tree
on both space-like and time-like complexity.

## 7. Holdout

Freeze:

- all candidate contact ratios;
- the 17 task-relevant walls;
- the 181-stratum task map;
- the decision tree.

Then test every

```text
1 <= u1 < u2 < u3 <= 20,
u3/u1 <= 8.
```

There are

\[
\boxed{928}
\]

such triples.

Every triple is classified into the exact first-witness semantics by the frozen
wall tree.  No wall or tree parameter is learned on the holdout.

Exploratory checks beyond the committed regression have also succeeded on much
larger integer and rational samples inside the same geometric domain; those are
not elevated to claim status here.

## 8. What has changed conceptually

The emerging computation is no longer

```text
enumerate speed tuples
    -> simulate / set-cover
    -> prune
```

but

```text
A/M differential contact law
    -> contact-collision arrangement
    -> task-relative wall quotient
    -> history-geometry optimization
    -> low-width, low-depth executable decision tree
```

In particular, the Hauffman structure is no longer merely an after-the-fact code
for known outcomes.  It is functioning as the variational principle that chooses
which calculus-generated distinctions should be asked, and in what order.

## 9. Next threshold

Still do not open unrestricted Gate B.

The next question is scaling in dimension and task horizon:

1. repeat the same construction for four relative speeds on a deliberately small
   solved world;
2. record growth of candidate walls, task-relevant strata, peak frontier,
   boundary volume, and expected depth;
3. compare growth against literal parameter/history counts;
4. search for repeated wall-arrangement motifs that can be objectified as new
   process primitives rather than recursively querying pairwise walls;
5. only if this native-language frontier stabilizes should the AM presentation be
   frozen and compared against unrestricted Shakespeare presentations.

The crucial quantity is now the growth law of the optimized history geometry,
not raw search-node count.

## Claim boundary

No new Lonely Runner case is proved.  This remains a bounded representation
calibration for three relative speeds.

What is established is the first nontrivial-dimensional closed loop

\[
\boxed{
\text{A/M calculus}
\to
\text{2D contact arrangement}
\to
\text{exact task quotient}
\to
\text{Hauffman/history optimization}
\to
\text{simultaneous space/time compression}.
}
\]
