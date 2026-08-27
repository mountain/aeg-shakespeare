# Problem frontier: AMP closure, ensembles, and carrier necessity

Status: frozen research contract for issue
[#150](https://github.com/mountain/process-geometry/issues/150).

## 1. Question

On the positive real line, or on a complex history lift with a chosen branch
of `Log`, consider

\[
A_t(x)=x+t,
\qquad
M_s(x)=e^s x,
\qquad
P_r(x)=\exp(e^r\Log x).
\]

The motivating hypothesis is that Addition describes local accumulation,
Multiplication describes rescaling or independent assembly, and Power
objectifies repeated same-kind assembly.  The hypothesis earns mathematical
credit only if it changes closure, representation, or a frozen computation.

The first gate asks:

> What is the smallest task-sufficient carrier for finite and iterated A/M/P
> histories, and can a Power-aware presentation compile an ensemble task
> without materializing its full Cartesian state space?

`AMP` is research-local terminology here.  It is not asserted to be the name
of an established mathematical field or one three-dimensional Lie group.

## 2. Frozen task family

The positive control uses a finite weighted state space `Omega` with partition
value

\[
Z_0=\sum_{\omega\in\Omega}w(\omega)>0.
\]

A homogeneous assembly stage is

\[
Z_{k+1}=e^{b_k}Z_k^{n_k},
\qquad n_k\in\mathbb N_{>0}.
\]

Its declared observer asks only for total partition value, logarithmic
partition value, and the number of base replicas.  It does not ask for named
microstates, correlations, marginals, or an interacting Hamiltonian.

The negative control inserts Addition in the state chart.  In the logarithmic
observer `y=log x`, this produces

\[
y\longmapsto \log(e^{\alpha y+\beta}+t),
\]

which must either remain in the finite M/P carrier or exhibit an exact carrier
upgrade witness.

## 3. Evidence firewall

Separate all of the following:

- a finite M/P word from the full A/M/P closure;
- integer replica count from arbitrary real or complex powering;
- fixed iteration height from symbolic or ordinal height;
- exact total-partition observation from reconstruction of the ensemble;
- a finite observer truncation from the full completed series;
- membership in a large ambient field from an effective implementation;
- compilation cost, certificate storage, replay cost, and output size.

Matrices and polynomials may verify local identities.  They receive no credit
as the ontology of the process rank.

## 4. Acceptance and kill conditions

The phase passes only if it supplies:

1. exact adjacent conjugation and Lie-bracket laws;
2. a proof that the three infinitesimal generators do or do not close;
3. an explicit infinite closure witness if they do not;
4. an exact M/P normal form and replayable ensemble certificate;
5. a negative control that leaves the finite normal form;
6. a minimum-carrier disposition including a surreal necessity verdict.

Narrow or stop if the apparent advantage is only:

- relabelling repeated multiplication as Power without a reusable operation;
- hiding full state enumeration in an oracle;
- using noninteger powers as literal replica counts;
- reporting `No` containment as an algorithm;
- choosing Conway simplicity solely to force a surreal answer;
- discarding interaction or correlation data that the observer actually asks
  to recover.

## 5. Claim ceiling

This Sonnet does not claim a complexity-class separation, a solution of the
three-dimensional Ising model, an exact renormalization theorem, a canonical
thermodynamic surreal limit, or a general surreal runtime.

```text
Epistemic maturity: T1 exact finite results + T0 continuation
Engineering status: Sonnet-local Python certificate
Mathematical Core: unchanged
Experimental/Public API: none
```
