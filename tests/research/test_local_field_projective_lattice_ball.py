"""Finite lattice-class oracle for the Bruhat--Tits ball.

The preceding local-field essay saw only the affine residue observations
x mod p**n.  This file performs the next exact calibration: primitive
covectors modulo p**n, quotiented by units, label normalized index-p**n
lattices around the standard lattice.  Reduction of those labels builds the
complete finite ball.

The implementation is deliberately research-local.  It is a finite oracle,
not a p-adic number package and not a proposed Bruhat--Tits framework API.
Classical lineage is recorded under [Serre-Trees-1980] and
[Ludwig-Merten-2026] in docs/REFERENCES.md.
"""

from __future__ import annotations

from dataclasses import dataclass
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
