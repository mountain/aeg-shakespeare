# Polynomial discovery layer: observers, invariants, and algebraic quotients

**Status:** first bounded discovery front-end; exact and reusable, but intentionally narrow.

## 1. Why this layer exists

Earlier Shakespeare machinery can preserve histories, discover finite process relations, maintain algebraic constraints, compare presentation costs, and continue a known algebraic quotient into Abelian geometry. A major manual gap remained earlier in the pipeline:

```text
primitive process
    -> [human chooses useful observable / invariant]
    -> quotient geometry
```

The first discovery layer removes part of that human bridge. Its current exact pipeline is

```text
process + algebraic constraints + degree budget
    -> quotient-reduced polynomial observer grammar
    -> process action on that grammar
    -> exact nullspace
    -> first-integral candidates
    -> invariant leaf
    -> elimination of source assignments
    -> algebraic observable relations.
```

This is not a claim that polynomial observers are universal. They are the first bounded proposal language because they admit exact certificates and interact cleanly with the existing constraint backend.

## 2. Observer grammar

`generate_polynomial_observer_basis` enumerates monomials through a declared total degree. If an `AlgebraicConstraintSet` is supplied, every proposal is reduced in the quotient and exact linear dependencies are removed.

Thus a geometric identity does not merely become another candidate observer. For example, on a circle the degree-two monomial space is reduced modulo the circle relation before process discovery begins.

The result records both the raw proposal count and the retained independent expressions. The ordering is a bounded search convention, not a canonical coordinate system.

## 3. First-integral discovery

For a quotient-reduced basis

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

`PolynomialInvariant` retains the discovered expression, its coordinates in the observer grammar, and the exact derivative remainder. Parameter-only and quotient-constant directions are treated as trivial and omitted from the nontrivial invariant list.

The method is deliberately template-free inside the declared polynomial span: the caller supplies the degree budget, not the form of the invariant.

## 4. Observable quotient discovery

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

`discover_first_order_process_quotient` is the first process-specific bridge. Given one proposed observer `U=F`, it automatically adds

\[
Y=DF
\]

and searches for relations among `(U,Y)` on the supplied leaf.

## 5. Pendulum discovery I

The executable vignette `tests/classical/test_pendulum_discovery_layer.py` starts before the mechanical energy is known.

Constraint preservation first closes the unresolved radial multiplier. Shakespeare then searches the degree-two polynomial observer grammar modulo rod and tangency constraints and discovers the unique nontrivial first-integral direction

\[
I=v_x^2+v_y^2+2q_y.
\]

Only afterwards is a symbol `K` introduced for the discovered invariant value. On the leaf `I=K`, the still caller-selected observer

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
    -> invariant leaf -> selected observer -> discover cubic.
```

## 6. What remains manual

The main unresolved choice has moved earlier but has not disappeared. In the pendulum vignette the caller still selects `q_y` as the observer whose first process jet should be eliminated.

The next discovery threshold is therefore:

```text
observer candidates
    -> quotient candidates
    -> structural / task cost
    -> Pareto-ranked observer choice.
```

For the pendulum, a useful next test is to compare low-cost position observables without naming the vertical coordinate in advance and ask whether the gravity-aligned observer wins because it produces a lower-complexity closed quotient.

After that, the same presentation-search interface should compare function-language candidates: raw constrained coordinates, polynomial quotient, A/M modules, and genus-one/Abelian language.

## 7. Claim boundary

The current layer does not provide:

- a complete invariant-generation algorithm;
- non-polynomial observer discovery;
- automatic choice of invariant leaves;
- automatic ranking of observable quotients;
- a general algebraic-geometry classifier;
- automatic function-theory selection.

Its narrower contribution is an executable exact bridge from bounded polynomial observer search to invariant and quotient discovery. This is the first missing front-end segment needed to connect raw process data to the existing Shakespeare representation machinery.
