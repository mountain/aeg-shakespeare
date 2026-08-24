"""Dimensional resource-bundle calibrations across five process problems.

The AM universal-history recalibration left one central candidate:

    dimensionless canonical shape
      + dimensional resource bundle
      + observer/unit transport
      + history resource cocycle
      + task-relative dual scalarization.

This essay recalculates pendulum, hard-particle first contact, translation
objectification, and Abelian period history under that contract.  A fifth,
independent state-local-clock shortest-arrival problem directly red-teams the
covariant Bellman equation: naive addition of values expressed in different
local units chooses the wrong policy, while parallel transport restores the
physical optimum and gauge covariance.

All structures remain research-local.  Passing this file does not establish a
generic resource bundle, canonical metric, or Bellman API.
"""

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Dimension:
    """Exponents of mass, length, and time for exact dimensional auditing."""

    mass: int = 0
    length: int = 0
    time: int = 0

    def __mul__(self, other):
        return Dimension(
            self.mass + other.mass,
            self.length + other.length,
            self.time + other.time,
        )

    def __truediv__(self, other):
        return Dimension(
            self.mass - other.mass,
            self.length - other.length,
            self.time - other.time,
        )


DIMENSIONLESS = Dimension()
MASS = Dimension(mass=1)
LENGTH = Dimension(length=1)
TIME = Dimension(time=1)
VELOCITY = LENGTH / TIME
ACCELERATION = LENGTH / (TIME * TIME)
ENERGY = MASS * VELOCITY * VELOCITY
ACTION = ENERGY * TIME


def test_pendulum_shape_scale_split_has_exact_dimensional_types():
    # E0=m*g*ell, t0=sqrt(ell/g), A0=E0*t0.  The square-root identity is
    # checked at the level of squared dimensions to keep exponents integral.
    energy_scale = MASS * ACCELERATION * LENGTH
    time_scale_squared = LENGTH / ACCELERATION
    action_scale_squared = (energy_scale * energy_scale) * time_scale_squared

    assert energy_scale == ENERGY
    assert time_scale_squared == TIME * TIME
    assert action_scale_squared == ACTION * ACTION

    # U, Y=dU/dtau, epsilon=H/E0, and omega=dU/Y are dimensionless; physical
    # clock and action are restored only by t0 and A0.
    assert DIMENSIONLESS / DIMENSIONLESS == DIMENSIONLESS
    assert TIME * DIMENSIONLESS == TIME
    assert ACTION * DIMENSIONLESS == ACTION


@dataclass(frozen=True)
class HardParticleResources:
    physical_wait: Fraction
    comparison_queries: int


def test_hard_particle_keeps_physical_wait_and_query_depth_as_distinct_resources():
    first_policy = HardParticleResources(Fraction(1), 2)
    second_policy = HardParticleResources(Fraction(4, 3), 1)

    # Neither dominates: the earlier physical result uses more comparisons.
    assert first_policy.physical_wait < second_policy.physical_wait
    assert first_policy.comparison_queries > second_policy.comparison_queries

    # Task duals, with declared conversion rates, legitimately select
    # different points on the same canonical resource frontier.
    latency_first = first_policy.physical_wait + Fraction(1, 10) * first_policy.comparison_queries
    latency_second = second_policy.physical_wait + Fraction(1, 10) * second_policy.comparison_queries
    query_first = first_policy.physical_wait + first_policy.comparison_queries
    query_second = second_policy.physical_wait + second_policy.comparison_queries

    assert latency_first < latency_second
    assert query_second < query_first


@dataclass(frozen=True)
class MaterializedCost:
    compile_time: Fraction
    run_time: Fraction
    storage_units: int

    def total_time(self, uses: int, storage_time_rate: Fraction) -> Fraction:
        return (
            self.compile_time
            + uses * self.run_time
            + storage_time_rate * self.storage_units
        )


def test_translation_objectification_is_dimensional_amortization_not_free_shortening():
    raw = MaterializedCost(Fraction(0), Fraction(3), 0)
    objectified = MaterializedCost(Fraction(8), Fraction(1), 2)
    storage_time_rate = Fraction(1, 2)

    # One use cannot repay compilation and storage; repeated use can.
    assert raw.total_time(1, storage_time_rate) < objectified.total_time(
        1, storage_time_rate
    )
    assert objectified.total_time(6, storage_time_rate) < raw.total_time(
        6, storage_time_rate
    )

    # The exact break-even threshold is task/workload dependent.
    winners = tuple(
        uses
        for uses in range(1, 9)
        if objectified.total_time(uses, storage_time_rate)
        < raw.total_time(uses, storage_time_rate)
    )
    assert winners == (5, 6, 7, 8)


def _matrix_vector(matrix, vector):
    return tuple(
        sum(row[index] * vector[index] for index in range(len(vector)))
        for row in matrix
    )


def _dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def test_abelian_resource_vector_and_task_dual_restore_basis_covariance():
    # Columns of B' are e1 and e1+e2.  The same displacement d=e2 has
    # standard coordinates c=(0,1) and sheared coordinates c'=(-1,1).
    standard_coordinates = (0, 1)
    sheared_coordinates = (-1, 1)
    basis_change = ((1, 1), (0, 1))
    assert _matrix_vector(basis_change, sheared_coordinates) == standard_coordinates

    # A physical/task covector lambda=(2,3) has coordinate representation
    # B'^T lambda=(2,5) in the sheared basis.  Pairing is invariant even though
    # naive L1 word length is not.
    standard_dual = (2, 3)
    transpose_change = ((1, 0), (1, 1))
    sheared_dual = _matrix_vector(transpose_change, standard_dual)

    assert sheared_dual == (2, 5)
    assert _dot(standard_dual, standard_coordinates) == 3
    assert _dot(sheared_dual, sheared_coordinates) == 3
    assert sum(map(abs, standard_coordinates)) == 1
    assert sum(map(abs, sheared_coordinates)) == 2


@dataclass(frozen=True)
class ClockGauge:
    """Physical time represented by one numeric unit in a local fiber."""

    physical_per_local: Fraction

    def local_value(self, physical_time: Fraction) -> Fraction:
        return physical_time / self.physical_per_local

    def transport_from(self, value, source):
        physical = value * source.physical_per_local
        return physical / self.physical_per_local


def _covariant_shortest_arrival(root_gauge, middle_gauge):
    terminal_value_middle = middle_gauge.local_value(Fraction(2))
    via_middle = (
        root_gauge.local_value(Fraction(1))
        + root_gauge.transport_from(terminal_value_middle, middle_gauge)
    )
    direct = root_gauge.local_value(Fraction(5))
    return via_middle, direct


def test_connection_covariant_bellman_repairs_state_local_unit_mismatch():
    root = ClockGauge(Fraction(2))
    middle = ClockGauge(Fraction(1, 2))

    middle_future = middle.local_value(Fraction(2))  # numeric 4 in middle units
    root_immediate = root.local_value(Fraction(1))   # numeric 1/2 in root units
    root_direct = root.local_value(Fraction(5))      # numeric 5/2 in root units

    # Naive Bellman adds 1/2 root-units to 4 middle-units and incorrectly
    # prefers the physically slower direct route.
    assert root_direct < root_immediate + middle_future

    # Transporting the future value into the root fiber recovers physical
    # times 3 versus 5, represented as 3/2 versus 5/2 root units.
    via_middle, direct = _covariant_shortest_arrival(root, middle)
    assert (via_middle, direct) == (Fraction(3, 2), Fraction(5, 2))
    assert via_middle < direct

    # Independent rescaling of both local gauges changes numeric values but
    # not the selected path or reconstructed physical value.
    rescaled_root = ClockGauge(Fraction(7))
    rescaled_middle = ClockGauge(Fraction(3))
    rescaled_via, rescaled_direct = _covariant_shortest_arrival(
        rescaled_root, rescaled_middle
    )
    assert rescaled_via < rescaled_direct
    assert rescaled_via * rescaled_root.physical_per_local == 3
    assert rescaled_direct * rescaled_root.physical_per_local == 5


def test_discrete_optical_arrival_separates_geometric_length_from_process_time():
    # Set c=1 in declared units.  A short geometric route through a slow medium
    # competes with a longer route through a fast medium.
    direct_length, direct_index = Fraction(2), Fraction(3)
    detour_edges = ((Fraction(2), Fraction(1)), (Fraction(2), Fraction(1)))

    direct_time = direct_length * direct_index
    detour_time = sum(length * index for length, index in detour_edges)
    detour_length = sum(length for length, _ in detour_edges)

    assert direct_length < detour_length
    assert detour_time < direct_time

    # Changing meters to centimeters scales length and c together; arrival
    # times and the Bellman choice stay fixed.
    unit_scale = Fraction(100)
    light_speed_scaled = unit_scale
    assert direct_length * unit_scale * direct_index / light_speed_scaled == direct_time
    assert sum(
        length * unit_scale * index / light_speed_scaled
        for length, index in detour_edges
    ) == detour_time

