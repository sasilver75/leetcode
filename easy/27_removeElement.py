"""
Given a non-sorted integer array nums and an integer val, remove all occurences of val
in nums in-place! The relative order of elements may be changed.

You must instead have the result be placed in the first part of the array nums.
If there are k elements after removing occurrences of val in nums.
It doesn't matter what you leave behind the first k elements.

Return k, nums
Do not allocate extra space -- use O(1) space.
"""

def removeElement(nums: list[int], target:int) -> tuple[int, list[int]]:
    i = 0
    k = 0
    # Walk i across
    # If the ith element is target, double incremenet i and single increment k
    # Else, single incremenet both
    while i < len(nums):
        if nums[i] == target:
            # ith element is the target
            i += 1
        else:
            # ith element is not the target
            nums[k] = nums[i]
            i += 1
            k += 1
    uniq = k
    while k < len(nums):
        nums[k] = "_"
        k += 1
    print(uniq, nums)
    return uniq, nums


    # Black out the remaining elements after k + checkpoint k before

def test(fn):
    assert fn([3, 2, 2, 3], 3) == (2, [2, 2, "_", "_"])
    assert fn([0, 1, 2, 2, 3, 0, 4, 2], 2) == (5, [0, 1, 3, 0, 4, "_", "_", "_"])

test(removeElement)