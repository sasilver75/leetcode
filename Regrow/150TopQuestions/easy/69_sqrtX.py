"""
Sqrt(x)

Given a non-negative integer x, return the square root of x rounded
down to the nearest integer. The return integer should be non-negative as
well.

You must not use any built-in exponent function or operator
For example, don't use pow(x, .5) in c++ or x ** .5 in python
"""


def sqrt(n: int) -> int:
    if n == 0:
        return 0
    for i in range(0, n + 1):
        sqr = i ** 2
        if sqr - n == 0:
            return i
        if sqr > n:
            return i - 1


# Case 1
assert sqrt(4) == 2

# Case 2
assert sqrt(8) == 2  # sqrt(8) is 2.82842 ... round down to nearest integer

# Additional Tests
cases = [(0, 0), (1, 1), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 3), (10, 3), (11, 3)]
for inp, ans in cases:
    assert sqrt(inp) == ans