"""
417 Pacific Atlantic Water Flow

There is an m*n rectangular island that borders on both the Pacific and Atlantic ocean

The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

                                Pacific
                            +----------------+
                            |                |
                Pacific     |                |  Atlantic
                            |                |
                            |                |
                            +----------------+
                                Atlantic


The island is partitioned into a grid of square cells.
Given an m*n integer matrix heights, where heights[r][c] represents the HEIGHT ABOVE SEA LEVEL of the cell at coordinate (r,c)

The island receives a lot of rain
    - Rain can flow to neighboring cells directly North/South/East/West of it, IF the neighboring cell's height is LESS THAN OR EQUAL TO the current
    cell's height.
    - Water can flow from any cell adjacent to an ocean into the ocean


Return a 2D list of grid coordinates result where result[i] = [r,c], denoting that rain water can flow from cell [r,c] ...
    to BOTH the Pacific and Atlantic ocean!

"""
from typing import Callable

"""
Notes:
    1. I think it's feasible that a cell very near the Atlantic ocean may need to take a very circuitous route around the board in order to then dump 
    in the Atlantic ocean (or similar).
    2. Because water can flow to equally-heighted cells, we have to keep track of the cells that we've visited in our current recursive branch, so
    as not to endlessly cycle
    3. I think we're going to have to do TWO iterations of this (which I don't think changes the asymptotic time complexity), the first where we'd 
    check for Atlantic flow, and the second checking for Pacific flow. Configure your explore function to take a success_fn that checks whether we're in a cell that can flow
    into the target ocean
"""


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    def success_atlantic(row: int, col: int) -> bool:
        # Are we on a cell on the right-most col or bottom-most row?
        return row == (len(heights) - 1) or col == (len(heights[0]) - 1)

    def success_pacific(row: int, col: int) -> bool:
        # Are we on a cell on the left-most col or top-most row?
        return row == 0 or col == 0

    def is_valid(row: int, col: int):
        # Is this cell on the board?
        return (
                0 <= row < len(heights) and
                0 <= col < len(heights[0])
            )

    def can_reach(row: int, col: int, visited: set, success_fn: Callable) -> bool:
        """
        Called on an unvisited cell, determine if the cell is a "success cell"
        A cell is a "success cell" if the target ocean can be reached from the current cell,
        either directly (basecase) or via any of the adjacent, valid (on-board), unvisited, flowable cells.
        """
        # Are we in a success position?
        if success_fn(row, col):
            return True

        # Visit the cell
        visited.add((row, col))

        # Consider all neighboring cells that we could recurse to
        dir_mods = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        recursable_cells = [
            [row + row_mod, col + col_mod]
            for row_mod, col_mod in dir_mods
            if (
                is_valid(row+row_mod, col+col_mod) and
                (row+row_mod, col+col_mod) not in visited and
                heights[row+row_mod][col+col_mod] <= heights[row][col]
            )
        ]

        # Return whether we could reach our objective by recursing into any adjacent, recursable cells
        return any(
            can_reach(r,c, visited.copy(), success_fn)
            for r, c in recursable_cells
        ) if recursable_cells else False


    acc = []

    for row in range(len(heights)):
        for col in range(len(heights[0])):
            if (
                    can_reach(row, col, set(), success_atlantic) and
                    can_reach(row, col, set(), success_pacific)
            ):
                acc.append([row, col])

    return acc


def test(fn):
    assert fn([[1, 2, 2, 3, 5],
               [3, 2, 3, 4, 4],
               [2, 4, 5, 3, 1],
               [6, 7, 1, 4, 5],
               [5, 1, 1, 2, 4]]) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    assert fn([[1]]) == [[0, 0]]


test(pacific_atlantic)
