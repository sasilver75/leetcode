"""
Longest Increasing Subsequence

Given an integer array `nums`, return the length of the longest STRICTLY INCREASING
SUBSEQUENCE.

Recall that a SUBSEQUENCE is an ordered but not-necesssarily contiguous
subset of the origina list
"""

"""
Most naive thing:
1. Generate all SUBSEQUENCEs
"""
def length_of_longest_liss_naive(nums: list[int]) -> int:
    subsequences = []
    def generate_subsequence(idx: int, built: list[int]):
        if idx == len(nums):
            subsequences.append(built)
            return
        # Either include or don't include the element @ idx
        generate_subsequence(idx+1, [*built, nums[idx]])
        generate_subsequence(idx+1, built)

    generate_subsequence(0, [])

    def is_increasing(sequence: list[int]) -> int:
        if not sequence:
            return True

        # Is the sequence strictly increasing?
        for i in range(1, len(sequence)):
            if not sequence[i] > sequence[i-1]:
                return False

        return True

    increasing_subsequences = [
        ss for ss in subsequences
        if is_increasing(ss)
    ]

    return max(len(ss) for ss in increasing_subsequences)

"""
How can we do better than 2^N for subsequences?
We want to know the length of the lognest increasing subsequence starting at 
index 0, looking right. Would it help us in this quest to know the length
of the longest increasing subsequence starting at index 1, for example?
Yes! Because if nums[0] < nums[1], then we can "extend" that existing subsequence
( or rather, create a new subsequenece starting at the 0th index, and append
the subseuqnece starting at the 1st index.

We can use this idea to populate a one-dimensional DP table from the "end"
of the list towards the front of the list.
dp[i] = LISS starting at dp[i]

This would be in O(N^2) time since we're talking about subsequences;
The 0th index could extend any subsequence starting at any index in the range [1...len(nums)-1]
So for dp[i], we can extend the length of any subsequence in dp[i+1]...dp[len(dp)-1] assuming
that the num num[i] is strictly less than num[otheridx] 
"""
def length_of_longest_liss(nums: list[int]) -> int:
    dp = [1] * len(nums) # Default is 1; each index could be just of length 1
    for idx in range(len(dp) - 1, -1, -1):
        for comparison_idx in range(idx+1, len(dp)):
            # Can we extend this subsequence?
            if nums[idx] < nums[comparison_idx]:
                # Should we extend it by one, or do we have something better?
                dp[idx] = max(dp[idx], dp[comparison_idx] + 1)

    # The largest isn't necessarily at dp[0] I don't think
    return max(dp)





def test(fn):
    assert fn([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert fn([0, 1, 0, 3, 2, 3]) == 4
    assert fn([7, 7, 7, 7, 7, 7, 7]) == 1

test(length_of_longest_liss_naive)
test(length_of_longest_liss)