"""
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

1) Each ROW much contain the digits 1-9 without repetition
2) Each COLUMN must contain the digits 1-9 without repetition
3) Each of the nine 3x3 sub-boxes of hte grid must contain the digits 1-9
without repetition

A sudoku board (partially filled) could be valid, but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules

So the question is more like: "At the current state of the sudoku board, are
they violating any of the three rules?"
"""


def valid_sudoku_naive(board: list[list[str]]) -> bool:
    """

    :return: Whether the Sudoku board is valid
    """
    if not board:
        return False

    for row in board:
        row_seen = set()
        for val in row:
            if val != ".":
                if val in row_seen:
                    return False
                row_seen.add(val)

    for col in range(len(board[0])):
        col_seen = set()
        for colRow in range(len(board)):
            val = board[colRow][col]
            if val != ".":
                if val in col_seen:
                    return False
                col_seen.add(val)

    for startRow, startCol in [
        [0, 0],
        [3, 0],
        [6, 0],
        [3, 0],
        [3, 3],
        [3, 6],
        [6, 0],
        [6, 3],
        [6, 6],
    ]:
        box_seen = set()
        for rowMod in [0, 1, 2]:
            for colMod in [0, 1, 2]:
                val = board[startRow + rowMod][startCol + colMod]
                if val != ".":
                    if val in box_seen:
                        return False
                    box_seen.add(val)

    return True


def valid_sudoku_naive_better(board: list[list[str]]) -> bool:
    """
    Instead of doing it in three passes through the board, we could do it in one pass
    through the board -- still O(N) complexity.
    :return: Whether the Sudoku board is valid
    """
    if not board:
        return False

    row_seens = {r: set() for r in range(len(board))}
    col_seens = {c: set() for c in range(len(board[0]))}
    box_seens = {
        rowStart: {
            colStart: set() for colStart in [0, 3, 6]
        } for rowStart in [0, 3, 6]
    }

    for row in range(len(board)):
        for col in range(len(board[0])):
            val = board[row][col]
            if val != ".":
                if val in row_seens[row]:
                    return False
                row_seens[row].add(val)

                if val in col_seens[col]:
                    return False
                col_seens[col].add(val)

                row_key = next(key for key in [6, 3, 0] if row >= key)
                col_key = next(key for key in [6, 3, 0] if col >= key)
                if val in box_seens[row_key][col_key]:
                    return False
                box_seens[row_key][col_key].add(val)

    return True


def valid_sudoku_board(board: list[list[str]]) -> bool:
    """Doesn't seem like there's a better solution"""
    pass


def assert_passes_test_cases(fn):
    assert fn([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                  , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                  , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                  , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                  , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                  , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                  , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                  , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                  , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])

    assert not fn([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                      , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                      , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                      , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                      , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                      , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                      , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                      , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                      , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])


assert_passes_test_cases(valid_sudoku_naive)
assert_passes_test_cases(valid_sudoku_naive_better)
