# Optical Noether discovery — A/M process audit and first exact slice

**Status:** T0 audit plus executable A/M generator slice; no claim of a complete
A/M lift, Noether theorem, or API promotion.

## 1. Why the classical baseline was insufficient

The first prototype in note 59 accepted a conventional density (F(q,v)) and
used forward automatic differentiation to inspect
(\partial F/\partial q^i).  It is a useful control, but it presupposes the
ordinary tangent representation and therefore does not test discovery in A/M
process space.

The stronger desired path is

\[
\text{raw arithmetic process}
\to
\text{A/M history transformation}
\to
\text{canonical process residual}
\to
\text{history payload / Noether charge}.
\]

## 2. Repository capability audit

The current implementation provides:

1. `ProcessFrame`, a declared family of derivations on an expression algebra;
2. `ProcessDirection`, a local combination of declared generators;
3. the one-coordinate affine A/M frame
   \(A=\partial_a\), \(M=\partial_v+a\partial_a\);
4. exact finite and infinitesimal A/M relations, including ([A,M]=A);
5. exact expression residuals through the SymPy representation backend.

It does **not** yet provide:

1. a canonical multi-coordinate A/M process-space lift;
2. synchronized multiplication gauges for positions and process velocities;
3. a second-order A/M jet intrinsic enough for mechanical acceleration;
4. automatic discovery of the A/M frame from raw arithmetic histories;
5. an A/M variational bicomplex or Noether/moment-map constructor;
6. an equivalence theorem connecting an AM charge to
   (\partial F/\partial v_i) only after projection.

The pendulum audit in `docs/vignettes/simple-pendulum.md` already records the
first three limitations.  They are therefore framework gaps, not accidents of
the optical example.

## 3. First executable A/M slice

Within the supported boundary, the new test declares a product assignment
frame for ((x,y,v_x,v_y)):

\[
A_xx=1,\quad
M_xx=x,\quad
M_xv_x=v_x,
\]

with the analogous (y) pair.  It verifies exact copies of

\[
[A_x,M_x]=A_x,
\qquad
[A_y,M_y]=A_y,
\qquad
[A_x,A_y]=0.
\]

The raw graded anisotropic optical density is

\[
F=(1+y^2)\sqrt{4v_x^2+v_y^2}.
\]

The search applies every declared A/M generator and canonicalizes its exact
symbolic residual.  It finds

\[
A_xF=0
\]

and no other invariant generator in the declared frame.  The finite history
(x\mapsto x+\epsilon) independently gives the same zero residual.  Adding
(x^2) destroys the symmetry exactly.

This is stronger than the sampled AD baseline in two respects: the candidate
is a literal process generator in the repository's A/M history calculus, and
the invariance result is an exact expression identity.  It is weaker than the
desired result because the product A/M frame is still declared rather than
discovered.

## 4. Precise stopping boundary

The present A/M layer can certify

\[
\text{declared process generator }A_x
\quad\text{is a symmetry of }F.
\]

It cannot yet derive

\[
A_x
\longmapsto
J_{A_x}
\longmapsto
p_x
\]

inside A/M process space.  Importing (p_x=\partial F/\partial v_x) at this
point would simply reintroduce the classical oracle.  Note 59 therefore remains
the downstream control that supplies the expected projection, not evidence
that AM discovered the charge.

## 5. Next implementation gate

The minimum non-circular advance is an experimental `AMJet`/variation object
with these obligations:

1. obtain its first variation from ordered A/M histories, not from an assumed
   Euclidean tangent vector;
2. retain the noncommutative relation ([A,M]=A);
3. distinguish base-process, velocity/process-jet, and observer-gauge slots;
4. derive a boundary payload for a symmetry generator;
5. project that payload to the classical optical momentum only in the final
   calibration step;
6. fail visibly on the (x^2)-perturbed density.

Until this gate passes, the accurate claim is **exact symmetry discovery in a
declared A/M process frame**, not **AM-Noether discovery**.

## 6. Governance

```text
Epistemic maturity: T0
Role: capability audit plus exact A/M symmetry slice
Theory Map Change: none
Experimental/Public API pressure: AMJet only after a separate design review
```
