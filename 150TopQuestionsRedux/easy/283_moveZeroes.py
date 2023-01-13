"""
Move Zeroes

Given an integer array `nums`, move all `0`'s to the END of it while maintaining
the relative order of the NON-ZERO elements.

Note that you must do this IN PLACE, without making a copy of the array!
"""

"""
[0,1,0,3,12] --> [1,3,12,0,0]

The idea is that we have TWO pointers -- a FAST one and a SLOW one.

Everything at/behind the slow one should zero-less.
The fast one should seek, looking for non-zero values that it can swap with zeroes

The key is that they both start at the beginning and move at the same speed.
"""


def move_zeroes(nums: list[int]) -> list[int]:
    slow = 0
    for fast, num in enumerate(nums):
        # Check for swap condition
        if num != 0 and nums[slow] == 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]

        if nums[slow] != 0:
            slow += 1

        # Implicitly, we advance fast every iteration of the for loop
    return nums




assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeroes([0]) == [0]
