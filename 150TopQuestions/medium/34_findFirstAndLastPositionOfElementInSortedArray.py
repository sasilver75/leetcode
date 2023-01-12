"""
Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in NON-DECREASING order,
find the STARTING and ENDING position of a given TARGET VALUE.

If target is NOT found in the array, return [-1, -1]

** You MUST write an algorithm with O(logn) runtime complexity
"""
from typing import Callable

"""
It's not like you can just do a normal binary search for the value.
I mean let's say that you found the value pretty easily -- then you have
to search for the beginning and end of the value range if it's repeated.

In the case where there are ALL repeats in nums ( [1,1,1,1] ), you'll end
up moving your pointers to (0, len(nums)), which is going to be O(N).

Okay, so why don't we search for like... (target-1) and (target+1) using binary
search? Well... the same problem. In the case where it's [0,0,1,2,2], we'd be
doing the same O(N) thing, in the worst case.

So what we're really doing IS a search for the number, but the condition
that we're looking for isn't just:

if nums[current] == target

it's instead

if nums[current] == target and nums[current - 1] < target
and
if nums[current] == target and nums[current + 1] > target

as edge pieces. We can binary search for each of these, as long as we know
that we're searching for either the left or the right boundary.

I think we could reuse some of the l, r bounds between
"""


def first_and_last(nums: list[int], target: int) -> list[int]:
    first, last = None, None

    # Search for LEFT BOUND
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        mid_v = nums[mid]

        # Match Condition for Left Bound (+ OR in case left bound is 0)
        if mid_v == target and (mid == 0 or nums[mid - 1] < target):
            first = mid
            break

        if mid_v >= target:  # Note the use of >= given that we're looking for left bound
            # Look Left
            r = mid - 1
        else:
            # Look Right
            l = mid + 1

    # Search for RIGHT BOUND
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        mid_v = nums[mid]

        # Target Condition for Right Bound (+ OR in case right bound is len(nums) - 1)
        if mid_v == target and (mid == len(nums)-1 or nums[mid + 1] > target):
            last = mid
            break

        if mid_v <= target:
            # Look Right
            l = mid + 1
        else:
            r = mid - 1

    return [first, last] if (first is not None and last is not None) else [-1, -1]


# -- Test Zone --
def test(fn: Callable):
    assert fn([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert fn([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert fn([], 0) == [-1, -1]
    assert fn([1, 2, 3, 3], 3) == [2, 3]
    assert fn([3, 3, 4, 5], 3) == [0, 1]
    assert fn([4,4,4,4], 4) == [0, 3]


test(first_and_last)
