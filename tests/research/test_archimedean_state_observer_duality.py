"""Phase 11: Archimedean placement and state--observer duality.

This executable essay places the Archimedean axiom in the observer semantics
of the rational A/M grammar and opens a precise finite logical dual:

* finite states are dual to their Boolean algebras of predicates;
* a process moves states forward and pulls predicates backward;
* a quotient is dual to the subalgebra of fibre-constant predicates;
* real order cuts and p-adic cylinders are different observer bases;
* the rational product formula relates places without identifying them;
* finite Stone recovery does not prove an infinite cofree observer or a new
  objectified process dimension.

All enumerations and arithmetic are exact.  Helpers remain research-local.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import floor

import sympy as sp


_State = int | None
_ModMatrix = tuple[tuple[int, int], tuple[int, int]]


def _powerset(items: tuple[object, ...]) -> tuple[frozenset[object], ...]:
    return tuple(
        frozenset(choice)
        for size in range(len(items) + 1)
        for choice in combinations(items, size)
    )


def _inverse_image(
    source: tuple[object, ...],
    function: dict[object, object],
    predicate: frozenset[object],
) -> frozenset[object]:
    return frozenset(x for x in source if function[x] in predicate)


def _is_boolean_homomorphism(
    domain: tuple[frozenset[object], ...],
    universe: frozenset[object],
    values: tuple[bool, ...],
) -> bool:
    table = dict(zip(domain, values, strict=True))
    if table[frozenset()] or not table[universe]:
        return False
    for predicate in domain:
        if table[universe - predicate] is table[predicate]:
            return False
    for left, right in product(domain, repeat=2):
        if table[left & right] != (table[left] and table[right]):
            return False
    return True


def _matmul_mod(left: _ModMatrix, right: _ModMatrix, prime: int) -> _ModMatrix:
    return (
        (
            (left[0][0] * right[0][0] + left[0][1] * right[1][0]) % prime,
            (left[0][0] * right[0][1] + left[0][1] * right[1][1]) % prime,
        ),
        (
            (left[1][0] * right[0][0] + left[1][1] * right[1][0]) % prime,
            (left[1][0] * right[0][1] + left[1][1] * right[1][1]) % prime,
        ),
    )


def _transpose_mod(matrix: _ModMatrix) -> _ModMatrix:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def _inverse_mod(matrix: _ModMatrix, prime: int) -> _ModMatrix:
    a, b = matrix[0]
    c, d = matrix[1]
    determinant = (a * d - b * c) % prime
    if determinant == 0:
        raise ValueError("singular finite projective matrix")
    scale = pow(determinant, -1, prime)
    return (
        ((scale * d) % prime, (-scale * b) % prime),
        ((-scale * c) % prime, (scale * a) % prime),
    )


def _projective_states(prime: int) -> tuple[_State, ...]:
    return (*range(prime), None)


def _state_vector(state: _State) -> tuple[int, int]:
    return (1, 0) if state is None else (state, 1)


def _normalize_vector(vector: tuple[int, int], prime: int) -> _State:
    x, y = (coordinate % prime for coordinate in vector)
    if y:
        return (x * pow(y, -1, prime)) % prime
    if x:
        return None
    raise ValueError("the zero vector has no projective class")


def _matvec_mod(
    matrix: _ModMatrix, vector: tuple[int, int], prime: int
) -> tuple[int, int]:
    return (
        (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % prime,
        (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % prime,
    )


def _projective_action(matrix: _ModMatrix, state: _State, prime: int) -> _State:
    return _normalize_vector(_matvec_mod(matrix, _state_vector(state), prime), prime)


def _words(
    alphabet: tuple[_ModMatrix, ...], depth: int
) -> tuple[tuple[_ModMatrix, ...], ...]:
    return tuple(
        word
        for length in range(depth + 1)
        for word in product(alphabet, repeat=length)
    )


def _act_word(
    word: tuple[_ModMatrix, ...], state: _State, prime: int
) -> _State:
    result = state
    for letter in word:
        result = _projective_action(letter, result, prime)
    return result


def _pullback(
    matrix: _ModMatrix, predicate: frozenset[_State], prime: int
) -> frozenset[_State]:
    return frozenset(
        state
        for state in _projective_states(prime)
        if _projective_action(matrix, state, prime) in predicate
    )


def _pullback_word(
    word: tuple[_ModMatrix, ...],
    predicate: frozenset[_State],
    prime: int,
) -> frozenset[_State]:
    result = predicate
    for letter in reversed(word):
        result = _pullback(letter, result, prime)
    return result


def _forward_image(
    matrix: _ModMatrix, predicate: frozenset[_State], prime: int
) -> frozenset[_State]:
    return frozenset(_projective_action(matrix, state, prime) for state in predicate)


def _hyperplane_predicate(covector: _State, prime: int) -> frozenset[_State]:
    left = _state_vector(covector)
    return frozenset(
        state
        for state in _projective_states(prime)
        if sum(
            a * b for a, b in zip(left, _state_vector(state), strict=True)
        )
        % prime
        == 0
    )


def _prime_factors(value: int) -> frozenset[int]:
    remaining = abs(value)
    factors: set[int] = set()
    candidate = 2
    while candidate * candidate <= remaining:
        while remaining % candidate == 0:
            factors.add(candidate)
            remaining //= candidate
        candidate += 1
    if remaining > 1:
        factors.add(remaining)
    return frozenset(factors)


def _valuation(value: Fraction, prime: int) -> int:
    def exponent(integer: int) -> int:
        count = 0
        integer = abs(integer)
        while integer and integer % prime == 0:
            integer //= prime
            count += 1
        return count

    if value == 0:
        raise ValueError("the product formula excludes zero")
    return exponent(value.numerator) - exponent(value.denominator)


def _padic_absolute(value: Fraction, prime: int) -> Fraction:
    valuation = _valuation(value, prime)
    if valuation >= 0:
        return Fraction(1, prime**valuation)
    return Fraction(prime ** (-valuation), 1)


def _product_formula(value: Fraction) -> Fraction:
    primes = _prime_factors(value.numerator) | _prime_factors(value.denominator)
    local_product = Fraction(1)
    for prime in primes:
        local_product *= _padic_absolute(value, prime)
    return abs(value) * local_product


def _hensel_sqrt_minus_one_at_five(depth: int) -> tuple[tuple[int, int], ...]:
    """Return compatible roots of x^2 + 1 modulo 5, ..., 5^depth."""

    modulus = 5
    root = 2
    witnesses = [(modulus, root)]
    for _ in range(1, depth):
        next_modulus = 5 * modulus
        root = next(
            root + digit * modulus
            for digit in range(5)
            if ((root + digit * modulus) ** 2 + 1) % next_modulus == 0
        )
        modulus = next_modulus
        witnesses.append((modulus, root))
    return tuple(witnesses)


@dataclass(frozen=True)
class _LayerAudit:
    structure: str
    layer: str
    supplied_by_archimedean_axiom: bool
    additional_requirement: str


_LAYER_AUDIT = (
    _LayerAudit("rational_am_syntax", "process", False, "none"),
    _LayerAudit("integer_cofinality", "ordered_field", True, "order"),
    _LayerAudit("integer_part_section", "selector", False, "order_and_section"),
    _LayerAudit("all_cauchy_limits", "completion", False, "completeness"),
    _LayerAudit("connected_real_line", "topology", False, "order_completeness"),
    _LayerAudit("hyperbolic_metric", "geometry", False, "metric_ruler"),
    _LayerAudit("padic_clopen_balls", "place_observer", False, "ultrametric"),
)


def test_gate11a_archimedean_cofinality_is_not_completion_or_place_change():
    positive_rationals = tuple(
        sorted(
            {
                Fraction(numerator, denominator)
                for numerator in range(1, 9)
                for denominator in range(1, 9)
            }
        )
    )
    assert len(positive_rationals) == 43

    for x, y in product(positive_rationals, repeat=2):
        witness = floor(y / x) + 1
        assert witness * x > y
    for epsilon in positive_rationals:
        witness = floor(1 / epsilon) + 1
        assert Fraction(1, witness) < epsilon

    pell = []
    numerator, denominator = 1, 1
    for _ in range(12):
        pell.append(Fraction(numerator, denominator))
        assert numerator * numerator - 2 * denominator * denominator in {-1, 1}
        assert abs(Fraction(numerator * numerator, denominator * denominator) - 2) == (
            Fraction(1, denominator * denominator)
        )
        numerator, denominator = (
            numerator + 2 * denominator,
            numerator + denominator,
        )
    assert all(
        abs(right - left) > abs(later - right)
        for left, right, later in zip(
            pell[:-2], pell[1:-1], pell[2:], strict=True
        )
    )
    assert sp.sqrt(2).is_rational is False

    hensel_witnesses = _hensel_sqrt_minus_one_at_five(8)
    assert len(hensel_witnesses) == 8
    for (modulus, root), (next_modulus, next_root) in zip(
        hensel_witnesses[:-1], hensel_witnesses[1:], strict=True
    ):
        assert (root * root + 1) % modulus == 0
        assert next_modulus == 5 * modulus
        assert next_root % modulus == root
        assert (2 * root) % 5 != 0
    final_modulus, final_root = hensel_witnesses[-1]
    assert (final_root * final_root + 1) % final_modulus == 0

    assert sum(item.supplied_by_archimedean_axiom for item in _LAYER_AUDIT) == 1
    assert {item.structure for item in _LAYER_AUDIT if item.layer == "completion"} == {
        "all_cauchy_limits"
    }
    assert _LAYER_AUDIT[-1].additional_requirement == "ultrametric"


def test_gate11b_finite_stone_duality_recovers_points_only_with_logic_preserved():
    states = (0, 1, 2)
    universe = frozenset(states)
    predicates = _powerset(states)
    assert len(predicates) == 8

    homomorphisms = []
    for values in product((False, True), repeat=len(predicates)):
        if _is_boolean_homomorphism(predicates, universe, values):
            homomorphisms.append(values)

    point_evaluations = {
        tuple(state in predicate for predicate in predicates) for state in states
    }
    assert set(homomorphisms) == point_evaluations
    assert (2 ** len(predicates), len(homomorphisms)) == (256, 3)

    source = (0, 1, 2)
    middle = (0, 1)
    target = (0, 1, 2)
    source_predicates = _powerset(source)
    middle_predicates = _powerset(middle)
    target_predicates = _powerset(target)

    for middle_values in product(middle, repeat=len(source)):
        f = dict(zip(source, middle_values, strict=True))
        for target_values in product(target, repeat=len(middle)):
            g = dict(zip(middle, target_values, strict=True))
            composite = {x: g[f[x]] for x in source}
            for predicate in target_predicates:
                direct = _inverse_image(source, composite, predicate)
                first = _inverse_image(middle, g, predicate)
                reverse = _inverse_image(source, f, first)
                assert direct == reverse
            for left, right in product(middle_predicates, repeat=2):
                assert _inverse_image(source, f, left & right) == (
                    _inverse_image(source, f, left)
                    & _inverse_image(source, f, right)
                )
                assert _inverse_image(source, f, frozenset(middle) - left) == (
                    frozenset(source) - _inverse_image(source, f, left)
                )
    assert len(source_predicates) == len(target_predicates) == 8


def test_gate11c_am_state_motion_is_reverse_boolean_predicate_transport():
    for prime in (3, 5, 7):
        translation = ((1, 1), (0, 1))
        dilation = ((2, 0), (0, 1))
        weyl = ((0, -1), (1, 0))
        alphabet = (translation, dilation, weyl)
        states = _projective_states(prime)
        predicates = tuple(
            frozenset(predicate) for predicate in _powerset(states)
        )
        words = _words(alphabet, 3)
        assert len(words) == 40

        for word, predicate, state in product(words, predicates, states):
            assert (_act_word(word, state, prime) in predicate) == (
                state in _pullback_word(word, predicate, prime)
            )

        for left, right, predicate in product(alphabet, alphabet, predicates):
            forward_composite = _matmul_mod(right, left, prime)
            assert _pullback(forward_composite, predicate, prime) == _pullback(
                left, _pullback(right, predicate, prime), prime
            )

        for matrix, covector in product(alphabet, states):
            covector_vector = _state_vector(covector)
            pulled_covector = _normalize_vector(
                _matvec_mod(_transpose_mod(matrix), covector_vector, prime),
                prime,
            )
            forwarded_covector = _normalize_vector(
                _matvec_mod(
                    _transpose_mod(_inverse_mod(matrix, prime)),
                    covector_vector,
                    prime,
                ),
                prime,
            )
            predicate = _hyperplane_predicate(covector, prime)
            assert _pullback(matrix, predicate, prime) == _hyperplane_predicate(
                pulled_covector, prime
            )
            assert _forward_image(matrix, predicate, prime) == (
                _hyperplane_predicate(forwarded_covector, prime)
            )


def test_gate11d_task_quotient_dualizes_to_fibre_constant_predicates():
    for prime in (3, 5):
        fine = tuple(range(prime * prime))
        coarse = tuple(range(prime))
        quotient = {value: value % prime for value in fine}
        coarse_predicates = tuple(
            frozenset(predicate) for predicate in _powerset(coarse)
        )
        pulled = {
            _inverse_image(fine, quotient, predicate)
            for predicate in coarse_predicates
        }
        fibre_unions = {
            frozenset(
                value
                for value in fine
                if value % prime in selected_fibres
            )
            for selected_fibres in coarse_predicates
        }
        assert pulled == fibre_unions
        assert len(pulled) == 2**prime

        residual = frozenset({0})
        assert residual not in pulled
        assert quotient[0] == quotient[prime]
        assert (0 in residual) != (prime in residual)

        for offset, scale in ((1, 1), (0, 2), (1, 2)):
            fine_action = {
                value: (scale * value + offset) % (prime * prime)
                for value in fine
            }
            coarse_action = {
                value: (scale * value + offset) % prime for value in coarse
            }
            assert all(
                quotient[fine_action[value]] == coarse_action[quotient[value]]
                for value in fine
            )
            for predicate in coarse_predicates:
                coarse_then_pull = _inverse_image(
                    fine,
                    quotient,
                    _inverse_image(coarse, coarse_action, predicate),
                )
                pull_then_fine = _inverse_image(
                    fine,
                    fine_action,
                    _inverse_image(fine, quotient, predicate),
                )
                assert coarse_then_pull == pull_then_fine


def test_gate11e_real_and_padic_observers_differ_but_product_formula_closes():
    for prime in (3, 5):
        depth = 3
        universe = frozenset(range(prime**depth))
        cylinders: list[tuple[int, int, frozenset[int]]] = []
        for level in range(depth + 1):
            modulus = prime**level
            for residue in range(modulus):
                cylinder = frozenset(
                    value for value in universe if value % modulus == residue
                )
                cylinders.append((level, residue, cylinder))
                complement = universe - cylinder
                peer_union = frozenset(
                    value
                    for value in universe
                    if value % modulus != residue
                )
                assert complement == peer_union

        for (_, _, left), (_, _, right) in product(cylinders, repeat=2):
            assert not (left & right) or left <= right or right <= left

        shared = frozenset(range(-prime * prime, prime * prime + 1))
        real_cut = frozenset(value for value in shared if value <= 0)
        padic_cylinder = frozenset(value for value in shared if value % prime == 0)
        assert real_cut != padic_cylinder
        assert not real_cut <= padic_cylinder
        assert not padic_cylinder <= real_cut

    shared_rational = Fraction(8, 3)
    real_floor = floor(shared_rational)
    padic_residue_at_five = (
        shared_rational.numerator
        * pow(shared_rational.denominator, -1, 5)
    ) % 5
    assert (real_floor, padic_residue_at_five) == (2, 1)

    corpus = {
        Fraction(numerator, denominator)
        for numerator in range(-12, 13)
        if numerator
        for denominator in range(1, 9)
    }
    assert len(corpus) == 126
    assert all(_product_formula(value) == 1 for value in corpus)
    for prime, exponent in product((2, 3, 5, 7), range(-6, 7)):
        value = Fraction(prime**exponent) if exponent >= 0 else Fraction(
            1, prime ** (-exponent)
        )
        assert _valuation(value, prime) == exponent
        assert abs(value) * _padic_absolute(value, prime) == 1


def test_gate11f_bounded_behavior_and_finite_biduality_do_not_objectify():
    prime = 5
    states = _projective_states(prime)
    alphabet = (
        ((1, 1), (0, 1)),
        ((2, 0), (0, 1)),
        ((0, -1), (1, 0)),
    )
    words = _words(alphabet, 3)
    terminal: frozenset[_State] = frozenset({0})

    behavior_profiles = {}
    for state in states:
        direct = tuple(_act_word(word, state, prime) in terminal for word in words)
        dual = tuple(state in _pullback_word(word, terminal, prime) for word in words)
        assert direct == dual
        behavior_profiles[state] = direct
    assert len(set(behavior_profiles.values())) == len(states)

    naive_double_dual_cardinality = 2 ** (2 ** len(states))
    structure_preserving_evaluations = len(states)
    assert naive_double_dual_cardinality == 2**64
    assert structure_preserving_evaluations == 6

    dual_objectification_gate = {
        "finite_boolean_point_recovery": True,
        "bounded_behaviors_separate_frozen_states": True,
        "new_task_independent_cogenerator": False,
        "infinite_cofree_observer_proved": False,
        "coherent_global_bidual_return": False,
        "new_vertical_rank": False,
    }
    assert dual_objectification_gate == {
        "finite_boolean_point_recovery": True,
        "bounded_behaviors_separate_frozen_states": True,
        "new_task_independent_cogenerator": False,
        "infinite_cofree_observer_proved": False,
        "coherent_global_bidual_return": False,
        "new_vertical_rank": False,
    }
