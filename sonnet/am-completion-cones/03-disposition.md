# Disposition: `CHAMBERS`

Status: mathematical disposition for the initial scope of issue #148.

## Decision

The initial rational-polyhedral AM completion problem receives the disposition

\[
\boxed{\texttt{CHAMBERS}}.
\]

The correct bounded object is not one pointed cone invariant under all power
translations.  It is a chambered system of cone-bounded completions.

For a pointed rational cone `C` and affine monoid \(S=C\cap G\), define
sectors

\[
\mathcal H_{g_0,C}=K[[g_0+S]].
\]

Their products and AM actions are typed by degree:

\[
\mathcal H_{g_0,C}\mathcal H_{g_1,C}
\longrightarrow
\mathcal H_{g_0+g_1,C},
\]

\[
A:\mathcal H_{g_0,C}
\longrightarrow
\mathcal H_{g_0-e_\nu,C},
\]

\[
M:\mathcal H_{g_0,C}
\longrightarrow
\mathcal H_{g_0,C},
\]

\[
P_A:\mathcal H_{g_0,C}
\dashrightarrow
\mathcal H_{g_0+e_\nu,C}.
\]

The dashed arrow records the resonance wall `nu=-1`, where the codomain must
include a typed `log-a` sector.

## Why not `CONE`

A fixed pointed cone cannot be invariant under both `+e_nu` and `-e_nu`.
Demanding literal closure under differentiation and primitives would insert a
line into the cone and destroy the finite-observer property.

The operators remain continuous because their degree shifts are bounded.  The
correct repair is typed chamber transport, not abandonment of completion.

## Why not `RAY-ONLY`

The two-generator calibration computes

\[
[X^2Y^2]\exp(X+Y+XY)=\frac74
\]

and exactly replays both `A` and `M`.  Thus the rank-one compiler's mathematics
extends coherently to a genuine rational bigrading.

## Why not `HIGHER-SUPPORT`

Pointed rational-polyhedral cones already guarantee:

- finite bounded observer slices;
- finite coefficient convolution;
- well-defined completed `exp` and `log1p` on the augmentation ideal;
- cofinality of all interior observer heights;
- continuous fixed-degree AM transport.

No frozen obstruction currently requires Hahn, transseries, hyperseries, or
surreal support.  Such objects remain candidates only if later tasks require
non-polyhedral well-ordered supports, unbounded rank raising, or symbolic
iteration heights.

## Consequence for the programme

The arithmetic geometry has acquired a more precise form:

> AM completion is a chambered, observer-filtered geometry over the
> `(power, character)` lattice.  Observer heights choose finite views; AM
> operators transport between views; resonance walls force typed extensions.

This is stronger than the first compiler result and narrower than a general
transseries claim.  It also explains why an observer with finite reach does
not need the whole ensemble: the declared cone and height make every visible
slice finite, while the completed carrier is recovered as their inverse
limit.

## Next mathematical gate

The next gate should study cone changes rather than parser syntax:

1. define transport between two different pointed cones sharing a face;
2. determine when their completed sectors glue along the common chamber;
3. identify the cocycle or obstruction carried by successive chart changes;
4. test whether this gluing recovers the AM affine action independently of a
   chosen cone.

That is the first place where completion, fibering, observer charts, and the
earlier ensemble discussion meet in one exact construction.
