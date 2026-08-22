# Canonical-observer claim ledger

**Status:** auditable research ledger for `research/canonical-observer-api`; not a stable API specification.

## 1. Purpose

For this research line, mathematical prose, executable code, test claims, and
bibliography are one artifact with several views.  A change is incomplete if it
updates only one view.

The ledger records, for each promoted or calibrated statement:

```text
mathematical statement
    <-> implementation owner
    <-> executable certificate
    <-> cited classical lineage
    <-> epistemic status
```

It does **not** make prose correctness mechanically decidable.  Its purpose is to
make discrepancies visible and reviewable.  The routine CI gate
`tests/test_canonical_observer_essay_hygiene.py` checks the mechanically
auditable subset: required essay sections, citation resolution/locators, and
Proof-map/test correspondence.

## 2. Process direction

### Statement

Given a declared process frame `X_i`,

\[
\mathscr D=\sum_i u^i X_i.
\]

The assignment ODE is a shadow obtained by applying `D` to assignment symbols;
`ProcessDirection` itself is not a trajectory, solver, or observer connection.

### Implementation owner

```text
src/aeg_shakespeare/process/local/direction.py
    ProcessDirection.apply
    ProcessDirection.assignment_rules
    ProcessDirection.as_system
```

### Executable certificates

```text
tests/classical/test_am_process_direction.py
    test_am_process_direction_has_the_expected_assignment_shadow

tests/classical/test_restricted_riccati_canonical_observer.py
    test_process_direction_precedes_assignment_ode

tests/classical/test_coupled_scalar_canonical_observer.py
    test_bidirectional_cross_coupling_forces_matrix_completion
```

### Classical lineage

- Hall 2015 for matrix Lie group/algebra background.
- Coddington--Levinson 1955 for the ordinary linear-ODE shadow.

### Status

**Implemented/calibrated.**  No claim of universal closed-form integration or
reparameterization invariance.

---

## 3. Exact constraint canonicalization

### Statement

A local observer may be selected by exact constraints

\[
\Phi(z,g)=0.
\]

Along declared base rates, maintaining the constraints gives

\[
D_z\Phi\,\dot z+D_g\Phi\,\dot g=0.
\]

When the symbolic local solution for `dot g` is unique, it defines the first
implemented observer-connection backend.

### Implementation owner

```text
src/aeg_shakespeare/presentation/canonicalization.py
    ConstraintCanonicalization.differentiated_constraints
    ConstraintCanonicalization.induced_connection
```

There is deliberately **no generic `Canonicalization` alias or base protocol** at
this stage.

### Executable certificates

```text
tests/classical/test_restricted_riccati_canonical_observer.py
    test_affine_root_canonicalization_induces_observer_connection

tests/classical/test_coupled_scalar_canonical_observer.py
    test_relative_scale_canonicalization_induces_connection
```

### Status

**Implemented backend, not universal definition.**  Kepler
orthogonality/osculation is the explicit red team showing that future
canonicalization backends need not be algebraic constraints.

---

## 4. Observer connection

### Statement

Observer dynamics is recorded as transport induced by maintaining the chosen
local canonical representation.  The current object stores provenance, base
rates, observer rates, and residual certificates; it does not yet assert a full
principal-bundle connection theory.

### Implementation owner

```text
src/aeg_shakespeare/analysis/connection.py
    ObserverConnection
```

### Executable certificates

Riccati and coupled-scalar tests above require

```text
connection.certified == True
```

and check the exact induced parameter rates.

### Status

**Evidence-bearing local transport record.**  Curvature, holonomy, horizontal
projection, composition, and path-ordered numerical transport remain unpromoted.

---

## 5. Canonical decomposition

### Statement

The working AEG Analysis split is

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp},
\]

read operationally as

```text
renormalize / remain in current representation,
transport / resonant observer motion,
complete / enlarge the representation.
```

The current API records a claimed split plus evidence; it does not prescribe a
universal projection/decomposition algorithm.

### Implementation owner

```text
src/aeg_shakespeare/analysis/decomposition.py
    CanonicalDecomposition
```

### Independent carrier calibrations

```text
Restricted Riccati
    Lie-direction carrier
    Q is completion relative to affine observer family

Coupled scalar registers
    multivariable Lie-direction carrier
    E12,E21 are completion relative to independent scalar rulers

Restricted Kepler
    finite function-module carrier
    n=0 / n=1 / n=2 -> renormalizable / resonant / completion

Lonely Runner Phase 8A (opt-in gate)
    finite persistent task-state carrier
    acceptance target 841 / 2 / 6
```

### Status

**Reusable result shape under cross-calibration.**  A universal discovery backend
or categorical unification of Lie and module completion remains an open research
question.

---

## 6. Riccati completion and bracket convention

### Statement

With repository convention

\[
[X,Y]=X(Y)-Y(X),
\]

and

\[
A=\partial_x,\quad M=x\partial_x,\quad Q=x^2\partial_x,
\]

we have

\[
[A,M]=A,
\qquad
[A,Q]=2M,
\qquad
[M,Q]=Q.
\]

### Executable certificate

```text
tests/classical/test_restricted_riccati_canonical_observer.py
    test_restricted_affine_observer_leaves_q_as_completion_direction
```

### Classical lineage

Cariñena--Marmo--Nasarre 1998; Hall 2015.

### Status

**Implemented exact bracket certificate.**  The classical `sl(2)` identification
is a shadow checked after the restricted affine decomposition.

---

## 7. Coupled-scalar sign audit

### Statement

With

\[
E_{12}=y\partial_x,
\qquad
E_{21}=x\partial_y,
\]

and the repository commutator convention,

\[
\boxed{[E_{12},E_{21}]=M_2-M_1.}
\]

### Implementation / certificate

```text
src/aeg_shakespeare/process/local/frame.py
    ProcessFrame.commutator

tests/classical/test_coupled_scalar_canonical_observer.py
    test_bidirectional_cross_coupling_forces_matrix_completion
```

### Consistency note

The externally supplied AEG Analysis v0.2 research note currently contains one
line with the opposite sign `M1-M2`.  Repository code/tests/docs use the
executable convention above.  The external note should be corrected at its next
revision; the structural statement that bidirectional shears generate the full
matrix algebra is unchanged.

### Status

**Known documentation discrepancy, localized and recorded.**

---

## 8. Restricted Kepler three-sector calibration

### Statement

For

\[
\rho_0=\alpha+b\cos\psi,
\qquad L_K=R^2+1,
\]

\[
\rho_0^2=
\left(\alpha^2+\frac{b^2}{2}\right)
+2\alpha b\cos\psi
+\frac{b^2}{2}\cos2\psi,
\]

with

\[
L_K1=1,
\quad L_K\cos\psi=0,
\quad L_K\cos2\psi=-3\cos2\psi.
\]

The restricted calibration labels these three sectors renormalizable,
resonant/transport, and completion respectively.  `R` then forces the companion
`sin(2 psi)` and hence the degree-two five-dimensional closed module.

### Executable certificate

```text
tests/classical/test_restricted_kepler_canonical_decomposition.py
```

### Classical lineage

Goldstein--Poole--Safko 2002, Arnold 1989, NIST DLMF §4.21.

### Status

**Bounded first-order calibration.**  Not a general perturbation theorem and not
a generic osculation/canonicalization backend.

---

## 9. Negative controls

### A/M

`ProcessDirection` is needed; `ObserverConnection` is not.  This prevents
conflating physical/process trajectory with observer transport.

### Pendulum

The selected `pair(q,e)` is a task-relative scalar **observable**, not the
dynamic observer state of the connection programme.

### Two-frequency oscillator

Coefficient-field refinement from two quadratic factors to four linear factors
is an exact presentation refinement but is not forced process completion; both
presentations remain Pareto-incomparable under the red-team cost profile.

### Galilean / magnetic translations

Central cocycle residuals pressure future lift/holonomy concepts but are not, by
themselves, observer connections.

### Status

**Implemented/audited boundaries.**  These negative controls are part of the API
evidence, not exclusions to be erased by later refactoring.

---

## 10. Sonnet 001 Phase 8A

### Pre-refinement classification

Using only the center-2 persistent task state plus new center-3 contact events,
let

```text
A = forced_earlier
B = effective_unresolved_crossing
```

and define

```text
stable              = not A and not B
transport-only      = A and not B
completion-required = B.
```

### Implementation owner

```text
sonnet/lonely-runner/python/local_contact_refinement.py
    analyze_center2_to_center3
```

The classification is computed before center-3 child semantics are evaluated.
Only afterwards are affected parents locally refined as a red-team oracle.

### Executable essay

```text
tests/research/test_lonely_runner_canonical_observer_decomposition.py
```

Routine CI skips the heavy census but still parses/checks this essay through the
literate hygiene test.  The dedicated workflow is

```text
.github/workflows/sonnet-lonely-runner-canonical-decomposition.yml
```

### Acceptance target

```text
841 stable
2 transport-only, each one uniform changed witness
6 completion-required, each genuinely branching
26 old full systems reopened
298 center-3 children evaluated
75 final witness semantics recovered
```

### Status

**Implementation staged; dedicated exact gate must pass before the target is
promoted to a new Phase-8 result.**

---

## 11. Reference ledger

Full bibliographic entries live in the executable essays that use them.  Core
anchors for this branch are:

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed.,
  Springer, 2015; DOI 10.1007/978-3-319-13467-3.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer,
  1989; DOI 10.1007/978-1-4757-2063-1.
- J. F. Cariñena, G. Marmo, J. Nasarre, "The nonlinear superposition principle
  and the Wei-Norman method," arXiv:physics/9802041 (1998),
  https://arxiv.org/abs/physics/9802041 .
- Herbert Goldstein, Charles P. Poole Jr., John L. Safko, *Classical Mechanics*,
  3rd ed., Addison-Wesley, 2002, Chapter 3, ISBN 0-201-65702-3.
- NIST Digital Library of Mathematical Functions, §4.21,
  https://dlmf.nist.gov/4.21 .
- David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes,"
  *Proceedings of the IRE* 40(9) (1952), 1098--1101;
  DOI 10.1109/JRPROC.1952.273898.
- T. Sungkawichai, T. Trakulthongchai, "Eleven, twelve, and thirteen lonely
  runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

## 12. Review rule

Before merging or promoting any item in this ledger:

1. update the mathematical statement here if its semantics changed;
2. update the implementation owner and executable certificate in the same
   branch;
3. keep the essay Proof map synchronized with real test functions;
4. verify every classical/historical claim has a resolvable reference with a
   useful locator;
5. label Shakespeare interpretation separately from cited classical facts;
6. run routine CI plus any dedicated opt-in research gate required by the row;
7. update the row's epistemic status only after the relevant gate has passed.

A discrepancy is a blocked research artifact, not a documentation cleanup for
later.
