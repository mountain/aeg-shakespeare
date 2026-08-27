# Compact-space Brownian red team

Status: finite cycle phase executed for
[#162](https://github.com/mountain/process-geometry/issues/162); circle
semantics and the sphere claim boundary are frozen.  No continuum heat-kernel
or mixing theorem is claimed.

## 1. Question

The line calibration can suggest that long process time, scale normalization,
and a Gaussian stable law are one universal mechanism.  Compact spaces force
three notions apart:

1. a locally Gaussian small-time chart;
2. a scale-renormalized law on a noncompact space;
3. a time-stationary invariant measure on a compact space.

The native red team starts before a continuum density.  It counts finite
nearest-neighbour histories on the integer lattice and pushes them through a
finite deck quotient.

## 2. Exact cycle quotient

For horizon (N), let

\[
\pi_N(\omega)=\sum_{j=1}^N\xi_j\in\mathbb Z,
\qquad \xi_j\in\{-1,+1\}.
\]

For the finite cycle (C_q=\mathbb Z/q\mathbb Z), the endpoint count at residue
(r) is exactly

\[
c_N^{(q)}(r)
=\sum_{k\in\mathbb Z}c_N(r+kq).
\]

At finite (N), only finitely many lifts have nonzero mass.  The software
retains every pair `(integer lift, count)` rather than discarding it after the
sum.  It then independently performs the chronological update directly on
(C_q) and compares the two constructions residue by residue.

For (q=5,N=7), both constructions return

\[
(14,35,22,22,35),
\]

with total mass (128=2^7).  The residue-zero deck fibre is

\[
\{(-5,7),(5,7)\},
\]

which makes the forgotten lift explicit.

This establishes a finite exact statement:

\[
\boxed{
\text{cycle endpoint counting}
=
\text{integer endpoint counting integrated along deck fibres}
}
\]

It does not require a wrapped Gaussian, Fourier basis, transition matrix, or
heat kernel.

## 3. Winding is task-relative residual information

On (C_4), the equal-horizon histories

\[
(+1,+1,+1,+1),
\qquad
(+1,-1,+1,-1)
\]

have integer lifts (4) and (0), but both have cycle endpoint zero.  Thus the
cycle endpoint quotient is exact for endpoint mass and inadequate for winding,
running extrema, or chronological path tasks.

The continuum circle statement

\[
S^1=\mathbb R/(2\pi\mathbb Z)
\]

has the same structure: a circle endpoint has an integer deck fibre on the
cover.  A wrapped law is the pushforward obtained by integrating over that
fibre.  This continuum interpretation is recorded here but not implemented as
a heat-kernel computation.

## 4. Period two blocks naive time forgetting

For the non-lazy nearest-neighbour walk on an even cycle, every step switches
the parity class.  The clock has period two.  Consequently the terminal law
cannot converge pointwise to the uniform law; its total-variation distance
from uniform is at least (1/2) at every finite time.

The implementation returns a typed `periodic-clock-obstruction` and names the
three distinct repairs:

- add a lazy stay event;
- pass to a continuous-time clock;
- use a Cesaro time observer.

These repairs are not silently identified.  On an odd cycle, or under a
strictly intermediate lazy probability, the clock is irreducible and the
period is one.  Stay probability one is separately rejected as a reducible
clock: the uniform law remains stationary, but every point mass is also
stationary, so stationarity alone cannot establish mixing.

For the exact lazy walk with stay probability (1/2), the uniform law is an
exact one-step fixed point.  A bounded (C_5) audit records decreasing rational
total-variation distances through horizon eight, ending at
(3571/163840).  This is evidence of a bounded trend, not a proof of an
asymptotic mixing theorem.

## 5. Two types of stable law

The red team uses separate machine-readable types:

| Mechanism | Example | Required operation |
| --- | --- | --- |
| `scale-renormalized` | line Gaussian | ensemble growth followed by dynamic spatial rescaling |
| `time-stationary` | uniform cycle/circle law | declared clock evolution on a compact carrier |

The uniform compact law must not be reported as a Gaussian or as a scaling
fixed point.  Conversely, line Brownian has no finite stationary probability
under raw physical-time evolution.

## 6. Sphere gate

The next compact red team is frozen around

\[
S^2=SO(3)/SO(2).
\]

It must retain the following obstructions before any computation is promoted:

- no single global additive position chart;
- no internal global spatial dilation while the radius is fixed;
- a tangent-chart Gaussian is not a global Gaussian law;
- curvature, chart transition, and holonomy remain residuals;
- the long-time stationary candidate is normalized area
  (dA/(4\pi)), not the line Gaussian.

Unlike the circle, (S^2) has no winding deck fibre from a nontrivial universal
cover.  A successful treatment must explain rotation histories and the
stabilizer quotient rather than reuse the circle proof.

## 7. Consequence for the boundary conjecture

The finite result weakens a too-simple claim that physical position must escape
to spatial infinity.  On a compact quotient, position remains bounded while
history depth and forgotten lifts grow.  The more plausible universal object
is therefore the ideal boundary of the time/history fibre, whose task
pushforward may appear as a scale-stable law, Haar measure, Riemannian volume,
or a more detailed path boundary.

The result supports further study of that distinction.  It does not yet prove
that one arithmetic-tower boundary produces all of these measures.
