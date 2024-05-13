"""
Game of Life

The board is made up of an `m x n` grid of cells, where each cell has an
initial state: `live`, represented by a 1, or `dead`, represented by a 0.

Each cell interacts with its EIGHT NEIGHBORS (hztl, vert, diag) using
the following four rules:

1) Any LIVE cell with FEWER THAN TWO live neighbors dies as if caused
by under-population

2) Any LIVE cell with TWO OR THREE live neighbors lives on to the next generation

3) Any LIVE cell with MORE THAN THREE LIVE NEIGHBORS dies, as if by over-population

4) Any DEAD cell with EXACTLY THREE live neighbors becomes a live cell, as if by
reproduction.

The next state is created by applying the above rules simultaneously to every cell
in the current state, where births and deaths occur simultaneously.


Given the current state of the `m x n` grid, return the NEXT state.
"""
import itertools


def gameOfLife(board: list[list[int]]):
    nextBoard = board.copy()

    def count_neighbors(row: int, col: int):
        # dirMods = [
        #     [-1,-1],
        #     [-1,0],
        #     [-1,1],
        #     [0,-1],
        #     ...
        # ]
        neighbor_count = 0
        dirMods = itertools.product([-1, 0, 1], [-1, 0, 1])
        for rowMod, colMod in dirMods:
            targetRow = row + rowMod
            targetCol = col + colMod
            if all(
                    0 <= targetRow < len(board),
                    0 <= targetCol < len(board[0])
            ):
                neighbor_count += board[targetRow][targetCol]

        return neighbor_count

    for row in range(len(board)):
        for col in range(len(board[0])):
            cell = board[row][col]
            neighbor_count = count_neighbors(row, col)

            if cell:
                # Alive: Apply Rules
                neighor_count = count_neighbors(row, col)
                if neighbor_count < 2:
                    # Dies by under_population
                    nextBoard[row][col] = 0
                elif neighbor_count <= 3:
                    # Lives On
                    nextBoard[row][col] = 1
                else:
                    # Dies by over-population
                    nextBoard[row][col] = 0

            else:
                # Dead: Apply Rules
                if neighor_count == 3:
                    # Re-alive by reproduction
                    nextBoard[row][col] = 1
                else:
                    # Dead
                    nextBoard[row][col] = 0

    return nextBoard


def test(fn):
    assert fn(
        [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    ) == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    assert fn(
        [[1, 1], [1, 0]]
    ) == [[1, 1], [1, 1]]
