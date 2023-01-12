"""
Reverse bits of a given 32 bits unsigned binary integer

Ex n=00000010100101000001111010011100 yields 964176192,
whose binary representation is 00111001011110000010100101000000, which
is the
"""

def reverse_bits(n: str) -> int:
    sum = 0
    for idx, bit in enumerate(n):
        sum += int(bit) * 2**idx
    return sum

assert reverse_bits("00000010100101000001111010011100") == 964176192
assert reverse_bits("11111111111111111111111111111101") == 3221225471





"""
Aside on signed vs unsigned binary numbers:
...
"""