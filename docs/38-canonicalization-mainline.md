# Canonicalization mainline

**Status:** C1–C3 passed and merged; C4 is parked as an unvalidated follow-up.  
**Main baseline:** `6ce0bb41467880b4b3bb9153c44c44ccaf0bd52b`.  
**Next programme step:** return to Sonnet 001 and reuse the validated canonicalization results there; do not continue expanding this calibration line first.

## 1. Frozen mainline result

The validated AEG Analysis order is

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

For the current exact-constraint backend,

\[
\Phi(j^kF(x),g)=0
\]

uses finite local process data and observer parameters only. Maintaining the normalization gives

\[
D_x\Phi\,F + D_g\Phi\,\dot g = 0,
\]

hence, on a regular stratum,

\[
\dot g = -(D_g\Phi)^{-1}D_x\Phi\,F.
\]

The observer ODE is therefore a consequence of canonicalization, not a future-aware optimizer or an externally supplied dynamics.

## 2. C1 — Riccati horizontal lift: merged

PR #50, squash commit `29cb2803da1aa2557f323a91a2fa0903a57abd41`.

For

\[
\dot x=(x-t)(x-t-1),
\]

local root normalization derives `r_dot=1,d_dot=0` and the canonical lift

\[
\dot y=y^2-y-1.
\]

Arbitrary affine observer rates reconstruct the same base process, while first-order coefficient-jet complexity changes from `2` in fixed/noncanonical controls to `0` canonically.

## 3. C2 — coupled two-register horizontal lift: merged

PR #51, squash commit `270c0d55bec06645a7765d9de70df6e40b08cc45`.

For

\[
\dot x=e^{-2t}y,
\qquad
\dot y=e^{2t}x,
\]

with determinant-one observer `u=p x, v=q y`, local balance plus `pq=1` derives

\[
p'=p,
\qquad q'=-q,
\]

and the canonical lift

\[
\dot u=u+v,
\qquad
\dot v=u-v.
\]

The same `2 -> 0` coefficient-jet reduction occurs, so C1 is not merely a one-dimensional root-normalization accident.

## 4. C3 — Kepler radial moving frame: merged

PR #52, squash commit `6ce0bb41467880b4b3bb9153c44c44ccaf0bd52b`.

Starting from the planar Cartesian Kepler flow, use only the local radial alignment

\[
Y=0,
\qquad X>0.
\]

Differentiating that normalization uniquely gives

\[
\dot\theta=\frac{V}{X}=\frac{h}{X^2}.
\]

The canonical moving frame exposes

\[
\dot X=U,
\qquad
\dot U=-\frac{\mu}{X^2}+\frac{V^2}{X},
\qquad
\dot V=-\frac{UV}{X},
\]

with no remaining observer-angle dependence, and then

\[
h=XV,
\qquad
\dot h=0,
\]

so the Cartesian flow becomes a radial shape ODE plus a conserved parameter and an observer reconstruction quadrature.

This is the first physical verification that canonicalization selects a distinguished observation path without changing the physical solution set.

## 5. What is now established

Three independent executable calibrations support the same causal structure:

```text
many representation paths
-> local finite canonicalization
-> differentiated normalization
-> induced observer ODE
-> distinguished horizontal lift
-> reduced representation variation / shape-gauge separation.
```

This is sufficient evidence to treat canonicalization as the primary research route. It does **not** prove a universal minimum principle or justify a large new public API.

## 6. Parked C4 — perturbed Kepler eccentricity frame

The branch `research/canonicalization-c4-eccentricity-frame` contains an unvalidated follow-up essay:

```text
tests/classical/test_perturbed_kepler_eccentricity_canonicalization.py
```

It explores whether alignment with the local eccentricity/Laplace–Runge–Lenz vector makes perturbation-induced eccentricity-magnitude change appear as `F_ren` and periapsis rotation as `F_res`, with zero completion in that carrier.

This work is **parked, not accepted**. It has not completed the same red-team / CI / merge cycle as C1–C3, and no claim from it should be treated as part of the validated mainline.

## 7. API discipline

The validated reusable surface remains

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition
```

Do not add `CanonicalLift`, `HorizontalPath`, a generic `Canonicalization` protocol, curvature/holonomy, or a universal representation-complexity functional merely from C1–C3.

The next useful pressure should come from applying these validated semantics back to Sonnet 001: first choose/derive the canonical observation path, then ask what residual representation growth and Hauffman/history organization remain.

## 8. Reference boundary

Moving-frame normalization, Riccati Lie-system structure, matrix linear dynamics, central-force reduction, and eccentricity-vector mechanics all have classical antecedents. The project-specific contribution being tested is the ordering

```text
local canonicalization
-> derived observer ODE
-> canonical process path
-> decomposition / completion only after the path is fixed.
```

All executable essays must continue to separate classical source claims from this AEG/Shakespeare reconstruction.
