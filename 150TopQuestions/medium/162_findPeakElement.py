"""
Find Peak Element

A peak element is an element that is trictly gerater than its neighbors

Given a 0-indexed integer araray nums, find a peak element, and then
return its index.

If the array contains multiple peaks, return the index of ANY of its peaks.

You may imagine that elements on the "border" of the list are always considered
to be strictly greater than a neighbor that is outside of the array.

Catch:
*** YOU MUST WRITE AN ALGORITHM THAT RUNS IN O(LOGN) TIME! ***
"""


"""

"""

def find_peak_dumb(nums: list[int]) -> int:
    for idx, num in enumerate(nums):
        prev = nums[idx-1] if idx-1 >= 0 else -float('inf')
        next = nums[idx+1] if idx+1 < len(nums) else float('inf')
        if (prev < num > next):
            return idx

    return None

"""
Now how could I possibly do this in LOG(N) time?
LOG(N) to me feels like it involves a binary search or something that breaks 
the list down into halves.

I can't really do any preprocessing of the list, since that would likely take
O(N) time.

So given an unsorted list of numbers, how would I know where to recurse if I
tried to do some sort of binary search on the numbers?

Example case:

[1,2,3,1,1,0,0]

So we find the middle element at index i.

[1,2,3,1,1,0,0]
       ^
And we look (let's say) at the ith and i-1th element to determine:
"At i, are we going uphill or downhill?"

If nums[i] <= nums[i-1], let's call that "downhill"
If nums[i] > nums[i-1], let's cal that "uphill"

We want to find SOME peak (not the global one, just SOME peak)

Does htis even make sense? Can there be a counter example?



[1,5,-2,0,1,1,1]

"""



"""
The solution below works to find A peak, but it doesn't work
if we assume that there are going to be PLEATEAUS in the geography 
(see example 3 that I cooked up). 

The strategy is a binary search where we just "go uphill"
"""

def findPeakElement(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l+r) // 2

        if (nums[mid-1] if mid-1>=0 else float('-inf')) < nums[mid] > (nums[mid+1] if mid+1 < len(nums) else float('-inf')):
            return mid

        if nums[mid] < (nums[mid+1] if mid+1 < len(nums) else float('inf')): # If we're going uphill
            l = mid+1 # Look uphill
        else:
            r = mid # Look downhill

    # Should never hit this :)
    return None


def test(fn):
    assert fn([1, 2, 3, 1]) == 2 #idx2 == 3
    assert fn([1, 2, 1, 3, 5, 6, 4]) in [1,5] #idx1/5 == 2,6
    # assert fn([1,5,-2,0,1,1,1]) == 1

# test(find_peak_dumb)
test(findPeakElement)