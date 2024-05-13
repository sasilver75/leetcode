"""
Give an integer array nums of 2n integers, group there integers
into n pairs (a1, b1), (a2,b2), ... (an, bn) such that the sum
of min(a[i], b[i]) for all i is maximized. Return the maximized sum.
"""

"""
O(N)
The dumb thing to do would be to generate all possible pairings
of numbers in nums, and determine the sum of pairs, and then choose
the pairing scheme with the highest sum.

O(NLOGN)
Or you could sort of realize that ...
    Sum means adding up a list of numbers
    The get the lowest sum, we want to add up the list of smallest numbers
    The numbers that we're adding are the pairwise minimum
    So we want to have all the smallest numbers available be the min for each pair
    This means that we'll be pairing up numbers from the "left" side of the sorted list
    with numbers from the "right" side
    To make that easier, we could just walk two pointers down from each side, making pairs while l < r
    
    O(N)
    Is there any way that we could do this in O(N) time?...
"""

"""
UH OH
Fuck I accidentlally kind of read that wrong

It was that the Sum of the MIN(pair) was MAXIMIZED
What does it mean to maximize the sum of mins?

Let's look at some exampls
[1,2,3,4] == 4, apparently
Pairs would include
(1,2), (3,4) = 1 + 3 = 4
(1,3), (2,4) = 1 + 2 = 3
(1,4), (2,3) = 1 + 2 = 3
(2,3), (1,4) = 2 + 1 = 3
(2,4), (1,3) = 2 + 1 = 3
(3,4), (1,2) = 3 + 1 = 4            ~~~ At least in this example, the max was reached when we did adjacent values in pairs

Yep, that worked.
So what's the idea here?
Is it that we don't want to "waste" a high number by pairing it with a low number? That makes sense to me.
The opposite of pairing with the further away number would be pairing with the closest number (in sorted order) -- its sibling :)
"""

def partition(nums: list[int]) -> int:
    if not nums:
        return 0

    sorted = merge_sort(nums)
    pairs = []

    for i in range(0, len(sorted), 2):
        pairs.append((sorted[i], sorted[i+1]))

    sum = 0
    for pair in pairs:
        sum += min(pair)
    return sum



def merge_sort(nums: list[int]):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    return merge(
        merge_sort(nums[0:mid]),
        merge_sort(nums[mid:])
    )

def merge(nums1: list[int], nums2: list[int]) -> list[int]:
    acc = []
    p1, p2 = 0, 0

    while p1 < len(nums1) and p2 < len(nums2):
        e1, e2 = nums1[p1], nums2[p2]
        if e1 <= e2:
            acc.append(e1)
            p1 += 1
        else:
            acc.append(e2)
            p2 += 1

    acc.extend(nums1[p1:])
    acc.extend(nums2[p2:])

    return acc




"""
[1,4,3,2] --> 4
(1,4), (2,3) -> 1 + 2 = 3
"""
assert partition([1,4,3,2]) == 4
assert partition([6,2,6,5,1,2]) == 9