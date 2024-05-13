"""
Surrounded Regions

Given an m * n matrix `board` containing `X` and `0`, CAPTURED all regions
that are 4-directionally surrounded by `X`

A region is CAPTURED by flipping all 0s into Xs in that surrounded region!
"""


"""
Hmmm. so how do we go about doing this?

It's pretty much a count islands/flood fill, except it's only for islands
that don't have any cells touching the edge of the board.

We can't eagerly flood the island though without exploring the whole thing, so I think we 
need to perhaps explore the whole island... before capturing/sinking it.

Initial Idea:
    - Do a pass through the board, doing an eager flood fill whenever we
     encounter an O cell, swapping them to something like C, meaning "Candidate"
    - Do another pass through the board. If we encounter a C on an edge position, then
    eagerly floodfill that C's island into an "E" island, meaning "Exclude"
     - Do a final pass through the board
        - Swap E's back to O's (they weren't able to be captured)
        - Swap C's to X's (they have been captured)
        
Second Idea - Much Better!:
    - Pass through the board, doing a DFS/BFS to traverse through islands of Os,
    affiliating them into a group. Stick that group into a groups accumulator.
    - For each group (set of (row,col) tuples), if the group is capturable (no cells
    being on the border), then capture the group.
"""
def capture_islands(board: list[list[str]]) -> None:
    affiliated_cells = set() # Cells belonging to ANY group
    groups = []

    def affiliate(row: int, col: int, group: set[tuple[int, int]]) -> None:
        # Affiliate the current row/col cell into the group
        group.add((row, col))
        affiliated_cells.add((row, col))

        # Recurse on all adjacent, valid, unaffiliated cells with 0-value
        dir_mods = [[-1,0], [1,0], [0,-1], [0,1]]
        for row_mod, col_mod in dir_mods:
            target_row = row + row_mod
            target_col = col + col_mod

            if (
                0 <= target_row < len(board) and
                0 <= target_col < len(board[0]) and
                board[target_row][target_col] == "O" and
                (target_row, target_col) not in affiliated_cells
            ):
                affiliate(target_row, target_col, group)

    def is_border_cell(row: int, col: int) -> bool:
        return (
            row == 0 or
            row == len(board) - 1 or
            col == 0 or
            col == len(board[0]) - 1
        )

    def capture(group: set[tuple[int, int]]) -> None:
        for row, col in group:
            board[row][col] = "X"

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "O" and (row, col) not in affiliated_cells:
                group = set()
                affiliate(row, col, group)
                groups.append(group)

    for group in groups:
        if not any(
            is_border_cell(r, c) for r,c in group
        ):
            capture(group)


def test(fn):
    """
    Notice in this first example that an O should not be flipped if:
        - It is on the border
        - It is adjacent to an O that should not be flipped

    In this case, the bottom O is on the border, so it shouldn't be flipped.
    The other three 0s form a surrounded region, so they're flipped.
    """
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    fn(board)
    assert board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]

    board = [["X"]]
    fn(board)
    assert board == [["X"]]

test(capture_islands)