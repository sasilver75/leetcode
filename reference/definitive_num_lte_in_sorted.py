"""
Given that you have a sorted array of numbers like
(with possible repeating elements)

[0,4,7,9,9,9,12,15,16]

If I ask you "How many numbers in nums are <= K?"
    (Application could be kthSmallestElementInSortedMatrix", asking for "how many elements in this list are lte K"?)

The naive solution would be to BSearch for K in the list, then probe linearly if there are repeats
But we want to improve that linear probing, since that's still O(N) in a list of all-K's.
"""


def b_search_count(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    count = 0
    while l <= r:
        mid = l + (r - l) // 2

        # Considering the current index. If we're currently <= target, then we're either BEFORE target on ON a part of the contiguous target
        # Everything at or before than our L pointer necessarily is less than our target, because the list is sorted
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1

    return l


# -- Test Zone --

assert b_search_count([1, 4, 7, 9, 9, 9, 12, 15, 16], 0) == 0
assert b_search_count([0, 4, 7, 9, 9, 9, 12, 15, 16], 1) == 1
assert b_search_count([0, 4, 7, 9, 9, 9, 12, 15, 16], 4) == 2
assert b_search_count([0, 4, 7, 9, 9, 9, 12, 15, 16], 5) == 2
assert b_search_count([0, 4, 7, 9, 9, 9, 12, 15, 16], 7) == 3
assert b_search_count([0, 4, 7, 9, 9, 9, 12, 15, 16], 8) == 3
assert b_search_count([0, 4, 7, 9, 9, 9, 12, 15, 16], 9) == 6
assert b_search_count([0, 4, 7, 9, 9, 9, 12, 15, 16], 13) == 7
assert b_search_count([0, 4, 7, 9, 9, 9, 12, 15, 16], 16) == 9
assert b_search_count([0, 4, 7, 9, 9, 9, 12, 15, 16], 17) == 9

assert b_search_count([0, 3, 5, 5, 5, 9], 3) == 2
assert b_search_count([0, 3, 5, 5, 5, 9], 5) == 5
assert b_search_count([0, 3, 5, 5, 5, 9], 6) == 5
assert b_search_count([0, 3, 5, 5, 5, 9], 9) == 6
