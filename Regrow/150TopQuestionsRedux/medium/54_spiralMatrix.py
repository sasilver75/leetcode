"""
Spiral Matrix

Given an m * n matrix, return all elements of the matrix in spiral order
This matrix is not necessarily a square matrix.
"""


"""
I think the idea here is that for every "layer" of the square, we're going to print the top side (L->R), right side (T->B), bottom side (R->L), left side (B->T)
Make sure not to "double count" the corner pieces
We can do this by keeping a ST,SB,TL,TR pointer to keep track of the edges of our current square.
A trick here though is that the matrix isn't necessarily going to be square - so it's possible that we'll eventually get to a point where there's just:
    - One row remaining (process that row left to right)
    - One col remaining (process that row top to bottom) ** <- Is this necessarily true?
    
Consider also the case in the first example where we'd only have a single cell left. In that case, it doesn't matter which we choose, as long as we just choose on of the strategies
above.
"""
def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    tl = 0
    tr = len(matrix[0])-1
    st = 0
    sb = len(matrix) - 1

    spiral_ordering = []

    while tl < tr and st < sb:
        # 1) Process Top Row (L -> R, Including all in row)
        for col in range(tl, tr+1):
            spiral_ordering.append(matrix[st][col])

        # 2) Process Right Col (T -> B, Not including top or bottom elements
        for row in range(st+1, sb):
            spiral_ordering.append(matrix[row][tr])

        # 3) Process Bottom Row (R -> L, Including all in row)
        for col in range(tr, tl-1, -1):
            spiral_ordering.append(matrix[sb][col])

        # 4) Process Left Col (B -> T, Not including top or bottom elements
        for row in range(sb-1, st, -1):
            spiral_ordering.append(matrix[row][tl])

        # Go to the next inner rectangle
        tl += 1
        tr -= 1
        st += 1
        sb -= 1

    # print(f"After squares: {spiral_ordering = }")

    # Is there just a Column left?
    if st == sb:
        for col in range(tl, tr+1):
            spiral_ordering.append(matrix[st][col])
    # Else, there's just a colum left
    elif tl == tr:
        for row in range(st, sb+1):
            spiral_ordering.append(matrix[row][tl])

    # print(f"Final: {spiral_ordering = }")
    return spiral_ordering




def test(fn):
    assert fn([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert fn([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


test(spiral_matrix)
