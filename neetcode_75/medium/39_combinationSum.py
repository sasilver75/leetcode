"""
Combination Sum
Category: DP

Given an array of distinct integer `candidates` and a target integer
`target`, returna LIST of all unique combinations of `candidates` where the
chosen numbers SUM to `target`. You may return the combinations in any order.

The SAME number may be chosen from `candidates` an UNLIMITED NUMBER of times.

The two combinations are unique if the FREQUENCY of at least one of the chosen
numbers is different.

The test cases are generated such that the number of
unique combinations that sum up to `target` is LESS THAN 150 combinations
for the given input.
"""
from typing import Optional

"""
Thinking:

"""


def combination_sum_naive(candidates: list[int], target: int) -> list[list[int]]:
    ways = set()

    def helper(chosen: Optional[list[int]] = None, remaining: int = target):
        if chosen is None:
            chosen = [0] * len(candidates)

        if remaining == 0:
            ways.add(tuple(chosen))  # Set needs to have hashable elements
            return

        for idx, candidate in enumerate(candidates):
            if remaining - candidate >= 0:
                new_chosen = [*chosen]
                new_chosen[idx] += 1
                helper(new_chosen, remaining - candidate)

    helper()  # Populate ways set, a set of (0,1,1,0) tuples

    def convert_to_candidates(counts: list[int]) -> list[int]:
        # Given a list of counts [0,3,2,0,1, ...] where the counts[i] = # of candidates[i] used, return the appropriate candidates selection
        acc = []
        for idx in range(len(counts)):
            for _ in range(counts[idx]):
                acc.append(candidates[idx])
        return acc

    return [convert_to_candidates(way) for way in ways]


"""
How can we do better?
We want to find the list of unique combinations of candidates where the chosen numbers
sum to target.

Does knowing combination_sum(149) help us find combination_sum(150)? Or vice versa?
Not obviously to me -- all of the combinations for 149 might not even be convertible to combinations
for 150, if there aren't the appropriate numbers in candidates. 
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()  # [1,3,5]. Having the candidates makes the iteration below much easier! (Allows us to ensure no duplicates; later items should be >= previous ones, making the result an ASC sequence)

    # Note that generating a list of empty lists is a little different than usual :(
    dp = [[] for _ in
          range(target + 1)]  # Note that DP is based on TARGET! So dp[x] is how many unique combinations can sum to [0]

    # Note that dp[0] (meaning the combinations of numbers in candidates that sum to 0) is going to be an empty list, so we can start at 1
    for t in range(1, len(dp)):  # "t" is acting as "target" in a subproblem
        for c in candidates:
            if c > t:
                break  # Neither c nor any candidates after c are small enough to be useful for this t (target).
            if c == t:
                dp[t].append([c])  # candidate "c" itself wholly sums to target "t", so it should be its own "combination list" in dp[t]'s list of combination lists
                break  # Since all c's after this c are greater that our current c, we can break after this
            else:
                # For every list in dp[t-c] (consider meaning of t-c)
                for combination in dp[t - c]:
                    if c >= combination[-1]: # If c is greater than the last element in the (asc) combination, add the extended version to our dp[t]
                        extended = combination + [c]
                        dp[t].append(extended)

    return dp[target]


def test(fn):
    assert all(el in fn([2, 3, 6, 7], 7) for el in [[2, 2, 3], [7]])
    assert all(el in fn([2, 3, 5], 8) for el in [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    assert fn([2], 1) == []


# test(combination_sum_naive)
test(combination_sum)
