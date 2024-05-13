"""
Two Sum

Given a list of integers nums and an integer target,
return indices of the two numbers such that they add to target

Guaranteed solution, exactly one solution
May not use the same element twice
Return the answer in any order
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    numbers = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in numbers:
            return [numbers[complement], idx]
        numbers[num] = idx


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
