"""
House Robber II
Category: DP

You're a professional robber planning to rob houses along a street!

All of the houses are arranged in a circle!
That means the first house is the neighbor of the last one!

Adjacent houses have security systems connected such that the police will
automatically be contacted if two adjacent houses are broken into on the same
night!

Given an integer array `nums` representing the amount of money in each house,
return the MAXIMM amount of moeny that you can rob tonight, without alerting
the police!
"""

"""
I'm thinking... the really only change that happened between HouseRobber
and HouseRobber II is:
" The houses are arranged in a circle "
Meaning if you rob the first house, you can't rob the last house.
And if you rob the last house, you can't rob the first house.
IE Rob (at most) ONE of  (first house, last house)
"""
def rob(houses: list[int]):
    # OPTIMIZATION NOTE: WE can even get away with using O(1) memory if we just keep track of the last two dp values

    # dp[i] = maximum amount of money we could have made by now
    dp = [0] * (len(houses) - 1) # Of length n-1 because for each of the two iterations, we'll exclude either the first or last house

    # First Iteration across DP: Assuming we ROB first house (last house does not exist)
    # This is going to look the same as HouseRobberI
    for i in range(len(dp)):
        dp[i] = max(
            dp[i-1] if i-1 >= 0 else 0, # Don't Rob
            houses[i] + (dp[i-2] if i-2 >= 0 else 0) # Rob
        )

    rob_first_best = dp[-1]

    # Second Iteration across DP: Assuming we DON'T ROB first house (first house does not exist)
    # This is going to look the same as HouseRobberI but we'll make a small modification for accessing indices in houses
    for i in range(len(dp)):
        dp[i] = max(
            dp[i-1] if i-1 >= 0 else 0, # Don't Rob
            houses[i+1] + (dp[i-2] if i-2 >= 0 else 0) # Rob (DP is "shifted over" 1 relative to houses)
        )

    rob_second_best = dp[-1]

    return max(
        rob_first_best,
        rob_second_best
    )

def test(fn):
    assert fn([2, 3, 2]) == 3  # Rob house 2
    assert fn([1, 2, 3, 1]) == 4  # Rob houses 1 and 3
    assert fn([1,2,3]) == 3 # Rob house 3

test(rob) # NOTE: WE can even get away with using O(1) memory if we just keep track of the last two dp values