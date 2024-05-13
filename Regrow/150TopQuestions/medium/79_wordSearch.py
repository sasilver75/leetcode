"""
Word Search

Given an m*n grid of characters `board` and a string `word`, return
`true` if `word` exists in the grid!

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are vertically or horizontally neighboring.

The same letter cell MAY NOT BE USED MORE THAN ONCE!

For example:

    a   b   c   e
    s   f   c   s       search: ABCCED  == True
    a   d   e   e

    [A] [B] [C] e
    s   f   [C] s
    a   [D] [E] e
"""
from typing import Optional


def word_search(grid: list[list[str]], word: str) -> bool:
    def helper(targetIdx: int, row: int, col: int, visited: Optional[set] = None):
        # Assuming that we're called on a valid cell and we're now looking for the char @ idx
        if visited is None:
            visited = set()

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # Up Down Left Right
        for row_mod, col_mod in directions:
            target_row = row + row_mod
            target_col = col + col_mod

            if (
                    0 <= target_row < len(grid) and
                    0 <= target_col < len(grid[0]) and
                    grid[target_row][target_col] == word[targetIdx] and
                    (target_row, target_col) not in visited
                ):

                # Did we just find the last character? Return True if so!
                if targetIdx == len(word) - 1:
                    return True

                new_visited = visited.copy()
                new_visited.add((target_row, target_col))
                if helper(targetIdx + 1, target_row, target_col, new_visited):
                    return True

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == word[0] and helper(1, row, col, set([(row, col)])):
                return True

    return False


# -- Test --

def test(fn):
    assert fn(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ], "ABCCED"
    ) == True

    assert fn(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ],
        "SEE"
    ) == True

    assert fn(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ],
        "ABCD"
    ) == False


test(word_search)
