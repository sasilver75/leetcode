""""
733 Flood Fill

An image is represented by an mxn integer grid IMAGE where IMAGE[i][j] represents
the pixel value of the image.

You are also given three integers: [sr, sc, color]. You should
perform a flood fill on the image starting from teh pixel image[sr][sc]

To perform a flood fill, consider the starting pixel plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel,
plus and pixels connected 4-directionally to those pixels (also w/ the same
color), and so on.
Replace the color of all the aforementioned pixels with color.

Return the modified image after performing the flood fill!

Example:
    https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg

"""


"""
Idea...

Visit target Cell (Mark it as 0)
Explore each adjacent cell (sensitive to edge of board) with a 1
"""

def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    # Could do thigns here like check if sr/sc are in image, or that image is actually a 2d array
    image = [lst.copy() for lst in image] # (!) //So we don't modify the input image
    initial_color = image[sr][sc]
    visit(image, sr, sc, initial_color, color, set())
    print(image)
    return image

def visit(image: list[list[int]], row: int, col: int, initial_color: int, target_color: int, visited: set) -> list[list[int]]:
    """
    Invoked only on valid (on-board) cells with target color
    """
    # Visit current cell
    image[row][col] = target_color
    visited.add((row, col))

    # Explore appropriate adjacent cells
    """
    Be careful! I thought I could apply each of [(-1, 0), (1, 0), (0, -1), (0, 1)] to
    my current location and then just catch an indexException if that were an invalid
    cell, but negative values (while invalid, to my rules) of course wrap aroudn to the back
    of the list in Python!
    A way to counter this would be for the x coordinate to be the min of (0, target_x)
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #UDLR
    n_row = len(image)
    n_col = len(image[0])
    for row_mod, col_mod in directions:
        # If we're modifying row to the right, don't let it go off board to the right (and so on)
        row_target = max(row + row_mod, 0) if row_mod <= 0 else min(row + row_mod, n_row-1)
        col_target = max(col + col_mod, 0) if col_mod <= 0 else min(col + col_mod, n_col-1)

        if image[row_target][col_target] == initial_color and (row_target, col_target) not in visited:
            print(f"From {row},{col} val {image[row][col]} , looking at {row_target},{col_target} because of mods {row_mod, col_mod} and target color is {image[row_target][col_target]}")
            visit(image, row_target, col_target, initial_color, target_color, visited)

# Case 1
img = [
    [1,1,1],
    [1,1,0],
    [1,0,1],
]
assert flood_fill(img, 1,1,2) == [
    [2,2,2],
    [2,2,0],
    [2,0,1],
]

# Case 2: This is one where the entire board is already the color that we want to flood fill. Will we just endlessly recurse around? :( Hope not!
# Had to add a "visited" list here... Which in the worst case is O(N) memory.
img = [
    [0,0,0],
    [0,0,0],
]
assert flood_fill(img, 0, 0, 0) == [
    [0,0,0],
    [0,0,0],
]




