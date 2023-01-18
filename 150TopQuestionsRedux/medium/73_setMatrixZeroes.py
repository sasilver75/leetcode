"""
Set Matrix Zeroes

Given an m * n integer matrix, if an element is 0, set
its entire row and column to 0s. You must do this in-place.
"""


def set_matrix_zeroes_naive(matrix: list[list[int]]) -> None:
    # TODO[SAM]: Input Validation/Early Returns
    zero_coordinates = []
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] == 0:
                zero_coordinates.append([row_idx, col_idx])

    def zero_row(row_idx: int) -> None:
        for col_idx in range(0, len(matrix[0])):
            matrix[row_idx][col_idx] = 0

    def zero_col(col_idx: int) -> None:
        for row_idx in range(0, len(matrix)):
            matrix[row_idx][col_idx] = 0

    for row_idx, col_idx in zero_coordinates:
        zero_row(row_idx)
        zero_col(col_idx)


def set_matrix_zeroes(matrix: list[list[int]]) -> None:
    rows = []
    cols = []
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] == 0:
                rows.append(row_idx)
                cols.append(col_idx)

    def zero_row(row_idx: int) -> None:
        for col_idx in range(0, len(matrix[0])):
            matrix[row_idx][col_idx] = 0

    def zero_col(col_idx: int) -> None:
        for row_idx in range(0, len(matrix)):
            matrix[row_idx][col_idx] = 0

    for row_idx in rows:
        zero_row(row_idx)
    for col_idx in cols:
        zero_col(col_idx)




def test(fn):
    b1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    fn(b1)
    assert b1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    b2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    fn(b2)
    assert b2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

test(set_matrix_zeroes_naive)
test(set_matrix_zeroes)
