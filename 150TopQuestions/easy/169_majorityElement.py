"""
Majority Element

Given an array nums of size n, return the MAJORITY element.

The majority element is the element that appears MORE THAN Floor(N/2) times.
You may assume that a majority element ALWAYS exist in the array.
"""


"""
Thinking:
Okay, given that we know that there IS a majority element, a simple thing we could do would be to reduce
across the list of nums, creating a hastable of number counts. Then we'd scan through the keys in the hashtable
and determine the key with the largest count.
That would be an O(N) time and O(N) space solution.

Is there a way that we could use constant O(1) memory?
If we sorted the elements, then we know that the center index (vaguely) would contain the majority element.
That would be an O(NlogN) time and O(1) space solution, if the sort was done in place (mutatively).
"""

def majority_element_ht(nums: list[int]) -> int:
    counts = {} # Could also use collections.defaultdict
    for num in nums:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

    max_num = None
    max_count = float('-inf')

    for num, count in counts.items():
        if count > max_count:
            max_count = count
            max_num = num

    return max_num

def majority_element_sort(nums: list[int]) -> int:
    sorted = merge_sort(nums) # Pretend this is in-place please :)
    mid = len(sorted) // 2
    return sorted[mid]


def merge_sort(nums: list[int]):
    if len(nums) <= 1:
        return nums

    mid = len(nums)//2

    return merge(
        merge_sort(nums[0:mid]),
        merge_sort(nums[mid:])
    )

def merge(l1: list[int], l2: list[int]) -> list[int]:
    acc = []
    p1, p2 = 0, 0

    while p1 < len(l1) and p2 < len(l2):
        e1 = l1[p1]
        e2 = l2[p2]
        if e1 <= e2:
            acc.append(e1)
            p1 += 1
        else:
            acc.append(e2)
            p2 += 1

    acc.extend(l1[p1:])
    acc.extend(l2[p2:])

    return acc

assert majority_element_ht([3, 2, 3]) == 3
assert majority_element_ht([2, 2, 1, 1, 1, 2, 2]) == 2


print(merge_sort([3,2,1,5,4,4]))
assert majority_element_sort([3, 2, 3]) == 3
assert majority_element_sort([2, 2, 1, 1, 1, 2, 2]) == 2


