"""
You have n coins and you want to build a staircase with
these coins.
The coins consist of k rows, where the ith row has exactly
i coins.
The last row of the staircase MAY be incomplete...

Ex: https://leetcode.com/problems/arranging-coins/

X
XX
XX[]
Input: 5
Output: 2
Because the 3rd row is incomplete, we return 2

X
XX
XXX
XX[][]
Input: 8
Output: 3
Because the 4th row is incomplete, we return 3
"""

"""
Thinking:
It seems weird in these pictures that the incomplete "bottom" row doesn't make
them a valid staircase. I think it's easier to turn your hear 90 degrees right
and thinking about building each stair "vertically". Then it's just a question of
how many complete stairs can you vertically build
"""

def stair_count(n: int) -> int:
    """
    O(N) time and O(1) space

    :param n: The number of coins to work with
    :return: The number of stairs that could be constructed using n coins
    """
    # Treat "n" as the number of remaining coins
    stair_cost = 1 # Cost in coins of building the next stair. Starts at 1

    # While we can still buy a stair...
    while n - stair_cost >= 0:
        n -= stair_cost
        stair_cost += 1

    # If we end and the stair_cost is 1, then we haven't built any stairs. If 2, we built one stair
    # General rule is we built (stair_cost - 1) stairs
    return stair_cost - 1



assert stair_count(5) == 2
assert stair_count(8) == 3