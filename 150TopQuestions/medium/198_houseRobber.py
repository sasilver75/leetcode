"""
House Robber

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, and
the only constraint stopping me from robbing each of them
is that adjacent houses have security systems connected, and the police
will automatically be contacted if two adjacent houses were broken into
on the same night!

Given an integer array `nums` representing the amount of moneyin
each house, return the MAXIMUM amount of money that you can rob tonight,
without alerting the police!

"""

"""
For the brute example, I'm thinking about doing a DFS via recursion
"""

def rob_brute(nums: list[int]) -> int:

    def helper(idx: int, money: int) -> int:
        if idx >= len(nums):
            return money

        # If you can rob, you either rob or pass. If you can't rob, you don't rob.
        return max(
            helper(idx+2, money+nums[idx]),
            helper(idx+1, money),
        )

    ans = helper(0, 0)
    print(ans)
    return ans


def rob_brute_alternative(nums: list[int]) -> int:

    def helper(idx: int, money: int, can_rob: bool) -> int:
        if idx >= len(nums):
            return money

        # If you can rob, you either rob or pass. If you can't rob, you don't rob.
        if can_rob:
            return max(
                helper(idx+1, money+nums[idx], False),
                helper(idx+1, money, True),
            )
        else:
            return helper(idx+1, money, True)

    return helper(0, 0, True)

"""
Insight: We'd never want to not rob TWO TIMES IN A ROW! That wouldn't make sense.

So given houses [1,2,3,1]

Houses:                 [1, 2, 3, 1]
MaxRobbery @ Index:     [1, 2, 4, 4]

Where the value at MaxRobbery position i is either:
    * Robbing this current house (because we didn't rob the last house)
    * Not robbing this current house (because we robbed the last one)
    
In other words:

MaxRobbery[i] = Max(
                    Houses[i] + Max_Robbery[i-2], # Rob this house
                    Max_Robbery[i-1] # Don't rob this house
            )

"""
def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    # Using Dynamic Programming
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = nums[1]

    for i in range(2, len(nums)):
        dp[i] = max(
            nums[i] + dp[i-2],
            dp[i-1]
        )

    return dp[-1]




# -- Test Zone --
def test(fn):
    assert fn([1,2,3,1]) == 4
    assert fn([2,7,9,3,1]) == 12

test(rob_brute)
test(rob_brute_alternative)
test(rob)