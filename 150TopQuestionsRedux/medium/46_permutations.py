"""
Permutations
Given an array of nums of DISTINCT integers, return all the possible
permutations! You can return the answer in any order.
"""
from typing import Optional


def get_permutations(nums: list[int]) -> list[list[int]]:
    permutations = []
    def recursive_helper(built: list[int], remaining: list[int]) -> None:
        if built is None:
            built = []

        if not remaining:
            permutations.append(built)
            return

        for char in remaining:
            new_built = [*built, char]
            new_remaining = [c for c in remaining if c != char]
            recursive_helper(new_built, new_remaining)

    recursive_helper([], nums)

    print(permutations)
    return permutations




def test(fn):
    ans1 = fn([1, 2, 3])
    assert all(ans in ans1 for ans in [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

    ans2 = fn([0, 1])
    assert all(ans in ans2 for ans in [[0, 1], [1, 0]])

    ans3 = fn([1])
    assert ans3 == [[1]]

test(get_permutations)