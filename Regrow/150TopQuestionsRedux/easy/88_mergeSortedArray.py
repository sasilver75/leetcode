"""
Merge Sorted Array

Given two integer arays nums1 and nums2, sorted in NON-DECREASING order, and two integers m and n, representing the number of elements in
nums1 and num2 respectively

MERGE nums1 and num2 into a single sorted array in non-decreasing order.

The final sorted array shouldn't be returned; it should instead be stored INSIDE the array nums1

To accommodate this, nums1 has a length of m+n, where the first m elements denote the elements that should be merged, and the last n elements are
set to 0 and should be ignored.
"""

def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid_idx = len(nums) // 2

    return merge_lists(
        merge_sort(nums[:mid_idx]),
        merge_sort(nums[mid_idx:])
    )

def merge_lists(nums1: list[int], nums2: list[int]) -> list[int]:
    acc = []
    p1, p2 = 0,0
    while p1 < len(nums1) and p2 < len(nums2):
        e1 = nums1[p1]
        e2 = nums2[p2]
        if e1 <= e2:
            acc.append(e1)
            p1 += 1
        else:
            acc.append(e2)
            p2 += 1

    acc.extend(nums1[p1:])
    acc.extend(nums2[p2:])
    return acc

def merge_naive(nums1: list[int], m:int, nums2: list[int], n: int) -> None:
    i = m
    while i < len(nums1):
        nums1[i] = nums2[i - m]
        i += 1
    print(nums1)

    sorted_nums1 = merge_sort(nums1)
    for i in range(len(sorted_nums1)):
        nums1[i] = sorted_nums1[i]



def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    pass


def test(fn):
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    fn(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    nums2 = []
    fn(nums1, 1, nums2, 0)
    assert nums1 == [1]

    nums1 = [0]
    nums2 = [1]
    fn(nums1, 0, nums2, 1)
    assert nums1 == [1]

test(merge_naive)