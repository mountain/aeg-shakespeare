# Phase 7e — four-speed scaling red team: sample trees are not geometry

**Status:** negative scaling result that sharpens the next AM-only requirement.

This note is deliberately a red team.  It records an attractive finite-sample
result that **must not** be promoted as a transferable representation.

## 1. Move to three-dimensional relative-M space

For four relative speeds

\[
0<u_1<u_2<u_3<u_4,
\]

quotient global M scale and use

\[
r_i=\frac{u_i}{u_1},\qquad i=2,3,4.
\]

The parameter space is 3-dimensional.

The A/M contact law still generates only pairwise ratio walls:

\[
\boxed{r_j=c\,r_i}
\]

for a contact ratio `c=beta/alpha` and runner pair `i<j`, with `r_1=1`.
Thus the wall families are

```text
r2 = c, r3 = c, r4 = c,
r3 = c*r2, r4 = c*r2, r4 = c*r3.
```

In logarithmic M coordinates

\[
x_i=\log r_i,
\]

these are simply

\[
\boxed{x_j-x_i=\log c.}
\]

This pair-difference form is the structural reason not to fall back to a generic
3D combinatorial search.

## 2. Direct contact-history scale probe

On all

```text
1 <= u1 < u2 < u3 < u4 <= 8
```

there are 70 literal quadruples.

The direct exact contact stopping process has approximately:

```text
25 first-witness task classes
peak frontier            15
boundary volume          88
average stopping depth   5.829
worst stopping depth     15
```

So the space-like frontier remains far smaller than the literal parameter count,
but both frontier and time depth grow relative to the three-speed calibration.

## 3. Tempting but unsafe finite-sample wall search

As a deliberately adversarial shortcut, generate bounded AM contact walls and use
all integer quadruples through speed 10 as a finite calibration set.  A greedy
conflict-separation stage followed by exact dynamic programming can find a small
wall family and a ternary tree that is exact on that finite calibration.

Using the speed<=8 distribution as usage weights, one such tree has weighted
path sum

\[
211
\]

on 70 inputs, hence expected depth

\[
\boxed{211/70\approx3.014.}
\]

Compared with direct contact evolution

\[
5.829\to3.014,
\]

this looks superficially excellent.

But it is not a safe Shakespeare result.

## 4. Frozen holdout failure

Freeze the walls, task map and decision tree.

Now move only one step outward, to all quadruples through speed 11 while keeping
the same relative domain

\[
r_4\le8.
\]

There are 245 such holdout-domain quadruples.  The frozen finite-sample tree makes
errors on 14 of them.

So the apparent compression was partly sample interpolation rather than a
complete contact-geometric quotient.

This is the exact analogue of the fixed-contact-jet failure seen in Phase 7b:

> increasing the size of a finite observation window is not a substitute for
> identifying the full process geometry.

## 5. Why the three-speed result survived and this one did not

Phase 7d did **not** select walls only from integer triples.  It explicitly
constructed every 0D/1D/2D stratum of the bounded rational contact arrangement,
then required the task map to be constant on the retained sign quotient before
any usage weights were introduced.

The four-speed shortcut skipped that completeness step because enumerating a
full generic 3D arrangement looked expensive.

The holdout failure says that this shortcut is not allowed.

## 6. Next abstraction: objectify the pair-difference arrangement

The right response is not brute-force enumeration of more quadruples.

The walls have the special form

\[
x_j-x_i=g,
\qquad g=\log c.
\]

So an AM contact arrangement can be represented by:

```text
runner vertices i
pair edges (i,j)
contact-ratio labels c
three-way sign constraints on u_j/(c*u_i)
consistency / realizability of the joint sign system
exact task observer on arrangement strata
```

This is much smaller and more structured than a generic hyperplane-arrangement
API.  It should remain research-local until an independent problem forces the
same abstraction.

The next implementation should therefore search over **consistent labeled
pair-difference sign systems** rather than enumerate an ambient Cartesian grid.
Huffman/history geometry can then optimize the resulting task-safe decision DAG
or tree.

## 7. Research criterion going forward

A four-speed AM representation is not accepted unless it passes all of:

1. **geometry completeness:** every retained quotient class has certified task
   semantics over the declared bounded contact arrangement, not merely sampled
   tuples;
2. **two-axis cost:** record frontier width/volume and expected/worst depth;
3. **frozen transfer:** larger solved holdout without new walls or task tuning;
4. **native language:** decisions remain A/M contact relations;
5. **no K=13 tuning:** the open frontier stays untouched.

## Claim boundary

The negative result does not weaken the Phase-7d three-speed result.  It prevents
us from overgeneralizing it.

The useful conclusion is:

\[
\boxed{
\text{sample-optimized AM wall tree}\neq
\text{task-complete AM contact geometry}.
}
\]

The next step is therefore structural objectification of the pair-difference
arrangement, not a larger empirical search.
