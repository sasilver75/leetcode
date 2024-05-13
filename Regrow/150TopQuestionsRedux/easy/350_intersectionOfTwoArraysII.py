"""
Intersection of TWo Arrays II

Given two integer arrays nums1 and num2, return an array
of their intersection.
EAch element in the result must appear as many times as it shows in both
arrays, and you may return the result in ANY order.
"""
import collections


def intersection_naive(nums1: list[int], nums2: list[int]) -> list[int]:
    # Smaller of the two should be used as the counter
    # Larger should be used to count for common elements
    larger = max([nums1, nums2], key=len)
    smaller = nums1 if larger == nums2 else nums2

    # Get char counts of smaller
    counts = collections.defaultdict(int)
    for char in smaller:
        counts[char] += 1

    # Acc, and decrement counts when processing larger
    acc = []
    for char in larger:
        if counts[char] > 0:
            acc.append(char)
            counts[char] -= 1

    """
    You could even further optimizing this by checking whether if any point
    the length of acc has equaled the length of {shorter}, at which point we
    don't need to process the remaining of {larger}. This doesn't change
    asymptotic complexity, but does avoid work.
    """

    print(acc)
    return acc



def test(fn):
    assert fn([1,2,2,1], [2,2]) == [2,2]
    ans = fn([4,9,5], [9,4,9,8,4])
    assert ans in [[4,9], [9,4]]

test(intersection_naive)