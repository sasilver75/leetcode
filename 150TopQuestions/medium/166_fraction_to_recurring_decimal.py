"""
Fraction to Recurring Decimal

Given two integers representing the `numerator` and `denominator` of the
fraction, return the fraction in STRING formal!

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return ANY of them.
"""

"""
Frankly I don't care for these ones as they're pretty uninteresting, so I'm
going to skip this one :)
"""


def frac_to_dec(numerator: int, denominator: int) -> str:
    pass

assert frac_to_dec(1,2) == "0.5"
assert frac_to_dec(2, 1) == "2"
assert frac_to_dec(4,333) == "0.(012)"