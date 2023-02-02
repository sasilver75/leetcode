"""
Jump Game

Given an integer array nums... you're initially positioned at the array's first index, and each element in the array
 represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
The last index is the last element in the list.
"""


def canJump(nums: list[int]) -> bool:
    cache = {}
    def explore(idx: int) -> bool:
        print("Exploring: ", idx)
        # Too Far!
        if idx >= len(nums):
            return False

        # Just Right
        if idx == len(nums) - 1:
            return True

        if idx in cache:
            return cache[idx]


        cache[idx] = any(
            explore(idx+jump_length)
            for jump_length in range(1, nums[idx]+1)
        )
        return cache[idx]

    return explore(0)


def test(fn):
    assert fn([2, 3, 1, 1, 4])
    assert not fn([3, 2, 1, 0, 4])

test(canJump)