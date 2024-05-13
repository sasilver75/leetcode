"""
Search in Rotated Sorted Array

There's an integer array `nums` sorted in ascending order (with DISTINCT values)

Prior to being passed to your function, nums is POSSIBLY ROTATED at some
unknown pivot index `k` (1 <= k < nums.length) such that the resulting
array is

[nums[k], nums[k+1], .... nums[n-1], nums[0], nums[1], ... nums[k-1]   (0-idxed)

For example, [0,1,2,3,4,5,6,7] might be rotated at pivot index 3 and
become [4,5,6,7,0,1,2]

Given the array `nums` AFTER the possible rotation, and an integer `target`,
return the index of `target` if it is nums, or -1 if it is NOT in nums.

*** You MUST write an algorithm with O(LOGN) runtime complexity. ***
"""
from typing import Callable

"""
The interesting thing here is that we can't even really linearly scan over the entire
list to see where the pivot point is... And there isn't a way to do a sort of 
binary search FOR the pivot point -- assuming you picked some middle index and
then did your comparison operation, you wouldn't know whether to recurse left or right.

Given that we HAVE to do this in O(logn) time...
1) I assume that there isn't any real preprocessing of the data that we can do,
since that would likely take O(N) time if we processed the whole `nums`.
2) So we have to binary search IN SPITE of the possibly-rotated list.


    4   5   6   7   0   1   2           search(0) == 4
    
In the above case, looking at the middle index would lead us to recurse in
the wrong direction. So maybe we don't just look for 0... Maybe we first 
look for the pivot point? In this case, it happens to be the same number.

But generally a pivot point would be the number that has a number to the 
left that's GREATER than it.

If we knew the pivot index, then we could do two "normal" binary searches 
on the nums[0:pivot] and nums[pivot:] subarrays.

Okay, so identifying a pivot element is easy once we're looking at it,
but how do we KNOW WHERE TO LOOK for it. Like assuming we look at the middle
element and it's NOT the pivot element, what reason would we have to
look either LEFT or RIGHT?

In the example above, we'd be looking at index=3 (value: 7). The pivot happens
to be to the right. Is there any information that would help us realize this?

What are some truths about a rotated array (in this specific sense?)

* We know that the rotated array starts at some interior index, and then
continues to the END OF THE ARRAY!
* Since the array was sorted before we began, we know that every element in
the rotated ending bit is LESS THAN the element just to the left of the pivot
element... hm...

Let's consider 
    4   5   6   7   0   1   2           search(0) == 4

* So we know that all of the elements in [0,1,2] are less than all of the
elements in [4,5,6,7]. But we really "don't know" at the outset WHEN this
pivoted portion beginnings. We DO know that extends to the end of the list.
So maybe having this value (2) is of interest?
What can we learn from (2)?
* We CAN'T infer how many elements there are in the rotated portion (0,1,2)
* We CAN'T infer how many elements there are in the non-rotated portion

We know that it's going to be a binary search of some sort, right, since it's
going to be O(log(N))?
"""

"""
INSIGHT:
Okay, here it is.

Original
    0   1   2   4   5   6   7
                mid
"Right" side pivot        
    4   5   6   7   0   1   2           search(0) == 4
               mid  ^
"Left" side pivot
    6   7   0   1   2   4   5
            ^  mid
            

If we look at the middle element... and compare it to the first element...
Let's "ASSUME" that the array is in "unpivoted," ASC sorted configuration.
If we compare the middle element to the first element, we would expect
the middle element to be >= the leftmost element!
If the middle element were somehow LESS THAN the left element, then
there must be a pivot somewhere to the LEFT! We could use that to binary 
search for our element, right?
Either:
* Pivot is to the left of mid
* Mid is our element
* Pivot is to the right of mid

"""


# Small Bug in this one
# def search_in_rotated_sorted_array(nums: list[int], target: int) -> int:
#
#     # Phase 1: Search for the pivot point
#     l, r = 0, len(nums) - 1
#
#     while l < r:
#         mid_idx = l + (r - l) // 2
#         mid_value = nums[mid_idx]
#         l_value = nums[l]
#
#         # Check for Pivot
#         if mid_value == target:
#             return mid_idx
#         if mid_value < nums[mid_idx - 1]:
#             pivot_idx = mid_idx
#
#
#         # Now, the interesting twist: The comparison operation!
#         if mid_value < l_value:
#             # Pivot is to the left: Look left
#             r = mid_idx - 1
#         else:
#             # Pivot is to the right: Look right
#             l = mid_idx + 1
#
#     def b_search(nums: list[int], target: int) -> int:
#         l, r = 0, len(nums) - 1
#
#         while l < r:
#             mid_idx = l + (r - l) // 2
#             mid_v = nums[mid_idx]
#
#             if target > mid_v:
#                 l = mid_idx + 1
#             elif target < mid_v:
#                 r = mid_idx - 1
#             else:
#                 return mid_idx
#
#         return -1
#
#     # Phase 2: Search Subarray 1 ([0: pivot_idx])
#     arr_1_result = b_search(0, pivot_idx - 1)
#     if arr_1_result >= 0:
#         return arr_1_result
#
#     # Phase 3: Search Subarray 2 ([pivot_idx:])
#     arr_2_result = b_search(pivot_idx, len(nums) - 1)
#     if arr_2_result >= 0:
#         return arr_2_result
#
#     return -1



# -- Test Zone --

def search_in_rotated_sorted_array(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid_idx = left + (right - left) // 2
        mid_val = nums[mid_idx]

        if mid_val == target:
            return mid_idx

        if mid_val >= nums[left]: # The Left Subarray is Sorted
            if nums[left] <= target <= nums[mid_idx]: # Is the value even in that range?
                right = mid_idx - 1 # Yes
            else:
                left = mid_idx + 1 # No -- Look right instead, even though it isn't sorted!

        else: # The Right Subarray is Sorted
            if nums[mid_idx] <= target <= nums[right]: # Is the value even in that range?
                left = mid_idx + 1 # Yes
            else:
                right = mid_idx - 1 # No -- Look left instead, even though it isn't sorted!

    return -1




def test(fn: Callable):
    assert fn([4, 5, 6, 7, 0, 1, 2], 0) == 4
    # assert fn([4, 5, 6, 7, 0, 1, 2], 3) == -1
    # assert fn([1], 0) == -1

test(search_in_rotated_sorted_array)