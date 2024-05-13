"""
Excel Sheet Column Number

Given a string "columnTitle" that represents the column title
as appears in an excel sheet, return its corresponding column NUMBER
"""
import string

"""
I think the intuition for this is that you're going to be walking it backwards

When we have just one letter, we have 26 spaces.
Wehn we have two letters, we have 26*26 = 676
When we have there letters, we have 26*26*26=17576 
The rule seems to be 26^N as the number of possibilities... does this help us?

A = A * 26^0
  = 1 * 1
  = 1

C = C * 26^0
  = 3 * 1
  = 3
  
AC = (C * 26^0) + (A * 26^1)
   = (3 * 1) + (1 * 26)
   = 3 + 26
   = 29
"""
def column_title(name: str) -> int:
    # name length is in [1,7]
    lookup = {char:val for char, val in zip(string.ascii_uppercase, range(1,27))}
    name = name.upper()[::-1]
    sum = 0
    for idx, char in enumerate(name):
        char_value = lookup[char]
        sum += char_value * (26**idx)
    return sum



print(column_title("A"))  # 1
print(column_title("AB"))  # 28
print(column_title("AZ")) # 52
print(column_title("ZY"))  # 701
print(column_title("BC")) # 55
print(column_title("CA")) # 79
print(column_title("ZZ")) # 702
print(column_title("AAA")) #703

# Bonus: How would we convert a number into