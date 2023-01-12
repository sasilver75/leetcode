"""
Given an array nums sorted in NON-DECREASING ORDER, remove the duplicates IN-PLACE
such that each unique element appears only once. The relative order should be
the same.

Since you can't change the length of hte array in some languages, you must
instead have the result be placed in the FIRST PART of the array nums.
So if there are k elements after removing duplicates, the first k elements
of nums should hold the final result.
It doesn't matter what you leave BEYOND the first k elements.

Return k after placing the final result in the first k slots of nums
DO NOT allocate extra space for another array. Do this in O(1) space
"""


### [0,1,1,2,3,3,4,5]
###    ik
def removeDuplicatesFromSorted(nums: list[int]) -> tuple[int, list]:
    if not nums or len(nums) == 1:
        return 0, nums
    k = 0
    kth_num = nums[k]
    seek = 1
    # Walking seek across
    while seek < len(nums):
        seekth_num = nums[seek]
        if seekth_num > kth_num: # Compare: Is seek greater than the kth number?
            # If so, k++ and nums[k] = nums[seek]
            k += 1
            nums[k] = seekth_num
            kth_num = seekth_num
        else:
            # Else: increase seek by one
            seek += 1

    uniq = k + 1
    # Any remaining elements after k need to be _s
    while k < len(nums) - 1:
        k += 1
        nums[k] = "_"
    return uniq, nums




def test(fn):
    assert fn([1, 1, 2]) == (2, [1, 2, "_"])
    assert fn([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == (5, [0, 1, 2, 3, 4, "_", "_", "_", "_", "_"])
    assert fn([]) == (0, [])

test(removeDuplicatesFromSorted)
