"""
Set Matrix Zeroes
Category: Matrix

Given an m*n integer matrix `matrix`, if an element is 0, set its
entire row and column to 0s.

You must do it IN PLACE
"""

"""
Here's the naivest solution:
    * Enuemrate all of the (row,col) pairs that contain a zero
    * For each (r,c) pair:
        - Zero out the matrix[r][_] cells
        - Zero out the matrix[_][c] cells
"""
def set_zeroes_naive(matrix: list[list[int]]) -> None:
    zeroes = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                zeroes.append((row, col))

    for z_row, z_col in zeroes:
        # Zero the row
        for col in range(len(matrix[0])):
            matrix[z_row][col] = 0

        # Zero the column
        for row in range(len(matrix)):
            matrix[row][z_col] = 0

    return matrix

"""
We can't do better than O(N) time. But can we do better than O(m*n) memory?
Yes - there's a small optimization to the previous one.
If two cells in the same row contain 0's, there's no point in zeroing out
the same row twice. So instead of keeping track of the (row, col) pairs 
that need to be zeroed, let's in instead:
    * Enumerate all the of the rows[] and columns[] that contain 0's
    * Zero all rows
    * Zero all columns 
    
This is O(M+N), since we at most would enumerate {every column} + {every row}
"""
def set_zeroes_better(matrix: list[list[int]]) -> None:
    z_rows = []
    z_cols = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                z_rows.append(row)
                z_cols.append(col)

    # Zero the z_rows
    for z_row in z_rows:
        for col in range(len(matrix[0])):
            matrix[z_row][col] = 0

    # Zero the cols
    for z_col in z_cols:
        for row in range(len(matrix)):
            matrix[row][z_col] = 0

    return matrix


"""
Can we do better than O(M+N) space complexity, retaining O(M+N) time?
Neetcode: https://www.youtube.com/watch?v=T41rL0L3Pnw

Is there a way that we can take the array of z_rows and the array of 
z_cols and PUT IT INTO the matrix, so we don't use additional space?

            1   0   1
            1   0   1
            0   1   1
            
Before in z_row, z_col, we were effectively using additional lists of 
length m and n. Pretty much we were constructing this:

z_cols =   [1,  1,  0]   <~ In some metaphorical, it's like a boolean vector
z_rows: [1] 1   0   1
        [1] 1   0   1
        [1] 0   1   1
        [1] 0   0   1

Our goal is to move these z_cols and z_rows INTO the matrix, rather than
have them be outside. What we're going to do is to be overwriting elements on
the leftmost col and the topmost row to indicate when a row or a column has 0's 
in it, and needs to be zeroed out.

One thing to note on is that there's "overlap" between these two lists, in the 
top-right-most. So we'll have to have one additional register to keep track of 
0'th row, since [0][0] is going to refer to 0'th column for us.
"""
def set_zeroes_best(matrix: list[list[int]]) -> list[list[int]]:
    n_rows, n_cols = len(matrix), len(matrix[0])
    row_zero = False # "first row is "Not" zero (yet)

    # Determine which rows/columns need to be zeroed
    for row in range(n_rows):
        for col in range(n_cols):
            if matrix[row][col] == 0:
                # Mark the Column
                matrix[0][col] = 0

                # Mark the Row
                if row > 0:  # For row zero, we have that dedicated register
                    matrix[row][0] = 0
                else:
                    row_zero = True

    # Through board again, ignoring first row and first column (since we rely on them to "repopulate" the interior of the board)
    for row in range(1, n_rows):
        for col in range(1, n_cols):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0

    # col_zero check
    if matrix[0][0] == 0:
        for row in range(n_rows):
            matrix[row][0] = 0

    # row_zero check
    if row_zero:
        for col in range(n_cols):
            matrix[0][col] = 0

    return matrix


# -- Test Zone --
def test(fn):
    assert fn([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    assert fn([
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


test(set_zeroes_naive)
test(set_zeroes_better)
test(set_zeroes_best)
