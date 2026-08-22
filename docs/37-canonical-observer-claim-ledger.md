# Canonical-observer claim ledger

**Status:** auditable research ledger for `research/canonical-observer-api`; not a stable API specification.

## 1. Purpose

For this research line, mathematical prose, executable code, tests, benchmark
records, and bibliography are one artifact with several views.  A change is
incomplete if it updates only one view.

Each row records

```text
mathematical statement
    <-> implementation owner
    <-> executable certificate
    <-> cited lineage
    <-> epistemic status.
```

Routine CI checks the mechanically auditable subset through
`tests/test_canonical_observer_essay_hygiene.py`.  Heavy Sonnet censuses remain
manual workflow gates and are cited by run id when their status is promoted.

## 2. `ProcessDirection`

**Statement.** For a declared process frame `X_i`,

\[
\mathscr D=\sum_i u^iX_i.
\]

Assignment ODEs are shadows obtained by applying `D` to assignment symbols;
`ProcessDirection` is not itself a path, solver, observer connection, or
reparameterization quotient.

**Owner / certificates.**

```text
src/aeg_shakespeare/process/local/direction.py

tests/classical/test_am_process_direction.py
tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

**Status.** **Implemented/calibrated.**

---

## 3. `ConstraintCanonicalization`

**Statement.** The first implemented canonicalization backend uses exact local
equations

\[
\Phi(z,g)=0
\]

and obtains observer rates by differentiating them along declared base rates and
solving uniquely for `dot g`.

**Owner / certificates.**

```text
src/aeg_shakespeare/presentation/canonicalization.py

tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

There is deliberately no generic `Canonicalization` alias or base protocol.

**Status.** **Implemented backend, not universal definition.** Restricted Kepler
remains the red team against forcing osculation/orthogonality into this backend.

---

## 4. `ObserverConnection`

**Statement.** `ObserverConnection` records actual local observer motion induced
by maintaining canonicalization.  It carries provenance, base rates, observer
rates, and exact residuals.

**Positive certificates.**

```text
src/aeg_shakespeare/analysis/connection.py

tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

**Negative discrete certificate.** Sonnet 001 Phase 8B inspected two one-to-one
center-depth updates initially suspected of same-family transport.  Both preserve
the exact witness boundary and mode and only shift event rank by `+2`.

```text
sonnet/lonely-runner/21-phase8b-history-reindex-red-team.md
workflow run 32584153291
```

**Status.** **Evidence-bearing transport record for continuous calibrations
only.** Sonnet 001 currently supplies no discrete `ObserverConnection` evidence.
Curvature, holonomy, composition, horizontal projection, and numerical path
ordering remain unpromoted.

---

## 5. `CanonicalDecomposition`

**Statement.** The reusable result shape is

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp},
\]

with a domain-specific certificate.  The API records a split but does not
prescribe a universal discovery algorithm.

**Owner.**

```text
src/aeg_shakespeare/analysis/decomposition.py
```

**Independent carriers.**

| Calibration | Carrier | Exact calibrated split |
| --- | --- | --- |
| Restricted Riccati | Lie directions | affine tangent / no resonance / `Q` completion |
| coupled scalar registers | multivariable Lie directions | diagonal ruler / no resonance / cross completion |
| Restricted Kepler | finite function module | `n=0 / n=1 / n=2` |
| Sonnet 001 | persistent finite task states | `843 / 0 / 6` |

For Sonnet 001:

\[
\boxed{
843F_{\rm ren}
=841\text{ identity-stable}+2\text{ history reindex},
\quad0F_{\rm res},
\quad6F_{\rm comp}.
}
\]

The earlier working map `841 / 2 / 6 -> renormalizable / resonant / completion`
was rejected by Phase 8B and must not be cited as final.

**Status.** **Reusable result shape supported by four qualitatively different
carriers.** Universal projection/decomposition remains open.

---

## 6. Riccati and coupled-scalar sign certificates

Repository commutator convention:

\[
[X,Y]=X(Y)-Y(X).
\]

For Riccati

\[
A=\partial_x,\quad M=x\partial_x,\quad Q=x^2\partial_x,
\]

\[
[A,M]=A,\qquad[A,Q]=2M,\qquad[M,Q]=Q.
\]

For coupled scalars

\[
E_{12}=y\partial_x,\qquad E_{21}=x\partial_y,
\]

\[
\boxed{[E_{12},E_{21}]=M_2-M_1.}
\]

**Certificates.**

```text
tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

The externally supplied AEG Analysis v0.2 note contains one line with the
opposite coupled-scalar sign.  Repository code/tests/docs use the executable
convention; the `gl(2)`/`aff(2)` structural conclusion is unchanged.

**Status.** **Implemented exact certificates; one external-note discrepancy
localized and recorded.**

---

## 7. Restricted Kepler three-sector calibration

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
**Status:** **bounded first-order function-module calibration, not a general
perturbation theorem.**

---

## 8. Negative controls

- **A/M:** process direction is needed; observer connection is not.
- **Pendulum:** `pair(q,e)` is a task-relative scalar observable, not a dynamic
  observer state.
- **Two-frequency oscillator:** coefficient-field refinement is exact but not
  automatically `F_comp`.
- **Galilean / magnetic translations:** central cocycle residuals pressure future
  lift/holonomy concepts but are not by themselves observer connections.
- **Sonnet 8B:** changed event/history index with invariant witness geometry is
  decoder renormalization, not observer transport.
- **Sonnet 8C:** minimum raw generator support is not automatically minimum task
  representation.
- **Sonnet 8D:** current-usage expected depth is not automatically refinement
  risk.

**Status.** **Implemented/audited boundaries.** These negative cases are part of
the API evidence.

---

## 9. Sonnet 001 Phase 8A/8B

**Behavioral partition before child semantics:**

```text
stable              841
nonbranching update   2
completion pressure   6.
```

Phase 8B witness audit:

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval').
```

Corrected canonical sectors: `843 / 0 / 6`.

**Owner / essay / notes.**

```text
sonnet/lonely-runner/python/local_contact_refinement.py
    analyze_center2_to_center3

tests/research/test_lonely_runner_canonical_observer_decomposition.py

sonnet/lonely-runner/20-phase8a-discrete-canonical-decomposition.md
sonnet/lonely-runner/21-phase8b-history-reindex-red-team.md
```

**Exact gate:** run `32584153291`, Python 3.12.14; 26 old full systems reopened,
298 children evaluated, 75 semantics recovered.

**Status.** **Exact bounded calibration passed.**

---

## 10. Sonnet 001 Phase 8C — minimum raw completion support

**Statement.** Search all varying center-3 process-generated wall signs below
each genuine `F_comp` parent.  Exact conflict-cover dynamic programming returns a
minimum-cardinality raw task-separating support.

**Owner / certificate / note.**

```text
sonnet/lonely-runner/python/local_contact_refinement.py
    _minimum_task_separating_coordinates

tests/research/test_lonely_runner_minimal_completion_residuals.py
sonnet/lonely-runner/22-phase8c-minimum-completion-residuals.md
```

**Result.** Minimum wall counts:

```text
1, 2, 2, 2, 3, 4.
```

Every selected wall is new at center 3.  Four supports already equal their task
quotient; two are over-refined:

```text
11 raw classes -> 7 tasks
13 raw classes -> 3 tasks.
```

**Exact gate:** run `32584599992`; 8C essay `1 passed in 7.55 s`.

**Status.** **Exact bounded minimum-raw-support calibration passed.**

---

## 11. Sonnet 001 Phase 8C.2 — residual objectification

**Statement.** Quotient each minimum raw sign language by exact first-witness
semantics and construct an exact adaptive decoder using only the selected
completion walls.

**Owner / certificate / note.**

```text
sonnet/lonely-runner/python/residual_objectification.py

tests/research/test_lonely_runner_residual_objectification.py
sonnet/lonely-runner/23-phase8c2-residual-objectification.md
```

**Strict quotient results:**

\[
\boxed{11\to7},
\qquad
\boxed{13\to3}.
\]

The `13 -> 3` support has four raw walls but adaptive decoder worst depth three;
its explicit decoder has six internal nodes and three shared semantic terminals.

**Exact gate:** run `32585634379`; 8C.2 essay `1 passed in 13.92 s`.

**Status.** **Exact bounded task-relative objectification passed.**  No universal
`ResidualQuotient` API is inferred.

---

## 12. Sonnet 001 Phase 8D — persistent DAG increment

**Statement.** Reuse the frozen center-2 68-label persistent Hauffman tree
unchanged; attach Phase-8C.2 decoders only at six genuine completion leaves.
History reindexing adds zero wall queries.  Merge equal final task terminals but
assume no cross-parent sharing of internal decoder nodes.

**Owner / certificate / note.**

```text
sonnet/lonely-runner/python/persistent_dag_increment.py

tests/research/test_lonely_runner_persistent_dag_increment.py
sonnet/lonely-runner/24-phase8d-persistent-dag-increment.md
```

**Exact structure:**

```text
center 2: 328 tree nodes / 109 internals / 177 terminal-merged DAG nodes
center 3: 376 tree nodes / 125 internals / 200 terminal-merged DAG nodes
increment: +48 tree nodes / +23 DAG nodes.
```

Updated width profile:

```text
1,3,3,9,27,48,63,72,75,39,18,15,3
```

so persistent graft `peak/worst = 75/12`.

The separately frozen fresh center-3 time-first tree has the **same** `376/125`
total/internal counts but `peak/worst = 72/10`.  This supports the bounded
separation:

```text
local completion/objectification -> amount of decision structure
global Hauffman placement        -> history location of that structure.
```

**Cost red team.** The historical 55-input current-task distribution hits none
of the eight refinement-sensitive parents, so its zero incremental depth is a
blind control.  Conditional on the 298 locally reopened children:

```text
288 completion children
 10 history-reindex children
544 new wall queries total
mean extra depth = 544/298 ≈ 1.8255 per reopened child
completion-only mean = 544/288 = 17/9 ≈ 1.8889
worst extra completion depth = 3.
```

**Exact gate:** run `32586254733`, Python 3.12.14; 8D essay `1 passed in 21.46 s`.

**Status.** **Exact bounded explicit persistent-DAG construction passed.**  The
200-node DAG is a conservative construction, not a minimum-DAG theorem.

---

## 13. Cost-semantics pressure after Phase 8D

**Statement.** Current usage weights and future refinement/continuation weights
must be represented separately.  In this calibration the former are provably
blind to all refinement-sensitive states.

A continuing-process cost must preserve at least distinct axes for

```text
current history / expected depth
frontier / boundary geometry
residual and decoder size
refinement / continuation work.
```

Do not collapse these into a scalar until an independent calibration justifies
the weighting.

**Status.** **API pressure established by exact negative/positive cost probes;
no new public cost field frozen yet.**

---

## 14. Next research row — refinement-aware Hauffman placement

Freeze the six completion residuals and decoders.  Search only over admissible
global wall placement/query order under separate current-usage and refinement
objectives.

Primary bounded target:

```text
persistent graft    peak/worst = 75/12
fresh center-3 tree peak/worst = 72/10
```

Determine whether global reordering can recover the better placement while
preserving the local incremental representation semantics, without returning to
full completion discovery.

Only afterwards should center-3 -> center-4 persistence be used as the next
scaling pressure.

**Status.** **planned / not yet established.**

---

## 15. Reference ledger

Full entries live in the executable essays. Core anchors:

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
- Richard M. Karp, "Reducibility among Combinatorial Problems," in *Complexity
  of Computer Computations*, 1972, pp. 85--103; DOI
  10.1007/978-1-4684-2001-2_9.
- David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes,"
  *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI
  10.1109/JRPROC.1952.273898.
- Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen
  lonely runners," arXiv:2604.23906 (2026),
  https://arxiv.org/abs/2604.23906 .

Project-specific interpretations are labeled separately and must not be
attributed to these sources.

## 16. Review rule

Before merging or promoting any row:

1. update the mathematical statement if semantics changed;
2. update implementation owner and executable certificate in the same branch;
3. keep Proof map synchronized with real test functions;
4. verify bibliographic claims and locators against authoritative records;
5. distinguish Shakespeare interpretation from cited classical facts;
6. run routine CI plus any required manual research gate;
7. change epistemic status only after those gates pass.

A discrepancy is a blocked research artifact, not documentation cleanup for
later.
