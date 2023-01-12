"""
Longest Increasing Subsequence

Given an integer array `nums`, return the LENGTH of the longest
STRICTLY INCREASING subsequence!


Sam Recall: Subsequences are ordered, but not necessarily contiguous.
"""
from typing import Optional


def lengthOfLissBrute(nums: list[int]) -> int:
    # Step 1: Generate all possible subsequences (increasing or not)
    subsequences = []

    def helper(idx: int = 0, built: Optional[list[int]] = None) -> None:
        # Given the current position, either include the number in your built or don't.
        if not built:
            built = []

        if idx >= len(nums):
            subsequences.append(built)
            return

        included = [*built, nums[idx]]
        # excluded = [*built] # Don't need to do this, I think it's fine to not.

        helper(idx + 1, included)
        helper(idx + 1, built)

    helper()

    def is_increasing(nums: list[int]) -> bool:
        if not nums:
            return False

        increasing = True
        for idx in range(len(nums)):
            if idx - 1 >= 0:
                if nums[idx] <= nums[idx - 1]:
                    increasing = False
                    break

        return increasing

    # Step 2: Find the max length increasing subsequence
    return max(
        len(ss) for ss in subsequences if is_increasing(ss)
    )


"""
Can we do better than the horrific brute solution above?

[0,1,0,3,2,3]

Can this be a dynamic progamming problem, bottom-up?

Where dp[i] = length of maximum increasing subsequence at index i?

What if the values in dp were (maxLength, lastNumber in Subsequence)?
And then for each element you could look backwards in the DP and take the maxLength (+1) of
the one with a lastNumber less than current number?

[(1,0), (2,1), (0, 0), (3,3), (3,2), (4,3)]

Or we don't have to encode that information in the tuple, do we?

Let's assume we already had this in our DP, and now we were considering idx=4
nums =  [0, 1, 0, 3, 2, 3]
dp =    [1, 2, 0, 3, ?, ?]

We could scan over all the indices in nums[0:3]
If the number if LESS THAN nums[4], then we can consider extending that subsequence.

We would take the maximum of all of these extendable subsequences (plus one), and 
set it as our value in our DP list.
"""


def lengthOfLiss(nums: list[int]) -> int:
    dp = [1] * len(nums)

    for idx in range(len(nums)):
        # Find the extendable previous sequences
        options = [
            dp[back_idx]
            for back_idx in range(0, idx)
            if nums[back_idx] < nums[idx]
        ]

        # Extend the longest extendable seequence
        dp[idx] = max(
            options
        ) + 1 if options else 1

    return dp[-1]


# -- Test --
def test(fn):
    assert fn([10, 9, 2, 5, 3, 7, 101, 18]) == 4  # 2 5 7 101 or 2 3 7 101
    assert fn([0, 1, 0, 3, 2, 3]) == 4  # 0 1 2 3
    assert fn([7, 7, 7, 7, 7]) == 1


test(lengthOfLissBrute)
test(lengthOfLiss)
