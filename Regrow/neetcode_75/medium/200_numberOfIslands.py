"""
Number of Islands
Category: Graph

Given an `m * n` 2D binary grid `grid` which represents a map of `1`s (land)
and `0`s (water), return the NUMBER of islands.

An island is surrounded by water and formed by connecting all adjacent lands
horizontally and vertically.
You may assume that all four edges of the grid are all surrounded by water.
"""


def n_islands(grid: list[list[str]]) -> int:
    """
    The idea is to iterate through the map, and when I encounter a land cell,
    SINK the entire island and increment the island count by one.

    We could either do this over a "Copy" of the `grid` map, which we would be
    free to mutate, or we could mutate the original `grid` map in such a way
    that we can then "unmutate" it back to its original state. This would involve
    less memory usage. My idea for this would be to set sunk sections to "2",
    and then afterwards to set all "2"s back to "1"s.

    But for ease of writing this "easy" problem, I'm going to just copy the
    lista nd mutate it.
    """
    grid = grid.copy()

    def sink(r: int, c: int) -> None:
        """
        Called on a land cell, sink the land cell and then
        sink any adjacent land cells
        """
        grid[r][c] = "0"
        dir_mods = [
            [0, 1],  # Up
            [0, -1],  # Down
            [1, 0],  # Right
            [-1, 0]  # Left
        ]
        for row_mod, col_mod in dir_mods:
            target_row, target_col = r + row_mod, c + col_mod
            # Check that the cell is on-board and a land cell
            if (
                    0 <= target_row < len(grid)
                    and 0 <= target_col < len(grid[0])
                    and grid[target_row][target_col] == "1"
            ):
                sink(target_row, target_col)

    n_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                sink(row, col)
                n_islands += 1

    return n_islands


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