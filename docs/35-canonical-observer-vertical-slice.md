# Canonical observer vertical slice

**Status:** research-only API shaping; not part of the 0.0.2 compatibility contract.

## 1. Current causal order

The AEG Analysis programme currently uses

```text
local canonicalization
    -> observer connection when the canonical representation actually moves
    -> canonical decomposition
    -> renormalize / transport / complete
    -> task-relative quotient/objectification of any new raw representation.
```

The last line is now forced by Sonnet 001 Phase 8C: a cardinality-minimal raw completion can still over-refine the task.

The branch currently contains only four reusable roles:

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition
```

No generic `Completion` object has been promoted.

## 2. `ProcessDirection`

`ProcessDirection` represents

\[
\mathscr D=\sum_i u^iX_i
\]

inside an already-declared `ProcessFrame`.  It may be lowered to a one-generator `ProcessSystem`, but assignment ODEs are shadows rather than the ontology of the process.

Executable controls:

```text
tests/classical/test_am_process_direction.py
tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

A/M is also a negative control: physical/process motion alone does not imply observer transport.

## 3. `ConstraintCanonicalization`

The first concrete canonicalization backend uses

\[
\Phi(z,g)=0.
\]

Differentiating the exact constraint along declared base rates and solving uniquely for observer-parameter rates produces the current exact `ObserverConnection` backend.

There is deliberately no generic `Canonicalization` alias or base protocol.  Restricted Kepler shows why: osculation, orthogonality, projection, or stationarity need not share this exact-equation implementation contract.

## 4. `ObserverConnection`

`ObserverConnection` is an evidence-bearing local transport record containing

```text
canonicalization provenance
base rates
observer rates
exact residuals.
```

It is justified by continuous examples where the canonical observer really moves:

- Restricted Riccati: root/separation parameters move to maintain an affine canonical form;
- coupled scalar registers: relative scale moves to maintain balanced cross coupling.

It does not yet define a principal bundle, horizontal projection, composition, curvature, holonomy, or numerical path ordering.

### Discrete red team

Sonnet 001 Phase 8B rejects a tempting false positive.  Two one-to-one task changes preserve the exact same witness boundary and mode and only shift event rank by `+2`; they are history/decoder reindexing, not observer motion.

Therefore Sonnet 001 currently provides **no discrete evidence for `ObserverConnection`**.

## 5. `CanonicalDecomposition`

The generic record stores a claimed split

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp}
\]

plus evidence without prescribing a universal discovery algorithm.

It has survived four qualitatively different carriers:

| Calibration | Carrier | Exact calibrated split |
| --- | --- | --- |
| Restricted Riccati | Lie directions | affine tangent / empty resonant sector / `Q` completion |
| coupled scalar registers | multivariable Lie directions | diagonal ruler / empty resonant sector / cross completion |
| Restricted Kepler | finite function module | `n=0 / n=1 / n=2` |
| Sonnet 001 Phase 8A/8B | persistent finite task states | `843 / 0 / 6` |

For Sonnet 001:

\[
\boxed{
843\text{ renormalizable}
=841\text{ identity-stable}+2\text{ history reindex},
\quad0\text{ resonant},
\quad6\text{ completion}.
}
\]

This strengthens the result shape while showing that the middle sector may be empty.

## 6. Restricted Riccati calibration

Executable essay:

```text
tests/classical/test_restricted_riccati_canonical_observer.py
```

With

\[
A=\partial_x,
\quad M=x\partial_x,
\quad Q=x^2\partial_x,
\]

an affine root/separation observer is selected by exact root constraints.  In `y=(x-r)/d`, observer transport absorbs the affine directions while `Q` survives as a genuine completion residual.  Only afterwards does the test identify the classical closure

\[
[A,M]=A,
\qquad[A,Q]=2M,
\qquad[M,Q]=Q
\]

with the Riccati `sl(2)` realization [Carinena-Marmo-Nasarre-1998; Hall-2015].

## 7. Coupled scalar calibration and sign audit

Executable essay:

```text
tests/classical/test_coupled_scalar_canonical_observer.py
```

The relative scale `rho` is selected by

\[
b_{12}\rho^2-b_{21}=0,
\]

hence

\[
\frac{\dot\rho}{\rho}
=
\frac12\left(
\frac{\dot b_{21}}{b_{21}}-
\frac{\dot b_{12}}{b_{12}}
\right).
\]

Observer motion remains in the diagonal-ruler algebra; bidirectional cross directions require matrix completion.

The repository convention is

\[
[X,Y]=X(Y)-Y(X).
\]

For

\[
E_{12}=y\partial_x,
\qquad E_{21}=x\partial_y,
\]

it gives

\[
\boxed{[E_{12},E_{21}]=M_2-M_1.}
\]

One line in the externally supplied AEG Analysis v0.2 note has the opposite sign.  Repository code/tests/docs use the executable convention; the external note should be corrected in its next revision.  The `gl(2)`/`aff(2)` generation statement is unchanged [Hall-2015].

## 8. Restricted Kepler calibration

Executable essay:

```text
tests/classical/test_restricted_kepler_canonical_decomposition.py
```

For

\[
\mathcal K_1=\operatorname{span}\{1,\cos\psi,\sin\psi\},
\qquad L_K=R^2+1,
\]

the squared shape forcing produces exact `n=0`, `n=1`, and `n=2` sectors.  Their `L_K` action distinguishes renormalization, resonance/modulation, and representation completion, and `R` forces the second-harmonic companion required for the five-dimensional `K_2` module [Goldstein-Poole-Safko-2002; Arnold-1989; DLMF-4.21].

This example intentionally does not force osculation through `ConstraintCanonicalization`.

## 9. Sonnet 001 Phase 8A/8B

Executable essay:

```text
tests/research/test_lonely_runner_canonical_observer_decomposition.py
```

Phase 8A predicts, before child semantics are evaluated,

```text
841 stable
2 nonbranching updates
6 completion pressure.
```

Phase 8B shows the two nonbranching cases are only history reindexing:

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval').
```

Thus final canonical sectors are `843 / 0 / 6`.

Corrected dedicated gate:

```text
workflow run: 32584153291
Python:       3.12.14
pytest:       1 passed in 7.95 s.
```

Result notes 20 and 21 preserve the behavioral classification and its later interpretive correction.

## 10. Sonnet 001 Phase 8C — minimum raw completion

Executable essay:

```text
tests/research/test_lonely_runner_minimal_completion_residuals.py
```

For each of the six genuine completion parents, every varying center-3 pair/contact wall sign is allowed as a primitive residual.  Exact conflict-cover dynamic programming finds a minimum-cardinality task-separating raw wall signature.

The six minimum wall counts are

\[
\boxed{1,2,2,2,3,4}.
\]

Every selected wall is **new at center 3**; no selected minimum signature needs an old latent wall.

Per-parent `(task semantics, wall count, residual sign classes)` profile:

```text
(3,1,3)
(3,4,13)
(5,2,5)
(5,2,5)
(5,2,5)
(7,3,11).
```

Four parents reach an exact task quotient directly.  Two remain over-refined even at minimum raw wall cardinality.  Therefore:

```text
completion pressure
    !=
minimum raw generator support
    !=
minimum task representation.
```

Dedicated exact run:

```text
workflow run: 32584599992
Python:       3.12.14
8A/8B:        1 passed in 8.04 s
8C:           1 passed in 7.55 s.
```

Full claim boundary is in `sonnet/lonely-runner/22-phase8c-minimum-completion-residuals.md` [Karp-1972].

## 11. Negative controls

The new vocabulary must say when **not** to apply itself:

- A/M: process direction but no moving observer;
- Pendulum: task-relative scalar **observable** selection, not dynamic observer transport;
- two-frequency oscillator: coefficient refinement is not automatically `F_comp`;
- Galilean/magnetic cocycles: lifted central-history pressure is not automatically a connection;
- Sonnet Phase 8B: changed history index is not observer motion;
- Sonnet Phase 8C: a cardinality-minimal wall tuple is not automatically a canonical primitive.

These negative controls are part of the API evidence.

## 12. Current API judgment

### Strongest candidates to retain

- `ProcessDirection`;
- evidence-bearing `CanonicalDecomposition`;
- provenance-generic `ObserverConnection` only for cases with actual observer motion.

### Provisional backend

- `ConstraintCanonicalization`.

### Explicitly not promoted yet

- generic `Canonicalization` protocol;
- discrete observer connection;
- universal `Completion` object;
- stationary/cost canonicalization;
- observer bundle;
- process-jet object;
- curvature/holonomy;
- numerical observer ODE integration.

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

`tests/test_canonical_observer_essay_hygiene.py` checks required sections, citation-key resolution and locators, and Proof-map/test correspondence.

`docs/11-references-and-test-essays.md` makes cross-artifact mathematical consistency a proof obligation.  `docs/37-canonical-observer-claim-ledger.md` maps formulas and claims to implementation owners, executable certificates, references, and epistemic status.

## 14. Next development order

Phase 8C now forces a narrower next step before the persistent DAG is frozen:

1. objectify/quotient the two over-refined minimum raw signatures into exact 7-value and 3-value residual primitives;
2. keep the four exact raw signatures as provisional completion primitives;
3. compare opaque parent identity vs raw tuple vs objectified residual on decoder/update cost;
4. then build the persistent DAG and measure incremental Hauffman geometry;
5. search separately for a true moving-observer discrete example only if a canonical frame actually changes.

Curvature/holonomy and a generic canonicalization protocol remain deferred.

## 15. References

[Hall-2015] Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd ed., Graduate Texts in Mathematics 222, Springer, 2015; DOI 10.1007/978-3-319-13467-3.

[Coddington-Levinson-1955] Earl A. Coddington, Norman Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955; linear differential equations begin p. 62; ISBN 978-0-07-099256-6.

[Carinena-Marmo-Nasarre-1998] J. F. Carinena, G. Marmo, J. Nasarre, "The nonlinear superposition principle and the Wei-Norman method," arXiv:physics/9802041 (1998), https://arxiv.org/abs/physics/9802041 .

[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989; DOI 10.1007/978-1-4757-2063-1.

[Goldstein-Poole-Safko-2002] Herbert Goldstein, Charles P. Poole Jr., John L. Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, Chapter 3, ISBN 0-201-65702-3.

[DLMF-4.21] NIST Digital Library of Mathematical Functions, §4.21, https://dlmf.nist.gov/4.21 .

[Karp-1972] Richard M. Karp, "Reducibility among Combinatorial Problems," in *Complexity of Computer Computations*, Plenum Press, 1972, pp. 85--103; DOI 10.1007/978-1-4684-2001-2_9.

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .
