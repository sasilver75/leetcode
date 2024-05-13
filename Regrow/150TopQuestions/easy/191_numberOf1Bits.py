"""
Number of 1 Bits


Write a function that takes an unsigned integer and returns
the number of '1' bits it has (also known as its Hamming Weight)
"""


def hamming_weight(s: str) -> int:
    if not len(s) == 32:
        raise ValueError("Input s must be a 32 bit unsigned integer")
    count = 0
    for char in s:
        if char == "1":
            count += 1
    return count


assert hamming_weight("00000000000000000000000000001011") == 3
assert hamming_weight("00000000000000000000000010000000") == 1
assert hamming_weight("11111111111111111111111111111101") == 31
