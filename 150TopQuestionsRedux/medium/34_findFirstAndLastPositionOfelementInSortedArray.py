"""
Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending
position of a given `target` value.

If target isn't found in the array, return [-1, -1]

It must run in O(NlogN) runtime complexity
"""

def searchRangeNaive(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1, -1]

    for starting_index in range(len(nums)):
          if nums[starting_index] == target:
              break

    if nums[starting_index] != target:
        return [-1,-1]

    ending_index = starting_index
    while ending_index + 1 < len(nums) and nums[ending_index+1] == target:
        ending_index += 1

    return [starting_index, ending_index]


"""
This is going to be two binary searches:
One for the first element in the range of target numbers
One for the last element in the range of target numbers

If the first 
"""
def searchRange(nums: list[int], target:int) -> list[int]:
    if not nums:
        return [-1, -1]

    # 1) Search for starting index of range of target in nums
    l, r = 0, len(nums) - 1
    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = nums[mid_idx]

        if mid_val == target and (mid_idx == 0 or nums[mid_idx-1] < target):
            # We found left edge of range
            break


        # If we're above target or within the range of target
        if mid_val >= target:
            # Look Left
            r = mid_idx - 1
        else:
            # Look Right
            l = mid_idx + 1

    # Did we even find the target in nums?
    if mid_val != target:
        return [-1, -1]

    rangeLeft = mid_idx

    # 2) Search for right edge
    l, r = 0, len(nums) - 1
    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = nums[mid_idx]

        if mid_val == target and (mid_idx == len(nums) - 1 or nums[mid_idx+1] > target):
            # We found left edge of range
            break

        # If we're below or in the target number range, look right
        if mid_val <= target:
            # Look Right
            l = mid_idx + 1
        else:
            r = mid_idx - 1

    rangeRight = mid_idx

    return [rangeLeft, rangeRight]

def test(fn):
    assert fn([5,7,7,8,8,10], 8) == [3,4]
    assert fn([5,7,7,8,8,10], 6) == [-1,-1]
    assert fn([], 0) == [-1,-1]

test(searchRangeNaive)
test(searchRange)