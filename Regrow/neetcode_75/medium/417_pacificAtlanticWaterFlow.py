"""
Pacific Atlantic Water Flow
Category: Graph

There is an m * n rectangular island that borders both the pacific ocean and
the atlantic ocean.

The PACIFIC ocean touches the island's LEFT and TOP edges
the ATLANTIC ocean touches the island's RIGHT and BOTTOM edges

The island is partitioned into a grid of square cells.

You're given an `m * n` integer matrix `heights` where `heights[r][c]`
represents the HEIGHT ABOVE SEA LEVEL of the cell @ coordinate (r, c)

The island receives a lot of rain, and the rain water can flow to neighboring
cells directly north/south/east/west IFF the neighboring cell's height is
LESS THAN OR EQUAL TO the current cell's height.

Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates `result` where result[i] = [ri, ci]
denotes that rain water can flow from cell (ri, ci) to BOTH the Pacific
and Atlantic oceans.

Sam interpreation: That is, `result` needs to be a list of all [row, col] coordinates
from which you could drain into both/either the atlantic/pacific ocean.
"""


def pacific_atlantic_naive(heights: list[list[int]]) -> list[list[int]]:

    def can_reach(row: int, col: int, atlantic: bool, visited: set[list[int]]) -> bool:
        visited.add((row, col))

        # Are we looking for atlantic and on the atlantic coast?
        if atlantic and (col == len(heights[0]) - 1 or row == len(heights) - 1):
            return True

        # Are we looking for pacific and on the pacific coast?
        if not atlantic and (col == 0 or row == 0):
            return True

        # Visit adjacent, valid (onboard), unvisited, DOWNHILL (<=) cells
        dir_mods = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1],
        ]
        for row_mod, col_mod in dir_mods:
            target_row, target_col = row + row_mod, col + col_mod
            if (
                0 <= target_row < len(heights)
                and 0 <= target_col < len(heights[0])
                and heights[target_row][target_col] <= heights[row][col]
                and (target_row, target_col) not in visited
                and can_reach(target_row, target_col, atlantic, visited.copy())
            ):
                return True

        return False

    acc = []
    for row in range(len(heights)):
        for col in range(len(heights[0])):
            if can_reach(row, col, False, set()) and can_reach(row, col, True, set()):
                acc.append([row, col])

    return acc

"""
Thinking: Is there any better way that we could do this?
I feel like perhaps we ought to be able to do "one" traversal instead of "two"
traversals for each cell, but that isn't a super meaningful change.

Instead, isn't theres some way that we could like... subproblem this?
For instance imagine that we'rei n the center square of the grid, and we know
that (from every other square around us) or (from one square around us), we 
KNOW we can reach the atlantic ocean. Then we'd be able to shortcircuit and skip
a lot of work. So it seems like subproblems might be useful to us in thinking about this.

Obviously, any coastal zone can reach their appropriate coast...
But how do we back-populate this 2D dynamic programming question?

Given grid:
    
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    
Let's first populate a DP for the ATLANTIC (right, bottom) ocean.

        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],

This would be the starting position... But can we actually populate
any other cells using this strategy? I mean consider this cell []:

    
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, [0], 0, 0, 1],
        [1, 1, 1, 1, 1],
        
This one could reach the atlantic ocean if the height @ it is >= the height
of the cell below it... but it's also possible that there could be a very circuitous
route that could be taken going UP then RIGHT then ... all the way to the coast.
I'm not sure that we could do a dynamic programming solution :( 

I think our DFS was the only option -- Leetcode solutions seem to confirm that
"""

def test(fn):
    assert all(coord in fn([
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]) for coord in [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])

    assert all(coord in fn([
        [1]
    ]) for coord in [[0, 0]])

test(pacific_atlantic_naive)