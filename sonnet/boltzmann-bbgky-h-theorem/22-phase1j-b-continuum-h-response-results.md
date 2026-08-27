# Phase 1J-B results — the missing theorem is a marked-molecule flux lift

**Verdict:** Phase 1J-B passes as a sharp continuum transfer contract and
finite exact obstruction result.  It does not pass as a continuum H-response
estimate.  Deng--Hani--Ma provide the bulk cumulant/molecule control needed to
motivate the source expansion, but their stated theorems do not construct the
collision-current response measure or control its pairing with the
logarithmic Boltzmann affinity.

**Contract:**
[21-phase1j-b-continuum-h-response-contract.md](./21-phase1j-b-continuum-h-response-contract.md).

**Executable:**
[test_continuum_collision_flux_response_budget.py](../../tests/research/test_continuum_collision_flux_response_budget.py).

## 1. What was established

The continuum target is now a signed response measure

\[
\nu_T^\epsilon=J_T^\epsilon-J_T[f]
\]

on one declared collision-event space, rather than a pointwise trace or a
discrete collision word.  For an admitted weak covector \(\psi\), its exact
semantic obligation is

\[
\langle J_T^\epsilon,\psi\rangle
=\langle J_T[f],\psi\rangle
+\langle\nu_T^\epsilon,\psi\rangle.
\]

For the H covector \(\psi_f=-\frac14\log(g'/g)\), clipping at level \(K\)
gives the exact sufficient response budget

\[
|\langle\nu_T^\epsilon,\psi_f\rangle|
\le
K\|\nu_T^\epsilon\|_{\mathrm{TV}}
+\int|\psi_f-\psi_f^K|\,d|\nu_T^\epsilon|.
\]

After adding the separately typed trace, marking, truncation, geometry, and
kinetic-comparison budgets, target H dissipation transfers whenever their
total is no larger than \(\mathcal D_T[f]\).  This is a conditional sufficient
criterion.  It does not assert that the required measure, chain rule, or
bounds currently exist.

## 2. Exact executable evidence

The frozen rational fixture has three cells of a collision-event test
partition.  Its response current has total variation \(7/16\), and its
pairing with the declared H-test shadow is \(23/16\).  At clipping level
\(K=2\):

- the clipped total-variation term is \(7/8\);
- the exact tail overshoot is \(9/16\);
- their sum is \(23/16\);
- the five-axis residual budget in the transfer fixture is \(1/8\);
- the total error budget is \(25/16\).

Target dissipation \(2\) certifies a negative adapted increment
\(-43/80\).  Reducing target dissipation to \(1\) leaves the same response and
errors but produces the positive increment \(37/80\).  Target monotonicity is
therefore not inherited without a quantitative response budget.

The unbounded-covector red team uses response masses
\(1/2,1/4,1/8,1/16\) and covector values \(2,4,8,16\).  Total variation tends
to zero while every pairing remains exactly one.  No estimate of the form

\[
\|\nu^\epsilon\|_{\mathrm{TV}}\to0
\quad\Longrightarrow\quad
\langle\nu^\epsilon,\psi^\epsilon\rangle\to0
\]

is valid for a moving unbounded covector family without a tail or uniform
integrability hypothesis.

The targeted run is:

    9 passed in 0.05s

## 3. What the primary theorem does and does not transfer

The audit of Deng--Hani--Ma yields the following claim grades.

| Object | Grade in this Sonnet | Reason |
| --- | --- | --- |
| Theorem 1 / equation (1.18) | external bulk-state adapter theorem | topology is bulk \(L^1\), uniformly over the stated horizon and particle orders |
| Proposition 3.25 | external bulk cumulant/molecule decomposition | estimates \(f_s\), \(E_H\), and error functions, not a contact-event measure |
| Proposition 6.2 | external bulk \(L^1\) estimate | no logarithmic collision covector or trace norm appears |
| Proposition 8.14 | external exact integration identity | its proof is Fubini plus variable identification |
| molecule cut as physical composition | rejected | the paper explicitly says the molecular/physical correspondence breaks after cutting |
| collision-flux response estimate | missing theorem | no trace/history pushforward into the Phase 1F weak flux topology is supplied |
| continuum H transfer | conditional contract only | needs flux lift, entropy chain rule, bounded test estimate, and tail control |

This blocks two tempting but invalid shortcuts:

1. bulk \(L^1\) smallness of \(E_H\) cannot be restricted to contact for
   free; and
2. the exact cut identity cannot be promoted from an estimation operator to
   physical molecule composition or arithmetic-rank evidence.

## 4. The next theorem-sized target

The highest-value next step is not a larger entropy search.  It is the
bounded, marked collision-flux theorem below.

### 4.1 Mark before cutting

For every pre-cut molecule \(M\), mark a root-visible collision atom \(n\).
Push the corresponding prescribed-dynamics integral forward to the physical
collision-event space before the paper's molecular/physical correspondence
is lost.  Denote the resulting measure by \(\kappa_{M,n}\).

The mark then travels through a cut only as an observable in an iterated
integral.  Proposition 8.14 may reorganize that integral; it does not make the
cut pieces physical histories.

### 4.2 Prove the bounded dual estimate first

For fixed \(K\) and \(T\), seek

\[
\sup_{\|\psi\|_\infty\le K}
\left|
\left\langle
\sum_{M,n}\kappa_{M,n}+\nu_{\mathrm{err}},\psi
\right\rangle
\right|
\le \eta_K(\epsilon,T),
\qquad
\eta_K(\epsilon,T)\to0.
\]

The estimate must display the cost of the mark, for example the number of
eligible C-atoms, together with molecule count, recollision rank, layer,
truncation, and contact-geometry factors.  Whether the existing molecule gain
absorbs that marking cost is an open analytic question, not assumed here.

### 4.3 Remove or retain the clip honestly

Only after the bounded theorem is available should one attempt

\[
\lim_{K\to\infty}
\sup_{\epsilon}
\int|\psi_f-\psi_f^K|\,d|\nu_T^\epsilon|=0.
\]

Possible routes include a positive lower bound on the tested compact region,
a weighted collision-flux estimate, or a renormalized clipped entropy task.
The contract does not choose among them without evidence.

## 5. Claim boundary

Phase 1J-B has earned:

- a topology-correct whole-response-measure target;
- an exact clipped/tail H-response budget;
- an exact obstruction to controlling a moving unbounded covector by total
  variation alone;
- a primary-source separation of bulk cumulant estimates, molecule cuts,
  physical histories, and weak collision flux;
- a theorem-sized next target with the marking operation placed before
  cutting.

It has not earned:

- construction of \(\nu_T^\epsilon\) from Deng molecules;
- a trace theorem or history/flux identification;
- a marked-molecule estimate;
- removal of the logarithmic clip;
- a nonlinear entropy chain rule for the microscopic marginal;
- a continuum or microscopic H theorem;
- molecule objectification, a response cocycle, arithmetic-rank promotion,
  or a generic API.

Phase 1J-A remains an independent branch of the programme.  None of its
finite collision-response conclusions is used here.

## 6. Repository effect

### Mathematical Core

Unchanged.  The finite measure inequality is classical duality used as a
problem-local certificate.  The research contribution is the precise
placement of the missing flux-lift and tail obligations.

### Engineering Architecture

Refined research-locally.  A future continuum evaluator must expose a source
flux route, event-space orientation, response measure, clipping level, tail,
and residual axes.  A single bulk error scalar is insufficient.

### Theory Map

Unchanged.  The result strengthens the adaptation-seam obstruction and the
T0/T1 evidence ledger without adding a V2 object or V5 calculus.

### API

No pressure.  The exact classes remain executable documentation only.
