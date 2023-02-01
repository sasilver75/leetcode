"""
Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the ONLY number in the range that's missing
from the array!

"""

"""
Here's an off-the-cuff O(NLOGN)/O(1) solution
"""


def missing_number_naive(nums: list[int]) -> int:
    nums.sort()
    for idx in range(len(nums)):
        num = nums[idx]
        if num != idx:
            return idx

    return len(nums)


"""
Can we do better than O(NLOGN)/O(1)?
We can do O(N)/O(N) pretty easily
"""


def missing_number_naive2(nums: list[int]) -> int:
    nums_set = set(nums)
    for idx in range(len(nums) + 1):
        if idx not in nums_set:
            return idx


"""
Can we do O(N)/O(1)?

Assume there were no holes in the list

Considering a list of length 3

[1,2,3] --> Sum=6, 0 is missing
[0,2,3] --> Sum=5, 1 is missing
[0,1,3] --> Sum=4, 2 is missing
[0,1,2] --> Sum=3, 3 is missing

This is interesting, isn't it... There's gotta be a relationship here

It seems like sum(1...N) - sum(given_list) = missing_value

"""


def missing_number(nums: list[int]) -> int:
    comparison_sum = sum(range(1, len(nums) + 1))  # ex [1,2,3] = 6
    actual_sum = sum(nums)  # ex [0,1,3] = 4
    return comparison_sum - actual_sum  # ex 6 - 4 = 2 is the mone that's missing


def test(fn):
    assert fn([3, 0, 1]) == 2
    assert fn([0, 1]) == 2
    assert fn([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


test(missing_number_naive)
test(missing_number_naive2)
test(missing_number)
