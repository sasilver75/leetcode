"""
Reverse Integer

Given a 32-bit SIGNED integer x, return x with its digits REVERSED.
If reversing x causes the value to go OUTSIDE the signed 32-bit integer range [-2^31. 2^31 - 1], then return 0.
"""


def reverse_integer(n: int) -> int:
    ns = str(n)
    neg = False
    if ns[0] == '-':
        neg = True
        ns = ns[1:]  # Clip of negative and flip bool
    ns = ns[::-1]

    # Reapply negative if needed
    n = int(ns) * (-1 if neg else 1)

    ans = n if (-2 ** 31 <= n <= 2 ** 31 - 1) else 0
    print(ans)
    return ans


assert reverse_integer(123) == 321
assert reverse_integer(-123) == -321
assert reverse_integer(120) == 21
