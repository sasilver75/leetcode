"""
Subsets

Given an integer array `nums` of unique elements, return all possible
subsets (the power set).

The solution MUST NOT CONTAIN ANY DUPLICATE SUBSETS!
 Return the solution in any order.
"""
from typing import Optional

"""
Thinking:
RE subsets:
 "A subset MAY NOT maintain relative ordering of elements and can or cannot be a contiguous part of an array.
 For a set of size n, we can have (2^n) sub-sets in total."
 
 I don't see in the examples any [1,3,2] orderings...
 So it seems like the 
"""
def generate_power_set(nums: list[int]) -> list[list[int]]:
    subsets = []

    def helper(idx: int, built: Optional[list[int]] = None) -> None:
        if built is None:
            built = []

        if idx == len(nums):
            subsets.append(built)
            return

        # Either add or don't add the current element
        helper(idx+1, [*built, nums[idx]])
        helper(idx+1, [*built])

    helper(0)

    return subsets


# -- Test --
def test(fn):
    a1 = fn([1,2,3])
    assert all(lst in a1 for lst in [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
    a2 = fn([0])
    assert all(lst in a2 for lst in [[], [0]])

test(generate_power_set)