"""
Unique Paths
Difficulty: Medium

A robot is located in the top-left corner of an `m * n` grid

The robot can only move either down or right at any point in time;
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?
"""


def unique_paths_naive(rows: int, cols: int) -> int:
    def helper(row: int, col: int):
        # How many ways are there to get to the end from m, n?

        # Base Case: We're at the target
        if row == rows - 1 and col == cols - 1:
            return 1

        right_count = helper(row, col + 1) if col + 1 < cols else 0
        down_count = helper(row + 1, col) if row + 1 < rows else 0

        return right_count + down_count

    return helper(0, 0)


def unique_paths(m: int, n: int) -> int:
    """
    Using 2-dimensional dynamic programming
    The idea is to start with an m*n dp array, with a 1 in the bottom-right

    And then populate the DP table from the bottom-right to the top-left...
    We can do this by populating columns from bottom to top, from right to left.
    """
    dp = [[None] * n for _ in range(m)]
    dp[-1][-1] = 1

    current_col = n - 1

    while current_col >= 0:
        # Populating DP bottom to top
        for row in range(m-1, -1, -1):
            if current_col == n-1 and row == m-1:
                continue

            dp_right = dp[row][current_col+1] if current_col + 1 < n else 0
            dp_down = dp[row+1][current_col] if row+1 < m else 0
            dp[row][current_col] = dp_right + dp_down

        current_col -= 1

    return dp[0][0]




def test(fn):
    assert fn(3, 7) == 28
    assert fn(3, 2) == 3
    assert fn(5, 1) == 1


test(unique_paths_naive)
test(unique_paths)
