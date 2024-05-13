"""
Write an algorithm to determine if a number n is HAPPY

a HAPPY NUMBER is a number defined by the following process:

1) Starting with any positive integer, replace the number by the um
of the squares of its deigits
2) Repeat the process until the number equals 1 (where it will stay), or it loops endlessly with
a cycle which does not include 1.
3) The numbers for which this process ends in 1 are happy.

Return whether n is a happy number.

Example:
    n = 19  --> True
Explanation:
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

Example:
    n = 2 -> False
Explanation:
    2^2 = 4
    4^2 = 8
    8^2 = 64
    6^2 + 4^2 = 52
    5^2 + 2^2 = 29
    2^2 + 9^2 = 85
    8^2 + 5^2 = 89 <
    64 + 81 = 145
    1+16+25 = 42
    16+4 = 20
    4 + 0 = 4
    16    = 16
    1 + 36 = 37
    9 + 49 = 58
    25 + 64 = 89  <<<< We've seen this before
    64 + 81 = 145 <<< Seen this before

Interesting things to note:
I think this could work if:
* You can prove that you will generate a sum of 1, 10, 100, 1000 at any point (True)
* You can prove that there will be a cycle at some point (False)

Interesting thing is that 58 and 85 both yielded the same 89 that started a cycle, in
the second example. Is this useful?
"""

def isHappy(n: int) -> bool:
    seen = set()
    while n != 1:
        n = sum([digit ** 2 for digit in str(n)])
        if n in seen:
            return False # Cycle
        else:
            seen.add(n)
    return True