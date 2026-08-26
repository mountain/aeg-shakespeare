# Phase 1A results — finite detailed-balance H theorem

Status: Phase 1A passed on the frozen model. This is a level-1 reexpression result, not structural discovery.

**Route correction after Phase 1C:** this result is retained as a post-hoc
kinetic control. It supplies the classical monotonicity answer and tests the
finite collision algebra, but it is not an input to the chart-first derivation.
The mother route now constructs layer-relative semantic adapters and an
autonomous target dynamics before reopening any H search.

## 1. Executed artifact

The executable record is tests/research/test_discrete_velocity_h_theorem.py.

It uses exactly the contract committed before implementation:

- six velocities \(\{\pm e_x,\pm e_y,\pm e_z\}\);
- three opposite-pair collision complexes \(X,Y,Z\);
- the reversible triangle \(X\rightleftarrows Y\rightleftarrows Z\rightleftarrows X\);
- conductances \((1,2,3)\);
- reference weights \(M=(1,2,3,6,3,2)\), whose three pair products are all 6;
- exact rational arithmetic and symbolic logarithmic identities.

No model parameter or witness was changed after the contract was frozen.

## 2. Exact result

For \(q_i=f_i/M_i\), an oriented collision channel

\[
(a,b)\longrightarrow(c,d)
\]

has activities \(A=q_aq_b\), \(B=q_cq_d\), flux

\[
J=c(A-B),
\]

and stoichiometric increment

\[
J(e_c+e_d-e_a-e_b).
\]

For

\[
\mathcal H_M(f)
=
\sum_i\left[f_i\log(f_i/M_i)-f_i+M_i\right],
\]

the executable symbolic calculation gives

\[
\dot{\mathcal H}_M
=
-\sum_\gamma c_\gamma
(A_\gamma-B_\gamma)
(\log A_\gamma-\log B_\gamma)
\le 0.
\]

The inequality is certified channel by channel from exact positive-rational
ordering and strict monotonicity of logarithm. No floating-point sign test is
used.

## 3. Certificate ledger

| Contract item | Executable witness | Result |
| --- | --- | --- |
| frozen velocity alphabet and collision graph | test_frozen_velocity_channels_are_reversible_and_conservative | pass |
| history reversal involution | the same test plus double reversal | pass |
| mass, momentum, kinetic-label conservation | exact stoichiometric sums | pass |
| reference detailed balance | test_frozen_reference_has_exact_detailed_balance | pass |
| orientation-independent vector field | test_reversing_channel_orientation_preserves_the_vector_field | pass |
| channel derivative identity | test_symbolic_channel_derivative_is_flux_times_affinity | pass |
| nonpositive exact rational H rate | test_exact_rational_h_rate_is_nonpositive_with_componentwise_equality | pass |
| componentwise equality characterization | the same test and disconnected red team | pass |
| inward boundary vector field | exhaustive \(3^6=729\)-state audit | pass |
| entropy sign convention | test_entropy_sign_is_opposite_to_h_sign | pass |

The targeted local run completed all 10 tests in 1.48 seconds.

## 4. Red-team ledger

### RT1 — reversibility is insufficient

For one two-way reaction with \(k_+=2\), \(k_-=1\), \(A=1\), and
\(B=3/2\),

\[
J=\frac12,
\qquad
\dot H=\frac12\log(3/2)>0.
\]

Thus the availability of both collision orientations does not imply the chosen
H theorem. A positive reference measure that symmetrizes the forward and
reverse rates is essential.

### RT2 — the reference measure is active structure

Changing \(M_5\) from 2 to 1 changes the \(Z\)-pair reference product from 6
to 3. The model validator rejects the H certificate. The reference measure is
not an additive normalization detail.

### RT3 — equality follows the collision-complex graph

With only \(X\rightleftarrows Y\), zero dissipation requires the \(X\) and
\(Y\) activities to agree but leaves \(Z\) unconstrained. On the connected
triangle, equality becomes

\[
q_0q_3=q_1q_4=q_2q_5.
\]

It does not require every \(q_i\) to equal one. Conserved directions and graph
connectivity determine the equilibrium manifold.

### RT4 — the boundary needs a different certificate

The vector field was checked on all population vectors in
\(\{0,1,2\}^6\). Every zero coordinate has nonnegative derivative, so the
nonnegative orthant is inward invariant on this fixture. The logarithmic
dissipation identity remains an interior result; it is not evaluated at
\(\log0\).

### RT5 — H and entropy have opposite orientation

For positive \(k_B\), \(S=-k_B\mathcal H_M\), hence

\[
\dot{\mathcal H}_M\le0
\quad\Longleftrightarrow\quad
\dot S\ge0.
\]

## 5. What the A/M reading actually earned

This phase exposes a precise but limited A/M structure:

1. Multiplication forms the incoming and outgoing pair activities.
2. The positive reference measure forms the dimensionless ratios \(q_i=f_i/M_i\).
3. Logarithm is the character from positive Multiplication to Addition.
4. Stoichiometric Addition pairs the antisymmetric flux with the additive affinity.
5. A sum over channels assembles local nonnegative dissipation certificates.

Power is not needed for the finite H identity. Forcing a P operation into this
phase would be decorative rather than explanatory. Power or exponential-family
structure remains a separate question for the partition-function control and
the hidden-oracle discovery phase.

The sharper structural condition is not bare reversibility but
**reference-measure symmetrizability**: forward and reverse physical rates must
admit a common positive conductance after division by the equilibrium pair
weights. That factorization is what turns collision reversal into a signed
square-like monotone pairing.

## 6. Process-geometry interpretation

The result supports the initial intuition only at the reduced kinetic level.
Once the finite collision vector field is declared, its H theorem can be read
as a local law on reversible channel generators:

\[
\text{multiplicative imbalance}
\times
\text{additive log affinity}
\ge0.
\]

It does not yet explain why a reversible microscopic system should lower to
that vector field. There is no history quotient, BBGKY marginal tower,
molecular-chaos section, singular limit, or missing reverse decoder in Phase
1A. Consequently, this result does not locate the origin of physical time's
arrow.

It also yields no higher-rank result. Collision-complex connectivity is an
observer structure at the current rank, not evidence that the arithmetic tower
has risen.

## 7. Claim boundary

Phase 1A earns exactly this claim:

> The frozen finite detailed-balance collision network has an exact
> process-local relative H theorem. Pair Multiplication, logarithmic additive
> affinity, reversible channel involution, and the positive reference measure
> jointly produce a nonnegative dissipation certificate.

It does not earn:

- discovery of the logarithm or relative entropy;
- uniqueness of H among candidate functionals;
- a continuum collision theorem;
- a derivation from finite-N mechanics;
- a BBGKY closure or propagation-of-chaos result;
- a universal entropy law across arithmetic ranks;
- any public API extraction.

## 8. Next gate

Proceed to Phase 1B under an information firewall:

1. freeze several training and held-out collision graphs;
2. hide \(f\log f\), the entropy name, Maxwellians, and the classical
   factorization from the solver;
3. search a declared A/M-native covector grammar;
4. quotient by conserved affine gauges;
5. compare with the hidden oracle only after ranking candidates;
6. report coverage and uniqueness separately.

Phase 2, which asks what one-body observation forgets, remains downstream of
that discovery gate.

