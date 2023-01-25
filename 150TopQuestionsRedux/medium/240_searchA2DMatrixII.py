"""
Search a 2D Matrix

Write an efficient algorithm for search for a value `target` in an m*n integer
matrix `matrix`. This matrix has the following properties:

1. Integers in each row are sorted in ascending order from left to right
2. Integers in each column are sorted in ascending order from top to bottom

Example:


    1   4   7   11  15
    2   5   7   12  19
    3   6   9   16  22
    10  13  14  17  24
    18  21  23  26  30

Above: notice that all rows are sorted ASC (L->R) and all columns are sorted
ASC (T->B).
"""

"""
Well... what's the naive way that we could do this?
What if we binary-searched each row (which is ASC) for the target?
    - For an m*n matrix, this is mlog(n)

or 

What if we binary-searched each column (which is ASC) for the target?
    - For an m*n matrix, this is nlog(m)
    
Ideally, we would do the one of these that's shorter. IE if the columns are 
longer, when we binary search along the columns.
"""


def binary_search(nums: list[int], target: int) -> bool:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        mid_v = nums[mid]

        if mid_v == target:
            return True
        elif target < mid_v:
            r = mid - 1
        else:
            l = mid + 1
    return False


def search_matrix_naive(matrix: list[list[int]], target: int) -> bool:
    for row in matrix:
        if binary_search(row, target):
            return True
    return False


"""
How can we be smarter?

Let's say we're searching for [5]
Let's start in the top-right position
                    
            C
R   1   4   7   11 (15)
    2  [5]  7   12  19
    3   6   9   16  22
    10  13  14  17  24
    18  21  23  26  30    

At (15): What can we we say about what we should do re: R or C, without knowing the reules?
    - Could the value be in this column, or should we consider the column to the left?
        - Yes is target >= first value in column
            > (Look to consider which row)
        - No if target < first value in column
            > Look at the Left Column 

    - Could the value be in this row, or should we consider the row below?
        - Yes if target >= first value in row
            ...
        - No if target < first value in row
        

TLDR: Repeatedly asking the question, given an index: 
    - Could the target be in this column C (restricted by R), or should we consider the left column?
    - Could the target be in this row R (restricted by C), or should we consider the below column?
I think it'd be fine to start in any corner using this logic. 
"""
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    r = 0
    c = len(matrix[0]) - 1
    while r != c:
        print(f"{r = } {c = } Searching for {target}, looking at {matrix[r][c]}")
        if matrix[r][c] == target:
            return True

        # Could the target be in this column, or should we consider the column to the left? (Can't go left of the first col)
        # Note: This column is constrained by the current value of R
        if c > 0:
            # Target can't be in this col if it's less than the starting value of this col (which starts at row r)
            if target < matrix[r][c]:
                c -= 1

        # Could the target be in this row, or should we consider the row below? (Can't go below the last row)
        # Note: This row is constrained by the current value of C
        if r < len(matrix)-1:
            # Target can't be in this row if it's less than the first value in the row
            if target > matrix[r][c]:
                r += 1

    # Did we find our target?
    return matrix[r][c] == target



def test(fn):
    """ C
  R 1   4   7   11  15
    2  [5]  7   12  19
    3   6   9   16  22
    10  13  14  17  24
    18  21  23  26  30
    """
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 7, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert fn(matrix, 5) == True
    assert fn(matrix, 20) == False


# test(search_matrix_naive)
test(search_matrix)
