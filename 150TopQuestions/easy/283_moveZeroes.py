"""
Move Zeroes
Given an integer array nums, move all 0s to the END of it, while maintaining the relative
order of all of the non-zero elements!

Note that you must do this IN-PLACE without making a copy of the array

Ex.

[2, 0, 1, 0, 3, 12]  -->  [2, 1, 3, 12, 0, 0]

[0] --> [0]

"""

"""
Thinking:
Okay, we're moving... and we encounter a zero. We could bubble it to the end of the array!
And then continue moving on.

This would be O(N^2) time in the worst case

Would there be an easier thing we could do with a second pointer?
"""

def move_zeroes(nums: list[int]) -> list[int]:
    # O(N^2) time and O(1) space
    for idx, num in enumerate(nums):
        if num == 0:
            swap_to_end(nums, idx)

    print(nums)
    return nums

def swap_to_end(nums, idx):
    if idx >= len(nums) - 1:
        return nums

    tmp = nums[idx]
    nums[idx] = nums[idx + 1]
    nums[idx + 1] = tmp

    swap_to_end(nums, idx+1)

# -----------------
def move_zeroes_clever(nums: list[int]) -> list[int]:
    # O(N) time and O(1) space
    """
    The idea is that we have two pointers -- a fast one, and a slow one.
    Everything at/behind the slow one should be zero-less. The fast one should seek, looking for values that it can swap with zeroes.
    The slow pointer should be seeking for the next zero (but shouldn't pass the fast pointer)

    The key is that they both start at the beginning and move at the same speed.
    """
    slow = 0
    for fast, num in enumerate(nums):
        # Check Swap Condition
        if nums[fast] != 0 and nums[slow == 0]:
            nums[fast], nums[slow] = nums[slow], nums[fast]

        # If needed (slow is not on a 0), advance slow
        if nums[slow] != 0:
            slow += 1

        # (Implicitly, advance fast every frame)

    print(nums)
    return nums


# -----------------

assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeroes([0]) == [0]

assert move_zeroes_clever([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeroes_clever([0]) == [0]
