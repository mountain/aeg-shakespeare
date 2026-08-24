"""Exact S1b census over the frozen depth-two expression grammar."""

from dataclasses import dataclass
from functools import lru_cache

from phase0_contract import expressions_through_depth_two
from phase1_s1_census import run_census, unrestricted_generator_nullspace


@lru_cache(maxsize=1)
def run_s1b_census():
    return run_census(expressions_through_depth_two())


@dataclass(frozen=True)
class StabilizerRedTeam:
    grammar_false_negatives: tuple
    genuine_asymmetric: tuple


@lru_cache(maxsize=1)
def _cached_stabilizer_classification():
    return classify_unrestricted_linear_stabilizers(run_s1b_census())


def classify_unrestricted_linear_stabilizers(census=None):
    if census is None:
        return _cached_stabilizer_classification()
    false_negatives = []
    genuine = []
    for expression in census.asymmetric_expressions:
        nullspace = unrestricted_generator_nullspace(expression)
        if nullspace:
            false_negatives.append((expression, nullspace))
        else:
            genuine.append(expression)
    return StabilizerRedTeam(tuple(false_negatives), tuple(genuine))
