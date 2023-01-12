"""
Count Negative Numbers in a Sorted Matrix

Given an m * n matrix `grid` which is sorted in non-increasing order both row-wise and column wise,
return the NUMBER of negative numbers in the grid!
"""


def count_negatives_linear(grid: list[list[int]]) -> int:
    return sum(
        el < 0
        for row in grid
        for el in row
    )


"""Oops, this doesn't work. It's because I thought the rows were sorted in ASC, but they're actually DESC. Woops! Would be easy to fix"""
def count_negatives_logarithmic(grid: list[list[int]]) -> int:
    if not grid:
        return 0
    # Doing log(x) searches across either rows or columns (the longer one), for each row or column (the shorter one)
    count = 0

    """We could do this logarithmic search on each row/col depending on which is longer, but I don't want to fuck with this right now"""
    # Matrix is WIDER than it is LONG. Logarithmic search through each row (which are longer)
    for row in grid:
        # Search for first occurrence of a positive number in sorted ASC
        l, r = 0, len(row) - 1
        leftmost_positive = -1

        while l <= r:
            mid_idx = l + (r - l) // 2
            mid_val = row[mid_idx]

            if mid_val >= 0:
                # We're in the positives (or 0)! Note the index and look left
                leftmost_positive = mid_idx
                r = mid_idx - 1
            else:
                # We're in the negatives; look right
                l = mid_idx + 1

        if leftmost_positive == -1:
            # all numbers are negative
            print("Adding ", len(row))
            count += len(row)
        else:
            print("Adding ", leftmost_positive)
            count += leftmost_positive

    print(count)
    return count


# Followup: Could you find an O(n + m) solution?

def test(fn):
    assert fn([
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]
    ]) == 8

    assert fn([
        [3, 2],
        [1, 0]
    ]) == 0


test(count_negatives_linear)
test(count_negatives_logarithmic)

nums = [-4, -2, -1, 0, 0, 3, 6, 8]
nums2 = [-2, -1]


def how_many_negatives(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    leftmost_positive = -1
    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = nums[mid_idx]

        if mid_val >= 0:
            # We're in the positives (or 0)! Note the index and look left
            leftmost_positive = mid_idx
            r = mid_idx - 1
        else:
            # We're in the negatives; look right
            l = mid_idx + 1

    if leftmost_positive == -1:
        # all numbers are negative
        return len(nums)

    return leftmost_positive


assert how_many_negatives(nums) == 3
assert how_many_negatives(nums2) == 2
