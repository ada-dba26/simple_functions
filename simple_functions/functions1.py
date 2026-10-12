from functools import cache

__all__ = ['my_sum', 'factorial', 'my_sin']


def my_sum(iterable):
    """Return the sum of the items in iterable."""
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    """Return n! for a non-negative integer n."""
    return n * factorial(n-1) if n else 1


def my_sin(x, terms=20):
    result = 0

    for n in range(terms):
        term = (-1)**n * x**(2*n + 1) / factorial(2*n + 1)
        result += term

    return result
