# Phase 7c — Huffman-style optimization over A/M contact walls

**Status:** first executable representation search in which the continuous A/M
calculus supplies the admissible decision surfaces and history geometry chooses
the tree.

Executable calibration:

```text
tests/research/test_lonely_runner_am_wall_huffman_search.py
```

## 1. From contact flow to decision grammar

For two positive relative speeds, quotient global M scale and write

\[
r=\frac{u_2}{u_1}>1.
\]

A lifted contact event has time

\[
\tau=e^{-v}\alpha,
\]

with contact constant `alpha=n+/-delta`.  Two events exchange order exactly when

\[
\frac{u_2}{u_1}=\frac{\beta}{\alpha}.
\]

Thus the continuous A/M contact calculus generates a family of exact decision
walls

\[
r=\beta/\alpha.
\]

A wall query has three intrinsic outcomes:

```text
r < wall     left chamber
r = wall     contact stratum
r > wall     right chamber
```

This is more faithful than forcing a generic binary representation: exact wall
points can have genuine Lonely Runner witnesses that neither adjacent open
chamber has.

## 2. Discover task-relevant walls, do not supply them

Generate bounded contact constants through center 8, form every collision ratio
`beta/alpha` in `1 < r < 12`, and use the exact first-witness observer to compare
the left chamber, wall stratum, and right chamber.

Most collision walls do not change the task and are discarded.

The surviving walls are discovered as

\[
\boxed{2,4,5,7,8,10,11.}
\]

They split the interval `1 < r <= 12` into

```text
8 open chambers + 7 exact wall strata = 15 strata
```

and all 15 have distinct first-witness semantics.

The important point is that these are not thresholds fitted to the finite input
sample.  They are generated from equality of continuous contact times and then
filtered by the task observer.

## 3. History-geometry objective

Use the finite training distribution

```text
1 <= u1 < u2 <= 12
```

with uniform weight on its 66 literal speed pairs.

The induced weights on the 15 contact strata are

```text
30, 6, 15, 3, 1, 2, 3, 1, 0, 1, 1, 1, 0, 1, 1
```

Now search over **ordered ternary trees whose internal nodes must be one of the
A/M contact walls**.  The cost is weighted root-to-leaf depth, exactly the
time-like coordinate in the history geometry.

Dynamic programming finds the minimum expected-depth wall tree.

Its root is

\[
r=2,
\]

and its total weighted depth is

\[
123.
\]

Therefore the expected number of wall tests is

\[
\boxed{L_{wall}=123/66\approx1.864.}
\]

This is a substantial reduction from the direct contact stopping process
reported in Phase 7b:

\[
L_{contact}=215/66\approx3.258.
\]

The speedup here is in **representation/process depth**, not yet a benchmark of
an upstream C++ implementation.

## 4. Compare with unrestricted ternary Huffman

A wall comparison has three outcomes, so the fair information-theoretic reference
is a ternary prefix code rather than the library's current binary-only Huffman
implementation.

For the same nonzero stratum weights, unrestricted ternary Huffman gives

\[
\boxed{L_{H,3}=108/66\approx1.636.}
\]

Thus the price paid for insisting that every branch be an executable A/M contact
wall is only

\[
\boxed{L_{wall}-L_{H,3}=15/66\approx0.227.}
\]

This is the cleanest result so far connecting the user's history/Huffman geometry
to the new calculus:

```text
AM calculus generates walls
        ->
task observer removes irrelevant walls
        ->
Huffman-style weighted-depth optimization orders the remaining walls
        ->
near-information-optimal executable representation
```

## 5. Holdout: geometry rather than interpolation

The training ratio set is sparse.  In particular it contains no ratio in the
open chamber

\[
7<r<8.
\]

For example

\[
r=15/2=7.5
\]

is absent.

Freeze the wall set, all chamber/wall task semantics, and the tree selected by
the `u<=12` weights.  Then test all distinct speed pairs with

```text
1 <= u1 < u2 <= 16,
ratio <= 12.
```

There are 116 such pairs, including 30 ratio values unseen during training.
Every one is classified into the exact first-witness task class by the frozen
wall tree.

In particular `15/2` is correct even though its entire open chamber had zero
training weight.

This is why the construction is not ordinary supervised interpolation: the
**continuous contact calculus supplies the chamber semantics before the weights
are used to optimize the tree**.

## 6. Space and time interpretation

The Phase-7b stopping tree had a strikingly narrow process frontier: at most four
contact-prefix states on the `u<=12` world, but average depth about `3.258`.

Phase 7c performs process objectification in the time direction.  Instead of
waiting for contact events one by one, it asks a small number of contact-wall
questions that jump directly between chambers/strata.

Thus the emerging optimization picture is genuinely two-dimensional:

- **space-like cost:** boundary/frontier information width;
- **time-like cost:** expected root-to-task depth;
- **admissibility:** every shortcut must be generated from the problem-native
  A/M/contact grammar and preserve exact task semantics.

Huffman is no longer merely a code layered after the mathematics.  It supplies
the variational principle for choosing among executable process trees generated
by the calculus.

## 7. API pressure

The current public `huffman_prefix_code` is binary and assumes the leaf symbols
are already fixed.  This calibration forces a richer research contract:

```text
process-generated decision surfaces
finite task strata
outcome arity of each decision
usage / probability measure
exact task certificate
boundary profile
expected / worst depth
optimal constrained prefix tree
```

No public API should be promoted from one example.  But the likely abstraction is
not simply `HuffmanCode`; it is a **costed task-stopping tree over admissible
process decisions**.

That object would directly unify the history geometry, process objectification,
and presentation-search layers.

## 8. Next step — three relative speeds

The two-speed line is now a successful calibration, not the target theorem.

Stay inside AM and move to three relative speeds.  The M quotient leaves a
2-dimensional relative parameter space.  Contact collisions become walls/curves
in that space; their arrangement defines chambers and lower-dimensional strata.

The next experiment should ask whether Shakespeare can:

1. generate the relevant contact arrangement from the A/M calculus;
2. quotient it by the exact first-witness / bounded-future task;
3. construct a low-frontier stopping tree over admissible wall tests;
4. optimize expected depth using the same history/Huffman principle;
5. transfer the frozen tree/chamber semantics to a larger solved holdout.

If the frontier remains controlled as dimension rises, this becomes a plausible
new representation for the actual Lonely Runner bottleneck.  If the arrangement
explodes immediately, that is the point at which this Sonnet may cease to be a
good calculus killer problem.

## Claim boundary

No new Lonely Runner case is proved here.  The result is a representation theorem
only for the bounded two-relative-speed calibration.

Its significance for Shakespeare is sharper:

\[
\boxed{
\text{continuous A/M calculus}
\to
\text{contact stratification}
\to
\text{Huffman-style optimal stopping tree}
}
\]

is now executable, exact on the calibration domain, and transferable to unseen
ratios inside the frozen geometric domain.
