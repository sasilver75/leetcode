"""
Search in Rotated Sorted Array

There's an integer array nums sorted in ASC order (with distinct values)

Prior to being passed to your function, nums is possibly rotated at an
unknown pivot index k (1 <= k < nums.length)

Such that the resulting array is nums[k], nums[k+1], ... nums[n-1], nums[0], nums[1], ... nums[k-1]
(0-indexed)

For example
[0,1,2,4,5,6,7] might be rotated at idx=3 and become
[4,5,6,7,0,1,2]

Given the array `nums` AFTER the possible rotation, and an integer `target`,
return the INDEX of `target` if it's in nums, or -1.

** YOU MUST WRITE AN ALGORITHM THAT RUNS IN LOGN RUNTIME COMPLEXITY **
"""


def search(nums: list[int], target: int) -> int:
    def find_rotation_index(nums) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid_idx = l + (r - l) // 2
            mid_val = nums[mid_idx]

            if nums[l] < nums[r]:
                # If the whole thing is ASC, then our POR is l
                return l

            # Question to ask here: Are the numbers unique; ie, can there be plateaus? I'm going to assume no for now
            # are we at a discontinuity? Yay!
            if (
                mid_idx - 1 >= 0 and
                nums[mid_idx-1] > mid_val
            ):
                return mid_idx

            # Is there a discontinuity in the left side somewhere
            """
            
                /
               /
              /
             /    /
                 /
            """
            if nums[l] > mid_val:
                r = mid_idx - 1
            else:
                l = mid_idx + 1



    rotation_index = find_rotation_index(nums)

    def b_search(nums: list[int]):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid_idx = l + (r - l) // 2
            mid_val = nums[mid_idx]

            if target < mid_val:
                r = mid_idx - 1
            elif target > mid_val:
                l = mid_idx + 1
            else:
                return mid_idx

        return l if l < len(nums) and nums[l] == target else -1

    left_result = b_search(nums[0:rotation_index])
    right_result = b_search(nums[rotation_index:])

    if left_result > -1:
        return left_result
    elif right_result > -1:
        return rotation_index + right_result
    else:
        return -1


def test(fn):
    assert fn([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert fn([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert fn([1], 0) == -1

test(search)