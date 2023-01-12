"""
House Robber
Category: DP

You are a professional robber planning to rob houses
along a street. Each house has a certain amount of money
stashed, and the only constraint stopping you from
robbing each of them is that the adjacent houses have security sytems
connected that will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money
of each house, return the maximum amount of money you can rob tonight WITHOUT
alerting the police.
"""


def rob_brute(nums: list[int]) -> int:
    def helper(idx: int, bag: int):
        # Given an idx, assume that we have the ability to rob. Do we rob or not?
        if idx >= len(nums):
            return bag

        # Rob the House or Don't
        return max(
            helper(idx + 1, bag),  # Don't rob this one.
            helper(idx + 2, bag + nums[idx])  # Rob this one; skip the next house
        )

    return helper(0, 0)


def rob_dp(nums: list[int]) -> int:
    dp = [0] * len(nums)

    for i in range(len(dp)):
        # Either Rob this House (and assume that you robbed two houses ago) or Don't rob this House (assume you robbed one house ago)
        dp[i] = max(
            nums[i] + (dp[i-2] if i - 2 >= 0 else 0), # Rob this house
            dp[i-1] if i - 1 >= 0 else 0 # Don't rob this house
        )

    return dp[-1]

def rob_dp_constant_memory(nums: list[int]) -> int:
    last_bag = 0
    two_bags_ago = 0
    for i in range(len(nums)):
        # Eitehr Rob this House or Don't
        bag = max(
            two_bags_ago + nums[i],
            last_bag
        )

        # Shift
        two_bags_ago = last_bag
        last_bag = bag

    return bag


# -- Test --
def test(fn):
    assert fn([1, 2, 3, 1]) == 4  # 1 3
    assert fn([2, 7, 9, 3, 1]) == 12  # 1 3 5


test(rob_brute)
test(rob_dp)
test(rob_dp_constant_memory)