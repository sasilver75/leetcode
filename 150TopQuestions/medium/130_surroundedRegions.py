"""
Given an m*n matrix `board` containing `X` and `0`, CAPTURE all regions
that are [4-directionally surrounded] by `X`.

A region is CAPTURED by flipping all `0`s into `X`s in that surrounded region


Ex:

    X   X   X   X           X   X   X   X
    X   O   O   X           X   X   X   X
    X   X   O   X   --->    X   X   X   X
    X   O   X   X           X   O   X   X
"""

"""
Musing:
The dumbest thing would be to scan through the whole board and make a list
of all of those 0's that are actually surrounded 4 X's. 

But you can see in the example above that the big island of 3 0's doesn't contain
any 0's that are entirely surrounded by Xs!

It's even possible that one like the upper-right 0, which only is surrounded by
TWO X's, is going to be flipped.

Question for Sam:
Will a 0 on the edge EVER be flipped? No, I believe. Since it will never be surroudned
on four sides.

"""
"""
Insight:
There's some wording in the question that kind of helps, I think:
"All REGIONS that are 4-dimensionally surrounded"
So what if the first thing we did was group these O's into "REGIONS," (islands)
and then validated that the regions were entirely surrounded by Water?

We could keep track of an "affiliated" set of cells, and then traverse through
the grid. Whenever we find a cell that's not yet affiliated, we affiliate that cell
and all of its neighboring (recursively) 0s.

As we consider each cell in a region, if we observe an adjacent 0, it MUST
be a 0 that's already in our island. So we can ignore them safely.
We're really just looking for edges of the board, in this case. If we see an
edge of the board, then we can't sink the island.
"""
from typing import Optional

def surrounded_regions(grid: list[list[int]]) -> list[list[int]]:
    nrow = len(grid)
    ncol = len(grid[0])
    regions = []

    def affiliate(row: int, col: int, region: set[tuple[int, int]]) -> None:
        # Called on a 0, it adds (row, col) to island and affiliates all adjacent,
        # unaffiliated 0s into the current region.
        # We even want to add 0's that are on the edge of the board, since those
        # will later be used to "invalidate" an island before capturing
        region.add((row, col))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # UDLR
        for rowMod, colMod in directions:
            targetRow = row + rowMod
            targetCol = col + colMod
            # Recurse on on-board, unvisited, 0-valued cells
            if 0 <= targetCol < nrow and 0 <= targetRow < ncol and (targetRow, targetCol) not in region and grid[targetRow][targetCol] == "O":
                affiliate(targetRow, targetCol, region)


    # Stage 1: Group Regions/Islands
    for row in range(nrow):
        for col in range(ncol):
            cell = grid[row][col]
            if cell == "O":
                region = set()
                affiliate(row, col, region)
                regions.append(region)


    # Stage 2: Sink each Region/Island that is sinkable
    for region in regions:
        # What makes a region unsinkable? That it has a cell on the border.
        if not any(
            row in (0, nrow-1) or col in (0, ncol-1) for row, col in region
        ):
            # Sink!
            for row, col in region:
                grid[row][col] = "X"

    return grid



def test(fn):
    """
    Notice in example 1 that an 0 should not be flipped if:
    1) It is on the border
    2) It is adjacent to an 0 that should not be flipped
    """
    assert fn([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]) == [
        ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
    assert fn([["X"]]) == [["X"]]

test(surrounded_regions)