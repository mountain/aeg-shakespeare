# Phase 1C results — layer adaptation before entropy

**Status:** exact finite Phase 1C calibration passed. Full repository CI run
1703 succeeded on Python 3.10 through 3.14 at the executable commit.

**Executable owner:**
\`tests/research/test_chart_first_collision_adapters.py\`.

**Contract owner:**
\`06-phase1c-chart-first-lift-contract.md\`.

## 1. Outcome

Phase 1C changes the main research object.

The useful object is not a globally invertible map from the original dynamics
to an A/M copy. It is a task-relative layer adapter. A strict decoder remains
appropriate for an ordinary coordinate chart inside one layer, but it is too
strong as a universal requirement across microscopic, correlation, kinetic,
and process layers.

The finite experiment establishes a four-step adequacy ladder:

1. a homogeneous A/M realization is coordinate-exact inside one layer;
2. two-body marginalization is task-exact for the present one-body state;
3. the same marginalization fails the next-derivative task;
4. augmenting the marginal by its A/M first jet restores exact adequacy for
   that one stronger task.

This is not semantic equivalence. It is a measured change in semantic
adaptation as the task is strengthened.

## 2. Red-team correction to the first contract

The first frozen Phase 1C draft required

\[
D\pi_\chi\,\widetilde F=F\circ\pi_\chi
\]

as the mother condition. That equation is legitimate for a lossless
same-layer chart, but it wrongly turns all cross-layer forgetting into an
error and silently demands a global semiconjugacy.

The contract was refrozen before execution. The replacement is an adapter

\[
\mathfrak A_{\ell\to m}
=
(a,\kappa,\rho,\mathcal Q,T,\varepsilon),
\]

with a declared state or jet map, continuation translator, result translator,
task family, horizon, and error budget. In the differentiable finite
calibration, adequacy is measured by the observable generator defect

\[
\Delta_q^{\ell\to m}
=
D(q\circ a)F_\ell
-
Dq\,F_m\circ a.
\]

Only the declared observables must have zero or controlled defect. An adapter
need not possess an inverse.

## 3. Exact fixture

The two-body source layer has ordered states

\[
(i,j)\in\{0,1,2\}^2
\]

and the reversible transitions

\[
(0,0)\rightleftarrows(1,2),
\qquad
(0,0)\rightleftarrows(2,1),
\]

at unit rate. The one-body observer is

\[
f_i
=
\frac12\left(\sum_jP_{ij}+\sum_jP_{ji}\right).
\]

The pair generator is split before lowering as

\[
\dot P_{ij}
=
A^{(2)}_{ij}+P_{ij}M^{(2)}_{ij},
\]

where \(A^{(2)}\) is nonnegative incoming supply and \(M^{(2)}\) is a
nonpositive exit rate.

For positive \(f_i\), the lowered A/M first jet is

\[
A^{(1)}_i
=
\sum_{jk}w_{i,jk}A^{(2)}_{jk},
\]

\[
M^{(1)}_i
=
\frac{\sum_{jk}w_{i,jk}P_{jk}M^{(2)}_{jk}}
     {\sum_{jk}w_{i,jk}P_{jk}},
\qquad
w_{i,jk}=\frac{\mathbf 1_{i=j}+\mathbf 1_{i=k}}2.
\]

Exact arithmetic verifies

\[
\boxed{
A^{(1)}_i+f_iM^{(1)}_i
=
\sum_{jk}w_{i,jk}\dot P_{jk}.
}
\]

This is the commuting square required by the next-derivative task. It is not a
full-future conjugacy.

## 4. The exact semantic split

The two frozen exchange-symmetric laws have the same one-body marginal:

\[
f^{(1)}=\left(\frac13,\frac13,\frac13\right).
\]

Their A/M first jets and derivatives differ.

| two-body law | \((A^{(1)}_0,M^{(1)}_0)\) | \((A^{(1)}_1,M^{(1)}_1)\) | \((A^{(1)}_2,M^{(1)}_2)\) | \(\dot f^{(1)}\) |
| --- | --- | --- | --- | --- |
| diagonal \(P_{00}=P_{11}=P_{22}=1/3\) | \((0,-2)\) | \((1/3,0)\) | \((1/3,0)\) | \((-2/3,1/3,1/3)\) |
| off-diagonal \(P_{ij}=1/6,\ i\ne j\) | \((1/3,0)\) | \((0,-1/2)\) | \((0,-1/2)\) | \((1/3,-1/6,-1/6)\) |

Therefore

\[
LP=L\widetilde P
\quad\text{but}\quad
L\mathcal GP\ne L\mathcal G\widetilde P.
\]

No autonomous one-body vector field can be defined from the marginal alone on
a domain containing both witnesses.

The failure is not caused by zeros. Mixing both laws with the uniform law
\(U_{ij}=1/9\) at weight \(\epsilon=1/4\) makes every entry strictly positive,
preserves the common uniform marginal, and leaves distinct derivatives:

\[
\dot f_\epsilon^{\mathrm{diag}}
=
\left(-\frac12,\frac14,\frac14\right),
\]

\[
\dot f_\epsilon^{\mathrm{off}}
=
\left(\frac14,-\frac18,-\frac18\right).
\]

## 5. What the A/M pair accomplishes

For the state-only adapter

\[
L:P^{(2)}\longmapsto f^{(1)},
\]

forgetting is appropriate for the present-marginal task. It becomes a
continuation residual only when the task asks for the next derivative.

The first-jet adapter

\[
J_\chi:
P^{(2)}
\longmapsto
\left(f^{(1)},A^{(1)},M^{(1)}\right)
\]

retains exactly enough information to evaluate that derivative:

\[
\operatorname{eval}_{A/M}(J_\chi P)
=
A^{(1)}+f^{(1)}M^{(1)}
=
L\mathcal GP.
\]

Phase 1C does not show that \(J_\chi P\) determines a second derivative or an
arbitrary future. The result is deliberately asymmetric:

> the A/M first jet repairs one witnessed task failure of the marginal
> adapter; it does not reconstruct the source layer.

This is the first concrete form of layer-relative semantic adaptation in this
Sonnet.

## 6. The closure seam is now located before H

Three maps must remain distinct:

\[
P^{(2)}
\xrightarrow{L}
f^{(1)},
\]

\[
P^{(2)}
\xrightarrow{J_\chi}
(f^{(1)},A^{(1)},M^{(1)}),
\]

\[
f^{(1)}
\xrightarrow{\sigma}
P^{(2)}.
\]

The first is observation, the second is an A/M process-jet adapter, and the
third would be a closure section or limiting reconstruction claim.

An autonomous kinetic equation on \(f^{(1)}\) appears only after a justified
section or limit makes the process jet a function of \(f^{(1)}\):

\[
F_\sigma(f)
=
\operatorname{eval}_{A/M}
\bigl(J_\chi(\sigma(f))\bigr).
\]

This ordering is important. Molecular chaos would belong at \(\sigma\), not
inside the definition of the chart. A monotone H-like functional should be
searched only after the induced target dynamics \(F_\sigma\) has been earned.

## 7. Calibration against Deng–Hani–Ma

The long-time derivation by Deng, Hani, and Ma propagates a cumulant ansatz
that keeps full collision-history memory, isolates a maximally factorised main
part, expands correlation errors through time layers, represents them by
molecules, and controls them with cutting algorithms and \(L^1\) estimates:

- https://arxiv.org/abs/2408.07818
- https://annals.math.princeton.edu/articles/22284
- https://arxiv.org/abs/2602.04407

Phase 1C suggests the following adapter reading, still as a calibration rather
than an identification theorem.

| proof object | adapter role to test | reason not to identify yet |
| --- | --- | --- |
| maximally factorised part | candidate target-layer section/main semantic component | factorisation is propagated and estimated, not a chart axiom |
| cumulant \(E_H^\varepsilon\) | source distinction retained beyond the factorised target | its exact relation to an A/M component is not established |
| layered collision history | continuation translator payload | time ordering and recollision memory are essential |
| molecule | finite history-evaluation carrier | it is a graph with analytic weights, not merely an equivalence class |
| cutting/fragmentation algorithm | adaptation-defect and cost certificate | it proves smallness through geometric/combinatorial estimates |
| \(L^1\) cumulant bound | approximate-adequacy budget \(\varepsilon_q\) | the topology and target task must be matched explicitly |

This changes the large-scale interpretation. The paper should not be read as
saying that correlations are simply “discarded.” It constructs an elaborate
source-layer carrier and proves that particular correlation contributions are
small enough for a declared kinetic comparison. That is much closer to a
certified approximate adapter than to a quotient equivalence.

## 8. Arithmetic rank and observer order

The finite experiment lives at one arithmetic rank and compares observer
orders \(s=2\) and \(s=1\). It supports the notation

\[
J_{r,s}^{(\chi)}:
X_{r,s+1}
\rightsquigarrow
\operatorname{Jet}_{A/M}(X_{r,s}),
\]

where the hooked arrow denotes task-relative adaptation rather than
equivalence.

At higher arithmetic rank, the same question can be asked only after
objectification and lowering are defined:

1. what is the higher-rank source history;
2. what A/M chart acts on its first germ;
3. what lower-rank observer is induced;
4. which intrinsic higher-rank observer does not factor through lowering;
5. for which continuation task the forgotten distinction becomes residual.

Phase 1C provides no rank-raising witness by itself.

### 8.1 A candidate continuation-depth index

The finite result also pressures a third, non-ontological index \(k\):
continuation or jet depth. At fixed arithmetic rank \(r\) and observer order
\(s\), the candidate comparison is

\[
J_{r,s}^{(k,\chi)}:
X_{r,s+k}
\rightsquigarrow
J_\chi^k(X_{r,s}).
\]

Phase 1C executes only:

- \(k=0\): present one-body marginal;
- \(k=1\): the A/M first jet determining one next derivative.

No \(k\ge2\) statement is certified. In the continuum hierarchy, applying a
generator can expose collision-boundary traces rather than a plain marginal,
so even the displayed \(s+k\) source is only a hypothesis to test.

The full-history cumulant construction in Deng--Hani--Ma is a strong negative
control against assuming that one fixed finite jet is uniformly adequate for
long-time comparison. Continuation depth \(k\), observer order \(s\), and
arithmetic rank \(r\) must therefore remain distinct.

## 9. Executable certificates

The research module contains 11 exact tests:

1. homogeneous same-layer chart and gauge covariance;
2. one-channel gain/loss derivative adequacy and process cone;
3. collision-involution covariance;
4. A/M product composition;
5. pair-generator gain/loss split and mass conservation;
6. exact present-marginal adaptation;
7. state-only next-derivative failure;
8. strictly positive residual witness;
9. A/M first-jet next-derivative adequacy;
10. equal marginal with distinct A/M first-jet semantics;
11. frozen adaptation-grade ledger.

Direct exact invocation passes all 11 certificates in approximately 0.04
seconds on the local runtime. The local runtime did not include pytest, so the
same functions were invoked directly. Full repository CI run 1703 then passed
on Python 3.10, 3.11, 3.12, 3.13, and 3.14; the Python 3.14 job reported 620
passed and 25 skipped, and the public quickstarts, package build, metadata
check, and external wheel verification also passed.

## 10. Claim boundary

Phase 1C earns:

- a correction from global semantic equivalence to layer-relative adaptation;
- an exact finite counterexample to one-body next-derivative sufficiency;
- an exact finite A/M first-jet repair for that task;
- a precise location for closure before entropy;
- a sharper, non-identificatory reading of the Deng–Hani–Ma proof architecture.

It does not earn:

- a new H theorem;
- an entropy formula;
- a unique or canonical A/M connection;
- full-future sufficiency of the A/M first jet;
- a continuum BBGKY adapter theorem;
- a proof of molecular chaos or the Boltzmann–Grad limit;
- an identification of cumulants with A or M;
- a new arithmetic rank;
- a generic API.

## 11. Next gate

The next phase should freeze a continuum adapter contract, not an entropy
grammar. It should:

1. write the exact hard-sphere \(s+1\to s\) collision-boundary operator;
2. split its declared incoming and outgoing traces into A/M process jets;
3. define the target observables and generator defects;
4. state the topology and error budget used by the kinetic limit;
5. locate the factorised section, cumulant residual, and collision-history
   continuation translator in the Deng–Hani–Ma construction;
6. only after the autonomous kinetic adapter is certified, reopen the search
   for a monotone state function.
