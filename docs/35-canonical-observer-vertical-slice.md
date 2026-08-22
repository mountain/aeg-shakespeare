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

The first calibrations all accept this boundary.  No `LocalProcessJet` object was
needed yet, so one has not been promoted merely because the theory contains a
jet language.

The A/M re-expression now has its own executable essay:

```text
tests/classical/test_am_process_direction.py
```

which checks the exact chain

```text
A/M ProcessFrame
    -> ProcessDirection
    -> assignment ODE shadow
    -> A/M-specific exact integration.
```

The affine-group / linear-ODE classical background used only for orientation is
cited in that essay [Hall-2015; Coddington-Levinson-1955].

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

There is now **no generic `Canonicalization` alias in the implementation**.  The
first temporary alias was removed after the Riccati/coupled-scalar essays were
migrated to the narrowed name.  This note and the code therefore agree on the
current public research surface.

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

Executable essay:

```text
tests/classical/test_restricted_riccati_canonical_observer.py
```

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
`sl(2)` Riccati realization.  The classical Lie-system identification is cited
in the executable essay [Carinena-Marmo-Nasarre-1998]; it is checked only after
the restricted decomposition, not used as its input.

## 7. Calibration B — two coupled scalar registers

Executable essay:

```text
tests/classical/test_coupled_scalar_canonical_observer.py
```

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

One line in the current external v0.2 theory note has the opposite sign.  The
code and this repository note use the executable convention above.  The sign
does not change the generated matrix algebra, but the discrepancy must be
corrected when the theory note is next revised.

Bidirectional coupling closes to the full matrix algebra (and to `aff(2)` after
translations); one-way coupling remains in the corresponding triangular
subalgebra.  Matrix-Lie-algebra background is cited in the executable essay
[Hall-2015].

## 8. Calibration C — Restricted Kepler function module

Executable essay:

```text
tests/classical/test_restricted_kepler_canonical_decomposition.py
```

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

The same `CanonicalDecomposition` record carries the three roles:

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
Kepler orthogonality/osculation gauge.  Classical central-force, perturbation,
and trigonometric references are carried by the executable essay
[Goldstein-Poole-Safko-2002; Arnold-1989; DLMF-4.21].

## 9. Current API judgment

After the three killer calibrations and the first A/M re-expression:

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

## 10. Literate-programming gate

The new mathematical essays are now required by CI to contain all repository
essay sections:

```text
Question
Primitive data
Classical lineage
Shakespeare reconstruction
Calibration statement
Proof map
Boundary
References
```

The hygiene test also checks that citation keys resolve to entries with useful
locators and that every test function named in the Proof map exists (and every
mathematical test function is represented in that Proof map):

```text
tests/test_canonical_observer_essay_hygiene.py
```

This gate is intentionally scoped to the new vertical slice until the older
classical/research corpus has been audited for the same standard.

## 11. Next development order

The first audit of Pendulum and the two-frequency oscillator has now been
recorded in `docs/36-classical-reexpression-audit.md`: both are important
negative controls against overusing the new vocabulary.

The next genuinely new pressure should therefore come from Sonnet 001 Phase 8,
which will test whether the persistent Hauffman `841/2/6` split can be
rediscovered by the same canonical-decomposition language in a discrete history
domain.  Curvature/holonomy and a generic canonicalization protocol remain
deferred.

## 12. References

[Hall-2015] Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An
Elementary Introduction*, 2nd ed., Graduate Texts in Mathematics 222, Springer,
2015, Chapters 2--3; DOI 10.1007/978-3-319-13467-3.

[Coddington-Levinson-1955] Earl A. Coddington, Norman Levinson, *Theory of
Ordinary Differential Equations*, McGraw-Hill, New York, 1955; linear
differential equations begin p. 62 in the standard edition; ISBN
978-0-07-099256-6.

[Carinena-Marmo-Nasarre-1998] J. F. Carinena, G. Marmo, J. Nasarre,
"The nonlinear superposition principle and the Wei-Norman method,"
arXiv:physics/9802041 (1998), https://arxiv.org/abs/physics/9802041 .

[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*,
2nd ed., Graduate Texts in Mathematics 60, Springer, 1989; DOI
10.1007/978-1-4757-2063-1.

[Goldstein-Poole-Safko-2002] Herbert Goldstein, Charles P. Poole Jr., John L.
Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, Chapter 3,
"The Central Force Problem," ISBN 0-201-65702-3.

[DLMF-4.21] NIST Digital Library of Mathematical Functions, §4.21,
"Identities" for trigonometric functions, https://dlmf.nist.gov/4.21 .
