# Phase 1F contract — weak flux and one-collision continuation

**Status:** frozen weak/mild continuation contract with one exact rational
history shadow.  The continuum weak BBGKY identity, Duhamel series, and
Deng--Hani--Ma expansion remain external theorem records.  This phase proves
no continuum trace theorem, kinetic limit, long-time estimate, or H theorem.

**Executable owner:**
`tests/research/test_weak_collision_history_cell.py`.

**Result owner:**
`12-phase1f-weak-mild-continuation-cell-results.md`.

## 1. Correction to the target task

Phase 1E rejected

\[
\text{bulk }L^1\text{ convergence}
\Longrightarrow
\text{pointwise collision-generator convergence}.
\]

The correction is not to pretend that a weak formulation makes the collision
boundary disappear.  It changes the declared target from a pointwise trace to
a pairing with a time-integrated collision-flux measure.  The source adapter
must still supply that measure, either from a justified boundary trace or
directly from microscopic collision histories.

The refined dependency is

```text
microscopic hard-sphere law and collision events
    -> expected oriented collision-counting/flux measure
    -> weak observable pairing over a declared horizon
    -> one-collision Duhamel history cells
    -> partial expansion with an explicit stopping rule
    -> molecule lowering and Fubini cuts
    -> truncation, recollision, and geometry residuals
    -> autonomous Boltzmann target when a limiting theorem applies
    -> H/Lyapunov question
```

The weak and mild targets are therefore *adapted continuation tasks*, not
decoders for the complete microscopic future.

## 2. Weak collision-flux task

Let \(F_s(t,Z_s)\) denote a fixed-\(N\) hard-sphere marginal in a setting
where the weak BBGKY formulation is justified.  Let \(\phi_s(t,Z_s)\) be a
smooth compactly supported test function satisfying the elastic boundary
compatibility required for collisions among the \(s\) retained particles.
Then the weak identity has the form

\[
\begin{aligned}
&\langle F_s(T),\phi_s(T)\rangle
-\langle F_s(0),\phi_s(0)\rangle\\
={}&
\int_0^T
\left\langle
F_s,
\left(\partial_t+\sum_{i=1}^s v_i\cdot\nabla_{x_i}\right)\phi_s
\right\rangle dt
+\mathcal J_{s,T}^{\epsilon,N}[F_{s+1};\phi_s].
\end{aligned}
\]

Write \(q_i=\omega\cdot(u-v_i)\) and
\(\alpha_{N,s}=(N-s)\epsilon^{d-1}\).  The collision functional is

\[
\begin{aligned}
\mathcal J_{s,T}^{\epsilon,N}[F_{s+1};\phi_s]
={}&\alpha_{N,s}\sum_{i=1}^s
\int_0^T\int
q_i\,
F_{s+1}^{\mathrm{tr}}
(t,Z_s,x_i+\epsilon\omega,u)\\
&\hspace{42mm}\times
\phi_s(t,Z_s)
\,d\omega\,du\,dZ_s\,dt.
\end{aligned}
\]

Pointwise trace notation is only shorthand.  The more invariant object for
this task is an oriented finite measure \(\mu_{s,T}\) on collision events, or
its positive Jordan pair

\[
d\mu_{s,T}^{\pm}
=
\alpha_{N,s}\sum_i(q_i)_\pm
F_{s+1}^{\mathrm{tr}}
\,dt\,dZ_s\,d\omega\,du.
\]

For \(\phi_s\ge0\), define

\[
\mathcal A_{s,T}[\phi_s]=\int\phi_s\,d\mu^+_{s,T}\ge0,
\qquad
\mathcal L_{s,T}[\phi_s]=\int\phi_s\,d\mu^-_{s,T}\ge0.
\]

Then

\[
\mathcal J_{s,T}[\phi_s]
=
\mathcal A_{s,T}[\phi_s]-\mathcal L_{s,T}[\phi_s].
\]

This is a horizon- and observer-dependent gain/loss process pair.  It is not
the same object as the pointwise \((A_s,L_s)\) jet of Phase 1E.

### 2.1 Two legitimate source routes

The weak flux can be supplied in two separately typed ways.

1. **Trace route.**  Prove enough regularity or use a weak Green formula so
   that the boundary flux measure has the displayed density.
2. **History route.**  Begin with almost-everywhere hard-sphere trajectories,
   form the collision-event counting measure, average it over the microscopic
   law, and identify the result with the weak boundary flux under a declared
   theorem.

Neither route follows from bulk \(L^1\) state convergence alone.  Moving to a
weak observable changes the topology and the required source payload; it does
not erase the Phase 1E obstruction.

## 3. Mild hierarchy and the one-collision cell

Let \(T_s^\epsilon(t)\) denote the internal \(s\)-particle hard-sphere flow
operator, and let \(C_{s,s+1}^{\epsilon,N}\) be the collision insertion from
Phase 1E.  The mild hierarchy is

\[
F_s(t)
=
T_s^\epsilon(t)F_s(0)
+\int_0^t
T_s^\epsilon(t-\tau)
C_{s,s+1}^{\epsilon,N}F_{s+1}(\tau)
\,d\tau.
\]

Its first iterated collision term is

\[
Q_{s,1}^{\epsilon,N}(t)G_{s+1}
=
\int_0^t
T_s^\epsilon(t-\tau)
C_{s,s+1}^{\epsilon,N}
T_{s+1}^\epsilon(\tau)G_{s+1}
\,d\tau.
\]

For a fixed summand, a one-collision history cell carries

\[
h=(T,\tau,i,\omega,u,\sigma,Z_s),
\qquad \sigma\in\{+,-\},
\]

with the following operations:

```text
target root at time T
    -> backward internal flow to collision time tau
    -> choose retained label i, partner velocity u, and normal omega
    -> choose gain/loss orientation sigma
    -> on gain, cross the elastic collision involution
    -> insert the partner at contact x_i +/- epsilon omega
    -> backward (s + 1)-particle flow to the source time
    -> evaluate source data and the flux weight
    -> integrate tau, omega, u, labels, and orientations
```

The executable freezes \(s=1\), one rational \((\omega,u)\) quadrature node,
factorized source data, and free motion between the single collision and the
endpoints.  It checks the cell's algebra; it does not approximate the
continuum angular or velocity integrals.

### 3.1 What the cell preserves and forgets

The cell preserves:

- target endpoint and declared horizon;
- collision time, orientation, retained-particle label, normal, and partner
  velocity;
- contact displacement and elastic preimage;
- source evaluation and signed flux weight;
- composition order of the two free segments and collision insertion.

It forgets or omits:

- histories with zero, two, or more inserted particles unless separately
  included;
- additional collisions within the chosen interval;
- unselected microscopic labels and the rest of the ensemble;
- recollision geometry and exceptional sets;
- the truncation tail and any theorem comparing it to a kinetic solution.

Consequently

\[
F_s(t)
=Q_{s,0}(t)F_s(0)+Q_{s,1}(t)F_{s+1}(0)+R_{s,\ge2}(t)
\]

is a typed truncation ledger, not an assertion that \(R_{s,\ge2}=0\).

## 4. A/M under weak time integration

Suppose on a pointwise positive chart the loss has

\[
L(t,z)=F(t,z)\nu(t,z),
\qquad M(t,z)=-\nu(t,z).
\]

For a nonnegative weak observable \(\phi\), its integrated multiplicative
contribution is

\[
-\mathcal L_T[\phi]
=
\int_0^T\int \phi(t,z)F(t,z)M(t,z)\,dz\,dt.
\]

In general this is not recovered from the unweighted time average

\[
\overline M_T=\frac1T\int_0^T M(t)\,dt.
\]

If the denominator is positive, the scalar rate that exactly reproduces this
one weak task is instead

\[
M_{\phi,T}^{\mathrm{eff}}
=
\frac{\int\phi F M}{\int\phi F}.
\]

This effective rate depends on the observer, occupation measure, and horizon.
It is not the pointwise \(M\), not a canonical state coordinate, and not a
continuation-complete process.  Thus the following square does not commute
without additional structure:

```text
pointwise gain/loss --divide by state--> pointwise A/M
        |                                  |
        | integrate against phi            | unweighted time average
        v                                  v
weak gain/loss --------- generally not --> one observer-free A/M pair
```

Phase 1F therefore keeps weak gain/loss primitive.  Any effective A/M lowering
must name its occupation/reference measure and observer family.

## 5. Deng--Hani--Ma selective continuation translator

The long-time proof does not recursively expand every component to time zero.
At each layer \([(\ell-1)\tau,\ell\tau]\), it:

1. expands the cumulant \(E_H(\ell\tau)\) into Duhamel integrals involving
   \(f_A((\ell-1)\tau)\) and earlier cumulants;
2. stops on the leading \(f_A\) factors and compares them with the Boltzmann
   solution;
3. recursively expands only the earlier cumulant factors;
4. retains collision-history structure until molecule and geometric estimates
   certify the required \(L^1\) bound.

The stopping rule is part of the semantic adapter.  A full expansion of the
leading factors would reintroduce the uncontrolled combinatorial growth that
the construction is designed to avoid.

### 5.1 History-to-molecule lowering

For this calibration, the lowering

\[
\mathcal H_{\mathrm{collision}}
\longrightarrow
\mathcal M_{\mathrm{molecule}}
\]

retains collision/overlap atoms, particle lines, relevant labels, collision
order, roots, and time layers.  It forgets precise positions, velocities, and
collision times.  Some topological reductions may also select only a subset
of overlaps.  A molecule is therefore a task-oriented combinatorial shadow,
not the literal trajectory.

### 5.2 Cutting is an integral-composition certificate

When a molecule is cut into \(M_1\) and \(M_2\), the paper's identity

\[
I_M=I_{M_1}\circ I_{M_2}
\]

is Fubini's theorem with the cut-interface variables held fixed for the inner
integral.  It supplies:

- a compositional evaluation law;
- an order in which variables can be integrated;
- a proof-cost and estimate interface.

It does not by itself supply:

- physical time evolution of one molecule into another;
- a quotient with a complete microscopic decoder;
- free arithmetic composition or all-composite lowering;
- evidence that molecule depth is arithmetic rank.

The executable includes a finite rational double-sum shadow of this precise
Fubini claim.

## 6. Frozen adapter record

| field | Phase 1F value |
| --- | --- |
| source | hard-sphere trajectory law plus oriented collision-event measure |
| state readout | bulk correlation family, kept separate from flux data |
| continuation payload | collision time, label, orientation, normal, partner state, free segments |
| target task | weak collision observable or one Duhamel term |
| horizon | a declared finite interval \([0,T]\) |
| process presentation | integrated positive gain/loss; A/M only after a declared weighted lowering |
| topology | signed/positive measure pairing against a declared test class |
| exactness | exact algebra for one rational history shadow |
| continuum status | classical/Deng--Hani--Ma external theorem records |
| residual | omitted histories, truncation tail, recollisions, geometry, kinetic comparison error |
| reconstruction | source points for the selected cell only; no complete microscopic decoder |

## 7. Solver plan

```text
Problem and task:
  Replace an unsafe pointwise trace target by a weak/mild collision task.

Primitive process:
  Hard-sphere free/internal flow and oriented collision events.

Required lift:
  Collision time, normal, partner velocity, sign, label, and contact point.

Candidate presentation:
  Positive integrated gain/loss measure paired with a test observable.

Exact evaluator:
  Fraction-valued one-node, one-collision history with exact Simpson
  integration of degree-at-most-two source weights.

Certificates:
  Endpoint reconstruction, elastic contact, gain/loss positivity,
  time-cut additivity, Fubini composition, weighted-A/M obstruction.

Failure semantics:
  Bulk-only input, omitted trace/history measure, unweighted A/M averaging,
  missing truncation residual, molecule-as-rank overclaim.

Baseline:
  Classical weak BBGKY and iterated Duhamel formulas; Deng--Hani--Ma partial
  time expansion and cutting identity.

Budget:
  Exact research fixture under one second; no new dependency or API.
```

## 8. Kill conditions

Phase 1F must be revised if it:

- says the weak form removes the collision trace rather than integrating it;
- derives a flux measure from bulk \(L^1\) data without a trace/history theorem;
- calls the one-collision term the full mild solution without its tail;
- drops collision orientation or contact displacement from the history cell;
- averages pointwise \(M\) without naming the occupation and observer weight;
- calls \(M_{\phi,T}^{\mathrm{eff}}\) an observer-independent state variable;
- recursively expands Deng--Hani--Ma's stopped leading factors and still
  attributes the resulting object to their partial expansion;
- calls a molecule the literal collision history;
- reads \(I_M=I_{M_1}\circ I_{M_2}\) as physical evolution or arithmetic-rank
  objectification;
- reopens H before the complete target semigroup and validity horizon are
  fixed.

## 9. Repository effect

### Mathematical Core

**Refinement pressure only.**  Phase 1F supplies a concrete continuation
translator with an observer-weighted process lowering.  The existing
task/horizon/topology/error adapter language already covers it.  No stable
Core edit is proposed from this single kinetic domain.

### Engineering Architecture

**Refined research-locally.**  The solver contract now distinguishes bulk
state input, collision-event/flux input, weak observable, selected history
cells, and truncation residual.  No reusable backend or API is introduced.

### Theory Map

**Unchanged.**  The result supports the semantic-adaptation transversal and
provides a sharper composition/no-objectification boundary.  It creates no
new axis or arithmetic rank.

## Sources

- Y. Deng, Z. Hani, X. Ma, *Long time derivation of the Boltzmann equation
  from hard sphere dynamics*, arXiv:2408.07818v3, especially Sections
  1.3.2--1.3.4, 2.1--2.3, and equations (2.10)--(2.11),
  https://arxiv.org/abs/2408.07818
- I. Gallagher, L. Saint-Raymond, B. Texier, *From Newton to Boltzmann: hard
  spheres and short-range potentials*, especially equations (4.3.1)--(4.3.8)
  and (6.2.1), https://arxiv.org/abs/1208.5753
