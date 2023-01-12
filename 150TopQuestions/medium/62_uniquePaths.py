"""
Unique Paths

There is a robot on an `m * n` grid.
The robot is initially located in the top-left corner, `grid[0][0]`

The robot attempst to move to the bottom-right corner, `grid[m-1][n-1]`
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the NUMBER OF POSSIBLE UNIQUE PATHS
that the robot can take to reach the bottom-right corner.
"""

"""
Even though we're actually going from [0, 0] to over to [3, 7],
it might be easier to just me decrementing these integers rather than
having some other variables to keep track 
"""
def unique_paths(m: int, n: int) -> int:
    ways = 0
    def explore(m_remaining: int, n_remaining: int) -> int:
        nonlocal ways
        if not m_remaining and not n_remaining:
            ways += 1
            return

        if m_remaining:
            explore(m_remaining-1, n_remaining)
        if n_remaining:
            explore(m_remaining, n_remaining-1)

    explore(m-1, n-1) # Since we're really starting at [2, 6] for a 3x7 board
    print(ways)
    return ways

# -- Test --
assert unique_paths(3, 7) == 28
assert unique_paths(3, 2) == 3


