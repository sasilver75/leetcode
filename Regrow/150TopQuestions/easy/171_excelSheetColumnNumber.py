"""
Excel Sheet Column Number

Given a string columnTtile that represents the column title as appears in an Excel sheet, return its cooresponding
column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
"""
import string

"""
Thinking: Can we get a few more examples (length 3) to make this make more sense?
AAA = 703

So it seems like A-Z is 1-26 inclusive. Cool.
AA is 27, which is 26 + 1
So the leading A is counting as 26

And if we extended that to AAA, it would be 703, which where the leading A accounts for (703-27)=676=26^2
So it seems like each number is "valued as":

(Base value of letter) * 26 ^ (ith index from the right [starting at 0])

So we would expect something like ZY to equal 25+(26*26) = 701, and CGF to equal 6+(26*7)+(26*26*3) = 2216 
"""

def excel_column_to_number(col: str) -> int:
    if not all(char in string.ascii_uppercase for char in col):
        raise ValueError("Bad Input -- All characters must be uppercase ascii letters")

    # Could either do a lookup table enumerating the value for each A...Z as 1...26
    # Or could realize that we can just subtract 64 so that ord('A') of 65 would equal 1, and so on.
    total = 0
    col = col[::-1] # Reverse the col
    for ind, dig in enumerate(col):
        total += (ord(dig) - 64) * (26 ** ind)

    return total



assert excel_column_to_number("A") == 1
assert excel_column_to_number("AB") == 28
assert excel_column_to_number("ZY") == 701
assert excel_column_to_number("AAA") == 703

