"""
Island Perimeter

You are given a ROW x COL grid representing a map
where grid[i][j] = 1 represents land, and grid[i][j] = 0 represents
water.

Grid cells are connected horizontally/vertically (not diagonally).

The grid is completely surrounded by water (off the board),
and there is exactly ONE island.

The island doesn't have any "lakes," meaning that the water inside
isn't' connected to the water around the island. One cell is a square
with side length 1. The grid is rectangular, and width/height don't exceed 100.

Determine the perimeter of the island.
"""


def get_perimeter(grid: list[list[int]]) -> int:
    """
    O(N) time and O(N) space
    """
    # No grid case
    if not grid or not grid[0]:
        return 0

    state = {
        "perimeter_count": 0,
        "visited_tiles": set()
    }
    # Scan for Land... Breaking out of a doubly-nested is kind of ugly (raising an exception, changing a boolean variable in the outer loop, etc).
    # A better solution that scanning the whole table and retaining the LAST land tile would be to do it in a single loop over a list of (i, j)
    # Found land @ i,j! Break. This could be extracted into a find_first_land function
    land_row, land_col = None, None
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == 1:
                land_row = row
                land_col = col

    # No land case
    if land_row is None:
        return 0

    explore(grid, land_row, land_col, state)

    print(state["perimeter_count"])
    return state["perimeter_count"]


def explore(grid: list[list[int]], row: int, col: int, state: dict) -> None:
    """
    Given a board and a current row/col tile CONTAINING A LAND TILE
    Explore the given tile, updating state (perim count, visited tiles)
    Recurse on all adjacent, appropriate tiles
    """

    # Assumption: This explore is only invoked on an on-board LAND tile

    # Mark Current Tile as Visited
    state["visited_tiles"].add((row, col))

    # View adjacent tiles
    directions = [
        [-1, 0], # Up
        [1, 0], # Down
        [0, -1], # Left
        [0, 1], # Right
    ]

    # Look Around... in each direction
    for dir in directions:
        # Adjacent tile (new_row, new_col)
        row_mod, col_mod = dir
        new_row = row + row_mod
        new_col = col + col_mod


        if not is_on_board(grid, new_row, new_col) or not grid[new_row][new_col]:
            # (Off-board) or (On-board Water Tile)
            state["perimeter_count"] += 1
        else:
            # (On-board Land Tile)
            # If we haven't visited it, visit it!
            if (new_row, new_col) not in state["visited_tiles"]:
                explore(grid, new_row, new_col, state)



def is_on_board(grid, row, col):
    """
    Given an actual legit board, is i, j off the board?
    """
    if row not in range(0, len(grid)) or col not in range(0, len(grid[0])):
        return False
    return True



case_1 = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
]
assert get_perimeter(case_1) == 16

case_2 = [
    [1]
]
assert get_perimeter(case_2) == 4  # Water OUTSIDE the perimeter should count for edge pieces!

case_3 = [
    [1, 0]
]
assert get_perimeter(case_3) == 4
