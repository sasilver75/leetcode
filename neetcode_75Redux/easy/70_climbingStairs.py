"""
Climbing Stairs

You're climbing a staircase; it takes n steps to reach the top.

Each time, you can either climb 1 or 2 steps. In HOW MANY DISTINCT WAYS can you climb to the TOP?
"""

"""
My question on reading this is:
- What does "Top" mean? Is it the last index in the list, or is it the index len(nums)?
    - It seems like this is getting to the 0th step from the nth step. 
"""


def climbing_stairs(n: int) -> int:
    def dfs(n):
        if n < 0:
            return 0
        if n == 0:
            return 1

        return dfs(n-1) + dfs(n-2)
    return dfs(n)

"""
Technicaly there was some repeat work being done, I think
Above, for the example of climbing_stairs(4)
This results in calls to:
CLIMB STAIRS 4
Called: DFS(4)
Called: DFS(3)
Called: DFS(2)
Called: DFS(1)
Called: DFS(0)
Called: DFS(-1)
Called: DFS(0)
Called: DFS(1)
Called: DFS(0)
Called: DFS(-1)
Called: DFS(2)
Called: DFS(1)
Called: DFS(0)
Called: DFS(-1)
Called: DFS(0)

So there's clearly work here that can be cached.
"""
def climbing_stairs_cached(n: int) -> int:
    print(f"\n CLIMB STAIRS {n}")
    cache = {}
    def dfs(n: int) -> int:
        print(f"Called: DFS({n})")
        if n < 0:
            print("Returning Base Case for < 0")
            return 0
        if n == 0:
            print("Returning Base Case for 0")
            return 1

        if n in cache:
            print(f"Returning Cached Response for {n}")
            return cache[n]

        minus_one = dfs(n - 1)
        minus_two = dfs(n - 2)

        cache[n-1] = minus_one
        cache[n-2] = minus_two

        return minus_one + minus_two

    return dfs(n)

def test(fn):
    assert fn(2) == 2  # 11 2
    assert fn(3) == 3  # 111 12 21
    assert fn(4) == 5  # 1111 112 121 211 22


test(climbing_stairs)
test(climbing_stairs_cached)
