"""
Find Minimum in Rotated Sorted Array (Medium)

Suppose an array of length n sorted in ascending order is rotated between 1 and N times
For example, the array
[0,1,2,3,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times
    [0,1,2,3,4,5,6,7] if it was rotated 7 times

Given the sorted rotated array of UNIQUE ELEMENTS, return the MINIMUM element of this array!
You must use an algorithm that runs in O(LogN) time

"""

"""
So I think the instructions are a little bit of a giveaway in terms of what we need to do (it's a binary search in LogN time)

The trick here is that the sorted array has been rotated, such that there's (possibly) a rotation point



    /
   /
  /
 /
/    
       /
      /
     /
    /


For example


OOOO
OOOOO
OOOOOO
OOOOOOOO
|
0
00

But it's possible that there's effectively no need to consider this rotation, if the list of length n was rotated n times,
meaning it arrived back in its origina shape

So:
1. Determine if the list has been "effectively" rotated
    - Determination method: If nums[0] < nums[-1] there is no rotation
    
2. Search through list(s)
    - If no rotation, just bsearch the list
    - If rotation, we ned to find where the rotation is, using binary search
        - Once we have the rotation point (say, 0, in [4,5,6,7,0,1,2]), then we can binary search twice in [0:point], [point:]
        
        
OOPS! I'm overcomplicating this.
It seems like the point of discontinuity is actually the minimum, using my diagrams above. So we're really searching for this point of discontinuity.

Given an index, 
"""


def find_min(nums: list[int]) -> int:
    l, r = 0, len(nums)-1

    while l <= r:
        # check to see if there's no rotation at all
        if nums[l] < nums[r]:
            return nums[l]  # No rotation; first element is min

        print(f"{l =}{r =}")
        mid_idx = l + (r-l)//2
        mid_val = nums[mid_idx]

        """"
        Future Sam: I don't actually think this is right? What if the mid_idx were the rotation point? Would we find it? 
        Adding a test case.
        """
        # Is there a discontinuity on the left? On the right? If there isn't one, it must be the leftmost element!
        if mid_val < nums[mid_idx-1]  and mid_val < nums[mid_idx+1]:
            return mid_val
        elif mid_val < nums[l]:
            # Discontinuity on the left; look left
            r = mid_idx - 1
        else: # mid_val > nums[r]
            # Discontinuity on the right; look right
            l = mid_idx + 1

    return nums[l]

def test(fn):
    assert fn([3,4,5,1,2]) == 1
    assert fn([4,5,6,7,0,1,2]) == 0
    assert fn([11,13,15,17]) == 11
    assert fn([10,11,7,8,9]) == 7 # This was returning 10, which is incorrect.

test(find_min)