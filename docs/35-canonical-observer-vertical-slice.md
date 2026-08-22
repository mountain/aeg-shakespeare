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

The reusable record does not prescribe the decomposition backend.  Riccati and
coupled-scalar examples partition Lie directions; Restricted Kepler partitions a
finite Fourier/function module; Sonnet 001 Phase 8A now adds a finite persistent
task-state carrier.

The current evidence therefore supports the *shape of the result* across four
qualitatively different carriers while leaving the mechanism discovering the
parts domain-specific.

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

## 9. Calibration D — Sonnet 001 Phase 8A discrete persistent states

Executable essay:

```text
tests/research/test_lonely_runner_canonical_observer_decomposition.py
```

Starting only from the center-2 persistent task representation and the newly
admitted center-3 contact layer, define

```text
A = forced_earlier
B = effective_unresolved_crossing

stable              = not A and not B
transport-only      = A and not B
completion-required = B
```

before evaluating any center-3 child semantics.

The dedicated exact gate recovered

```text
841 stable
2 non-branching changed-witness states
6 genuinely branching states
```

as a disjoint exhaustive partition of 849 task-safe parents.  Only afterwards,
refining 26 old full systems into 298 local children verified that the two
non-branching states each have one changed witness while all six completion
states split; the local update recovers all 75 center-3 semantics.

Recorded evidence:

```text
workflow run 32583659546
Python 3.12.14
1 passed in 5.82 s
```

The duration is provenance only.  Full claim boundary is in
`sonnet/lonely-runner/20-phase8a-discrete-canonical-decomposition.md`.

This result strengthens `CanonicalDecomposition` as a backend-neutral result
shape.  It does **not** establish a discrete `ObserverConnection`: the two
non-branching cases must still be inspected to determine whether the observer
state itself moves or whether only history/witness indexing changes.

## 10. Current API judgment

After the three killer classical calibrations, the A/M negative control, and the
Phase-8A discrete red team:

### Strongest candidates to retain

- `ProcessDirection`;
- generic-provenance `ObserverConnection` for calibrated continuous transports;
- evidence-bearing `CanonicalDecomposition` across Lie, module, and finite task
  carriers.

### Provisional backend

- `ConstraintCanonicalization`.

### Explicitly not promoted yet

- generic `Canonicalization` base class/protocol;
- a discrete observer-connection protocol;
- stationary/cost canonicalization;
- observer bundle;
- local process-jet class;
- curvature/holonomy;
- universal Lie/module/task-state completion API;
- numerical observer ODE integration.

## 11. Literate-programming and consistency gate

The new mathematical essays are required by CI to contain all repository essay
sections:

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

The hygiene test checks citation keys/locators and Proof-map/test correspondence:

```text
tests/test_canonical_observer_essay_hygiene.py
```

Cross-artifact mathematical consistency is now an explicit repository proof
obligation in `docs/11-references-and-test-essays.md`.  The branch maintains an
auditable statement/code/test/reference/status map in

```text
docs/37-canonical-observer-claim-ledger.md
```

so a formula, sign convention, API name, or epistemic-status change cannot be
treated as a prose-only cleanup.

## 12. Next development order

Pendulum and the two-frequency oscillator remain important negative controls,
as recorded in `docs/36-classical-reexpression-audit.md`.

Phase 8A has now passed.  The next task is Phase 8B: inspect the two
non-branching changed-witness states and decide whether they exhibit true
same-family observer transport or merely a history/event-index reparameterization.
No discrete `ObserverConnection` should be introduced before this distinction is
settled.

Curvature/holonomy and a generic canonicalization protocol remain deferred.

## 13. References

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

[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .
