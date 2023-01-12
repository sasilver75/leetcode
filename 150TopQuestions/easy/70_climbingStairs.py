"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps
In how many distinct ways can you climb to the top?
"""

def climbing_stairs(n: int) -> int:
    # Base Case
    if n <= 2:
        return n

    # Recursive
    return climbing_stairs(n-1) + climbing_stairs(n-2)


assert climbing_stairs(2) == 2
assert climbing_stairs(3) == 3
assert climbing_stairs(4) == 6 # (1111), (112), (121), (211), (22)