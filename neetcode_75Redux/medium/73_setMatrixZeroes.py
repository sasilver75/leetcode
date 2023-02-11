"""
Set Matrix Zeroes

Given an m * n integer matrix MATRIX, if an element is 0, set its entire row and column to 0's

You must do it IN PLACE
"""

def set_zeroes(matrix: list[list[int]]):
    z_rows = set()
    z_cols = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                z_rows.add(row)
                z_cols.add(col)

    for r in z_rows:
        for r_col in range(len(matrix[0])):
            matrix[r][r_col] = 0

    for c in z_cols:
        for row in range(len(matrix)):
            matrix[row][c] = 0

    return matrix


assert set_zeroes([[1,1,1],[1,0,1],[1,1,1]])
assert set_zeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
