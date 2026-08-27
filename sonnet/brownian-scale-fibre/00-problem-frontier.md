# Problem frontier: recalculate Brownian motion from process fibres

Status: frozen S0/S1 contract for
[#158](https://github.com/mountain/process-geometry/issues/158), downstream of
[#140](https://github.com/mountain/process-geometry/issues/140) and the
native-method firewall merged in
[#157](https://github.com/mountain/process-geometry/pull/157).

## 1. Primitive process before the continuum answer

The first carrier is the finite history space

\[
\Omega_N=\{\xi_1\cdots\xi_N:\xi_j\in\{-1,+1\}\}
\]

with chronological concatenation.  The endpoint task is

\[
\pi_N(\omega)=\sum_{j=1}^N\xi_j,
\qquad
K_N(0,x)=\frac{|\pi_N^{-1}(x)|}{|\Omega_N|}.
\]

The literal history, endpoint, fibre multiplicity, and pushforward probability
are different objects.  For the endpoint task, concatenation gives exactly

\[
K_{N+M}(0,z)=\sum_x K_N(0,x)K_M(x,z).
\]

The executable phase proves this first as an integer fibre-count identity.  It
does not infer that two paths with the same endpoint are equivalent for
first-passage, maximum, occupation, or physical-decoder tasks.

## 2. Blind scale obligation without a supplied Gaussian

For a centered finite increment law, let

\[
\kappa(s)=\log\mathbb E[e^{s\xi}].
\]

Independence makes the aggregate response additive: the log response of
\(N\) increments at probe scale \(N^{-a}s\) is

\[
N\kappa(N^{-a}s).
\]

The native calculation reads the raw law and certifies exactly

\[
\kappa(0)=\kappa'(0)=0,
\qquad
\kappa''(0)=\sigma^2>0.
\]

This is not used as a truncated power series.  The exact integral identity

\[
\kappa(s)=\int_0^s(s-u)\kappa''(u)\,du
\]

shows that the first active centered response has order two.  Population
growth and probe contraction therefore balance only when

\[
1-2a=0.
\]

The software solves that equation after discovering the active order; it is
not passed \(a=1/2\).  For the symmetric unit law, one may independently sharpen
the residual by

\[
\log\cosh s-\frac{s^2}{2}
=-\int_0^s(s-u)\tanh^2u\,du.
\]

This phase certifies a necessary nontrivial scale and its local response
coefficient.  It does **not** yet prove convergence to a Gaussian law or a
continuum path process.

## 3. Method firewall

S0/S1 have no allowed lowering witness.  The native source contains only the
finite increment law, exact centered response, chronological histories,
endpoint fibres, and their composition.  Classical local expansion,
transform, continuum PDE, and simulation routes are declared separately in
`phase0_contract.py` and cannot enter a native trace without a later
task-adequacy witness.

This is deliberately stronger than asking an agent not to use an oracle in
prose: the merged method tool rejects the corresponding event in a native lane.

## 4. Held-out and red-team cases

- A biased finite law returns the typed result `centering-required`; the drift
  cannot be hidden inside a fluctuation scale.
- An infinite-variance law is outside the first finite-law grammar.  A later
  heavy-tail phase must enlarge the carrier and rediscover its scale rather
  than force the diffusive answer.
- Histories `(+1,-1)` and `(-1,+1)` share endpoint zero but have different
  running maxima.  Endpoint fibres are task-exact only for endpoint observers.
- Lattice return to a point, continuum return to a neighbourhood, and
  continuum hitting of a singleton remain separate S2 claims; the 2D boundary
  is not compressed into one word, “recurrent.”

## 5. Relation to the larger programme

This is the first independent scale/fibre family after the Bessel-based draft
in PR #141.  It pressures U1, U2, U3, U4, and Effective Analysis because the
same construction connects raw histories, scale, measured fibres, a continuum
lowering, and later physical response.  At S0/S1 it remains T1 and leaves the
Mathematical Core, Engineering Architecture, Theory Map, dependencies, and API
unchanged.

Surreal numbers are not needed for this finite-height task.  That is a negative
runtime result, not an argument against later AMP or higher-height uses.

## 6. Claim ceiling

No new Brownian theorem, central-limit theorem, heat-kernel theorem,
stochastic-calculus replacement, general stochastic solver, speedup, particle
size inference, or arithmetic-universality result is claimed.
