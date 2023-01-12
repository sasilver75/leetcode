"""
Roate Image

You are given an n*n 2D Matrix represneting an image
Rotate the image by 90 degree (CLOCKWISE)

You have to rotate the image IN-PLACE, which means that you have to modify
the input 2D Matric Directly. Do NOT allocate another 2d matrix to do rotation.
"""

"""
Let's have an example Grid

    1   2   3                       7   4   1
    4   5   6           -->         8   5   2
    7   8   9                       9   6   3

I notice first that the center element doesn't seem to have to move -- but there are 
square matrices that are even-lengthed and don't have a center element, and all elements move.
So that isn't very interesting.

N = 3  (length)
[0, 1] swaps with [1,2]
[1, 2] swaps with [2, 1]
[2, 1] swaps with [1, 0]
[1,0] swaps with [0, 1]

No obvious common relationship with those, to me...

Row 0 becomes column 2
Row 1 becomes column 1
Row 2 becomes column 0
...
Row X becomes column N - X - 1

But one of the problems that we're going to have to deal with is that we 
have to do the swap "in place" -- I don't know if that means that we can't
allocate additional memory or not.

However we determine to swap A with B, it seems like... once we start swapping,
we have to continue swapping?
Or perhaps it's like:

for element in topRow:
    swap # performs 4 swaps recursively, or something
    
But this would only swap the elements on the outside...

for row in ceil(nRows/2):
    for rowCol in currentRow:
        swap(row, rowCol) # Performs 4 swaps

But even that wouldn't be right... I mean imagine we're talking about our
        1   2   3
        4   5   6
        7   8   9
matrix above. We'd do a swap(...) on each of the first row elements (which acutually
in this case would solve the whole thing) and then we'd go to the second row and do
an accidental SECOND rotation started at mat[1][0] and mat[1][2]. Nope.

Let's look at a bigger matrix...
        1   2   3   4
        5   6   7   8
        9   10  11  12
        13  14  15  16

In this one it seems like we would want to do a swap(...) on each of the
elements of the first row, which would solve the outermost layer
Then on the second row, we'd want to swap only the "inner" elements, starting
at [1][1] and [1][2]

Let's look at a slightly larger one
        1   2   3   4   5
        6   7   8   9   10
        11  12  13  14  15
        16  17  18  19  20
        21  22  23  24  25
In this one we'd want to start swaps on the elements that I'll highlight below
        1   2   3   4   _
        _   7   8   9   _
        _   _   _   _   _   <-- This could actually be ignored, couldn't it
        _   _   _   _   _
        _   _   _   _   _
Note that I left out the top-right one! Because that's where the 1 @ [0][0] is
going to swap to.
        
And for a bigger one: N=6
        1   2   3   4   5   _       (row0)
        _   8   9   10  _   _       (row1)
        _   _   15  _   _   _       (row2)
        _   _   _   _   _   _
        _   _   _   _   _   _
        _   _   _   _   _   _
        
        0   1   2   3   4   5
        
This of course makes sense now that we know that we're "rotating" a quarter
of the square around.

Given that it's an N*N matrix, what sort of set of expressions could we use to
set up our swaps, given hte examples above?

for row in N // 2:
    for col in range(0+row, N-row-1):
        swap(row, col)
        
Great! So now that we know that we need to swap on these elements,
Given that we're on a small matrix like 
N=3:
        1   2   3
        4   5   6
        7   8   9

And we're swapping 2@[0,1], how do we know the indexes that will be involved
with swapping?

N=3:
[0,0] -> [0,2], [2,2], [2,0]
[0,1] -> [1,2], [2,1], [1,0]
...
[a,b] -> [b, N-1-a], [N-1-a, N-1-b], [N-1-b, a] ?

Does this work on [0,1]? for N=3
[a,b] -> [0,1] -> [1, 2], [2, 1], [1,0]    Yes

What about for 7@[1,1] on an N=5?
        1   2   3   4   5
        6  (7)  8  (9) 10
        11  12  13  14  15
        16 (17)  18 (3)  20
        21  22  23  24  25

[a,b] -> [1,1] -> [1, 3], [3, 3], [3, 1] ? Yes!

"""


def rotate(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)

    def swap(row, col):
        """
        Given [row,col] -> [col, N-1-row], [N-1-row, N-1-col], [N-1-col, row] are the interesting cells
        We need to do a CLOCKWISE rotation

        So given        1       2
                        4       3

        We need         4       1
                        3       2

        If those were in list form. [1,2,3,4] becomes [4, 1, 2, 3]

        Note: This might break the memory rules. See my second solution for a better option.
        """

        locations = [
            (row, col),
            (col, n - 1 - row),
            (n - 1 - row, n - 1 - col),
            (n - 1 - col, row),
        ]
        values = [
            matrix[r][c] for r, c in locations
        ]
        rotated_values = [values[3], *values[0:3]]

        for location, newValue in zip(locations, rotated_values):
            r, c = location
            matrix[r][c] = newValue


    for row in range(n // 2):
        for col in range(row, n - row - 1):
            swap(row, col)

    print(matrix)
    return matrix

# --- Neetcode: https://youtu.be/fMSJSS7eO1w
"""
    1   2   3           7   4   1
    4   5   6     -->   8   5   2
    7   8   9           9   6   3
    
It's a square matrix. Notice that rotating the image by 90 degrees clockwise
means that we're turning the "first row" in the "last column", above.

The challenge here is definitely doing it in-place.
The problem is... when you're moving the 1 to where the 3 is, you have to figure
out what you want to do with the 3, before you overwrite it.
Because that 3 should be moved to where the 9 is,
and that 9 should be moved to where the 3 is,
and that 7 should be moved to where the 1 is.

So 1/3/7/9 are connected, but there are still values in the outer layer that
need moving
Namely 2/6/8/4 need to be rotated as well.

We're going to do this in O(N^2) time, meaning we only have to look at each cell once.
Memory complexity should be constant O(1)

We're going to rotate the outermost square, then the innermost square.

        5   1   9   11
        2   4   8   10
        13  3   6   7
        15  14  12  16

We know that 5 -> 11 -> 16 -> 15 -> 5 is going to occur
And we'll keep doing that with every element in the top row.

        L           R    
     T  5   1   9   11
        2   4   8   10
        13  3   6   7
     B  15  14  12  16
     
     Neet uses these TBLR (top bottom left right) pointers to keep track of the recursion

The idea is that we rotate the outer edge of the square, and then recurse on the interior square
 which is also going to be a square matrix subproblem.
 We just take our TBLR pointers and move them "inwards"
 
            L   R    
        5   1   9   11
     T  2   4   8   10
     B  13  3   6   7
        15  14  12  16
        
And we're just doing this "WHILE L < R" (or T < B, whatever - it's square)

So how did the swapping work with the temporary variables?
It's easiest to do it in reverse/counterclockwise order, which only requires one tmp.

        5   _   _   11
        _   _   _   _
        _   _   _   _
        15  _   _   16

1) Store 5 in a temporary variable tmp
2) "Shift" 15 to 5, overwriting 5
3) "Shift" 16 to 15, overwriting 15
4) "Shift" 11 to 16, overwriting 16
5) "Shift" tmp to 11, overwriting 11 with 5

See Here: https://ibb.co/hMHBnWN
        
"""

def neetcode_rotate(matrix: list[list[int]]) -> list[list[int]]:
    left, right = 0, len(matrix) - 1

    while left < right: # For each layer
        for i in range(right - left): # For each element in layer that needs swapping
            top, bottom = left, right

            # Save the Top Left value
            tmp = matrix[top][left + i]

            # move BottomLeft into TopLeft
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottomRight into topLeft
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move topRight into bottomRight
            matrix[bottom][right - i] = matrix[top + i][right]

            # move tmp into topRight
            matrix[top + i][right] = tmp

        left += 1
        right -= 1

    return matrix

# -- Test Zone: Confirm that I've actually copied these down correctly if FAIL

def test(fn):
    assert fn([ # N=3
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]) == [
               [7, 4, 1],
               [8, 5, 2],
               [9, 6, 3]
           ]

    assert fn([
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]) == [
               [15, 13, 2, 5],
               [14, 3, 4, 1],
               [12, 6, 8, 9],
               [16, 7, 10, 11]
           ]

test(rotate)
test(neetcode_rotate)
