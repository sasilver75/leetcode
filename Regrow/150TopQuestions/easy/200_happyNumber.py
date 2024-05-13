"""
Happy Number

Write an algorithm to determine if a number n is happy.

A HAPPY NUMBER is a number defined by the following process:
1) Starting with any positive integer, replace the number by the sum of
the squares of its digits.
2) Repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include one.
3) Those numbers for which this process ends in 1 are happy.

Return TRUE if N is a happy number, else FALSE
"""

def is_happy(n: int) -> bool:
    seen = set()
    while n != 1:
        n = sum([int(digit) ** 2 for digit in str(n)])
        if n in seen:
            return False
        seen.add(n)
    return True

assert is_happy(19) == True
assert is_happy(2) == False