"""
Two Sum (Easy)

Given an array of integers UMS and an integer TARGET, return INDICES of the TWO NUMBERS such that they add up to TARGET
You may assume that each input would have only ONE SOLUTION, and you MAY NOT USE THE SAME ELEMENT TWICE
"""
import collections


def two_sum_naive(nums: list[int], target: int) -> list[int]:
    for idx in range(len(nums)):
        for pair_index in range(idx+1, len(nums)):
            if nums[idx] + nums[pair_index] == target:
                return [idx, pair_index]

def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for idx, num in enumerate(nums):
        # Have we seen this number's complement in the past? At what index?
        complement = target - num
        if complement in lookup:
            # It's specified in the test cases that the earlier index comes first
            return [lookup[complement], idx]

        # Otherwise, add this number to lookup (overwriting any existing occurrence of that number
        lookup[num] = idx






def test(fn):
    assert fn([2, 7, 11, 15], 9) == [0, 1]
    assert fn([3, 2, 4], 6) == [1, 2]
    assert fn([3, 3], 6) == [0, 1]

# test(two_sum_naive)
test(two_sum)