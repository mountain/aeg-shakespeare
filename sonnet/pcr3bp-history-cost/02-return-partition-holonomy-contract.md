# PCR3BP Phase 2 contract: return, partition, and holonomy

**Status:** frozen experiment contract; no Phase 2 numerical result is claimed.
Phase 0 and Phase 1 remain complete calibrations and are not retrospectively
rewritten by this note.

**Theory prerequisite:**
`docs/63-thermodynamic-objectification-and-partition-towers.md`.

## 1. Why Phase 2 has been redefined

The original continuation suggested a Poincare return kernel and then a
possible Bellman/Huffman task.  The thermodynamic-objectification audit changes
the center of gravity:

```text
old emphasis     return data -> possible control/coding problem
new emphasis     return process -> partition pushforward -> holonomy loss audit
```

The uncontrolled PCR3BP has no native action set, so manufacturing a control
problem now would mix physical dynamics with an arbitrary intervention model.
A return ensemble, roof cost, and twisted transfer calibration require no such
invention.  They directly test which proposed process-geometry coordinates are
independent:

\[
\text{free lifted carrier},\quad
\text{dynamical pruning},\quad
\text{cost character},\quad
\text{task quotient},\quad
\text{holonomy payload},\quad
\text{flattening obstruction}.
\]

Bellman and Huffman are therefore downstream branches.  They become legitimate
only after an action/task and a continuation-stable finite source are declared.

## 2. Completed baseline and unresolved interface

Phase 0 established one costed free-group history census at

```text
mu = 0.1,       C = 3.55 < C1,
```

using two upward vertical cuts from the primaries.  Phase 1 established local
state reconstruction from the Kepler scale jet and used two outward horizontal
axis rays to calibrate synthetic based loops and the Bellman-state boundary.

The two gate systems are both valid presentations of the twice-punctured
configuration plane, but their comparison has not been constructed.  Their
words, transition matrices, and spectra must not be mixed as though the
generator names were literally identical.

This unresolved presentation interface is the first Phase 2 gate, not a minor
plotting choice.

## 3. Primitive process and forbidden imports

The physical process remains the dimensionless rotating-frame PCR3BP vector
field and Jacobi oracle from Phase 0.  No projection to a constant-Jacobi leaf
is allowed during integration.  Every accepted trajectory carries its measured
maximum Jacobi drift.

The local observer state remains the Phase 1 scale jet

\[
(u_1,u_2,\beta_1,\beta_2,\text{orientation},C),
\]

which reconstructs the physical section state under the stated regularity
conditions.

The first implementation must not import as an oracle:

- a known Markov partition or symbolic itinerary;
- a periodic-orbit catalogue;
- an `SL(2)` observer connection inserted independently of the gate history;
- a controller, reward, or action set chosen only to make Bellman applicable;
- a stationary probability measure inferred from one finite trajectory;
- a continuous-flow Ruelle zeta interpretation.

Numerical integration, event localization, finite quadrature/Ulam bins, and
the already declared `Gamma(2)` deck comparison are admissible presentations,
not ontology.

## 4. Frozen section and ensemble

Keep

\[
\mu=0.1,
\qquad
p_1=(-\mu,0),
\qquad
p_2=(1-\mu,0),
\]

and compute \(C_1\) from the existing exact numerical oracle.  The first
three Jacobi levels are

\[
\mathcal C=
\{3.55,\ C_1-0.01,\ C_1+0.01\}.
\]

They retain the Phase-0 open-neck value, add a near-threshold open value, and
add a near-threshold closed value.  The singular level \(C=C_1\) is excluded
from the convergence gate because its separatrix can produce unbounded return
times; it may be studied later as a separate limiting experiment.

For each \(C\), use the oriented section

\[
\Sigma_C=
\{y=0,\ \dot y>0,\ x\in[p_1+0.03,p_2-0.03]\}.
\]

Parameterize the admissible part by \((x,s)\), where

\[
v(C,x)=\sqrt{2\Omega(x,0)-C},
\qquad
v_x=s\,v(C,x),
\qquad
v_y=\sqrt{1-s^2}\,v(C,x),
\]

with \(s\in[-0.9,0.9]\) and only points satisfying
\(2\Omega(x,0)-C>0\).  At the closed-neck level, the admissible section may
split into components; that split is data and must not be filled by
interpolation.

The pilot grids are cell-centered midpoint tensor grids `16 x 16` and
`32 x 32` in `(x,s)` before admissibility filtering.  For `N x N`, use

\[
\Delta x=\frac{p_2-p_1-0.06}{N},
\qquad
\Delta s=\frac{1.8}{N},
\]

and the corresponding half-cell-shifted nodes.  Every admissible node has raw
reference weight \(\Delta x\Delta s\); the raw section volume is the sum of
those weights, and normalized probability divides by that sum.  A `64 x 64`
grid is a manually dispatched refinement only if the first two fail to
stabilize the reported quantities.  Default CI must use small semantic
fixtures, not the full integrations.

Both raw quadrature mass and normalized probability must be stored.  Mapping
points into scale-jet cells pushes these `(x,s)` weights forward; it must not
reset a new uniform measure in scale coordinates.  Partition functions from
different Jacobi levels may be compared as separately declared normalized
conditional ensembles; any comparison of absolute/raw partition mass must
retain the reference-volume factor.

The `N x N` midpoint grid is a **microquadrature**, not automatically the
finite-state partition.  Aggregate it into `M x M` section macrocells with
`(N,M)=(16,4)` and `(32,4)` to test sampling refinement at fixed cells, then
use `(32,8)` to test cell refinement.  The optional `(64,8)` run is required
before interpreting an unstable `(32,8)` result.  Empty or forbidden
macrocells are omitted with their raw reference mass recorded.

At the closed-neck level, the actual state label is

\[
(\text{rectangular macrocell},\ \text{connected admissible component}).
\]

A rectangle crossing the forbidden `L1` gap therefore produces two labels
rather than reconnecting the two physical section components.  Occupancy,
base-path corrections, and every common refinement use this component-aware
label.

## 5. First-event return record

For a run with maximum step \(h\), arm the return detector only after the
trajectory has entered \(y<-h^2\); this excludes the initial point without
charging an arbitrary clock deadband and shrinks with the event tolerance.  A
candidate near-return that crosses the numerical section without first
clearing this band is `ambiguous`, not a return.  Then integrate until exactly
one terminal event:

1. **return** — the next transverse crossing of `y=0` with `v_y>0`;
2. **collision-1 / collision-2** — the corresponding primary distance reaches
   the existing guard radius `0.015`;
3. **escape** — radius reaches the existing guard `4.0` with outward radial
   velocity;
4. **timeout / no-return** — dimensionless clock reaches `60`;
5. **ambiguous** — grazing, simultaneous, or refinement-unstable event.

Ambiguous samples are reported with their quadrature mass and excluded from
claimed invariant comparisons.  They must not be silently assigned to the
nearest event.

Every record contains:

```text
Jacobi level C
initial (x,s) and quadrature weight
initial and terminal physical state
initial and terminal scale jet
terminal event and dimensionless roof time tau = t_event - t_initial
event bracket and interpolation fraction defining t_event
raw and reduced word in each gate presentation
deck matrix / declared representation payload
minimum primary distance
maximum Jacobi drift
step/event tolerances and refinement identity
```

For absorbing outcomes the recorded word is an open prefix, not a closed-cycle
class.  Only true returns enter a return-to-return cycle determinant.

### 5.1 Multi-return continuation records

The one-step table supplies the Ulam return map.  The state-sufficiency audit
also needs past information, so every returned pilot sample is continued until
the first absorption, eight accepted returns, or cumulative clock `60`,
whichever comes first.  At the start of each edge, freeze the reduced
chronological word accumulated **before** that edge.  Word-only predictors use
past suffix lengths `1`, `2`, and `4`; they never inspect the outgoing edge
word.  The initial edge has an empty past suffix and is not used to claim
word-only predictive power.

Training and held-out data are split by complete initial-condition chains, not
by individual edges, so later edges from one physical history cannot leak into
both sets.  For zero-based midpoint-grid indices `(i,j)`, the frozen holdout is
`(i + 3*j) % 5 == 0`; every edge descended from that initial point remains in
the same split.

## 6. Mandatory two-gate presentation audit

Call the Phase-0 vertical cuts \(G_0\) and the Phase-1 outward rays \(G_1\).
The same numerically converged trajectory must be observed by both gate
systems before any finite quotient is fitted.

The comparison target is not literal word equality.  Search for:

- a free-group automorphism \(\phi:F_2\to F_2\) determined first on synthetic
  based generator loops;
- section-cell base-path corrections \(b_i\in F_2\);
- a common refinement of section cells when the two presentations place an
  endpoint on different observer boundaries.

For an edge \(e:i\to j\), the auditable change-of-presentation law is

\[
g_e^{(1)}
=b_i^{-1}\,\phi(g_e^{(0)})\,b_j.
\]

This convention matches the repository's chronological right-appending word
and matrix products, so the intermediate \(b_j\) factors telescope.  On a
closed cycle, the product therefore changes by the generator
reparameterization and a conjugacy, so an appropriately transformed character
is invariant.

The representation must transform with the generators.  If \(\rho_0\) is the
declared representation in the `G0` basis, use

\[
\rho_1=\rho_0\circ\phi^{-1},
\qquad
B_i=\rho_1(b_i).
\]

For identical physical edges, roof weights, and common-refinement cells, the
block matrices must then satisfy

\[
K_1=D^{-1}K_0D,
\qquad
D=\operatorname{diag}(B_i).
\]

This is the similarity law that permits trace and determinant comparison.
Reusing the same numerical `Gamma(2)` generator matrices under a nontrivial
\(\phi\) without this precomposition is an invalid comparison.

If no stable \(\phi\), finite endpoint coboundary, and transformed
representation explain the two gate records under grid/tolerance refinement,
then:

- word-level quantities remain presentation-relative;
- the proposed twisted spectra do not pass the Phase 2 claim gate;
- the experiment stops before a process-geometry classification claim.

Synthetic loops alone are necessary but insufficient.  The relation must also
hold on the physical return ensemble, including mixed histories.

## 7. Numerical convergence gate

Use the existing distance-adapted RK4 implementation as the baseline and add
event bracketing/interpolation without projecting the state.  For every sample
used in a theorem-shaped table, compare the schedules

```text
max_step h       = 1e-3, 5e-4, 2.5e-4
min_step         = h/32
section/gate root tolerance and return-arm band = h^2
```

The existing fixed `5e-5` minimum step is not used for this gate: near the
`0.015` collision guard it would dominate all three runs and create a false
refinement.  Event/root tolerances and the minimum step therefore shrink with
\(h\), and the recorded actual steps must confirm that a common floor did not
control the two finest trajectories.

An accepted record requires:

- identical terminal-event class at the two finest resolutions;
- identical reduced words in both gate presentations at the two finest
  resolutions;
- roof-time change at most `1e-4 * max(1,tau)`;
- maximum Jacobi drift below `1e-7` at both finest resolutions;
- no unresolved grazing or simultaneous gate/section event.

These thresholds are experiment gates, not claims of a symplectic or rigorous
integrator.  A record failing the Jacobi bound is unresolved and excluded; an
additional refinement study may diagnose the failure but does not waive the
gate.  If more than five percent of the normalized ensemble mass is ambiguous
or unresolved at either of the two near-threshold levels, stop and improve
event regularization before increasing the orbit count.

## 8. Finite return representations

The first finite object is a **sub-Markov empirical/Ulam return graph**, not a
claimed Markov partition.  Return macrocells use the `(N,M)` schedule above and
the reconstructing section state or its scale-jet equivalent.  Multiple
microquadrature histories contribute to each populated source macrocell;
absorbing outcomes carry the missing row mass.

Keep two weights distinct:

- \(\omega_h\) is the normalized initial-section quadrature mass used to
  integrate stopping observables;
- \(p_e=P(e\mid i)\) is the source-cell conditional transition mass used in
  a return-kernel row.

For each source cell, conditional masses over return edges, physical absorbing
outcomes, and an ambiguous/unresolved diagnostic sink sum to one.  Removing
all non-return columns makes the return-only matrix sub-Markov.  A separately
reported nonambiguous-conditioned kernel may renormalize after deleting the
diagnostic sink, but it must not be confused with the raw row.  Initial
source-cell mass must not be inserted again into every matrix step; doing so
would make cycle coefficients depend spuriously on the sampling-grid cell
volume.

The one-step Ulam rows use only the midpoint microquadrature launched from the
section.  The later edges of the multi-return chains are reserved for the
continuation/state audit and are not silently treated as fresh independent
section samples.  For a held-out prediction table, a source macrocell must
contain at least eight training chains and two held-out chains.  Report the raw
and normalized mass of cells below this occupancy.  If that mass exceeds five
percent, increase `N` at fixed `M` (or reject that `M`); do not repair the claim
with an unreported data-dependent cell merge.

Compare three state languages on held-out continuation edges:

```text
word suffix only
scale-jet/section cell only
scale-jet cell plus deck residual
```

For each language, report prediction of:

- return versus each absorbing outcome;
- next return cell;
- roof-time mean and variance;
- next gate/deck payload at the declared character resolution.

The word-only failure already found in Phase 1 is a required negative control.
A finite cell language may be called an **approximate continuation-stable
quotient** only if held-out discrepancies decrease under both sample and cell
refinement.  If the required cell count grows without stabilization, retain a
continuous-state transfer problem and do not introduce a finite Huffman source.

## 9. Partition and holonomy observables

For a declared terminal task \(Q\) and normalized initial weights
\(\omega_h\), the finite stopping partition is

\[
Z_Q(\beta)=
\sum_{h:\,Q(h)}\omega_h e^{-\beta\tau_h}.
\]

At \(\beta=0\), the raw physical terminal-outcome masses plus the separately
listed ambiguous/unresolved mass \(M_{\mathrm{amb}}\) must sum to one.  Let
\(A\) be the union of accepted physical outcomes.  Then

\[
Z_A^{\mathrm{raw}}(0)=1-M_{\mathrm{amb}},
\qquad
\overline Z_A(\beta)
=\frac{Z_A^{\mathrm{raw}}(\beta)}{1-M_{\mathrm{amb}}}.
\]

Frontier/coarea comparisons use the conditional accepted-history weights in
\(\overline Z_A\); the raw accepted mass is reported separately.  More
generally, write \(M_Q=Z_Q(0)>0\) for one accepted outcome subset.  Then

\[
-\partial_\beta\log Z_Q(0)
=\frac{1}{M_Q}\sum_{h:\,Q(h)}\omega_h\tau_h
\]

is its conditional mean roof, not its raw first moment.  Only the explicitly
conditioned \(\overline Z_A\) is normalized to mass one and compared directly
with the conditional weighted roof cost and the finite frontier identity from
`docs/62-task-covariant-complexity-coarea.md` and
`docs/63-thermodynamic-objectification-and-partition-towers.md`.

For \(M_Q=0\), report the zero mass; its logarithm and conditional derivative
are undefined.

For return cells \(i,j\), define the finite twisted block matrix

\[
K_{\beta,\rho}(i,j)
=\sum_{e:i\to j}
p_e e^{-\beta\tau_e}\rho(g_e),
\]

where \(p_e=P(e\mid i)\) is the conditional Ulam/empirical edge mass.  Every
table must state its source-cell normalization and its absorbing row defect.
Compare:

1. the trivial scalar representation;
2. at least one task-motivated abelian/sign character;
3. the two-dimensional `Gamma(2)` deck representation used in the finite
   theory calibration.

The research question is information loss:

> Which return histories merge under scalar partition data but remain
> distinguishable under a task-visible representation?

For each finite matrix, the formal coefficients of

\[
\det(I-zK_{\beta,\rho})^{-1}
=\exp\left(
\sum_{n\ge1}\frac{z^n}{n}\operatorname{Tr}K_{\beta,\rho}^n
\right)
\]

are auditable finite-graph quantities.  They are not called the PCR3BP Ruelle
zeta function.  If reduced words are the intended cycle objects, immediate
inverse cancellations must be removed by a last-symbol/nonbacktracking lift
rather than by using the ordinary adjacency matrix.

## 10. Cost axes and discretization

Keep the following axes separate:

```text
physical roof cost tau
raw and reduced gate count
deck-character / hyperbolic translation data
section-cell resolution
ensemble/reference weight
numerical integration and event-localization cost
```

A declared roof unit \(u\) may produce the exact pair

\[
(\lfloor\tau/u\rfloor,\ \tau\bmod u),
\]

with the carry law from `docs/63`.  The integer bin alone is not an additive
cost unless all accepted roofs lie on the same lattice or the residual is
task-invisible at the declared tolerance.

## 11. Phase gates

### Phase 2A — presentation and event layer

Deliver:

- one integrator path observed simultaneously by `G0` and `G1`;
- synthetic-loop generator map plus physical-ensemble coboundary audit;
- converged return/absorbing records at the `16 x 16` pilot resolution.

Exit only if event classes, roof costs, and both gate records are stable under
the numerical refinement gate.

### Phase 2B — finite return and partition layer

Deliver:

- the `(16,4)`, `(32,4)`, and `(32,8)` microgrid/macrocell sub-Markov return
  graphs;
- source-cell train/holdout occupancy and low-occupancy mass ledger;
- held-out comparison of word, scale-jet, and combined state languages;
- scalar stopping partitions and exact derivative/direct-cost agreement;
- ambiguous and absorbing mass ledger.

Exit only if the reported task quantities stabilize under grid refinement or
the result explicitly concludes that the finite quotient failed.

### Phase 2C — holonomy and cycle layer

Deliver:

- trivial, abelian/sign, and `Gamma(2)` twisted matrices;
- finite trace-power enumeration and determinant coefficients;
- two-gate covariance comparison;
- a scalarization red team with histories merged by scalar data and separated
  by the declared task character.

Exit only if the gate comparison law survives.  Otherwise retain the result
as a presentation-relative negative calibration.

### Later, separate branches

- A controlled Bellman problem requires a physically stated action set,
  transition law, cost, and terminal task.
- Huffman requires a continuation-stable finite source with stable conditional
  probabilities and a declared code cost.
- Periodic-orbit cycle expansions require independent hyperbolicity,
  convergence, and completeness evidence.

None of these branches blocks Phase 2A--2C.

## 12. Red teams and stop conditions

Stop or weaken the claim when:

- gate changes cannot be explained by the declared automorphism/coboundary;
- grazing mass or event ambiguity exceeds the threshold;
- Jacobi drift, word, outcome, or roof time fails refinement;
- the finite cell count grows without stable held-out prediction;
- scalar partition data erase a task-visible deck distinction;
- a twisted character is treated as a positive probability despite negative
  or complex values;
- closed-cycle traces are used for absorbing open prefixes;
- a different Jacobi level is compared after silently renormalizing away its
  reference section volume;
- same-scale nested partitions flatten but are still called rank raising;
- a numerical finite graph is renamed a Markov partition or a continuous-flow
  zeta function;
- a control or Huffman claim appears before its missing semantics are supplied.

After two grid refinements, failure of the principal task quantities to
stabilize triggers a finite-proxy conclusion or a continuous-operator redesign,
not a larger undirected orbit census.

## 13. Claim boundary and Theory Map effect

Phase 2 may establish:

- a converged finite return/absorbing ensemble for the frozen section;
- an explicit relation between two gate presentations;
- finite scalar and twisted partition identities on the empirical graph;
- evidence about which state/payload is sufficient for declared tasks.

It cannot by itself establish:

- complete PCR3BP symbolic dynamics or a Markov partition;
- a canonical gate or canonical ensemble;
- a Ruelle zeta function for the flow;
- a Bellman optimum or Huffman code;
- completeness of the proposed classification tuple;
- Arithmetic Geometric Universality.

```text
Primitive assumptions: rotating PCR3BP, fixed Jacobi leaves, declared section
Task semantics: terminal outcome, return cell, roof statistics, optional deck character
Candidate grammar: finite section cells + absorbing states + deck residual
Certificates: Jacobi/event refinement, held-out continuation, gate coboundary,
              finite trace/determinant identities
Theory Map effect now: no promotion; calibrates the refined V2/V3 boundary
                       while pressuring H0/H2/H3 and V5
API pressure: none
```
