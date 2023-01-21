"""
Number of Islands

Given an m * n binary grid `grid` which represents a map of `1`s (land)
and `0`s (water), return the NUMBER OF ISLANDS

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume that all four edges of the
grid are all surrounded by water.
"""


"""
I think we can eagerly flood islands when we encounter them, incrementing the 
island count before me make our first count to sink().

For the DFS/BFS whatever we use to flood an island...
    - Called on a valid (on-board) island (1) cell...
    - Sink the Cell
    - Recurse on any adjacent land cells [We don't need ot keep a notion of "visited"]
        - If we're unable to modify the list, we could either allocate a whole new copy of the
        board or we could "sink" islands to a "2" state, and then clean up "2"s to "1"s at the end.
"""
def count_islands(grid: list[list[str]]) -> int:
    island_count = 0

    def sink(row_idx: int, col_idx: int) -> None:
        """Sink the target land cell and all of its neighbors (recursively)"""
        grid[row_idx][col_idx] = "0"

        dir_mods = [[-1, 0], [1, 0], [0,-1], [0,1]]
        for row_mod, col_mod in dir_mods:
            target_row_idx = row_idx + row_mod
            target_col_idx = col_idx + col_mod

            # If the target cell is valid (on-board) and land, sink it
            if (
                0 <= target_row_idx < len(grid) and
                0 <= target_col_idx < len(grid[0]) and
                grid[target_row_idx][target_col_idx] == "1"
            ):
                sink(target_row_idx, target_col_idx)


    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx] == "1":
                island_count += 1
                sink(row_idx, col_idx)

    return island_count



assert count_islands(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
) == 1

assert count_islands(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
) == 3

