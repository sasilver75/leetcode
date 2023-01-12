"""
Definitive Binary Search

Given a sorted list, find a number in it, returning the index or -1 if n/a
"""
from typing import Callable


def binary_search_recursive(nums: list[int], target: int) -> int:
    def helper(l: int, r: int):
        # Base Case: Down to one element and it isn't target? Oops!
        if not nums:
            return -1
        if l - r == 0 and nums[l] != target:
            return -1

        # Determine midpoint - This method avoids integer overflow possible by (l + r) // 2
        mid_idx = l + (r - l) // 2

        # Determine middle value and return/recurse appropriately
        mid_num = nums[mid_idx]
        if target < mid_num:
            # Recurse Left
            return helper(l, mid_idx - 1)
        elif target > mid_num:
            # Recurse Right
            return helper(mid_idx + 1, r)
        else:
            # Found it
            return mid_idx

    return helper(0, len(nums) - 1)


def binary_search_iterative(nums: list[int], target):
    if not nums:
        return -1

    l, r = 0, len(nums) - 1

    while l <= r:  # <=, not just <!
        mid_i = l + (r - l) // 2
        mid_v = nums[mid_i]

        if target < mid_v:
            r = mid_i - 1
        elif target > mid_v:
            l = mid_i + 1
        else:
            return mid_i

    return -1


def test(fn: Callable):
    assert fn([0, 2, 5, 7, 8, 9, 11, 14, 15, 23], 14) == 7
    assert fn([1, 2, 3, 4], 2) == 1
    assert fn([19, 20, 22], 21) == -1
    assert fn([], 21) == -1


test(binary_search_recursive)
test(binary_search_iterative)

"""
There are some variations on Binary Search that are probably useful to know about:
It can become a little more complex when there are duplicate values in your list of numbers!

Here are some variations:
1) Contains (True or False)
2) Index of FIRST occurrence of a key
3) Index of LAST occurrence of a key
4) Index of least element GREATER than key
5) Index of greatest element LESS THAN key

In each of these cases, the base logic remains the same, but there's
a minor variation in implementation.


"""


def binary_search_contains(nums: list[int], target: int) -> bool:
    """
    1) True or False: Is the target in nums?
    This is just like a "normal" binary search for the index of a target, except
    we return True if we find it, else False.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid_idx = left + (right - left) // 2
        mid_val = nums[mid_idx]

        if target < mid_val:
            # Look Left
            right = mid_idx - 1
        elif target > mid_val:
            # Look Right
            left = mid_idx + 1
        else:
            # We found our target
            return True

    return False


nums = [2, 3, 3, 5, 5, 5, 6, 6]
assert binary_search_contains(nums, 4) == False
assert binary_search_contains(nums, 6) == True
assert binary_search_contains(nums, 3) == True


# ----------

def binary_search_first_occurrence_of_key(nums: list[int], target: int) -> bool:
    """
    2) Index of first occurrence of target
        (And if target is not found, return -1)

    The key is that we binary search like we usually do... but when we
    DO find that mid_val == target, we just _note_ down the index at which
    we've last discovered
    """
    left, right = 0, len(nums) - 1
    last_seen_idx = -1

    while left <= right:
        mid_idx = left + (right - left) // 2
        mid_val = nums[mid_idx]


        if target < mid_val:
            # Look Left
            right = mid_idx - 1
        elif target > mid_val:
            # Look Right
            left = mid_idx + 1
        else:
            # We've found it! Note it + look LEFT (for the FIRST occurrence)
            last_seen_idx = mid_idx
            right = mid_idx - 1

    return last_seen_idx


nums = [2, 3, 3, 5, 5, 5, 6, 6]
assert binary_search_first_occurrence_of_key(nums, 3) == 1
assert binary_search_first_occurrence_of_key(nums, 5) == 3
assert binary_search_first_occurrence_of_key(nums, 4) == -1


# ----------

def binary_search_last_occurrence_of_key(nums: list[int], target: int) -> bool:
    """
    3) Index of last occurrence of target
        - Return -1 if not present
    This is just like 2) -- we do a "normal" binary search for the target
    element, but the difference is that whenever we encounter a cell that has
    the target value, rather than early-returning, we NOTE down the index that
    we're at as the "last_seen_index," and then look RIGHT for the LAST occurrence
    if this target value.
    """
    left, right = 0, len(nums) - 1
    last_seen_index = -1

    while left <= right:
        mid_idx = left + (right - left) // 2
        mid_val = nums[mid_idx]

        if target > mid_val:
            # Look Right
            left = mid_idx + 1
        elif target < mid_val:
            # Look Left
            right = mid_idx - 1
        else:
            # Found it! Note it and then look RIGHT for the LAST occurrence
            last_seen_index = mid_idx
            left = mid_idx + 1

    return last_seen_index


nums = [2, 3, 3, 5, 5, 5, 6, 6]
assert binary_search_last_occurrence_of_key(nums, 3) == 2
assert binary_search_last_occurrence_of_key(nums, 4) == -1
assert binary_search_last_occurrence_of_key(nums, 5) == 5


# ----------


def binary_search_least_greater_than(nums: list[int], target: int) -> bool:
    """
    4) Index (FIRST occurrence) of least integer greater than target
        - Return -1 if target is already the greatest element in nums
    This works similarly to a normal binary search, but when we see that
    we're at a point where we're "to the right of" the target value, we note down
    our current location as the "last known index with value greater than target",
    and then look left. Otherwise, we just look right.
    """
    left, right = 0, len(nums) - 1
    last_seen_greater_than = -1

    while left <= right:
        mid_idx = left + (right - left) // 2
        mid_val = nums[mid_idx]

        if target < mid_val:
            # Target is to our Left; We're GREATER than target, and we want to remember the least_greater_than
            # So note this index down, then look left
            last_seen_greater_than = mid_idx
            right = mid_idx - 1
        elif target > mid_val:
            # Target is to our Right
            left = mid_idx + 1
        else:
            # Found Target; Look right, since we want the last greater than
            left = mid_idx + 1

    return last_seen_greater_than

nums = [2, 3, 3, 5, 5, 5, 6, 6]
assert binary_search_least_greater_than(nums, 2) == 1
assert binary_search_least_greater_than(nums, 5) == 6
assert binary_search_least_greater_than(nums, 3) == 3


# ----------

def binary_search_greatest_less_than(nums: list[int], target: int) -> bool:
    """
    5) Index (LAST occurrence) of greatest integer lesser than target
    """
    left, right = 0, len(nums) - 1
    last_seen_less_than = -1

    while left <= right:
        mid_idx = left + (right - left) // 2
        mid_val = nums[mid_idx]

        if target > mid_val:
            # Target is to the right; we are currently LESS THAN target
            # Note the current index as the last_seen_less_than, and then look right
            last_seen_less_than = mid_idx
            left = mid_idx + 1
        elif target < mid_val:
            # Target is to the left; we are currently GREATER THAN target
            # Look to the left
            right = mid_idx - 1
        else:
            # We're at Target
            # Look to the left
            right = mid_idx - 1

    return last_seen_less_than


nums = [2, 3, 3, 5, 5, 5, 6, 6]
assert binary_search_greatest_less_than(nums, 2) == -1
assert binary_search_greatest_less_than(nums, 5) == 2
assert binary_search_greatest_less_than(nums, 6) == 5

# ----------
