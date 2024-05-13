"""
Number of Islands

Given an `m x n` 2d binary grid `grid` which represents a map
of 1's (land) and 0's (water), return the number of islands!

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically.

You may assume all four edges of the grid are all surrounded by water.
"""

"""
The "problem" with this question is:
    * When you hit a land tile
        - Being able to explore that island, and "count" it as one island
    * And then when you continue searching, not accidentally "rediscovering"
        that same island.

To tackle that problem, you could either keep track of all visited land squares,
or you could "sink" an island by mutating the grid as you're exploring it.

    Q: Hold up, is there some sort of problem with swapping 1's to 0's, given
    that there's logic that asks whether adjacent tiles are 0's?
    A: Nope! If two islands' tiles were going to interact in anyway, they'd
    by definition be one island. We can safely sink islands without damaging
    our logic for other islands.
"""

def n_islands(grid: list[list[int]]) -> int:
    nrow = len(grid)
    ncol = len(grid[0])

    def explore(row: int, col: int) -> None:
        # Explore and Sink an Island. Called on a land cell.
        grid[row][col] = "0"

        dir_mods = [[-1,0], [1,0], [0,-1], [0,1]] # UDLR
        for row_mod, col_mod in dir_mods:
            target_row = row + row_mod
            target_col = col + col_mod

            # If target cell is valid and contains land, explore it
            if (
                    0 <= target_row < nrow and
                    0 <= target_col < ncol and
                    grid[target_row][target_col] == "1"
            ):
                explore(target_row, target_col)

    island_count = 0
    for row in range(nrow):
        for col in range(ncol):
            cell = grid[row][col]
            if cell == "1":
                island_count += 1
                explore(row, col)

    return island_count



def test(fn):
    assert fn([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1

    assert fn([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3

test(n_islands)