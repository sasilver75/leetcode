"""
Spiral Matrix

Given an m*n matrix, return al elements of the matrix in spiral order


"""


"""
Key: use TRBL pointers

1   2   3   4
5   6   7   8
9   10  11  12

Needs to become: 1 2 3 4 8 12 11 10 9 5 6 7 8

USING TRBL pointers:

    TL          TR
  ST 1   2   3   4
     5   6   7   8
  SB 9   10  11  12

Do all the cells in the ST'th Row LEFT TO RIGHT
Do all the cells in the TR'th Column (besides the ST'th one and SB'th one) TOP TO BOTTOM
Do all the cells in the SB'th Row RIGHT TO LEFT
Do all the cells in the TL'th Column (besides hte SB'th one and ST'th one) BOTTOM TO TOP 

Then move pointers towards eachother

         TL  TR
      1   2   3   4
ST/SB 5   6   7   8
      9   10  11  12

Recurse
    if Special Cases: If we know that ST==SB: We have just one row
        We just go ACROSS (LR) the ST'th row, from TL to TR inclusive
    else Special Cases: If we know that TL==TR: We have just one column
        We just go DOWN (TB) the TL'th row, from ST to SB inclusive
        
Else, we just do our normal thing
"""

def spiral_order(matrix: list[list[int]]) -> list[int]:
    pass


assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]