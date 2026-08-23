# Canonicalization mainline

**Status:** active research line after PR #49 closure.  
**Base:** squash-merged `main` commit `a5f6aad35cb930a664229bddadfc291087c49ae9`.  
**Primary question:** can local canonicalization select a distinguished representation path whose induced observer ODE reduces representation complexity before any completion step is invoked?

## 1. Mainline order

The intended AEG Analysis order is now frozen as

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

This order matters.  Completion and Hauffman/history geometry are downstream mechanisms.  They must not replace the logically prior question of which representation path should be used to observe the original process.

## 2. Canonicalization is not a future-aware optimizer

A canonicalization is local.  In the exact constraint backend it has the form

\[
\Phi(j^kF(x),g)=0,
\]

where `g` is the observer representation and only finite current process data are allowed.  Maintaining the normalization along the physical flow gives

\[
D_x\Phi\,F + D_g\Phi\,\dot g = 0,
\]

hence, on a regular stratum,

\[
\dot g = -(D_g\Phi)^{-1}D_x\Phi\,F.
\]

The observer ODE is therefore derived from the local normalization.  It is not selected after inspecting the future trajectory or full propagator.

## 3. C1 — Riccati horizontal-lift calibration

The first mainline executable essay is

```text
tests/classical/test_riccati_canonical_horizontal_lift.py
```

It uses

\[
\dot x=(x-t)(x-t-1)
\]

and the affine observer family `x=q+s y`.

The experiment must establish all of the following in one file:

1. **many lifts:** arbitrary local observer rates produce different lifted coefficient triples while reconstructing the same base Riccati process exactly;
2. **local quotient:** instantaneous root normalization sends the physical Riccati polynomial to the one-modulus family
   \[
   \kappa y(y-1),\qquad \kappa=cd;
   \]
3. **derived transport:** differentiating only the root constraints induces the observer rates;
4. **horizontal path:** for the declared nonautonomous coefficient path the induced rates are `r_dot=1,d_dot=0`;
5. **representation advantage:** the canonical lift is
   \[
   \dot y=y^2-y-1,
   \]
   while fixed and noncanonical lifts remain explicitly time dependent;
6. **bounded complexity certificate:** first-order coefficient-jet complexity changes from `2` in the fixed and noncanonical frames to `0` in the canonical frame.

The purpose is not to claim a universal minimum principle.  It is to demonstrate the complete causal chain

```text
representation freedom
-> local normalization
-> induced observer ODE
-> distinguished path
-> exact reduction in representation variation.
```

No new public API is introduced by C1.

## 4. C2 — coupled moving frame

C2 should pressure-test C1 in a genuinely multivariable system.  The target properties are:

- a non-scalar observer family;
- canonicalization derived from local process data rather than an externally supplied matrix ODE;
- exact observer transport in a triangular/affine matrix family;
- a red team separating one-way coupling from two-way coupling;
- a representation-complexity metric that cannot be explained by one-dimensional root normalization alone.

Only if C1 and C2 preserve the same semantic role should a generic `Canonicalization` protocol or `CanonicalLift` object be considered.

## 5. C3 — Kepler moving observer

C3 is the first physical pressure test.  It should use a genuinely moving local frame and distinguish

\[
F_{\rm ren},\qquad F_{\rm res},\qquad F_{\rm comp}
\]

without assuming a Fourier or linear spectral ontology as primitive input.

A successful C3 would connect canonical observation paths to the existing restricted Kepler function-module completion results.

## 6. Success criteria for the mainline

The mainline is not validated merely because `ConstraintCanonicalization.induced_connection()` returns a symbolic solution.  Each serious calibration must distinguish:

1. **gauge multiplicity:** many representation paths exist over the same base process;
2. **locality:** no future trajectory or propagator enters the canonicalization;
3. **derivation:** observer motion follows from maintaining the normalization;
4. **advantage:** the canonical path reduces a declared exact representation-complexity measure against fixed and noncanonical controls;
5. **honest completion:** residual directions that cannot be absorbed by the observer remain explicit rather than being gauged away by definition.

## 7. API discipline

The merged research surface already contains

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition
```

These remain sufficient for C1.  Do not add a generic `Canonicalization`, `CanonicalLift`, `HorizontalPath`, `RepresentationComplexity`, bundle, curvature, or holonomy object until at least two independent executable essays need to retain the same information.

The immediate research priority is therefore **canonicalization semantics and measurable path advantage**, not API breadth.

## 8. Reference boundary

Moving-frame normalization has classical antecedents, including Fels and Olver's moving coframe algorithm.  Riccati Lie-system structure is classical.  The specific ordering

```text
local canonicalization -> derived observer ODE -> representation-complexity comparison
```

is the Shakespeare/AEG reconstruction and should be labeled as such in executable essays.
