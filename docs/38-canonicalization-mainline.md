# Canonicalization mainline

**Status:** C1–C4 executable calibrations passed; this mechanism-exploration line is closed.  
**Validated baseline before C4:** `6ce0bb41467880b4b3bb9153c44c44ccaf0bd52b`.  
**C4 validation:** routine Python 3.10–3.14 CI run `32618121736` passed tests, quickstarts, build, metadata checks, and external wheel installation.  
**Next programme step:** return to Sonnet 001 and apply canonicalization *before* completion/Hauffman analysis.

## 1. Frozen mechanism

The validated AEG Analysis order is now

```text
primitive process calculus
-> representation freedom / many lifts
-> local canonicalization
-> induced observer connection / observer ODE
-> canonical lifted path
-> evolution in the canonical representation
-> CanonicalDecomposition
-> representation completion only when genuinely necessary
-> history/interleaving/Hauffman organization
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

The observer ODE is therefore a consequence of canonicalization. It is not a future-aware optimizer, a trajectory oracle, or an externally supplied dynamics.

---

## 2. C1 — Riccati horizontal lift

PR #50, squash commit `29cb2803da1aa2557f323a91a2fa0903a57abd41`.

For

\[
\dot x=(x-t)(x-t-1),
\]

local root normalization derives

\[
r'=1,
\qquad d'=0,
\]

and the canonical lift

\[
\dot y=y^2-y-1.
\]

Arbitrary affine observer rates reconstruct the same base process, while first-order coefficient-jet complexity changes from `2` in fixed/noncanonical controls to `0` canonically.

**What C1 establishes:** the canonical path can be derived locally and can strictly reduce representation variation.

---

## 3. C2 — coupled two-register horizontal lift

PR #51, squash commit `270c0d55bec06645a7765d9de70df6e40b08cc45`.

For

\[
\dot x=e^{-2t}y,
\qquad
\dot y=e^{2t}x,
\]

with determinant-one observer

\[
u=p x,
\qquad v=q y,
\qquad pq=1,
\]

local balance derives

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

The same `2 -> 0` coefficient-jet reduction occurs.

**What C2 establishes:** C1 is not a one-dimensional root-normalization accident; the same semantics survives a genuinely multivariable moving frame.

---

## 4. C3 — Kepler radial moving frame

PR #52, squash commit `6ce0bb41467880b4b3bb9153c44c44ccaf0bd52b`.

Starting from the planar Cartesian Kepler flow, use only local radial alignment

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

with no observer-angle dependence. Since

\[
h=XV,
\qquad
\dot h=0,
\]

the Cartesian flow becomes

\[
\dot X=U,
\qquad
\dot U=\frac{h^2}{X^3}-\frac{\mu}{X^2},
\qquad
\dot\theta=\frac{h}{X^2},
\qquad
\dot h=0.
\]

**What C3 establishes:** canonicalization is not only an algebraic simplification trick. On a physical flow it fixes representation freedom, separates shape from observer motion, and leaves the physical solution set unchanged.

---

## 5. C4 — perturbed Kepler eccentricity frame

Executable essay:

```text
tests/classical/test_perturbed_kepler_eccentricity_canonicalization.py
```

Validation: Python 3.10–3.14 routine CI run `32618121736` passed.

For the perturbed planar Kepler process

\[
\dot{\mathbf r}=\mathbf v,
\qquad
\dot{\mathbf v}
=-\frac{\mu}{r^3}\mathbf r+\mathbf f,
\]

define the eccentricity / Laplace–Runge–Lenz vector

\[
\mathbf e
=
\frac{\mathbf v\times\mathbf h}{\mu}
-
\frac{\mathbf r}{r}.
\]

Direct differentiation cancels the unperturbed inverse-square contribution and leaves exactly

\[
\boxed{
\dot{\mathbf e}
=
\frac{
\mathbf f\times\mathbf h
+
\mathbf v\times(\mathbf r\times\mathbf f)
}{\mu}.
}
\]

Choose a rotating observer whose first axis is locally aligned with `e`:

\[
E_\perp=0,
\qquad
E_\parallel>0.
\]

Writing the perturbation-induced eccentricity-vector rate as

\[
G_\parallel,\qquad G_\perp,
\]

maintaining the canonicalization uniquely induces

\[
\boxed{
\dot\varpi=\frac{G_\perp}{E_\parallel}.
}
\]

Hence the canonical frame itself distinguishes

\[
\boxed{
F_{\rm ren}=G_\parallel
}
\]

as eccentricity-magnitude change and

\[
\boxed{
F_{\rm res}=G_\perp
}
\]

as periapsis/orientation transport absorbed by the observer connection.

At the exact local elliptic calibration state

\[
\mu=1,
\quad
\mathbf r=(1,0),
\quad
\mathbf v=(0,\sqrt{3/2}),
\quad
\mathbf e=(1/2,0),
\]

with local perturbation `f=(f_r,f_t)`, the executable result is

\[
\dot e=\sqrt6\,f_t,
\qquad
\dot\varpi=-\sqrt6\,f_r.
\]

In this two-dimensional eccentricity-vector carrier,

\[
\boxed{F_{\rm comp}=0.}
\]

The perturbation correction is exhausted by shape renormalization plus observer transport.

This zero-completion result is intentionally contrasted with the earlier restricted Kepler function-module calibration, where the second harmonic produces genuine completion. Therefore

\[
\boxed{
F_{\rm comp}
\text{ is representation/task relative, not an intrinsic label on the physical force.}
}
\]

**What C4 establishes:** canonicalization does not merely choose a simpler path; it can generate the `renormalizable / observer-transport` split before completion is considered.

---

## 6. Mechanism-level conclusion

C1–C4 support the following causal chain across algebraic, multivariable, and physical examples:

```text
many representation paths
-> local canonicalization
-> differentiated normalization
-> induced observer ODE
-> distinguished horizontal lift
-> reduced representation variation / shape-gauge separation
-> canonical decomposition
-> completion only for the residual that the chosen representation cannot absorb.
```

The crucial conceptual order is now:

\[
\boxed{
\text{canonicalize first; classify residuals second; complete representation last.}
}
\]

This changes how Sonnet 001 should be revisited. Its existing completion walls, task objectification, controlled interleaving, and Hauffman geometry are downstream evidence. They must not be used to define the canonicalization retroactively.

---

## 7. What remains deliberately unproved

The mechanism closure does **not** establish:

1. that the canonical path globally minimizes a universal representation-cost functional;
2. that every useful canonicalization can be expressed by exact constraints `Phi=0`;
3. that the iterative representation-growth process always closes in finitely many steps;
4. that `F_ren/F_res/F_comp` is representation independent;
5. a universal `CanonicalLift`, bundle, curvature, holonomy, or automatic completion API.

Those are separate research questions, not missing pieces required before using the validated mechanism.

---

## 8. API judgment at closure

Retain the current narrow research surface:

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition
```

Do **not** promote yet:

```text
generic Canonicalization protocol
CanonicalLift / HorizontalPath
universal Completion / ResidualQuotient
representation-complexity scalar
bundle / curvature / holonomy
automatic canonicalization or completion discovery.
```

The experiments justify the semantics of the existing objects, not a broader taxonomy.

---

## 9. Handoff to Sonnet 001

The next research line should begin from the already validated mechanism:

```text
A/M/contact primitive calculus
-> identify representation freedom / lifts
-> derive a local Sonnet canonicalization without using the downstream oracle
-> derive the corresponding observer evolution / canonical history path
-> only then compute F_ren / F_res / F_comp
-> objectify genuine completion residuals
-> reuse controlled interleaving and Hauffman/history geometry downstream.
```

The key question is whether the existing Sonnet wall/history system contains representation freedom that should be quotiented by canonicalization *before* completion search.

`K=13` remains frozen while that representation question is developed.

---

## 10. Evidence boundary

Classical ingredients—Riccati Lie systems, matrix moving frames, central-force reduction, eccentricity-vector mechanics, and moving-frame normalization—are not claimed as new mathematics. The AEG/Shakespeare research claim is the executable ordering

```text
local canonicalization
-> derived observer ODE
-> canonical process path
-> decomposition relative to that path
-> completion only for genuine residuals.
```

This canonicalization mechanism line is now closed. Further progress should occur in a new Sonnet 001 thread rather than by adding C5/C6 calibrations here.
