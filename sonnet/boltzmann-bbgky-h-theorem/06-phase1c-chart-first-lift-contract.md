# Phase 1C contract — chart-first dual-process lift

**Status:** frozen before Phase 1C execution.

**Logical status:** this file is later in repository chronology but earlier in
the research dependency graph than Phases 1A and 1B.  Those phases are retained
as post-hoc kinetic controls.  They no longer define the mother route.

**Planned executable owner:**
`tests/research/test_chart_first_collision_lift.py`.

**Planned result owner:**
`07-phase1c-chart-first-lift-results.md`.

## 1. Correction and purpose

The previous route began with the known H theorem and then asked whether its
logarithmic flux--affinity structure matched Addition and Multiplication.
That is a useful calibration, but it does not answer the first-principles
question.

Phase 1C begins instead with a physical evolution law and lifts every scalar
quantity into one declared chart carrying two process components.  Only after
the lifted dynamics, its gauge freedom, its observer lowering, and its
continuation residual have been determined may a monotone functional be
searched for.

The dependency order is therefore

[
	ext{physical dynamics}
longrightarrow
	ext{lossless chart lift}
longrightarrow
	ext{dual-process dynamics}
longrightarrow
	ext{observer/task lowering}
longrightarrow
	ext{Lyapunov search}.
]

No entropy, logarithmic covector, Maxwellian, partition function, or
molecular-chaos closure is permitted in the Phase 1C solver.

## 2. Three distinct objects

For every scalar physical quantity (u), distinguish:

1. the physical value (u);
2. a homogeneous chart representative ((x_u,y_u)), with (y_u>0);
3. the two process velocities ((A_u,M_u)) along a lifted history.

The decoder is

[
pi_chi(x_u,y_u)=-rac{x_u}{y_u}=u.
]

The process velocities are

[
A_u=-rac{dot x_u}{y_u},
qquad
M_u=-rac{dot y_u}{y_u}.
]

Direct differentiation gives the exact tangent decoder

[
oxed{dot u=A_u+uM_u.}
]

Thus (A_u) is the additive process component and (M_u) is the
multiplicative rate component in this chart.  They are process quantities,
not two independent physical observables and not yet a quotient.

This is the homogeneous form of the affine A/M process coframe.  If a fibre
coordinate (v) is introduced only for comparison, then
(	heta_A=du-u,dv), (	heta_M=dv), and
(du=	heta_A+u	heta_M).  Phase 1C performs no logarithmic coordinate
construction and does not use (v) computationally.

## 3. Fibre gauge and connection

The homogeneous representative has the time-dependent gauge freedom

[
(x_u,y_u)longmapsto(ho x_u,ho y_u),
qquad ho>0.
]

Writing (kappa=dotho/ho), its process velocities transform as

[
A_ulongmapsto A_u+ukappa,
qquad
M_ulongmapsto M_u-kappa.
]

The decoded tangent is invariant:

[
(A_u+ukappa)+u(M_u-kappa)=A_u+uM_u.
]

A physical ODE

[
dot u=F(u)
]

therefore lifts first to the affine constraint

[
A_u+uM_u=F(u).
]

A **connection** or chart policy chooses one point of this affine fibre.  It is
additional structure and must not be confused with the decoder.  Phase 1C
compares three frozen policies:

| policy | (A_u) | (M_u) | domain |
| --- | ---: | ---: | --- |
| additive | (F) | (0) | all decoded scalars |
| multiplicative | (0) | (F/u) | (u
e0) |
| gain--loss | (G) | (-
u) | (F=G-
u u) |

All three must decode to the same base tangent on their common domain.  No
policy is called canonical merely because it is convenient.

## 4. First-principles collision lift

For a positive kinetic density, write the collision law in its primitive
gain--loss form

[
D_tf=Q^+(f,f)-
u[f],f,
qquad
D_t=partial_t+vcdot
abla_x.
]

The chart-first collision connection is

[
oxed{A_f=Q^+(f,f),qquad M_f=-
u[f].}
]

This choice is admissible without mentioning entropy:

- (A_fge0) is incoming additive supply;
- (M_fle0) is the multiplicative survival/hazard rate;
- (A_f+fM_f) is exactly the original collision operator;
- the two components retain the gain/loss orientation erased by their sum.

For one frozen reversible channel

[
(0,1)longleftrightarrow(2,3),
qquad
X=f_0f_1,quad Y=f_2f_3,
]

with rate (c>0), set

[
F=c(-X+Y,-X+Y,X-Y,X-Y).
]

The gain--loss process components are frozen as

[
egin{array}{c|cc}
i&A_i&M_i\ hline
0&cY&-cf_1\
1&cY&-cf_0\
2&cX&-cf_3\
3&cX&-cf_2.
end{array}
]

The executable must reconstruct (F_i=A_i+f_iM_i) exactly and must integrate
the homogeneous chart equations

[
dot x_i=-y_iA_i,
qquad
dot y_i=-y_iM_i
]

back to the same base tangent.

## 5. Compositional laws to test

The lift must respect the product operation without choosing an entropy
coordinate.  If (w=uv), then

[
A_w=vA_u+uA_v,
qquad
M_w=M_u+M_v,
]

and hence

[
dot w=A_w+wM_w.
]

For a positive weighted lowering

[
q=sum_alpha w_alpha u_alpha,
qquad w_alphage0,
]

freeze

[
A_q=sum_alpha w_alpha A_alpha,
qquad
M_q=
rac{sum_alpha w_alpha u_alpha M_alpha}
     {sum_alpha w_alpha u_alpha}
]

when (q>0).  This gives

[
dot q=A_q+qM_q
      =sum_alpha w_alphadot u_alpha.
]

The formula is a chart-compatible lowering law.  It does not claim that
Addition and Multiplication alone determine a unique connection for arbitrary
signed cancellation.

## 6. Minimal BBGKY seam

Use a finite exact two-particle Markov collision process on ordered pair states
((i,j)in{0,1,2}^2).  The only active transitions are

[
(0,0)ightleftarrows(1,2),
qquad
(0,0)ightleftarrows(2,1),
]

all with the same positive rate (c).  Let (P_{ij}) be the exact two-body
law and define the exchange-averaged one-body marginal

[
f_i=rac12left(sum_jP_{ij}+sum_jP_{ji}ight).
]

At pair level, the Markov generator has the exact gain--loss lift

[
A^{(2)}_{ij}
 =sum_{kell	o ij}c_{kell,ij}P_{kell},
qquad
M^{(2)}_{ij}
 =-sum_{ij	o kell}c_{ij,kell}.
]

Lower it using the rule of Section 5 to obtain
((A^{(1)}_i,M^{(1)}_i)).  The executable must verify

[
dot f_i=A^{(1)}_i+f_iM^{(1)}_i
        =L_idot P.
]

It must then exhibit two exchange-symmetric positive two-body laws with the
same one-body marginal but different one-body process pairs and different
next derivatives.  This is an exact continuation-residual witness:

[
P
ewidetilde P,quad LP=Lwidetilde P,
quad
Lmathcal GP
e Lmathcal Gwidetilde P.
]

The witness proves only that the one-body marginal is not sufficient for the
next-derivative task.  It does not prove a Boltzmann--Grad limit, propagation
of chaos, or a universal entropy law.

## 7. Frozen witnesses

Use the following two exchange-symmetric probability laws.

**Diagonal law**

[
P_{00}=P_{11}=P_{22}=rac13,
]

with all other entries zero.

**Off-diagonal law**

[
P_{ij}=rac16quad(i
e j),
]

with all diagonal entries zero.

Both have the uniform one-body marginal.  Their derivatives under the frozen
generator must differ exactly.  Zeros are intentional boundary data; a
separate strictly positive perturbation sharing the same marginal must also be
tested so that the residual is not attributed only to the boundary.

## 8. Oracle firewall

The implementation may use:

- rational arithmetic;
- homogeneous ratios;
- finite products and sums;
- exact differentiation identities;
- nonnegative Markov or collision rates;
- marginalization.

It may not import or evaluate:

- (H[f]), (flog f), Shannon entropy, or relative entropy;
- a logarithm or exponential;
- a Maxwellian or Gibbs law;
- the classical entropy-production factorization;
- Phase 1B's learned character.

The words above may appear in this contract and in firewall assertions, but
the executable discovery path must contain no logarithmic numerical oracle.

## 9. Certificates

1. projective decoder certificate;
2. exact tangent-decoder certificate;
3. time-dependent gauge covariance;
4. equality of additive, multiplicative, and gain--loss base tangents;
5. nonnegative-gain/nonpositive-rate cone for positive collision states;
6. exact one-channel collision reconstruction;
7. exact product-process composition;
8. exact marginal-lowering square;
9. equal-marginal/different-derivative BBGKY witness;
10. strictly positive version of the residual witness;
11. collision-involution covariance;
12. mass conservation before and after lowering.

## 10. Red teams and kill conditions

The phase fails or must be weakened if:

- the homogeneous chart changes the decoded physical ODE;
- a gauge-dependent split is reported as a physical observable without a
  declared connection;
- the gain--loss split is called unique without frozen locality/cone axioms;
- marginal lowering fails to commute with the generator;
- the residual witness changes the declared one-body marginal;
- the only residual witness relies on zero probabilities;
- an entropy or logarithmic oracle enters candidate selection;
- BBGKY observer order (s) is renamed arithmetic rank (r);
- a one-step derivative certificate is called full future reconstruction.

## 11. Rank and observer ledger

Phase 1C occupies one arithmetic rank and two observer orders.  A useful
notation is

[
X_{r,s}^{(chi)},
]

where (r) is arithmetic/process rank, (s) is correlation/observer order,
and (chi) is the chart/connection choice.  None of these indices determines
the others.

The Phase 1C pair-level to marginal-level map moves from (s=2) to (s=1)
at fixed (r).  It is not rank raising.  Higher-rank observations remain a
separate vertical program requiring objectification, new free composition,
and a lowering law on every legal composite.

## 12. Budget and claim boundary

The executable must use exact `Fraction` arithmetic, remain below one second
on the routine fixture, introduce no dependency, and remain research-local.

Passing Phase 1C would establish an exact chart-first reexpression of a finite
collision law and an exact finite continuation-residual witness.  It would
not establish:

- a new H theorem;
- discovery of entropy;
- uniqueness or canonicity of the gain--loss connection;
- a continuum Boltzmann or BBGKY theorem;
- a microscopic derivation of molecular chaos;
- a new arithmetic rank;
- a generic package API.
