"""
Rotate Image
Category: Matrix

You are given an `n * n` 2D matrix representing an image

Rotate the image by 90 degrees (clockwise)

You have to rotate the image IN-PLACE, meaning you have to
modify the input 2D matrix directly.
Do NOT allocate another 2D matrix and do the rotation!
"""

"""
Given an index, what are the four indices involved with rotations?
USEFUL NOTE: The matrix that we're going to be given is a SQUARE matrix (n*n)


        14  13  2   5   5
        14  3   4   1   4
        12  6   8   9   3
        16  7   10  11  2
        12  4   9   2   14
    
    Say we had some SWAP function that took care of determining which
    indices to swap with when we invoked it with swap(row, col)
    
    Which elements would we have to call it on?
        
        14  13  2   5   _
        _   3   4   _   _
        _   _   _   _   _
        _   _   _   _   _
        _   _   _   _   _
        
    I've left the center one as _ becasue we don't technically have to 
    call it on that square.
    For each "Square", we're calling SWAP(...) on all of the cells
    along the top row, besides the last cell in the top row.
    
    And if we used 4 pointers to keep track of the square:

        TL              TR
    ST  14  13  2   5   5
        14  3   4   1   4
        12  6   8   9   3
        16  7   10  11  2
    SB  12  4   9   2   14
    
    then
    
            TL     TR
        14  13  2   5   5
    ST  14  3   4   1   4
        12  6   8   9   3
    SB  16  7   10  11  2
        12  4   9   2   14
        
What we we really care about is the ST'th row, from TL -> TR (inclusive),
ignoring the TR'th element.
And we'd be doing this series of swaps (and shifting 4pointers) while
ST < SB. When ST == SB, we necessarily are looking at a single-cell-square,
which we can skip.

Notice that we actually don't even need the SB pointer except for this exit
condition -- but because it's a square matrix, we could also easily use
While TL < TR as an exit condition, so let's just NOT even use an SB!

Okay, now for the swap logic...

Given that I have:

            TL     TR
        14  13  2   5   5
    ST  14  3   4   1   4
        12  6   8   9   3
    SB  16  7   10  11  2
        12  4   9   2   14
        
    And I'm calling Swap(1,2) to swap [4, 9, 10, 6], how do I determine the indices
    to swap?
    
    N = 5
    TL = 1
    TR = 3
    ST = 1
    SB = 3
    
    I think one way of looking at it is that... given that we're 
    calling swap(row, col) across teh entire top row...
     
     for targetCol in range(0, tr - tl):  #  ignore the TR'th col, remember
        swap[st][targetCol]
    
     given that the "row" is "shrinking" at each layer...
     Say we're calling it on matrix[1][2]
     We're really calling it on 3rd column ([2]), but within the given row,
     we're really calling it on the 2nd "effective" column, which is 
     targetCol - TL = 1
     
     So to generate the three other indices:
     
    swap(row=1,col=2)
     
    N = 5
    TL = 1
    TR = 3
    ST = 1
    SB = 3
    
    delta = col - TL = 2 - 1 = 1  (ie we're operating on the 1'th col of the given square
        enscribed by TL/TR/ST/SB 
        
    So the other three ones are:
        [st+delta, tr] for right side
        [sb, tr - delta] for bottom
        [sb-delta, tl] for left
        
        (with the one it was called on was below, but we don't need to calculate it)
        [st, tl+delta]
        
    
    
    
    


"""

def print_matrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])

def rotate(matrix: list[list[int]]) -> list[list[int]]:
    tl = 0
    tr = len(matrix[0]) - 1
    st = 0
    sb = len(matrix) - 1

    def swap(row: int, col: int, tl: int, tr: int, st: int, sb: int, matrix) -> None:
        delta = col - tl

        print("\n Before: ")
        print_matrix(matrix)
        cells = [ # Make sure to get the order right here; they should be going in any clockwise order
            [sb - delta, tl],
            [sb, tr - delta],
            [st+delta, tr],
            [row, col],
        ]
        print(cells)
        tmp_value = matrix[cells[0][0]][cells[0][1]] # VALUE of cells[1]

        for idx, pair in enumerate(cells[:-1]):
            target_row, target_col = pair
            source_row, source_col = cells[idx+1]
            matrix[target_row][target_col] = matrix[source_row][source_col]


        # Process last one
        target_row, target_col = cells[-1]
        matrix[target_row][target_col] = tmp_value

        print("After: ")
        print_matrix(matrix)

    while st < sb:
        for i in range(tr - tl):
            swap(st, tl + i, tl, tr, st, sb, matrix)

        st += 1
        sb -= 1
        tl += 1
        tr -= 1

    return matrix


def test(fn):
    assert fn([
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