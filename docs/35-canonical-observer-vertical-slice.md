# Canonical observer vertical slice

**Status:** research-only API shaping; not part of the 0.0.2 compatibility contract.

## 1. Current causal order

The AEG Analysis programme is now best represented as

```text
process direction
    -> local canonicalization when needed
    -> observer connection only when the canonical observer actually moves
    -> canonical decomposition
    -> renormalize / transport / complete
    -> minimum process-generated completion support
    -> task-relative residual objectification
    -> history/DAG placement under explicit cost semantics.
```

The last three lines are not theoretical ornament.  Sonnet 001 Phases 8C--8D forced them experimentally: a minimum raw completion can over-refine the task, and an objectified local completion can have the correct total amount of decision structure while still being globally poorly placed in history.

The branch still contains only four reusable research roles:

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition.
```

No generic `Completion`, `ResidualQuotient`, persistent-DAG, or Hauffman-action API has been promoted.

## 2. `ProcessDirection`

For an existing process frame `X_i`,

\[
\mathscr D=\sum_i u^iX_i.
\]

`ProcessDirection` acts on the assignment algebra and may be lowered to a one-generator `ProcessSystem`; an ordinary ODE is therefore a representation shadow, not the process ontology.

Executable controls:

```text
tests/classical/test_am_process_direction.py
tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

A/M is the negative control: process motion alone does not imply observer transport.

## 3. `ConstraintCanonicalization`

The first implemented canonicalization backend is the exact local condition

\[
\Phi(z,g)=0.
\]

Differentiating it along declared base rates and solving uniquely for observer rates gives the current exact connection backend.

There is deliberately no generic `Canonicalization` protocol.  Restricted Kepler remains the red team: osculation, orthogonality, projection, or stationarity need not share the exact-equation implementation contract.

## 4. `ObserverConnection`

`ObserverConnection` records actual observer motion required to maintain a local canonical representation.  Current positive calibrations are:

- Restricted Riccati: root/separation parameters move inside the affine observer family;
- coupled scalar registers: relative scale moves while preserving the balancing condition.

It stores provenance, base rates, observer rates, and exact residuals.  It does not yet define principal-bundle structure, curvature, holonomy, composition, or numerical path ordering.

### Discrete red team

Sonnet 001 Phase 8B rejected a tempting false positive.  Two one-to-one center-depth updates preserve the exact same witness boundary and mode and merely shift event rank by `+2`:

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval').
```

These are history/decoder reindexing, not observer motion.  Sonnet 001 therefore currently provides **no discrete evidence for `ObserverConnection`**.

## 5. `CanonicalDecomposition`

The generic result record stores

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp}
\]

plus evidence, without prescribing a universal decomposition algorithm.

It has now survived four qualitatively different carriers:

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

The empty middle sector is part of the calibration, not a missing feature.

## 6. Classical killer calibrations

### Restricted Riccati

`tests/classical/test_restricted_riccati_canonical_observer.py` starts from

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

`tests/classical/test_coupled_scalar_canonical_observer.py` selects the relative ruler by

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

With the repository convention `[X,Y]=X(Y)-Y(X)` and

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

and classifies the exact `n=0`, `n=1`, `n=2` forcing sectors as renormalization, resonance/modulation, and function-module completion.  This calibrates `CanonicalDecomposition` across a non-Lie carrier without pretending that Kepler osculation is already implemented by `ConstraintCanonicalization` [Goldstein-Poole-Safko-2002; Arnold-1989; DLMF-4.21].

## 7. Sonnet 001: completion is not one operation

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

Every selected wall is new at center 3.  Four raw signatures already equal their task quotient.  Two are over-refined:

\[
11\text{ raw classes}\to7\text{ task classes},
\qquad
13\text{ raw classes}\to3\text{ task classes}.
\]

Phase 8C.2 objectifies these quotients and constructs exact adaptive decoders using only the selected completion walls.  In the `13 -> 3` case, raw support contains four walls but decoder worst depth is only three.

Executable essays:

```text
tests/research/test_lonely_runner_minimal_completion_residuals.py
tests/research/test_lonely_runner_residual_objectification.py
```

Result notes 22 and 23 preserve the full proof maps and boundaries [Karp-1972; Huffman-1952].

## 8. Sonnet 001 Phase 8D: local completion versus global placement

`tests/research/test_lonely_runner_persistent_dag_increment.py` keeps the center-2 68-label persistent Hauffman tree unchanged and grafts the six objectified completion decoders only at genuine `F_comp` leaves.

Frozen center-2 tree:

```text
tree/boundary nodes  328
internal nodes       109
terminal-merged DAG  177
peak                   72
worst depth              9.
```

The six completion decoders add 16 internal query nodes and 38 path leaves.  The explicit center-3 graft is therefore

\[
328-6+16+38=\boxed{376}
\]

prefix-tree nodes,

\[
109+16=\boxed{125}
\]

internal nodes, and after merging 75 final semantic terminals,

\[
125+75=\boxed{200}
\]

persistent DAG nodes.

Thus one contact layer adds `+48` tree nodes but only `+23` explicit DAG objects after semantic objectification.

### Structural comparison

The separately frozen fresh center-3 time-first tree also has `376` total nodes and `125` internal nodes, but its peak/worst pair is `(72,10)` while the local graft has

\[
\boxed{(75,12)}.
\]

Hence Phase 8D cleanly separates:

```text
local completion/objectification -> how much decision structure is needed
global Hauffman placement        -> where that structure sits in history.
```

Equality of total node counts is a bounded calibration fact, not a graph-isomorphism or universality theorem.

## 9. Cost semantics: current usage is not refinement risk

The historical 55-input center-2 Hauffman distribution hits none of the eight refinement-sensitive parents:

```text
completion inputs       0
history-reindex inputs  0
extra wall queries      0.
```

Its zero incremental cost is therefore a **sampling blind spot**, not evidence that refinement is free.

Conditional on the actual 298 locally reopened children, 288 lie below genuine completion parents and ten below the two history-reindex parents.  Exact local decoders use

\[
\boxed{544}
\]

new wall queries in total:

\[
E[d_{\rm extra}\mid\text{reopened}]
=\frac{544}{298}\approx1.8255,
\]

\[
E[d_{\rm extra}\mid F_{\rm comp}]
=\frac{544}{288}=\frac{17}{9}\approx1.8889,
\]

with worst extra depth three.

Therefore current usage weights and continuation/refinement weights must remain separate cost axes.  This is now the strongest new pressure on Shakespeare's presentation-cost layer.

Recorded exact 8D run:

```text
workflow run: 32586254733
Python:       3.12.14
8D:           1 passed in 21.46 s.
```

## 10. Negative controls

The new vocabulary must say when **not** to apply itself:

- A/M: process direction but no moving observer;
- Pendulum: task-relative scalar observable selection, not observer transport;
- two-frequency oscillator: coefficient refinement is not automatically `F_comp`;
- Galilean/magnetic cocycles: central history residual is not automatically a connection;
- Sonnet 8B: changed history index is not observer motion;
- Sonnet 8C: minimum raw wall support is not automatically a canonical primitive;
- Sonnet 8D: current-usage expected depth is not automatically future refinement cost.

These failures and empty sectors are part of the API evidence.

## 11. Current API judgment

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
- persistent-DAG public object;
- stationary/cost canonicalization;
- observer bundle;
- generic process-jet object;
- curvature/holonomy;
- numerical observer ODE integration.

## 12. Next pressure on the cost API

Freeze all local completion semantics from Sonnet 8A--8D.  The next experiment changes only **global wall placement**.

The cost model must be able to compare at least:

```text
current history / expected-depth cost
frontier / boundary geometry
residual and decoder size
explicit continuation/refinement workload.
```

In particular, refinement weights must not be silently inferred from current usage samples.  A refinement-aware Hauffman search should ask whether the already-discovered `376/125` decision structure can be rearranged from the persistent graft's `(peak,worst)=(75,12)` toward the fresh center-3 `(72,10)` geometry without changing the six completion residuals.

Only after this placement problem is understood should a center-3 -> center-4 persistence experiment be used to pressure a more general API.

## 13. Literate-programming / consistency gate

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

`tests/test_canonical_observer_essay_hygiene.py` checks required sections, citation-key resolution and locators, and Proof-map/test correspondence.  `docs/37-canonical-observer-claim-ledger.md` maps important mathematical claims to implementation owners, executable certificates, references, and epistemic status.

## 14. References

[Hall-2015] Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd ed., Graduate Texts in Mathematics 222, Springer, 2015; DOI 10.1007/978-3-319-13467-3.

[Carinena-Marmo-Nasarre-1998] J. F. Carinena, G. Marmo, J. Nasarre, "The nonlinear superposition principle and the Wei-Norman method," arXiv:physics/9802041 (1998), https://arxiv.org/abs/physics/9802041 .

[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989; DOI 10.1007/978-1-4757-2063-1.

[Goldstein-Poole-Safko-2002] Herbert Goldstein, Charles P. Poole Jr., John L. Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, Chapter 3, ISBN 0-201-65702-3.

[DLMF-4.21] NIST Digital Library of Mathematical Functions, §4.21, https://dlmf.nist.gov/4.21 .

[Karp-1972] Richard M. Karp, "Reducibility among Combinatorial Problems," in *Complexity of Computer Computations*, Plenum Press, 1972, pp. 85--103; DOI 10.1007/978-1-4684-2001-2_9.

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .
