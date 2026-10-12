import pytest
import numpy as np

from simple_functions import my_sum, factorial, my_sin


class TestSimpleFunctions:
    """Tests for the functions in functions1.py."""

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4),
    ])
    def test_my_sum(self, iterable, expected):
        """my_sum adds up the items of lists and tuples."""
        assert my_sum(iterable) == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1),
    ])
    def test_factorial(self, number, expected):
        """factorial is right for small numbers, inluding 0!=1"""
        assert factorial(number) == expected

    @pytest.mark.parametrize('x', [
        0,
        np.pi / 6,
        np.pi / 2,
        np.pi,
        2 * np.pi,
    ])
    def test_my_sin(self, x):
        assert my_sin(x) == pytest.approx(
            np.sin(x),
            abs=1e-12
        )
