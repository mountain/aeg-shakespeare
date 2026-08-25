# Polynomial discovery layer: observables, invariants, and algebraic images

**Status:** first bounded discovery front-end; exact and reusable, but intentionally narrow.

## 1. Why this layer exists

Earlier Process Geometry machinery can preserve histories, discover finite
process relations, maintain algebraic constraints, compare presentation costs,
and continue a known algebraic carrier into Abelian geometry. A major manual
gap remained earlier in the pipeline:

```text
primitive process
    -> [human chooses useful observable / invariant]
    -> selected algebraic carrier
```

The first discovery layer removes part of that human bridge. Its current exact pipeline is

```text
process + algebraic constraints + degree budget
    -> constraint-reduced polynomial observable grammar
    -> process action on that grammar
    -> exact nullspace
    -> first-integral candidates
    -> invariant leaf
    -> elimination of source assignments
    -> algebraic observable relations.
```

This is not a claim that polynomial observables are universal. They are the
first bounded proposal language because they admit exact certificates and
interact cleanly with the existing constraint backend.

## 2. Observable grammar

`generate_polynomial_observable_basis` enumerates monomials through a declared total degree. If an `AlgebraicConstraintSet` is supplied, every proposal is reduced in the quotient and exact linear dependencies are removed.

Thus a geometric identity does not merely become another candidate observable.
For example, on a circle the degree-two monomial space is reduced modulo the
circle relation before process discovery begins.

The result records both the raw proposal count and the retained independent expressions. The ordering is a bounded search convention, not a canonical coordinate system.

## 3. First-integral discovery

For a constraint-reduced basis

\[
b_1,\ldots,b_n,
\]

Shakespeare computes

\[
D b_1,\ldots,D b_n
\]

and reduces these derivatives modulo the declared constraints. Writing the reduced derivatives in a common monomial coordinate table gives an exact linear map. Nullspace vectors

\[
(c_1,\ldots,c_n)
\]

produce candidates

\[
I=\sum_i c_i b_i
\]

with

\[
D I=0\pmod{\mathcal I}.
\]

`PolynomialInvariant` retains the discovered expression, its coordinates in the
observable grammar, and the exact derivative remainder. Parameter-only and
constraint-constant directions are treated as trivial and omitted from the
nontrivial invariant list.

The method is deliberately template-free inside the declared polynomial span: the caller supplies the degree budget, not the form of the invariant.

## 4. Observable algebraic-image discovery

Once an invariant leaf or other algebraic task leaf has been declared, `discover_observable_relations` introduces fresh symbols for selected observables and eliminates the original source assignments with a lexicographic Groebner backend.

For observables

\[
F_1,\ldots,F_m
\]

and fresh symbols

\[
U_1,\ldots,U_m,
\]

the elimination ideal contains the original constraints together with

\[
U_i-F_i=0.
\]

Every returned relation is pulled back to the source assignments and reduced again in the original constraint quotient. The result therefore carries an independent exact remainder certificate rather than exposing only an elimination polynomial.

`discover_first_order_observable_image` is the first process-specific bridge.
Given one proposed observable `U=F`, it automatically adds

\[
Y=DF
\]

and searches for relations among `(U,Y)` on the supplied leaf.

## 5. Pendulum discovery I

The executable vignette `tests/classical/test_pendulum_discovery_layer.py` starts before the mechanical energy is known.

Constraint preservation first closes the unresolved radial multiplier. Process
Geometry then searches the degree-two polynomial observable grammar modulo rod
and tangency constraints and discovers the unique nontrivial first-integral
direction

\[
I=v_x^2+v_y^2+2q_y.
\]

Only afterwards is a symbol `K` introduced for the discovered invariant value.
On the leaf `I=K`, the still caller-selected observable

\[
U=q_y,
\qquad
Y=DU=v_y
\]

produces by exact elimination

\[
\boxed{Y^2=(K-2U)(1-U^2).}
\]

The conventional energy notation `K=2E` and the classification of the cubic as genus one occur only as classical shadows.

This changes the previous calibration boundary:

```text
before:
    supplied energy -> supplied reduced observables -> verify cubic

after:
    primitive constrained process -> discover invariant
    -> invariant leaf -> selected observable -> discover cubic.
```

## 6. What remains manual

The main unresolved choice has moved earlier but has not disappeared. In the
pendulum vignette the caller still selects `q_y` as the observable whose first
process derivative should be eliminated.

The next discovery threshold is therefore:

```text
observable candidates
    -> algebraic-image candidates
    -> structural / task cost
    -> Pareto-ranked observable choice.
```

For the pendulum, a useful next test is to compare low-cost position observables
without naming the vertical coordinate in advance and ask whether the
gravity-aligned observable wins because it produces a lower-complexity
algebraic image.

After that, the same presentation-search interface should compare
function-language candidates: raw constrained coordinates, polynomial
algebraic images, A/M modules, and genus-one/Abelian language.

## 7. Claim boundary

The current layer does not provide:

- a complete invariant-generation algorithm;
- non-polynomial observable discovery;
- automatic choice of invariant leaves;
- automatic ranking of observable algebraic images;
- a general algebraic-geometry classifier;
- automatic function-theory selection.

Its narrower contribution is an executable exact bridge from bounded polynomial
observable search to invariant and algebraic-image discovery. It does not by
itself establish a task-semantic quotient or a decoder.
