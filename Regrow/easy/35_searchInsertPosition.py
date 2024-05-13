"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index
where it WOULD be if it were inserted in order.

Try to write this in O(logn) complexity
"""
import math


def linearSearchAttempt(nums: list[int], target:int) -> int:
    for idx, val in enumerate(nums):
        if val >= target:
            return idx
    return len(nums)


def binarySearch(lst: list, target: int):
    """Returns the index of the target value ... or the index of where it ought to be in a sorted list"""
    l, r = 0, len(lst) - 1

    while l <= r:
        # Determine middle index + value -> Compare to index
        mid = (l+r) // 2
        mid_v = lst[mid]
        if mid_v == target:
            return mid
        if mid_v < target:
            # Look right
            l = mid + 1
        else:
            # Look left
            r = mid - 1

    # If we didn't find target, l is where it ought to be! Consider a list of [2] and target of 3. What happens? Yep.
    return l

def binarySearchTwo(lst: list[int], target: int) -> int:
    # Just doing it again for muscle memory.
    l, r = 0, len(lst) - 1

    while l <= r:
        mid = (r + l) // 2
        mid_v = lst[mid]
        if mid_v == target:
            return mid
        elif mid_v > target:
            # Look Left
            r = mid - 1
        else:
            # Look Right
            l = mid + 1

    # here is where, if you weren't looking for the insertion point, you might do something else.
    return l

def test(fn):
    cases = [
        [[[1, 3, 5, 6], 5], 2],
        [[[1, 3, 5, 6], 2], 1],
        [[[1, 3, 5, 6], 7], 4]
    ]
    for case in cases:
        inputs, soln = case
        ans = fn(*inputs)
        print(f"Inputs: {inputs}")
        print(f"ans: {ans}")
        print(f"correct: {ans == soln} \n")

# test(linearSearchAttempt)
test(binarySearch)