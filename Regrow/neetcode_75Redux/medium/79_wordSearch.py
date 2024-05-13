"""
Word Search

Given an m * n grid of characters board and a string word, return true if word exists in the grid

The word can be constructed from letters of sequentially-adjacent cells, where adjacent
cells are horizontally or vertically neighboring.

the same letter cell may not be used more than once.
"""

"""
I think this "word search" naively is going to be a depth-first search through the graph, keeping track
of the visited cells so that we don't count the same letter twice

dfs(idx: int, visited: set[tuple[int,int]])) -> bool:

"""


def exists(board: list[list[str]], word: str) -> bool:
    def dfs(row: int, col: int, idx: int, visited: set) -> bool:
        # Check if row/col is already visited; return false if it is
        if (row, col) in visited:
            return False
        # Check if row/col is even valid; return false if it isn't
        if not (0 <= row < len(board) and 0 <= col < len(board[0])):
            return False
        # Check if board[row][col] containers the char @ word[idx]; return false if it isn't
        if board[row][col] != word[idx]:
            return False

        # Did we just find our last character? Return True!
        if idx == len(word)-1:
            return True

        # Mark the cell as visited
        visited.add((row, col))

        dir_mods = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        return any(
            dfs(row+row_mod, col+col_mod, idx+1, visited.copy())
            for row_mod, col_mod in dir_mods
        )

    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(row, col, 0, set()):
                return True

    return False


assert exists([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED") == True
assert exists([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE") == True
assert exists([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB") == False
