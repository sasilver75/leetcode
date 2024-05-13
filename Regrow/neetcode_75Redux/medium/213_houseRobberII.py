"""
House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.

All houses are arranged in a CIRCLE

Adjacency houses have security systems connected, and will automatically contact the police if two
adjacent houses were broken into on a single night

Given an integer array representing hte amuont of $ in each house, return the maximum amount of money you can rob tonight wihtout
alerting the police.


[1,2,3,1] -> 4
"""

"""
I the insight that makes solving this circular one easier is to
do the rob process where you can rob the first house (and not the last house)
and do where you can rob the last house (and not the first house)

And to take the max of these two.


"""


def rob(nums: list[int]) -> int:
    houses_can_rob_first = nums[:-1]
    houses_cannot_rob_first = nums[1:]

    best_bag = -float('inf')

    for houses in [houses_can_rob_first, houses_cannot_rob_first]:
        dp = [0] * len(houses)
        for idx in range(len(dp) - 1, -1, -1):
            bag_if_rob = nums[idx] + (dp[idx + 2] if idx + 2 < len(dp) else 0)
            bag_if_no_rob = dp[idx + 1] if idx + 1 < len(dp) else 0
            dp[idx] = max(
                bag_if_rob,
                bag_if_no_rob
            )

        print(dp)

        best_bag = max(best_bag, dp[0])

    print(best_bag)
    return best_bag


def test(fn):
    assert fn([2, 3, 2])
    assert fn([1, 2, 3, 1])


test(rob)
