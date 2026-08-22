# Canonical observer vertical slice

**Status:** research-only API shaping; not part of the 0.0.2 compatibility contract.

## 1. Why this slice exists

The current AEG Analysis programme gives the causal order

```text
local canonicalization
    -> observer connection
    -> observer/process ODE
    -> canonical decomposition
    -> transport or minimal completion
```

The implementation should preserve that order without turning every theoretical
term into a Python class before independent examples force the same retained
semantics.

This branch therefore introduces only four small roles:

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition
```

They are calibrated simultaneously rather than frozen in advance.

## 2. `ProcessDirection`

`ProcessDirection` lives under `process.local` and represents only

\[
\mathscr D=\sum_i u_iX_i
\]

for an already-declared `ProcessFrame`.

It can be lowered to a one-generator `ProcessSystem` assignment shadow, but it is
not a path, solver, connection, or reparameterization class.  Proportional
directions are not automatically identified: Sundman-type examples show that
parameterization can change analytic and reconstruction complexity.

The first three calibrations all accept this boundary.  No `LocalProcessJet`
object was needed yet, so one has not been promoted merely because the theory
contains a jet language.

## 3. Exact constraint canonicalization

The first concrete backend is `ConstraintCanonicalization`:

\[
\Phi(\text{local data},g)=0.
\]

It differentiates the exact constraints along caller-declared local base rates
and solves for observer-parameter rates.  A unique local solution produces an
`ObserverConnection` carrying the differentiated residual certificate.

This is intentionally narrower than a universal `Canonicalization` class.
Restricted Kepler already shows why: orthogonality/osculation or stationarity
conditions should not be disguised as algebraic equations merely to fit the
first implementation.

A hidden, non-exported `Canonicalization` alias exists only as a transition aid
inside the first research commits and must be removed before this slice is
promoted or merged as a stable interface.

## 4. `ObserverConnection`

`ObserverConnection` is an evidence-bearing local transport record:

```text
canonicalization provenance
base rates
observer rates
exact residuals
```

Its provenance carrier is generic.  The connection object therefore does not
commit future backends to the exact-constraint implementation.

The object deliberately does not yet define:

- a principal bundle;
- horizontal/vertical projections;
- composition;
- curvature;
- holonomy;
- path-ordered numerical integration.

Those structures should be promoted only after independent executable essays
show what information must survive.

## 5. `CanonicalDecomposition`

`CanonicalDecomposition` records the working split

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp}
\]

as three caller-defined parts plus evidence.

The reusable record does not prescribe the decomposition backend.  This is
already necessary: Riccati and coupled-scalar examples partition Lie directions,
whereas Restricted Kepler partitions a finite Fourier/function module.

The current evidence says the *shape of the result* is reusable while the
mechanism discovering the parts is not yet universal.

## 6. Calibration A — Restricted Riccati

Start from

\[
\Xi=aA+bM+cQ,
\qquad
A=\partial_x,\quad
M=x\partial_x,\quad
Q=x^2\partial_x,
\]

but restrict the observer family to affine transformations.

The two instantaneous-root conditions select the affine observer.  Their
differentiation induces the root/separation transport.  In the moving coordinate
`y=(x-r)/d`, the process becomes

\[
\dot y
=-\frac{\dot r}{d}
+\left(-\kappa-\frac{\dot d}{d}\right)y
+\kappa y^2,
\qquad \kappa=cd.
\]

The first two directions lie in the restricted affine observer algebra; `Q`
remains outside it.  The exact completion bracket table is

\[
[A,M]=A,\qquad [A,Q]=2M,\qquad [M,Q]=Q,
\]

so adjoining the residual direction gives the standard three-dimensional
`sl(2)` realization.

This is the first exact calibration of

```text
canonicalize -> transport -> genuine completion.
```

## 7. Calibration B — two coupled scalar registers

For

\[
\dot x=b_{11}x+b_{12}y,
\qquad
\dot y=b_{21}x+b_{22}y,
\]

start from independent scalar rulers and define

\[
E_{12}=y\partial_x,
\qquad
E_{21}=x\partial_y.
\]

A relative scale `rho` is locally canonical when

\[
b_{12}\rho^2-b_{21}=0.
\]

Differentiating that condition gives

\[
\frac{\dot\rho}{\rho}
=\frac12\left(
\frac{\dot b_{21}}{b_{21}}-
\frac{\dot b_{12}}{b_{12}}
\right)
\]

on the canonical leaf.  This observer motion remains diagonal, while both cross
couplings survive as completion directions.

### Bracket-sign audit

The repository defines

\[
[X,Y]=X(Y)-Y(X).
\]

With the displayed `E12,E21` definitions this gives

\[
[E_{12},E_{21}]=M_2-M_1.
\]

One line in the current v0.2 theory note has the opposite sign.  The sign does
not change the generated matrix algebra, but future notes/tests should use the
repository convention consistently.

Bidirectional coupling closes to the full matrix algebra (and to `aff(2)` after
translations); one-way coupling remains in the corresponding triangular
subalgebra.  This is an important minimality red team.

## 8. Calibration C — Restricted Kepler function module

Use

\[
\mathcal K_1=\operatorname{span}\{1,\cos\psi,\sin\psi\},
\qquad
L_K=R^2+1,
\quad R=\partial_\psi.
\]

For the squared Kepler shape forcing,

\[
(\alpha+b\cos\psi)^2
=
\left(\alpha^2+\frac{b^2}{2}\right)
+2\alpha b\cos\psi
+\frac{b^2}{2}\cos2\psi.
\]

The same `CanonicalDecomposition` record can carry the three roles:

```text
n=0  -> renormalizable
n=1  -> resonant observer transport
n=2  -> representation completion
```

because

\[
L_K1=1,
\qquad
L_K\cos\psi=0,
\qquad
L_K\cos2\psi=-3\cos2\psi.
\]

The second harmonic forces the minimal `R`-closed extension

\[
\mathcal K_2
=
\operatorname{span}
\{1,\cos\psi,\sin\psi,\cos2\psi,\sin2\psi\}.
\]

Crucially, this vignette does **not** use `ConstraintCanonicalization` for the
Kepler orthogonality/osculation gauge.  That absence is evidence: the generic
canonicalization interface is not yet known well enough to freeze.

## 9. Current API judgment

After the three calibrations:

### Strongest candidates to retain

- `ProcessDirection`;
- generic-provenance `ObserverConnection`;
- evidence-bearing `CanonicalDecomposition`.

### Provisional backend

- `ConstraintCanonicalization`.

### Explicitly not promoted yet

- generic `Canonicalization` base class/protocol;
- stationary/cost canonicalization;
- observer bundle;
- local process-jet class;
- curvature/holonomy;
- universal Lie/module completion API;
- numerical observer ODE integration.

## 10. Next development order

The next stage should use the current slice to re-read existing classical essays
rather than enlarge the abstraction first.

Suggested migration order:

1. Translation / Dilation / A-M: expose process directions and distinguish
   process paths from assignment ODE shadows.
2. Pendulum discovery sequence: retain it as a likely static/trivial-connection
   control; do not force observer dynamics where none is needed.
3. Oscillator / coefficient-extension red team: reinterpret refinement through
   decomposition/completion cost without asserting that finer splitting is
   canonical.
4. Galilean / magnetic translations: keep as future pressure for lifted
   transport/holonomy, not as justification to add curvature now.
5. Sonnet 001 Phase 8: test whether the persistent Hauffman `841/2/6` split can
   be rediscovered from the same canonical-decomposition language in a discrete
   domain.

Only after these migrations should the branch decide what deserves a stable
semantic namespace export and remove the transition alias.
