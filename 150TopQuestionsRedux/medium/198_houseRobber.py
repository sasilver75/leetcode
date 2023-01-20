"""
House Robber

You're a professional robber plannig to rob houses along a street!

Each house has a certain amount of money stsashed, and the only constraint
stopping you from robbing each is that adjacent houses have connected securitty
systems, and will automatically contact the police if two adjacent houses
get robbed on the same night!

Given an integer array nums representing the amount of money of eaech house, return the maximum amount of money
You can rob tonight without alerting the police
"""

"""
A Naive solution using a depth-first search approach
"""


def rob_naive(nums: list[int]) -> int:
    def secure_the_bag(idx: int, bag: int) -> int:
        # Given a current house position (and the ability to steal), we can
        # either not rob the current house, or rob the current house and skip the next house
        if idx >= len(nums):
            return bag

        return max(
            secure_the_bag(idx + 2, bag + nums[idx]),
            secure_the_bag(idx + 1, bag)
        )

    return secure_the_bag(0, 0)


"""
We can do this in a more performant way, in O(N) time by using a DP table
DP[i] = Maximum that you could rob form the nums[i:]
DP[-1] = nums[-1]
"""


def rob(nums: list[int]) -> int:
    dp = [None] * len(nums)

    # Populate the DP table in reverse
    for idx in range(len(dp) - 1, -1, -1):
        # Rob or don't rob
        one_forward = dp[idx + 1] if idx + 1 < len(nums) else 0
        two_forward = dp[idx + 2] if idx + 2 < len(nums) else 0
        dp[idx] = max(
            nums[idx] + two_forward,  # Rob
            one_forward  # Don't rob
        )

    return dp[0]


def test(fn):
    assert fn([1, 2, 3,
               1]) == 4  # Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.
    assert fn([2, 7, 9, 3, 1]) == 12  # Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).


test(rob_naive)
test(rob)
