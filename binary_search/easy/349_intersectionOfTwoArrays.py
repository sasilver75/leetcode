"""
Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection!

Each element in the result must be UNIQUE, and you may return the result in any order
"""


def intersection_naive(nums1: list[int], nums2: list[int]) -> list[int]:
    # O(N) time and O(N) space
    nums1set = set(nums1)
    nums2set = set(nums2)
    return list(nums1set.intersection(nums2set))


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    # Instead of using two sets, we could do a binary search in nums2 for every element
    # in nums1... but we also have to check that it isn't already in our accumulator, which would
    # be a set... So we can still have O(N) memory, but now it's O(NlogN) time... Not a good tradeoff
    pass


def test(fn):
    assert fn([1, 2, 2, 1], [2, 2]) == [2]
    assert fn([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]

test(intersection_naive)