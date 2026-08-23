# Canonical-observer claim ledger

**Status:** auditable research ledger for `research/canonical-observer-api`; not a stable API specification.  
**Sonnet contact-depth status:** closed through a finite certificate for the entire infinite remaining first-witness contact alphabet.

## 1. Purpose

For this research line,

```text
mathematical statement
<-> implementation owner
<-> executable certificate
<-> cited lineage
<-> epistemic status
```

must remain synchronized.  Routine CI checks the mechanically auditable subset through `tests/test_canonical_observer_essay_hygiene.py`; heavy exact Sonnet experiments remain manual workflows after one auditable run.

---

## 2. `ProcessDirection`

**Statement.** For a declared process frame `X_i`,

\[
\mathscr D=\sum_i u^iX_i.
\]

Assignment ODEs are shadows of this local process direction; `ProcessDirection` is not itself a path, solver, observer connection, or reparameterization quotient.

**Owner / certificates.**

```text
src/aeg_shakespeare/process/local/direction.py

tests/classical/test_am_process_direction.py
tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

**Status:** **implemented/calibrated.**

---

## 3. `ConstraintCanonicalization`

**Statement.** The first backend uses exact local equations

\[
\Phi(z,g)=0
\]

and obtains observer rates by differentiating along declared base rates and solving uniquely for `dot g`.

**Owner / certificates.**

```text
src/aeg_shakespeare/presentation/canonicalization.py

tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

There is deliberately no generic `Canonicalization` protocol.

**Status:** **implemented backend, not universal definition.** Restricted Kepler is the red team against forcing osculation/orthogonality into this backend.

---

## 4. `ObserverConnection`

**Statement.** `ObserverConnection` records actual local observer motion required to preserve canonicalization.  It carries provenance, base rates, observer rates, and exact residuals.

**Positive certificates.**

```text
src/aeg_shakespeare/analysis/connection.py

tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

**Discrete negative certificate.** Sonnet 001 produces history/decoder reindexing at both center-2 -> 3 and center-3 -> 4: witness boundary/mode are fixed and only event rank shifts by `+2`.

**Status:** **continuous evidence-bearing transport record only.** Sonnet supplies no discrete observer-motion evidence. Curvature, holonomy, composition, horizontal projection, and numerical observer ODE integration remain unpromoted.

---

## 5. `CanonicalDecomposition`

**Statement.** The reusable result shape is

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp},
\]

with domain-specific evidence and no universal discovery algorithm.

**Owner:** `src/aeg_shakespeare/analysis/decomposition.py`.

**Carrier calibrations.**

| Calibration | Carrier | Exact split |
| --- | --- | --- |
| restricted Riccati | Lie directions | affine tangent / empty resonance / `Q` completion |
| coupled scalar registers | multivariable Lie directions | diagonal ruler / empty resonance / cross completion |
| restricted Kepler | finite function module | `n=0 / n=1 / n=2` |
| Sonnet center 2 -> 3 | persistent finite task states | `843 / 0 / 6` |
| Sonnet center 3 -> 4 | persistent constraint/task cells | `2746 / 0 / 7` |

**Status:** **reusable result shape supported across several carriers.** Universal projection/decomposition remains open.

---

## 6. Classical sign / completion certificates

Repository convention:

\[
[X,Y]=X(Y)-Y(X).
\]

Riccati:

\[
A=\partial_x,\quad M=x\partial_x,\quad Q=x^2\partial_x,
\]

\[
[A,M]=A,\quad[A,Q]=2M,\quad[M,Q]=Q.
\]

Coupled scalars:

\[
E_{12}=y\partial_x,\quad E_{21}=x\partial_y,
\]

\[
[E_{12},E_{21}]=M_2-M_1.
\]

The opposite-sign line in the external AEG Analysis v0.2 note is a localized documentation discrepancy; repository code/tests/docs use the executable convention.

**Status:** **implemented exact classical-shadow certificates.**

---

## 7. Sonnet Phase 8A/B — first canonical split

**Behavioral detector before child semantics:**

```text
841 stable
2 nonbranching pressure
6 completion pressure.
```

Phase 8B shows both nonbranching cases preserve witness boundary/mode and shift rank by `+2`.

**Correct split:**

\[
\boxed{843F_{\rm ren}\oplus0F_{\rm res}\oplus6F_{\rm comp}.}
\]

**Owners/certificates.**

```text
sonnet/lonely-runner/python/local_contact_refinement.py
tests/research/test_lonely_runner_canonical_observer_decomposition.py
sonnet/lonely-runner/20-phase8a-discrete-canonical-decomposition.md
sonnet/lonely-runner/21-phase8b-history-reindex-red-team.md
```

**Status:** **exact bounded calibration passed; no discrete ObserverConnection.**

---

## 8. Sonnet Phase 8C/C.2 — completion is a pipeline

Minimum raw center-3 wall supports:

\[
1,2,2,2,3,4.
\]

All selected walls are new at center 3.  Four raw supports equal their task quotient; two require task-relative objectification:

\[
11\to7,
\qquad13\to3.
\]

**Owners/certificates.**

```text
sonnet/lonely-runner/python/local_contact_refinement.py
sonnet/lonely-runner/python/residual_objectification.py

tests/research/test_lonely_runner_minimal_completion_residuals.py
tests/research/test_lonely_runner_residual_objectification.py
```

**Status:** **exact bounded minimum-support/objectification calibration passed.** No universal `Completion` or `ResidualQuotient` API.

---

## 9. Sonnet Phase 8D/D.2 — persistent geometry and cost axes

Local center-3 graft:

```text
center 2  328 tree / 109 internal / 177 DAG
center 3  376 tree / 125 internal / 200 DAG
peak/worst local graft 75/12.
```

A fresh center-3 tree has the same `376/125` inventory but `72/10`, separating decision content from placement.

Historical 55-input usage is blind to all eight refinement-sensitive states.  Conditional on 298 reopened children, exact extra-wall work is

\[
544/298\approx1.8255
\]

per reopened child; completion-only `544/288=17/9`, worst extra depth three.

Old-prefix refinement weighting exposes a Pareto tradeoff between current depth, future depth, volume, peak frontier, and worst depth.  No sampled old-prefix-first representation reaches both fresh `peak<=72` and `worst<=10`.

**Status:** **exact bounded geometry/cost red team passed.** Current-use cost and future-refinement cost are distinct axes; no scalar future cost frozen.

---

## 10. Sonnet Phase 8E — activation and controlled interleaving

Clean activation depths for the seven center-3 completion walls:

\[
3,3,5,7,8,9,9.
\]

No wall has shared clean activation.  Cross-parent sharing therefore needs temporary collateral splitting followed by semantic reconvergence.

Controlled interleaving uses only

```text
21 old walls + 7 generated center-3 walls
```

and exact center-2 constraints to construct 2,753 feasible joint items / 75 tasks.  Exact 28-predicate search recovers

```text
weighted depth 135
376 tree / 125 internal / 200 DAG
peak/worst 72/10.
```

Four new-wall nodes are genuine cross-parent activations.

**Owners/certificates.**

```text
sonnet/lonely-runner/python/activation_geometry.py
sonnet/lonely-runner/python/controlled_interleaving.py

tests/research/test_lonely_runner_activation_geometry.py
tests/research/test_lonely_runner_controlled_interleaving.py
```

**Status:** **exact bounded activation/interleaving calibration passed.** One process problem is insufficient to promote public activation/reconvergence API.

---

## 11. Sonnet Phase 9A — frozen-rule center-4 scaling

The 28-predicate center-3 state materializes as

\[
2753\text{ cells},\quad75\text{ tasks},\quad13609\text{ exact closure atoms}.
\]

The generic detector first replays the exact Phase-8 `841/2/6` sets, then unchanged gives center-4 pressure

\[
\boxed{2744\text{ stable}+2\text{ nonbranching}+7\text{ completion}.}
\]

Only `9/2753≈0.327%` of current cells reopen.

**Owner/certificate:**

```text
sonnet/lonely-runner/python/persistent_constraint_cells.py
tests/research/test_lonely_runner_center4_constraint_cells.py
```

**Status:** **exact frozen-rule scaling calibration passed.** `ConstraintCell` remains research-local.

---

## 12. Sonnet Phase 9B — exact local semantics and stale-claim correction

The two nonbranching cells are history reindexing.  All seven completion cells genuinely branch and each has exactly three task semantics.

An earlier essay assertion `2,2,3,3,4,4,4` was stale and has been rejected.  An independent local full-stratum oracle agrees with the current lazy oracle on all nine pressure cells:

```text
2 cells -> 1 task each
7 cells -> 3 tasks each.
```

The lazy oracle touches latent older walls, but that touched set is an algorithm trace only.

**Owners/certificates.**

```text
sonnet/lonely-runner/python/center4_semantic_redteam.py
sonnet/lonely-runner/python/center4_local_full_oracle.py

tests/research/test_lonely_runner_center4_semantic_redteam.py
```

**Status:** **exact semantic red team passed; stale multiplicity claim corrected.**

---

## 13. Sonnet Phase 9C — minimum center-4 completion

Every one of the seven completion cells has minimum support size one, and all choose the same genuinely new ternary wall:

\[
\boxed{\frac{u_4}{u_3}\ ?\ \frac{19}{11}.}
\]

For each branching cell, signs `-1,0,+1` map one-to-one to its three tasks.  Every minimum support has `(new,latent)=(1,0)`.  One lazy grammar has two walls / nine raw classes, but minimization still returns the same one wall / three task classes.

Thus the latent older walls touched by Phase 9B are **solver/certificate trace**, not minimum representation necessity.

**Owner/certificate:**

```text
sonnet/lonely-runner/python/center4_minimal_completion.py
tests/research/test_lonely_runner_center4_minimal_completion.py
```

**Status:** **exact bounded minimum-support calibration passed.** Certificate provenance may be richer than task ontology.

---

## 14. Sonnet Phase 9D — center-4 persistent update

The discovered wall is appended globally to form a 29-predicate presentation.

```text
center 3
  cells/tasks               2753 / 75
  tree/internal/DAG          376 / 125 / 200
  peak/worst/weighted         72 / 10 / 135

center 4
  cells/tasks               3067 / 81
  closure atoms             14967
  tree/internal/DAG          391 / 130 / 211
  peak/worst/weighted         75 / 10 / 135.
```

Exact increment:

\[
\boxed{\Delta\text{internal}=5,\quad\Delta\text{DAG}=11,\quad\Delta\text{task}=6.}
\]

The new wall occurs at five internal nodes, two cross-parent; earliest activation depth six.

**Owner/certificate:**

```text
sonnet/lonely-runner/python/center4_persistent_update.py
tests/research/test_lonely_runner_center4_persistent_update.py
```

**Exact run:** `32615437445`.

**Status:** **exact bounded persistent scaling update passed.**

---

## 15. Sonnet Phase 10A/B — center 5 is a semantic no-op

Frozen center-4 -> 5 pressure:

\[
\boxed{3067\text{ stable}+0\text{ nonbranching}+0\text{ completion}.}
\]

Direct exact event/witness comparisons:

\[
14967\times8=119736.
\]

All 119,736 center-5 comparisons are strictly later; zero are earlier/equal or unresolved.

**Owners/certificate.**

```text
sonnet/lonely-runner/python/center5_pressure.py
sonnet/lonely-runner/python/center5_semantic_noop.py

tests/research/test_lonely_runner_infinite_contact_tail_closure.py
```

**Exact runs:** `32615622103`, `32615805013`.

**Status:** **exact center-5 no-op passed.**

---

## 16. Sonnet Phase 10C — infinite contact-tail closure

For each positive-speed runner, center-5 enter is the earliest event among every center `n>=5`:

\[
\alpha_{5,\mathrm{enter}}=5-\delta=\frac{24}{5},
\qquad
\alpha_{n,\mathrm{kind}}\ge\frac{24}{5}.
\]

The finite anchor certificate checks

\[
14967\times4=59868
\]

closure-atom/runner comparisons.  Every one is strictly later than the current first witness; zero are earlier/equal or unresolved.

Therefore

\[
\boxed{
\text{the finite 29-predicate center-4 presentation is sufficient for first-witness semantics over the entire infinite remaining contact alphabet.}
}
\]

**Owner/certificate:**

```text
sonnet/lonely-runner/python/infinite_contact_tail_closure.py
tests/research/test_lonely_runner_infinite_contact_tail_closure.py
sonnet/lonely-runner/28-phase9-10-center4-scaling-and-infinite-tail-closure.md
```

**Exact run:** `32615960292`.

**Status:** **exact model/task-specific infinite-tail closure passed.** Not a Lonely Runner theorem and not a universal finite-presentation theorem.

---

## 17. Negative controls / epistemic boundaries

- process motion is not observer motion;
- scalar observable selection is not dynamic observer state;
- history/event reindex is not observer transport;
- minimum raw completion is not minimum task representation;
- current-use depth is not future-refinement cost;
- zero-collateral activation is too strict for cross-parent sharing;
- solver/certificate wall queries are not minimum-representation necessities;
- exact closure provenance is a useful backend but not thereby public ontology;
- one discrete process does not justify a universal activation/reconvergence API;
- infinite-tail closure here is first-witness/task/model specific.

These negative results are first-class API evidence.

---

## 18. Current promotion judgment

### Retain

```text
ProcessDirection
ConstraintCanonicalization     # concrete backend
ObserverConnection             # actual observer motion only
CanonicalDecomposition         # backend-neutral result shape
```

### Do not promote yet

```text
generic Canonicalization
Completion
ResidualQuotient
ConstraintCell
PersistentDAG
Activation/Reconnection
scalarized future cost
discrete ObserverConnection
curvature/holonomy
numerical observer ODE integration.
```

The contact-depth Sonnet line is closed.  The next discrete API pressure should come from an unrelated process problem.  Separately, the observer-ODE programme should return to a calibration with a genuinely moving canonical frame.

`K=13` remains a frozen holdout.

---

## 19. Review rule

Before promoting any claim:

1. synchronize mathematical statement, implementation owner, executable certificate, and note;
2. run routine CI plus any required manual heavy gate;
3. distinguish construction inputs from post-construction oracles;
4. record negative/red-team results rather than rewriting history;
5. never convert a solver trace into ontology without a minimum/task-relative check;
6. require an independent problem before promoting Sonnet-specific activation/reconvergence semantics.

## 20. References

Full bibliographic entries live in the executable essays.  Core anchors include Hall 2015, Arnold 1989, Huffman 1952, and Sungkawichai–Trakulthongchai 2026.  Project-specific Shakespeare interpretations are labeled separately and are not attributed to those sources.
