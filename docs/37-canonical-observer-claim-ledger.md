# Canonical-observer claim ledger

**Status:** auditable research ledger for `research/canonical-observer-api`; not a stable API specification.

## 1. Purpose

For this research line, mathematical prose, executable code, test claims, and bibliography are one artifact with several views.  A change is incomplete if it updates only one view.

Each row records

```text
mathematical statement
    <-> implementation owner
    <-> executable certificate
    <-> cited lineage
    <-> epistemic status.
```

Routine CI checks the mechanically auditable subset through `tests/test_canonical_observer_essay_hygiene.py`; dedicated heavy workflows certify bounded censuses that should not run across the full Python matrix.

## 2. `ProcessDirection`

**Statement.** For a declared process frame `X_i`,

\[
\mathscr D=\sum_i u^iX_i.
\]

Assignment ODEs are shadows obtained by applying `D` to assignment symbols; `ProcessDirection` is not itself a path, solver, observer connection, or reparameterization quotient.

**Owner / certificates.**

```text
src/aeg_shakespeare/process/local/direction.py

tests/classical/test_am_process_direction.py
tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

**Lineage.** Hall 2015; Coddington--Levinson 1955 for affine/linear-ODE shadows.

**Status.** **Implemented/calibrated.**

---

## 3. `ConstraintCanonicalization`

**Statement.** The first implemented canonicalization backend uses exact local equations

\[
\Phi(z,g)=0
\]

and obtains observer rates by differentiating them along declared base rates and solving uniquely for `dot g`.

**Owner / certificates.**

```text
src/aeg_shakespeare/presentation/canonicalization.py

tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

There is deliberately no generic `Canonicalization` alias or base protocol.

**Status.** **Implemented backend, not universal definition.** Restricted Kepler remains the red team against forcing osculation/orthogonality into this exact-equation backend.

---

## 4. `ObserverConnection`

**Statement.** `ObserverConnection` records actual local observer motion induced by maintaining canonicalization.  It carries provenance, base rates, observer rates, and exact residuals.

**Owner / positive certificates.**

```text
src/aeg_shakespeare/analysis/connection.py

tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

**Negative discrete certificate.** Sonnet 001 Phase 8B inspected two one-to-one center-depth updates initially suspected of same-family transport.  Both preserve the exact witness boundary and mode and only shift event rank by `+2`; they are history/decoder reindexing, not observer motion.

```text
sonnet/lonely-runner/21-phase8b-history-reindex-red-team.md
workflow run 32584153291
```

**Status.** **Evidence-bearing transport record for continuous calibrations only.** Sonnet 001 currently supplies no discrete `ObserverConnection` evidence. Curvature, holonomy, composition, horizontal projection, and numerical path ordering remain unpromoted.

---

## 5. `CanonicalDecomposition`

**Statement.** The working result shape is

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp},
\]

with a domain-specific certificate.  The API records a split but does not prescribe a universal discovery algorithm.

**Owner.**

```text
src/aeg_shakespeare/analysis/decomposition.py
```

**Independent carrier calibrations.**

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

The earlier working map `841 / 2 / 6 -> renormalizable / resonant / completion` was rejected by Phase 8B and must not be cited as final.

**Status.** **Reusable result shape supported by four qualitatively different carriers.** Universal projection/decomposition or categorical unification remains open.

---

## 6. Riccati bracket/completion certificate

With repository convention

\[
[X,Y]=X(Y)-Y(X),
\]

and

\[
A=\partial_x,\quad M=x\partial_x,\quad Q=x^2\partial_x,
\]

\[
[A,M]=A,\qquad[A,Q]=2M,\qquad[M,Q]=Q.
\]

**Certificate:** `tests/classical/test_restricted_riccati_canonical_observer.py`.  
**Lineage:** Cariñena--Marmo--Nasarre 1998; Hall 2015.  
**Status:** **implemented exact classical-shadow certificate after restricted decomposition.**

---

## 7. Coupled-scalar sign audit

With

\[
E_{12}=y\partial_x,\qquad E_{21}=x\partial_y,
\]

repository code gives

\[
\boxed{[E_{12},E_{21}]=M_2-M_1.}
\]

**Owner/certificate:**

```text
src/aeg_shakespeare/process/local/frame.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

The externally supplied AEG Analysis v0.2 note contains one line with the opposite sign `M1-M2`.  Repository code/tests/docs consistently use the executable sign.  The external note should be corrected in its next revision; the `gl(2)`/`aff(2)` generation statement is unchanged.

**Status:** **known documentation discrepancy, localized and recorded.**

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

with

\[
L_K1=1,
\quad L_K\cos\psi=0,
\quad L_K\cos2\psi=-3\cos2\psi.
\]

**Certificate:** `tests/classical/test_restricted_kepler_canonical_decomposition.py`.  
**Lineage:** Goldstein--Poole--Safko 2002; Arnold 1989; NIST DLMF §4.21.  
**Status:** **bounded first-order function-module calibration, not a general perturbation theorem.**

---

## 9. Negative controls

- **A/M:** process direction is needed; observer connection is not.
- **Pendulum:** `pair(q,e)` is a task-relative scalar observable, not a dynamic observer state.
- **Two-frequency oscillator:** coefficient-field refinement is exact but not automatically `F_comp`; competing presentations remain Pareto-incomparable in the red-team profile.
- **Galilean / magnetic translations:** central cocycle residuals pressure future lift/holonomy concepts but are not by themselves observer connections.
- **Sonnet 001 Phase 8B:** changed event/history index with invariant witness boundary and mode is decoder renormalization, not observer transport.

**Status:** **implemented/audited boundaries.** These negative cases are part of the API evidence.

---

## 10. Sonnet 001 Phase 8A/8B

**Pre-refinement behavioral partition.** Using only old center-2 persistent state plus newly admitted center-3 events:

```text
A = forced_earlier
B = effective_unresolved_crossing

stable              = not A and not B
nonbranching_update = A and not B
completion_pressure = B
```

This yields `841 / 2 / 6` before center-3 child semantics are evaluated.

**Phase-8B witness audit.**

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval')
```

Both preserve boundary/mode and shift only event rank by `+2`.

**Corrected canonical sectors:** `843 renormalizable / 0 resonant / 6 completion`.

**Owner / essay / notes:**

```text
sonnet/lonely-runner/python/local_contact_refinement.py
    analyze_center2_to_center3

tests/research/test_lonely_runner_canonical_observer_decomposition.py

sonnet/lonely-runner/20-phase8a-discrete-canonical-decomposition.md
sonnet/lonely-runner/21-phase8b-history-reindex-red-team.md
```

**Exact gate:** run `32584153291`, Python 3.12.14, `1 passed in 7.95 s`; 26 old full systems reopened, 298 children evaluated, 75 semantics recovered.  Timing is provenance only.

**Status:** **exact bounded 8A/8B calibration passed.**

---

## 11. Sonnet 001 Phase 8C — minimum raw completion support

**Statement.** For each of the six genuine `F_comp` parents, search every varying center-3 pair/contact wall sign available in its local child geometry.  A selected signature must distinguish every pair of children with different task semantics.  Exact dynamic programming over the cross-task conflict cover gives minimum **raw wall cardinality**.

**Owner / certificate / note:**

```text
sonnet/lonely-runner/python/local_contact_refinement.py
    _minimum_task_separating_coordinates
    analyze_center2_to_center3

tests/research/test_lonely_runner_minimal_completion_residuals.py

sonnet/lonely-runner/22-phase8c-minimum-completion-residuals.md
```

**Exact result.** The six minimum wall counts are

```text
1, 2, 2, 2, 3, 4
```

and every selected wall is genuinely new at center 3.  The union of local selected supports contains seven distinct new contact walls.

Per-parent `(task semantics, wall count, residual classes)` profile:

```text
(3,1,3)
(3,4,13)
(5,2,5)
(5,2,5)
(5,2,5)
(7,3,11)
```

Thus four parents already obtain an exact task quotient in the minimum raw wall grammar, while two remain over-refined even at minimum wall cardinality.

**Exact gate:** run `32584599992`, Python 3.12.14; 8A/8B essay `1 passed in 8.04 s`, 8C essay `1 passed in 7.55 s`.  Timing is provenance only.

**Lineage:** Karp 1972 for set-cover background; Sungkawichai--Trakulthongchai 2026 for Lonely Runner; Huffman 1952 for later coding/depth optimization.

**Status:** **exact bounded minimum-raw-support calibration passed.** It does not yet establish minimum task representation; the two over-refined cases require residual quotient/objectification.

---

## 12. Next research row — residual objectification / Phase 8D bridge

Target the two over-refined parents:

```text
minimum raw wall support
    -> compound/task-relative residual quotient
    -> exact decoder
    -> cost against raw tuple and opaque persistent-ID baseline.
```

The four exact raw signatures may be frozen as provisional local completion primitives.

After all six residuals are objectified, build the persistent DAG and measure incremental Hauffman geometry.

**Status:** **planned / not yet established.**

---

## 13. Reference ledger

Full entries live in the executable essays. Core anchors:

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015; DOI 10.1007/978-3-319-13467-3.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989; DOI 10.1007/978-1-4757-2063-1.
- Earl A. Coddington, Norman Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955; linear differential equations begin p. 62; ISBN 978-0-07-099256-6.
- J. F. Cariñena, G. Marmo, J. Nasarre, "The nonlinear superposition principle and the Wei-Norman method," arXiv:physics/9802041 (1998), https://arxiv.org/abs/physics/9802041 .
- Herbert Goldstein, Charles P. Poole Jr., John L. Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, Chapter 3, ISBN 0-201-65702-3.
- NIST Digital Library of Mathematical Functions, §4.21, https://dlmf.nist.gov/4.21 .
- Richard M. Karp, "Reducibility among Combinatorial Problems," in *Complexity of Computer Computations*, 1972, pp. 85--103; DOI 10.1007/978-1-4684-2001-2_9.
- David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.
- Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .

Project-specific interpretations are labeled separately and must not be attributed to these sources.

## 14. Review rule

Before merging or promoting any row:

1. update the mathematical statement if semantics changed;
2. update implementation owner and executable certificate in the same branch;
3. keep Proof map synchronized with real test functions;
4. verify bibliographic claims and locators against authoritative records;
5. distinguish Shakespeare interpretation from cited classical facts;
6. run routine CI plus any required dedicated research gate;
7. change epistemic status only after those gates pass.

A discrepancy is a blocked research artifact, not documentation cleanup for later.
