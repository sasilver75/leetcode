"""
Word Search

Given an m * n grid of characters `board` and a string `word`, return `true` if `word` exists in the grid

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontaly or
vertically neighboring. the same letter cell may not be used more than once!
"""


def exist(board: list[list[str]], word: str) -> bool:

    def explore(r: int, c: int, idx: int, seen: set[tuple]) -> bool:
        """
        Called on a valid on-board cell
        Looking for character at word[idx] in board[r][c]
        :param r:
        :param c:
        :param idx:
        :param seen:
        :return:
        """
        if board[r][c] != word[idx]:
            return False

        if idx == (len(word)-1):
            return True

        seen.add((r, c))

        dir_mods = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]
        for row_mod, col_mod in dir_mods:
            # If on board and not visited, visit it!
            target_row = r + row_mod
            target_col = c + col_mod

            if (
                (0 <= target_row < len(board)) and
                (0 <= target_col < len(board[0])) and
                ((target_row, target_col)) not in seen
                and explore(target_row, target_col, idx+1, seen.copy())
            ):
                return True

        return False

    for row_idx in len(board):
        for col_idx in len(board[0]):
            if explore(row_idx, col_idx, 0, set()):
                return True

    return False






def test(fn):
    assert fn(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED") == True
    assert fn([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE") == True
    assert fn(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB") == False

test(exist)
