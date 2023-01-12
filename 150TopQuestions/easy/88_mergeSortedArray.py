"""
Merge Sorted Array

You are given two integer arrays nums1 and num2s, sorted in NON-DECREASING
order.

Merge nums1 and nums2 into a single array sorted in non-decreasing order

The final sorted array should not be returned by the function, but should
instead be stored INSIDE the array nums1!

To accommodate this, nums1 has a length of m + n, where the first m elements
denote the elements that should be merged, and the last n elements are set
to 0 and should be ignored. nums2 has a length of n.
"""

"""

        i   k
    1   2   3   3   5   6       2   5   6
                                j

    Insight: attempting to move two pointers from left to right on both
    arrays leads to a lot of annoying shuffling and pointer management.

    If you instead start with two pointers at the BACK of each of the two
    lista and move them leftwards, it becomes much more like a sorted list
    merge operation with two pointers (plus an additional one keeping track of 
    the current insertion point)
"""

def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    i = m - 1 # nums1 index
    j = len(nums2) - 1 # nums2 index
    k = len(nums1) - 1 # insertion index in nums1

    while i >= 0 and j >= 0:
        # Since we're packing nums1 from right to left, we want the higher value
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # I don't believe you actually have to do this for i (nums1) -- Nope! You don't
    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    print(nums1)
    return nums1








assert merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
assert merge_sorted_array([1], 1, [], 0) == [1]
assert merge_sorted_array([0], 0, [1], 1) == [1]  # See that m is 0
