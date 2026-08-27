# Two-generator AM cone calibration

Status: exact calibration of the initial cone theorems.

## 1. The cone

Take

\[
G=\mathbb Z^2,
\qquad
r=(1,0),
\qquad
s=(0,1),
\]

and the pointed cone

\[
C=\mathbb R_{\ge0}r+\mathbb R_{\ge0}s.
\]

Write

\[
X=X^r=a,
\qquad
Y=X^s=e^v.
\]

Then

\[
K[[C\cap G]]=K[[X,Y]].
\]

The native AM operators are

\[
A(X^pY^q)=pX^{p-1}Y^q,
\]

\[
M(X^pY^q)=(p+q)X^pY^q.
\]

Thus `A` is differentiation in the power direction, while the exponential
character direction remains fixed.

## 2. A genuinely two-ray completed expression

Consider

\[
F(X,Y)=\exp(X+Y+XY).
\]

Because the argument has zero constant term and support in the positive cone,
`F` is defined in the completed cone algebra.  Factorization gives

\[
F=\exp(X)\exp(Y)\exp(XY).
\]

Therefore

\[
[X^pY^q]F
=\sum_{k=0}^{\min(p,q)}
\frac1{(p-k)!(q-k)!k!}.
\]

At target bidegree `(2,2)`,

\[
[X^2Y^2]F
=\frac1{2!2!}
+1
+\frac1{2!}
=\boxed{\frac74}.
\]

This coefficient cannot be interpreted as a calculation on one unspecified
rank-one ray: it receives contributions from the two generators and their
mixed degree.

## 3. Exact `A` transport

Differentiating the completed expression gives

\[
AF=(1+Y)F.
\]

The coefficient transported from source degree `(2,2)` to target degree
`(1,2)` is

\[
[X^1Y^2]AF
=2[X^2Y^2]F
=\frac72.
\]

The product side gives independently

\[
[X^1Y^2](1+Y)F
=[X^1Y^2]F+[X^1Y^1]F
=\frac32+2
=\frac72.
\]

This is exact chamber transport by `-r`; it is not an endomorphism preserving
the zero cone sector term by term.

## 4. Exact `M` action

Since `M` measures total AM weight,

\[
MF=(X+Y+2XY)F.
\]

At `(2,2)`, the eigenvalue calculation gives

\[
[X^2Y^2]MF
=4\cdot\frac74
=7.
\]

The product calculation agrees:

\[
[X^2Y^2](X+Y+2XY)F
=\frac32+\frac32+2\cdot2
=7.
\]

## 5. Paired observer heights

Two admissible heights are

\[
h_1(p,q)=p+q,
\qquad
h_2(p,q)=2p+q.
\]

Both define the same formal completion `K[[X,Y]]`.  They assign different
horizons to the same target:

\[
h_1(2,2)=4,
\qquad
h_2(2,2)=6.
\]

Their scalar bounded slices contain respectively

\[
\#\{(p,q)\in\mathbb N^2:p+q\le4\}=15,
\]

\[
\#\{(p,q)\in\mathbb N^2:2p+q\le6\}=16
\]

lattice degrees.  The exact componentwise down-set of `(2,2)` contains only
nine degrees.

Hence three notions must remain distinct:

1. the completed carrier, which is unchanged;
2. the scalar observer height, which defines a cofinal topology;
3. the exact target down-set, which may give a sharper dependency slice.

This is the first exact instance in which observer charts preserve semantics
but alter computational economy.

## 6. Primitive chambers and resonance

On the zero chamber, every monomial has `p>=0`, so the ordinary primitive

\[
P_A(X^pY^q)
=\frac1{p+1}X^{p+1}Y^q
\]

maps `K[[C cap G]]` into the translated chamber `X K[[X,Y]]` and satisfies

\[
A P_A F=F.
\]

After one negative chamber shift, the boundary contains

\[
X^{-1}Y^q.
\]

Its primitive is

\[
\log(X)Y^q,
\]

with the declared positive-real witness `X=a>0`.  The whole boundary
`p=-1`, not a single isolated scalar, is therefore a resonance wall.

## 7. What this calibration establishes

The two-ray example verifies:

- locally finite completed multiplication;
- exact mixed exp coefficients;
- `A` as degree-shifting chamber transport;
- `M` as an endomorphism of each chamber;
- semantic invariance under paired admissible heights;
- a genuine distinction between height windows and exact target down-sets;
- ordinary primitive transport and the codimension-one `log-a` wall.

No stronger support order is needed for any of these operations.
