"""
Pascal's triangle

Given an integer numRows, return the first numRows of Pascal's Triangle!
In Pascal's Triangle, each row is the sum of the two numbers directly above it,
as shown:

                1
            1       1
        1       2       1
    1       3       3       1
1       4       6       4       1
"""

"""
Thinking:
Insight is that all of the rows that have "interior numbers" (rows 3+),
the exterior numbers are all 1's! So we need to take the pairwise sums of the 
row above the current row, and then smush that resulting list between two 1's.
"""


def pascal(nrows: int) -> list[list[int]]:
    acc = []
    for row_n in range(nrows):
        if row_n == 0:
            acc.append([1])
        elif row_n == 1:
            acc.append([1, 1])
        else:
            last_row = acc[-1]
            sums = adjacent_sums(last_row)
            new_row = [1, *sums, 1]
            acc.append(new_row)
    return acc


def adjacent_sums(nums: list[int]) -> list[int]:
    # Given a list nums of length 2+, return a list that's the parwise sums
    acc = []
    for i in range(1, len(nums)):
        acc.append(nums[i] + nums[i - 1])
    return acc


assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(1) == [[1]]
