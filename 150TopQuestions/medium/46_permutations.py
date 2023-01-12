"""
Permutations

Given an array nums of distinct integers, return ALL THE POSSIBLE
PERMUTATIONS! You can return the answer in ANY order.
"""
from typing import Optional

"""
[1,2,3] --> [1,2,3] using start=0, step=1
        --> [1,3,2] using start=0, step=2 (with wrap)
        --> [2,1,3] using start=1, step=2 (with wrap)
        --> [2,3,1] using start=1, step=1 (with wrap)
        --> [3,1,2] using start=2, step=1 (with wrap)
        --> [3,2,1] using start=2, step=1 (with wrap)
        
I suspect that for each N starting indices, you can do N-1 (call it N) factorial combinations of the other ones?
So in this case we could do 2! = 2*1 = 2 options for each starting index

Let's try it it with [1,2,3,4]

[1,2,3,4] --> [1,2,3,4] using start=0, stpe=1
          --> [1,2,4,3]  /!\ This is actually NOT creatable using our strategy 
          of some constant step. So we can't pursue this one.

Let's just try to bust through it using a lot of memory and time complexity
and then we'll look at the proper solution
"""


def permutations(nums: list[int]) -> list[list[int]]:
    perms = []
    def helper(remaining_nums: list[int], built_list: Optional[list[int]] = None):
        if not built_list:
            built_list = []

        # If we're out of numbers, add it to perms.
        if not remaining_nums:
            perms.append(built_list)
            return

        # for idx, num in enumerate(remaining_nums): # NOTE: This works just fine, but I think my other solution is cleaner
        #     helper([n for i, n in enumerate(remaining_nums) if i != idx], [*built_list, num])

        for idx, num in enumerate(remaining_nums):
            # Recurse into the future having that THAT element as the next element in the built list
            helper(remaining_nums[:idx] + remaining_nums[idx+1:], [*built_list, num])


    helper(nums)

    print(perms)
    return perms



def test(fn):
    assert fn([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert fn([0, 1]) == [[0, 1], [1, 0]]
    assert fn([1]) == [[1]]

test(permutations)