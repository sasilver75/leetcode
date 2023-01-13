"""
191 Number of One Bits

Write a function taking an unsigned integer, and returning the number of "1"
bits that it has, also known as its hamming weight.
"""

def hamming_weight(n: int) -> int:
    # Convert to binary 32-bit bitstring
    bitarray = [0]*32
    for i in range(len(bitarray)):
        exp = len(bitarray) - i - 1
        if 2 ** exp <= n:
            bitarray[i] = 1
            n -= (2**exp)
    count_ones = sum(bitarray)
    print(bitarray, count_ones)
    return count_ones



def test(fn):
    assert fn(0b00000000000000000000000000001011) == 3
    assert fn(0b00000000000000000000000010000000) == 1
    assert fn(0b11111111111111111111111111111101) == 31

test(hamming_weight)