"""
Find Target Indices After Sorting Array

You're given a 0-indexed integer array `nums` and a target element `target`

A TARGET INDEX is an index i such that nums[i] == target

Return a LIST of the target indices of nums after sorting nums in non-decreasing order.
If there are no target indices, return an empty list.

The returned list (of indices) must be sorted in increasing order.
"""

"""
Thinking:

Given [1,2,5,2,3], we first sort nums into sorted_nums.
nums = [1,2,5,2,3]
sorted_nums = [1,2,2,3,5]

We need the range of indices that contain our target number.
So we need to do a "left binary search" for the start of the range (where sn[i+1] > target),
and then a "right binary search" for the end of the range (where sn[i-1] < target).

Sorting takes O(NLogN) time
Seeking for Start, End takes Log(N) time for each

So we could actually just do a regular ond binary search for `target`, then linearly probe/scan for the start/end and not change the asymptotic complexity.
"""
def target_indices(nums: list[int], target: int) -> list[int]:
    nums.sort()

    def binary_search(nums: list[int], target: int) -> int:
        l, r = 0 , len(nums) - 1

        while l <= r:
            mid_idx = l + (r - l)//2
            mid_val = nums[mid_idx]

            if mid_val == target:
                return mid_idx
            elif target > mid_val:
                l = mid_idx + 1
            else:
                r = mid_idx - 1

        return -1


    idx = binary_search(nums, target)
    if idx == -1:
        return []

    l, r = idx, idx
    while l - 1 >= 0 and nums [l-1] == target:
        l -= 1
    while r + 1 < len(nums) and nums[r+1] == target:
        r += 1

    return [i for i in range(l, r+1)]


def test(fn):
    assert fn([1, 2, 5, 2, 3], 2) == [1, 2]
    assert fn([1, 2, 5, 2, 3], 3) == [3]
    assert fn([1, 2, 5, 2, 3], 5) == [4]

test(target_indices)