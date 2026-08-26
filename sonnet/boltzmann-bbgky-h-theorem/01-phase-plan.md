# Initial research plan and gates

Status: frozen T0 plan. No phase below has been executed.

## 0. Firewall between three claims

The study contains three tracks that must not be merged by rhetoric.

| Track | Question | Earliest admissible claim |
|---|---|---|
| A. Kinetic H theorem | Why is a functional monotone for a declared collision semigroup? | exact finite identity, then calibrated continuum statement |
| B. Micro-to-kinetic passage | Why does reversible many-body dynamics admit that reduced semigroup? | theorem-scoped limiting and closure statement |
| C. Higher-rank observation | What can be observed after processes themselves become composable objects? | typed lowering plus a witnessed intrinsic observer |

Tracks A and B are logically independent: a proof of the H theorem for the Boltzmann equation is not a derivation of that equation from mechanics. Track C begins only after a rank semantics has been earned.

The classical formula may be supplied to the baseline track. It must be hidden from the discovery track until evaluation.

## 1. Problem and solver contract

### Problem

Locate the operation that turns reversible collision histories into a reduced semigroup carrying a monotone state functional, and identify the residual that records why the reduction is not reversibly decodable.

### Primitive domain

Begin with a finite reversible binary-collision network. Hard-sphere dynamics is a later external calibration domain, not the first search space.

### Tasks

- Task A: determine the next derivative of the one-body state.
- Task B: determine whether a candidate state functional is monotone.
- Task C: distinguish two microscopic ensembles with the same declared one-body state.
- Task D: reconstruct or falsify reconstruction of the incoming collision data.
- Task E: at higher arithmetic rank, classify lowering-induced and intrinsic observers.

### Exactness and literature boundaries

- finite-network phases require exact algebra or symbolic verification;
- hard-sphere literature phases are theorem records unless a proof is independently reproduced;
- numerical evidence may reject a candidate but cannot certify a universal identity;
- every density must be a dimensionless ratio relative to a declared measure before a logarithm is taken.

### Required deliverables per phase

Each phase record must state assumptions, forbidden structures, task, candidate grammar, certificates, cost, red teams, claim boundary, and effects on the Mathematical Core, Engineering Architecture, and Theory Map.

## 2. Phase 1A — supplied-baseline finite H theorem

### Frozen model

Let \(V=\{1,\ldots,n\}\) be a finite velocity alphabet. A collision channel is an oriented pair

\[
(i,j)\longleftrightarrow(k,\ell)
\]

with an involution exchanging incoming and outgoing pairs. Freeze:

- positive reference weights \(M_i\);
- nonnegative channel rates;
- exchange symmetries;
- conserved labels such as mass, momentum, or energy;
- a detailed-balance relation for the pair weights;
- the finite collision ODE.

The exact choice of \(V\) and channels must be committed before candidate evaluation.

### Supplied baseline

Use the known relative-entropy candidate

\[
H_M(f)=\sum_i f_i\log\frac{f_i}{M_i}.
\]

Derive its time derivative channel by channel and reduce the sign to

\[
(a-b)(\log a-\log b)\ge 0
\]

or the equivalent exponential-chart form.

### Certificates

1. positivity and mass-domain certificate;
2. collision-involution certificate;
3. conserved-affine-subspace certificate;
4. detailed-balance certificate;
5. exact derivative identity;
6. nonnegative dissipation certificate;
7. equality characterization on every connected collision component.

### Red teams

- break detailed balance while preserving channel reversibility;
- remove one exchange symmetry;
- choose a disconnected collision graph;
- insert a zero population and audit boundary limits;
- change reference weights without updating the rates;
- reverse the H/S sign convention.

### Gate

Passing Phase 1A certifies only a faithful finite reexpression. It does not certify discovery, continuum validity, or a microscopic derivation.

## 3. Phase 1B — hidden-oracle A/M/P discovery

### Information firewall

Hide from the solver:

- the formula \(f\log f\);
- the logarithm as a named entropy coordinate;
- the Maxwellian or equilibrium answer;
- the classical entropy-production factorization.

A separate evaluator retains these as the oracle baseline.

### Frozen candidate grammar

The grammar may contain:

- Addition and Multiplication on positive weights;
- ratios \(f_i/M_i\);
- composition, inversion where typed, and differentiation;
- logarithm and exponential only if admitted as generic positive-coordinate charts rather than entropy-specific hints;
- separable functionals
  \[
  F_\phi(f)=\sum_i M_i\phi(f_i/M_i);
  \]
- gradients and covectors modulo conserved affine functionals.

Power operations beyond what the grammar already supports are not admitted merely to fit the answer.

### Search tasks

1. Search covectors whose collision pairing has a uniform sign.
2. Integrate admissible covectors to candidate state functionals.
3. Quotient candidates by additive constants and conserved affine quantities.
4. Evaluate on the frozen network and held-out collision networks.
5. Compare with the hidden oracle only after ranking is fixed.
6. Run an unrestricted symbolic baseline only after native failure or ambiguity is recorded.

### Metrics

- exact sign certificate;
- coverage across held-out networks;
- uniqueness modulo declared gauge;
- grammar complexity;
- dependence on supplied symmetries;
- transfer to a changed reference measure;
- counterexample count.

### Gate

The logarithmic covector is called rediscovered only if it is selected without oracle leakage, transfers to held-out networks, and survives gauge reduction. Coverage and uniqueness must be reported separately.

## 4. Phase 1C — Shannon and partition-function controls

This control prevents three nearby logarithmic constructions from being collapsed: kinetic \(H\), Shannon or relative entropy of a declared law, and the equilibrium partition normalizer.

### Finite exact controls

For a normalized law \(p\), verify the sign relation between

\[
\sum_i p_i\log p_i
\quad\text{and}\quad
\mathsf S_{\mathrm{Sh}}(p).
\]

For a positive reference law \(m\), compute

\[
D(p\Vert m)=\sum_i p_i\log\frac{p_i}{m_i}
\]

and record how it changes under normalization, state refinement, and a change of reference measure.

For a finite energy system, enumerate exactly

\[
Z(\beta)=\sum_x m_xe^{-\beta E_x},
\]

then certify the Gibbs variational identity, the energy derivative of \(\log Z\), and the cumulants obtained from higher derivatives where defined.

### A/M/P typing test

Any A/M/P rewrite must declare what Power means. Repeated Multiplication, real exponentiation, complex powering, and the exponential coordinate are not interchangeable operations.

Test:

- independent assembly, where \(Z_{A\times B}=Z_AZ_B\);
- the additive chart, where \(\log Z\) turns that product into a sum;
- interacting assembly, where the factorization fails and the interaction residual is explicit;
- nested same-scale partition sums, which may flatten by coherent measure transport;
- a candidate higher-rank partition object with brackets, interaction, or a new reference measure.

### Red teams

- use a dimensionful density inside a logarithm;
- change the base measure while treating entropy as unchanged;
- infer kinetic monotonicity from the equilibrium Gibbs variational principle;
- call \(\log Z\) higher-rank merely because it contains an exponential;
- use Shannon entropy for an unnormalized or continuous density without declaring the reference;
- treat a cumulant-generating derivative as a BBGKY correlation without a map between the sample spaces.

### Gate

The phase may certify exact identities and a typed A/M/P presentation. It may not identify partition functions with kinetic H, nor promote a higher arithmetic rank, unless a nonflattening process object and lowering law are witnessed.

## 5. Phase 2 — observer insufficiency and the BBGKY seam

### Construction

Construct an exact finite microscopic collision process and the projection \(\pi_1\) to its one-body law. Exhibit two microscopic laws \(F\) and \(G\) such that

\[
\pi_1F=\pi_1G
\]

but

\[
\left.\frac{d}{dt}\pi_1F_t\right|_{t=0}
\ne
\left.\frac{d}{dt}\pi_1G_t\right|_{t=0}.
\]

This is the finite witness that the one-body observer is not dynamically closed.

### Candidate continuation observables

Compare, without identifying them prematurely:

- the full two-body marginal;
- the connected two-body cumulant;
- the incoming collision trace;
- a collision-history word;
- the smallest task-stable refinement found by partition refinement.

### Certificates

- exact equality of the one-body states;
- exact inequality of their next derivatives;
- sufficiency or insufficiency of each candidate refinement;
- minimality relative to the frozen candidate family;
- explicit reverse-time discriminator.

### Red teams

- correlations invisible to the selected collision channels;
- hard-core exclusion mistaken for dynamical correlation;
- a residual that predicts one derivative but not two;
- an observer that separates \(F\) and \(G\) but is not stable under continuation;
- scalar entropy difference substituted for a full continuation witness.

### Gate

The phase may claim a task-relative residual. It may not call that residual a new arithmetic rank or Shannon information without further structure.

## 6. Phase 3 — hard-sphere and long-time calibration

This phase is record-only unless proofs are independently reproduced.

### Typed theorem record

Record separately:

1. reversible \(N\)-particle hard-sphere flow;
2. Liouville equation on the admissible exclusion domain;
3. BBGKY hierarchy and collision-boundary terms;
4. factorized or chaotic initial data;
5. Boltzmann hierarchy and Boltzmann equation;
6. Boltzmann–Grad scaling;
7. topology, time interval, and exceptional sets;
8. the kinetic H theorem after the limiting equation is obtained.

### One-sidedness audit

Identify exactly where forward time enters: initial chaos, incoming boundary conditions, recollision estimates, limiting topology, or uniqueness of the kinetic solution. Test every sentence against reversed microscopic trajectories.

### Modern proof audit

For the Deng–Hani–Ma long-time result, record:

- the theorem as published;
- the collision-history and cumulant objects actually used;
- the role of molecules and cutting;
- the topology and error estimates;
- the interval of validity;
- which repository analogies are literal, conjectural, or false.

### Gate

Every conclusion receives one of three labels: external theorem, reproduced result, or process-geometry interpretation. No label may be silently upgraded.

## 7. Phase 4 — observers on a higher arithmetic tower

This phase starts only when a candidate higher rank has grounded semantics, free composition, and compositional lowering.

### Rank-domain gate

A candidate rank \(r+1\) must provide:

- a type of rank-\(r\) process object;
- an identity and associative free composition, up to the declared equivalence;
- a lowering map to rank-\(r\) process semantics;
- a task quotient at the higher rank;
- a nonempty family of lowering-induced observers;
- at least one candidate intrinsic observer.

The first candidates may compare Addition-to-Multiplication objectification and free symmetric assembly. A full A/M/P tower is not assumed in advance.

### Observer classification

For every \(O\in\mathrm{Obs}(\mathrm{Sem}(X_r))\), form

\[
L_r^*O=O\circ L_r.
\]

Then test candidate intrinsic observers of:

- assembly brackets;
- interaction graph;
- object type;
- scale and units;
- reference measure;
- holonomy or path dependence;
- continuation residual after lowering.

### Factorization test

For an observer \(P:X_{r+1}\to Y\), decide whether there exists \(\bar P\) with

\[
P=\bar P\circ L_r.
\]

If not, record the witnessed pair that lowering identifies while \(P\) separates it. This earns a discriminator only. To earn a new state coordinate, the discriminator must also be task-relevant and stable under composition and continuation.

### Gate

A higher-rank observer is not evidence for a higher-rank entropy until a semigroup, reference structure, and monotonicity certificate have been supplied at that rank.

## 8. Phase 5 — cross-rank H diagnostics

### Candidate relations

Given legitimate \(H_r\) and \(H_{r+1}\), test rather than assume:

- flattening:
  \[
  H_{r+1}=H_r\circ L_r;
  \]
- monotone comparison:
  \[
  H_{r+1}\ge H_r\circ L_r;
  \]
- residual decomposition:
  \[
  H_{r+1}=H_r\circ L_r+R_{r+1};
  \]
- observer-indexed family rather than a single scalar;
- absence of any closed scalar Lyapunov functional.

### Red teams

- same-scale log-sum-exp flattening presented as rank raising;
- dimensionful logarithms;
- bracket-sensitive composition that destroys flattening;
- interaction energy stored outside the lower state;
- an induced observer renamed intrinsic;
- a coordinate chart mistaken for a lowering map;
- a scalar functional that forgets holonomy or continuation data;
- correlation order \(s\) silently substituted for process rank \(r\).

### Promotion gate

No generic entropy, rank, or observer API is proposed unless at least two non-isomorphic domains require the same minimal structure and the cross-rank law survives the red teams.

## 9. Cost and CI budget

- Phase 1 exact enumeration: target at most \(10^4\) channels per fixture.
- Symbolic checks: target under 10 seconds per fixture.
- Partition refinement: finite states only, with explicit state-count cap.
- Stochastic exploration, if used: fixed seeds and deterministic replay artifacts.
- Literature audits: no CI cost.
- Research tests remain outside the default suite until stable and cheap.

If a budget is exceeded, shrink the fixture or record a bounded exploratory result; do not weaken the certificate silently.

## 10. Failure semantics

Every attempted claim receives one label:

- pass — certificate satisfies the frozen gate;
- counterexample — a red team falsifies it;
- inconclusive — search or computation ends without a certificate;
- oracle-dependent — succeeds only after classical structure is supplied;
- domain-mismatch — the candidate is not typed for the declared process;
- rank-not-earned — observation exists, but objectification/free composition/lowering is missing.

## 11. Phase effect ledger

| Phase | Mathematical Core | Engineering Architecture | Theory Map |
|---|---|---|---|
| T0 | unchanged | unchanged | calibration pressure only |
| 1A | finite H identity record | research-local fixtures | calibrates H3 |
| 1B | possible A/M covector evidence | discovery harness only | may pressure A/M chart edge |
| 1C | entropy/partition-function separation | finite normalization controls | calibrates same-scale flattening |
| 2 | task-relative continuation residual | exact partition-refinement tools | calibrates H1 and H4 |
| 3 | theorem-scoped micro/kinetic seam | no generic code | calibrates one-sided limit story |
| 4 | possible rank-observer variance law | research-local observer registry | may pressure rank/objectification edge |
| 5 | possible cross-rank Lyapunov relation | no API before transfer | promotion only after two-domain evidence |
