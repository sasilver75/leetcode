"""
Longest Increasing Path in a Matrix
Difficulty: HARD

Given an m * n integers grid `matrix`, return the LENGTH of the longest
INCREASING path in matrix!

From each cell, you can move only in the fourth cardinal directions. You cannot
"wrap" around the sides of the list (ie go out of bounds and come out on the other side)
"""


def longest_increasing_path_naive(grid: list[list[int]]) -> int:
    longest = 0

    def dfs(row: int, col: int, visited: set[tuple]):
        nonlocal longest
        """
        Called on an unvisited cell, visit the cell, update longest
        and then recurse on unvisited increasing neighboring cells
        """
        visited.add((row, col))

        dir_mod = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for row_mod, col_mod in dir_mod:
            target_row = row + row_mod
            target_col = col + col_mod

            # Recurse on all on-board, unvisited, ascending neighbors
            if (
                    0 <= target_row < len(grid)
                    and 0 <= target_col < len(grid[0])
                    and (target_row, target_col) not in visited
                    and grid[target_row][target_col] > grid[row][col]
            ):
                dfs(target_row, target_col, visited.copy())

        longest = max(longest, len(visited))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            dfs(r, c, set())

    return longest


"""
Whelp, I suppose there's some sort of caching solution here. I guess that 
does make sense. I think it would have to be characterized by your 
current position and the spaces that you've used.

dp = {
    (row, col, set((visited_row,visited_col), ...)): length of longest increasing path from here
}

But this dp would only really be useful to us if we'd visited exactly the same
cells as some past traversal. What are the odds of that? It doesn't seem SUPER high!
But it's possible...

The recursive bit would be 1 + max(neighbors), right? 
"""


def longest_increasing_path(grid: list[list[int]]) -> int:
    """
    So this solution "doesn't run" right now.
    I can't tell if it works -- the problem is that "set" isn't hashable,
    so we can't use (int, int, set) as a key in the dp dict.

    We could get around that with a bunch of linear searches and recasting
    from list of visited cells to a tuple before hashing it... but that sucks.

    surely there's a better option from neetcode.

    Edit: Oh, yeah it's some horrifying crackhead insight solution.
    Not interested in this! :)
    """
    dp = {}

    dir_mods = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]

    def is_on_board(row: int, col: int) -> bool:
        return (
                0 <= row < len(grid)
                and 0 <= col < len(grid[0])
        )

    def dfs(row: int, col: int, visited: set[tuple]) -> int:
        # Base Case 1: The answer to this is in cache
        current_key = (row, col, visited)
        if current_key in dp:
            return dp[current_key]

        # Visit current cell
        visited.add((row, col))

        # Base Case 2: We can't visit any adjacent cells ("We can't go anywhere)
        # If it's either not a valid cell
        #   Or it IS a valid cell and either:
        #       - we've visited it
        #       - it's non-increasing
        if all(
                not is_on_board(target_row, target_col) or (
                    is_on_board(target_row, target_col) and (
                        (target_row, target_col) in visited
                        or grid[target_row][target_col] <= grid[row][col]
                    )
                )
                for row_mod, col_mod in dir_mods
                for target_row, target_col in ((row + row_mod, col + col_mod),)
        ):
            dp[current_key] = len(visited)
            return dp[current_key]

        # We know that at least one adjacent cell is recursible into
        ans = max(
            dfs(target_row, target_col, set.copy())
            for row_mod, col_mod in dir_mods
            for target_row, target_col in ((row+row_mod, col+col_mod),)
            if is_on_board(target_row, target_col)
            and (target_row, target_col) not in visited
            and grid[target_row][target_col] > grid[row][col]
        )
        dp[current_key] = ans
        return dp[current_key]

    length = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            length = max(length, dfs(row, col, set()))

    return length


def test(fn):
    assert fn([
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]) == 4

    assert fn([
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]) == 4

    assert fn([[1]]) == 1


test(longest_increasing_path_naive)
test(longest_increasing_path)
