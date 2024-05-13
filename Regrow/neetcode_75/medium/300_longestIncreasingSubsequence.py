"""
Longest Increasing Subsequence
Category: DP

Given an integer array `nums`, return the LENGTH of the longest
STRICTLY INCREASING subsequence!
"""
from typing import Optional

"""
Thinking: Okay, subsequences are interesting because they're 
ORDERED but NOT-NECESSARILY CONTIGUOUS!
"""

def longest_liss_brute(nums: list[int]) -> int:
    subsequences = []
    def helper(idx: int, built: Optional[list[int]] = None):
        if built is None:
            built = []
        if idx >= len(nums):
            subsequences.append(built)
            return

        # Choose to either include or not include the num @ idx in nums
        helper(idx+1, built) # Not include
        helper(idx+1, [*built, nums[idx]]) # Include

    helper(0, None)

    # Alternatively, we could have generated only-increasing subsequences above
    def is_increasing(nums: list[int]):
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
        return True


    return max(
        [len(ss) for ss in subsequences if is_increasing(ss)],
    )



"""
DP Insight:

The left side of an increasing subsequence is by necessity the lowest number
in the subsequence.
When asking if we can extend a "later" subsequence,

[ {our Number}  ... {beginningOfSomeSubsequenceThatContinuesOn} ]
We just need to ask: Is our number strictly less than the first number in the subesquence?

So we can populate a DP list where dp[i] is the length of the longest increasing subsequence
starting at index i. Then return max(dp), I suppose?

dp of length len(nums)
dp[i] = length of longest increasing SS starting at i, going to the end
dp[i] = max(dp[x]) + 1 for all x > i if nums[x] > nums[i]
This would be O(N^2) instead of 2^N or whatever 
"""
def longest_liss(nums: list[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(dp) - 1, -1, -1):
        # For every subsequence after
        for j in range(i+1, len(dp)):
            # If that subsequence is extensible, extend it?
            if nums[j] > nums[i]:
                dp[i] = max(
                    dp[i],
                    dp[j] + 1
                )
    print(dp)
    return max(dp)


# ---- Test Zone ----

def test(fn):
    assert fn([10,9,2,5,3,7,101,18]) == 4
    assert fn([0,1,0,3,2,3]) == 4
    assert fn([7,7,7,7,7,7,7]) == 1 # This one is sort of a hint, in a way, right?

test(longest_liss_brute)
test(longest_liss)