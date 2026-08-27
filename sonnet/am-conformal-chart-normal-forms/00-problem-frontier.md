# AM Conformal Charts and Joint Normal Forms: Research Frontier

## Current status

- **Maturity:** T0/T1; the Phase 1 exact mechanism calibration is complete,
  while the economy and discovery claims remain unestablished.
- **Scope:** research-local under `sonnet/`; no change to the Mathematical
  Core, Theory Map, or Public API.
- **Strongest responsible claim:** Riccati scalar fields, two-dimensional
  projective lifts, Möbius charts and matrix conjugation, and scalar gauge close
  exactly over the rationals.  The projectivization of a constant-coefficient
  two-dimensional linear system produces a scalar field of degree at most two,
  so a generic nonzero cubic term is a neighboring no-go.  It has not been
  shown that the AM grammar can discover a chart superior to classical
  baselines, nor that it lowers the net computational cost of the pendulum or
  PCR3BP.

## 0. Inherited evidence and remaining obligations

Since this study was initialized, other research lines have completed several
prerequisites.  They provide reusable boundaries and calibrations; they are
not results about the joint normal form studied in this Sonnet.

| Source | Result that may be inherited | What this Sonnet must still prove |
| --- | --- | --- |
| pendulum marked-carrier / Mathematical Core | Cartesian first-principles entry; separate accounting for unit, clock, cover, and decoder | joint chart/module search and net cost |
| Boltzmann--BBGKY chart-first adapter | reversible same-layer charts must be separated from cross-layer task adapters | exact chart covariance within a fixed conformal atlas |
| Boltzmann--BBGKY contrast/odds audit | one chart may simplify dynamics while another simplifies the composition law | joint polynomial-like / matrix-like Pareto frontier |
| Phase 12C fibred change calculus | observer response after a chart change still has independent existence and coherence obligations | how chart selection changes response/evaluator cost |
| PCR3BP history-cost | word, clock, deck, and hyperbolic cost are accounted for separately | joint cost of a local atlas and variation/monodromy |

The main question posed in #119 has therefore not been superseded.  Phase 1
only calibrates the mechanism; Phases 2 and 3 must not re-prove the foundations
above or treat them as an economy theorem.

## 1. Problem-native statement

Process Geometry does not begin by rewriting a physical equation in different
notation.  It begins by choosing a presentation space that carries the
process, then projects process quantities to physical quantities through a
readout.  One physical quantity can typically be represented by two process
quantities; for example, in a projective chart,

$$
a=-\frac{x}{y}.
$$

The same physical readout may have different expressions in different charts.
We freeze the following working premise:

> On regular overlaps of the declared AM conformal atlas, chart transitions
> are conformal.  Chart selection may change coefficients, sparsity, singularity
> locations, bases, and numerical conditioning, but it cannot freely change the
> task, topology, moduli, single-valuedness data, or physical units.

The central question is this: given a physical task, an AM process
presentation, and its conformal atlas, is there a discoverable and certifiable
chart together with a finite module basis such that

1. the **polynomial-like part** becomes a low-complexity scalar carrier,
   coefficient system, or recurrence;
2. the **matrix-like part** becomes a low-complexity action table, transition
   matrix, or period basis;
3. both parts close under the same transformation law;
4. the physical readout, units, clock, and global reconstruction remain exactly
   correct; and
5. the total symbolic--numerical cost strictly improves on a credible baseline
   in the Pareto order.

This is not the question whether an arbitrary change of variables can make a
formula prettier.  It is a constrained joint-normal-form and
presentation-search problem.

## 2. Primitive objects and task semantics

Every instance must first freeze the following inputs:

- the primitive physical process or history language and the task whose
  observations are allowed;
- the AM process space $P$, its complex/conformal structure $J$, and the
  declared Addition/Multiplication actions;
- the physical readout $\pi:P\to X$ or task readout $\mathcal O$;
- regular domains, singular sets, boundaries, branch points, and marked points
  that must be retained;
- units and the ordered projective frame, especially transport of the physical
  unit $1$ in $(0,1,\infty)$;
- the baseline chart, baseline solver, accuracy, budget, and workload.

A candidate chart $\phi:U\to V$ is task-equivalent only when it is conformally
invertible on the declared domain and its lifted dynamics
$\widetilde F_\phi$ and the physical dynamics $F$ satisfy

$$
\pi_*\widetilde F_\phi=F.
$$

For a discrete process, use the corresponding commuting diagram or stepwise
readout identity.  The chart round trip, readout, units, clock, and branch
selection must all enter the certificate.

This exact round trip applies only to an invertible chart within one semantic
layer.  If the source and target states or continuation interfaces differ, use
the task-relative semantic adapter from the Mathematical Core and declare the
task, horizon, topology, error budget, residual, and closure.  Cross-layer
forgetting must not be disguised as a chart change.  A task quotient is a
third operation and requires an independent proof of continuation adequacy.

## 3. Five transformations that must remain separate

This Sonnet does not permit the following operations to be grouped under the
single phrase "change charts":

| Operation | Allowed effect | Structure requiring separate accounting |
| --- | --- | --- |
| conformal chart transition | rewrite local coordinates on a regular overlap | atlas switching, singularities, units, and decoder |
| projective/Möbius transformation | rearrange a projective frame and finitely many marked points | cross-ratios, physical unit, and the point at infinity |
| module-basis or gauge transformation | conjugate/rewrite a matrix-like action | basis reconstruction and condition number |
| ramified cover | make a quantity single-valued or regularize a collision | covering degree, deck data, and branch selection |
| time reparameterization | change the integration clock | physical-time reconstruction and cost |

A task quotient is not a chart transition either: it may forget history
information and must be justified independently by task equivalence.

## 4. Candidate joint normal form

A candidate is a tuple

$$
\mathfrak N=(\phi,\,\mathcal B,\,p,\,R,\,D),
$$

where $\phi$ is a chart, $\mathcal B$ is a finite module basis, $p$ is
polynomial-like scalar data, $R$ is matrix-like action data, and $D$ is the
physical decoder.  Ideally, the chart and basis transformations act jointly as

$$
p\mapsto p^{\phi},
\qquad
R\mapsto G^{-1}R^{\phi}G-G^{-1}\dot G,
$$

where the derivative term is present or absent according to whether the task
concerns an algebraic action, a differential equation, or a connection.  This
formula is only a candidate transformation contract.  Each phase must derive
it anew from the concrete primitive process; it must not be treated as a
general theorem.

### 4.1 Polynomial-like

This provisionally means a scalar carrier describable in the chosen chart by
finite generation, low degree, or low recurrence complexity, including the
exponential--polynomial weight chain already present in AM function theory.  It
is not the same as an ordinary polynomial, and it does not assume that every
task lies in a finite-dimensional chain.

### 4.2 Matrix-like

This provisionally means a finite action table for several process components,
local bases, or period/monodromy data.  It records more than the linear
combinations induced by commutativity of Addition: it must also record how the
chart, gauge, cover, and decoder transform the table.

### 4.3 Joint rather than separate minimization

Minimizing only the degree of $p$ may make $R$ dense, the decoder expensive,
or the number of charts larger.  Diagonalizing only $R$ may introduce branch
functions, poor conditioning, or broken physical units.  The normal form
therefore uses a cost vector rather than one "shortest formula":

$$
C(\mathfrak N)=(
C_{\rm coeff},
C_{\rm action},
C_{\rm singular},
C_{\rm atlas},
C_{\rm decoder},
C_{\rm unit},
C_{\rm eval},
C_{\rm residual}
).
$$

Report only the Pareto frontier unless the workload supplies weights.

## 5. Search discipline

### 5.1 Native language first

Search first among candidates generated by primitive Addition/Multiplication
actions, task-visible marked points, and a finite chart grammar.  Only then
compare with an unrestricted search over classical transformations.  Do not
solve the problem first and then package the classical answer as a
"discovery."

### 5.2 Oracle firewall

- Legendre forms, elliptic functions, period ratios, Levi--Civita maps, and
  other known answers may be used as post-hoc oracles and baselines.
- Unless a phase explicitly declares them as inputs, do not feed their
  parameters, branch-point pairings, period bases, or regularizing maps to the
  proposal generator.
- Candidate generation, scoring, verification, and oracle comparison must have
  an auditable boundary.

### 5.3 Bounded grammar

"All conformal maps" is not an executable search space.  Phase 0 must freeze a
finite or enumerable grammar, for example one generated by finite AM actions,
task-visible marks, low-height Möbius transformations, and declared local
chart compositions.  Any grammar expansion must be recorded as a new
experimental phase rather than selected after the result is known.

## 6. First calibration: projective/Riccati prototype

If

$$
a=-\frac{x}{y},
\qquad
\dot a=c_0+c_1a+c_2a^2,
$$

then the classical two-dimensional lift

$$
\frac{d}{dt}
\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}
c_1/2 & -c_0\\
c_2 & -c_1/2
\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
$$

recovers the same Riccati equation on $y\neq0$; adding a scalar matrix
$\gamma I$ does not change the projective readout.  This example calibrates
only four things:

- how two process quantities read out as one physical quantity;
- how polynomial-like coefficients enter a matrix-like action;
- how a Möbius chart and matrix conjugation fit together; and
- why scalar gauge is presentational redundancy rather than new physics.

It is a positive control from standard theory, not a new AM discovery.  A
cubic scalar field is the neighboring red team that blocks the unwarranted
inference that every nonlinearity can be linearized in two dimensions.

## 7. Second calibration: the pendulum

The pendulum must begin from the existing first-principles route: Cartesian
primitive quantities and physical constraints come first, and only then is a
task carrier formed.  The current comparable baseline is

$$
Y^2=2(E-U)(1-U^2),
\qquad
dt=\frac{dU}{Y}.
$$

The research question is not to announce a Legendre transformation in
advance, but to test whether

1. a restricted grammar can discover a low-cost conformal chart from
   task-visible branch and marked-point data;
2. the chart jointly simplifies the polynomial-like carrier and the
   period/module basis;
3. the added costs of physical units, clock, branches, and decoder cancel the
   apparent simplification;
4. the square-period case at $E=0$ can serve as an exact calibration without
   leaking $\tau=i$ to the proposal generator; and
5. equilibria, ordinary oscillations, rotations, and the degenerate
   separatrix regime require different atlases rather than one falsely global
   chart.

Cross-ratios, the $j$-invariant, period lattices, and monodromy are candidate
residuals that cannot be removed freely by a chart.  This Sonnet must use
certificates to determine their actual role in task cost.

## 8. Third calibration: the planar circular restricted three-body problem

PCR3BP is an independent stress test, not a decorative application of a
pendulum result.  Each experiment must first declare a local region and task,
such as short-time propagation, a Poincaré return, or a near-collision segment,
then compare

- baseline physical/rotating coordinates;
- a pure conformal chart change;
- a separately recorded ramified cover when necessary;
- a separately recorded time reparameterization when necessary; and
- the joint cost of polynomial-like local coefficients and a matrix-like
  variation/monodromy table.

Collision regularization must not be credited secretly as a benefit of a
Möbius chart, and a local chart improvement must not be used to infer global
integrability.  The existing
[`pcr3bp-history-cost/`](../pcr3bp-history-cost/) Sonnet independently records
word, clock, deck, and hyperbolic cost.  The two research lines remain separate
until they have a common certificate.

## 9. Falsifiable hypotheses

- **H1 — chart covariance:** every admissible candidate has exact readout,
  unit, clock, and round-trip certificates.
- **H2 — effective simplification:** at least one nontrivial task admits a
  strict Pareto improvement rather than merely a shorter character string.
- **H3 — joint normal form:** the scalar carrier and finite action table must
  be selected jointly; separate minima are generally not a joint minimum.
- **H4 — conformal residual:** moduli, cross-ratios, periods, monodromy, or the
  marked unit form task-relative residuals that a chart cannot remove.
- **H5 — locality boundary:** for PCR3BP, the best object is more likely a
  task-local atlas than one global normal chart.

## 10. Kill conditions and red teams

Any of the following must narrow or close the corresponding claim:

- the alleged simplification reduces only notation length while increasing
  decoder, atlas, branch, or numerical cost;
- a candidate is not conformal or injective on the task domain, or disguises a
  cover or time change as a chart;
- a transported unit is reset to $1$ without charging for the additional
  normalization;
- the physical readout, clock, or task-equivalence diagram fails to commute;
- a singularity is moved outside the current coordinate patch and then no
  longer tracked;
- the proposal generator gains access to a frozen classical answer;
- the advantage comes only from ordinary Möbius normalization, with no added
  contribution from the native AM grammar;
- a local improvement is used improperly to infer a global normal form,
  global integrability, or disappearance of topology; or
- under matched budgets, the native AM search remains inferior to the
  baseline.  A negative result must still be retained.

## 11. Certificate requirements

Every phase must provide at least

- the chart domain, overlaps, Jacobian/conformality, and round-trip
  certificates;
- pushforward/pullback identities for process actions;
- certificates for the physical readout, units, clock, branches, and decoder;
- transformation certificates for the polynomial-like carrier and matrix-like
  action;
- a control baseline, frozen budget, full cost vector, and Pareto comparison;
- red teams for singularities, degenerate regimes, bad conditioning, and
  cross-chart switching; and
- discovery-input logs and an audit of the oracle firewall.

## 12. Theory and engineering impact boundary

If successful, the calibration may refine presentation search, unit
covariance, observers/decoders, and effective analysis in the Mathematical
Core.  It may also add a research-local schema for conformal atlases and joint
module cost to the Engineering Architecture.

The Theory Map is unchanged at present: this study remains T0/T1, horizontal,
and local.  An extraction candidate may be proposed only after at least two
independent problem classes among Riccati, the pendulum, and PCR3BP force the
same interface and the precision, calibration, abstraction, and foundation
gates have been passed.  Any Public API must still mature through Experimental.
