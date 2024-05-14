"""
Given a non-negative integer x, return the square root of x rounded down
 to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 


"""

import itertools


def sqrt_naive(x: int) -> int:
    best = -1
    for n in range(0, x):
        if n**2 <= x:
            best = n
        else:
            break
    return best

def sqrt(x: int) -> int:
    """
    Well what's the definition of a square root? It's a number that, when squared, equals
    the number that we're looking for.
    We want the one that's "rounded down"
    So what we reall want is:
    "Find the largest number z that, when squared, is <= x"

    There's a range of numbers that we could test, in the worst case 0..x
    I think we could do this linearly, or we could do it binary search style
    """
    l, r = 0, x

    while l <= r:
        mid = l + (r - l) // 2

        # test
        sq = mid**2
        if sq == x:
            return mid
        elif sq > x:
            r = mid -1
        else:
            l = mid + 1
    
    return r





cases = (
    (4, 2),
    (8,2),
    (10, 3),
    (11, 3),
    (12,3),
    (14,3),
    (16,4),
    (17,4)
)

for fn, (inp, ans) in itertools.product([sqrt], cases):
    assert fn(inp) == ans, f"{fn.__name__}, {inp}"