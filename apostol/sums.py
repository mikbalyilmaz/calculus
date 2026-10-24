"""Sums used with the method of exhaustion (Volume 1, Part I 1).

Author: Muhammed Ikbal Yilmaz
"""

import numpy as np


def power_sum(n, k):
    """1^k + 2^k + ... + n^k as an exact integer (0 when n < 1)."""
    return sum(j ** k for j in range(1, n + 1))


def sum_of_squares(n):
    """1^2 + 2^2 + ... + n^2 from the closed form n(n + 1)(2n + 1)/6."""
    return n * (n + 1) * (2 * n + 1) // 6


def sum_of_cubes(n):
    """1^3 + 2^3 + ... + n^3 from the closed form (n(n + 1)/2)^2."""
    return (n * (n + 1) // 2) ** 2


def rectangle_sums(f, b, n):
    """Inner and outer rectangle sums of an increasing function f on [0, b] with n equal subintervals.

    The inner sum uses the value at the left end of each subinterval, the outer sum the value at the right end, so
    that inner <= area <= outer. Returns (inner, outer).
    """
    x = np.linspace(0.0, b, n + 1)
    width = b / n
    y = f(x)
    return width * float(np.sum(y[:-1])), width * float(np.sum(y[1:]))


def inscribed_semicircle_area(n, radius=1.0):
    """Area under the polygon inscribed in the upper half of a circle, with n equal steps along the diameter.

    The polygon joins the points (x_j, sqrt(r^2 - x_j^2)), x_j = -r + 2rj/n; its area is the sum of n trapezoids.
    """
    x = np.linspace(-radius, radius, n + 1)
    y = np.sqrt(np.clip(radius ** 2 - x ** 2, 0.0, None))
    return float(np.sum(np.diff(x) * (y[:-1] + y[1:]) / 2.0))
