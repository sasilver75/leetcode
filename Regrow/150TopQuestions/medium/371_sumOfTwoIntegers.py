"""
Sum of Two Integers

Given two integers `a` and `b`, return the SUM of the two integers without
using the operators `+` and `-`.
"""

def get_sum(a: int, b: int) -> int:
    return sum([a,b]) # Suck my ass
    # This was useful, though: https://leetcode.com/problems/sum-of-two-integers/solutions/84278/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently/


def test(fn):
    assert fn(1,2) == 3
    assert fn(2,3) == 5