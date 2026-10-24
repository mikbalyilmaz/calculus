"""Finite sets: subsets, inclusion relations and power sets (Volume 1, Part I 2).

Sets whose elements are sets are written with frozenset, because a Python set can only contain hashable objects.

Author: Muhammed Ikbal Yilmaz
"""

from itertools import combinations


def power_set(elements):
    """All subsets of a finite set, ordered by size and then in the order of `elements`."""
    items = list(elements)
    return [frozenset(c) for k in range(len(items) + 1) for c in combinations(items, k)]


def is_proper_subset(a, b):
    """True when every element of a is in b and a != b."""
    return a <= b and a != b


def inclusions(named_sets):
    """All pairs (X, Y) of names with X a subset of Y, X != Y as names, in the order of `named_sets`."""
    names = list(named_sets)
    return [(x, y) for x in names for y in names if x != y and named_sets[x] <= named_sets[y]]


def cover_relations(named_sets):
    """Pairs (X, Y) with X a proper subset of Y and no Z strictly between them (the edges of a Hasse diagram)."""
    names = list(named_sets)
    s = named_sets
    out = []
    for x in names:
        for y in names:
            if is_proper_subset(s[x], s[y]) and not any(
                    is_proper_subset(s[x], s[z]) and is_proper_subset(s[z], s[y]) for z in names):
                out.append((x, y))
    return out


def roster(values, fmt=str):
    """A set written in roster notation, with its elements in increasing order: {-1, 1}."""
    return "{" + ", ".join(fmt(v) for v in sorted(values)) + "}" if values else "∅"
