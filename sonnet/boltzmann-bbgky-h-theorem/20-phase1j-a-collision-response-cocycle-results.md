# Phase 1J-A results — ordered collision response reaches C2

**Status:** passed on the frozen finite carrier.

**Contract:**
[`19-phase1j-a-collision-response-cocycle-contract.md`](./19-phase1j-a-collision-response-cocycle-contract.md).

**Executable:**
[`test_collision_response_cocycle.py`](../../tests/research/test_collision_response_cocycle.py).

## 0. Result in one sentence

Two overlapping reversible XOR collision cells induce a noncommutative
renewed target action (C0), exact retained-law response reconstruction whose
forgotten form is genuinely set-valued (C1), and an exact state-dependent
response cocycle (C2); the parity product character is exposed, but no closed
covector, H potential, continuum transfer, generic calculus, or rank promotion
is claimed.

## 1. Exact execution ledger

The executable contains ten tests and passed in approximately (0.27) seconds
on the reference Python 3.12 environment.

| Certificate | Exact scope | Result |
|---|---:|---|
| local reversible collisions | 2 gates, 8 microstates | pass |
| target formula/baseline agreement | 3 rational target states, 2 gates | 6/6 pass |
| target word action | 3 states, 25 prefix/suffix pairs | 75/75 pass |
| C1 reconstruction | 36 positive laws, 2 gates | 72/72 pass |
| forgotten response fibre | 6,435 denominator-eight laws scanned; 57 in the fixed fibre | exact five-valued relation |
| C2 cocycle | 36 positive laws, 25 prefix/suffix pairs | 900/900 pass |
| naive-addition red team | 1 frozen correlated law | counterexample; transport repairs it |
| product character | 3 rational states, 2 gates | 6/6 pass |
| chart ledger | 2 charts, 5 cost axes | recorded |
| claim grading | C0--C4 plus continuum/H/rank | stops at C2 |

All probabilities and responses are `Fraction` values.  No random or
floating-point evidence enters a certificate.

## 2. C0: collision-derived order survives lowering

Each collision gate is a pair-local bijective involution and leaves the third
site fixed.  On the microscopic witness ((1,0,0)), left-then-right and
right-then-left give respectively

\[
(1,1,1)
\qquad\text{and}\qquad
(1,1,0).
\]

Order remains visible in the renewed target process.  For

\[
p=\left(\frac14,\frac13,\frac25\right),
\]

the two chronological words give

\[
B_{(L,R)}(p)
=
\left(\frac14,\frac5{12},\frac{29}{60}\right),
\]

\[
B_{(R,L)}(p)
=
\left(\frac14,\frac5{12},\frac7{15}\right).
\]

The independent-section target formula agrees exactly with direct
microscopic pushforward.  Empty words act as the identity, and every frozen
prefix/suffix pair satisfies chronological concatenation.  This passes C0
for the declared renewed target action.

It does not prove that (pi) is a quotient of the microscopic collision
process.  C1 supplies the obstruction.

## 3. C1: exact reconstruction is retained-law, not base-only

For all 72 positive-law/gate cases,

\[
\pi U_gF=B_g(\pi F)+r_g(F)
\]

held exactly.  Thus retaining the microscopic law gives a regular response
section for the next-observation task.

After microscopic forgetting, fix

\[
p=\left(\frac12,\frac12,\frac12\right).
\]

Among the 6,435 denominator-eight probability tables, exactly 57 have these
three one-site occupancies.  Their left-collision response relation is

\[
\mathcal R_L(p)
=
\left\{
\left(0,-\frac12,0\right),
\left(0,-\frac14,0\right),
(0,0,0),
\left(0,\frac14,0\right),
\left(0,\frac12,0\right)
\right\}.
\]

Two explicit laws with the same (p) require the extreme responses
((0,-1/2,0)) and ((0,1/2,0)).  The independent section requires zero.
Consequently no function of (p) and the gate alone can reconstruct all
three microscopic continuations.  The honest forgotten object is the exact
five-valued relation, not a secretly chosen response.

This is a positive C1 result with retained source data and a negative descent
result after forgetting.

## 4. C2: nonlinear transport repairs response composition

For every frozen law and prefix/suffix pair, the executable verified

\[
r_{u\mathbin{\|}v}(F)
=T_v\bigl(B_u(\pi F),r_u(F)\bigr)+r_v(U_uF),
\]

with

\[
T_v(y,r)=B_v(y+r)-B_v(y).
\]

The identity passed 900 exact cases, including empty words and both collision
orders.  This earns C2 for the retained-law response section on the frozen
word atlas.

The transport is essential.  For the positive denominator-ten law with
counts

\[
(1,1,1,1,1,1,1,3),
\]

the base state is ((3/5,3/5,3/5)) and

\[
r_L(F)=\left(0,-\frac2{25},0\right),
\qquad
r_R(U_LF)=\left(0,0,\frac2{25}\right).
\]

Naive addition predicts

\[
\left(0,-\frac2{25},\frac2{25}\right),
\]

but the exact composite response is

\[
r_{(L,R)}(F)=\left(0,-\frac2{25},\frac{12}{125}\right).
\]

Transport changes the earlier response to

\[
T_R\left(B_L(p),r_L(F)\right)
=
\left(0,-\frac2{25},\frac2{125}\right),
\]

whose sum with the later response is exactly (r_{(L,R)}(F)).  The missing
(2/125) is the state-dependent cross effect of the second bilinear target
map.  Correlation responses therefore do not compose by free vector addition.

## 5. Collision-product chart and the C3 boundary

For occupancy (p), a gate (i\to j) has the bilinear law

\[
p_j'=p_i+p_j-2p_ip_j.
\]

The parity character

\[
z(p)=1-2p
\]

turns it into

\[
z_j'=z_i z_j.
\]

This identity passed on all six frozen state/gate pairs.  It is the first
collision-derived composition character in this Sonnet: the simpler
multiplicative rule follows from the actual overlapping collision fixture,
not from the adjacent affine A/M control used in Phase 1I.

The chart does not yet select a closed one-form.  Its admitted image includes
(z=0) and negative values, so a real log chart would be partial and would
add an analytic primitive excluded by the contract.  No derivative or
integration test was performed.  C3 is therefore **not selected**, not
failed.

## 6. Five-axis chart audit

| Cost axis | Occupancy chart | Parity-character chart | Verdict |
|---|---|---|---|
| target dynamics | bilinear XOR formula | one multiplication | parity simpler |
| composition | ordered target maps | collision-product character | parity exposes the native product |
| covector | none selected | log candidate is partial | inconclusive at C3 |
| decoder | identity | affine half-map | occupancy simpler |
| response | additive correction, nonlinear transport | character difference, not free addition | neither removes retained-law dependence |

The audit is a structural ledger, not a scalar economy theorem.  It records a
real tradeoff: the parity chart lowers target formula complexity but adds a
decoder and does not eliminate the response fibre.

## 7. Red-team outcomes

| Red team | Outcome |
|---|---|
| reverse collision order | both microscopic and target outputs change |
| change correlations at fixed one-site marginals | response ranges from (-1/2) to (1/2) |
| use renewed zero response on correlated laws | exact reconstruction fails |
| add consecutive response vectors | misses the third component by (2/125) on the frozen witness |
| transport the earlier response | exact composite reconstruction restored |
| apply a log chart across (z=0) or sign changes | domain mismatch |
| identify target action with microscopic quotient | rejected by the five-valued response relation |

## 8. Claim grade

| Gate | Grade | Boundary |
|---|---|---|
| C0 action skeleton | **pass** | ordered renewed collision-word action |
| C1 response reconstruction | **pass** | regular with retained microscopic law |
| C1 after forgetting | **counterexample to uniqueness** | exact set-valued relation |
| C2 regular cocycle | **pass** | state-dependent transport on frozen words |
| C3 closed covector | **inconclusive / not selected** | product character only |
| C4 effective compression | **not tested** | full microscopic law still retained |
| continuum H response | **not claimed** | Phase 1J-B estimate required |
| generic fibre calculus | **not claimed** | single finite XOR domain |
| arithmetic rank | **unchanged** | no new object type or cross-domain transfer |

## 9. What changed

Phase 1I could say only that an exact one-step response existed and that naive
residual addition failed.  Phase 1J-A now supplies the missing positive
structure on a genuinely ordered collision fixture:

1. a collision-derived noncommutative target action;
2. a typed set-valued response relation after forgetting;
3. a regular response section when microscopic data are retained;
4. the exact nonlinear transport law required for composition;
5. a collision-product character arising from the same fixture.

This is a meaningful advance from a response ledger to a bounded C0--C2
calculus.  It does not answer future adequacy or effective compression, and
it does not transfer to hard spheres.

## 10. Arithmetic Universality result

The fixture provides bounded U2/U4 pressure: the parity character converts
the native XOR collision update from an additive/bilinear probability formula
to multiplication.  The C2 law also provides an exact calculational benefit
by locating the cross term that naive residual addition misses.

The evidence remains arithmetic-specific and one-domain.  It earns no U5
universality claim, rank promotion, or generic API.

## 11. Repository effects

### Mathematical Core

Unchanged.  The result is a research-local finite theorem, not a domain-
independent law.

### Engineering Architecture

No public change.  The executable essay keeps target action, response
relation, retained response, transport, and chart ledger as local types.

### Theory Map

Unchanged.  The result strengthens the empirical basis of the response/
covariance transversal but does not promote a node or edge.

### Research Program

Phase 1J-A is complete through C2.  The next honest gate is Phase 1J-B: state
a continuum correlation response in the weak collision-flux topology of
Phases 1E/1F and prove a bound strong enough to pair with the intended
covector.  Bulk (L^1) control alone remains insufficient.
