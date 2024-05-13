"""
Spiral Matrix
Category: Matrix

Given an `m x n` matrix, return all elements of the
matrix in SPIRAL ORDER!
"""

"""
        1   2   3   4   5
        6   7   8   9   10
        11  12  13  14  15
        16  17  18  19  20
        21  22  23  24  25
        
        
        1   2   3   4   5
        6   7   8   9   10
        11  12  13  14  15
        16  17  18  19  20
        
        1   2   3
        4   5   6
        7   8   9
        10  11  12
        13  14  15
        
# Using topLeft (tl) and topRight(tr) and sideTop and sideBottom (st, sb) pointers
while tl <= tr and rt <= rb:
    # Traverse across top row left to right (inclusive of all elements)
    # Traverse across right column top to bottom (skipipng top/bottom)
    # Traverse across bottom row right to left (inclusive of all elementS)
    # Traverse across left column bottom to top (skipping top/bottom)
"""
def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    acc = []
    tl, tr = 0, len(matrix[0]) - 1
    st, sb = 0, len(matrix) - 1

    # Special case when all tr == tr and st == sb, or just one? Should == be in this loop?
    while tl < tr and st < sb:
        # Traverse Top Row Left to Right (Inclusive of ends)
        for col in range(tl, tr+1):
            acc.append(matrix[st][col])

        # Traverse Right Col Top to Bottom (Exclusive of ends)
        for row in range(st+1, sb):
            acc.append(matrix[row][tr])

        # Traverse Bottom Row Right to Left (Inclusive of Ends)
        for col in range(tr, tl-1, -1):
            acc.append(matrix[sb][col])

        # Traverse Left Col Bottom to Top (Exclusive of ends)
        for row in range(sb-1, st, -1):
            acc.append(matrix[row][tl])

        tl += 1
        tr -= 1
        st += 1
        sb -= 1

    if tl == tr and st == sb:
        # We have a single cell remaining
        acc.append(matrix[tl][st])
    elif tl == tr:
        # We have a single column remaining
        for row in range(st, sb+1):
            acc.append(matrix[row][tl])

    else:
        # tr == tb: We have a single row remaining
        for col in range(tl, tr+1):
            acc.append(matrix[st][col])

    print(acc)
    return acc




# -- Test --
def test(fn):
    assert fn([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    assert fn([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]) == [1,2,3,4,8,12,11,10,9,5,6,7]

test(spiral_matrix)