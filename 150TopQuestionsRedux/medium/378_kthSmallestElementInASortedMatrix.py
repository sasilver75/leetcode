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

We might 

"""
def kthSmallestNaive(matrix: list[list[int]]) -> int:
    pass


def test(fn):
    assert fn([
        [1,5,9],
        [10,11,13],
        [12,13,15],
    ], k = 8) == 13

    assert fn([
        -5
    ], k=1) == -5