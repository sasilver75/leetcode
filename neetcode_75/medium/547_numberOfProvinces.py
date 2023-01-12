"""
Number of Provinces
Category: Graph

There are `n` cities. Some of them are connected, while some of them
are not.
If city `a` is directly connected with city `b`, and city `b` is directly
connected with city `c`, then `a` is indirectly connected with `c`.

A PROVINCE is a group of directed or indirectly connected cities, and
no other cities outside of the group.

Given an `n * n` matrix `isConnected` where `isConnected[i][j]` = 1 if
the `i`'th city and the `j`th city are directly connected, and 0 otherwise.

Return the total number of provinces
"""

"""
Thinking:
    - This is a square matrix. The number of cities is len(matrix)
    - The "number of connected components" in a graph is going to be 
    the way to go. It doesn't seem (from my self-produced third example) that
    "counting islands" is the same thing. Different!
"""


def n_provinces(is_connected: list[list[int]]):
    n = len(is_connected)  # Can use this to initialize parents/rank and also to count components
    parents = [i for i in range(n)]
    rank = [1] * n

    def find(n: int) -> int:
        """Given a city, find the 'capital' of the 'province'"""
        cur = n
        while parents[cur] != cur:
            cur = parents[cur]
        return cur

    def merge(n1: int, n2: int) -> bool:
        """
        Attempt to merge two cities' provinces, returning True if successful, else False
        Merging may fail if the two cities belong to the same province already
        """
        c1, c2 = find(n1), find(n2)

        if c1 == c2:
            return False

        if rank[c1] >= rank[c2]:
            parents[c2] = c1
            rank[c1] += rank[c2]
        else:
            parents[c1] = c2
            rank[c2] += rank[c1]

        return True

    for row in range(len(is_connected)):
        for col in range(len(is_connected[0])):
            if is_connected[row][col] and merge(row, col):
                # This is robust to "merging a city with itself"
                n -= 1

    return n


def test(fn):
    assert fn([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]) == 2

    assert fn([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]) == 3

    assert fn([
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]) == 2  # This would be 2, I think. Self-example here that "counting islands? doesn't work

test(n_provinces)