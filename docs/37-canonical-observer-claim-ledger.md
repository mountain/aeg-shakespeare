# Canonical-observer claim ledger

**Status:** auditable research ledger for `research/canonical-observer-api`; not a stable API specification.

## 1. Purpose

For this research line, mathematical prose, executable code, test claims, and bibliography are one artifact with several views.  A change is incomplete if it updates only one view.

The ledger records

```text
mathematical statement
    <-> implementation owner
    <-> executable certificate
    <-> cited classical lineage
    <-> epistemic status.
```

Routine CI checks the mechanically auditable subset through `tests/test_canonical_observer_essay_hygiene.py`; dedicated heavy workflows certify bounded research censuses that should not run across the full Python matrix.

## 2. `ProcessDirection`

### Statement

For a declared process frame `X_i`,

\[
\mathscr D=\sum_i u^iX_i.
\]

Assignment ODEs are obtained by applying `D` to assignment symbols; `ProcessDirection` itself is not a path, solver, observer connection, or reparameterization quotient.

### Owner / certificates

```text
src/aeg_shakespeare/process/local/direction.py

tests/classical/test_am_process_direction.py
tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

### Lineage

Hall 2015; Coddington--Levinson 1955 for the classical affine/linear-ODE shadows.

### Status

**Implemented/calibrated.**

---

## 3. `ConstraintCanonicalization`

### Statement

The first implemented canonicalization backend uses exact local equations

\[
\Phi(z,g)=0,
\]

and obtains observer rates by differentiating them along declared base rates and solving uniquely for `dot g`.

### Owner / certificates

```text
src/aeg_shakespeare/presentation/canonicalization.py

tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

There is deliberately no generic `Canonicalization` alias or base protocol.

### Status

**Implemented backend, not universal definition.**  Restricted Kepler remains the explicit red team against pretending that osculation/orthogonality must share this exact-equation backend.

---

## 4. `ObserverConnection`

### Statement

`ObserverConnection` records local observer motion induced by maintaining canonicalization.  It carries canonicalization provenance, base rates, observer rates, and exact residuals.

### Owner / positive certificates

```text
src/aeg_shakespeare/analysis/connection.py

tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

### Negative discrete certificate

Sonnet 001 Phase 8B inspected the two center-depth updates initially suspected of being same-family transport.  Both retain exactly the same witness boundary and mode and only shift the event rank by `+2`.  They are history/decoder reindexing, not observer motion.

```text
sonnet/lonely-runner/21-phase8b-history-reindex-red-team.md
workflow run 32584153291
```

### Status

**Evidence-bearing local transport record for continuous calibrations only.**  Sonnet 001 currently provides no discrete `ObserverConnection` evidence.  Curvature, holonomy, composition, horizontal projection, and numerical path-ordered transport remain unpromoted.

---

## 5. `CanonicalDecomposition`

### Statement

The working result shape is

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp},
\]

with a caller/domain-specific certificate.  The API records the split but does not prescribe a universal discovery algorithm.

### Owner

```text
src/aeg_shakespeare/analysis/decomposition.py
```

### Independent carrier calibrations

| Calibration | Carrier | Exact calibrated split |
| --- | --- | --- |
| Restricted Riccati | Lie directions | affine tangent / empty resonant sector / `Q` completion |
| coupled scalar registers | multivariable Lie directions | diagonal ruler / empty resonant sector / cross completion |
| Restricted Kepler | finite function module | `n=0 / n=1 / n=2` |
| Sonnet 001 Phase 8A/8B | persistent finite task states | `843 / 0 / 6` |

For Sonnet 001:

\[
\boxed{
843\;F_{\rm ren}
=841\text{ identity-stable}+2\text{ history reindex},
\quad0\;F_{\rm res},
\quad6\;F_{\rm comp}.
}
\]

The earlier working map `841 / 2 / 6 -> renormalizable / resonant / completion` was explicitly rejected by Phase 8B and must not be cited as the final canonical decomposition.

### Status

**Reusable result shape supported by four qualitatively different carriers.**  Universal projection/decomposition or categorical unification remains open.

---

## 6. Riccati completion

With repository convention

\[
[X,Y]=X(Y)-Y(X),
\]

and

\[
A=\partial_x,
\quad M=x\partial_x,
\quad Q=x^2\partial_x,
\]

the executable bracket table is

\[
[A,M]=A,
\qquad[A,Q]=2M,
\qquad[M,Q]=Q.
\]

Certificate:

```text
tests/classical/test_restricted_riccati_canonical_observer.py
```

Lineage: Cariñena--Marmo--Nasarre 1998; Hall 2015.

Status: **implemented exact classical-shadow certificate after restricted decomposition.**

---

## 7. Coupled-scalar sign audit

With

\[
E_{12}=y\partial_x,
\qquad E_{21}=x\partial_y,
\]

and the repository commutator convention,

\[
\boxed{[E_{12},E_{21}]=M_2-M_1.}
\]

Owner/certificate:

```text
src/aeg_shakespeare/process/local/frame.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

The externally supplied AEG Analysis v0.2 note contains one line with the opposite sign `M1-M2`.  Repository code/tests/docs consistently use the executable sign.  The external note should be corrected in its next revision; the `gl(2)`/`aff(2)` generation statement is unchanged.

Status: **known documentation discrepancy, localized and recorded.**

---

## 8. Restricted Kepler three-sector calibration

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

and

\[
L_K1=1,
\quad L_K\cos\psi=0,
\quad L_K\cos2\psi=-3\cos2\psi.
\]

Executable certificate:

```text
tests/classical/test_restricted_kepler_canonical_decomposition.py
```

Lineage: Goldstein--Poole--Safko 2002; Arnold 1989; NIST DLMF §4.21.

Status: **bounded first-order function-module calibration, not a general perturbation theorem.**

---

## 9. Negative controls

- **A/M:** `ProcessDirection` is needed; `ObserverConnection` is not.
- **Pendulum:** `pair(q,e)` is a task-relative scalar observable, not a dynamic observer state.
- **Two-frequency oscillator:** coefficient-field refinement is exact but not automatically `F_comp`; the real/extended presentations remain Pareto-incomparable in the red-team profile.
- **Galilean / magnetic translations:** central cocycle residuals pressure future lift/holonomy concepts but are not by themselves observer connections.
- **Sonnet 001 Phase 8B:** a changed event/history index with invariant witness boundary and mode is decoder renormalization, not observer transport.

Status: **implemented/audited boundaries; these negative cases are part of the API evidence.**

---

## 10. Sonnet 001 Phase 8A/8B

### Pre-refinement behavioral partition

Using only old center-2 persistent state plus newly admitted center-3 events:

```text
A = forced_earlier
B = effective_unresolved_crossing

stable              = not A and not B
nonbranching_update = A and not B
completion_pressure = B
```

This yields exactly

```text
841 / 2 / 6
```

before center-3 child semantics are evaluated.

### Phase-8B witness audit

The two nonbranching cases are

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval')
```

so both preserve boundary and mode and change only event rank by `+2`.

### Corrected canonical sectors

```text
843 renormalizable
  0 resonant / observer transport
  6 completion
```

### Owner / essay / notes

```text
sonnet/lonely-runner/python/local_contact_refinement.py
    analyze_center2_to_center3

tests/research/test_lonely_runner_canonical_observer_decomposition.py

sonnet/lonely-runner/20-phase8a-discrete-canonical-decomposition.md
sonnet/lonely-runner/21-phase8b-history-reindex-red-team.md
```

### Exact gate

```text
workflow: .github/workflows/sonnet-lonely-runner-canonical-decomposition.yml
run id:   32584153291
Python:   3.12.14
result:   1 passed in 7.95 s
```

The same run verifies:

```text
26 old full systems reopened
298 center-3 children evaluated
75 final witness semantics recovered.
```

Timing is provenance only.

### Status

**Exact bounded 8A/8B calibration passed.**  It supports the renormalizable/completion distinction and explicitly rejects the proposed discrete transport interpretation for the two nonbranching states.

---

## 11. Next research row — Phase 8C

Target: make the six `F_comp` states constructive.

Required result:

```text
completion parent
    -> minimal new contact/sign residual signature
    -> exact pair-difference closure
    -> exact child-task reconstruction
    -> cost comparison with opaque persistent-ID baseline.
```

Status: **planned / not yet established.**

---

## 12. Reference ledger

Full entries live in the executable essays.  Core anchors:

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015; DOI 10.1007/978-3-319-13467-3.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989; DOI 10.1007/978-1-4757-2063-1.
- Earl A. Coddington, Norman Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955; linear differential equations begin p. 62; ISBN 978-0-07-099256-6.
- J. F. Cariñena, G. Marmo, J. Nasarre, "The nonlinear superposition principle and the Wei-Norman method," arXiv:physics/9802041 (1998), https://arxiv.org/abs/physics/9802041 .
- Herbert Goldstein, Charles P. Poole Jr., John L. Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, Chapter 3, ISBN 0-201-65702-3.
- NIST Digital Library of Mathematical Functions, §4.21, https://dlmf.nist.gov/4.21 .
- David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.
- Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

Project-specific interpretations are labeled separately in the essays and must not be attributed to these references.

## 13. Review rule

Before merging or promoting any row:

1. update this mathematical statement if semantics changed;
2. update implementation owner and executable certificate in the same branch;
3. keep Proof map synchronized with real test functions;
4. verify bibliographic claims and locators against authoritative records;
5. distinguish Shakespeare interpretation from cited classical facts;
6. run routine CI plus any required dedicated research gate;
7. change epistemic status only after those gates pass.

A discrepancy is a blocked research artifact, not documentation cleanup for later.
