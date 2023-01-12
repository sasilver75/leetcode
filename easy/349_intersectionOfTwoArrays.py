"""
Given two integer arrays num1 and num2, return an array of their intersection.

Each element in the result must be UNIQUE and you must return the result
in ANY ORDER.
"""

"""
Hmmm...
It'd be trivial I think to do the intersection of two hashsets

I don't think we can do any better on space complexity without losing O(N)
time. We could sort each of the lists on O(NLOGN) in place
"""

def trivial_intersection(arr1: list[int], arr2:list[int]) -> list[int]:
    """O(N) time and O(N) space using a hash set"""
    arr1_set = set(arr1)
    common = set()
    for el in arr2:
        if el in arr1_set:
            common.add(el)
    return list(common)

assert trivial_intersection([1,2,2,1], [2,2]) == [2]
assert trivial_intersection([4,9,5], [9,4,9,8,4]) == [9,4]