"""
Perfect Squares

Given an integer n, return the least number of perfect square numbers that
sum to n.

A perfect square is an integer that is the square of an integer; in otehr
words, it is the product of some integer with itself!

For example:

1,
4,
9,
16 are perfect squares while 3 and 11 are not.
"""

"""
Thinking:
I can do this one :)
I think there are two phases to this problem:

1) Generate all of the squares that we could use in this problem,
from [0...n].

2) This is now a "jumping" problem, where we have to get from 0 -> n,
using only the "jumps" available from our Step 1 above.
    - We could either solve this recursively (brute force), or with DP!
    - The DP solution would be... "What's the fewest number of jumps we could make
    to get to this n?"
"""


def num_squares(n: int) -> int:
    if n == 0:
        return 0

    squares = [i ** 2 for i in range(1, n) if i ** 2 <= n]  # Is there a more elegant way to do this
    dp = [None] * (n + 1)  # "indexed" list. "None" indicates "you can't get here with squares"
    dp[0] = 0

    # print(dp, squares)

    for idx in range(len(dp)):
        # What's the shortest way that I can get to the ith index?
        valid_pasts = [dp[idx - square] for square in squares if idx - square >= 0 and dp[idx - square] is not None]
        if valid_pasts:
            dp[idx] = min(valid_pasts) + 1

    # print(dp)
    return dp[n]


def test(fn):
    assert fn(5) == 2  # 4 + 1
    assert fn(12) == 3  # 4 + 4 + 4
    assert fn(13) == 2  # 4 + 9


test(num_squares)
