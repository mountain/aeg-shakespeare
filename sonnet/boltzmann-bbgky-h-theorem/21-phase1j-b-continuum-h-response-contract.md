# Phase 1J-B contract — continuum collision-flux H-response budget

**Status:** frozen record-only continuum contract with nine exact rational
measure certificates.  The Deng--Hani--Ma results remain external theorem
records.  This phase proves no collision trace or history-to-flux lift,
Boltzmann--Grad flux estimate, entropy chain rule for a hard-sphere marginal,
or microscopic H theorem.

**Executable owner:**
[`test_continuum_collision_flux_response_budget.py`](../../tests/research/test_continuum_collision_flux_response_budget.py).

**Result owner:**
[`22-phase1j-b-continuum-h-response-results.md`](./22-phase1j-b-continuum-h-response-results.md).

## 0. Dependency firewall

Phase 1J-B depends on the continuum task typing of
[Phase 1E](./09-phase1e-continuum-collision-adapter-contract.md), the weak
collision-flux measure of
[Phase 1F](./11-phase1f-weak-mild-continuation-cell-contract.md), and the
finite response-budget pattern of
[Phase 1I](./17-phase1i-charted-fibre-calculus-contract.md).

It is independent of Phase 1J-A.  In particular, this contract does not use a
finite collision-covector selector, a response cocycle, or any conclusion
about a preferred chart.  Conversely, this phase supplies no continuum
evidence to 1J-A.

The native response object here is one signed measure on an entire declared
collision-event space.  It is not a word with one discrete letter per
collision.  The finite executable uses event cells only as atoms of a test
partition for exact measure arithmetic.

## 1. Primary-source audit

The calibration source is Deng--Hani--Ma,
[*Long time derivation of the Boltzmann equation from hard sphere dynamics*](https://arxiv.org/abs/2408.07818),
accepted by the
[Annals of Mathematics](https://annals.math.princeton.edu/articles/22284).
Its usable statements and their limits are:

| Paper statement | Earned input | What it does not supply |
| --- | --- | --- |
| Theorem 1, equation (1.18) | uniform-in-time bulk \(L^1\) convergence of \(f_s\) to the factorized Boltzmann state, for the declared \(s\), horizon, and hypotheses | a contact trace, collision-current measure, or entropy-covector pairing |
| Proposition 3.25, equations (3.14)--(3.20) | a truncated cumulant expansion with molecule bounds and separately displayed errors | a boundary-flux expansion or an H-response identity |
| Proposition 6.2, equations (6.3)--(6.4) | bulk \(L^1\) smallness of nonempty cumulants and one error family | control of an unbounded logarithmic observable on collision events |
| Proposition 8.13, equation (8.1) | deleting an O-atom gives an integral inequality | physical deletion or a new composition law |
| Proposition 8.14, equation (8.2) | \(I_M=I_{M_1}\circ I_{M_2}\) as an iterated-integral/Fubini identity | composition of physical histories, response-cocycle regularity, or arithmetic-rank objectification |

The last boundary is explicit in Definition 8.3: after cutting, the paper
says the correspondence between the molecular and physical pictures breaks
down and subsequently uses only molecule language.  The cut is therefore an
estimate operation.  It may help prove a marked integral bound, but it cannot
be relabelled as free physical composition.

The paper mentions entropy in its motivation but does not state an H theorem,
use a \(\log f\) collision covector, or prove the flux estimate required below.

## 2. Assumptions and declared task

Fix a horizon \([0,T]\), a one-particle root task, and a hard-sphere diameter
\(\epsilon\).  Let \(\Sigma_T^\epsilon\) be the measurable collision-event
space carrying, at minimum,

\[
(t,x,v,u,\omega,\sigma),
\qquad
t\in[0,T],\quad \omega\in\mathbb S^{d-1},
\quad \sigma\in\{+,-\},
\]

together with the contact geometry and any root label needed by the weak
BBGKY pairing.  Let \(\mathcal M(\Sigma_T^\epsilon)\) be the finite signed
measures on this space.

The source must supply an oriented collision-flux measure by one of the two
routes already frozen in Phase 1F:

1. a boundary trace or weak Green theorem; or
2. an averaged microscopic collision-event counting measure plus an
   identification theorem.

Bulk \(L^1\) correlation convergence is not a third route.

Let \(J_T^\epsilon\) be the actual signed collision current and
\(J_T[f]\) the declared stopped/factorized target current.  Both must use the
same orientation convention and event test class.  The continuum response
fibre element is

\[
\nu_T^\epsilon=J_T^\epsilon-J_T[f]
\in\mathcal M(\Sigma_T^\epsilon).
\]

For every admitted test covector \(\psi\), the native response ledger is

\[
\boxed{
\langle J_T^\epsilon,\psi\rangle
=\langle J_T[f],\psi\rangle
+\langle\nu_T^\epsilon,\psi\rangle .
}
\]

For a cut \(0<S<T\), restriction of measures gives the exact horizon law

\[
\nu_{[0,T]}^\epsilon
=\nu_{[0,S]}^\epsilon+\nu_{[S,T]}^\epsilon.
\]

This is measure additivity, not a molecule-composition or response-cocycle
claim.

## 3. Conditional H-response ledger

For a strictly positive target solution \(f\), define on a binary collision
event

\[
g=ff_*,\qquad g'=f'f_*',\qquad
a_f=\log\frac{g'}{g}.
\]

With the usual collision orientation, the Boltzmann dissipation over the
horizon is

\[
\mathcal D_T[f]
=\frac14\int (g'-g)a_f\,d\lambda_T\ge0,
\]

where \(d\lambda_T\) includes time, position, velocities, normal, and the
hard-sphere collision kernel.  Write the H-test covector as

\[
\psi_f=-\frac14a_f.
\]

If a justified entropy chain rule and flux identification are available, the
adapted one-particle observable has the conditional ledger

\[
\Delta H_T^{\mathrm{adapted}}
=-\mathcal D_T[f]
+\langle\nu_T^\epsilon,\psi_f\rangle
+e_{\mathrm{tr}}
+e_{\mathrm{mark}}
+e_{\mathrm{trunc}}
+e_{\mathrm{geom}}
+e_{\mathrm{kin}}.
\]

The five residual axes respectively record:

- trace/history-to-flux identification;
- marking a root-visible collision in a history or molecule integral;
- truncated dynamics and omitted histories;
- finite-\(\epsilon\) contact geometry and scaling;
- comparison of the stopped \(f_A\) branch with the Boltzmann solution.

The displayed equality is a target contract, not a theorem supplied by this
phase.  In particular, \(H(f_1^\epsilon)\) is nonlinear in the marginal and
does not follow from inserting a fixed weak test into BBGKY without a chain
rule.

## 4. Clipped covector and exact sufficient budget

The logarithmic affinity is unbounded when \(f\) approaches zero.  For
\(K>0\), define

\[
\psi_f^K=\max(-K,\min(K,\psi_f)),
\qquad
r_f^K=\psi_f-\psi_f^K.
\]

Then every finite signed response measure satisfies

\[
\begin{aligned}
|\langle\nu_T^\epsilon,\psi_f\rangle|
&\le
|\langle\nu_T^\epsilon,\psi_f^K\rangle|
+|\langle\nu_T^\epsilon,r_f^K\rangle|\\
&\le
K\|\nu_T^\epsilon\|_{\mathrm{TV}}
+\int|r_f^K|\,d|\nu_T^\epsilon|.
\end{aligned}
\]

Let

\[
\mathcal E_T^K
=K\|\nu_T^\epsilon\|_{\mathrm{TV}}
+\int|r_f^K|\,d|\nu_T^\epsilon|
+\sum_j|e_j|.
\]

A sufficient, not necessary, transfer condition is

\[
\boxed{\mathcal D_T[f]\ge\mathcal E_T^K.}
\]

Under the missing equality and finiteness hypotheses this certifies
\(\Delta H_T^{\mathrm{adapted}}\le0\).  The contract separates two obligations:

1. bound the response against a fixed clipped class; and
2. prove uniform integrability of the logarithmic tail as \(K\to\infty\), or
   retain \(K\) as part of a renormalized task.

Small total variation alone cannot solve the second obligation uniformly over
an unbounded covector class.  The executable red team uses a mass \(1/n\)
paired with value \(n\): total variation tends to zero while the pairing stays
one.

## 5. Missing Deng-calibrated theorem

For the \(s=1\) BBGKY task, the flux reads two-particle data.  Proposition
3.25 can be applied to the \(s=2\) bulk correlation, but restricting that
expansion to contact is precisely the operation not justified by its bulk
\(L^1\) estimates.

The next theorem worth attempting is a **marked-molecule flux lift**:

1. before any cut, mark a root-visible C-atom representing the tested
   collision event;
2. push the corresponding prescribed-dynamics integral to
   \(\Sigma_T^\epsilon\), obtaining a signed or Jordan-pair measure
   \(\kappa_{M,n}\);
3. prove a bounded-test estimate for the sum of marked measures, with the
   mark retained as an integration observable through every cut;
4. use Proposition 8.14 only as an iterated-integral identity and never as a
   physical-history composition after cutting;
5. sum molecule, truncation, geometry, and \(f_A\to f\) errors in the same
   flux dual norm;
6. establish the logarithmic tail separately.

A first admissible target is

\[
\sup_{\|\psi\|_\infty\le K}
|\langle\nu_T^\epsilon,\psi\rangle|
\le \eta_K(\epsilon,T),
\qquad
\eta_K(\epsilon,T)\to0,
\]

with every dependence on \(K,T\), molecule size, recollision rank, and the
number of possible marks explicit.  Only after this bounded theorem should
the tail needed for \(\psi_f\) be attacked.

## 6. Candidate grammar, certificates, and cost

The candidate grammar is deliberately small:

- finite signed collision-current measures;
- restriction and addition of measures over time horizons;
- pairing with a declared covector;
- total variation, clipping, and a tail overshoot;
- five separately typed scalar residuals.

The executable certifies:

1. stopped current plus the whole response measure reconstructs all declared
   weak pairings;
2. response measures and pairings add under a horizon cut;
3. a bounded covector is controlled by total variation;
4. the full pairing splits exactly into clipped and tail parts;
5. vanishing total variation does not uniformly control a moving unbounded
   covector;
6. the boxed budget is sufficient and can fail when response exceeds target
   dissipation;
7. one bulk \(L^1\) error record admits distinct flux responses;
8. trace, marking, truncation, geometry, and kinetic residuals remain
   separately auditable;
9. external, exact-shadow, missing-theorem, conditional, rank, and API claims
   remain separately graded.

All values are exact rational numbers.  The computational cost is linear in
the number of event cells.  This measures only ledger arithmetic, not the
analytic cost of constructing the continuum measure.

## 7. Forbidden structures and red teams

The phase forbids:

- inferring a collision trace from bulk \(L^1\) convergence;
- replacing a continuum response measure by one discrete word letter per
  collision;
- recursively expanding the stopped \(f_A\) branch and attributing that move
  to Deng--Hani--Ma;
- calling \(I_M=I_{M_1}\circ I_{M_2}\) physical evolution or free molecule
  composition;
- pairing a bare \(L^1\) cumulant estimate with \(\log f\);
- hiding the covector tail or adapter errors in an unnamed \(o(1)\);
- treating observer order, molecule size, continuation depth, and arithmetic
  rank as one index;
- promoting a response fibre, generic calculus, partition tower, holonomy,
  or API.

Red teams include the bulk/flux nonidentifiability pair, the vanishing-TV
unbounded-covector family, a response that reverses target dissipation, and
separately signed residual axes whose cancellation would be invisible after
premature aggregation.

## 8. Kill conditions

The continuum transfer must be narrowed or rejected if:

- the actual and target currents do not live on the same event space and
  orientation convention;
- the proposed source route does not construct a finite flux measure;
- marking a collision destroys the molecule bounds without an explicit
  replacement budget;
- cutting is given a physical interpretation after the paper's stated
  correspondence has broken;
- the clipped estimate is not uniform in the declared horizon and molecule
  grammar;
- the logarithmic tail fails to vanish or remain within the target
  dissipation;
- a nonlinear entropy chain rule is assumed rather than proved;
- any independent conclusion from Phase 1J-A is used as continuum evidence.

## 9. Repository boundary

### Mathematical Core

Unchanged.  The phase isolates a problem-native sufficient response budget
and a missing flux-lift theorem.  It proves no generic measure response law or
cross-layer Lyapunov theorem.

### Engineering Architecture

Research-local refinement.  Continuum transfer is now ordered as source flux,
whole-measure response, clipped dual estimate, logarithmic tail, residual
budget, and only then an H claim.

### Theory Map

Unchanged.  The result sharpens T0/T1 pressure on the history-loss and
adaptation seams without objectifying molecules or raising arithmetic rank.

### API

No pressure.  The exact measure classes remain inside one executable essay.
