"""
Cantains Duplicate (Easy)

Given an integer array nums, return true if any value appears AT LEAST TWICE in the array, and return FALSE
if every element is distinct
"""

"""
Options (Roughly increasing in goodness):
1. For every element in the array, start a new scan, looking at every other element in the array. Are there any duplicates? O(N^2)
2. Sort the list. For every element in the array, are there adjacent, identical elements? O(NLogN)
3. Use a hash set to keep track fo observed elements. Does our current element already exist in the hash set? If yes, !, if not, add it. O(N)
"""


def contains_duplicate_scan(nums: list[int]) -> bool:
    for base_index in range(len(nums)):
        for comparison_index in range(len(nums)):
            if nums[base_index] == nums[comparison_index] and base_index != comparison_index:
                return True
    return False


def contains_duplicate_sort(nums: list[int]) -> bool:
    if len(nums) == 1:
        return False
    sorted_nums = list(sorted(nums))
    for idx in range(1, len(sorted_nums)):
        if sorted_nums[idx] == sorted_nums[idx - 1]:
            return True
    return False


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def test(fn):
    assert fn([1, 2, 3, 1]) == True
    assert fn([1, 2, 3, 4]) == False
    assert fn([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


for fn in [
    contains_duplicate_scan,
    contains_duplicate_sort,
    contains_duplicate,
]:
    test(fn)
