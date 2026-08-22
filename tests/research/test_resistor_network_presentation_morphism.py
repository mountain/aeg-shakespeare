"""Resistor networks: boundary semantics as a presentation quotient.

Question
--------
Does the presentation-morphism pattern found in KdV survive in a domain with no
soliton, PDE, spectral-curve, or integrability vocabulary?

Primitive data
--------------
A finite resistor presentation is represented only by undirected edges carrying
conductances.  Boundary nodes are distinguished from internal nodes.  The task
semantics is the Dirichlet-to-Neumann response matrix

    I_boundary = Lambda * V_boundary.

For a Kirchhoff matrix split into boundary/interior blocks, the response is the
Schur complement

    Lambda = L_BB - L_BI * L_II^{-1} * L_IB.

All computations below are exact SymPy rational/symbolic algebra.  No electrical
network object is added to the public Shakespeare API.

Classical lineage
-----------------
Y-Delta transformations and boundary response matrices are classical electrical
network constructions.  Curtis, Ingerman, and Morrow show, for circular planar
resistor networks, that critical networks are related by Y-Delta moves according
to their connection data and that the conductances of a critical network are
recoverable from its response matrix.  See [Curtis-Ingerman-Morrow-1998] in
``docs/REFERENCES.md``.

Shakespeare reconstruction
---------------------------
The first test does *not* insert the Y->Delta conductance formulas.  It builds a
symbolic three-leg star and a triangle with unknown edge conductances, computes
the two boundary response matrices, and solves

    Lambda_star = Lambda_triangle.

The unique solution recovers the classical conductance transformation.  Thus the
local presentation morphism is discovered from task-semantic equality.

The second test uses two adjacent internal nodes.  Eliminating U first and V
first gives genuinely different intermediate graphs.  Nevertheless both
intermediate presentations have the same boundary response as the original.
Completing the two elimination histories yields the same boundary-only graph.
This is task-semantic confluence of overlapping Schur-complement histories.

Red team
--------
The third test demonstrates why a morphism certificate must state the *full task
quotient*.  A fake triangle is chosen so that two natural scalar Dirichlet-energy
probes agree exactly with the true Y->Delta network.  A third probe and the full
response matrix disagree.  Partial observer agreement is therefore weaker than
presentation equivalence.

Calibration statement
---------------------
Passing this file certifies that:

1. exact boundary semantics uniquely forces the symbolic Y->Delta conductances;
2. two different internal-elimination histories preserve the same DtN quotient;
3. their intermediate graphs may differ even while task semantics agree;
4. complete elimination is order-independent in the calibrated example; and
5. two exact scalar power probes do not determine the full boundary response.

Claim boundary
--------------
This does not implement arbitrary circular-planar recovery, critical-graph
recognition, positivity/circular-minor theory, or a general graph-rewrite engine.
It also does not yet promote ``PresentationMorphism``.  Its role is narrower:
provide a non-KdV source of the same pressure toward

    source presentation -> certified local transformation -> target presentation

with preservation tested in a declared task quotient rather than by syntax.
"""

from __future__ import annotations

from itertools import combinations

import sympy as sp

Edge = tuple[str, str]
Graph = dict[Edge, sp.Expr]


def edge_key(left: str, right: str) -> Edge:
    if left == right:
        raise ValueError("self-loops are not part of the resistor presentation")
    return tuple(sorted((left, right)))


def add_conductance(
    graph: Graph,
    left: str,
    right: str,
    conductance: sp.Expr,
) -> Graph:
    out = dict(graph)
    key = edge_key(left, right)
    out[key] = sp.cancel(out.get(key, sp.S.Zero) + sp.sympify(conductance))
    if sp.simplify(out[key]) == 0:
        del out[key]
    return out


def graph_from_edges(edges) -> Graph:
    graph: Graph = {}
    for left, right, conductance in edges:
        graph = add_conductance(graph, left, right, conductance)
    return graph


def graph_nodes(graph: Graph) -> tuple[str, ...]:
    nodes: set[str] = set()
    for left, right in graph:
        nodes.add(left)
        nodes.add(right)
    return tuple(sorted(nodes))


def kirchhoff_matrix(graph: Graph, nodes: tuple[str, ...]) -> sp.Matrix:
    positions = {node: index for index, node in enumerate(nodes)}
    matrix = sp.zeros(len(nodes))
    for (left, right), conductance in graph.items():
        i = positions[left]
        j = positions[right]
        matrix[i, i] += conductance
        matrix[j, j] += conductance
        matrix[i, j] -= conductance
        matrix[j, i] -= conductance
    return matrix.applyfunc(sp.cancel)


def response_matrix(graph: Graph, boundary: tuple[str, ...]) -> sp.Matrix:
    """Exact Dirichlet-to-Neumann matrix after eliminating all interior nodes."""

    boundary = tuple(boundary)
    all_nodes = set(graph_nodes(graph))
    if not set(boundary) <= all_nodes:
        raise ValueError("every boundary node must occur in the graph")
    interior = tuple(sorted(all_nodes - set(boundary)))
    nodes = boundary + interior
    matrix = kirchhoff_matrix(graph, nodes)
    size = len(boundary)
    boundary_block = matrix[:size, :size]
    if not interior:
        return boundary_block.applyfunc(sp.cancel)
    boundary_interior = matrix[:size, size:]
    interior_boundary = matrix[size:, :size]
    interior_block = matrix[size:, size:]
    response = (
        boundary_block
        - boundary_interior * interior_block.inv() * interior_boundary
    )
    return response.applyfunc(sp.cancel)


def eliminate_internal_node(graph: Graph, node: str) -> Graph:
    """One local Schur-complement/star-mesh elimination.

    Degree three is the conductance-form Y->Delta move.  Higher degree is the
    corresponding star-mesh/Kron step.  Keeping this helper test-local avoids
    turning one calibration into a public graph API.
    """

    incident: list[tuple[str, sp.Expr]] = []
    retained: Graph = {}
    for (left, right), conductance in graph.items():
        if left == node:
            incident.append((right, conductance))
        elif right == node:
            incident.append((left, conductance))
        else:
            retained[(left, right)] = conductance
    if len(incident) < 2:
        raise ValueError("internal elimination requires degree at least two")
    total = sp.cancel(sum(conductance for _, conductance in incident))
    if sp.simplify(total) == 0:
        raise ValueError("total incident conductance must be nonzero")

    out = retained
    for (left, left_c), (right, right_c) in combinations(incident, 2):
        out = add_conductance(
            out,
            left,
            right,
            sp.cancel(left_c * right_c / total),
        )
    return {edge: sp.cancel(value) for edge, value in out.items()}


def triangle_graph(a_b: sp.Expr, b_c: sp.Expr, c_a: sp.Expr) -> Graph:
    return graph_from_edges(
        (
            ("A", "B", a_b),
            ("B", "C", b_c),
            ("C", "A", c_a),
        )
    )


def quadratic_power(response: sp.Matrix, voltage: sp.Matrix) -> sp.Expr:
    return sp.expand((voltage.T * response * voltage)[0])


def test_symbolic_y_delta_is_discovered_from_boundary_response():
    a, b, c = sp.symbols("a b c", nonzero=True)
    star = graph_from_edges(
        (
            ("A", "X", a),
            ("B", "X", b),
            ("C", "X", c),
        )
    )
    star_response = response_matrix(star, ("A", "B", "C"))

    x_ab, x_bc, x_ca = sp.symbols("x_ab x_bc x_ca")
    triangle = triangle_graph(x_ab, x_bc, x_ca)
    triangle_response = response_matrix(triangle, ("A", "B", "C"))

    equations = [
        sp.together(entry)
        for entry in list(triangle_response - star_response)
    ]
    solutions = sp.solve(equations, (x_ab, x_bc, x_ca), dict=True)
    assert len(solutions) == 1
    discovered = solutions[0]

    denominator = a + b + c
    assert sp.simplify(discovered[x_ab] - a * b / denominator) == 0
    assert sp.simplify(discovered[x_bc] - b * c / denominator) == 0
    assert sp.simplify(discovered[x_ca] - c * a / denominator) == 0

    discovered_triangle = triangle_graph(
        discovered[x_ab],
        discovered[x_bc],
        discovered[x_ca],
    )
    assert response_matrix(discovered_triangle, ("A", "B", "C")) == star_response


def test_overlapping_eliminations_are_task_semantically_confluent():
    graph = graph_from_edges(
        (
            ("A", "U", sp.Integer(2)),
            ("B", "U", sp.Integer(3)),
            ("U", "V", sp.Integer(5)),
            ("V", "C", sp.Integer(7)),
            ("V", "D", sp.Integer(11)),
        )
    )
    boundary = ("A", "B", "C", "D")
    original_response = response_matrix(graph, boundary)

    eliminate_u_first = eliminate_internal_node(graph, "U")
    eliminate_v_first = eliminate_internal_node(graph, "V")

    # These are genuinely different intermediate presentations.
    assert eliminate_u_first != eliminate_v_first
    assert "V" in graph_nodes(eliminate_u_first)
    assert "U" in graph_nodes(eliminate_v_first)

    # Yet each local morphism preserves the declared task quotient exactly.
    assert response_matrix(eliminate_u_first, boundary) == original_response
    assert response_matrix(eliminate_v_first, boundary) == original_response

    # Completing the two histories yields one boundary-only presentation.
    left_normal = eliminate_internal_node(eliminate_u_first, "V")
    right_normal = eliminate_internal_node(eliminate_v_first, "U")
    assert left_normal == right_normal
    assert response_matrix(left_normal, boundary) == original_response

    expected = {
        ("A", "B"): sp.Rational(138, 205),
        ("A", "C"): sp.Rational(14, 41),
        ("A", "D"): sp.Rational(22, 41),
        ("B", "C"): sp.Rational(21, 41),
        ("B", "D"): sp.Rational(33, 41),
        ("C", "D"): sp.Rational(154, 41),
    }
    assert left_normal == expected


def test_two_weak_power_probes_do_not_certify_full_boundary_equivalence():
    star = graph_from_edges(
        (
            ("A", "X", sp.Integer(3)),
            ("B", "X", sp.Integer(5)),
            ("C", "X", sp.Integer(7)),
        )
    )
    boundary = ("A", "B", "C")
    target = response_matrix(star, boundary)

    # The true triangle conductances are (1, 7/3, 7/5).  Perturb in a
    # direction invisible to two scalar Dirichlet-energy probes.
    epsilon = sp.Rational(1, 10)
    impostor = triangle_graph(
        sp.Integer(1) + epsilon,
        sp.Rational(7, 3) - 5 * epsilon,
        sp.Rational(7, 5) + epsilon,
    )
    fake = response_matrix(impostor, boundary)

    probe_ab = sp.Matrix((1, -1, 0))
    probe_ac = sp.Matrix((1, 0, -1))
    probe_bc = sp.Matrix((0, 1, -1))

    assert quadratic_power(target, probe_ab) == quadratic_power(fake, probe_ab)
    assert quadratic_power(target, probe_ac) == quadratic_power(fake, probe_ac)

    assert quadratic_power(target, probe_bc) != quadratic_power(fake, probe_bc)
    assert fake != target

    # The failure is exact, not numerical.
    defect = (fake - target).applyfunc(sp.cancel)
    assert defect == sp.Matrix(
        (
            (sp.Rational(1, 5), sp.Rational(-1, 10), sp.Rational(-1, 10)),
            (sp.Rational(-1, 10), sp.Rational(-2, 5), sp.Rational(1, 2)),
            (sp.Rational(-1, 10), sp.Rational(1, 2), sp.Rational(-2, 5)),
        )
    )
    assert defect * sp.ones(3, 1) == sp.zeros(3, 1)
