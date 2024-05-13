"""
Maximum Subarray

Given an integer array nums, find the SUBARRAY which has the LARGEST SUM
and return its SUM
"""


def max_subarray_sum_brute(nums: list[int]) -> int:
    if not nums:
        return 0

    # Generate all subarrays
    subarrays = []
    for start in range(0, len(nums)):
        for end in range(start, len(nums)):
            subarrays.append(nums[start: end + 1])

    # Get the maximum of them
    return max([sum(subarray) for subarray in subarrays])

    # Get the maximum of them
    # max_sum = None
    # for subarray in subarrays:
    #     subarray_sum = sum(subarray)
    #     max_sum = max(max_sum, subarray_sum) if max_sum is not None else subarray_sum
    # return max_sum


"""

"""


def max_subarray_sum_dp(nums: list[int]) -> int:
    """
    The idea of this DP solution is that we're going to do a bottom-up 1-dimensional
    dynamic programming solution... Where we'll work from the back of the array.

    And at each point in the DP table, it's the max subarray sum starting at
    that point and moving to the right.
    """
    dp = [None] * len(nums)
    dp[-1] = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        dp[i] = max(nums[i], nums[i] + dp[i + 1])
    # print(dp)
    return max(dp)  # The subarray could start at any location in the list


def test(fn):
    assert fn([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert fn([1]) == 1
    assert fn([5, 4, -1, 7, 8]) == 23


test(max_subarray_sum_brute)
test(max_subarray_sum_dp)
