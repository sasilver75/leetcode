"""
Search in Rotated Sorted Array

There's an integer array nums sorted in ascending order (with distinct values)

Prior to being passed to your function, nums is POSSIBLY ROTATED an unknown pivot index k (1 <= k <= nums.length)
- The list may be rotated, or it may not be rotated.

For example, [0,1,2,4,5,6,7] might rotated at pivot index 3 and become [4,5,6,7,0,1,2]
                    ^

Given the array nums AFTER the POSSIBLE rotation, and an integer `target`, return the index of target if it is in nums, or -1 if it is not in nums.

** You must write an algorithm with O(NLogN) run time complexity
"""

"""
Thinking: Again, this is fine the point of rotation/discontinuity (if it exists), and then do a binary search for values within the resulting 


  /
 /
/
     /
    /
   /
   
1. Search for the point of discontinuity
2. Binary search in nums[:point] and nums[point:] for target, if there is a point of discontinuity; else just bsearch through nums
"""


def binary_search_for_point_of_discontinuity(nums: list[int]) -> int:
    """Given a list that may contain a rotation, find the index of rotation"""
    if len(nums) <= 1:
        return -1  # Signaling no rotation

    # Now the search for the point of rotation (that exists) can proceed
    l, r = 0, len(nums) - 1

    while l <= r:
        # Check the current l:r+1 span: Is it ASC? then the point of rotation is l.
        if nums[l] < nums[r]:
            # No discontinuity; return l (Check; if l == 1, then return -1, since there's no effective rotation)
            return l if l != 0 else -1

        # There is a point of discontinuity; is it in l:mid_idx, or mid_idx:r+1?
        mid_idx = l + (r - l) // 2

        if nums[mid_idx - 1] > nums[mid_idx] < nums[mid_idx + 1]:
            return mid_idx
        elif nums[l] > nums[mid_idx - 1]:
            r = mid_idx - 1
        else:
            l = mid_idx + 1

    # Not sure that we should ever hit this
    return l


assert binary_search_for_point_of_discontinuity([3, 4, 5, 1, 2]) == 3
assert binary_search_for_point_of_discontinuity([4, 5, 6, 7, 0, 1, 2]) == 4
assert binary_search_for_point_of_discontinuity([11, 13, 15, 17]) == -1
assert binary_search_for_point_of_discontinuity([10, 11, 7, 8, 9]) == 2  # This was returning 10, which is incorrect.


def binary_search(nums: list[int], l: int, r: int, target: int) -> int:
    """Return the index of target's unique occurrence in nums, or -1"""

    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = nums[mid_idx]

        if target < mid_val:
            r = mid_idx - 1
        elif target > mid_val:
            l = mid_idx + 1
        else:
            return mid_idx

    return l if l < len(nums) and nums[l] == target else -1


assert binary_search([1, 4, 6, 8, 21, 75], 0, 5, 6) == 2
assert binary_search([1, 4, 6, 8, 21, 75], 0, 5, 1) == 0
assert binary_search([1, 4, 6, 8, 21, 75], 0, 5, 75) == 5
assert binary_search([1, 4, 6, 8, 21, 75], 0, 5, 15) == -1

"""
This one got really sloppy, but it works. The point is to just determine the rotation point (if it exists) and then to
binary search through each of the lists (if there are two).
"""

def search(nums: list[int], target: int) -> int:
    point = binary_search_for_point_of_discontinuity(nums)

    # If no effective rotation, search list
    if point == -1:
        return binary_search(nums, 0, len(nums)-1, target)

    # Search left and right spans
    left_result = binary_search(nums, 0, point-1, target)
    return left_result if left_result != -1 else binary_search(nums, point, len(nums)-1, target)

"""
There's a way to do it where we don't have to search for the rotation point ahead of time.
"""
def search_smarter(nums: list[int], target:int) -> int:
    """Return the index of target in nums if it exists, else -1"""
    l, r = 0, len(nums) - 1

    while l <= r:
        mid_idx = l + (r - l) // 2

        # Is the mid_idx == target?
        if nums[mid_idx] == target:
            return mid_idx # Return the index we found it at

        # Is the left half sorted?
        if nums[mid_idx] > nums[l]:
            # left half is sorted. Could target possibly be in it?
            if nums[l] <= target < nums[mid_idx]:
                # Target could be in it; search in the left side
                r = mid_idx - 1
            else:
                # left half is sorted but target is not in it; search teh right side
                l = mid_idx + 1
        else:
            # right half is sorted. Could target possibly be in it?
            if nums[mid_idx] < target <= nums[r]:
                l = mid_idx + 1
            else:
                # right half is sorted but target is not in it; search the left side
                r = mid_idx - 1

    # We didn't find it :(
    return -1


def test(fn):
    # Rotation
    assert fn([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert fn([4, 5, 6, 7, 0, 1, 2], 3) == -1

    # No Rotation
    assert fn([1], 0) == -1
    assert fn([1, 2, 3], 2) == 1


for f in [
    search,
    search_smarter
]:
    test(f)
