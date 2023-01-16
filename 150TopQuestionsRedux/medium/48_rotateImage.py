"""
Rotate Image

Given an n*n 2D square matrix representing an image, rotate the
image by 90 degrees (clockwise)

You have to rotate the image IN-PLACE by modifying the matrix directly!
"""

"""
Let's assume that we had a swap(row, col) function that, given a target cell, swapped in-place the four cells (including target cell) that need rotating.
Which target cells would we call swap on?

    1   2   3   4   5       _   _   _   _   _
    6   7   8   9   10      _   7   8   9   _
    11  12  13  14  15  ->  _   12  13  14  _
    16  17  18  19  20      _   17  18  19  _
    21  22  23  24  25      _   _    _  _   _
    
For each "layer" of the square, call swap(row, col) on every cell in the top row besides the last cell.
To process layers of the squarwe, let's maintain four points -- a SideTop, SideBottom, TopLeft, and TopRight
 
 Note that the matrix isn't necessarily going to be a square matrix.
 NEVERMIND, it actually is, if you look at the constraints. That makes this a lot easier.
"""

def print_matrix(matrix, is_before=True):
    print(f"Printing Matrix {'BEFORE' if is_before else 'AFTER'}")
    for row in matrix:
        print(row)

def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    def rotate_cell(st: int, sb: int, tl: int, tr: int, offset: int) -> None:
        """
        Given target cell (row, col) and the dimensions of the matrix, how do we determine which are the other three cells to use?
        The "Top Left" cell is the row, col cell: [row, col]
        The "Top Right" cell: [row, length(matrix[0]-col-1]
        The "Bottom Left" cell: [length(matrix)-row-1, col]
        The "Bottom Right" cell: [length(matrix)-row-1, length(matrix[0]-col-1)
        """
        targets = [
            [sb-offset, tl],  # Bottom Left
            [sb, tr-offset],  # Bottom Right
            [st+offset, tr],  # Top Right
            [st, tl+offset],  # Top Left
        ]
        print(f" Preparing to swap {targets}")
        print_matrix(matrix)
        tmp_value = matrix[targets[0][0]][targets[0][1]]  # This will be used to overwrite the top left cell. Its' the VALUE here, not the
        for i in range(len(targets) - 1):
            target_row, target_col = targets[i]
            source_row, source_col = targets[i + 1]
            matrix[target_row][target_col] = matrix[source_row][source_col]

        matrix[targets[-1][0]][targets[-1][1]] = tmp_value

        print_matrix(matrix, False)

    side_top = 0
    side_bottom = len(matrix) - 1
    top_left = 0
    top_right = len(matrix[0]) - 1

    # What should this condition be?
    while side_top < side_bottom and top_left < top_right:
        # Call swap on all of the top row cells besides the last one
        for offset in range(0, top_right - top_left):
            rotate_cell(side_top, side_bottom, top_left, top_right, offset)

        side_top += 1
        side_bottom -= 1
        top_left += 1
        top_right -= 1


    print("END: ")
    print_matrix(matrix)
    return matrix


def test(fn):
    """
    1   2   3       7   4   1
    4   5   6  ->   8   5   2
    7   8   9       9   6   3
    """
    # assert fn([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    """
    5   1   9   11          15  13  2   5
    2   4   8   10   ->     14  3   4   1
    13  3   6   7           12  6   8   9
    15  14  12  16          16  7   10  11
    """
    assert fn([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) == [[15, 13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7, 10, 11]]


test(rotate_matrix)
