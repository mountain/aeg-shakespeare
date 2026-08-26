# Phase 1B contract — blind collision-covector discovery

Status: frozen before implementation and evaluation.

Phase 1A was a supplied-baseline H theorem. Phase 1B removes the entropy formula from the discovery inputs and asks what covector law is forced by reversible binary-collision tasks.

The intended result may be positive, negative, or mixed. In particular, discovering a multiplicative-character class does not by itself establish a unique real logarithmic scale.

## 1. Problem-native task

Let \(\psi:\mathbb R_{>0}\to\mathbb R\) be an unknown species-blind covector. For a reversible channel with incoming activities \(a,b\) and outgoing activities \(c,d\), the separable functional derivative has the form

\[
\dot F
=
\kappa(ab-cd)
\bigl[\psi(c)+\psi(d)-\psi(a)-\psi(b)\bigr].
\]

The discovery task is not given \(F\), \(f\log f\), a logarithm, or an equilibrium distribution. It receives only:

- positive multiplicative activities;
- pair formation by Multiplication;
- reversible pair replacement;
- Addition of the two one-site covector values;
- the requirement that the local rate never have the wrong sign;
- continuity as the regularity class for the later continuum interpretation.

Equivalently, the required sign law is

\[
(ab-cd)
\bigl[
\psi(a)+\psi(b)-\psi(c)-\psi(d)
\bigr]
\ge 0.
\]

## 2. Fibre lemma before finite search

The continuum theorem obligation is separated from the finite search.

If \(ab=cd=P\), compare \((a,b)\) with \((ce^\varepsilon,d)\). For \(\varepsilon>0\) and \(\varepsilon<0\), the sign law gives opposite one-sided inequalities. Continuity at \(\varepsilon=0\) therefore forces

\[
\psi(a)+\psi(b)=\psi(c)+\psi(d)
\qquad\text{whenever}\qquad
ab=cd.
\]

Setting \((c,d)=(ab,1)\) yields

\[
\psi(ab)-\psi(1)
=
\bigl[\psi(a)-\psi(1)\bigr]
+
\bigl[\psi(b)-\psi(1)\bigr].
\]

Thus the centered covector

\[
\chi(x)=\psi(x)-\psi(1)
\]

must be a Multiplication-to-Addition character.

The executable discovery is allowed to use pair-product fibre equality only because this lemma is stated and audited first. It is not allowed to use the classical classification of continuous characters until post-hoc evaluation.

## 3. Frozen finite worlds

For distinct primes \(p_1,\ldots,p_d\) and a bound \(N\), define the exact multiplicative world

\[
E(p_1,\ldots,p_d;N)
=
\left\{
\prod_{j=1}^d p_j^{n_j}
:
-N\le n_j\le N
\right\}.
\]

Each element is represented by its literal Multiplication history and its integer exponent normal form. Equality and order of the resulting positive rational numbers are computed exactly.

### Training worlds

- \(T_1=E(2;2)\);
- \(T_2=E(2,3;2)\).

### Held-out worlds

- \(H_1=E(2,3;3)\), used for strict-order transfer;
- \(H_2=E(2,3;4)\), used for H-sign transfer;
- \(H_3=E(2,3,5;1)\), used for structural dimension transfer.

No held-out world may participate in grammar generation, coefficient selection, or tie-breaking.

## 4. Frozen candidate grammars

Two grammars are compared.

### G0 — unrestricted finite observer table

Assign one unknown scalar \(\psi_x\) to every \(x\in E\). For every two unordered pairs with the same product, impose

\[
\psi_a+\psi_b=\psi_c+\psi_d.
\]

Exact rational linear algebra computes the complete survivor space. This is the coverage control: a native grammar is not credited if it misses unrestricted finite survivors.

### G1 — bounded A/M exponent grammar

The literal Multiplication history supplies exponent coordinates \(n_1,\ldots,n_d\). Candidate covectors are exact linear combinations of every monomial of total degree at most two:

\[
1,\quad n_i,\quad n_i n_j.
\]

The search is not told which coefficients should vanish. Pair-product fibre equations are applied to the complete grammar and the exact coefficient nullspace is returned.

Forbidden candidate constructors:

- logarithm or exponential;
- \(f\log f\) or any named entropy;
- Maxwellian parameters;
- numerical targets derived from the classical answer;
- Fourier or spectral coordinates;
- arbitrary neural or floating-point function fitting;
- held-out counterexamples.

## 5. Frozen order selector

If the \(T_2\) survivor space contains a constant gauge and two prime-history directions, quotient the constant and normalize the positively oriented \(2\)-direction to weight one.

For a remaining rational \(3\)-direction weight \(r=m/n>0\):

1. enumerate reduced fractions with \(1\le m,n\le8\);
2. retain candidates strictly preserving the exact order of every distinct pair in \(T_2\);
3. rank by
   \[
   (m+n,\max(m,n),m,n);
   \]
4. freeze the unique minimum before applying \(H_1\) or \(H_2\).

This selector is deliberately finite and simplicity-biased. Failure on held-out worlds is an admissible and informative result.

## 6. Oracle firewall

Discovery inputs contain no call to a logarithm.

Only after the survivor space, selected rational weight, and held-out outcomes are frozen may the evaluator use the classical facts that:

- continuous characters of \((\mathbb R_{>0},\times)\) into \((\mathbb R,+)\) are scalar multiples of \(\log x\);
- the corresponding two-prime weight ratio is
  \[
  \frac{\log3}{\log2};
  \]
- integrating a positive logarithmic covector gives relative entropy modulo affine gauge.

The implementation must keep discovery functions and the post-hoc oracle comparison visibly separate. Source inspection must confirm that discovery functions do not call the oracle.

## 7. Conserved-affine gauge

Three distinct freedoms must be reported separately:

1. \(\psi\mapsto\psi+\text{constant}\), invisible to every \(2\leftrightarrow2\) channel;
2. multiplication of \(\psi\) by a positive scalar, which preserves sign but changes units;
3. addition of a species-dependent collision invariant in the left kernel of the frozen six-velocity stoichiometric matrix.

The executable record must compute the exact left kernel for the Phase 1A network and compare it with the declared mass and momentum labels. Equality modulo gauge is not literal formula equality.

## 8. Metrics and certificates

Record:

- literal point and unordered-pair counts in every world;
- pair-product fibre count and equation-matrix rank;
- unrestricted survivor dimension;
- G1 monomial count and survivor dimension;
- whether G1 spans all unrestricted survivors on training worlds;
- the selected rational order weight and its exact training margin;
- strict-order transfer to \(H_1\);
- local H-sign transfer to \(H_2\);
- structural dimension transfer to \(H_3\);
- exact nested order bounds for \(E(2,3;N)\), \(1\le N\le6\);
- the Phase 1A conserved-affine gauge dimension;
- targeted runtime.

Coverage and uniqueness are separate metrics.

## 9. Frozen red teams

### RT1 — collision algebra without order

Remove the positive-rational order constraints. Independent prime-history weights must remain visible. The experiment must not claim a unique logarithmic scale.

### RT2 — finite simplicity overfit

Apply the frozen simplest rational \(T_2\) selector to \(H_1\) and \(H_2\). Any equality defect, order reversal, or positive H rate is recorded rather than repaired.

### RT3 — larger multiplicative alphabet

Transfer the structural grammar to \(H_3\). A new prime generator may add a character direction. That is not counted as failure of the character law, but it is failure of a fixed two-weight coordinate to be universal.

### RT4 — negative orientation

Negating a valid character must reverse the H sign on a nonstationary channel.

### RT5 — gauge masquerading as discovery

Adding constants or collision invariants must leave every channel affinity unchanged. Such candidates are one quotient class, not separate discoveries.

### RT6 — regularity removal

The continuum classification may use continuity or monotonicity. It may not claim that the bare algebraic Cauchy equation alone selects the ordinary logarithm on all positive reals.

## 10. Cost and placement

- one research-local test module;
- standard-library exact fractions plus existing SymPy;
- no public API changes;
- no stochastic search;
- target under 10 seconds;
- all candidate counts and ranks deterministic;
- full default CI must remain green.

## 11. Phase gate

Three labels are possible.

### Character-class discovery

Earned if the finite task oracle selects exactly the multiplicative-character survivor class, the native grammar covers the unrestricted finite survivor space, and the class transfers structurally to held-out worlds.

### Logarithmic-scale discovery

Earned only if a scale selector chosen without oracle access transfers to held-out order and H-sign tasks and the continuum regularity theorem identifies the same ray up to positive scale.

### Partial or negative uniqueness result

Required if the character class transfers but the finite selector does not. In that case the phase must state which extra structure—larger order worlds, continuity, Archimedean comparison, or another task—is needed.

No result in this phase derives the kinetic equation from microscopic mechanics or raises arithmetic rank.
