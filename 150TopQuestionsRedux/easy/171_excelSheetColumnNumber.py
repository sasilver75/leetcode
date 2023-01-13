"""
Excel Sheet Column Number

Given a string `columnTitle` that representes the column title as it might
appear in an excel sheet, return its corresponding column number.

For example:
A->1
B->2
C->3
...
Z-> 26
AA-> 27
AB-> 28
...
"""

"""
This is pretty much just Base-26, isn't it?
If we can map A->1, B->2, Z->26
Then we can evaluate valeus at a position as we do for base 10

It's generally digit * base ** exp

So base 10:
412 = (2 * 10 ** 0)[2] + (1 * 10 ** 1)[10] + (4 * 10 ** 2)[400] = 412

And for base 26:
AB = (2 * 26 ** 0)[2] + (1 * 26 ** 1)[26] = 28
"""
def title_to_number(column_title: str) -> int:

    def to_base_ten(char: str) -> int:
        """
        A helper function to convert A...Z to 1...26
        """
        return ord(char) - 64

    acc = 0
    for idx in range(len(column_title) - 1, -1, -1):
        char = column_title[idx]
        digit = to_base_ten(char)
        exp = len(column_title) - idx - 1
        acc += digit * 26 ** exp

    return acc


assert title_to_number("A") == 1
assert title_to_number("AB") == 28
assert title_to_number("ZY") == 701