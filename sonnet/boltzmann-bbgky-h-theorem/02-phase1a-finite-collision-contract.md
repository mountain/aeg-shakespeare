# Phase 1A contract — finite reversible collision network

Status: frozen before implementation and evaluation.

This phase is a supplied-baseline calibration. The relative-entropy functional and logarithmic covector are deliberately visible. Success can certify a faithful finite H theorem, but not discovery of \(H\), a continuum Boltzmann theorem, a BBGKY closure, or a microscopic-to-kinetic limit.

## 1. Primitive model

### Velocity alphabet

Use six labelled velocities in \(\mathbb Z^3\):

\[
\begin{aligned}
v_0&=(1,0,0), & v_3&=(-1,0,0),\\
v_1&=(0,1,0), & v_4&=(0,-1,0),\\
v_2&=(0,0,1), & v_5&=(0,0,-1).
\end{aligned}
\]

The three opposite pairs are

\[
X=(0,3),\qquad Y=(1,4),\qquad Z=(2,5).
\]

Every pair has total momentum zero and total kinetic label
\(\lVert v_i\rVert^2+\lVert v_j\rVert^2=2\).

### Collision graph

Freeze the reversible triangle

\[
X\rightleftarrows Y,\qquad
Y\rightleftarrows Z,\qquad
Z\rightleftarrows X
\]

with positive conductances

\[
c_{XY}=1,\qquad c_{YZ}=2,\qquad c_{ZX}=3.
\]

A channel is stored with an orientation for bookkeeping, but reversing it must negate the flux and leave the induced vector field unchanged.

### Reference weights

Freeze

\[
M=(1,2,3,6,3,2).
\]

The opposite-pair products agree:

\[
M_0M_3=M_1M_4=M_2M_5=6.
\]

This is the detailed-balance certificate for the frozen channel graph.

### State and dynamics

The state is a strictly positive population vector

\[
f=(f_0,\ldots,f_5)\in\mathbb R_{>0}^6.
\]

Write the dimensionless relative activities

\[
q_i=\frac{f_i}{M_i}.
\]

For an oriented channel \((a,b)\to(c,d)\), define

\[
A=q_aq_b,\qquad B=q_cq_d,\qquad
J=c_{ab,cd}(A-B).
\]

Its stoichiometric contribution is

\[
\dot f
=
J(e_c+e_d-e_a-e_b).
\]

The full vector field is the sum over the three frozen channels.

No continuum collision kernel, spatial transport, probability normalization, molecular-chaos assumption, or BBGKY truncation is part of this model.

## 2. Supplied H functional

Use the reference-relative functional

\[
\mathcal H_M(f)
=
\sum_{i=0}^{5}
\left[
f_i\log\frac{f_i}{M_i}-f_i+M_i
\right].
\]

The affine correction does not change the derivative on a mass-conserving flow, but it makes the reference state normalization explicit.

The target channel identity is

\[
\frac{d}{dt}\mathcal H_M(f)
=
-\sum_{\gamma}
c_\gamma
(A_\gamma-B_\gamma)
(\log A_\gamma-\log B_\gamma)
\le 0.
\]

Each summand is nonnegative before the minus sign because logarithm is strictly increasing on \(\mathbb R_{>0}\).

## 3. Process-geometry reading

| Frozen object | Research-local role |
|---|---|
| oriented collision channel | one-step reversible history generator |
| reversed channel | history involution |
| population vector \(f\) | declared reduced state |
| pair activity \(q_iq_j\) | Multiplication payload |
| logarithm of pair activity | additive collision affinity |
| channel conductance | positive comparison weight |
| collision graph | legal continuation grammar |
| conserved affine labels | task-invisible gauge directions |
| channel dissipation | local certificate |
| zero-dissipation component relation | quotient/equality certificate |

This phase does not yet construct the microscopic history space whose quotient gives \(f\). That missing construction belongs to Phase 2 and Phase 3.

## 4. Required certificates

Implementation must supply exact or symbolic certificates for:

1. all six velocities and all three channels;
2. the channel reversal involution;
3. momentum, kinetic-label, and total-population conservation;
4. detailed balance of the frozen reference weights;
5. invariance of the vector field under reversing every stored channel orientation;
6. the symbolic channel derivative identity;
7. nonpositive \(\dot{\mathcal H}_M\) for exact positive rational states;
8. zero dissipation exactly when pair activities agree on each connected component of the collision graph;
9. nonnegative inward vector-field components at zero-population boundary faces;
10. the sign conversion \(S=-k_B\mathcal H_M\).

Universal sign is certified structurally by exact ordering of positive rational activities and monotonicity of logarithm. Floating-point sampling is not a theorem certificate.

## 5. Frozen red teams

### RT1 — reversible reactions without detailed balance

Use one reversible channel with positive physical rates

\[
k_+=2,\qquad k_-=1
\]

and unit reference weights. At pair activities \(A=1\) and \(B=3/2\),

\[
J=k_+A-k_-B=\frac12,
\qquad
\dot H=J\log(B/A)=\frac12\log(3/2)>0.
\]

This must falsify the claim that two-way reaction availability alone implies the chosen H theorem.

### RT2 — mismatched reference measure

Change one reference weight so that one opposite-pair product differs. The detailed-balance validator must reject the model before an H certificate is issued.

### RT3 — disconnected collision graph

Keep only \(X\rightleftarrows Y\). Equal \(X\) and \(Y\) activities must give zero dissipation even when the \(Z\) activity differs. Equality is therefore componentwise, not global without graph connectivity.

### RT4 — boundary state

Allow nonnegative populations only for the boundary audit. Whenever \(f_i=0\), the \(i\)th vector-field component must be nonnegative. The derivative formula containing logarithms remains an interior theorem; the boundary uses the continuous extension \(x\log x\to0\), not an illicit evaluation of \(\log0\).

### RT5 — sign convention

The executable record must state that \(\mathcal H_M\) is nonincreasing and \(S=-k_B\mathcal H_M\) is nondecreasing. It must not call both quantities increasing.

## 6. Forbidden moves

- Do not tune the velocity set, conductances, reference weights, or red-team witnesses after seeing failures.
- Do not use a floating-point tolerance to certify an exact identity.
- Do not call this mass-action network the finite-\(N\) hard-sphere dynamics.
- Do not infer molecular chaos, propagation of chaos, or a Boltzmann–Grad limit.
- Do not present the supplied logarithm as A/M/P discovery.
- Do not promote research helpers into the public API.
- Do not interpret the collision-complex graph order as arithmetic rank.

## 7. Cost and test placement

- implementation remains in one research test module;
- no more than six species and three production channels;
- exact rational and SymPy checks only;
- targeted runtime budget: under 10 seconds;
- no new runtime dependency;
- the default suite must remain deterministic.

## 8. Phase gate

Phase 1A passes only if all ten certificates and all five red teams pass on the frozen model.

A pass earns the statement:

> The finite detailed-balance collision network admits an exact process-local reexpression of the relative H theorem, with Multiplication pair activities, logarithmic additive affinities, reversible channel histories, and componentwise equality certificates.

It does not earn structural discovery or any claim about the BBGKY-to-Boltzmann passage.
