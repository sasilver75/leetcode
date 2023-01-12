"""
Intended to be my definitive, correct versions
of the mergesort algorithm
"""


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_partition = merge_sort(nums[:mid])
    right_partition = merge_sort(nums[mid:])

    return merge(left_partition, right_partition)


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


print(merge_sort([3,1,6,3,5,7,8,3]))
print(merge_sort([1,3,51,2,54]))
print(merge_sort([]))