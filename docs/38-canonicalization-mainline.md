# Canonicalization mainline

**Status:** C1 and C2 merged; C3 physical Kepler moving-frame calibration active.  
**Main baseline after C2:** `270c0d55bec06645a7765d9de70df6e40b08cc45`.  
**Primary question:** can local canonicalization select a distinguished representation path whose induced observer ODE reduces representation complexity before any completion step is invoked?

## 1. Mainline order

The intended AEG Analysis order is frozen as

```text
primitive process calculus
-> local canonicalization
-> induced observer connection / observer ODE
-> canonical lifted path
-> evolution in the canonical representation
-> CanonicalDecomposition
-> representation completion only when genuinely necessary
-> repeat until task closure.
```

Completion and Hauffman/history geometry are downstream mechanisms. They must not replace the logically prior question of which representation path should be used to observe the original process.

## 2. Canonicalization is local, not future-aware optimization

For the current exact-constraint backend,

\[
\Phi(j^kF(x),g)=0,
\]

uses only finite current process data and observer parameters. Maintaining the normalization along the physical flow gives

\[
D_x\Phi\,F + D_g\Phi\,\dot g = 0,
\]

and, on a regular stratum,

\[
\dot g = -(D_g\Phi)^{-1}D_x\Phi\,F.
\]

The observer ODE is therefore derived from the local normalization. It is not selected after inspecting the future trajectory or full propagator.

## 3. C1 — Riccati horizontal lift: passed and merged

Executable essay:

```text
tests/classical/test_riccati_canonical_horizontal_lift.py
```

Merged in PR #50, squash commit `29cb2803da1aa2557f323a91a2fa0903a57abd41`.

Calibration:

\[
\dot x=(x-t)(x-t-1),
\]

with affine observer `x=q+s y` and root normalization

\[
\Phi_0=a+br+cr^2=0,
\qquad
\Phi_1=a+b(r+d)+c(r+d)^2=0.
\]

The executable result is:

- arbitrary local affine observer rates give different lifts of the same base Riccati process;
- instantaneous root normalization reduces the physical shape to
  \[
  \kappa y(y-1),\qquad\kappa=cd;
  \]
- differentiating only the root constraints induces
  \[
  r'=1,\qquad d'=0;
  \]
- the canonical lift is
  \[
  \dot y=y^2-y-1;
  \]
- first-order coefficient-jet complexity is `2` in fixed and noncanonical controls and `0` canonically.

No new public API was needed.

## 4. C2 — coupled two-register horizontal lift: passed and merged

Executable essay:

```text
tests/classical/test_coupled_diagonal_canonical_horizontal_lift.py
```

Merged in PR #51, squash commit `270c0d55bec06645a7765d9de70df6e40b08cc45`.

Calibration:

\[
\dot x=e^{-2t}y,
\qquad
\dot y=e^{2t}x,
\]

with determinant-one diagonal observer

\[
u=p x,\qquad v=q y,\qquad pq=1,
\]

and local balance

\[
b_{12}p^2-b_{21}q^2=0.
\]

The executable result is:

- many determinant-one diagonal observer paths reconstruct the same base process;
- balance collapses the two cross-coupling coefficients to one modulus while `pq=1` fixes common scale gauge;
- frozen observer rates fail to preserve the normalization;
- differentiating the two local constraints induces
  \[
  p'=p,
  \qquad
  q'=-q;
  \]
- the canonical lift is
  \[
  \dot u=u+v,
  \qquad
  \dot v=u-v;
  \]
- coefficient-jet complexity is again `2 -> 0` relative to fixed/noncanonical controls;
- the one-way-coupling stratum is excluded rather than silently forced into this canonicalization.

C2 therefore rejects the explanation that C1 was merely a one-dimensional Riccati/root accident. No new public API was needed.

## 5. C3 — Kepler radial moving frame: active physical pressure test

Current executable essay:

```text
tests/classical/test_kepler_radial_canonical_horizontal_lift.py
```

Start from the planar Cartesian Kepler process and an arbitrary rotating observer. Define

\[
X=\cos\theta\,x+\sin\theta\,y,
\qquad
Y=-\sin\theta\,x+\cos\theta\,y,
\]

with analogous rotated velocities `U,V`. The only canonicalization is local radial alignment

\[
\Phi=Y=0,
\]

on the branch `X>0`.

No polar-coordinate ODE or angular-rate formula is supplied. Differentiating the normalization should force

\[
\dot\theta=\frac{V}{X}=\frac{h}{X^2}.
\]

The intended exact horizontal-lift result is

\[
\dot X=U,
\qquad
\dot U=-\frac{\mu}{X^2}+\frac{V^2}{X},
\qquad
\dot V=-\frac{UV}{X},
\]

so the observer angle disappears from the shape subsystem. Then

\[
h=XV,
\qquad
\dot h=0,
\]

and the original Cartesian flow is represented as

\[
\dot X=U,
\qquad
\dot U=\frac{h^2}{X^3}-\frac{\mu}{X^2},
\qquad
\dot\theta=\frac{h}{X^2},
\qquad
\dot h=0.
\]

C3 is a physical moving-frame calibration. It does not yet claim an osculating-element backend or perturbed-Kepler `F_ren/F_res/F_comp` split.

## 6. What C1+C2 already establish

The mainline is no longer supported by one example. Two independent executable systems now share the same causal structure:

```text
many representation paths
-> local finite canonicalization
-> differentiated normalization
-> induced observer ODE
-> distinguished horizontal lift
-> exact reduction in representation variation.
```

This supports the semantic role of canonicalization and observer connection. It still does **not** establish a universal optimizer/minimum principle.

## 7. Remaining validation gates

A serious canonicalization calibration must continue to distinguish:

1. **gauge multiplicity:** many representation paths exist over the same base process;
2. **locality:** no future trajectory or propagator enters the canonicalization;
3. **derivation:** observer motion follows from maintaining the normalization;
4. **advantage:** the canonical path reduces a declared exact representation-complexity measure or separates shape from gauge variables;
5. **honest completion:** residual directions that cannot be absorbed by observer motion remain explicit rather than being gauged away by definition.

After C3, the next Kepler step should introduce perturbation and ask whether the canonical physical frame naturally exposes `F_ren`, `F_res`, and `F_comp` before reconnecting to the existing restricted function-module completion essay.

## 8. API discipline

The current public/research surface remains

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition
```

Do not add a generic `Canonicalization`, `CanonicalLift`, `HorizontalPath`, `RepresentationComplexity`, bundle, curvature, or holonomy object merely because C1 and C2 succeeded. C3 is still using the exact-constraint backend. A generic canonicalization protocol should wait for an independent calibration that forces a genuinely different backend such as osculation, orthogonality, projection, or stationarity.

## 9. Reference boundary

Moving-frame normalization has classical antecedents, including Fels and Olver's moving-coframe algorithm. Riccati Lie-system structure, matrix linear dynamics, and central-force reduction are classical. The specific AEG/Shakespeare ordering

```text
local canonicalization
-> derived observer ODE
-> canonical process path
-> representation-complexity / shape-gauge comparison
-> completion only for genuine residuals
```

is the project reconstruction and must remain explicitly distinguished from the classical source claims.
