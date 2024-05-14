"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
 and two integers m and n, representing the number of elements in nums1 and nums2 
 respectively.

 [0, 1, 1, 2, 3, _, _, _] m = 4  (m+n=7)
 [1 ,2 ,3] n = 3

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but should instead be 
stored INSIDE the array nums1! To accommodate this, nums1 has a length of m+n, where the 
first m elements denote the elements that hsould be merged, and the last n elements
are set to 0 and should be ignoreed. Nums 2 has a length of n.
"""

def merge_sorted_arrays(nums1: list[int], m, nums2: list[int], n) -> None:
    """
    Insight:Attempting to move two pointers from left to right on both arrays
    leads to a lot of annoying shuffling nad pointer management

    If we instead start with two pointers at the BACK of each of the list
    and move them leftwards, it becomes much more like a sorted list merge
    operation with two pointers (plus an additional one keeping the current insertion point)
    """
    i = m - 1  # nums1 index for comparison numbers
    j = len(nums2) - 1  # nums2 index for comparison numbers
    k = len(nums1) - 1  # Tracking Insertion index in nums1

    while i>= 0 and j>=0:
        # Since we're packing nums1 from right to left (in reverse)
        # we want the higher value
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    
    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    print(nums1)
        




cases = (
    ([1,2,3,0,0,0], 3, [2,5,6], 3),  # 1,2,2,3,5,6
    ([1], 1, [], 0), # 1
    ([0], 0, [1], 1) # 1
)

for nums1, n, nums2, m in cases:
    merge_sorted_arrays(nums1, n, nums2, m)