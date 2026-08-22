# Canonical observer vertical slice

**Status:** research-only API shaping; not part of the 0.0.2 compatibility contract.

## 1. Current causal order

The AEG Analysis programme currently uses

```text
local canonicalization
    -> observer connection when canonicalization actually moves
    -> canonical decomposition
    -> renormalize / transport / complete
```

The implementation must preserve this causal order without forcing every theoretical term into every example.

The branch currently contains only four small roles:

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition
```

The first three continuous killer calibrations and the Sonnet 001 discrete red team have now made their boundaries sharper.

## 2. `ProcessDirection`

`ProcessDirection` represents only

\[
\mathscr D=\sum_i u^iX_i
\]

inside an already-declared `ProcessFrame`.  It can be lowered to a one-generator `ProcessSystem`, but the ordinary assignment ODE is a shadow rather than the ontology of the process.

Executable controls:

```text
tests/classical/test_am_process_direction.py
tests/classical/test_restricted_riccati_canonical_observer.py
tests/classical/test_coupled_scalar_canonical_observer.py
```

The A/M essay is also a negative control: process motion alone does not imply observer transport.

## 3. `ConstraintCanonicalization`

The first concrete canonicalization backend is the exact local constraint

\[
\Phi(z,g)=0.
\]

Differentiating it along declared base rates and solving uniquely for observer-parameter rates produces the current exact `ObserverConnection` backend.

There is deliberately no generic `Canonicalization` alias or base protocol.  Restricted Kepler already shows why: osculation, orthogonality, projection, or stationarity need not have the same implementation contract as an exact algebraic constraint.

## 4. `ObserverConnection`

`ObserverConnection` is an evidence-bearing local transport record containing

```text
canonicalization provenance
base rates
observer rates
exact residuals
```

It is currently justified by examples in which the canonical observer actually moves:

- Restricted Riccati: root/separation parameters move to maintain the affine canonical form;
- coupled scalar registers: relative scale moves to maintain balanced cross coupling.

It does **not** yet define a principal bundle, horizontal projection, composition, curvature, holonomy, or numerical path-ordered integration.

### Discrete red team

Sonnet 001 Phase 8B provides an important negative result: two center-depth updates initially suspected of being observer transport preserve the exact same witness boundary and mode and only shift the event rank by `+2`.  They are history/decoder reindexing, not observer motion.

Therefore Sonnet 001 does **not** currently constitute discrete evidence for `ObserverConnection`.

## 5. `CanonicalDecomposition`

The generic record stores a claimed split

\[
F=F_{\rm ren}+F_{\rm res}+F_{\rm comp}
\]

plus evidence, without prescribing a universal decomposition algorithm.

It has now survived four qualitatively different carriers:

| Calibration | Carrier | Exact role split |
| --- | --- | --- |
| Restricted Riccati | Lie directions | affine tangent / no resonance / `Q` completion |
| coupled scalars | multivariable Lie directions | diagonal ruler / no resonance / cross-direction completion |
| Restricted Kepler | function-module modes | `n=0 / n=1 / n=2` |
| Sonnet 001 Phase 8A/8B | persistent finite task states | `843 / 0 / 6` |

For Sonnet 001, the exact final interpretation is

\[
\boxed{
843\text{ renormalizable}
=841\text{ identity-stable}+2\text{ history reindex},
\quad0\text{ resonant},
\quad6\text{ completion}.
}
\]

This strengthens the case for the **result shape** while simultaneously showing that the middle sector need not be nonempty.

## 6. Calibration A — Restricted Riccati

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

an affine root/separation observer is selected by exact root constraints.  In `y=(x-r)/d`, observer transport absorbs the `A,M` directions while the quadratic coefficient survives as a genuine completion residual.  Only afterwards does the test identify the familiar classical closure

\[
[A,M]=A,
\qquad[A,Q]=2M,
\qquad[M,Q]=Q,
\]

with the Riccati `sl(2)` realization [Carinena-Marmo-Nasarre-1998; Hall-2015].

## 7. Calibration B — coupled scalar registers

Executable essay:

```text
tests/classical/test_coupled_scalar_canonical_observer.py
```

The relative scale `rho` is selected by

\[
b_{12}\rho^2-b_{21}=0,
\]

so

\[
\frac{\dot\rho}{\rho}
=
\frac12
\left(
\frac{\dot b_{21}}{b_{21}}
-
\frac{\dot b_{12}}{b_{12}}
\right).
\]

The connection remains in the diagonal-ruler algebra; bidirectional cross directions require matrix completion.

### Bracket-sign audit

The repository convention is

\[
[X,Y]=X(Y)-Y(X).
\]

With

\[
E_{12}=y\partial_x,
\qquad E_{21}=x\partial_y,
\]

this gives

\[
\boxed{[E_{12},E_{21}]=M_2-M_1.}
\]

The externally supplied AEG Analysis v0.2 note contains one line with the opposite sign.  Repository code/tests/docs use the executable convention above; the external note should be corrected at its next revision.  The generated `gl(2)`/`aff(2)` structural conclusion is unchanged [Hall-2015].

## 8. Calibration C — Restricted Kepler function module

Executable essay:

```text
tests/classical/test_restricted_kepler_canonical_decomposition.py
```

For

\[
\mathcal K_1=\operatorname{span}\{1,\cos\psi,\sin\psi\},
\qquad
L_K=R^2+1,
\]

the forcing `rho_0^2` produces exact `n=0`, `n=1`, and `n=2` sectors.  Their `L_K` action distinguishes renormalization, resonance/modulation, and representation completion, and `R` forces the second-harmonic companion needed for the five-dimensional `K_2` module [Goldstein-Poole-Safko-2002; Arnold-1989; DLMF-4.21].

This vignette intentionally does not force Kepler osculation through `ConstraintCanonicalization`.

## 9. Calibration D — Sonnet 001 Phase 8A/8B

Executable essay:

```text
tests/research/test_lonely_runner_canonical_observer_decomposition.py
```

Phase 8A chooses, before child semantics are evaluated,

```text
841 stable
2 nonbranching updates
6 completion pressure
```

from two local predicates on the old persistent state and the newly admitted contact layer.

Phase 8B then red-teams the two middle cases.  Their exact witness records are

```text
(11, ((1,1,'exit'),), 'interval') -> (13, ((1,1,'exit'),), 'interval')
(12, ((1,1,'exit'),), 'interval') -> (14, ((1,1,'exit'),), 'interval')
```

so the witness geometry is unchanged and only history rank is renormalized.

Corrected dedicated gate:

```text
workflow run: 32584153291
Python:       3.12.14
pytest:       1 passed in 7.95 s
```

The exact final canonical sectors are therefore `843 / 0 / 6`, not the earlier working `841 / 2 / 6` mapping.  Result notes 20 and 21 preserve both the original behavioral classification and the subsequent interpretive correction.

## 10. Negative controls

The new vocabulary must have clear non-applicability cases:

- A/M: process direction, but no moving canonical observer;
- Pendulum: task-relative scalar **observable** selection, not dynamic observer transport;
- two-frequency oscillator: coefficient-field refinement is not automatically `F_comp`;
- Galilean/magnetic cocycles: lifted central-history pressure is not automatically an observer connection;
- Sonnet 001 Phase 8B: changed history index is not observer motion.

These negative controls are part of the API evidence.

## 11. Current API judgment

### Strongest candidates to retain

- `ProcessDirection`;
- evidence-bearing `CanonicalDecomposition`;
- provenance-generic `ObserverConnection` for cases with actual canonical observer motion.

### Provisional backend

- `ConstraintCanonicalization`.

### Explicitly not promoted yet

- generic `Canonicalization` protocol;
- discrete observer connection;
- stationary/cost canonicalization;
- observer bundle;
- process-jet object;
- curvature/holonomy;
- universal completion engine;
- numerical observer ODE integration.

## 12. Literate-programming / consistency gate

New mathematical essays must contain

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

`tests/test_canonical_observer_essay_hygiene.py` checks required sections, reference-key resolution and locators, and Proof-map/test correspondence.

`docs/11-references-and-test-essays.md` now makes cross-artifact consistency a proof obligation.  `docs/37-canonical-observer-claim-ledger.md` maps each important formula or claim to implementation owner, executable certificate, bibliography, and epistemic status.

## 13. Next development order

The Sonnet route now continues with **Phase 8C**, not with a discrete observer ODE:

1. derive the smallest structured residuals for the six genuine completion states;
2. certify their minimal pair-difference/process closure;
3. build the persistent DAG and measure incremental Hauffman geometry;
4. search separately for a true discrete moving-observer example only if a canonical frame actually changes.

Curvature/holonomy and a generic canonicalization protocol remain deferred.

## 14. References

[Hall-2015] Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd ed., Graduate Texts in Mathematics 222, Springer, 2015, Chapters 2--3; DOI 10.1007/978-3-319-13467-3.

[Coddington-Levinson-1955] Earl A. Coddington, Norman Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, New York, 1955; linear differential equations begin p. 62 in the standard edition; ISBN 978-0-07-099256-6.

[Carinena-Marmo-Nasarre-1998] J. F. Carinena, G. Marmo, J. Nasarre, "The nonlinear superposition principle and the Wei-Norman method," arXiv:physics/9802041 (1998), https://arxiv.org/abs/physics/9802041 .

[Arnold-1989] V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Graduate Texts in Mathematics 60, Springer, 1989; DOI 10.1007/978-1-4757-2063-1.

[Goldstein-Poole-Safko-2002] Herbert Goldstein, Charles P. Poole Jr., John L. Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002, Chapter 3, ISBN 0-201-65702-3.

[DLMF-4.21] NIST Digital Library of Mathematical Functions, §4.21, "Identities" for trigonometric functions, https://dlmf.nist.gov/4.21 .

[Huffman-1952] David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101; DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat Trakulthongchai, "Eleven, twelve, and thirteen lonely runners," arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .
