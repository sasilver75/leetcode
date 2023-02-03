"""
Number of Islands

Given an m*n 2D binary grid `grid` which represents a map of
1s (land) and 0s (water)

return the NUMBER OF ISLANDS

An island is surrounded by waters and is formed by connecting
adjacent lands horizontally or vertically.

You may assume all four edges of the grid are all surrounded by water.

"""

"""
I can think of two ways of doing this...
1. Keeping track of the land cells that we've "sunk" by keeping track of the (row,col)s
that we've sunk in the past
2. Not even keeping track of the land cells we've visit -- instead of remembering
the sunk cells, we just mutate those cells to a third value (eg "2"). At the end, we can 
mutate these cells back to the normal land cells.
"""


def number_of_islands_memory(grid: list[list[str]]) -> int:
    sunk_cells = set()
    count = 0

    def recursive_sink(r: int, c: int) -> None:
        """
        Explore a contiguous island, adding land cell coordinates to sunk_cells.

        Called on an unsunk cell, sink the cell and then recurse on every
        valid neighbor that is an un-sunk land cell
        """
        sunk_cells.add((r, c))

        dir_mods = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for r_mod, c_mod in dir_mods:
            target_r = r + r_mod
            target_c = c + c_mod

            # If target cell lis valid (on board), unvisited land
            if (
                    0 <= target_r < len(grid) and
                    0 <= target_c < len(grid[0]) and
                    grid[target_r][target_c] == "1" and
                    (target_r, target_c) not in sunk_cells
            ):
                recursive_sink(target_r, target_c)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1" and (row, col) not in sunk_cells:
                recursive_sink(row, col)
                count += 1

    print(count)
    return count


def number_of_islands_mutative(grid: list[list[str]]) -> int:
    count = 0

    def recursive_sink(r: int, c: int) -> int:
        grid[r][c] = "2"

        dir_mods = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for r_mod, c_mod in dir_mods:
            r_target = r + r_mod
            c_target = c + c_mod

            if (
                0 <= r_target < len(grid) and
                0 <= c_target < len(grid[0]) and
                grid[r_target][c_target] == "1"
            ):
                recursive_sink(r_target, c_target)

    # Sinking and Counting
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                recursive_sink(row, col)
                count += 1

    # Cleanup
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "2":
                grid[row][col] == "1"

    return count


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


test(number_of_islands_memory)
test(number_of_islands_mutative)
