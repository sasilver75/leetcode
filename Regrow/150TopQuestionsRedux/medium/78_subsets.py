"""
Subsets

Given an integer array `nums` of UNIQUE ELEMENTS, return all of the possible
subsets (the power set)

The solution set must NOT contain duplicate subsets -- return the
solution in ANY ORDER
"""


def get_subsets(nums: list[int]) -> list[list[int]]:
    subsets = []
    def recursive_helper(built: list[int], idx: int):
        if idx == len(nums):
            subsets.append(built)
            return

        # Either include or don't include the number @ idx in nums in built
        recursive_helper([*built, nums[idx]], idx+1)
        recursive_helper(built, idx+1)

    recursive_helper([], 0)
    print(f"{subsets = }")
    return subsets



def test(fn):
    a1 = fn([1, 2, 3])
    assert all(ans in a1 for ans in [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    a2 = fn([0])
    assert all(ans in a2 for ans in [[], [0]])


test(get_subsets)
