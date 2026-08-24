# Noether blind discovery prototype — first falsifiable step

**Status:** T0 classical automatic-differentiation control baseline;
research-local; no API promotion.  This note does not use A/M process space;
the exact supported A/M slice and its stopping boundary are audited in note 60.

## 1. Goal

The preceding calibrations supplied the relevant symmetry and conserved
quantity by hand.  That establishes compatibility, but not discovery.  This
prototype asks a narrower, falsifiable question:

> Given only a raw differentiable process density (L(q,v)), can the program
> identify cyclic coordinate translations and construct their Noether
> momenta without symmetry or charge annotations?

The first target is an anisotropic graded optical density

\[
F(q,v)=(1+y^2)\sqrt{4v_x^2+v_y^2}.
\]

The detector is not told that (x) is cyclic or that the desired charge is
(\partial F/\partial v_x).

## 2. Mechanism

A small forward-mode automatic-differentiation jet evaluates the raw callable
and obtains

\[
\left(
\frac{\partial F}{\partial q^i},
\frac{\partial F}{\partial v^i}
\right)
\]

at several generic probes.  For each coordinate-translation generator
(X_i=\partial_{q^i}), it evaluates the infinitesimal invariance residual

\[
\mathcal L_{X_i}F=\frac{\partial F}{\partial q^i}.
\]

Vanishing residual nominates a cyclic direction.  The generic Noether rule
then pairs that generator with

\[
J_i=\frac{\partial F}{\partial v^i}.
\]

On the unannotated optical density the program discovers only the (x)
translation.  At ((x,y)=(7,0)) and (v=(3,8)), it constructs

\[
F=10,
\qquad
p_x=\frac65,
\qquad
p_y=\frac45.
\]

Adding an explicit (x^2) term destroys the detected symmetry.  This negative
control prevents the test from merely assuming that the first coordinate is
cyclic.

## 3. A second discovered feature: parameter gauge

The raw optical density is one-homogeneous in velocity.  The automatically
constructed momenta obey Euler's identity

\[
p_iv^i=F,
\]

and hence the canonical Hamiltonian

\[
H_c=p_iv^i-F
\]

vanishes.  This recognizes positive path reparameterization as gauge-like and
separates path shape from clock parameterization.

## 4. What has and has not been achieved

Within the conventional tangent representation, this is a move from post-hoc
calibration to constrained discovery:

\[
\text{raw density}
\to
\text{candidate generator}
\to
\text{invariance residual}
\to
\text{Noether covector}.
\]

It does **not** yet prove a symmetry globally.  Finite generic probes can miss
exceptional dependence or cancellations.  Nor does it discover arbitrary Lie
generators, boundary/interface symmetries, gauge transformations, or task
resource maps.  The current scope is deliberately restricted to coordinate
translations so that failure is observable and the detector cannot fit an
unbounded explanatory structure.

More importantly, it does not establish A/M discovery.  The input already
assumes ordinary position/velocity coordinates and the implementation obtains
ordinary partial derivatives by automatic differentiation.  Its proper role is
the classical control oracle against which an independent A/M route must be
calibrated.

## 5. Next gates

1. Replace probe evidence by a symbolic or polynomial identity certificate.
2. Search affine generators rather than coordinate axes alone.
3. Include boundary strata so the anisotropic interface symmetry is recovered
   globally, not layer by layer.
4. Discover gauge-exact changes (A\mapsto A+d\chi) and closed-loop magnetic
   holonomy from a raw connection.
5. Separate symmetry-derived history payloads from task-supplied orders and
   scalarizations.
6. Only after these gates, connect the discovered payload to covariant Bellman
   or Hamilton--Jacobi optimization.

## 6. Governance

```text
Epistemic maturity: T0
Role: constrained blind-discovery prototype
Theory Map Change: none
Experimental/Public API pressure: none
```
