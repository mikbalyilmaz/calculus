"""Checks of the helper code against independent computations: brute-force sums, exact rational arithmetic,
closed forms and exhaustive enumeration of finite sets. Run from the repository root with `pytest`."""

import sys
from fractions import Fraction
from itertools import product
from math import comb, pi
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apostol.sets import cover_relations, inclusions, is_proper_subset, power_set, roster  # noqa: E402
from apostol.sums import (inscribed_semicircle_area, power_sum, rectangle_sums, sum_of_cubes,  # noqa: E402
                          sum_of_squares)


def test_power_sums_against_loops():
    for n in range(0, 60):
        assert power_sum(n, 2) == sum(j * j for j in range(1, n + 1)) == sum_of_squares(n)
        assert power_sum(n, 3) == sum(j ** 3 for j in range(1, n + 1)) == sum_of_cubes(n)


def test_identities_1_3_and_1_4():
    for n in range(1, 2001):
        assert Fraction(sum_of_squares(n)) == Fraction(n**3, 3) + Fraction(n**2, 2) + Fraction(n, 6)
        assert Fraction(sum_of_squares(n - 1)) == Fraction(n**3, 3) - Fraction(n**2, 2) + Fraction(n, 6)


def test_inequality_of_exercise_3():
    for k in range(1, 9):
        for n in range(1, 301):
            assert (k + 1) * power_sum(n - 1, k) < n ** (k + 1) < (k + 1) * power_sum(n, k)


def test_rectangle_sums_of_x_squared():
    for n in (1, 2, 6, 50):
        for b in (0.5, 1.0, 2.0):
            inner, outer = rectangle_sums(lambda x: x**2, b, n)
            assert abs(inner - b**3 / n**3 * sum_of_squares(n - 1)) < 1e-12
            assert abs(outer - b**3 / n**3 * sum_of_squares(n)) < 1e-12
            assert inner < b**3 / 3 < outer
            assert abs((outer - inner) - b**3 / n) < 1e-12


def test_inscribed_semicircle_area():
    assert abs(inscribed_semicircle_area(2) - 1.0) < 1e-15        # the triangle with vertices (-1,0), (0,1), (1,0)
    areas = [inscribed_semicircle_area(n) for n in (2, 4, 8, 16, 1000)]
    assert all(a < b for a, b in zip(areas, areas[1:]))
    assert 0 < pi / 2 - areas[-1] < 1e-4


def test_power_set_and_relations():
    subsets = power_set({1, 2, 3, 4})
    assert len(subsets) == 16 == len(set(subsets))
    assert [sum(len(s) == k for s in subsets) for k in range(5)] == [comb(4, k) for k in range(5)]
    sets = {"A": frozenset({-1, 1}), "B": frozenset({1}), "C": frozenset({1}), "D": frozenset({2}),
            "E": frozenset({-17, 1}), "F": frozenset({-17, 1, -8 - 47 ** 0.5, -8 + 47 ** 0.5})}
    assert set(inclusions(sets)) == {("B", "A"), ("C", "A"), ("B", "C"), ("C", "B"), ("B", "E"), ("C", "E"),
                                     ("B", "F"), ("C", "F"), ("E", "F")}
    assert set(cover_relations(sets)) == {("B", "A"), ("C", "A"), ("B", "E"), ("C", "E"), ("E", "F")}
    assert roster({1, -1}) == "{-1, 1}" and roster(set()) == "∅"


def test_exercise_20_by_enumeration():
    triples = list(product(power_set({1, 2, 3}), repeat=3))
    assert all(a - (b | c) == (a - b) - c for a, b, c in triples)
    assert all((a - (b - c) == (a - b) | c) == (c <= a) for a, b, c in triples)
    assert not is_proper_subset(frozenset({1}), frozenset({1}))
