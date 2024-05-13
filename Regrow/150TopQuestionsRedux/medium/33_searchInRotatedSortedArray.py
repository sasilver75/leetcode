"""
Search in Rotated Sorted Array

There is an integer array `nums` sorted in ASCENDING order, with DISTINCT
values!

Prior to being passed to your function, nums is possible ROTATED at some unknown
pivot index, such that
[0,1,2,4,5,6,7] is rotated at pivot index 3, becoming
[4,5,6,7,0,1,2]

Given the array nums AFTER the possible rotation, and an integer
target, return the INDEX of the target if it's in nums, or -1 if it's not
in nums.
"""


def search_naive(nums: int, target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


"""
If it were just a normal sorted array, it would be nice to binary search.
But the rotation complicates things :(
The rotation pretty much "splits" the previously sorted list into TWO
sorted lists coexisting in the last list structure.

Visual example of [4,5,6,7,0,1,2]
       @
      @@
     @@@
    @@@@
    @@@@
    @@@@  @
    @@@@_@@
    
It would be nice if we could somehow performantly search for the rotation point,
and then do a binary search on each side
          
          
          /
         /  /
        /  /
        
            /
         / / 
        / /
        
How could we binary search for the rotation point?
Let's use [4,5,6,7,0,1,2] as an example

Select the middle index, get the value: 7
        [4,5,6,7,0,1,2]
         l     ^     r

If we then look at the rightmost element @ r

Is nums[r] > nums[mid]?
This would indicate that the rotation point is to the left, since the right side is ascending
Otherwise, the rotation point is to the right.

The condition that we're looking for, in a rotation point is a local minima

"""


def search(nums: int, target: int) -> int:
    # 1) Search for Rotation Point
    l, r = 0, len(nums) - 1
    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = nums[mid_idx]

        # The pivot index is guaranteed to not be an end index
        if nums[mid_idx - 1] > mid_val < nums[mid_idx + 1]:
            break

        if mid_val < nums[r]:
            r = mid_idx - 1
        else:
            l = mid_idx + 1

    # mid_idx is the rotation index

    # 2) Binary Search through each (you can check ranges of start/end to determine which to search
    # Which of the two ASC subarrays should our value be in, based on their range?
    # [4,5,6,7,0,1,2]
    print(f"For {nums} the mid_idx is {mid_idx}")
    for l, r in [(0, mid_idx - 1), (mid_idx, len(nums) - 1)]:
        while l <= r:
            mid_idx = l + (r - l) // 2
            mid_val = nums[mid_idx]

            if target > mid_val:
                l = mid_idx + 1
            elif target < mid_val:
                r = mid_idx - 1
            else:
                return mid_idx

    return -1


"""
Retro: I was having problems because 
"""


def test(fn):
    assert fn([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert fn([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert fn([1], 0) == -1


test(search_naive)
test(search)
