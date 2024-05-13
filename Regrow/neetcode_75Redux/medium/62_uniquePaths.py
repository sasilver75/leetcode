"""
Unique Paths

Robot on an m * n grid, starts in the top left, needs to get to eh bottom right.
Given the integers m and n, return the NUMBER OF POSSIBLE UNIQUE PATHS the robot can take to reach the bottom corner.
"""


def unique_paths(m: int, n: int) -> int:
    n_ways = 0

    def explore(downs_remaining: int, rights_remaining: int) -> None:
        """Return the number of possible unique paths from m_remaining, n_remaining to 0, 0"""
        nonlocal n_ways
        # Base Case
        if rights_remaining == 0 and downs_remaining == 0:
            n_ways += 1
            return

        if downs_remaining:
            explore(downs_remaining - 1, rights_remaining)
        if rights_remaining:
            explore(downs_remaining, rights_remaining - 1)

    explore(m-1, n-1) # Because it's an m*n matrix, it takes m-1, n-1 steps to get to the end
    print(n_ways)
    return n_ways


"""
We can also formulate this as a DP array that matches the Roboyt array
And populate it bottom to top, right to left
dp[-1][-1] = 1, since that's the target location

dp[ridx][cidx] = dp[ridx-1][cidx] + dp[ridx][cidx-1]  # Add the belo and right cells
"""
def unique_paths_2d(m: int, n: int) -> int:
    dp = [
        [0] * n
        for row in range(m)
    ]
    dp[-1][-1] = 1

    # Populate the DP table bottom row to top row, from right to left within teach row
    for row in range(m-1, -1, -1):
        for col in range(n - 1, -1, -1):
            # Skip the bottom right cell
            if row == m-1 and col == n-1:
                continue

            # A cell is the addition of the right/below cells
            below = dp[row+1][col] if row+1 < m else 0
            right = dp[row][col+1] if col+1 < n else 0
            dp[row][col] = below + right

    return dp[0][0]



def test(fn):
    assert fn(3, 2) == 3
    assert fn(3, 7) == 28


test(unique_paths)
test(unique_paths_2d)