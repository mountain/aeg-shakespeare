# Phase 1F results — weak flux and one-collision continuation

**Status:** six exact research-local certificates passed.  The continuum weak
BBGKY, Duhamel, and Deng--Hani--Ma statements remain external theorem records.

**Contract:**
`11-phase1f-weak-mild-continuation-cell-contract.md`.

**Executable:**
`tests/research/test_weak_collision_history_cell.py`.

## 1. Outcome

Phase 1F answers the next question left by the boundary-trace obstruction.

> A safe weak adapter does not decode a boundary trace from a bulk state.  It
> takes an oriented collision-event/flux measure as additional source data and
> preserves only its pairing with a declared observable over a declared
> horizon.

The minimal mild continuation unit is

\[
T_s(T-\tau)
\circ C_{s,s+1}^{\epsilon,N}
\circ T_{s+1}(\tau),
\]

integrated over the collision time and collision variables.  It is exactly a
source free segment, an oriented collision insertion, and a target free
segment.  One such cell is not the full future: all omitted cells and
recollisions remain in a truncation/history residual.

The phase also finds a second chart boundary.  Pointwise A/M coordinates do
not descend to a single observer-independent time-averaged A/M pair.  The
effective multiplicative coordinate for one weak task is weighted by that
task's observable and occupation measure.

## 2. Frozen one-collision history

The exact shadow uses

\[
x_T=(1,2),\qquad v=(1,0),\qquad T=3/2,
\]

\[
u=(-1,0),\qquad
\omega=(-3/5,-4/5),\qquad
w=5/6,
\]

with \(\epsilon=1/10\), prefactor \(\alpha=7/6\), and

\[
f_0(x,v)=10+x_0+2x_1+v_0^2.
\]

Because \(\omega\cdot(u-v)=6/5\), the quadrature coefficient
\(w(\omega\cdot(u-v))_+\) is exactly one.  Along every frozen free segment,
each one-body density is affine in the collision time \(\tau\); its
factorized pair weight is quadratic.  Exact rational Simpson evaluation is
therefore an identity, not a numerical approximation for this fixture.

### 2.1 History reconstruction certificate

At \(\tau=2/3\), the executable:

1. transports the endpoint root backward to the contact point;
2. applies the elastic involution to obtain incoming root/partner velocities;
3. transports both incoming particles backward to time zero;
4. transports them forward again to the declared contact points;
5. reflects the velocities and recovers the endpoint root exactly.

All position, momentum, energy, contact, and endpoint identities use
`fractions.Fraction` equality.

### 2.2 Integrated gain/loss certificate

The time-integrated positive flux pair is

| quantity | exact value |
| --- | ---: |
| integrated gain \(\mathcal A_T\) | \(273\,506\,541/781\,250\) |
| integrated loss \(\mathcal L_T\) | \(164\,633/400\) |
| signed weak collision contribution | \(-384\,338\,297/6\,250\,000\) |

Both gain and loss are positive even though their signed difference is
negative.  This is the time-integrated analogue of the Phase 1E positive cone,
but it is indexed by the chosen horizon, collision quadrature, and weak
observable.

### 2.3 Time-cut certificate

For the exact cut \(c=5/8\), the executable verifies

\[
\mathcal A_{[0,T]}
=\mathcal A_{[0,c]}+\mathcal A_{[c,T]},
\qquad
\mathcal L_{[0,T]}
=\mathcal L_{[0,c]}+\mathcal L_{[c,T]}.
\]

This is additivity of the collision-flux measure under a cut of its time
domain.  It is not a Markov or semigroup theorem for the reduced state.

## 3. Exact A/M averaging obstruction

Pointwise on the loss branch,

\[
L(\tau)=F(\tau)\nu(\tau),
\qquad M(\tau)=-\nu(\tau),
\qquad F(\tau)M(\tau)=-L(\tau)
\]

holds exactly.  Now choose the nonconstant weak observer

\[
\phi(\tau)=1+\tau/3.
\]

The fixture obtains

| quantity | exact value |
| --- | ---: |
| observed occupation \(\int\phi F\) | \(435/16\) |
| observed A/M contribution \(\int\phi FM\) | \(-10\,353/20\) |
| unweighted rate average \(T^{-1}\int M\) | \(-5\,677/300\) |
| observer/occupation-weighted rate | \(-476/25\) |

Consequently

\[
\left(\int\phi F\right)
\left(\frac1T\int M\right)
\ne
\int\phi FM,
\]

while

\[
M_{\phi,T}^{\mathrm{eff}}
=
\frac{\int\phi FM}{\int\phi F}
=-\frac{476}{25}
\]

reproduces this one weak task exactly.

This supports the chart-first intuition with a necessary qualification:

- the pointwise chart is selected by the local state and collision flux;
- lowering it to a horizon-level chart requires a declared observer-weighted
  occupation measure;
- the resulting scalar is task-specific and is not a closed process state.

## 4. Exact cut-composition shadow

The finite rational kernel fixture obtains

\[
I_{M_2}(Q)=(3,35/12),
\qquad
I_{M_1}(I_{M_2}(Q))=\frac{3689}{420}.
\]

Direct evaluation of the full double sum gives the same value.  This is the
exact finite form of

\[
I_M=I_{M_1}\circ I_{M_2}.
\]

The certificate deliberately proves only Fubini/operator composition.  It
does not turn the cut into physical time evolution, a decoder, or a new
arithmetic rank.

## 5. Reading the Deng--Hani--Ma construction

The Phase 1F reading is now more precise than the earlier general analogy.

### 5.1 The partial expansion is a selective continuation policy

At each time layer, Deng--Hani--Ma expand cumulants into local Duhamel
integrals, stop at leading \(f_A\) factors, and recursively expand only the
earlier cumulants.  The stop/continue decision is not bookkeeping: it prevents
the leading terms from accumulating the uncontrolled full time-expansion
growth.

In process-geometry terms, the proof does not seek one representation that is
equally adequate for every continuation.  It uses two adapted continuations:

| component | continuation policy | target certificate |
| --- | --- | --- |
| leading \(f_A\) | stop and compare with Boltzmann | kinetic leading term |
| connected cumulant \(E_H\) | continue through earlier layers | small connected residual |

This is concrete evidence for replacing global semantic equivalence by
layer- and task-specific continuation adaptation.

### 5.2 A molecule is a lossy but useful history presentation

The molecule retains collision graph, particle-line incidence, collision
order, roots, and time layers.  It forgets exact positions, velocities, and
collision times.  That loss is acceptable for the integral-estimation task
because the associated operator and constraints still support the required
cutting argument.

The important point is not merely that information was forgotten.  It is that
the retained presentation remains compositionally usable for the declared
estimate.  This matches the current objectification intuition, while still
falling short of arithmetic-rank promotion because no new free grammar and
all-composite lowering have been proved.

## 6. Executed certificates

Six exact tests pass:

1. backward source reconstruction reaches contact and the target endpoint;
2. the integrated collision observable has positive gain/loss parts;
3. collision-flux integration is additive under an exact time cut;
4. pointwise A/M requires observer-weighted, not unweighted, averaging;
5. a molecule cut lowers to exact Fubini/operator composition;
6. weak state, collision flux, one Duhamel term, full continuation, and
   objectification claims remain separately graded.

Together with Phases 1C and 1E, the focused dependency-free run now contains
23 exact certificates.

## 7. Claim boundary

Phase 1F has earned:

- a precise weak collision-flux adapter contract;
- a typed one-collision Duhamel continuation cell;
- exact history reconstruction and time-cut certificates;
- an exact observer-weighted A/M averaging obstruction;
- an exact Fubini composition shadow of molecule cutting;
- a more concrete reading of partial expansion as a selective continuation
  translator.

It has not earned:

- a boundary flux measure from arbitrary bulk \(L^1\) correlations;
- an independent derivation of the weak BBGKY or Duhamel hierarchy;
- control of the two-or-more-collision tail or recollisions;
- a proof of the Deng--Hani--Ma estimates;
- an observer-independent integrated A/M state;
- a full microscopic decoder, H theorem, or arithmetic-rank objectification.

## 8. Next gate

The next gate is no longer to add another isolated collision identity.  It is
to freeze a **two-cell selective continuation comparison**:

1. one leading branch that stops at \(f_A\);
2. one connected branch that continues through an earlier cumulant;
3. a declared cut interface and truncation residual;
4. a time-reversal red team showing why the same continuation policy cannot be
   used symmetrically in both directions;
5. only then, a target-semigroup/H question on the stopped kinetic branch.

That comparison will decide whether layer-wise semantic adaptation is merely
descriptive vocabulary or a calculable rule for choosing which histories to
continue and which to stop.

## 9. Repository effect

### Mathematical Core

Refinement pressure only.  The result gives one concrete selective
continuation adapter but does not yet justify a general law.

### Engineering Architecture

Research-local refinement.  The executable separates state, flux, history,
observer, cut, and tail residual; no dependency, backend, or API is added.

### Theory Map

Unchanged.  The result supports the adaptation transversal and sharpens the
composition/objectification boundary without promoting a node or edge.
