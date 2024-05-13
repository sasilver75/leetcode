"""
Given two integer arrays nums1 and num2s, return an array of their
intersecting elements.
Each element in the result MUST appear as many times as it shows in BOTH arrays,
and you must return the result in any order
"""


"""
Must appear as many times as it shows in BOTH arrays!
Meaning if X occurs 3 times in nums1 and 5 times in num2, we have XXX in the 
intersection array

nums1: YYY
nums2: [No Ys]
intesectoin: [No Ys]

nums1: ZZZZ
nums2: ZZZZZ
intersection: ZZZZ 
"""
def intersection(nums1: list[int], nums2:list[int]) -> list[int]:
    """
    O(N) time and O(N) space
    """
    counts1 = {}
    counts2 = {}
    for num in nums1:
        if not num in counts1:
            counts1[num] = 0
        counts1[num] += 1
    for num in nums2:
        if not num in counts2:
            counts2[num] = 0
        counts2[num] += 1

    common = []
    for letter in counts1:
        common_count = min(counts1[letter], counts2.get(letter, 0))
        while common_count:
            common.append(letter)
            common_count -= 1

    print(common)
    return common


assert intersection([1,2,2,1], [2,2]) == [2,2]
assert intersection([4,9,5], [9,4,9,8,4]) == [4,9]

# -----

"""
What if the given array is already sorted?
"""

def intersection_on_sorted(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    If the given array is sorted, we still can't do better
    than O(N) time... but we can do better than O(N) memory! We can do O(1)!

    2 2 4 5 5 8 9 9 9 9--> "higher" because it starts with a higher number
    0 1 2 2 3 4 5 5 --> "lower" because it starts with a lower number
    """
    intersection = []
    p1, p2 = 0, 0
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            intersection.append(nums1[p1])
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1

    return intersection


assert intersection_on_sorted([2,5,6,6,7,8,9], [6,6,8]) == [6,6,8]
assert intersection_on_sorted([0,0,1,2,3], [0, 2, 3]) == [0,2,3]

"""
Q:What if num1's size is small compared to num2's size?
Which of our algorithms are better?

--> I think they're both still O(N) time in the wost case, meaning every
 element needs to be visited.
"""''

"""
q: What if the elements of nums2 are stored on disk, and memory
is limited such that you cannot load all elements into the memory at once?

In that case, the two pointer algorithm is going to be better -- because
while they're both O(N) time, the O(N) memory requirement of the first solution
(using an in-memory hashtable for each) isn't going to work, because 
we just said that we can't fit the entire thing in memory.
"""

