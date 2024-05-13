"""
Hamming Distance

The Hamming Distance between two integers is the number of positions at which
the corresponding bits are different!

Given two integers x and y, return the HAMMING DISTANCE between them!
"""

def hd(x: int, y: int) -> int:
    x_binstring = binstring(x)
    y_binstring = binstring(y)
    print(f"Binstrings are {x_binstring} and {y_binstring}")

    bit_diffs = 0

    x_idx, y_idx = len(x_binstring) - 1, len(y_binstring) - 1
    while x_idx >= 0 and y_idx >= 0:
        x_bit = x_binstring[x_idx]
        y_bit = y_binstring[y_idx]

        bit_diffs += int(x_bit != y_bit)

        x_idx -= 1
        y_idx -= 1

    # print(f"Checkpoint 1: {bit_diffs}")

    while x_idx >= 0:
        x_bit_char = x_binstring[x_idx]
        if x_bit_char == '1':
            bit_diffs += 1
        x_idx -= 1

    # print(f"Checkpoint 2: {bit_diffs}")

    while y_idx >= 0:
        y_bit_char = y_binstring[y_idx]
        if y_bit_char == '1':
            bit_diffs += 1
        y_idx -= 1

    # print(f"Checkpoint 3: {bit_diffs}")

    print(bit_diffs)
    return bit_diffs



def binstring(n: int) -> str:
    bits = []

    while n > 0:
        bits.append(n % 2)
        n = n // 2

    return "".join([str(bit) for bit in bits[::-1]]) if bits else "0"

assert binstring(0) == "0"
assert binstring(1) == "1"
assert binstring(4) == "100"
assert binstring(11) == "1011"


"""
            V
    0   0   1
    1   0   0
    ^
"""
assert hd(1, 4) == 2

assert hd(3, 1) == 1

"""
Okay, that was a good exercise! But there's also an "easier"
way to determine the hamming distance using "bit manipulation"

HD:    0   0   1
       1   0   0    =   2
    
What we're actually doing is the sum of the bitwise XOR, right?

    4 ^ 1 == 5 == 1 0 1 -> 2
    
"""

def hd_bitwise(x: int, y: int) -> int:
    xor = x ^ y # XOR operation
    ham = 0 # For storing the # of 1s from the XOR operation
    while xor != 0: # While there's still bits to check
        ham += xor % 2 # Increase ham when a 1 is seen
        xor >>= 1 # Rightward bit shift (101 -> 10 -> 1 -> 0 -> 0)
    return ham

