"""
Unique Paths

Theres's a robot on an m*n grid. The robot is initially located in the top-left corner (ie grid[0][0]). Ther obot tries to move
to the bottom right corner (ie grid[m-1][n-1]). The robot can only move either down or right at any point in time
Given two integers m and n, return the NUMBER OF POSSIBLE UNIQUE PATHS that the robot can take to reach the bottom-right corner.
"""

def n_paths_brute(m: int, n: int) -> int:
    n_ways = 0
    def recursive_explorer(m: int, n: int):
        nonlocal n_ways
        print(f"Called with {m = } {n = }")
        if m == 0 and n == 0:
            n_ways += 1
            return

        if m > 0:
            recursive_explorer(m-1, n)
        if n > 0:
            recursive_explorer(m, n-1)

    recursive_explorer(m-1, n-1)
    return n_ways

def test(fn):
    assert fn(3,7) == 28
    assert fn(3,2) == 3

test(n_paths_brute)