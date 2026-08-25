"""Finite lattice-class oracle for the Bruhat--Tits ball.

The preceding local-field essay saw only the affine residue observations
x mod p**n.  This file performs the next exact calibration: primitive
covectors modulo p**n, quotiented by units, label normalized index-p**n
lattices around the standard lattice.  Reduction of those labels builds the
complete finite ball.

The implementation is deliberately research-local.  It is a finite oracle,
not a p-adic number package and not a proposed Bruhat--Tits framework API.
Classical lineage is recorded under [Serre-Trees-1980],
[Ludwig-Merten-2026], and [Huffman-1952] in docs/REFERENCES.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from heapq import heapify, heappop, heappush
from itertools import count
from math import isqrt

import pytest


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, isqrt(value) + 1))


@dataclass(frozen=True, order=True)
class _NormalizedLatticeClass:
    """One standard-root lattice class at a declared finite depth.

    At depth n > 0 the class is represented by a primitive covector
    [a:b] modulo p**n.  Unit multiples have the same kernel lattice

        L_[a:b] = {(x, y): a*x + b*y == 0 mod p**n}.

    Two disjoint charts give a unique finite representative:

        affine:   [r:1],      r mod p**n;
        infinity: [1:p*t],    t mod p**(n-1).
    """

    prime: int
    depth: int
    chart: str
    coordinate: int

    def __post_init__(self) -> None:
        if not _is_prime(self.prime):
            raise ValueError("prime must be prime")
        if self.depth < 0:
            raise ValueError("depth must be nonnegative")
        if self.depth == 0:
            if (self.chart, self.coordinate) != ("root", 0):
                raise ValueError("depth zero has only the standard root")
            return
        if self.chart == "affine":
            bound = self.prime**self.depth
        elif self.chart == "infinity":
            bound = self.prime ** (self.depth - 1)
        else:
            raise ValueError("positive-depth class needs a projective chart")
        if not 0 <= self.coordinate < bound:
            raise ValueError("coordinate is outside its canonical residue range")

    @classmethod
    def root(cls, prime: int) -> "_NormalizedLatticeClass":
        return cls(prime, 0, "root", 0)

    @classmethod
    def from_primitive(
        cls,
        prime: int,
        depth: int,
        first: int,
        second: int,
    ) -> "_NormalizedLatticeClass":
        """Quotient one primitive pair by all units modulo p**depth."""

        if depth <= 0:
            raise ValueError("a projective residue needs positive depth")
        modulus = prime**depth
        first %= modulus
        second %= modulus
        if first % prime == 0 and second % prime == 0:
            raise ValueError("the covector is not primitive")

        if second % prime:
            inverse = pow(second, -1, modulus)
            return cls(prime, depth, "affine", first * inverse % modulus)

        inverse = pow(first, -1, modulus)
        normalized_second = second * inverse % modulus
        assert normalized_second % prime == 0
        return cls(
            prime,
            depth,
            "infinity",
            normalized_second // prime,
        )

    @property
    def modulus(self) -> int:
        return self.prime**self.depth

    @property
    def primitive_covector(self) -> tuple[int, int]:
        if self.depth == 0:
            raise ValueError("the root has no projective covector")
        if self.chart == "affine":
            return self.coordinate, 1
        return 1, self.prime * self.coordinate

    @property
    def parent(self) -> "_NormalizedLatticeClass":
        if self.depth == 0:
            raise ValueError("the root has no parent")
        if self.depth == 1:
            return self.root(self.prime)
        return self.from_primitive(
            self.prime,
            self.depth - 1,
            *self.primitive_covector,
        )

    @property
    def children(self) -> tuple["_NormalizedLatticeClass", ...]:
        """Return the exact one-step projective-cylinder refinements."""

        if self.depth == 0:
            return _sphere(self.prime, 1)
        if self.chart == "affine":
            stride = self.prime**self.depth
        else:
            stride = self.prime ** (self.depth - 1)
        return tuple(
            type(self)(
                self.prime,
                self.depth + 1,
                self.chart,
                self.coordinate + digit * stride,
            )
            for digit in range(self.prime)
        )

    @property
    def lattice_basis(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """Give an integral basis for the normalized p-adic lattice."""

        if self.depth == 0:
            return (1, 0), (0, 1)
        if self.chart == "affine":
            return (1, -self.coordinate), (0, self.modulus)
        shift = self.prime * self.coordinate
        return (self.modulus, 0), (-shift, 1)

    def contains(self, vector: tuple[int, int]) -> bool:
        if self.depth == 0:
            return True
        first, second = self.primitive_covector
        x, y = vector
        return (first * x + second * y) % self.modulus == 0

    def basis_coordinates(self, vector: tuple[int, int]) -> tuple[int, int]:
        """Recover exact integral coordinates or reject a nonmember."""

        if not self.contains(vector):
            raise ValueError("vector is not in the normalized lattice")
        x, y = vector
        if self.depth == 0:
            return x, y
        if self.chart == "affine":
            return x, (y + self.coordinate * x) // self.modulus
        shift = self.prime * self.coordinate
        return (x + shift * y) // self.modulus, y

    def act_on_projective_label(
        self,
        matrix: tuple[tuple[int, int], tuple[int, int]],
    ) -> "_NormalizedLatticeClass":
        """Act on the projective label by a matrix invertible modulo p.

        With the kernel convention this is the contragredient lattice action;
        the explicit name prevents that convention from being hidden.
        """

        if self.depth == 0:
            return self
        (a, b), (c, d) = matrix
        if (a * d - b * c) % self.prime == 0:
            raise ValueError("matrix must be invertible modulo the prime")
        first, second = self.primitive_covector
        return self.from_primitive(
            self.prime,
            self.depth,
            a * first + b * second,
            c * first + d * second,
        )


def _sphere(prime: int, depth: int) -> tuple[_NormalizedLatticeClass, ...]:
    if depth <= 0:
        raise ValueError("sphere depth must be positive")
    return tuple(
        [
            _NormalizedLatticeClass(prime, depth, "affine", residue)
            for residue in range(prime**depth)
        ]
        + [
            _NormalizedLatticeClass(prime, depth, "infinity", residue)
            for residue in range(prime ** (depth - 1))
        ]
    )


def _ball(prime: int, radius: int) -> set[_NormalizedLatticeClass]:
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    vertices = {_NormalizedLatticeClass.root(prime)}
    for depth in range(1, radius + 1):
        vertices.update(_sphere(prime, depth))
    return vertices


def _rebuild(
    basis: tuple[tuple[int, int], tuple[int, int]],
    coordinates: tuple[int, int],
) -> tuple[int, int]:
    (u1, u2), (v1, v2) = basis
    first, second = coordinates
    return first * u1 + second * v1, first * u2 + second * v2


def _minimum_exact_bits(number_of_states: int) -> int:
    """Return ceil(log2(number_of_states)) without floating point."""

    if number_of_states <= 0:
        raise ValueError("the task must have at least one state")
    return (number_of_states - 1).bit_length()


def _huffman_code_lengths(weights: tuple[Fraction, ...]) -> tuple[int, ...]:
    """Compute exact binary Huffman lengths for one declared finite source.

    The heap stores leaf memberships so the result is an actual coding-tree
    calculation.  No Bruhat--Tits edge is silently reused as a binary edge.
    """

    if not weights:
        raise ValueError("a source alphabet must be nonempty")
    if any(weight <= 0 for weight in weights):
        raise ValueError("source weights must be positive")
    if sum(weights, start=Fraction(0)) != 1:
        raise ValueError("source weights must sum to one")

    serial = count()
    heap = [
        (Fraction(weight), next(serial), (index,))
        for index, weight in enumerate(weights)
    ]
    heapify(heap)
    lengths = [0] * len(weights)
    while len(heap) > 1:
        left_weight, _, left_leaves = heappop(heap)
        right_weight, _, right_leaves = heappop(heap)
        merged_leaves = left_leaves + right_leaves
        for index in merged_leaves:
            lengths[index] += 1
        heappush(
            heap,
            (
                left_weight + right_weight,
                next(serial),
                merged_leaves,
            ),
        )
    return tuple(lengths)


def _canonical_prefix_code(lengths: tuple[int, ...]) -> tuple[str, ...]:
    """Materialize a deterministic prefix decoder from certified lengths."""

    if not lengths:
        raise ValueError("a code needs at least one symbol")
    if len(lengths) == 1:
        if lengths != (0,):
            raise ValueError("a singleton source has zero-length code")
        return ("",)
    if any(length <= 0 for length in lengths):
        raise ValueError("a nonsingleton prefix code needs positive lengths")

    ordered = sorted((length, index) for index, length in enumerate(lengths))
    codewords = [""] * len(lengths)
    code = 0
    previous_length = 0
    for length, index in ordered:
        code <<= length - previous_length
        if code >= 1 << length:
            raise ValueError("the lengths violate the binary Kraft bound")
        codewords[index] = format(code, f"0{length}b")
        code += 1
        previous_length = length

    if any(
        right.startswith(left)
        for left_index, left in enumerate(codewords)
        for right_index, right in enumerate(codewords)
        if left_index != right_index
    ):
        raise AssertionError("canonical code construction must be prefix-free")
    return tuple(codewords)


def _decode_prefix_stream(stream: str, codewords: tuple[str, ...]) -> tuple[int, ...]:
    """Decode one binary stream or reject an incomplete/unknown suffix."""

    if any(bit not in "01" for bit in stream):
        raise ValueError("a binary code stream contains a non-bit")
    decoder = {codeword: index for index, codeword in enumerate(codewords)}
    if len(decoder) != len(codewords) or "" in decoder:
        raise ValueError("stream decoding needs distinct nonempty codewords")

    result = []
    start = 0
    for stop in range(1, len(stream) + 1):
        word = stream[start:stop]
        if word in decoder:
            result.append(decoder[word])
            start = stop
    if start != len(stream):
        raise ValueError("the stream has an incomplete or unknown suffix")
    return tuple(result)


def test_unit_projective_quotient_is_exactly_the_finite_kernel_quotient():
    """Raw primitive pairs collapse iff their normalized lattices agree."""

    prime = 3
    depth = 2
    modulus = prime**depth
    canonical_to_kernel = {}
    kernel_to_canonical = {}

    for first in range(modulus):
        for second in range(modulus):
            if first % prime == 0 and second % prime == 0:
                continue
            vertex = _NormalizedLatticeClass.from_primitive(
                prime,
                depth,
                first,
                second,
            )
            kernel = tuple(
                (first * x + second * y) % modulus == 0
                for x in range(modulus)
                for y in range(modulus)
            )
            assert canonical_to_kernel.setdefault(vertex, kernel) == kernel
            assert kernel_to_canonical.setdefault(kernel, vertex) == vertex

    expected_classes = modulus + modulus // prime
    units = modulus - modulus // prime
    primitive_pairs = modulus**2 - (modulus // prime) ** 2
    assert len(canonical_to_kernel) == len(kernel_to_canonical) == expected_classes
    assert primitive_pairs == expected_classes * units


def test_normal_forms_are_index_pn_lattices_with_exact_coordinates():
    for prime in (2, 3):
        for depth in range(1, 4):
            modulus = prime**depth
            for vertex in _sphere(prime, depth):
                basis = vertex.lattice_basis
                determinant = basis[0][0] * basis[1][1] - basis[0][1] * basis[1][0]
                assert abs(determinant) == modulus
                assert all(vertex.contains(vector) for vector in basis)

                for x in range(modulus):
                    for y in range(modulus):
                        vector = (x, y)
                        if vertex.contains(vector):
                            coordinates = vertex.basis_coordinates(vector)
                            assert _rebuild(basis, coordinates) == vector
                        else:
                            with pytest.raises(ValueError):
                                vertex.basis_coordinates(vector)


def test_reduction_builds_the_complete_rooted_bruhat_tits_ball():
    for prime in (2, 3, 5):
        radius = 4
        vertices = _ball(prime, radius)
        root = _NormalizedLatticeClass.root(prime)
        edges = {(vertex.parent, vertex) for vertex in vertices if vertex != root}

        expected_vertices = 1 + (prime + 1) * (prime**radius - 1) // (prime - 1)
        assert len(vertices) == expected_vertices
        assert len(edges) == len(vertices) - 1

        degree = {vertex: 0 for vertex in vertices}
        for parent, child in edges:
            assert parent.depth + 1 == child.depth
            degree[parent] += 1
            degree[child] += 1

        assert degree[root] == prime + 1
        for vertex in vertices:
            if 0 < vertex.depth < radius:
                assert degree[vertex] == prime + 1
            elif vertex.depth == radius:
                assert degree[vertex] == 1

            cursor = vertex
            for _ in range(vertex.depth):
                cursor = cursor.parent
            assert cursor == root


def test_projective_cylinders_form_exact_refining_frontiers():
    """Each positive-depth cylinder has p children; the root has p + 1."""

    for prime in (2, 3, 5):
        root = _NormalizedLatticeClass.root(prime)
        assert root.children == _sphere(prime, 1)
        assert len(root.children) == prime + 1

        for depth in range(1, 4):
            frontier = _sphere(prime, depth)
            expected_size = (prime + 1) * prime ** (depth - 1)
            assert len(frontier) == expected_size
            assert all(len(vertex.children) == prime for vertex in frontier)
            assert all(
                child.parent == vertex
                for vertex in frontier
                for child in vertex.children
            )
            assert {
                child
                for vertex in frontier
                for child in vertex.children
            } == set(_sphere(prime, depth + 1))


def test_discrete_shell_increment_and_task_memory_are_exact_but_distinct():
    """Finite coarea-like shell growth does not identify depth with memory."""

    for prime in (2, 3, 5, 7):
        for depth in range(1, 5):
            sphere_size = (prime + 1) * prime ** (depth - 1)
            ball_size = 1 + (prime + 1) * (prime**depth - 1) // (prime - 1)
            previous_ball_size = (
                1
                if depth == 1
                else 1
                + (prime + 1) * (prime ** (depth - 1) - 1) // (prime - 1)
            )

            assert len(_sphere(prime, depth)) == sphere_size
            assert len(_ball(prime, depth)) == ball_size
            assert ball_size - previous_ball_size == sphere_size
            assert _minimum_exact_bits(sphere_size) == (
                sphere_size - 1
            ).bit_length()

    assert tuple(
        _minimum_exact_bits(len(_sphere(3, depth)))
        for depth in range(1, 4)
    ) == (2, 4, 6)


def test_root_symmetric_cylinder_source_is_projectively_consistent():
    """Uniform finite frontiers push exactly to their parent frontier."""

    for prime in (2, 3, 5):
        root = _NormalizedLatticeClass.root(prime)
        for depth in range(1, 4):
            frontier = _sphere(prime, depth)
            mass = Fraction(1, len(frontier))
            assert sum((mass for _ in frontier), start=Fraction(0)) == 1

            if depth == 1:
                pushed_mass = {root: sum(
                    (mass for _ in frontier),
                    start=Fraction(0),
                )}
                assert pushed_mass == {root: Fraction(1)}
                continue

            parent_frontier = _sphere(prime, depth - 1)
            pushed_mass = {
                parent: sum(
                    (mass for child in frontier if child.parent == parent),
                    start=Fraction(0),
                )
                for parent in parent_frontier
            }
            assert set(pushed_mass.values()) == {
                Fraction(1, len(parent_frontier))
            }


def test_huffman_tree_depends_on_source_law_not_projective_geometry():
    """One cylinder frontier supports different exact optimal binary trees."""

    frontier = _sphere(3, 2)
    assert len(frontier) == 12

    uniform_weights = (Fraction(1, 12),) * 12
    skewed_weights = (Fraction(1, 2),) + (Fraction(1, 22),) * 11
    uniform_lengths = _huffman_code_lengths(uniform_weights)
    skewed_lengths = _huffman_code_lengths(skewed_weights)

    assert sorted(uniform_lengths) == [3] * 4 + [4] * 8
    assert sum(
        weight * length
        for weight, length in zip(uniform_weights, uniform_lengths)
    ) == Fraction(11, 3)
    assert sum(
        weight * length
        for weight, length in zip(skewed_weights, skewed_lengths)
    ) == Fraction(61, 22)
    assert skewed_lengths[0] == 1
    assert uniform_lengths != skewed_lengths

    for lengths in (uniform_lengths, skewed_lengths):
        codewords = _canonical_prefix_code(lengths)
        message = tuple(range(len(frontier))) + (0, 5, 11)
        stream = "".join(codewords[index] for index in message)
        assert _decode_prefix_stream(stream, codewords) == message

    with pytest.raises(ValueError, match="nonempty"):
        _huffman_code_lengths(())
    with pytest.raises(ValueError, match="positive"):
        _huffman_code_lengths((Fraction(1), Fraction(0)))
    with pytest.raises(ValueError, match="sum to one"):
        _huffman_code_lengths((Fraction(1), Fraction(1)))
    with pytest.raises(ValueError, match="non-bit"):
        _decode_prefix_stream("102", ("0", "10", "11"))
    with pytest.raises(ValueError, match="suffix"):
        _decode_prefix_stream("1", ("0", "10", "11"))


def test_phase0_residues_are_exactly_the_affine_patch_not_the_whole_sphere():
    prime = 3
    for depth in range(1, 5):
        modulus = prime**depth
        affine_patch = {
            _NormalizedLatticeClass.from_primitive(prime, depth, residue, 1)
            for residue in range(modulus)
        }
        full_sphere = set(_sphere(prime, depth))

        assert len(affine_patch) == modulus
        assert len(full_sphere - affine_patch) == prime ** (depth - 1)
        assert all(vertex.chart == "infinity" for vertex in full_sphere - affine_patch)

        for residue in range(modulus):
            vertex = _NormalizedLatticeClass.from_primitive(
                prime,
                depth,
                residue,
                1,
            )
            for observed in range(2 * modulus):
                assert vertex.contains((1, -observed)) == (
                    observed % modulus == residue
                )
            if depth > 1:
                assert vertex.parent == _NormalizedLatticeClass.from_primitive(
                    prime,
                    depth - 1,
                    residue % (modulus // prime),
                    1,
                )

    root = _NormalizedLatticeClass.root(prime)
    affine_first_layer = {
        _NormalizedLatticeClass(prime, 1, "affine", residue)
        for residue in range(prime)
    }
    assert len(affine_first_layer) == prime
    assert len({vertex for vertex in _sphere(prime, 1) if vertex.parent == root}) == (
        prime + 1
    )


def test_right_inversion_forces_the_missing_projective_chart():
    prime = 5
    depth = 3
    inversion = ((0, -1), (1, 0))
    translation = ((1, 7), (0, 1))
    unit_dilation = ((2, 0), (0, 1))
    sphere = set(_sphere(prime, depth))
    affine = {vertex for vertex in sphere if vertex.chart == "affine"}
    infinity = sphere - affine

    inverted = {
        vertex.act_on_projective_label(inversion)
        for vertex in sphere
    }
    assert inverted == sphere
    assert all(
        vertex.act_on_projective_label(inversion).act_on_projective_label(inversion)
        == vertex
        for vertex in sphere
    )

    affine_multiples_of_p = {
        vertex
        for vertex in affine
        if vertex.coordinate % prime == 0
    }
    assert {
        vertex.act_on_projective_label(inversion)
        for vertex in infinity
    } == affine_multiples_of_p
    assert {
        vertex.act_on_projective_label(inversion)
        for vertex in affine_multiples_of_p
    } == infinity

    assert all(
        vertex.act_on_projective_label(translation).chart == "affine"
        for vertex in affine
    )
    assert all(
        vertex.act_on_projective_label(unit_dilation).chart == "affine"
        for vertex in affine
    )


def test_oracle_rejects_undefined_projective_and_lattice_operations():
    with pytest.raises(ValueError, match="not primitive"):
        _NormalizedLatticeClass.from_primitive(3, 2, 3, 6)
    with pytest.raises(ValueError, match="positive depth"):
        _NormalizedLatticeClass.from_primitive(3, 0, 1, 0)
    with pytest.raises(ValueError, match="canonical residue"):
        _NormalizedLatticeClass(3, 2, "affine", 9)

    vertex = _NormalizedLatticeClass.from_primitive(3, 2, 1, 1)
    with pytest.raises(ValueError, match="invertible"):
        vertex.act_on_projective_label(((3, 0), (0, 1)))
    with pytest.raises(ValueError, match="not in"):
        vertex.basis_coordinates((1, 0))
