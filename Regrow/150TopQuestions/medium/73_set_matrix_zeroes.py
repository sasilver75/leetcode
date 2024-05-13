"""
Set Matrix Zeroes

Given an `m*n` integer matrix `matrix`, if an element is 0,
set its ENTIRE ROW AND COLUMN to 0s!

You MUST do it "in place!"
"""

"""

Is there anything wrong with scanning through the grid, noting all of 
the cells that have a 0 in them, and THEN going through and, for each of them,
setting the column and row to zero? 

There would definitely be some repeated/unnecessary work
But let's start with that
"""


def set_matrix_zeroes_brute(grid: list[list[int]]) -> list[list[int]]:
    """
    We do a O(M*N) traversal of every cell to get all the zeroes.
    In the worst case, they're all zeroes already.
    For each of these zeroes (every cell), we then do a column-zero and row-zero,
    which is M+N work.
    So it's O((M*N)(M+N)), perhaps?
    """
    m = len(grid)  # N Rows
    n = len(grid[0])  # N Cols

    # Get the Zeroes
    zeroes = []
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 0:
                zeroes.append((row, col))

    # Zero out each row/col of each zero (repeated/unnecessary work here)
    for row, col in zeroes:
        # Zero the Row
        for c in range(n):
            grid[row][c] = 0
        # Zero the Col
        for r in range(m):
            grid[r][col] = 0

    return grid


"""
Okay... So what we're doing is zeroing rows and zeroing cols.
Instead of keeping track of the cells that have zeroes on them,
let's just keep track of the rows and cols that we have to zero (they can be done
independently).
"""

def set_matrix_zeroes(grid: list[list[int]]) -> list[list[int]]:
    n_rows = len(grid) # m
    n_cols = len(grid[0]) # n

    row_targets = set()
    col_targets = set()

    for row in range(n_rows):
        for col in range(n_cols):
            if grid[row][col] == 0:
                row_targets.add(row)
                col_targets.add(col)

    for row_target in row_targets:
        for col in range(n_cols):
            grid[row_target][col] = 0

    for col_target in col_targets:
        for row in range(n_rows):
            grid[row][col_target] = 0

    return grid


def set_matrix_zeroes_alt(grid: list[list[int]]) -> list[list[int]]:
    n_rows = len(grid)  # m
    n_cols = len(grid[0])  # n

    row_targets = set()
    col_targets = set()

    for row in range(n_rows):
        for col in range(n_cols):
            if grid[row][col] == 0:
                row_targets.add(row)
                col_targets.add(col)

    # Above is same as previous

    # Just scan through the whole grid once.
    for row in range(n_rows):
        for col in range(n_cols):
            if row in row_targets or col in col_targets:
                grid[row][col] = 0

    return grid


# -- Test --
def test(fn):
    assert fn([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]) == [
               [1, 0, 1],
               [0, 0, 0],
               [1, 0, 1]
           ]

    assert fn([
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5],
    ]) == [
               [0, 0, 0, 0],
               [0, 4, 5, 0],
               [0, 3, 1, 0]
           ]


test(set_matrix_zeroes_brute)
test(set_matrix_zeroes)
test(set_matrix_zeroes_alt)
