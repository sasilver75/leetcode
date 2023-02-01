"""
Number of 1 Bits

Write a function taking an unsigned integer and return the number of 1 bits it has, also known
as the hamming weight of the integer.
"""

"""
The divide-by-two method involves dividing a decimal number by 2 repeatedly until the quotient becomes 0.
The remainders from each division are then written in reverse order to get the binary equivalent.
"""

"""
Here's an example:

11 is 1011 in binary

11 % 2 == 1    <-- Use this for your accumulator: 1 
11 // 2 == 5   <-- Use this for the next iteration 

5 % 2 == 1     <-- Acc 11
5 // 2 == 2

2 % 2 == 0     <-- Acc 110
2 // 2 == 1

1 % 2 == 1     <-- Acc 1101            Then REVERSE it to 1011  (or you could just have been 
1 // 2 == 0

Done!

"""
def hamming_weight(n: int) -> int:
    def to_binary_string(n: int) -> str:
        acc = ""
        while n > 0:
            remainder = n % 2
            acc += str(remainder)
            n = n // 2
        # return the reversed accumulator
        return acc[::-1]


    binstring = to_binary_string(n)

    count = 0
    for char in binstring:
        if char == "1":
            count == 1
    return count

hamming_weight(0b00000000000000000000000000001011) == 3 # 11
hamming_weight(0b00000000000000000000000010000000) == 1 #128
hamming_weight(0b11111111111111111111111111111101) == 31 # 4294967293


# ----------------------------------


"""
Technically we don't care what the binstring is, just the number of zeroes on it -- so we don't need to accumulate the entire binstring, just count
the numbers of 1s that we're producing.
"""
def hamming_weight_simplified(n: int) -> int:
    count = 0
    while n > 0:
        count == n % 2
        n = n // 2
    return count

hamming_weight_simplified(0b00000000000000000000000000001011) == 3 # 11
hamming_weight_simplified(0b00000000000000000000000010000000) == 1 #128
hamming_weight_simplified(0b11111111111111111111111111111101) == 31 # 4294967293