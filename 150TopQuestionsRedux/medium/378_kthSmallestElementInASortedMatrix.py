"""
378 Kth Smallest Element in a Sorted Matrix

Given an n*n matrix (SQUARE) where each of the
rows and columns is sorted in ascendign order, return the Kth smallest
element in the matrix!

Note that the kth smallest element in the sorted order, not the kth
distinct element.

Find a solution with a memory complexity better than O(N^2)
"""

"""
Here's the idea that I'm thinking of:

We want to find the Kth Smallest Element in a Sorted Matrix!

Since the ROWS and COLUMNS are sorted in the ascending order,
- we know that the MAXIMUM element is in the bottom-right corner
- we know that the MINIMUM element is in the bottom-right corner

So given the matrix :
 
    1   5   9
    10  11  13
    12  13  15

Without looking at the whole matrix, we know that every element in the matrix
is going to be in the range [1, 15]

Could we do some sort of binary search on the RANGE, above? Where we sort of 
evaluate as a given point: 
    -"How many elements in the matrix are there that 
    are smaller than this number?"

And we could do that by doing a binary search on each row in the matrix
for the element (just greater than) our queried number, and sum
the number of elements per row.

So for the range 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]   Length=14
                      ^
                      
We determine that the middle element is 8. 
Here, we're _guessing_ that 8 is the element that has k elements <= it in the matrix

The compare this guess (that k elements <= guess) to the actual (# of elements <= it) and adjust our search accordingly

We need:
- n_lte(nums: list[int], guess: int) -> int
    - Returns the number of elements in sorted list `nums` that are <= `guess`, using binary search to search for the rightmost occurrence of guess
- get_matrix_lte(guess: int) -> int:
    - Wraps n_lte and returns the number of elements <= guess in the entire board 
- binary search routine on the range from [matrix[0][0], matrix[-1][-1]]

"""


def n_lte(nums: list[int], guess: int) -> int:
    """Count the number of elements in sorted list `nums` <= `guess` using binary search"""
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        mid_v = nums[mid]

        if mid_v <= guess:
            l = mid + 1
        else:
            r = mid - 1

    return l


assert n_lte([1, 2, 3, 3, 4, 5, 6, 7], 1) == 1
assert n_lte([1, 2, 3, 3, 4, 5, 6, 7], 2) == 2
assert n_lte([1, 2, 3, 3, 4, 5, 6, 7], 3) == 4
assert n_lte([1, 2, 3, 3, 4, 5, 6, 7], 4) == 5
assert n_lte([1, 2, 3, 3, 4, 5, 6, 7], 7) == 8
assert n_lte([1,2,3,3,3,4,5,6,8], 0) == 0
assert n_lte([1, 2, 3, 3, 3, 4, 5, 6, 8], 1) == 1
assert n_lte([1, 2, 3, 3, 3, 4, 5, 6, 8], 2) == 2
assert n_lte([1, 2, 3, 3, 3, 4, 5, 6, 8], 3) == 5
assert n_lte([1, 2, 3, 3, 3, 4, 5, 6, 8], 4) == 6
assert n_lte([1, 2, 3, 3, 3, 4, 5, 6, 8], 8) == 9


def n_lte_board(board: list[list[int]], guess: int):
    count = 0
    for row in board:
        count += n_lte(row, guess)

    # print(f"{guess = }: {count =}")
    return count


def kthSmallestNaive(matrix: list[list[int]], k:int) -> int:
    """
    Key: An important part of the setup is that l and r start at the inclusive
    ends of the range of values that could be in matrix
    """
    l = matrix[0][0]
    r = matrix[-1][-1]

    """
    Key: This binary search needs to resolve to the SMALLEST value for which {(count elements <= value) == k}, I think
    This is necessarily going to give us a value that's actually in matrix!
    """
    while l <= r:
        mid = l + (r - l) // 2

        if n_lte_board(matrix, mid) >= k:
            r = mid - 1
        else:
            l = mid + 1

    return l



def test(fn):
    assert fn([
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
    ], k=8) == 13

    assert fn([
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
    ], k=2) == 5

    assert fn([
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
    ], k=5) == 11

    assert fn([
        [-5]
    ], k=1) == -5

test(kthSmallestNaive)