"""
Permutations

Given an array `nums` of distinct integers, return all the possible permutations.

You can return teh answer in any order.

Example:
    [1,2,3]

Can become:
[
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
]

NOTE: All integers in the list are unique! :)
"""
import random


def permutations_naive(nums: list[int]) -> list[list[int]]:
    perms = []

    def dfs(remaining: list[int], running_perm: list[int]) -> None:
        if not remaining:
            perms.append(running_perm)
            return

        for idx in range(len(remaining)):
            dfs([*remaining[:idx], *remaining[idx+1:]], [*running_perm, remaining[idx]])

    dfs(nums, [])

    return perms


# Is there even a better solution for this? I dunno!
def permutations(nums: list[int]) -> list[list[int]]:
    pass


def test(fn):
    assert all(ans in fn([1, 2, 3]) for ans in [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    assert fn([0, 1]) == [[0, 1], [1, 0]]
    assert fn([1]) == [[1]]

test(permutations_naive)
# test(permutations)
