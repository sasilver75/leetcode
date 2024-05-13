"""
Word Search
Category: Matrix

Given an m * n grid of characters `board` and a string `word`, return `true`
if `word` exists in the grid!

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are either HORIZONTALLY or VERTICALLY neighboring.

The same letter cell may not be used more than once.
"""
from typing import Optional


def exists(board: list[list[str]], word: str) -> bool:
    if not word:
        return False

    def search(row: int, col: int, idx: int, visited: set) -> bool:
        """
        Called on a not-yet-explored cell, does it contain our target character?
            - If so, continue recursion on valid, unexplored neighbors
        """
        char = word[idx]

        if board[row][col] != char:
            return False

        # It matches :)
        visited.add((row, col)) # This could be anywhere above

        if idx == len(word) - 1:
            # We just found the last character! :)
            return True

        dir_mods = [
            [0, 1],  # Right
            [0, -1],  # Left
            [1, 0],  # Down
            [-1, 0]  # Up
        ]

        # For every neighboring (hypothetical) cell...
        for row_mod, col_mod in dir_mods:
            target_row = row + row_mod
            target_col = col + col_mod

            # If that cell is valid (on-board) and unvisited, recurse into it!
            if (
                0 <= target_row < len(board)
                and 0 <= target_col < len(board[0])
                and (target_row, target_col) not in visited
                and search(target_row, target_col, idx+1, visited.copy())
            ):
                return True

        # No neighboring cells matched
        return False

    for row in range(len(board)):
        for col in range(len(board[0])):
            if search(row, col, 0, set()):
                return True

    return False


def test(fn):
    assert fn([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ], "ABCCED") == True

    assert fn([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ], "SEE") == True

    assert fn([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ], "ABCB") == False


test(exists)
