from collections import defaultdict
"""
There is a robot starting at the position (0,0) in the origin,
on a 2D plane.

Given a sequence of its moves, judge if this robot ENDS UP AT (0,0) after
completing its moves.

You are given a string moves that represents the move sequence of the robot,
where the ith character represents the ith move.
Valid moves are R, L, U, D

Return true if the robot returns to the origin after it finishes all of its
moves, or false otherwise.
"""

"""
Thinking: The thing about applying movement operations is that they're
commutative with respect to the final outcome after they've been applied.

So R R L R and R L R R both end you up at (2,0)
So if we want to make sure that the robot ends up at 0,0, then we 
know there have to be an equal number of 
"""


def will_return_to_origin(move_string: str) -> bool:
    move_counts = defaultdict(lambda: 0)
    for dir in move_string:
        move_counts[dir] += 1

    return abs(move_counts["R"] - move_counts["L"]) == 0 and abs(move_counts["U"] - move_counts["D"]) == 0

def will_return_to_origin_alternative(move_string: str) -> bool:
    horizontal = 0 # net ∆
    vertical = 0 # net ∆
    for char in move_string:
        if char == "L":
            horizontal -= 1
        elif char == "R":
            horizontal += 1
        elif char == "U":
            vertical += 1
        else:
            vertical -= 1
    return not any([horizontal, vertical])


assert will_return_to_origin("UD") == True
assert will_return_to_origin("LL") == False

assert will_return_to_origin_alternative("UD") == True
assert will_return_to_origin_alternative("LL") == False