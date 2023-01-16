"""
Jump Game

Given an integer array `nums`, you're initially positioned at the array's first index, and each element in the array represents your
maximum jump length at that position

Return TRUE if you can even reach the last index, or FALSE otherwise
"""


def can_reach(nums: list[int]) -> bool:

    def recursive_explorer(idx: int) -> bool:
        if idx >= len(nums):
            # Base Case: Overshot
            return False
        if idx == len(nums) - 1:
            # Base Case: Arrived at Goal
            return True

        # Using DFS to explore options
        return any(
            recursive_explorer(idx+jump_size)
            for jump_size in range(1, nums[idx] + 1)
        )

    return recursive_explorer(0)


def test(fn):
    assert can_reach([2, 3, 1, 1, 4]) == True
    assert can_reach([3, 2, 1, 0, 4]) == False

test(can_reach)