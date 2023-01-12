"""
Spiral Matrix

Given an m x n matrix, return ALL elements of the matrix in SPIRAL ORDER

> Assuming M != N necessarily
"""


"""
Thinking:

    1   2   3
    4   5   6       ->      1   2   3   6   9   8   7   4   5
    7   8   9
    

    1   2   3   4
    5   6   7   8   ->  1   2   3   4   5   6   7   8   9   10  11  12
    9  10   11  12
    
Because they're not necessarily square matrices, so it's not like our
recursive case can be "Do the next layer in," can we? Or can we?
Maybe it's just that we have to define what "next layer in" means.

Let's look at a little bit of a bigger matrix -- I think we can do this
while managing four pointers TRBL (Top Right Bottom Left)

     1  2   3   4   5
     6  7   8   9   10
     11 12  13  14  15
     16 17  18  19  20
     
     Ans:   1   2   3   4   5   10  15  20  19  18  17  16  11  6  ...
            7   8   9   12  13  14
    
I used a ... to denote where I think the second recursive call might start.

Starting position of TRBL for first call
     L              R   
   T 1  2   3   4   5
     6  7   8   9   10
     11 12  13  14  15
   B 16 17  18  19  20

Starting position of TRBL for second call
        L       R   
     1  2   3   4   5
   T 6  7   8   9   10
   B 11 12  13  14  15
     16 17  18  19  20

I think we do this while (T >= B AND L <= R) ?
And each iteration we:
L += 1, R -= 1
T += 1, B -= 1

Because imagine a verry skinny array like
    L   R
  T 1   2
    3   4 --> 1 2 4 6 8 7 5 3 ...
    5   6           (And then we do our next recursive call, where L > R,
  B 7   8               so we don't do anything.
  
But now what describes the cells that we visit, given a TRBL (and M + N)?

Say we're in the first recurrence relationship of 
        
    L           R
  T 1   2   3   4       M = 3
    5   6   7   8       N = 4
  B 9   10  11  12

    L=0, R=3
    T=0, B=2
    
There might be something clever... But can we just do this?
1) Visit all Cells in the T'th Row where L <= CellCol <= R
2) Visit all Cells in the R'th Column where T < CellRow < B   (Notice not inclusive to avoid double counting)  
3) Visit all Cells in the B'th Row where L <= CellCol <= R (Notice same RULES as 1)
4) Visit all Cells in the L'th Column where T < CellRow < B
"""


def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    """
    Spirally traverse an m*n matrix    (m rows, n cols)
    """
    m = len(matrix)
    n = len(matrix[0])
    trail = []

    def helper(l: int, r: int, t: int, b: int):
        if l > r or t > b: # Exhausted
            return

        if l == r and t == b: # Center single element
            trail.append(matrix[l][t])
            return


        # 1) Visit all Cells in the T'th Row where L <= CellCol <= R
        for col in range(l, r+1): # Left to Right (inclusive)
            trail.append(matrix[t][col])

        if t != b: # If there's actually more than one row in the current iteration
            # 2) Visit all Cells in the R'th Column where T < CellRow < B   (Notice not inclusive to avoid double counting)
            for row in range(t+1, b): # Top to Bottom (exclusive)
                trail.append(matrix[row][r])

            # 3) Visit all Cells in the B'th Row where L <= CellCol <= R (Notice same RULES as 1)
            for col in range(r, l - 1, -1): # Right to Left (inclusive)
                trail.append(matrix[b][col])

            # 4) Visit all Cells in the L'th Column where T < CellRow < B
            for row in range(b-1, t, -1): # Bottom to Top (exclusive)
                trail.append(matrix[row][l])

        # Recurse
        print("Trail after iteration: ", trail)
        helper(l+1, r-1, t+1, b-1)


    helper(0, n - 1, 0, m - 1)
    print(trail)
    return trail

"""
     L           R
T    1   2   3   4
     5   6   7   8
B    9   10  11  12
"""

def test(fn):
    assert fn([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert fn([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

test(spiral_matrix)