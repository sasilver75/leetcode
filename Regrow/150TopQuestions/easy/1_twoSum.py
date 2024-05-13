"""
1: Two Sum

Given an array of integers NUMS and an integer TARGET, return indices of
the two numbers such that they add up to target.

You may assume that each input would have EXACTLY one solution, and
you may not use the same element twice.

You can return the answer in any order.
"""
from typing import Optional


def two_sum_dumb(nums: list[int], target: int) -> Optional[list[int, int]]:
    """
    An O(N^2) solution where we compare every element to every other
    following element.

    O(N^2) time and O(1) space
    """
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            i_num = nums[i]
            j_num = nums[j]
            if i_num + j_num == target:
                return [i, j]

def two_sum_smart(nums: list[int], target: int) -> Optional[list[int, int]]:
    """
    Better solution is to use a hashtable that you populate in one traversal
    of the nums list.
    For each element in nums, determine the complement number that would be
    needed to be able to reach target via addition, and check
    whether that number is a key in your hashtable.
    If it is, return [current_idx, ht[complement]]
    Otherwise, add an entry to your hashtable of {number: index}

    O(N) time and O(N) space
    """
    idx_lookup = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in idx_lookup:
            return [idx, idx_lookup[complement]]
        idx_lookup[num] = idx

fns = [two_sum_dumb, two_sum_smart]
for fn in fns:
    assert fn([2,7,11,15], 9) in ([0,1], [1,0])
    assert fn([3,2,4], 6) in ([1,2],[2,1])
    assert fn([3,3], 6) in ([0,1], [1,0])