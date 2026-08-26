# Phase 1E contract — hard-sphere collision-boundary adaptation

**Status:** frozen continuum contract with one exact rational quadrature
shadow.  The hard-sphere and Boltzmann--Grad statements below are theorem
records from the cited literature unless explicitly labelled as an executed
repository certificate.  This phase proves no continuum limit, trace theorem,
propagation of chaos, or H theorem.

**Executable owner:**
`tests/research/test_hard_sphere_continuum_adapter_seam.py`.

**Result owner:**
`10-phase1e-continuum-collision-adapter-seam-results.md`.

## 1. Why the continuum seam is not one map

Phase 1C proved in a finite model that a one-body state can be exact for a
present-state task and inadequate for its next derivative.  In the hard-sphere
continuum this distinction becomes sharper: the BBGKY derivative is driven by
the trace of the next correlation on a collision boundary.  A bulk marginal,
a boundary trace, and a time-integrated collision history are therefore three
different semantic carriers.

The continuum dependency is

```text
hard-sphere law on the exclusion carrier
    -> rescaled bulk correlation family
    -> oriented contact-boundary traces
    -> positive gain/loss process jet
    -> A/M chart where the target density is positive
    -> factorized incoming-trace section plus residual
    -> mild collision-history comparison
    -> autonomous Boltzmann dynamics when the limiting theorem applies
    -> H/Lyapunov question
```

The principal Phase 1E correction is:

> The bulk \(L^1\) comparison in the Deng--Hani--Ma theorem is not by itself a
> collision-generator certificate.  Boundary-flux adequacy is a stronger
> task, and long-time continuation requires history structure beyond one
> Banach-norm estimate.

## 2. Source carrier, reference measure, and correlation readout

### 2.1 Fixed-particle hard-sphere carrier

For diameter \(\epsilon>0\), dimension \(d\ge2\), and particle number \(N\),
the admissible phase carrier is

\[
\mathcal D_N^\epsilon
=
\left\{
Z_N=(x_i,v_i)_{i=1}^N\in\mathbb R^{2dN}:
|x_i-x_j|\ge\epsilon\quad(i\ne j)
\right\}.
\]

Away from a Lebesgue-null exceptional set, the hard-sphere flow is unique,
measure preserving, and reversible.  At \(|x_i-x_j|=\epsilon\), put
\(\omega=(x_i-x_j)/\epsilon\); the velocity reflection is

\[
v_i'=v_i-((v_i-v_j)\cdot\omega)\omega,
\qquad
v_j'=v_j+((v_i-v_j)\cdot\omega)\omega.
\]

The exact finite-\(N\) BBGKY formula below may be read on symmetric densities
or measures relative to Lebesgue measure on \(\mathcal D_N^\epsilon\).  Its
boundary values are trace data; pointwise notation presupposes enough
regularity and otherwise stands for the weak formulation.

### 2.2 Grand-canonical carrier used by Deng--Hani--Ma

The long-time theorem uses

\[
\Gamma_\epsilon=\bigsqcup_{N\ge0}\mathcal D_N^\epsilon,
\qquad
\lambda_\epsilon|_{\mathcal D_N^\epsilon}=\frac{1}{N!}\,dZ_N.
\]

Relative to this declared reference, its initial probability law has weight

\[
\frac1{\mathcal Z_\epsilon}
\epsilon^{-(d-1)N}
\prod_{j=1}^N f_0(z_j)
\mathbf 1_{\mathcal D_N^\epsilon}(Z_N).
\]

If \(W_N^\epsilon(t,Z_N)\) denotes the evolved density convention used in the
paper, the order-\(s\) readout is the *rescaled grand-canonical correlation*

\[
f_s^\epsilon(t,Z_s)
=
\epsilon^{(d-1)s}
\sum_{n\ge0}\frac1{n!}
\int W_{s+n}^\epsilon(t,Z_{s+n})\,dZ_{s+1:s+n}.
\]

It must not be silently typed as a normalized \(s\)-particle probability
marginal.  It is a factorial/correlation density adapted to the
Boltzmann--Grad scaling.  The probability law on \(\Gamma_\epsilon\), its
density relative to \(\lambda_\epsilon\), and the correlation readout
\(f_s^\epsilon\) are distinct objects.

## 3. Exact \(s+1\to s\) collision-boundary observation

For the fixed-\(N\) hierarchy, set

\[
\alpha_{N,s}=(N-s)\epsilon^{d-1}.
\]

For a nonnegative \((s+1)\)-particle trace \(F_{s+1}\), define

\[
\begin{aligned}
(C_{s,s+1}^{\epsilon,N}F_{s+1})(Z_s)
={}&\alpha_{N,s}
\sum_{i=1}^s
\int_{\mathbb S^{d-1}\times\mathbb R^d}
\omega\cdot(u-v_i)\\
&\qquad\qquad\times
F_{s+1}(Z_s,x_i+\epsilon\omega,u)
\,d\omega\,du .
\end{aligned}
\]

With \(a_+=\max(a,0)\) and \(a_-=\max(-a,0)\), this has the positive split

\[
C_{s,s+1}^{\epsilon,N}=C_{s,s+1}^{+,\epsilon,N}
-C_{s,s+1}^{-,\epsilon,N},
\]

\[
C_{s,s+1}^{\pm,\epsilon,N}F
=
\alpha_{N,s}\sum_{i=1}^s
\int
(\omega\cdot(u-v_i))_\pm
F(Z_s,x_i+\epsilon\omega,u)\,d\omega\,du .
\]

The BBGKY equation is, in its justified weak/trace sense,

\[
\left(\partial_t+\sum_{i=1}^s v_i\cdot\nabla_{x_i}\right)
F_N^{(s)}
=
C_{s,s+1}^{\epsilon,N}F_N^{(s+1)}.
\]

This formula is the continuum analogue of the finite Phase 1C seam, but the
source object is not merely the bulk value of \(F_N^{(s+1)}\).  The operator
reads its oriented trace at \(|x_{s+1}-x_i|=\epsilon\).

Under \(N\epsilon^{d-1}=1\),

\[
\alpha_{N,s}=1-\frac{s}{N}\longrightarrow1
\]

for fixed \(s\).  Scaling removes the prefactor defect; it does not remove the
contact displacement, correlation trace, or recollision history by itself.

## 4. The primitive process jet is gain/loss before it is A/M

Define the material collision derivative

\[
\mathcal D_s
=
\partial_t+\sum_{i=1}^s v_i\cdot\nabla_{x_i}.
\]

The boundary observation supplies the positive cone

\[
A_s=C_{s,s+1}^{+,\epsilon,N}F_N^{(s+1)}\ge0,
\qquad
L_s=C_{s,s+1}^{-,\epsilon,N}F_N^{(s+1)}\ge0,
\]

and hence

\[
\mathcal D_sF_N^{(s)}=A_s-L_s.
\]

Only on the positive domain \(F_N^{(s)}>0\) may one pass to the A/M chart

\[
M_s=-\frac{L_s}{F_N^{(s)}}\le0,
\qquad
\mathcal D_sF_N^{(s)}=A_s+F_N^{(s)}M_s.
\]

Thus \((A_s,L_s)\) is the chart-independent process cone for this task, while
\((A_s,M_s)\) is a division chart on its positive part.  At a zero of the
target density the gain/loss trace may remain meaningful although \(M_s\) is
undefined.  A continuum implementation must therefore not make division by
the target state part of the primitive collision object.

This also answers one part of the chart-first question.  The two process
amounts do not arise from duplicating the bulk physical state.  They arise by
splitting the *oriented collision-boundary flux* before lowering it to the
visible material derivative.

## 5. Oriented factorization and the limiting Boltzmann jet

For a positive-flux collision node put

\[
B_i(\omega,u;v_i)=(\omega\cdot(u-v_i))_+.
\]

The inverse elastic reflection is

\[
v_i^*=v_i-((v_i-u)\cdot\omega)\omega,
\qquad
u^*=u+((v_i-u)\cdot\omega)\omega.
\]

The hard-sphere boundary condition transports an outgoing trace to this
incoming preimage.  Consequently the factorized closure is more precisely an
*oriented incoming-trace section* plus collision involution, not an assertion
that an arbitrary bulk product satisfies the finite-\(N\) Liouville boundary
condition exactly.

After \(\epsilon\to0\), the order-one target jet becomes

\[
A_0[f](x,v)
=
\int B(\omega,u;v)
f(x,v^*)f(x,u^*)\,d\omega\,du,
\]

\[
L_0[f](x,v)
=
f(x,v)
\int B(\omega,u;v)f(x,u)\,d\omega\,du,
\]

so on \(f>0\),

\[
M_0[f](x,v)
=
-\int B(\omega,u;v)f(x,u)\,d\omega\,du.
\]

Therefore

\[
(\partial_t+v\cdot\nabla_x)f
=A_0[f]+fM_0[f]
=Q^+(f,f)-\nu[f]f.
\]

This is a same-target-layer A/M identity once the factorized incoming-trace
section and limiting equation have been earned.  It is not a decoder for the
hard-sphere history.

## 6. Exact defect ledger

Let \(K_\epsilon\) denote the collision-boundary operator after removing the
prefactor \(\alpha_{N,s}\), and let \(\sigma_{\epsilon}^{\mathrm{tr}}(f)\)
denote the oriented factorized trace section.  Write the actual source trace
as

\[
F_{s+1}
=
\sigma_{\epsilon}^{\mathrm{tr}}(f)+g_{s+1}^{\mathrm{tr}}.
\]

Then the instantaneous target-generator defect has the algebraic
decomposition

\[
\begin{aligned}
\alpha_{N,s}K_\epsilon F_{s+1}
-K_0\sigma_0^{\mathrm{tr}}(f)
={}&
(\alpha_{N,s}-1)K_0\sigma_0^{\mathrm{tr}}(f)\\
&+\alpha_{N,s}
\left(K_\epsilon\sigma_\epsilon^{\mathrm{tr}}(f)
-K_0\sigma_0^{\mathrm{tr}}(f)\right)\\
&+\alpha_{N,s}K_\epsilon g_{s+1}^{\mathrm{tr}}.
\end{aligned}
\]

The three displayed residuals are:

1. **scaling defect** — \((N-s)\epsilon^{d-1}-1\);
2. **contact/geometric defect** — the \(x_i\pm\epsilon\omega\) boundary
   displacement and exclusion geometry;
3. **correlation-trace defect** — failure of the incoming boundary trace to
   factorize.

For a long-time mild comparison there is at least one further ledger:
recollision/truncation/history error.  It is not an instantaneous scalar term
until a Duhamel or collision-history representation has been selected.

The exact rational Phase 1E executable certifies this decomposition for one
quadrature shadow with every one of the three displayed terms nonzero.  That
certificate proves the typing and algebra of the ledger, not a continuum
bound on any term.

## 7. The trace obstruction

Bulk \(L^1\) smallness does not control a codimension-one boundary trace.  The
elementary family

\[
g_n(r)=\max(1-nr,0),\qquad r\ge0,
\]

satisfies

\[
\|g_n\|_{L^1(\mathbb R_+)}=\frac1{2n}\longrightarrow0,
\qquad
g_n(0)=1.
\]

Placed in the normal coordinate to a contact surface, it is an exact red team
against the implication

\[
\text{bulk }L^1\text{ adequacy}
\quad\Longrightarrow\quad
\text{boundary-flux or generator adequacy}.
\]

Therefore the collision-boundary jet requires one of the following, each with
its own hypotheses:

- a boundary trace norm or flux-measure estimate;
- regularity strong enough for a trace theorem;
- a weak/mild observable in which the boundary term is already integrated;
- a collision-history expansion whose geometric estimates control the
  boundary encounters directly.

This is not a criticism of the Deng--Hani--Ma theorem.  It explains why that
proof propagates structural collision-history information rather than trying
to iterate one bulk Banach-norm estimate.

## 8. The Deng--Hani--Ma adapter, typed by task

Let \(f(t,z)\) be the regular Boltzmann solution on \([0,t_{\mathrm{fin}}]\)
under the hypotheses of their Theorem 1.  Their main state comparison is

\[
\sup_{0\le t\le t_{\mathrm{fin}}}
\sup_{s\le|\log\epsilon|}
\left\|
f_s^\epsilon(t,Z_s)
-\mathbf1_{\mathcal D_s^\epsilon}(Z_s)
\prod_{j=1}^s f(t,z_j)
\right\|_{L^1(\mathbb R^{2ds})}
\le\epsilon^\theta.
\]

This certifies the following adapter cell as an **external theorem**:

| field | theorem-scoped value |
| --- | --- |
| source | grand-canonical hard-sphere law on \(\Gamma_\epsilon\) |
| state readout | rescaled correlations \(f_s^\epsilon\) |
| target | factorized Boltzmann hierarchy with exclusion indicator |
| task family | bounded observables dual to the displayed bulk \(L^1\) comparison |
| horizon | \([0,t_{\mathrm{fin}}]\), the declared regular lifespan |
| observer order | uniformly \(s\le|\log\epsilon|\) |
| topology/error | bulk \(L^1\), budget \(\epsilon^\theta\) |
| ensemble | grand canonical in the proof; the authors state a canonical analogue |
| reconstruction | no microscopic-history decoder |

It does **not** by itself fill the boundary-flux row.  That row is protected by
the trace obstruction in Section 7.

### 8.1 What carries the continuation certificate

At time layers \(t=\ell\tau\), the paper expands

\[
f_s^\epsilon(t,Z_s)
=
\prod_{j\in[s]}f_A(t,z_j)
+
\sum_{\varnothing\ne H\subseteq[s]}
\left(\prod_{j\in[s]\setminus H}f_A(t,z_j)\right)
E_H^\epsilon(t,z_H).
\]

The cumulants satisfy theorem-specific \(L^1\) estimates, while their
construction retains more than their norms:

| proof object | Phase 1E role | explicit non-identification |
| --- | --- | --- |
| \(f_A\) | propagated main/factorized component | not a global inverse section of the microscopic law |
| \(E_H^\epsilon\) | signed connected correlation residual | not a conditional probability and not one A or M component |
| partial time expansion | continuation translator/certificate | not a finite jet |
| layered collision history | retained source history | not a bulk marginal |
| molecule | combinatorial evaluation shadow retaining order and layer | forgets precise geometry, velocities, and times |
| \(|IN_M|\) | normalized history-contribution bound | not the probability of a macro fibre without additional typing |
| cutting | compositional integration/cost certificate | not physical time evolution or objectification |
| truncation error | explicit failure/residual channel | not absorbed into the cumulant name |

The paper emphasizes that no natural Banach norm can simply propagate the
cumulant smallness layer by layer: microscopic reversibility would contradict
such a same-norm induction.  Instead it propagates the partial-expansion
structure, represents connected histories by molecules, and estimates the
associated integrals.  A cut yields the operator composition

\[
I_M=I_{M_1}\circ I_{M_2},
\]

while recollision circuit rank supplies an \(\epsilon\)-gain that offsets the
combinatorial number of molecules.

This is the strongest current evidence for reading the proof as a
history-bearing, certified approximate semantic adapter.  It is also a red
team against replacing the continuation translator by one fixed-order A/M
jet over a long horizon.

## 9. Frozen task matrix

| source -> target | task | status |
| --- | --- | --- |
| hard-sphere flow -> evolved grand-canonical law | microscopic evolution | exact a.e. external dynamics |
| source law -> \(f_s^\epsilon\) | bulk correlation readout | exact definition |
| \(f_{s+1}\) boundary trace -> \((A_s,L_s)\) | next material derivative | exact operator contract |
| positive \((F_s,A_s,L_s)\) -> \((F_s,A_s,M_s)\) | charted derivative | exact where \(F_s>0\) |
| bulk \(L^1\) error -> collision boundary trace | generator task | rejected by exact red team |
| hard-sphere correlations -> factorized Boltzmann hierarchy | bulk \(L^1\), declared horizon | external Deng--Hani--Ma theorem |
| one A/M jet -> complete long-time comparison | unrestricted continuation | unclaimed and red-teamed by full histories |
| autonomous Boltzmann equation -> H | monotonicity | downstream classical control, not Phase 1E |

## 10. Solver plan and executable boundary

```text
Problem and task:
  Type the continuum s+1 -> s collision adapter and isolate its defects.

Primitive process / constraints:
  Hard-sphere exclusion carrier, elastic reflection, oriented contact flux.

Parameter regime and units:
  d >= 2; diameter epsilon; dimensionless Boltzmann--Grad prefactor alpha.

Required lift and residuals:
  Incoming/outgoing traces, correlation trace, contact displacement,
  collision-history/recollision data for long horizons.

Candidate presentation:
  Positive gain/loss cone; A/M division chart only on positive target states.

Exact evaluator:
  Fraction-valued one-node rational quadrature shadow.

Continuum evaluator:
  Literature theorem record only; no repository numerical solver.

Certificates:
  Collision involution and conserved momentum/energy;
  gain/loss and A/M identities;
  three-term generator-defect decomposition;
  bulk-L1/boundary-trace counterexample.

Failure semantics:
  zero-target A/M chart failure; missing trace regularity; bulk-only budget;
  unclaimed full-future reconstruction.

Baseline:
  Classical hard-sphere BBGKY operator and Deng--Hani--Ma Theorem 1.

Budget:
  exact research fixture under one second; no new dependency.
```

The executable is a quadrature *shadow* of the continuum formula.  It may
certify algebraic covariance and an obstruction, but it may not report
continuum convergence, numerical stability, or a kinetic theorem.

## 11. Kill conditions

Phase 1E must be revised if it:

- calls \(f_s^\epsilon\) a normalized probability marginal;
- evaluates the boundary collision operator from a bulk \(L^1\) class without
  a trace or mild formulation;
- divides by \(F_s=0\) to manufacture a multiplicative rate;
- hides the oriented factorization/closure inside the definition of the chart;
- treats the exclusion indicator as a dynamical cumulant without separating
  reference carrier from connected correlation;
- identifies \(E_H^\epsilon\), a conditional fibre law, and an A/M component;
- turns the theorem's bulk \(L^1\) budget into an unproved generator-defect
  estimate;
- calls a molecule the literal collision history after it has forgotten
  geometric variables and times;
- calls the cutting composition a new arithmetic rank without a free grammar
  and all-composite lowering;
- reopens entropy search before the autonomous target layer and its declared
  horizon are fixed.

## 12. Repository effect

### Mathematical Core

**Refinement pressure only.**  Phase 1E splits a continuum adapter into bulk,
boundary-trace, and mild-history tasks and adds a precise trace obstruction.
The current semantic-adapter and measured-fibre language can express the
split.  No stable Core edit is proposed from this single continuum
calibration.

### Engineering Architecture

**Refined locally.**  A continuum collision adapter must record boundary
trace/flux semantics separately from its bulk norm and must keep a gain/loss
cone before an A/M division chart.  The executable remains research-local; no
backend or API changes.

### Theory Map

**Unchanged.**  The result supports the emerging task-covariant adaptation
transversal and sharpens its failure boundary.  It does not add an axis,
promote a generic adapter, or raise arithmetic rank.

## Sources

- Y. Deng, Z. Hani, X. Ma, *Long time derivation of the Boltzmann equation
  from hard sphere dynamics*, arXiv:2408.07818v3, especially Definitions
  1.1--1.4, Theorem 1, and Sections 1.3.2--1.3.6,
  https://arxiv.org/abs/2408.07818
- Annals of Mathematics publication record for the same work,
  https://annals.math.princeton.edu/articles/22284
- I. Gallagher, L. Saint-Raymond, B. Texier, *From Newton to Boltzmann: hard
  spheres and short-range potentials*, especially equations (4.3.2)--(4.3.8)
  and (4.4.1)--(4.4.6), https://arxiv.org/abs/1208.5753
