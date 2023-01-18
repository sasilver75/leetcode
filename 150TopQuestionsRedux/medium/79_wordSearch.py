"""
Word Search

Given an m * n grid of characters `board` and a string `word`, return `true`
if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are either HORIZONTALLY or VERTICALLY neighboring.
The same letter cell may not be used more than once.
"""
import itertools


def word_search(board: list[list[str]], s: str) -> bool:
    def recursive_search(row_idx: int, col_idx: int, s_idx: int, visited: list[list[int]]) -> bool:
        if s_idx == len(s):
            return True

        if board[row_idx][col_idx] != s[s_idx]:
            return False

        # Found character :) Recurse on all valid, unvisited neighbors
        # This could be one big list comprehension too
        dir_mods = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # Up Down Left Right
        adjacent_cells = [[row_idx+row_mod, col_idx+col_mod] for row_mod, col_mod in dir_mods]
        valid_adjacent_cells = [[row_idx,col_idx] for row_idx, col_idx in adjacent_cells if 0 <= row_idx < len(board) and 0 <= col_idx < len(board[0])]
        unvisited_valid_adjacent_cells = [[row_idx,col_idx] for row_idx,col_idx in valid_adjacent_cells if [row_idx,col_idx] not in visited]

        new_visited = [*visited, [row_idx, col_idx]]
        return any(
            recursive_search(target_row, target_col, s_idx+1, new_visited.copy())
            for target_row, target_col in unvisited_valid_adjacent_cells
        )

    for row_idx, col_idx in itertools.product(range(len(board)), range(len(board[0]))):
        if recursive_search(row_idx, col_idx, 0, []):
            return True

    return False


def test(fn):
    assert fn(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], s="ABCCED") == True
    assert fn(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], s="SEE") == True
    assert fn(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], s="ABCB") == False

test(word_search)