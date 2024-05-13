"""
House Robber

You're a professional robber trying to rob houses along a street.
Each house has a certain amount of money stashed; the only constraint stopping you from robbing each of them
is that the adjacent houses have security systems connected, so you can't rob adjacent houses.

Give an integer array nums representing the amount of money of each house, return the maximum amount of money
you can rob tonight without alerting the police.
"""


def rob_naive(houses: list[int]) -> int:
    max_bag = -float('inf')
    def explore(idx: int, bag: int) -> None:
        nonlocal max_bag
        if idx >= len(houses):
            max_bag = max(max_bag, bag)
            return

        # We can rob at our current location; Either rob or don't rob
        explore(idx+2, bag + houses[idx]) # Rob
        explore(idx+1, bag) # Don't rob

    explore(0, 0)
    return max_bag


"""
We can do a 1-dimensional dynamic programming solution, I think
dp of length houses

dp[i] = maximum we could rob in houses[i:]
So we can populate this dp table from left to right

dp[i] = max(
    houses[i] + dp[i+2], # Rob this house, and be unable to rob the following house.
    dp[i+1] # Don't rob this house
)
"""
def rob(houses: list[int]) -> int:
    dp = [None] * len(houses) # It doesn't really matter what we initialize theses to; they'll all be populated.

    for idx in range(len(dp) - 1, -1 ,-1):
        best_if_no_rob = dp[idx+1] if idx + 1 < len(dp) else 0
        best_if_rob = dp[idx+2] if idx + 2 < len(dp) else 0

        dp[idx] = max(
            houses[idx] + best_if_rob,
            best_if_no_rob
        )

    return dp[0]

def test(fn):
    assert fn([1, 2, 3, 1]) == 4
    assert fn([2, 7, 9, 3, 1]) == 12


test(rob_naive)
test(rob)
