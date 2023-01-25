"""
Game of Life

The m * n gboard is made up of cells, where each cell has an initial state:
- live (represented by a 1)
- dead (represented by a 0)

Each cell interacts with its EIGHT NEIGHBORS (incl diagonal)

Rules:
    - A live cell with FEWER THAN TWO live neighbors dies by underpopulation
    - A live cell with two or three live neighbors lives on to next generation
    - A live cell with MORE THAN THREE live neighbors dies by overpopulation
    - A dead cell with EXACTLY THREE live neighbors becomes a live cell, as if by reproduction

The next state is created by applying the above rules SIMULTANEOUSLY to every cell
in the current state, where births and deaths occur simultaneously.

Given the current state of the m * n grid `board`, return the NEXT state.

****Modify the board in-place, don't return anything!***

"""

"""
We have to do this in-place.
It would be a mistake to eagerly-update each cell in the board to the 
n+1th state , since the rules assume that you're considering adjacent cells in 
the nth state. 

So we have to either allocate a whole new next_board "array", or do it in-place
in a clever manner.

Could we have each cell take the form of (current, next), where maybe we
"initialize" each cell to (current, None), and go through hte board populating
the Nones into nextStates, and then go through the board and just keep the nextStates?

Another more general way of doing this I think would just be to turn
the nextStates of the board into a log

next_state_log = [firstRowFirstCol, firstRowSecondCol, firstRowThirdCol, ... secondRowTFirstCol]

And then we can just replay that log over the entire array, getting the next state.
I guesss this isn't any better than allocating a whole new array.

INSIGHT:
    There are only four different TRANSITIONS that can occur:
    0 -> 0 : "2"
    0 -> 1 : "3"
    1 -> 0 : "4"
    1 -> 1 : "5"
    We could eagerly go through the board and convert the numbers to their
    transition number.
    And then at the end we could convert from transition numbers to next numbers
    This would only take constant extra space.
"""


def game_of_life(board: list[list[int]]) -> None:

    def get_live_neighbors(row_idx: int, col_idx: int) -> int:
        """
        Count live neighbors of the cell in the current generation
        This is complicated by
        """
        # All 8 directions
        dir_mods = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],  # Skipping 0,0
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1]
        ]
        # Get on-board neighboring cell addresses
        valid_neighbors = [
            [row_idx + row_mod, col_idx + col_mod]
            for row_mod, col_mod in dir_mods
            if (
                    0 <= row_idx + row_mod < len(board) and
                    0 <= col_idx + col_mod < len(board[0])
            )
        ]

        # Count the "live" cells of valid_neighbors
        live_neighbors = 0
        for neighbor_row, neighbor_col in valid_neighbors:
            neighbor_state = board[neighbor_row][neighbor_col]
            # Is the cell alive in the CURRENT generation (1, 4, 5)
            if neighbor_state in [1, 4, 5]:
                live_neighbors += 1

        return live_neighbors

    def get_next_generation_state(row_idx: int, col_idx: int) -> int:
        """
        Determine the state for the next generation @ an unmapped cell, given current state
        by applying the rules of life
        """
        current_state = board[row_idx][col_idx]
        live_neighbors = get_live_neighbors(row_idx, col_idx)

        # Apply the rules of life
        """
        Rules:
        - A live cell with FEWER THAN TWO live neighbors dies by underpopulation
        - A live cell with two or three live neighbors lives on to next generation
        - A live cell with MORE THAN THREE live neighbors dies by overpopulation
        - A dead cell with EXACTLY THREE live neighbors becomes a live cell, as if by reproduction
        """
        if current_state == 1:
           return 1 if live_neighbors in [2,3] else 0
        else:
            return 1 if live_neighbors == 3 else 0


    mapper = {  # (current,next) -> mapped
        (0, 0): 2,
        (0, 1): 3,
        (1, 0): 4,
        (1, 1): 5
    }
    remapper = {  # mapped -> next
        2: 0,
        3: 1,
        4: 0,
        5: 1
    }


    for row_idx in range(len(board)):
        for col_idx in range(len(board[0])):
            current_generation_state = board[row_idx][col_idx]
            next_generation_state = get_next_generation_state(row_idx, col_idx)
            board[row_idx][col_idx] = mapper[(current_generation_state, next_generation_state)]

    for row_idx in range(len(board)):
        for col_idx in range(len(board[0])):
            board[row_idx][col_idx] = remapper[board[row_idx][col_idx]]

    return board


def test(fn):
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    fn(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    board = [[1, 1], [1, 0]]
    fn(board)
    assert board == [[1, 1], [1, 1]]

test(game_of_life)
