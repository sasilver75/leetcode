"""
Missing Number

Given an array nums containing n distinct numbers in the range
[0, n], return the only number in the range that's missing from the array.
"""


def missing_number(nums: list[int]) -> int:
    # O(N) time and O(N) Space
    n = len(nums)  # All numbers should be in [0, n]
    unseen = set(range(0, n+1))

    for num in nums:
        unseen.remove(num)

    return next(iter(unseen))


def missing_number_space_efficient(nums: list[int]) -> int:
    n = len(nums)
    nums = merge_sort(nums) # Pretend this is in-place and mutative


    if nums[0] != 0:
        return 0

    for i in range(1, n):
        if nums[i] - nums[i-1] != 1:
            return nums[i] - 1

    return n


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    return merge(
        merge_sort(nums[0:mid]),
        merge_sort(nums[mid:]),
    )

def merge(l1: list[int], l2: list[int]) -> list[int]:
    acc = []
    p1, p2 = 0, 0

    while p1 < len(l1) and p2 < len(l2):
        e1, e2 = l1[p1], l2[p2]
        if e1 <= e2:
            acc.append(e1)
            p1 += 1
        else:
            acc.append(e2)
            p2 += 1

    acc.extend(l1[p1:])
    acc.extend(l2[p2:])

    return acc



assert missing_number([3, 0, 1]) == 2
assert missing_number_space_efficient([3, 0, 1]) == 2

assert missing_number([0, 1]) == 2
assert missing_number_space_efficient([0, 1]) == 2

assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
assert missing_number_space_efficient([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
