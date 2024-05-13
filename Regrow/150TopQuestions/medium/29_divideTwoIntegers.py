"""
Divide two Integers

Given two integers `dividend` and `divisor`, divide two integers
WITHOUT using multiplication, division, or the modulus operator.

The integer division should truncate toward zero, which means LOSING
its fractional part. 8.32 -> 8 and -2.34 -> -2

Return the QUOTIENT after dividing `dividend` by `divisor`
i.e.    Dividend / Divisor = Quotient

NOTE: Assume we're dealing in an environment that could only deal with integers
in the 32-bit signed integer range of [-2**31, 2*31 - 1].
If the quotient is outside those ranges, return the bound.
"""
from typing import Callable


def divide(dividend: int, divisor: int) -> int:
    # Assuming both positive dividend/divisor
    negative_modifier = 1 if dividend*divisor > 0 else -1
    dividend, divisor = abs(dividend), abs(divisor)

    count = 0
    while dividend - divisor >= 0:
        dividend -= divisor
        count += 1

    return count * negative_modifier




# -- Test Zone --
def test(fn: Callable):
    assert fn(10, 3) == 3
    assert fn(7, -3) == -2

test(divide)