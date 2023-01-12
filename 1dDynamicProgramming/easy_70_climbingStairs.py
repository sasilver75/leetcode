"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time, you can either climb 1 or 2 steps. In how many distinct ways
can you get to the top?
"""

def climb(n: int) -> int:
    if n <= 0:
        return 0
    if n <= 2:
        return n

    return climb(n-2) + climb(n-1)

# Let's try with memoization?
class SolutionBad:
    def __init__(self):
        self.cache = {}

    def climb(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 2:
            return n

        n_2 = self.cache[n-2] if (n-2) in self.cache else climb(n-2)
        n_1 = self.cache[n-1] if (n-1) in self.cache else climb(n-1)
        ways = n_2 + n_1

        print(f"Setting cache at {n} for {ways}")
        self.cache[n] = ways

        print(self.cache)
        return ways

# Observe that the above doesn't actually work becuase we're doing it top-down. So we're
# always solving things that aren't in the cache...'
s1 = SolutionBad()


def climb_good(n: int) -> int:
    # Dynamic Programming doesn't have to be recursive.
    cache = [0, 1, 2]
    for i in range(3, n+1):
        cache.append(cache[i-1] + cache[i-2])

    return cache[n]

def climb_better(n: int) -> int:
    # We actually don't need to keep track of all O(N) in memory.
    # Technically we only need to keep track of the "last two" registers
    if n <= 2:
        return max(0, n)

    n_minus_2 = 1
    n_minus_1 = 2

    for i in range(3, n+1):
        n_i = n_minus_2 + n_minus_1
        n_minus_2 = n_minus_1
        n_minus_1 = n_i

    return n_i



# assert s.climb(2) == 2
# assert s.climb(3) == 3
# assert s.climb(4) == 5
# assert s.climb(5) == 8


assert climb_good(2) == 2
assert climb_good(3) == 3
assert climb_good(4) == 5
assert climb_good(5) == 8

assert climb_better(2) == 2
assert climb_better(3) == 3
assert climb_better(4) == 5
assert climb_better(5) == 8