"""
Happy Number

Write an algorithm to determine if a number n is happy

A number if happy by the following process:
- Starting with any positive integer , replace the number by the sum of the
squares of its digits
- Repeat the process until the number equals 1 (wher eit will stay), or loop endlessly in a cycle,
which doesn't include 1.
- The numbers for which the process ends in 1 are happy
"""

def is_happy(n: int) -> bool:

    def replace(num: int) -> int:
        """Replace the number by the sum of the squares of its digits"""
        num_string = str(num)
        acc = 0
        for ns in num_string:
            acc += int(ns)**2
        return acc

    # Given the nature of the transformation, if we EVER reach a number that we've already seen,
    # then we know that we're entering a cycle.
    seen = set()
    while True:
        if n in seen:
            return False
        if n == 1:
            return True

        seen.add(n)

        n = replace(n)

assert is_happy(19) == True
assert is_happy(2) == False