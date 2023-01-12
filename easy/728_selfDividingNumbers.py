"""
A self-dividing number is a number that's divisible by every digit it contains.

For example: 128 is a self dividing number because
128 % 1 == 0, 127 % 2 == 0, and 128 % 8 == 0

A self-dividing number is NOT ALLOWED to contain the digit 0
    -> Does this mean it won't be present? Or that we should quick-fail these?

Given two integers LEFT and RIGHT, return a list of all the self-dividing numbers
in the range [left, right] (inclusive on both ends).
"""

def self_dividing_numbers(l: int, r: int) -> list[int]:
    acc = []
    for n in range(l, r+1):
        if all(
                int(digit_char) != 0 and n % int(digit_char) == 0
                for digit_char in str(n)
        ):
            acc.append(n)
    return acc

assert self_dividing_numbers(1, 22) == [1,2,3,4,5,6,7,8,9,11,12,15,22]
assert self_dividing_numbers(47, 85) == [48,55,66,77]