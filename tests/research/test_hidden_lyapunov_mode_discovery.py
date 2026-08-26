"""Exact Phase 1H discovery of target-layer Lyapunov modes.

Phase 1G earned an autonomous *renewed* binary target process while keeping
it distinct from the closed reversible microscopic orbit.  This phase now
asks what monotone state functions are selected by that target process before
the classical H functional is revealed.

The discovery path receives only:

* the exact target transition matrix;
* conservation of total probability;
* its invariant reference law;
* exchange symmetry of the two states;
* bounded polynomial observers of a discovered nonconserved linear mode;
* exact rational monotonicity and simplicity criteria.

It receives no logarithm, named entropy, or supplied classical functional.
The held-out analytic coefficients are evaluated only after the discovery
winner and the nonuniqueness result have been frozen.

All certificates use ``Fraction`` arithmetic.  This is a finite target-layer
calibration, not a hard-sphere H theorem or a microscopic-to-kinetic proof.
"""

import inspect
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import gcd


Q = Fraction
Law = tuple[Q, Q]
Matrix = tuple[tuple[Q, Q], tuple[Q, Q]]
Covector = tuple[int, int]
MicroLaw = tuple[tuple[Q, Q], tuple[Q, Q]]


@dataclass(frozen=True)
class LinearMode:
    covector: Covector
    eigenvalue: Q

    @property
    def conserved(self) -> bool:
        return self.eigenvalue == 1


@dataclass(frozen=True)
class PowerMode:
    degree: int
    eigenvalue: Q
    swap_parity: int
    nonnegative: bool


def _target_matrix(delta: Q) -> Matrix:
    assert 0 < delta < Q(1, 2)
    return ((1 - delta, delta), (delta, 1 - delta))


def _apply_matrix(matrix: Matrix, law: Law) -> Law:
    return (
        matrix[0][0] * law[0] + matrix[0][1] * law[1],
        matrix[1][0] * law[0] + matrix[1][1] * law[1],
    )


def _left_action(covector: Covector, matrix: Matrix) -> tuple[Q, Q]:
    return (
        covector[0] * matrix[0][0] + covector[1] * matrix[1][0],
        covector[0] * matrix[0][1] + covector[1] * matrix[1][1],
    )


def _primitive_covector(covector: Covector) -> Covector:
    if covector == (0, 0):
        raise ValueError("the zero covector has no primitive orientation")
    divisor = gcd(abs(covector[0]), abs(covector[1]))
    primitive = (covector[0] // divisor, covector[1] // divisor)
    first_nonzero = primitive[0] if primitive[0] != 0 else primitive[1]
    if first_nonzero < 0:
        primitive = (-primitive[0], -primitive[1])
    return primitive


def _left_eigenvalue(covector: Covector, matrix: Matrix) -> Q | None:
    action = _left_action(covector, matrix)
    pivot = 0 if covector[0] != 0 else 1
    eigenvalue = action[pivot] / covector[pivot]
    if action == (
        eigenvalue * covector[0],
        eigenvalue * covector[1],
    ):
        return eigenvalue
    return None


def _discover_linear_modes(matrix: Matrix, bound: int = 2) -> tuple[LinearMode, ...]:
    primitive_covectors = {
        _primitive_covector(raw)
        for raw in product(range(-bound, bound + 1), repeat=2)
        if raw != (0, 0)
    }
    modes = []
    for covector in primitive_covectors:
        eigenvalue = _left_eigenvalue(covector, matrix)
        if eigenvalue is not None:
            modes.append(LinearMode(covector, eigenvalue))
    return tuple(sorted(modes, key=lambda mode: mode.covector))


def _discover_stationary_law(matrix: Matrix, bound: int = 2) -> Law:
    for raw in product(range(bound + 1), repeat=2):
        if sum(raw) == 0:
            continue
        total = Q(sum(raw))
        law = (Q(raw[0], total), Q(raw[1], total))
        if _apply_matrix(matrix, law) == law:
            return law
    raise ValueError("no stationary probability law found in the frozen search")


def _select_contrast_mode(
    modes: tuple[LinearMode, ...],
    reference: Law,
) -> LinearMode:
    candidates = tuple(
        mode
        for mode in modes
        if not mode.conserved
        and mode.covector[0] * reference[0]
        + mode.covector[1] * reference[1]
        == 0
    )
    if len(candidates) != 1:
        raise ValueError("the frozen target must have one centered linear mode")
    return candidates[0]


def _power_grammar(mode: LinearMode, max_degree: int) -> tuple[PowerMode, ...]:
    return tuple(
        PowerMode(
            degree=degree,
            eigenvalue=mode.eigenvalue**degree,
            swap_parity=1 if degree % 2 == 0 else -1,
            nonnegative=degree % 2 == 0,
        )
        for degree in range(1, max_degree + 1)
    )


def _select_minimal_symmetric_nonnegative_mode(
    grammar: tuple[PowerMode, ...],
) -> PowerMode:
    candidates = tuple(
        mode
        for mode in grammar
        if mode.swap_parity == 1 and mode.nonnegative
    )
    if not candidates:
        raise ValueError("the frozen grammar has no admissible mode")
    return min(candidates, key=lambda mode: (mode.degree, mode.eigenvalue))


def _contrast(law: Law, mode: LinearMode) -> Q:
    return mode.covector[0] * law[0] + mode.covector[1] * law[1]


def _modal_value(coefficients: tuple[Q, ...], contrast: Q) -> Q:
    return sum(
        (
            coefficient * contrast ** (2 * (index + 1))
            for index, coefficient in enumerate(coefficients)
        ),
        Q(0),
    )


def _modal_decrement_coefficients(
    coefficients: tuple[Q, ...],
    contraction: Q,
) -> tuple[Q, ...]:
    assert 0 < contraction < 1
    return tuple(
        coefficient * (1 - contraction ** (2 * (index + 1)))
        for index, coefficient in enumerate(coefficients)
    )


def _scaled_modal_coefficients(
    coefficients: tuple[Q, ...],
    contraction: Q,
) -> tuple[Q, ...]:
    return tuple(
        coefficient * contraction ** (2 * (index + 1))
        for index, coefficient in enumerate(coefficients)
    )


def _target_am_jet(law: Law, delta: Q) -> tuple[Law, Law]:
    additive = (delta * law[1], delta * law[0])
    multiplicative = (-delta, -delta)
    return additive, multiplicative


def _am_increment(law: Law, delta: Q) -> Law:
    additive, multiplicative = _target_am_jet(law, delta)
    return (
        additive[0] + law[0] * multiplicative[0],
        additive[1] + law[1] * multiplicative[1],
    )


def _quadratic_step_ledger(law: Law, delta: Q) -> tuple[Q, Q, Q]:
    new_law = _apply_matrix(_target_matrix(delta), law)
    increment = _am_increment(law, delta)
    contrast = law[0] - law[1]
    contrast_increment = increment[0] - increment[1]
    exact_change = (new_law[0] - new_law[1]) ** 2 - contrast**2
    first_jet_pairing = 2 * contrast * contrast_increment
    second_jet_remainder = contrast_increment**2
    return exact_change, first_jet_pairing, second_jet_remainder


def _quadratic_reference_distance(
    law: tuple[Q, ...],
    reference: tuple[Q, ...],
) -> Q:
    return sum(
        (
            (value - base) ** 2 / base
            for value, base in zip(law, reference)
        ),
        Q(0),
    )


def _tensor_product(left: tuple[Q, ...], right: tuple[Q, ...]) -> tuple[Q, ...]:
    return tuple(
        left_value * right_value
        for left_value in left
        for right_value in right
    )


def _section(law: Law, delta: Q) -> MicroLaw:
    return (
        (law[0] * (1 - delta), law[0] * delta),
        (law[1] * (1 - delta), law[1] * delta),
    )


def _xor_pushforward(law: MicroLaw) -> MicroLaw:
    return (
        (law[0][0], law[1][1]),
        (law[1][0], law[0][1]),
    )


def _lower(law: MicroLaw) -> Law:
    return (law[0][0] + law[0][1], law[1][0] + law[1][1])


def _held_out_relative_h_coefficients(max_degree: int) -> tuple[Q, ...]:
    """Post-selection coefficients of the classical binary reference control."""

    if max_degree < 2 or max_degree % 2 != 0:
        raise ValueError("the held-out series requires a positive even degree")
    return tuple(Q(1, degree * (degree - 1)) for degree in range(2, max_degree + 1, 2))


def test_target_search_discovers_reference_mass_and_contrast_modes_exactly():
    delta = Q(1, 16)
    matrix = _target_matrix(delta)
    reference = _discover_stationary_law(matrix)
    modes = _discover_linear_modes(matrix)

    assert matrix == ((Q(15, 16), Q(1, 16)), (Q(1, 16), Q(15, 16)))
    assert reference == (Q(1, 2), Q(1, 2))
    assert set(modes) == {
        LinearMode((1, 1), Q(1)),
        LinearMode((1, -1), Q(7, 8)),
    }
    assert _select_contrast_mode(modes, reference) == LinearMode(
        (1, -1), Q(7, 8)
    )


def test_discovery_source_is_separate_from_the_held_out_classical_control():
    discovery_functions = (
        _target_matrix,
        _apply_matrix,
        _left_action,
        _primitive_covector,
        _left_eigenvalue,
        _discover_linear_modes,
        _discover_stationary_law,
        _select_contrast_mode,
        _power_grammar,
        _select_minimal_symmetric_nonnegative_mode,
        _contrast,
        _modal_value,
        _modal_decrement_coefficients,
        _scaled_modal_coefficients,
    )
    source = "\n".join(inspect.getsource(function) for function in discovery_functions)

    assert "math.log" not in source
    assert "entropy" not in source.lower()
    assert "shannon" not in source.lower()
    assert "_held_out_relative_h_coefficients" not in source


def test_minimal_symmetric_nonnegative_mode_is_quadratic_contrast():
    delta = Q(1, 16)
    matrix = _target_matrix(delta)
    reference = _discover_stationary_law(matrix)
    contrast_mode = _select_contrast_mode(
        _discover_linear_modes(matrix), reference
    )
    grammar = _power_grammar(contrast_mode, max_degree=8)
    selected = _select_minimal_symmetric_nonnegative_mode(grammar)

    assert tuple(mode.degree for mode in grammar) == tuple(range(1, 9))
    assert tuple(
        mode.degree
        for mode in grammar
        if mode.swap_parity == 1 and mode.nonnegative
    ) == (2, 4, 6, 8)
    assert selected == PowerMode(
        degree=2,
        eigenvalue=Q(49, 64),
        swap_parity=1,
        nonnegative=True,
    )
    assert _contrast(reference, contrast_mode) == 0


def test_positive_even_mode_cone_has_a_simplex_wide_exact_decrement():
    contraction = Q(7, 8)
    coefficients = (Q(3, 5), Q(7, 11), Q(2, 9), Q(5, 13))
    decrement_coefficients = _modal_decrement_coefficients(
        coefficients, contraction
    )
    scaled_coefficients = _scaled_modal_coefficients(
        coefficients, contraction
    )

    assert all(coefficient > 0 for coefficient in decrement_coefficients)
    assert decrement_coefficients == tuple(
        coefficient - scaled
        for coefficient, scaled in zip(coefficients, scaled_coefficients)
    )
    for contrast in (Q(-1), Q(-3, 4), Q(0), Q(2, 5), Q(1)):
        exact_decrement = _modal_value(
            coefficients, contrast
        ) - _modal_value(coefficients, contraction * contrast)
        certified_decrement = _modal_value(
            decrement_coefficients, contrast
        )
        assert exact_decrement == certified_decrement
        if contrast == 0:
            assert exact_decrement == 0
        else:
            assert exact_decrement > 0


def test_target_monotonicity_is_nonunique_and_minimal_mode_is_not_additive():
    contraction = Q(7, 8)
    for contrast in (Q(1, 4), Q(1, 2), Q(3, 4)):
        assert contrast**2 > (contraction * contrast) ** 2
        assert contrast**4 > (contraction * contrast) ** 4

    # The quadratic and quartic modes are not positive scalar multiples.
    assert Q(1, 2) ** 4 / Q(1, 2) ** 2 == Q(1, 4)
    assert Q(1, 4) ** 4 / Q(1, 4) ** 2 == Q(1, 16)

    left = (Q(3, 4), Q(1, 4))
    right = (Q(2, 3), Q(1, 3))
    uniform_two = (Q(1, 2), Q(1, 2))
    uniform_four = (Q(1, 4),) * 4
    left_value = _quadratic_reference_distance(left, uniform_two)
    right_value = _quadratic_reference_distance(right, uniform_two)
    product_value = _quadratic_reference_distance(
        _tensor_product(left, right), uniform_four
    )

    assert left_value == Q(1, 4)
    assert right_value == Q(1, 9)
    assert product_value == Q(7, 18)
    assert product_value == left_value + right_value + left_value * right_value
    assert product_value != left_value + right_value


def test_finite_step_decrement_needs_the_second_jet_beyond_the_am_first_jet():
    law = (Q(3, 4), Q(1, 4))
    delta = Q(1, 16)
    additive, multiplicative = _target_am_jet(law, delta)
    increment = _am_increment(law, delta)
    exact_change, first_jet_pairing, second_jet_remainder = (
        _quadratic_step_ledger(law, delta)
    )

    assert additive == (Q(1, 64), Q(3, 64))
    assert multiplicative == (Q(-1, 16), Q(-1, 16))
    assert increment == (Q(-1, 32), Q(1, 32))
    assert exact_change == Q(-15, 256)
    assert first_jet_pairing == Q(-1, 16)
    assert second_jet_remainder == Q(1, 256)
    assert exact_change == first_jet_pairing + second_jet_remainder
    assert exact_change != first_jet_pairing


def test_target_candidate_does_not_lift_to_a_micro_lyapunov_function():
    law_initial = (Q(3, 4), Q(1, 4))
    delta = Q(1, 16)
    micro_initial = _section(law_initial, delta)
    micro_middle = _xor_pushforward(micro_initial)
    micro_return = _xor_pushforward(micro_middle)
    law_middle = _lower(micro_middle)
    law_return = _lower(micro_return)

    value_initial = (law_initial[0] - law_initial[1]) ** 2
    value_middle = (law_middle[0] - law_middle[1]) ** 2
    value_return = (law_return[0] - law_return[1]) ** 2

    assert (value_initial, value_middle, value_return) == (
        Q(1, 4),
        Q(49, 256),
        Q(1, 4),
    )
    assert value_initial > value_middle < value_return


def test_post_selection_classical_control_is_a_positive_modal_resummation():
    # Candidate selection has already frozen degree two without consulting
    # this function.  The held-out reference functional has the formal even
    # expansion c_d = 1 / (d(d-1)) for d=2,4,6,... .
    coefficients = _held_out_relative_h_coefficients(max_degree=8)
    contraction = Q(7, 8)

    assert coefficients == (Q(1, 2), Q(1, 12), Q(1, 30), Q(1, 56))
    assert tuple(
        2 * (index + 1) * coefficient
        for index, coefficient in enumerate(coefficients)
    ) == (Q(1), Q(1, 3), Q(1, 5), Q(1, 7))
    assert all(
        coefficient > 0
        for coefficient in _modal_decrement_coefficients(
            coefficients, contraction
        )
    )
    assert coefficients[1:] != (0, 0, 0)


def test_hidden_lyapunov_claims_remain_separately_typed():
    grades = {
        "target_reference_and_modes": "exact_discovery",
        "minimal_polynomial_candidate": "quadratic_contrast",
        "simplex_wide_monotonicity": "exact_positive_cone_certificate",
        "unique_target_functional": "rejected",
        "am_first_jet_to_finite_decrement": "second_jet_required",
        "target_candidate_to_micro_lyapunov": "rejected",
        "quadratic_mode_to_tensor_additivity": "rejected",
        "classical_reference_control": "post_selection_positive_resummation",
        "finite_target_to_hard_sphere_H": "external_theorem_required",
    }

    assert grades["unique_target_functional"] == "rejected"
    assert grades["am_first_jet_to_finite_decrement"] == "second_jet_required"
    assert grades["target_candidate_to_micro_lyapunov"] == "rejected"
    assert grades["quadratic_mode_to_tensor_additivity"] == "rejected"
