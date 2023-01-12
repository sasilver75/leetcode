"""
Given an integer n, return an array ans of length n + 1 such
that for each i (0 <= i <= n),
ans[i] is the number of i's in the binary representation of i

Ex:
n = 2
Output = [0, 1, 1]
0 --> 0
1 --> 1
2 --> 10
"""

def bit_counts(n: int) -> list[int]:
    bit_strings = [num_to_binary(i)for i in range(0, n+1)]
    return [sum([int(bit) for bit in bit_string]) for bit_string in bit_strings]

def num_to_binary(n: int) -> int:
    """
    Consider 6 == 110
    6 // 2 is 3 == 11
    3 // 2 is 1 == 1
    Do we notice that we're chopping off a digit each time? And that digit
    is actually the remainder of the // 2.

    That is, 6 // 2 has a remainder of 0... and results in 3
             3 // 2 has a remainder of 1... and results in 1
             1 // 2 has a remainder of 1... and results in 0
                                      011
                                Reverse this... 110
    """
    bin_list = []
    while n > 0:
        bin_list.append(n % 2)
        n = n // 2
    return "".join(str(bit) for bit in bin_list[::-1])

    # First, we need to get the biggest power of two chunk that we can take out

for i in range(10):
    print(i , num_to_binary(i))

assert bit_counts(2) == [0,1,1]
assert bit_counts(5) == [0,1,1,2,1,2]