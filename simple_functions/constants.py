from functools import cache
from numpy import sqrt
from simple_functions.functions1 import factorial

__all__ = ['pi']


def pi(terms=1):
    """Approximate pi using Ramanujan's series."""
    return 1./(2.*sqrt(2.)/9801.*rsum(terms))


@cache
def rsum(n):
    """Sum terms from k=0 to k=n."""
    t = factorial(4*n)*(1103+26390*n)/(factorial(n)**4*396**(4*n))
    return t + rsum(n-1) if n else t
