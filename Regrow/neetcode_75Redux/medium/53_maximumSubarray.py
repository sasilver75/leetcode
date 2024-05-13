"""
Maximum Subarray (Medium)

Given an integers array nums, find the SUBARRAY with the largest sum, and return ITS Sum
"""

"""
Ways of going about this:
1. Generate every possible subarray, and 
    - This can be optimized to not first materialize the subarray, but to calculate the sum for each subarray as you go, and not use additional memory

2. Note that we don't care about WHAT the subarray is, or its location. Just consider that we want to determine the maximum sum that we could get by
assessing a contiguous subarray of our nums array. At a current position in the list, and given some sum "behind you", when would you want to extend
that sum? The answer is whenever it's >= 0. Otherwise, you'd prefer to just start a new subarray sum.
"""


def max_subarray_sum_naive(nums: list[int]) -> int:
    subarrays = []
    for starting_index in range(len(nums)):
        for ending_index in range(starting_index, len(nums)):
            subarrays.append(nums[starting_index:ending_index + 1])

    max_sum = -float('inf')
    for sa in subarrays:
        max_sum = max(max_sum, sum(sa))
    return max_sum


def max_subarray_sum_naive_optimized(nums: list[int]) -> int:
    max_sum = -float('inf')
    for start_index in range(len(nums)):
        for end_index in range(start_index, len(nums)):
            sum = 0
            for idx in range(start_index, end_index + 1):
                sum += nums[idx]
            max_sum = max(max_sum, sum)
    return max_sum


"""
Consider: Would you like to extend the previous sum, or start a new one?
"""


def max_subarray_sum(nums: list[int]) -> int:
    max_sum = -float('inf')
    running_sum = -float('inf')
    for num in nums:
        # Extend the previous or start a new subarray?
        running_sum = max(running_sum + num, num)
        max_sum = max(max_sum, running_sum)

    return max_sum


def test(fn):
    assert fn([1, 2, 3]) == 6
    assert fn([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert fn([1]) == 1
    assert fn([5, 4, -1, 7, 8]) == 23
    assert fn([-3, -2, -1]) == -1


test(max_subarray_sum_naive)
test(max_subarray_sum_naive_optimized)
test(max_subarray_sum)
