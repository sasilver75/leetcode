"""
Sort Colors

Given an array `nums` with `n` objects colored red/white/blue, sort them
IN-PLACE so that objects of the same color are adjacent, with the colors
in the order red, white, and blue.

We will use the integers 0, 1, 2 to represent the colors red, white, and lue

You must solve this without using the library's sort function.
"""

def sort_colors(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


# --  Test --
def test(fn):
    assert fn([2,0,2,1,1,0]) == [0,0,1,1,2,2]
    assert fn([2,0,1]) == [0,1,2]

test(sort_colors)