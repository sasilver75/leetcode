"""
Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection!

Each element in the result must appear as many times as it shows in both arrays,
and you may return the result in any order.
"""

"""
Thinking:

The easy way I think would be to do character count dicts for each list -- 
counts1 and counts2.
And then you can iterate through the keys of EITHER of the counts dicts and 
append the min(counts1[key], counts2[key]) to the acc.
"""


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    acc = []
    counts1, counts2 = {}, {}

    for nums, counts in zip((nums1, nums2), (counts1, counts2)):
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

    for num in counts1:
        acc.extend([num] * min(counts1.get(num, 0), counts2.get(num, 0)))

    return acc


"""
Is there any way that we could do this without using O(N) space?
Well... not really -- since the accumulator will be, in the worst case, length N...

But we COULD in-place sort them, and then scan through each with a pointer on
each sorted list, appending to an accumulator list.
"""

assert intersection([1, 2, 2, 1], [2, 2]) == [2, 2]
assert intersection([4, 9, 5], [9, 4, 9, 8, 4])
