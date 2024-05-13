"""
Combination Sum

Given an array of DISTINCT integers `candidates` and a target integer `target`

Return a list of all UNIQUE combinations of `candidates` where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the FREQUENCY of at least one of teh chosen numbers is different.
"""


def combination_sum_naive(nums: list[int], target: int) -> list[list[int]]:
    ways = set()

    def helper(remaining: int, used: list[int]) -> None:
        if remaining == 0:
            ways.add(tuple(used))
            return

        # For every spendable number, spend into the future
        for idx, num in enumerate(nums):
            if remaining - num >= 0:
                new_remaining = remaining - num
                new_used = used.copy()
                new_used[idx] += 1  # Increment usage of that number
                helper(new_remaining, new_used)

    helper(target, [0] * len(nums))

    print(f"{ways = }")

    # Translate the frequencies back into numbers
    def translate(tup: tuple[int]) -> list[int]:
        acc = []
        for idx, count in enumerate(tup):
            for _ in range(count):
                acc.append(nums[idx])
        return acc

    ans = [translate(tup) for tup in ways]
    print(ans)
    return ans

"""
How can we be more performant than that? Can we do a 1D DP on len(target+1), where dp[i] =  the list of unique combinations of candidates that make i?
Except when we populate that left to right gets messy, because just because you had multiple lists

CRACKHEAD SOLUTION BELOW

Let's say we had fn([2, 3, 6, 7], 7)


target = 7
candidates = [2, 3, 6, 7]

Generate the list
[[], [], [], [], [], [], [], []]


For each target index target (left to right), starting at 1... Where target represents the # we're trying to sum to
    consider each candidate.
    We know that if the candidate is 

"""
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort() # This is the key that enables the logic in this problem! [edit]: I think it'd actually be possible to do this without sorting; just the "breaks" wouldn't be possible. I'll provide it in a reimplementation at the bottom.

    # list of list of combinations that sum to the target
    dp = [[] for _ in range(0, target+1)]   # dp[t] = list of combinations that sum to target

    for t in range(1, len(dp)):
        for candidate in candidates:
            if candidate > t:
                # This candidate can't be used, and any later candidates also can't be used, since they're ASC
                break
            elif candidate == t:
                # This candidate wholly equals t. That means it's its own "combination". That also means no later candidates will be useful, since candidates are both ASC and unique (meaning all later candidates will be too big to be useful)
                dp[t].append([candidate])
                break
            else:
                # candidate < t
                # This candidate is useful, and can be used to extend ALL of the combinations in dp[t-candidate], if that's a valid index
                if t - candidate >= 0: # is it valid
                    for combination in dp[t-candidate]:
                        # Extend each combination that sums to t-candidate with candidate, summing to t.
                        extended_combination = [*combination, candidate]
                        dp[t].append(extended_combination)

    return dp[-1]

# This is just to prove to myself that it's possible to do this without sorting of candidates
def combination_sum_without_sorting(candidates: list[int], target:int) -> list[list[int]]:
    # Not sorting the candidates here
    dp = [[] for _ in range(target+1)]
    for t in range(1, len(dp)):
        for candidate in candidates:
            if candidate > t:
                # Not a useful candidate for this target sum
                continue
            elif candidate == t:
                dp[t].append([candidate])
            else:
                # candidate < t
                if t - candidate >= 0:
                    for combination in dp[t-candidate]:
                        dp[t].append([*combination, candidate])

    return dp[-1]


def test(fn):
    ans1 = fn([7, 6, 2, 3,], 7)
    assert all(ans in ans1 for ans in [[2, 2, 3], [7]])

    ans2 = fn([2, 3, 5], 8)
    assert all(ans in ans2 for ans in [[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    ans3 = fn([2], 1)
    assert ans3 == []


test(combination_sum_naive)
test(combination_sum)
test(combination_sum_without_sorting) # Yep! Works without sorting too, although it's a nice little optimization.
