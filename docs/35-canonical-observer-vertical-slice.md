# Canonical observer vertical slice

**Status:** research-only API shaping; not part of the 0.0.2 compatibility contract.  
**Sonnet scaling status:** the bounded center-2 -> center-3 representation loop is closed through controlled interleaving; next pressure is center-3 -> center-4 replay without changing the rules.

## 1. Current causal order

The AEG Analysis / Shakespeare reconstruction is now best represented as

```text
process direction
    -> local canonicalization when needed
    -> observer connection only when the canonical observer actually moves
    -> canonical decomposition
    -> renormalize / transport / complete
    -> minimum process-generated completion support
    -> task-relative residual objectification
    -> persistent history placement
    -> controlled activation / semantic reconvergence when new predicates interleave.
```

The final three stages were forced by Sonnet 001 rather than imported from the smooth theory.  In particular:

- minimum raw completion can over-refine the declared task;
- local completion can discover the correct amount of decision structure while placing it poorly in history;
- controlled old/new predicate interleaving can improve placement without adding completion primitives.

The branch still contains only four reusable research roles:

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition.
```

No generic `Completion`, `ResidualQuotient`, `ActivationPolicy`, persistent-DAG, or Hauffman-action API has been promoted.

## 2. `ProcessDirection`

For a declared process frame `X_i`,

\[
\mathscr D=\sum_i u^iX_i.
\]

`ProcessDirection` acts on the assignment algebra and may be lowered to a one-generator `ProcessSystem`; an ordinary ODE is therefore an assignment shadow rather than process ontology.

Executable controls:

```text
tests/classical/test_am_process_direction.py
tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

A/M is a negative control: process motion alone does not imply observer transport.

## 3. `ConstraintCanonicalization`

The first implemented canonicalization backend uses exact local equations

\[
\Phi(z,g)=0.
\]

Differentiating them along declared base rates and solving uniquely for observer rates yields the current exact connection backend.

There is deliberately no generic `Canonicalization` protocol.  Restricted Kepler remains the red team against pretending that osculation, orthogonality, projection, or stationarity must share this exact-equation implementation contract.

## 4. `ObserverConnection`

`ObserverConnection` records actual observer motion required to maintain a local canonical representation.  Positive calibrations remain continuous:

- Restricted Riccati: root/separation parameters move inside an affine observer family;
- coupled scalar registers: relative scale moves while preserving the balancing condition.

It stores provenance, base rates, observer rates, and exact residuals.  It does not yet define principal-bundle structure, curvature, holonomy, composition, or numerical path ordering.

### Discrete red team

Sonnet 001 Phase 8B rejected a tempting false positive.  Two one-to-one center-depth updates preserve the same witness boundary and mode and only shift event rank by `+2`:

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval').
```

These are history/decoder reindexing, not observer motion.  Sonnet 001 currently provides **no discrete evidence for `ObserverConnection`**.

## 5. `CanonicalDecomposition`

The generic record stores

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp}
\]

plus evidence, without prescribing a universal decomposition algorithm.

It has survived four qualitatively different carriers:

| Calibration | Carrier | Exact calibrated split |
| --- | --- | --- |
| Restricted Riccati | Lie directions | affine tangent / no resonance / `Q` completion |
| coupled scalars | multivariable Lie directions | diagonal ruler / no resonance / cross completion |
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

The empty middle sector is part of the calibration.

## 6. Classical killer calibrations

### Restricted Riccati

`tests/classical/test_restricted_riccati_canonical_observer.py` begins with

\[
A=\partial_x,
\quad M=x\partial_x,
\quad Q=x^2\partial_x,
\]

restricts the observer to an affine root/separation family, derives observer motion from exact root constraints, and leaves `Q` as genuine completion.  Only afterwards does it identify

\[
[A,M]=A,
\qquad[A,Q]=2M,
\qquad[M,Q]=Q
\]

with the classical Riccati `sl(2)` realization [Carinena-Marmo-Nasarre-1998; Hall-2015].

### Coupled scalar registers

`tests/classical/test_coupled_scalar_canonical_observer.py` selects a relative ruler by

\[
b_{12}\rho^2-b_{21}=0
\]

and derives

\[
\frac{\dot\rho}{\rho}
=\frac12\left(
\frac{\dot b_{21}}{b_{21}}-
\frac{\dot b_{12}}{b_{12}}
\right).
\]

With repository convention `[X,Y]=X(Y)-Y(X)` and

\[
E_{12}=y\partial_x,
\qquad E_{21}=x\partial_y,
\]

the executable sign is

\[
\boxed{[E_{12},E_{21}]=M_2-M_1.}
\]

One line in the externally supplied AEG Analysis v0.2 note has the opposite sign; repository code/tests/docs retain the executable convention [Hall-2015].

### Restricted Kepler

`tests/classical/test_restricted_kepler_canonical_decomposition.py` uses

\[
\mathcal K_1=\operatorname{span}\{1,\cos\psi,\sin\psi\},
\qquad L_K=R^2+1
\]

and classifies exact `n=0`, `n=1`, `n=2` forcing sectors as renormalization, resonance/modulation, and function-module completion.  This calibrates `CanonicalDecomposition` across a non-Lie carrier without pretending that Kepler osculation is already implemented by `ConstraintCanonicalization` [Goldstein-Poole-Safko-2002; Arnold-1989; DLMF-4.21].

## 7. Sonnet 001: completion is a pipeline

Phases 8C and 8C.2 separate

```text
completion pressure
    != minimum raw process-generator support
    != minimum task representation.
```

For the six `F_comp` parents, exact conflict-cover search over new center-3 contact walls gives minimum raw support sizes

\[
\boxed{1,2,2,2,3,4}.
\]

Every selected primitive wall is new at center 3.  Four raw signatures already equal their task quotient.  Two over-refine:

\[
11\text{ raw classes}\to7\text{ task classes},
\qquad
13\text{ raw classes}\to3\text{ task classes}.
\]

Exact task-relative objectification closes both quotients.  In the `13 -> 3` case the raw support contains four walls while decoder worst depth is only three.

Executable essays:

```text
tests/research/test_lonely_runner_minimal_completion_residuals.py
tests/research/test_lonely_runner_residual_objectification.py
```

## 8. Persistent graft: amount of structure versus placement

Phase 8D keeps the frozen center-2 68-label persistent Hauffman tree unchanged and grafts the six objectified completion decoders only at genuine completion leaves.

Center 2:

```text
328 tree/boundary nodes
109 internal nodes
177 terminal-merged DAG nodes
peak/worst = 72/9.
```

Local center-3 graft:

```text
376 tree nodes
125 internal nodes
200 terminal-merged DAG nodes
peak/worst = 75/12.
```

Thus one contact layer adds `+48` tree nodes but only `+23` explicit DAG objects after semantic merging.

A separately frozen fresh center-3 time-first tree has the same `376/125` total/internal structure but `peak/worst = 72/10`.  This gives the bounded separation

```text
local completion/objectification -> how much decision structure is needed
history placement                -> where that structure sits.
```

## 9. Cost semantics: current usage is not continuation risk

The historical 55-input center-2 Hauffman distribution hits none of the eight refinement-sensitive parents.  Its zero incremental depth is a sampling blind spot, not evidence that refinement is free.

Conditional on the 298 locally reopened children, exact local decoders use

\[
544
\]

new wall queries:

\[
E[d_{\rm extra}\mid\text{reopened}]
=\frac{544}{298}\approx1.8255,
\]

\[
E[d_{\rm extra}\mid F_{\rm comp}]
=\frac{544}{288}=\frac{17}{9}\approx1.8889,
\]

with worst extra depth three.

Current usage and continuation/refinement workloads must therefore remain separate cost axes.

Phase 8D.2 then reweighted only the old 21-wall prefix.  Small refinement weight can improve refinement time and worst depth cheaply while badly enlarging frontier space; the sampled profiles are Pareto-nondominated.  No sampled old-prefix-first candidate reaches the fresh target `peak<=72`, `worst<=10`.

This makes the architecture, not scalar weighting, the bottleneck.

## 10. Activation geometry and controlled interleaving

### Clean activation red team

Relative to the frozen old tree, the seven new completion walls have earliest zero-collateral activation depths

\[
\boxed{3,3,5,7,8,9,9}.
\]

No wall has a shared clean activation: even walls used by four completion parents become clean only after a single actual user remains.  Cross-parent sharing therefore requires temporary collateral splitting plus semantic reconvergence.

Executable essay:

```text
tests/research/test_lonely_runner_activation_geometry.py
```

### Controlled interleaving

Instead of enumerating the full center-3 arrangement, exact center-2 constraints are refined only by the seven frozen new walls.  Together with the old 21 task-relevant wall signs this produces a 28-predicate joint representation with

\[
\boxed{2,753\text{ feasible items}}
\]

and exactly 75 final task semantics.

With the original current-usage weights only (`lambda=0`), exact search over all 28 predicates yields

```text
current weighted depth total  135
completion-child depth total 2708
tree/boundary nodes           376
internal query nodes          125
terminal-merged DAG nodes     200
peak frontier                  72
worst depth                    10.
```

These match all frozen structural metrics of the independently constructed fresh center-3 time-first tree used as the placement oracle, without supplying that tree or the full 72,241-state arrangement.

The decision inventory is unchanged:

```text
109 old-wall internal nodes
 16 new-wall internal nodes
---
125 total.
```

Four new-wall nodes are cross-parent activations.  The first new wall appears at depth five; the seven first-activation depths are

\[
\boxed{5,6,7,7,8,8,9}.
\]

Hence the placement improvement is a partial-order/sharing change, not more completion structure:

\[
\boxed{
\text{completion discovers the required decisions};
\quad
\text{controlled interleaving/reconvergence organizes them in history}.
}

Executable essay:

```text
tests/research/test_lonely_runner_controlled_interleaving.py
```

Exact certification run `32587582896`: activation essay `1 passed in 36.33 s`; controlled-interleaving essay `1 passed in 152.67 s`.

## 11. Negative controls now established

- A/M: process direction but no moving observer;
- Pendulum: task-relative scalar observable selection, not observer transport;
- two-frequency oscillator: coefficient refinement is not automatically `F_comp`;
- Galilean/magnetic cocycles: central history residual is not automatically a connection;
- Sonnet 8B: changed history index is not observer motion;
- Sonnet 8C: minimum raw support is not automatically a canonical primitive;
- Sonnet 8D: current-usage expected depth is not continuation risk;
- Sonnet 8E.0: zero-collateral activation is too strict for cross-parent sharing.

These failures and empty sectors are part of the API evidence.

## 12. Current API judgment

### Strongest candidates to retain

- `ProcessDirection`;
- evidence-bearing `CanonicalDecomposition`;
- provenance-generic `ObserverConnection` only where an observer actually moves.

### Provisional backend

- `ConstraintCanonicalization`.

### Explicitly not promoted yet

- generic `Canonicalization` protocol;
- discrete observer connection;
- universal `Completion` / `ResidualQuotient`;
- public activation/interleaving policy;
- persistent-DAG public object;
- stationary/cost canonicalization;
- observer bundle;
- generic process-jet object;
- curvature/holonomy;
- numerical observer ODE integration.

The new candidate semantic role suggested by Sonnet is smaller than a DAG class: an **activation/interleaving certificate** would retain when a process predicate may enter a history early and why collateral branches may safely reconverge.  One problem is insufficient for promotion.

## 13. Next scaling pressure

The center-2 -> center-3 representation loop is now closed.  Further center-3 tuning risks overfitting.

The next Sonnet experiment is center-3 -> center-4 replay with frozen rules:

```text
persistent state
    -> local affected-state detection
    -> canonical decomposition
    -> minimum new process support
    -> task-relative objectification
    -> sparse persistent graft
    -> conditional refinement workload
    -> controlled interleaving from only newly certified walls
    -> compare with fresh center-4 oracle only after construction.
```

No center-2 -> 3 counts, wall identities, or fitted thresholds may be used as proposal heuristics.  Only reusable process/constraint/task rules are allowed.

Even if that scaling replay succeeds, activation/reconvergence should not become public API until a second unrelated process problem pressures the same retained semantics.

## 14. Literate-programming / consistency gate

Every new substantial essay contains

```text
Question
Primitive data
Classical lineage
Shakespeare reconstruction
Calibration statement
Proof map
Boundary
References.
```

`tests/test_canonical_observer_essay_hygiene.py` checks required sections, citation-key resolution/locators, and Proof-map/test correspondence.  `docs/37-canonical-observer-claim-ledger.md` maps important claims to implementation owners, executable certificates, references, and epistemic status.

## 15. References

[Hall-2015] Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd ed., Graduate Texts in Mathematics 222, Springer, 2015; DOI 10.1007/978-3-319-13467-3.

[Carinena-Marmo-Nasarre-1998] J. F. Carinena, G. Marmo, J. Nasarre, "The nonlinear superposition principle and the Wei-Norman method," arXiv:physics/9802041 (1998), https://arxiv.org/abs/physics/9802041 .

[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989; DOI 10.1007/978-1-4757-2063-1.

[Goldstein-Poole-Safko-2002] Herbert Goldstein, Charles P. Poole Jr., John L. Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, Chapter 3, ISBN 0-201-65702-3.

[DLMF-4.21] NIST Digital Library of Mathematical Functions, §4.21, https://dlmf.nist.gov/4.21 .

[Karp-1972] Richard M. Karp, "Reducibility among Combinatorial Problems," in *Complexity of Computer Computations*, Plenum Press, 1972, pp. 85--103; DOI 10.1007/978-1-4684-2001-2_9.

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .
