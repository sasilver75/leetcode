"""
Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is MISSING from the array
"""

"""
So there's only one number that's "missing"
We could:
    0) Check if len == 1: If so, return nums[0]+1
    1) Sort the nums
    2) Scan across 
        * Start at i=1, look backwards by one index and see if it's ONE away.
        * If it's more than one away, the missing number is nums[i]-1
    3) If no "hole" detected, it's nums[-1] + 1
"""


def missing(nums: list[int]) -> int:
    sorted = merge_sort(nums)
    i = 1
    while i < len(sorted):
        # If the previous number was different, but there's a "gap" between
        if (sorted[i-1] != sorted[i]) and (sorted[i-1] + 1 != sorted[i]):
            # return what the "gap" number is
            return sorted[i] - 1
        i += 1

    return nums[-1] + 1 if nums else 0 # Arbitrary as to what to do if nums is empty


def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(l1: list[int], l2: list[int]) -> list[int]:
    merged = []
    p1 = 0
    p2 = 0
    while p1 < len(l1) and p2 < len(l2):
        e1 = l1[p1]
        e2 = l2[p2]
        if e1 <= e2:
            merged.append(e1)
            p1 += 1
        else:
            merged.append(e2)
            p2 += 1
    merged.extend(l1[p1:])
    merged.extend(l2[p2:])
    return merged


assert missing([3,0,1]) == 2
assert missing([0,1]) == 2
assert missing([9,6,4,2,3,5,7,0,1]) == 8