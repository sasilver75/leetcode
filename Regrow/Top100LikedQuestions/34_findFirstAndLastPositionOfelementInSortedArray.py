"""
Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in non-decreasing (read: ASC)
order, find the starting and ending position of a given target value

If target is NOT FOUND in the array, return -1, -1
"""

"""
Thinking: 

=== Naivest ===
Just scan linearly across the whole thing, noting the first and last occurrence
of the number.
This will take O(N) time.

=== Naive ===
So the naive thing that you could do here is do a binary search for the 
occurrence of the target number.
Maybe we then linearly probe/scan for the first/last occurrence, from our 
landing site.
Say this lands you at an occurrence in the middle of the span of occurrences -- 
or even that the entire list is the target element. 
This will take O(N) time.

=== Smart === 
Do a binary search for the leftmost occurrence
Do a binary search for the rightmost occurrence


Obviousuly for all of these you have to handle the case where it isn't found

"""


def first_and_last_naivest(nums: list[int], target: int) -> list[int]:
    first = -1
    last = -1
    for idx, num in enumerate(nums):
        if num == target:
            if first == -1:
                first = idx
            last = idx
    print(f"first_and_last_naivest: {first, last}")
    return [first, last]


def first_and_last_naive(nums: list[int], target: int) -> list[int]:
    if not nums:
        print(f"first_and_last_naive {-1, -1} from no nums")
        return [-1, -1]

    l, r = 0, len(nums) - 1
    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = nums[mid_idx]

        if target < mid_val:
            r = mid_idx - 1
        elif target > mid_val:
            l = mid_idx + 1
        else:
            break

    # mid_idx might have value
    if nums[mid_idx] != target:
        print(f"first_and_last_naive {-1, -1} from not found")
        return [-1, -1]

    l, r = mid_idx, mid_idx
    while l -1 >= 0 and nums[l-1] == target:
        l -= 1
    while r + 1 < len(nums) and nums[r+1] == target:
        r += 1

    print(f"first_and_last_naive {l, r} from search")
    return [l, r]

def first_and_last(nums: list[int], target: int) -> list[int]:
    if len(nums) == 0:
        return [-1, -1]

    # Step 1: Binary Search for Leftmost
    l, r = 0, len(nums) - 1

    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = nums[mid_idx]

        if target <= mid_val:
            # Will this get us the answer, or do we need to keep track of the last
            r = mid_idx - 1
        else:
            l = mid_idx + 1

    # Did we even find our target?
    if nums[l] != target:
        return [-1, -1]

    # Note use of l here for left side search
    left = l

    # Step 2: Binary Search for Rightmost
    l, r = 0, len(nums) - 1

    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = nums[mid_idx]

        if target >= mid_val:
            # Will this get us the answer, or do we need to keep track of the last
            l = mid_idx + 1
        else:
            r = mid_idx - 1

    # Note use of r here for right side search
    right = r

    return [left, right]



def test(fn):
    assert fn([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert fn([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert fn([], 0) == [-1, -1]


# test(first_and_last_naivest)
# test(first_and_last_naive)
test(first_and_last)
