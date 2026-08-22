# Canonical-observer claim ledger

**Status:** auditable research ledger for `research/canonical-observer-api`; not a stable API specification.

## 1. Purpose

For this research line, mathematical prose, executable code, tests, benchmark
records, and bibliography are one artifact with several views. A change is
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
`tests/test_canonical_observer_essay_hygiene.py`. Heavy Sonnet censuses remain
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
by maintaining canonicalization. It carries provenance, base rates, observer
rates, and exact residuals.

**Positive certificates.**

```text
src/aeg_shakespeare/analysis/connection.py

tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

**Negative discrete certificate.** Sonnet 001 Phase 8B inspected two one-to-one
center-depth updates initially suspected of same-family transport. Both preserve
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

with a domain-specific certificate. The API records a split but does not
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
opposite coupled-scalar sign. Repository code/tests/docs use the executable
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
- **Sonnet 8E.0:** zero-collateral activation is too strict to explain the
  cross-parent sharing needed by the successful interleaved history.

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
each genuine `F_comp` parent. Exact conflict-cover dynamic programming returns a
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

Every selected wall is new at center 3. Four supports already equal their task
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

**Status.** **Exact bounded task-relative objectification passed.** No universal
`ResidualQuotient` API is inferred.

---

## 12. Sonnet 001 Phase 8D — persistent DAG increment

**Statement.** Reuse the frozen center-2 68-label persistent Hauffman tree
unchanged; attach Phase-8C.2 decoders only at six genuine completion leaves.
History reindexing adds zero wall queries. Merge equal final task terminals but
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

The local graft has `peak/worst = 75/12`; the separately frozen fresh center-3
time-first tree has the **same** `376/125` total/internal counts but `72/10`.

**Cost red team.** Historical current-task weights hit none of the eight
refinement-sensitive parents. Conditional on the 298 locally reopened children:

```text
288 completion children
 10 history-reindex children
544 new wall queries total
mean extra depth = 544/298 ≈ 1.8255 per reopened child
completion-only mean = 544/288 = 17/9 ≈ 1.8889
worst extra completion depth = 3.
```

**Exact gate:** run `32586254733`, Python 3.12.14; 8D essay `1 passed in 21.46 s`.

**Status.** **Exact bounded explicit persistent-DAG construction passed.** The
200-node DAG is a conservative construction, not a minimum-DAG theorem.

---

## 13. Sonnet 001 Phase 8D.2 — refinement-aware old-prefix placement

**Statement.** Freeze all local completion residuals and decoders; alter only the
old 21-wall prefix ordering using proposal weights

\[
w_\lambda=(1-\lambda)w_{\rm current}/55+\lambda w_{\rm refine}/288.
\]

**Owner / certificate / note.**

```text
sonnet/lonely-runner/python/refinement_aware_huffman.py

tests/research/test_lonely_runner_refinement_aware_huffman.py
sonnet/lonely-runner/25-phase8d2-refinement-aware-placement.md
```

**Exact sampled profiles include:**

```text
lambda=0:    current 135, completion 2933, nodes 376, peak/worst 75/12
lambda=1/16: current 136, completion 2146, nodes 376, peak/worst 93/9
lambda=1/4:  current 143, completion 2027, nodes 376, peak/worst 87/10
lambda=1/2:  current 163, completion 1739, nodes 376, peak/worst 90/9
lambda=1:    current 234, completion 1721, nodes 427, peak/worst 108/9.
```

After duplicate metric profiles are collapsed, all five sampled profiles are
Pareto-nondominated across current depth, refinement depth, updated volume, peak,
and worst depth. No sampled old-prefix-first candidate reaches both `peak<=72`
and `worst<=10`.

**Exact gate:** run `32586811587`, Python 3.12.14; essay `1 passed in 29.03 s`.

**Status.** **Exact bounded seven-mixture placement calibration passed.** It
establishes a genuine time/frontier tradeoff and localizes the remaining problem
to architecture rather than scalar weight tuning.

---

## 14. Sonnet 001 Phase 8E.0 — activation geometry

**Statement.** Relative to the frozen old persistent tree, a new completion wall
has a *clean activation* when at least one completion user survives and every
surviving non-user already has a fixed sign on that wall. Shared-clean requires
at least two surviving users.

**Owner / certificate / note.**

```text
sonnet/lonely-runner/python/activation_geometry.py

tests/research/test_lonely_runner_activation_geometry.py
sonnet/lonely-runner/26-phase8e0-activation-geometry.md
```

**Exact result.** The seven frozen new walls have sorted earliest clean depths

\[
\boxed{3,3,5,7,8,9,9}.
\]

No wall has any shared-clean activation in the frozen old tree. Even the two
walls used by four completion parents become clean only after a single actual
completion user remains.

**Exact gate:** run `32587582896`, Python 3.12.14; activation essay `1 passed in
36.33 s`.

**Status.** **Exact bounded activation-geometry calibration passed.** It proves
that zero-collateral activation is too strict to explain cross-parent sharing;
it does not prove interleaving impossible.

---

## 15. Sonnet 001 Phase 8E — controlled interleaving

**Statement.** Construct a joint decision representation from the 21 old
task-relevant wall signs plus **exactly seven** Phase-8C new completion-wall
signs. Feasible new-wall combinations are generated from center-2 exact
multiplicative constraints only. Stable parents keep their task, the two reindex
parents use their frozen updated task, and the six completion parents use only
the frozen Phase-8C.2 decoders.

**Owner / certificate / note.**

```text
sonnet/lonely-runner/python/controlled_interleaving.py

tests/research/test_lonely_runner_controlled_interleaving.py
sonnet/lonely-runner/27-phase8e-controlled-interleaving.md
```

**Joint representation:**

\[
\boxed{2,753\text{ feasible items},\qquad75\text{ final task semantics}.}
\]

No full 72,241-state center-3 arrangement or fresh center-3 tree topology is
used to construct the joint world.

**Current-usage-only exact tree (`lambda=0`):**

```text
current weighted depth total  135
completion-child depth total 2708
tree/boundary nodes           376
internal query nodes          125
terminal-merged DAG nodes     200
peak frontier                  72
worst depth                    10.
```

These match all frozen structural metrics of the independently constructed fresh
center-3 time-first tree used as the placement oracle, while preserving current
weighted depth `135`.

The decision inventory remains `109 old + 16 new = 125` internals. Four of the
16 new-wall nodes are cross-parent activations; earliest new-wall depth is five.
The seven first-activation depths are

\[
\boxed{5,6,7,7,8,8,9}.
\]

Thus the successful improvement changes partial order/sharing rather than the
number of completion decisions:

```text
completion discovers required decisions
controlled interleaving/reconvergence organizes them in history.
```

Small refinement mixtures move activation earlier and reduce completion-child
depth further, but increase peak frontier (`lambda=1/16` and `1/4` both give
current 136, completion 1972, `peak/worst=87/10`).

**Exact gate:** run `32587582896`, Python 3.12.14; controlled-interleaving essay
`1 passed in 152.67 s`.

**Status.** **Exact bounded controlled-interleaving calibration passed.** Matching
checked structural metrics does not establish tree isomorphism or universal
optimality.

---

## 16. New presentation/history pressure after Phase 8E

**Statement.** The bounded Sonnet loop distinguishes three independent roles:

```text
representation content:
    which process distinctions are required

semantic objectification:
    which raw distinctions are task-equivalent

history placement:
    when distinctions enter, which contexts share them, and where equivalent
    branches may reconverge.
```

The successful Phase-8E tree uses cross-parent new-wall activations even though
Phase 8E.0 proved there are no shared-clean activation points in the frozen old
tree. Therefore any reusable future role must permit **temporarily collateral
splitting with certified semantic reconvergence**.

A possible future abstraction is an activation/interleaving certificate, not a
full public `PersistentDAG` class. One Sonnet is insufficient for promotion.

**Status.** **Reusable semantic pressure identified; no new public API promoted.**

---

## 17. Cost-semantics pressure after Phase 8E

**Statement.** Current time, continuation/refinement time, and frontier-space
geometry must remain separate axes. A scalar current/refinement mixture is useful
for proposal generation but can improve time while making frontier width much
worse.

A continuing-process cost should preserve at least

```text
current history / expected depth
continuation / refinement work
frontier / boundary geometry
residual and decoder size.
```

**Status.** **Exact bounded pressure established; no new public cost field frozen
until an independent continuation calibration exists.**

---

## 18. Scaling gate — center 3 -> center 4

The center-2 -> center-3 loop is closed. The next Sonnet experiment must reuse
the frozen procedure without tuning its rules:

```text
persistent representation
    -> local affected-state detection from the next contact layer
    -> canonical decomposition
    -> minimum new process support
    -> task-relative residual objectification
    -> sparse persistent graft
    -> conditional refinement workload
    -> controlled interleaving using only newly certified walls
    -> fresh center-4 oracle comparison only after construction.
```

No center-2 -> center-3 counts, wall identities, or fitted thresholds may be
hard-coded as center-4 proposal heuristics. Only reusable process, exact
constraint, and declared-task rules are admissible.

Even a successful center-3 -> center-4 replay is not enough to promote
activation/reconvergence to public API; a second unrelated process calibration
must pressure the same retained semantics.

**Status.** **next scaling experiment / not yet established.**

---

## 19. Reference ledger

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

## 20. Review rule

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
