# Primitive construction histories

**Status:** first operation-generated proposal layer.

## 1. Why proposal generation needs its own IR

The presentation-search layer can compare candidate seed grammars, but it should
not receive candidate expressions stripped of how they were constructed.

For Shakespeare, two constructions may have the same final symbolic value while
remaining distinct process histories.  For example

\[
(x+y)+z
\qquad\text{and}\qquad
x+(y+z)
\]

may simplify to the same commutative polynomial, yet they are not automatically
the same construction presentation.  Associativity, commutativity, or any other
construction quotient must be declared rather than inherited from a symbolic
backend by accident.

## 2. `PrimitiveConstruction`

A primitive proposal now carries a tree certificate:

- atomic leaves are caller-supplied expressions;
- internal nodes are caller-declared `SymbolicOperation`s;
- each operation has arity, semantics, explicit cost, and an optional declared
  commutativity property;
- tree depth, operation count, construction cost, and a human-readable recipe
  are retained.

The final SymPy expression is stored separately in `PrimitiveProposal`.

Thus Shakespeare can compare

\[
(\text{expression},\;\text{construction history},\;\text{construction cost})
\]

instead of using expression equality as the representation ontology.

## 3. Bounded generation

`generate_primitive_proposals` explores construction trees under explicit bounds:

- maximum construction depth;
- maximum polynomial degree;
- maximum number of generated non-atomic candidates.

Rejected constructions retain a reason certificate.  Semantic duplicates are
kept when their construction trees differ.  Only argument permutations for an
operation explicitly declared `commutative=True` are quotiented automatically;
associativity is not inferred.

## 4. Connection to presentation search

`search_primitive_proposals` is the first executable bridge from this operation
layer to the common Shakespeare pipeline.

For every primitive proposal it:

1. uses the proposal expression as a candidate process seed;
2. grows the process-generated grammar;
3. discovers process relations and relation factors;
4. checks exact target reconstruction;
5. includes explicit construction-tree cost in the default structural cost;
6. returns the task-sufficient Pareto frontier.

Semantically equal expressions with different construction trees remain separate
search candidates.

## 5. Current limitation

The first generator is a bounded symbolic tree enumerator, not a learned or
Huffman-like objectification policy.  It also uses polynomial degree as one
backend bound.

The next step is to make proposal generation **adaptive**: repeated/reusable
history subtrees, task signatures, relation compression, and boundary usage
measures should influence which construction trees are proposed first.  That is
where grammar induction and the history-geometry/Huffman line should meet.
