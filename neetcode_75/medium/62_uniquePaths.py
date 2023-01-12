"""
Unique Paths
Category: DP

There is a robot on an `m * n` grid.
The robot is initially located at the TOP-LEFT corner (i.e. grid[0][0]).

The robot tries to move to the bottom-right corner (ie grid[m-1][n-1]).
The robot can only move either DOWN or RIGHT at any point in time.

Given hte two integers m and n, return the NUMBER of possible unique paths that the robot
can take to reach the bottom-right corner!
"""


def unique_paths_brute(m: int, n: int) -> int:
    ways = 0

    def helper(row: int, col: int) -> None:
        nonlocal ways
        if row == m - 1 and col == n - 1:
            ways += 1
            return

        if row >= m or col >= n:
            return  # Off board

        helper(row + 1, col)  # Down
        helper(row, col + 1)  # Right

    helper(0, 0)
    return ways


"""
How can we do better?
If we were at (r, c) and we knew that we could move to either
(r+1, c) or (r, c+1), then it would be handy to already know the answer to
those questions, right? :) 

So dp[row][col] can be the number of ways to get to the end from [row][col]
How do we initialize? How do we progress? 

dp[row][col] = dp[row+1][col] + dp[row][col+1]   Where dp[r][c] that's offboard returns 0


    _   _   _   _
    _   _   _   _
    _   _   _   1           Initialized
    
    _   _   _   _
    _   _   _   _
    _   _   _   1  
    
    * Populate the nR-1'th row cells that aren't populated (right to left)
    * Populate the nC-1'th col cells that aren't populated (bottom to top)
    
    Same for nR-2, nC-2... all while >= 0th is being considered

     
"""


def unique_paths(m: int, n: int) -> int:
    # M rows and N columns
    nRow, nCol = m, n

    dp = [
        [0] * nCol
        for _ in range(m)
    ]
    dp[nRow - 1][nCol - 1] = 1

    # (r)ow and (c)olumn pointers initialized at the last row, last col
    r, c = nRow - 1, nCol - 1
    while r >= 0 or c >= 0:

        if r >= 0:
            # Populate the r'th row, right to left
            for rowCol in range(nCol - 1, -1, -1):
                # dp[a][b] = dp[a+1][b] + dp[a][b+1]  assuming on board
                if (r, rowCol) != (nRow - 1, nCol - 1):  # ignore the bottom-right-most cell
                    dp[r][rowCol] = (
                            (dp[r + 1][rowCol] if r + 1 < nRow else 0)
                            +
                            (dp[r][rowCol + 1] if rowCol + 1 < nCol else 0)
                    )

            r -= 1

        if c >= 0:
            # Populate the c'th column, bottom to top
            for colRow in range(nRow - 1, -1, -1):
                # dp[a][b] = dp[a+1][b] + dp[a][b+1]  assuming on board
                if (colRow, c) != (nRow - 1, nCol - 1):  # ignore the bottom-right-most cell
                    dp[colRow][c] = (
                            (dp[colRow + 1][c] if colRow + 1 < nRow else 0)
                            +
                            (dp[colRow][c + 1] if c + 1 < nCol else 0)
                    )

            c -= 1

    print(dp)
    return dp[0][0]


def test(fn):
    assert fn(3, 7) == 28
    assert fn(3, 2) == 3


# test(unique_paths_brute)
test(unique_paths)
