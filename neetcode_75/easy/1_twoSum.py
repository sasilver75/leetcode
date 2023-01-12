"""
Two Sum
Category: Array

Given an array of integers `nums` and an integer
target `target`, return indices of the two numbers such
that they add up to a `target`

You may assume that each input would have exactly
one solution, and you may NOT use the same element twice.

You can return the answer in any order
"""


def two_sum_naive(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {num: idx for idx, num in enumerate(nums)}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in lookup and lookup[complement] != idx:  # Don't match with yourself! ;)
            return [idx, lookup[complement]]


def test(fn):
    assert fn([2, 7, 11, 15], 9) in ([0, 1], [1, 0])
    assert fn([3, 2, 4], 6) in ([1, 2], [2, 1])
    assert fn([3, 3], 6) in ([0, 1],)


test(two_sum_naive)
test(two_sum)
