"""
Reverse Bits

Reverse bits of a given 32-bits unsigned integer

"""

def reverse_bits(s: str) -> int:
    s = s[::-1]
    acc = 0
    for idx in range(len(s) - 1, -1, -1):
        digit = s[idx]
        exp = len(s) - idx - 1
        acc += int(digit) * 2 ** exp
    return acc



assert reverse_bits("00000010100101000001111010011100") == 964176192
assert reverse_bits("11111111111111111111111111111101") == 3221225471