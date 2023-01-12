"""
Valid Sudoku

Determine if a 9x9 Sudoku board is valid.

ONLY THE FILLED CELLS need to be considered valid according to the following rules:

1) Each row much contain the digits 1-9 without repetition
2) Each column must contain the digits 1-9 without repetition
3) Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9
without repetition

Note:
    Only the filled cells need to be validated according to the aforementioned
    rules
"""
import collections
from typing import Callable


def solve_naive(board: list[list[str]]) -> bool:
    # Check Columns
    for col in range(len(board[0])):
        # Col Set
        col_seen = set()
        for row in range(len(board)):
            val = board[row][col]
            if val in col_seen and val != ".":
                return False
            col_seen.add(val)

    # Check Rows
    for row in range(len(board)):
        # Row Set
        row_seen = set()
        for col in range(len(board[0])):
            val = board[row][col]
            if val in row_seen and val != ".":
                return False
            row_seen.add(val)

    # Check Boxes
    row_col_starts = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    for row_start, col_start in row_col_starts:
        square_seen = set()
        for row_mod in range(0, 3):
            for col_mod in range(0, 3):
                val = board[row_start + row_mod][col_start + col_mod]
                if val in square_seen and val != ".":
                    return False
                square_seen.add(val)

    # LGTM
    return True


"""
Okay, but we're visiting every cell multiple times -- at least once for each
rule, right? This would be slightly faster...

We can use O(N^2) memory instead of O(N) memory to do this
"""


def solve(board: list[list[str]]) -> bool:
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)  # key = (r/3, c/3)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue

            # Check for failure conditions if we were to add val to rule sets
            if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
                return False

            # Add val to rule sets
            rows[r].add(val)
            cols[c].add(val)
            squares[(r // 3, c // 3)].add(val)

    # No violations; we must be good!
    return True


# -- Test Pass --

def test(fn: Callable) -> None:
    board_1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert fn(board_1)

    board_2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert fn(board_2) == False


test(solve)
