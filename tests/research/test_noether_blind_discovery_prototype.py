"""Minimal blind Noether discovery from a raw differentiable process density.

The detector is deliberately small: it receives only a callable L(q, v),
probes coordinate-translation generators by automatic differentiation, and
constructs the associated Noether momentum dL/dv.  Expected symmetries and
charges are not annotations on the input model.

This is a T0 falsifiable prototype, not a complete Lie-symmetry solver.
"""

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class Jet:
    value: float
    gradient: tuple[float, ...]

    @classmethod
    def variable(cls, value, dimension, index):
        gradient = [0.0] * dimension
        gradient[index] = 1.0
        return cls(float(value), tuple(gradient))

    @classmethod
    def constant(cls, value, dimension):
        return cls(float(value), (0.0,) * dimension)

    def _coerce(self, other):
        if isinstance(other, Jet):
            return other
        return Jet.constant(other, len(self.gradient))

    def __add__(self, other):
        other = self._coerce(other)
        return Jet(
            self.value + other.value,
            tuple(a + b for a, b in zip(self.gradient, other.gradient)),
        )

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, tuple(-entry for entry in self.gradient))

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        return Jet(
            self.value * other.value,
            tuple(
                self.gradient[i] * other.value
                + self.value * other.gradient[i]
                for i in range(len(self.gradient))
            ),
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self._coerce(other)
        return Jet(
            self.value / other.value,
            tuple(
                (self.gradient[i] * other.value - self.value * other.gradient[i])
                / (other.value * other.value)
                for i in range(len(self.gradient))
            ),
        )

    def __pow__(self, exponent):
        return Jet(
            self.value**exponent,
            tuple(
                exponent * self.value ** (exponent - 1) * entry
                for entry in self.gradient
            ),
        )


def jet_sqrt(value):
    root = sqrt(value.value)
    return Jet(
        root,
        tuple(entry / (2 * root) for entry in value.gradient),
    )


def _evaluate_with_jet(lagrangian, position, velocity):
    dimension = 2 * len(position)
    q = tuple(
        Jet.variable(value, dimension, index)
        for index, value in enumerate(position)
    )
    v = tuple(
        Jet.variable(value, dimension, len(position) + index)
        for index, value in enumerate(velocity)
    )
    return lagrangian(q, v)


def discover_translation_symmetries(lagrangian, probes, tolerance=1e-12):
    """Return coordinate axes whose infinitesimal translation leaves L fixed."""

    coordinate_count = len(probes[0][0])
    residuals = [0.0] * coordinate_count
    for position, velocity in probes:
        evaluated = _evaluate_with_jet(lagrangian, position, velocity)
        for axis in range(coordinate_count):
            residuals[axis] = max(residuals[axis], abs(evaluated.gradient[axis]))
    return tuple(axis for axis, residual in enumerate(residuals) if residual <= tolerance)


def noether_translation_momenta(lagrangian, position, velocity):
    evaluated = _evaluate_with_jet(lagrangian, position, velocity)
    offset = len(position)
    return tuple(evaluated.gradient[offset:]), evaluated.value


def anisotropic_graded_optical_density(position, velocity):
    """Raw Finsler density; no symmetry or momentum metadata is supplied."""

    _, y = position
    vx, vy = velocity
    refractive_index = 1 + y * y
    return refractive_index * jet_sqrt(4 * vx * vx + vy * vy)


def symmetry_broken_density(position, velocity):
    x, _ = position
    return anisotropic_graded_optical_density(position, velocity) + x * x


def test_blind_detector_finds_only_the_true_optical_translation_symmetry():
    probes = (
        ((-2, 1), (3, 4)),
        ((1, 2), (5, 12)),
        ((3, -1), (8, 15)),
    )

    # x is absent from the raw density, while the graded index depends on y.
    # The expected axis is asserted only after discovery.
    discovered = discover_translation_symmetries(
        anisotropic_graded_optical_density, probes
    )
    assert discovered == (0,)

    # Adding an x-dependent term destroys the candidate; this guards against a
    # detector that merely assumes the first coordinate is cyclic.
    assert discover_translation_symmetries(symmetry_broken_density, probes) == ()


def test_discovered_generator_constructs_noether_momentum_without_formula_hint():
    position = (7, 0)
    velocity = (3, 8)
    momenta, optical_density = noether_translation_momenta(
        anisotropic_graded_optical_density, position, velocity
    )

    # AD constructs dF/dv.  The x component 4*3/10=6/5 is the charge paired
    # with the discovered translation generator; it was not input as metadata.
    assert optical_density == 10
    assert abs(momenta[0] - 6 / 5) < 1e-12
    assert abs(momenta[1] - 4 / 5) < 1e-12

    # One-homogeneity, also checked from the raw density, implies the optical
    # canonical Hamiltonian p.v-F vanishes: parameter choice is gauge-like.
    canonical_hamiltonian = sum(
        momentum * speed for momentum, speed in zip(momenta, velocity)
    ) - optical_density
    assert abs(canonical_hamiltonian) < 1e-12

