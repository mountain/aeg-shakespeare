# Phase 1J-B3 results — bounded marking survives the global formal sum

**Verdict:** Phase 1J-B3 passes for the formal pre-cut signed molecule family.
The bounded event observable can be removed before the Deng--Hani--Ma
operation sequence, leaving only a linear molecule-size factor. That factor
is absorbed into the proof's existing geometric molecule-size sum. The
resulting formal marked family is absolutely convergent in total variation.

It does **not** follow that this formal measure is the microscopic hard-sphere
collision current or the response measure required by Phase 1J-B.

**Contract:**
[25-phase1j-b3-marked-operation-sequence-contract.md](./25-phase1j-b3-marked-operation-sequence-contract.md).

**Executable:**
[test_marked_operation_sequence_summation.py](../../tests/research/test_marked_operation_sequence_summation.py).

## 1. The main deduction

For each molecule \(M\), root-visible C-atom \(n\), and bounded event test
\(\psi\),

\[
\left|\langle\kappa_{M,n},\psi\rangle\right|
\le \lVert\psi\rVert_\infty\,\lVert\lvert IN_M\rvert\rVert_{L^1}.
\]

Summing eligible atoms gives the sole additional cost

\[
\lvert\mathcal C_H(M)\rvert\le \lvert M\rvert=m.
\]

The paper's global proof already sums a product of the schematic form

\[
C^m\lvert\log\epsilon\rvert^{C_*\rho}
\times C^m\lvert\log\epsilon\rvert^{C_*\rho}
\times \tau^{m/9}\epsilon^{a+b\rho}.
\]

The first two factors represent molecule choices and operation sub-cases; the
last represents the final integral bound. Inserting the mark multiplies this
by \(m\), but

\[
mC^m\le(2C)^m.
\]

Thus the mark changes a generic exponential constant and consumes no
positive \(\epsilon\)-power. Under the source paper's parameter hierarchy,

\[
\sum_M \lvert\mathcal C_H(M)\rvert
       \lVert\lvert IN_M\rvert\rVert_{L^1}
\le C\epsilon^{a+b\lvert H\rvert}
\]

for some \(a,b>0\) after the usual generic-constant enlargement and, if
needed, a harmless weakening of slack. This gives an enumeration-independent
formal signed measure and full bounded-dual control.

## 2. Why no marked elementary estimates were needed

The original B3 plan proposed carrying a test observable through every good,
normal and bad elementary component. For bounded tests this is unnecessary.
The correct order is:

1. define the collision event on the physical pre-cut molecule;
2. pair it with \(\psi\);
3. take absolute value and use \(\lvert\psi\rvert\le K\);
4. remove the mark; and only then
5. run deletion, cutting, splitting and final summation on the positive
   unmarked integral.

This ordering matters. It avoids trying to reconstruct physical collision
data after molecule cutting has destroyed that interpretation. It also
explains exactly why the method stops at bounded tests: an unbounded
logarithmic affinity cannot be erased by one uniform \(K\).

## 3. Source-level audit

The inference uses the source paper as follows:

- Definitions 3.22--3.23 supply signed \(IN_M\) and positive
  \(\lvert IN_M\rvert\).
- Proposition 3.25 supplies domination by positive molecule sums, but only
  domination—not a marked current identity.
- Proposition 7.2 contributes
  \(C^m\lvert\log\epsilon\rvert^{C_*\rho}\) molecule choices.
- Proposition 7.5 converts \(\lVert IN_M\rVert_{L^1}\) to \(I_M(Q_M)\).
- Definition 8.10 and Proposition 8.18 control deletion/cutting/splitting
  sub-cases.
- Proposition 9.7 and equations (9.51)--(9.53) supply sub-case count and the
  positive gain that closes the global sum.

The formal signed molecule sum is therefore a corollary of the proof
architecture, not a theorem stated in the paper. The hard-sphere current
identity remains a new obligation.

## 4. Exact certificate ledger

The rational summation fixture separates molecule choices, operation
sub-cases and local gains. After multiplication its effective ratios are

\[
q_m=\frac14,
\qquad
q_\rho=\frac1{16}.
\]

The exact infinite totals are

\[
\mathcal S_{\mathrm{unmarked}}=\frac1{1440},
\qquad
\mathcal S_{\mathrm{marked}}=\frac1{1080}.
\]

Their ratio is \(4/3\): linear marking changes only a constant. The maximal
marked tail after molecule size eight is

\[
\sum_{m>8,\,\rho\ge1}
m q_m^m q_\rho^\rho\times\frac1{32}
=\frac7{70778880}<10^{-6}.
\]

The targeted run is:

    13 passed in 0.05s

The operation fixture also checks that deleting O-atoms preserves C-marks,
cuts route each mark exactly once, and support partitions do not duplicate
mass.

## 5. Red-team results

Two failures are now explicit.

First, if the effective molecule-size ratio reaches one, the marked partial
sums grow as triangular numbers. No atom-count argument repairs a missing
geometric gain.

Second, if the number of eligible marks grows exponentially, for example
\(2^m\) against an unmarked ratio \(2^{-m}\), every size contributes one and
the series diverges. The B3 conclusion therefore depends essentially on the
structural bound \(\lvert\mathcal C_H(M)\rvert\le m\), not merely on finiteness
of each molecule.

The large-component error family remains conditional on its separate source
hierarchy: equation (9.82) has an extra
\(\epsilon^{-C_*\lvert H\rvert}\) loss, which the paper absorbs using
\(m\ge\Lambda_\ell\) and a \(\tau^{m/2}\) reserve. The linear mark factor does
not change that mechanism, but B3 does not merge this error type with the
cumulant family.

## 6. What has and has not advanced

B3 has earned:

- a formal signed pre-cut molecule current;
- absolute total-variation summability of its bounded marked family;
- full bounded \(L^\infty\)-dual control at that formal level;
- a proof that linear mark count consumes no positive-power margin;
- exact routing semantics for deletion, cutting and splitting; and
- explicit geometric and exponential-mark kill conditions.

B3 has not earned:

- equality between the formal sum and a current determined by \(E_H\);
- identification with the actual microscopic collision-boundary flux;
- the stopped/actual/target response decomposition of Phase 1J-B;
- a marked interpretation of \(\mathrm{Err}_2\) or final
  \(f_s^{\mathrm{err}}\);
- an unbounded logarithmic pairing, entropy chain rule or H theorem; or
- a Core theorem, Theory Map object, rank claim or generic API.

## 7. Next theorem-sized gate

Phase 1J-B4 should be **physical signed-current identification**. It must
return to the pre-absolute-value expansion and prove that the marked signed
molecule terms reconstruct a declared microscopic collision current, with:

1. collision orientation and gain/loss signs;
2. actual, truncated and target current types;
3. trace/history identification on one declared event space;
4. separately measured truncation, geometry and terminal-error currents; and
5. equality of bounded weak pairings, not merely domination by a positive
   measure.

Only after B4 should the logarithmic tail be reopened. The main remaining
obstruction has shifted from summability to semantic/analytic identification.

## 8. Repository effect

### Mathematical Core

Unchanged. The new result is a research-level corollary of an external proof
architecture plus classical absolute convergence.

### Engineering Architecture

Refined research-locally. A continuum evaluator should mark before cutting,
erase bounded tests before estimation, and keep formal summability separate
from current identification.

### Theory Map

Unchanged. The result strengthens U4/E adaptation evidence but supplies no
new objectified process or calculus.

### API

No pressure. All executable classes remain problem-local certificates.
