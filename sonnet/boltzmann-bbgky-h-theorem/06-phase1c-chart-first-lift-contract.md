# Phase 1C contract — chart-first layer adaptation

**Status:** refrozen before Phase 1C execution after the strict-decoder red team.

**Logical status:** this file is later in repository chronology but earlier in
the research dependency graph than Phases 1A and 1B. Those phases are retained
as post-hoc kinetic controls. They no longer define the mother route.

**Planned executable owner:**
\`tests/research/test_chart_first_collision_adapters.py\`.

**Planned result owner:**
\`07-phase1c-chart-first-adaptation-results.md\`.

## 1. Two corrections

The first correction is to begin with the physical evolution law, not with the
known H theorem, and only later ask whether a monotone functional emerges.

The second correction was forced by an immediate red team against the first
version of this contract. Requiring a charted dynamics to decode globally and
strictly to the original dynamics conflates two different constructions:

1. a coordinate chart inside one semantic layer;
2. an adapter between layers that legitimately forget different distinctions.

A same-layer chart may be locally lossless. A micro-to-correlation,
correlation-to-kinetic, or physical-to-process passage need not be invertible
and need not conjugate the complete dynamics. It must instead be adequate for
declared observations and continuations, with its defect and forgotten
information recorded.

The revised dependency order is

\[
\text{layered physical dynamics}
\longrightarrow
\text{process chart inside each layer}
\longrightarrow
\text{task-relative layer adapters}
\longrightarrow
\text{adaptation defect and residual}
\longrightarrow
\text{Lyapunov search}.
\]

No entropy, logarithmic covector, Maxwellian, partition function, or
molecular-chaos closure is permitted in the Phase 1C solver.

## 2. A semantic layer

A semantic layer is typed by

\[
\mathcal L
=
(X,\mathcal H,\mathcal C,\Phi,\mathrm{Obs},Q),
\]

where:

- \(X\) is the layer's state carrier;
- \(\mathcal H\) is its admitted history or germ carrier;
- \(\mathcal C\) is its continuation interface;
- \(\Phi\) is its evolution law;
- \(\mathrm{Obs}\) is its observer family;
- \(Q\) is the declared task family.

The microscopic law, an \(s\)-body marginal hierarchy, a one-body kinetic
law, and an A/M process presentation are therefore not presumed to have the
same states, continuations, or equality relation.

A coordinate chart \(\chi:U\leftrightarrow V\) internal to one layer may be
required to preserve that layer's dynamics on its domain. That requirement is
not exported to an inter-layer map.

## 3. A layer adapter

An adapter from source layer \(\mathcal L_\ell\) to target layer
\(\mathcal L_m\) contains at least

\[
\mathfrak A_{\ell\to m}
=
(a,\kappa,\rho,\mathcal Q,T,\varepsilon):
\mathcal L_\ell\rightsquigarrow\mathcal L_m.
\]

Its data are:

- a state, history-germ, or jet map \(a\);
- a continuation translator \(\kappa_x\) sending each declared target
  continuation to an admissible source continuation;
- a result translator \(\rho_q\);
- a declared target task family \(\mathcal Q\);
- a continuation horizon \(T\);
- an exact or approximate error budget \(\varepsilon_q\).

For \(x\in X_\ell\), a target continuation \(k\), and \(q\in\mathcal Q\), the
adapter is adequate when

\[
d_q\!\left(
 q_m(a(x)\cdot k),
 \rho_q\!\left(q_\ell(x\cdot\kappa_x(k))\right)
\right)
\le \varepsilon_q.
\]

This condition does not require \(a\) to be injective, surjective, invertible,
or a global semiconjugacy. It states only which target continuations and
observations the source-to-target representation preserves.

Forgotten distinctions are not automatically errors. They become a
continuation residual precisely when two source histories identified by the
adapter are separated by a declared source continuation or by a stronger
target task.

## 4. Infinitesimal adequacy

For smooth layers with vector fields \(F_\ell,F_m\), define the generator
defect seen by a target observable \(q\) as

\[
\Delta_q^{\ell\to m}(x)
=
D(q\circ a)_xF_\ell(x)
-
Dq_{a(x)}F_m(a(x)).
\]

The phase distinguishes four grades.

| grade | requirement | responsible language |
| --- | --- | --- |
| coordinate exact | full vector-field equality in one chart domain | same-layer change of coordinates |
| task-exact | \(\Delta_q=0\) for every declared \(q\in\mathcal Q\) | exact adapter for \(\mathcal Q\) |
| task-approximate | \(\|\Delta_q\|\le\varepsilon_q\) on the frozen domain | certified approximation |
| interpretive only | no frozen task/defect certificate | analogy, not a result |

Full equality

\[
Da\,F_\ell=F_m\circ a
\]

is a special case. It is not the Phase 1C mother requirement.

## 5. The A/M chart is a process-jet chart

A scalar value alone does not determine two process components. For a scalar
observable \(u\) on a declared dynamic layer, the A/M chart acts on its
first history germ:

\[
j^1u
\longmapsto
(u;A_u,M_u),
\qquad
\mathcal L_Fu=A_u+uM_u.
\]

The pair \((A_u,M_u)\) describes the additive supply and multiplicative rate
seen in that chart. It need not reconstruct the complete source state or its
future.

There is a useful same-layer homogeneous realization,

\[
u=-\frac{x_u}{y_u},
\qquad
A_u=-\frac{\dot x_u}{y_u},
\qquad
M_u=-\frac{\dot y_u}{y_u},
\]

for which

\[
\dot u=A_u+uM_u.
\]

Under \((x_u,y_u)\mapsto(\rho x_u,\rho y_u)\), with
\(\kappa=\dot\rho/\rho\),

\[
(A_u,M_u)\mapsto(A_u+u\kappa,M_u-\kappa),
\]

and the visible first derivative is unchanged. This projective model is a
lossless same-layer control and a gauge audit. It is not the definition of
cross-layer adequacy and is not required to decode microscopic dynamics.

## 6. First-principles kinetic chart

For a positive kinetic density, write the collision law in gain--loss form

\[
D_tf=Q^+(f,f)-\nu[f]\,f.
\]

The frozen A/M process chart is

\[
A_f=Q^+(f,f),
\qquad
M_f=-\nu[f].
\]

This choice is made before any entropy question:

- \(A_f\ge0\) is additive incoming supply;
- \(M_f\le0\) is the multiplicative survival or hazard rate;
- the target-layer first-derivative task reads \(D_tf=A_f+fM_f\);
- gain/loss orientation is retained even when their sum is small or zero.

For one reversible channel

\[
(0,1)\longleftrightarrow(2,3),
\qquad
X=f_0f_1,\quad Y=f_2f_3,
\]

with rate \(c>0\), freeze

\[
F=c(-X+Y,-X+Y,X-Y,X-Y)
\]

and

\[
\begin{array}{c|cc}
i&A_i&M_i\\ \hline
0&cY&-cf_1\\
1&cY&-cf_0\\
2&cX&-cf_3\\
3&cX&-cf_2.
\end{array}
\]

The identity \(F_i=A_i+f_iM_i\) is a same-layer task-exact certificate for the
next-derivative observer. It is not a claim that the A/M pair is semantically
equivalent to the complete collision history.

## 7. Process composition inside the chart

The product task has the exact A/M rule

\[
w=uv,
\qquad
A_w=vA_u+uA_v,
\qquad
M_w=M_u+M_v,
\]

so that

\[
\mathcal L_Fw=A_w+wM_w.
\]

For a positive weighted observation

\[
q=\sum_\alpha w_\alpha u_\alpha,
\qquad w_\alpha\ge0,
\]

freeze the lowering rule

\[
A_q=\sum_\alpha w_\alpha A_\alpha,
\qquad
M_q=
\frac{\sum_\alpha w_\alpha u_\alpha M_\alpha}
     {\sum_\alpha w_\alpha u_\alpha}
\]

when \(q>0\). It certifies the declared derivative observation,

\[
\mathcal L_Fq=A_q+qM_q,
\]

but does not imply that every continuation available before lowering exists
after lowering.

## 8. The finite BBGKY seam as an adapter comparison

Use a finite exact two-particle Markov collision layer on ordered pair states

\[
(i,j)\in\{0,1,2\}^2.
\]

The only active transitions are

\[
(0,0)\rightleftarrows(1,2),
\qquad
(0,0)\rightleftarrows(2,1),
\]

all with rate \(c>0\). Let \(P_{ij}\) be the two-body law and define the
exchange-averaged one-body marginal

\[
f_i=\frac12\left(\sum_jP_{ij}+\sum_jP_{ji}\right).
\]

Compare two adapters.

### 8.1 State-only adapter

\[
L:P\longmapsto f.
\]

It is exact for the present one-body marginal task. Phase 1C must red-team its
adequacy for the next-derivative task.

### 8.2 A/M first-jet adapter

At pair level, the Markov generator has gain and loss-rate fields

\[
A^{(2)}_{ij}
=\sum_{k\ell\to ij}c_{k\ell,ij}P_{k\ell},
\qquad
M^{(2)}_{ij}
=-\sum_{ij\to k\ell}c_{ij,k\ell}.
\]

Lower them by Section 7 to obtain

\[
J_\chi:P\longmapsto
\left(f;A^{(1)},M^{(1)}\right).
\]

The declared target task reads

\[
\dot f_i=A^{(1)}_i+f_iM^{(1)}_i.
\]

Phase 1C must test whether \(J_\chi\) is task-exact for this one-step
derivative task. It must not infer adequacy for the second derivative, an
arbitrary continuation, or the full future.

This makes the research question precise:

> Does the A/M first-jet chart repair the exact task failure of the state-only
> marginal adapter, and exactly which stronger continuations still require a
> residual?

## 9. Frozen witnesses

Use two exchange-symmetric laws.

**Diagonal law**

\[
P_{00}=P_{11}=P_{22}=\frac13,
\]

with all other entries zero.

**Off-diagonal law**

\[
P_{ij}=\frac16\quad(i\ne j),
\]

with all diagonal entries zero.

Both have uniform one-body marginal. Their marginal derivatives under the
frozen generator must differ.

To rule out a boundary-only explanation, also use

\[
P_\epsilon^{\mathrm{diag}}
=(1-\epsilon)P^{\mathrm{diag}}+\epsilon U,
\qquad
P_\epsilon^{\mathrm{off}}
=(1-\epsilon)P^{\mathrm{off}}+\epsilon U,
\]

where \(U_{ij}=1/9\) and \(\epsilon=1/4\). Both laws are strictly positive,
retain the same uniform marginal, and must still have different derivatives.

## 10. Frozen tasks and adaptation matrix

| source → target | task | expected grade |
| --- | --- | --- |
| homogeneous A/M → scalar | same-layer value and first derivative | coordinate exact |
| collision gain/loss → kinetic derivative | next derivative | task-exact |
| two-body law \(P\) → marginal \(f\) | present marginal | task-exact |
| two-body law \(P\) → marginal \(f\) | next derivative | rejected by witness |
| two-body law \(P\) → \((f,A^{(1)},M^{(1)})\) | next derivative | task-exact |
| \((f,A^{(1)},M^{(1)})\) → complete two-body future | unrestricted continuation | unclaimed |

The executable may certify or reject only these frozen cells.

## 11. Oracle firewall

The implementation may use:

- exact rational arithmetic;
- homogeneous ratios;
- finite products and sums;
- finite Markov gain/loss generators;
- marginalization;
- task signatures and generator defects.

It may not import or evaluate:

- \(H[f]\), \(f\log f\), Shannon entropy, or relative entropy;
- logarithm or exponential;
- Maxwellian or Gibbs laws;
- the classical entropy-production factorization;
- Phase 1B's learned character.

## 12. Certificates

1. same-layer homogeneous chart certificate;
2. gauge covariance of the visible first derivative;
3. exact one-channel gain/loss task adapter;
4. nonnegative-gain/nonpositive-rate cone;
5. collision-involution covariance;
6. product-process composition;
7. exact pair-generator gain/loss split;
8. exact present-marginal adapter;
9. rejection of state-only next-derivative adequacy;
10. strict-positive residual witness;
11. exact A/M first-jet next-derivative adapter;
12. mass conservation before and after lowering;
13. explicit adaptation-grade ledger.

## 13. Kill conditions

The phase fails or must be weakened if:

- global semantic equivalence is inferred from a task-exact square;
- a cross-layer adapter is required to possess an inverse without task need;
- forgotten distinctions are called errors without a separating continuation;
- a gauge-dependent A/M split is reported without a chart policy;
- the residual witness changes the declared present marginal;
- the only residual witness uses boundary probabilities;
- the A/M first-jet adapter fails the declared derivative task;
- one-step adequacy is called full-future reconstruction;
- an entropy or logarithmic oracle enters the solver;
- BBGKY observer order \(s\) is renamed arithmetic rank \(r\).

## 14. Rank, observer, and chart ledger

Use

\[
X_{r,s}^{(\chi)},
\]

where \(r\) is arithmetic/process rank, \(s\) is correlation/observer order,
and \(\chi\) is the chart or adapter policy. None determines the others.

Phase 1C moves between \(s=2\) and \(s=1\) at fixed \(r\). It is not rank
raising. Higher-rank observations remain a separate vertical program requiring
objectification, new free composition, and a lowering interpretation on every
legal composite.

## 15. Budget and claim boundary

The executable must use exact \`Fraction\` arithmetic, remain below one second
on the routine fixture, introduce no dependency, and remain research-local.

Passing Phase 1C would establish a finite hierarchy of semantic adapters:

- a strict same-layer coordinate control;
- a task-exact but forgetful present-marginal adapter;
- an exact failure of that adapter for the next derivative;
- an A/M first-jet adapter adequate for that stronger task.

It would not establish a new H theorem, entropy discovery, global semantic
equivalence, a continuum Boltzmann or BBGKY theorem, molecular chaos,
a new arithmetic rank, or a generic package API.
