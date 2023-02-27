"""
Word Search

Given an m * n grid of characters BOARD and a string WORD, return TRUE if WORD
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are HORIZONTALLY OR VERTICALLY NEIGHBORING

The same letter cell may not be used more than once
"""


def exist(board: list[list[str]], word: str) -> bool:
    def explore(row: int, col: int, word_idx: int = 0, seen: set[tuple] = None) -> bool:
        if seen is None:
            seen = set()

        # Check if current cell is off-board
        if (
            (0 > row or row >= len(board)) or
            (0 > col or col >= len(board[0]))
        ):
            return False

        # Check if current cell contains target character
        if board[row][col] != word[word_idx]:
            return False

        # Current Cell Contains Target Character! Woo

        # Was that our last character?
        if word_idx == len(word) - 1:
            return True

        seen.add((row, col))

        dir_mods = [
            [0, 1],
            [0, -1],
            [-1, 0],
            [1, 0]
        ]
        for row_mod, col_mod in dir_mods:
            target_row = row + row_mod
            target_col = col + col_mod

            if (target_row, target_col) not in seen and explore(target_row, target_col, word_idx+1, seen.copy()):
                return True

        return False



    return any(
        explore(row_idx, col_idx)
        for row_idx in range(len(board))
        for col_idx in range(len(board[0]))
    )


def test(fn):
    assert fn(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ],
        word="ABCCED"
    ) == True

    assert fn(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ],
        word="SEE"
    ) == True

    assert fn(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ],
        word="ABCB"
    ) == False

test(exist)