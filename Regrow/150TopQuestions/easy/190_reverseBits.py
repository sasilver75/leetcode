"""
Reverse Bits

Reverse bits of a given 32-bit unsigned integer
"""

def reverse_bits(bits: str) -> int:
    rev_bits = bits[::-1]
    return binstring_to_decimal(rev_bits)

def binstring_to_decimal(s: str) -> int:
    total = 0
    s_rev = s[::-1]
    for idx, bit in enumerate(s_rev):
        total += int(bit) * (2**idx)
    return total

# ----------
def reverse_bits_combined(bits: str) -> int:
    # Noticed that above we're reversing the string twice. We techincally don't have to do that.
    total = 0
    for idx, bit in enumerate(bits):
        total += int(bit) * (2 ** idx)
    return total

# ----------
assert binstring_to_decimal("0001") == 1
assert binstring_to_decimal("0101") == 5
assert binstring_to_decimal("0011") == 3
assert binstring_to_decimal("1001") == 9

assert reverse_bits("00000010100101000001111010011100") == 964176192 # The input represents the unsigned integer 43261596, so return 064176192, which has a binary representation of 00111001011110000010100101000000
assert reverse_bits("11111111111111111111111111111101") == 3221225471 # The input's reverse binary representation is 10111111111111111111111111111111, so return 3221225471

assert reverse_bits_combined("00000010100101000001111010011100") == 964176192 # The input represents the unsigned integer 43261596, so return 064176192, which has a binary representation of 00111001011110000010100101000000
assert reverse_bits_combined("11111111111111111111111111111101") == 3221225471 # The input's reverse binary representation is 10111111111111111111111111111111, so return 3221225471

