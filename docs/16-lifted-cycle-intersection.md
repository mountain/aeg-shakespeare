# Lifted-cycle intersection: when two crossings are only one crossing

The period-matrix layer exposed a precise missing datum: the A/B periods only become a Riemann period presentation after the cycles themselves carry the canonical symplectic intersection form.

This note records the first executable approximation to that topological structure.

## 1. The base drawing is insufficient

For a hyperelliptic double cover

\[
y^2=P(x),
\]

a point of the Riemann surface is not just \(x\). Away from the branch locus it is \((x,+\sqrt{P(x)})\) or \((x,-\sqrt{P(x)})\).

Consequently two projected paths may cross at exactly the same \(x\)-value while their lifted paths occupy opposite sheets. Such a crossing is not an intersection of the curves on the Riemann surface.

This gives a particularly clean instance of a general Shakespeare principle:

\[
\boxed{\text{visible state geometry does not determine lifted-history geometry}.}
\]

The classical statement is simply the topology of a branched covering. The history wording is the project interpretation.

## 2. Sampled algebraic intersection

`lifted_path_intersections(left, right)` takes two already-continued `LiftedSquareRootPath` objects.

For each transverse polygonal crossing of their base projections it records:

- the base point;
- the two segment indices;
- the orientation sign \(+1\) or \(-1\);
- whether the interpolated lifted `y` values are on the same sheet, opposite sheets, or numerically unresolved.

Only same-sheet crossings contribute to

\[
I(\alpha,\beta)=\sum_p \operatorname{sign}_p(\alpha,\beta).
\]

An unresolved sheet comparison raises rather than being silently discarded.

The current routine is numerical. It assumes transverse well-resolved polygonal paths away from branch points and does not yet certify invariance under homotopy.

## 3. From pairings to a sampled symplectic form

For an `AbelianCycleSystem` ordered as

\[
(a_1,\ldots,a_g,b_1,\ldots,b_g),
\]

`sampled_intersection_form` measures all pairwise signed intersections and compares the resulting integer matrix with

\[
J=\begin{pmatrix}0&I_g\\-I_g&0\end{pmatrix}.
\]

The returned `SampledIntersectionForm` records skew symmetry, determinant/unimodularity, and the residual from this canonical matrix.

This is the first point where the period pipeline contains both:

\[
\text{analytic data: } A,B,\tau
\]

and

\[
\text{sampled topological data: } J.
\]

`SampledRiemannProfile` only passes when the sampled pairing is canonical and the measured normalized period matrix is symmetric with positive-definite imaginary part.

It remains a sampled profile, not a theorem prover for the Riemann bilinear relations.

## 4. Pendulum V

For the symmetric pendulum quotient

\[
Y^2=2U(U^2-1),
\]

we reuse the two counterclockwise ellipses around the branch pairs

\[
\{-1,0\},\qquad \{0,1\}.
\]

Their projections cross twice.

The lifted histories reveal something the plane picture cannot:

- at the upper crossing the two continued `Y` values agree, so the paths really intersect on the surface;
- at the lower crossing the continued `Y` values differ by sign, so the projected crossing lies on opposite sheets.

Thus

\[
\boxed{2\text{ projected crossings}\quad\longrightarrow\quad1\text{ surface intersection}.}
\]

The surviving crossing has positive orientation, giving

\[
a\cdot b=+1
\]

and hence

\[
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Together with the directly measured periods this gives

\[
\tau\approx i,
\qquad
\operatorname{Im}\tau>0.
\]

If the B-cycle is reversed, the same machinery gives

\[
a\cdot(-b)=-1,
\qquad
\tau\approx-i,
\]

and the positive-imaginary-part condition fails. Orientation of history is therefore simultaneously visible in the topological pairing and in the analytic period normalization.

The complete cited executable essay is `tests/classical/test_pendulum_cycle_intersection.py`.

## 5. What this unlocks—and what it does not

The implemented chain is now

\[
\boxed{
\text{process}
\to
\text{quotient curve}
\to
\text{differentials}
\to
\text{lifted histories}
\to
\text{periods}
\to
\text{sampled intersection form}
\to
\text{Riemann-shape consistency}.
}
\]

The next mathematical obstruction is sharper than before. We need to replace hand-chosen cycles and sampled intersection counts with a reusable cycle-construction layer whose homology and intersection properties are controlled by construction.

For hyperelliptic families with known branch points, the next candidate abstraction is therefore a branch-cut/cycle presentation that can generate a canonical symplectic basis and connect it to the numerical lifts. Only after that step should Shakespeare promote the current sampled Riemann profile to a stronger certificate or introduce a Jacobian representation.

## References

See `docs/REFERENCES.md`, especially:

- [Forster-1981], for covering surfaces and compact Riemann surfaces;
- [Farkas-Kra-1992], for canonical homology bases, Abelian differentials, and period matrices;
- [Mumford-1983], for the period-matrix/Jacobian setting.
