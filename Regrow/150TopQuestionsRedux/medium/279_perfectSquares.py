"""
Perfect Squares

Given an integer n, return the LEAST NUMBER OF PERFECT SQUARE NUMBERS
that sum to n

A perfect square is an integer that's the square of an integer;
in other words, it's the product of some integer with itself. For example,
1,4,9,16 are perfect squares
3,11 are not
"""
from collections import deque

"""
Okay, here's the naive way that I can think of doing it:
1. Generate all perfect squares in 1...N
2. Generate all possible ways of getting to n using the squares, and note 
the shortest path.

"""
# Helper
def generate_squares(n: int):
    acc = []
    i = 1
    while (s := i ** 2) <= n:  # Check out use of Walrus operator
        acc.append(s)
        i += 1
    return acc



def num_squares_naive(n: int) -> int:
    squares = generate_squares(n) # eg [1,4,9], n=12

    fewest_squares = float("inf")
    def dfs_for_shortest(total: int, squares_used: int):
        nonlocal fewest_squares

        if squares_used > fewest_squares:
            return

        if total == n:
            fewest_squares = min(fewest_squares, squares_used)

        options = [square for square in squares if total + square <= n]
        for op in options:
            dfs_for_shortest(total+op, squares_used+1)

    dfs_for_shortest(0, 0)

    print(fewest_squares)
    return fewest_squares

"""
Is there a way that we can do this in a smarter way?
Well if you think about the recursive tree of calls
    If we had the options [1,4,9], at each position in the recursive
    tree of calls, we have 3 children options. 
    
    In a sense we're looking for the shallowest point in the tree that
    gets us to the result, so it makes sense to me that a breadth-first search
    would probably be more performant, though I'm not sure it changes the 
    asynmptotic complexity from dfs.
"""
def num_squares(n: int) -> int:
    squares = generate_squares(n)

    # Iterative BFS: We want to return the first one we see with RT=N
    nodes = deque()
    nodes.appendleft((0, 0)) # [(running_total, num_used), ...]
    while nodes:
        running_total, num_used = nodes.pop()
        if running_total > n:
            continue # We should never even hit this if we're enqueueing correctly
        if running_total == n:
            return num_used

        for square in squares:
            if (new_total := running_total+square) <= n:
                nodes.appendleft((new_total, num_used+1))

    # .... Shouldn't get here ever


def test(fn):
    assert fn(12) == 3 # 4 + 4 + 4
    assert fn(13) == 2 # 4 + 9

test(num_squares_naive)
test(num_squares)