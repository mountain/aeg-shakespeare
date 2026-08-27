# Phase 1J-B3 contract — bounded formal marked-family summation

**Status:** frozen and executed as a proof-level corollary contract.

**Parent question:** Phase 1J-B2 proved total-variation contraction for one
root-visible collision mark in one pre-cut molecule integral. B3 asks whether
the mark count can pass through the full Deng--Hani--Ma molecule and
operation-sequence summation without consuming the positive-power gain.

**Dependency firewall:** B3 uses B2's fixed-molecule pushforward lemma and the
positive absolute-integral estimates in the continuum paper. It uses no
conclusion from Phase 1J-A. The resulting object is a formal signed molecule
current, not yet the microscopic hard-sphere collision current.

## 1. Primary-source proof seam

The source is Y. Deng, Z. Hani and X. Ma,
[*Long time derivation of the Boltzmann equation from hard sphere dynamics*](https://arxiv.org/abs/2408.07818).
B3 uses the following statements at their stated strength.

| Source object | Exact role | Claim not imported |
| --- | --- | --- |
| Definitions 3.22--3.23, equations (3.10)--(3.13) | define the signed \(IN_M\) and positive \(\lvert IN_M\rvert\); the sign is \((-1)^{\lvert M\rvert_O}\) | a collision-current identity |
| Proposition 3.25, equations (3.17)--(3.18) | dominate \(E_H\) and \(\mathrm{Err}_1\) by positive molecule sums | equality between a marked sum and the cumulant current |
| Proposition 7.2, equation (7.2) | at fixed \(m=\lvert M\rvert\) and \(\rho\), molecule choices are at most \(C^m\lvert\log\epsilon\rvert^{C_*\rho}\) | a marked estimate by itself |
| Proposition 7.5, equations (7.7)--(7.8) | identifies \(\lVert IN_M\rVert_{L^1}\) with the positive associated integral \(I_M(Q_M)\) and root normalization | a boundary trace theorem |
| Definition 8.10 and Proposition 8.18 | deletion, cutting and support splitting dominate \(I_M(Q_M)\) by final sub-cases | physical composition of cut histories |
| Proposition 9.7, equation (9.51) | bounds sub-case count and guarantees enough good-versus-bad gain | preservation of an unbounded test observable |
| equations (9.52)--(9.53) | close the global molecule-size/recollision/sub-case sum | identification with actual collision flux |

The source paper's operation sequence deletes only O-atoms, cuts molecules,
and splits \(Q\) by an indicator partition. A root-visible C-atom is therefore
never deleted; a cut places it in exactly one component; and splitting does
not change the molecule.

## 2. Formal pre-cut marked family

Let \(H\) be the retained root-label set and let

\[
\mathcal C_H(M)
=\{n\in M:n\text{ is a C-atom incident to a particle line rooted in }H\}.
\]

For the signed measure underlying \(IN_M\), the pre-cut event map \(e_n\)
defines

\[
\kappa_{M,n}:=(e_n)_\#\lambda_M.
\]

The formal marked family is

\[
\mathfrak K_H^\epsilon
=\sum_{[M]\in F_{\Lambda_\ell},\,r(M)=H}
  \sum_{n\in\mathcal C_H(M)}\kappa_{M,n}.
\]

This notation initially denotes a family of signed measures. Its existence
as an enumeration-independent signed measure must be earned by absolute
total-variation summability.

## 3. The early mark-erasure lemma

For every bounded measurable event test \(\psi\), B2 gives

\[
\left|\langle\kappa_{M,n},\psi\rangle\right|
\le \lVert\psi\rVert_\infty\,\lVert\lvert IN_M\rvert\rVert_{L^1}.
\]

Therefore

\[
\sum_{n\in\mathcal C_H(M)}
\left|\langle\kappa_{M,n},\psi\rangle\right|
\le \lVert\psi\rVert_\infty
   \lvert\mathcal C_H(M)\rvert
   \lVert\lvert IN_M\rvert\rVert_{L^1}
\le \lVert\psi\rVert_\infty
   \lvert M\rvert
   \lVert\lvert IN_M\rvert\rVert_{L^1}.
\]

The decisive move is to take this bound **before** applying the operation
sequence. The bounded observable is then erased, and the remainder is exactly
the positive integral already treated by Propositions 7.5, 8.18 and 9.7. No
marked analogue of every elementary \(L^\infty\to L^\infty\) estimate is
needed for this bounded-test theorem.

This shortcut is unavailable for the unbounded logarithmic Boltzmann affinity.

## 4. Global summation theorem target

Define the absolute marked budget

\[
\mathcal B_H^\epsilon
=\sum_{[M]\in F_{\Lambda_\ell},\,r(M)=H}
 \lvert\mathcal C_H(M)\rvert
 \lVert\lvert IN_M\rvert\rVert_{L^1}.
\]

Equation (9.52), with the mark inserted, differs only by a factor
\(m=\lvert M\rvert\). The source proof contributes:

- \(C^m\lvert\log\epsilon\rvert^{C_*\rho}\) from molecule choices;
- another \(C^m\lvert\log\epsilon\rvert^{C_*\rho}\) from operation sub-cases;
  and
- \(\tau^{m/9}\) together with positive \(\epsilon\)-power gain from each
  final sub-case in (9.53).

Since

\[
mC^m\le (2C)^m\qquad(m\ge1),
\]

the linear mark count merely enlarges the generic exponential constant. The
same parameter hierarchy that makes the unmarked molecule-size sum geometric
also closes the marked sum. Consequently, for the \(F_{\Lambda_\ell}\)
cumulant family there exist source-hierarchy constants \(a,b,C>0\) such that,
for sufficiently small \(\epsilon\),

\[
\mathcal B_H^\epsilon\le C\epsilon^{a+b\lvert H\rvert}.
\]

The symbolic \(a,b\) preserve the proof's positive-power content without
silently asserting that the exact displayed exponent in Proposition 6.2 is
itself a stated marked theorem. The proof permits the same positive-power form
after enlarging generic constants and, if necessary, slightly weakening the
recorded slack.

It follows that \(\mathfrak K_H^\epsilon\) is an absolutely convergent formal
signed measure and

\[
\sup_{\lVert\psi\rVert_\infty\le K}
\left|\langle\mathfrak K_H^\epsilon,\psi\rangle\right|
\le K\mathcal B_H^\epsilon.
\]

Thus the strongest bounded test class, equivalently total variation, closes
for the formal molecule current.

## 5. Error-family grading

The proof treats error types differently and B3 retains that typing.

| Family | B3 grade | Reason |
| --- | --- | --- |
| \(F_{\Lambda_\ell}\) cumulant molecules | pass | the only new factor is \(m\), absorbed into the geometric size sum |
| \(F^{\mathrm{err}}_{\Lambda_\ell}\) large-component molecules | conditional pass under the source hierarchy | (9.82) has an extra \(\epsilon^{-C_*\lvert H\rvert}\), already absorbed by the \(\tau^{m/2}\) reserve using \(m\ge\Lambda_\ell\); a further linear \(m\) is harmless |
| \(\mathrm{Err}_2\) | outside this marked sum | Proposition 3.25 gives a separately typed norm estimate, not this molecule-current representation |
| final \(f_s^{\mathrm{err}}\) | outside this gate | Proposition 6.3/Section 15 uses a different terminal error analysis |

No error norm is reinterpreted as a collision-current measure.

## 6. Executable obligations

The exact rational certificate must verify:

1. deletion of an O-atom preserves every eligible C-mark;
2. a cut routes each pre-cut mark to exactly one component;
3. support splitting partitions the marked pairing without duplication;
4. bounded tests are erased before the operation sequence;
5. \(m\le2^m\) absorbs the linear mark factor into a generic exponential base;
6. a paper-shaped size/recollision envelope is geometrically summable;
7. linear marking changes only the summation constant, not its ratios;
8. an exact tail proves absolute convergence of the formal current;
9. the full bounded test ball is controlled for formal partial currents;
10. large-component error absorption remains separately conditional;
11. a unit size ratio is a kill condition;
12. exponentially many marks can erase a size gain; and
13. current identification, logarithmic tests, entropy and H remain open.

The executable is
[test_marked_operation_sequence_summation.py](../../tests/research/test_marked_operation_sequence_summation.py).

## 7. Claim ceiling

Passing B3 earns absolute summability and total-variation control for the
**formal pre-cut signed molecule family**. It does not earn:

- equality between this formal family and a current associated with \(E_H\);
- an actual/truncated/target hard-sphere collision-flux identity;
- a trace theorem or control of separately typed residual currents;
- an unbounded logarithmic test or uniform-integrability estimate;
- an entropy chain rule or continuum/microscopic H theorem;
- molecule objectification, arithmetic-rank promotion or a generic API.

The expected repository effect remains research-level U4/E. Core, Theory Map
and public API remain unchanged.
