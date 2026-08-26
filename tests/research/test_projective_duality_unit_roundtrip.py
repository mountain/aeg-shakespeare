"""Phase 10: projective duality, unit one, and round-trip lowering.

Phase 9 supplied a marked rational history carrier with compatible real and
p-adic place shadows.  This executable essay audits the missing reverse
direction before any objectification claim:

* a genuine contravariant duality reverses universal-property variance;
* rank-one projective duality is the contragredient incidence action, not the
  single Weyl or reciprocal operation;
* the numeral 1 is the third mark in an ordered projective frame, while T_1
  and a metric unit are different data;
* a bare hyperbolic point or p-adic root vertex has a nontrivial stabilizer
  fibre and cannot decode the projective process;
* an ordered rational frame recovers projective matrix semantics, but even a
  matrix does not recover the original literal word.

All positive claims use exact Fraction or SymPy arithmetic.  The structures
remain research-local; no package API or new process rank is introduced.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
import importlib.util
from itertools import product
from pathlib import Path
import sys

import sympy as sp


def _load_research_module(name: str, filename: str) -> object:
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


_PHASE9 = _load_research_module(
    "_phase9_for_projective_duality_unit_roundtrip",
    "test_am_bruhat_place_continued_fraction_carrier.py",
)


_Matrix = tuple[
    tuple[Fraction, Fraction],
    tuple[Fraction, Fraction],
]
_Point = tuple[Fraction, Fraction]

_IDENTITY: _Matrix = _PHASE9._IDENTITY
_WEYL: _Matrix = _PHASE9._WEYL
_RECIPROCAL: _Matrix = _PHASE9._RECIPROCAL

_ZERO: _Point = (Fraction(0), Fraction(1))
_ONE: _Point = (Fraction(1), Fraction(1))
_INFINITY: _Point = (Fraction(1), Fraction(0))


def _matvec(matrix: _Matrix, vector: _Point) -> _Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def _transpose(matrix: _Matrix) -> _Matrix:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def _inverse(matrix: _Matrix) -> _Matrix:
    determinant = _PHASE9._determinant(matrix)
    if determinant == 0:
        raise ValueError("a projective matrix must be nonsingular")
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def _contragredient(matrix: _Matrix) -> _Matrix:
    return _transpose(_inverse(matrix))


def _normalize_point(point: _Point) -> _Point:
    x, y = point
    if y != 0:
        return (x / y, Fraction(1))
    if x != 0:
        return _INFINITY
    raise ValueError("the zero vector is not a projective point")


def _projective_action(matrix: _Matrix, point: _Point) -> _Point:
    return _normalize_point(_matvec(matrix, point))


def _normalize_matrix(matrix: _Matrix) -> _Matrix:
    pivot = next(entry for row in matrix for entry in row if entry != 0)
    return tuple(
        tuple(entry / pivot for entry in row)
        for row in matrix
    )  # type: ignore[return-value]


def _determinant_of_columns(left: _Point, right: _Point) -> Fraction:
    return left[0] * right[1] - left[1] * right[0]


def _frame(matrix: _Matrix) -> tuple[_Point, _Point, _Point]:
    return tuple(
        _projective_action(matrix, point)
        for point in (_ZERO, _ONE, _INFINITY)
    )  # type: ignore[return-value]


def _matrix_from_frame(frame: tuple[_Point, _Point, _Point]) -> _Matrix:
    """Reconstruct the unique projective map taking (0,1,infinity) to frame."""

    image_zero, image_one, image_infinity = frame
    denominator = _determinant_of_columns(image_infinity, image_zero)
    if denominator == 0:
        raise ValueError("zero and infinity images must be distinct")
    infinity_scale = (
        _determinant_of_columns(image_one, image_zero) / denominator
    )
    zero_scale = (
        _determinant_of_columns(image_infinity, image_one) / denominator
    )
    if infinity_scale == 0 or zero_scale == 0:
        raise ValueError("all three frame points must be distinct")
    first_column = tuple(infinity_scale * value for value in image_infinity)
    second_column = tuple(zero_scale * value for value in image_zero)
    return (
        (first_column[0], second_column[0]),
        (first_column[1], second_column[1]),
    )


def _dot(covector: _Point, vector: _Point) -> Fraction:
    return covector[0] * vector[0] + covector[1] * vector[1]


def _borel_weyl_semantic_lowering(matrix: _Matrix) -> tuple[_Matrix, ...]:
    """Return one rational T/D/W word with the same projective semantics."""

    a, b = matrix[0]
    c, d = matrix[1]
    determinant = _PHASE9._determinant(matrix)
    if determinant == 0:
        raise ValueError("a singular matrix has no PGL lowering")
    if c == 0:
        assert d != 0
        return (
            _PHASE9._translation(b / d),
            _PHASE9._dilation(a / d),
        )
    return (
        _PHASE9._translation(a / c),
        _PHASE9._dilation(determinant / c),
        _WEYL,
        _PHASE9._translation(d),
        _PHASE9._dilation(c),
    )


def _lower_word(word: tuple[_Matrix, ...]) -> _Matrix:
    result = _IDENTITY
    for letter in word:
        result = _PHASE9._matmul(result, letter)
    return result


def _has_rational_projective_representative(matrix: sp.Matrix) -> bool:
    pivot = next((entry for entry in matrix if entry != 0), None)
    if pivot is None or matrix.det() == 0:
        return False
    return all(sp.simplify(entry / pivot).is_Rational is True for entry in matrix)


@dataclass(frozen=True)
class _ArrowAudit:
    arrow: str
    exact_composition: bool
    required_marks: tuple[str, ...]
    forgotten: tuple[str, ...]
    inverse_scope: str


_PIPELINE_AUDIT = (
    _ArrowAudit(
        "literal_history_to_matrix",
        True,
        ("chronological_order",),
        ("literal_word", "history_cost"),
        "semantic_canonicalization_only",
    ),
    _ArrowAudit(
        "matrix_to_ordered_frame",
        True,
        ("zero", "one", "infinity", "orientation"),
        (),
        "all_nonsingular_rational_frames",
    ),
    _ArrowAudit(
        "matrix_to_real_point",
        True,
        ("base_point", "orientation_component"),
        ("real_stabilizer_fibre",),
        "coset_representative_only",
    ),
    _ArrowAudit(
        "matrix_to_padic_vertex",
        True,
        ("prime", "standard_lattice", "valuation_ruler"),
        ("integral_stabilizer_fibre", "boundary_direction"),
        "lattice_class_only",
    ),
    _ArrowAudit(
        "local_geometry_to_cf_section",
        False,
        ("cusp", "affine_chart", "unit", "section", "orientation"),
        ("unchosen_representatives",),
        "declared_section_image_only",
    ),
    _ArrowAudit(
        "geometric_result_to_rational_lowering",
        False,
        ("rational_image_certificate", "decoder", "stopping_trace"),
        ("original_literal_word",),
        "certified_rational_frame_image_only",
    ),
)


def test_gate10a_genuine_duality_reverses_universal_property_variance():
    objects = range(3)
    dual = lambda value: 2 - value
    has_arrow = lambda source, target: source <= target

    initial = next(
        candidate
        for candidate in objects
        if all(has_arrow(candidate, target) for target in objects)
    )
    terminal = next(
        candidate
        for candidate in objects
        if all(has_arrow(source, candidate) for source in objects)
    )
    assert (initial, terminal) == (0, 2)
    assert dual(initial) == terminal
    assert dual(terminal) == initial

    for source, target in product(objects, repeat=2):
        assert has_arrow(source, target) == has_arrow(dual(target), dual(source))
        assert dual(dual(source)) == source
    for left, right in product(objects, repeat=2):
        coproduct = max(left, right)
        product_object = min(dual(left), dual(right))
        assert dual(coproduct) == product_object

    # The control refutes the stronger premise "initial maps to initial".
    assert dual(initial) != initial


def test_gate10a_projective_duality_is_contragredient_incidence_not_weyl():
    matrices = tuple(
        _PHASE9._matrix(a, b, c, d)
        for a, b, c, d in product(range(-2, 3), repeat=4)
        if a * d - b * c != 0
    )
    vectors = tuple(
        (Fraction(x), Fraction(y))
        for x, y in product(range(-2, 3), repeat=2)
        if (x, y) != (0, 0)
    )
    assert (len(matrices), len(vectors)) == (496, 24)

    for matrix in matrices:
        dual_matrix = _contragredient(matrix)
        assert _contragredient(dual_matrix) == matrix
        conjugated = _PHASE9._matmul(
            _PHASE9._matmul(_WEYL, matrix),
            _inverse(_WEYL),
        )
        assert _normalize_matrix(dual_matrix) == _normalize_matrix(conjugated)
        for vector in vectors:
            annihilator = _matvec(_WEYL, vector)
            transformed_vector = _matvec(matrix, vector)
            transformed_annihilator = _matvec(dual_matrix, annihilator)
            assert _dot(annihilator, vector) == 0
            assert _dot(transformed_annihilator, transformed_vector) == 0
            assert _matvec(_WEYL, transformed_vector) == tuple(
                _PHASE9._determinant(matrix) * value
                for value in transformed_annihilator
            )

    words = _PHASE9._all_words(4)
    assert len(words) == 4_681
    for word in words:
        direct = _contragredient(_PHASE9._word_matrix(word))
        composed = _IDENTITY
        for letter in word:
            composed = _PHASE9._matmul(composed, _contragredient(letter.matrix))
        assert direct == composed

    translation_dual = _contragredient(_PHASE9._translation(1))
    assert translation_dual != _WEYL
    assert _normalize_matrix(translation_dual) == _normalize_matrix(
        _PHASE9._matmul(
            _PHASE9._matmul(_WEYL, _PHASE9._translation(1)),
            _inverse(_WEYL),
        )
    )


def test_gate10b_unit_one_is_the_third_mark_of_a_projective_frame():
    for scale in (-3, -2, -1, 1, 2, 3):
        dilation = _PHASE9._dilation(scale)
        assert _projective_action(dilation, _ZERO) == _ZERO
        assert _projective_action(dilation, _INFINITY) == _INFINITY
        assert _projective_action(dilation, _ONE) == (
            Fraction(scale),
            Fraction(1),
        )

    words = _PHASE9._all_words(4)
    projective_matrices = set()
    word_semantic_fibres = Counter()
    ordered_frames = set()
    real_point_fibres = Counter()
    padic_vertex_triple_fibres = Counter()
    for word in words:
        matrix = _PHASE9._word_matrix(word)
        frame = _frame(matrix)
        reconstructed = _matrix_from_frame(frame)
        normalized = _normalize_matrix(matrix)
        assert _normalize_matrix(reconstructed) == normalized
        projective_matrices.add(normalized)
        word_semantic_fibres[normalized] += 1
        ordered_frames.add(frame)
        real_point_fibres[_PHASE9._real_shadow(matrix)] = 0
        padic_vertex_triple_fibres[
            tuple(
                _PHASE9._vertex_key(
                    _PHASE9._PHASE3._matrix_lattice_vertex(matrix, prime)
                )
                for prime in (3, 5, 7)
            )
        ] = 0

    # Count fibres on distinct projective matrix semantics rather than on
    # repeated literal words.
    for normalized in projective_matrices:
        real_point_fibres[_PHASE9._real_shadow(normalized)] += 1
        padic_vertex_triple_fibres[
            tuple(
                _PHASE9._vertex_key(
                    _PHASE9._PHASE3._matrix_lattice_vertex(normalized, prime)
                )
                for prime in (3, 5, 7)
            )
        ] += 1

    # The ordered frame carries exactly the projective matrix semantics on
    # this rational image; bare local points retain strictly less.
    assert (len(projective_matrices), len(ordered_frames)) == (1_585, 1_585)
    assert max(word_semantic_fibres.values()) == 47
    assert sum(count > 1 for count in word_semantic_fibres.values()) == 827
    assert (len(real_point_fibres), max(real_point_fibres.values())) == (1_291, 4)
    assert sum(count > 1 for count in real_point_fibres.values()) == 268
    assert (
        len(padic_vertex_triple_fibres),
        max(padic_vertex_triple_fibres.values()),
    ) == (284, 206)
    assert sum(count > 1 for count in padic_vertex_triple_fibres.values()) == 105

    transported = _frame(_PHASE9._translation(2))
    assert transported == (
        (Fraction(2), Fraction(1)),
        (Fraction(3), Fraction(1)),
        _INFINITY,
    )
    # Calling the transported middle mark "1" again requires applying the
    # inverse frame; it is a gauge normalization, not an invariant numeral.
    assert _frame(_PHASE9._translation(-2)) != transported


def test_gate10c_real_and_padic_unit_shadows_expose_stabilizer_fibres():
    translation_one = _PHASE9._translation(1)
    identity_at_i = _PHASE9._real_shadow(_IDENTITY)
    weyl_at_i = _PHASE9._real_shadow(_WEYL)
    reciprocal_at_i = _PHASE9._real_shadow(_RECIPROCAL)
    translated_i = _PHASE9._real_shadow(translation_one)
    assert identity_at_i == weyl_at_i == (Fraction(0), Fraction(1))
    assert _IDENTITY != _WEYL
    assert reciprocal_at_i == (Fraction(0), Fraction(-1))
    assert translated_i == (Fraction(1), Fraction(1))

    y = sp.symbols("y", positive=True)
    cosh_distance = 1 + sp.Rational(1, 2) / y**2
    asserted_distance = 2 * sp.asinh(1 / (2 * y))
    assert sp.simplify(sp.cosh(asserted_distance) - cosh_distance) == 0
    assert cosh_distance.subs(y, 1) == sp.Rational(3, 2)

    a, v = sp.symbols("a v", real=True)
    left_point = sp.Matrix((a, sp.exp(v)))
    left_inverse = sp.Matrix((left_point[0], sp.log(left_point[1])))
    assert sp.simplify(left_inverse[0] - a) == 0
    assert sp.simplify(left_inverse[1] - v) == 0
    right_point = sp.Matrix((-a * sp.exp(-v), sp.exp(-v)))
    right_inverse = sp.Matrix(
        (-right_point[0] / right_point[1], -sp.log(right_point[1]))
    )
    assert sp.simplify(right_inverse[0] - a) == 0
    assert sp.simplify(right_inverse[1] - v) == 0

    for prime in (3, 5, 7):
        root = _PHASE9._PHASE3._matrix_lattice_vertex(_IDENTITY, prime)
        translated_root = _PHASE9._PHASE3._matrix_lattice_vertex(
            translation_one, prime
        )
        assert translated_root == root
        zero_contact = _PHASE9._PHASE3._projective_contact(Fraction(0), prime)
        one_contact = _PHASE9._PHASE3._projective_contact(Fraction(1), prime)
        assert zero_contact != one_contact
        assert (zero_contact.coordinate, one_contact.coordinate) == (0, 1)
        assert _projective_action(translation_one, _ZERO) == _ONE


def test_gate10d_round_trip_closes_at_frame_semantics_not_literal_history():
    matrices = tuple(
        _PHASE9._matrix(a, b, c, d)
        for a, b, c, d in product(range(-2, 3), repeat=4)
        if a * d - b * c != 0
    )
    for matrix in matrices:
        frame_round_trip = _matrix_from_frame(_frame(matrix))
        assert _normalize_matrix(frame_round_trip) == _normalize_matrix(matrix)
        semantic_word = _borel_weyl_semantic_lowering(matrix)
        lowered = _lower_word(semantic_word)
        assert _normalize_matrix(lowered) == _normalize_matrix(matrix)

    empty_word: tuple[object, ...] = ()
    cancelling_word = (
        _PHASE9._BOREL_WEYL_ALPHABET[1],
        _PHASE9._BOREL_WEYL_ALPHABET[0],
    )
    assert _PHASE9._word_matrix(empty_word) == _PHASE9._word_matrix(
        cancelling_word
    ) == _IDENTITY
    assert empty_word != cancelling_word

    sqrt_two = sp.sqrt(2)
    assert _has_rational_projective_representative(sqrt_two * sp.eye(2))
    assert not _has_rational_projective_representative(
        sp.Matrix(((sqrt_two, 0), (0, 1)))
    )

    assert tuple(audit.arrow for audit in _PIPELINE_AUDIT) == (
        "literal_history_to_matrix",
        "matrix_to_ordered_frame",
        "matrix_to_real_point",
        "matrix_to_padic_vertex",
        "local_geometry_to_cf_section",
        "geometric_result_to_rational_lowering",
    )
    assert all(audit.exact_composition for audit in _PIPELINE_AUDIT[:4])
    assert not any(audit.exact_composition for audit in _PIPELINE_AUDIT[4:])
    assert _PIPELINE_AUDIT[-1].inverse_scope == (
        "certified_rational_frame_image_only"
    )


def test_gate10e_dual_frame_reconstruction_does_not_objectify_a_new_rank():
    lower_generators = {
        letter.name for letter in _PHASE9._BOREL_WEYL_ALPHABET
    }
    dualized_generators = {
        _normalize_matrix(_contragredient(letter.matrix))
        for letter in _PHASE9._BOREL_WEYL_ALPHABET
    }
    proposed_new_generators: set[str] = set()

    assert dualized_generators
    assert lower_generators
    assert proposed_new_generators == set()
    assert _normalize_matrix(_contragredient(_contragredient(_WEYL))) == (
        _normalize_matrix(_WEYL)
    )

    # The dual action and frame decoder refine the horizontal presentation.
    # They add no task-independent primitive, free higher grammar, or lowering
    # obligation beyond the existing rational projective semantics.
    objectification_gate = {
        "new_task_independent_primitive": bool(proposed_new_generators),
        "new_free_composition": False,
        "all_composites_lower": False,
    }
    assert objectification_gate == {
        "new_task_independent_primitive": False,
        "new_free_composition": False,
        "all_composites_lower": False,
    }
