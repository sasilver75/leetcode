"""
Longest Increasing Subsequence (LISS)

Given an integer array nums, return hte length of the longest STRICTLY INCREASING subsequence

RECALL: Subsequences are ordered, but not necessarily contiguous parts sub-collections of the array.
"""

"""
Let's generate every subsequence, and filter them to the strictly increasing ones, and then take the length of the longest one.
"""
def liss_naive(nums: list[int]) -> int:
    subsequences = []
    def generate_subsequence(idx: int, built_subsequence: list) -> None:
        # Two options at the current index: Add it to the subsequence or don't
        if idx == len(nums):
            subsequences.append(built_subsequence)
            return

        # Add it
        new_built_subsequence = [*built_subsequence, nums[idx]]
        generate_subsequence(idx+1, new_built_subsequence)

        # Don't add it
        generate_subsequence(idx+1, built_subsequence)


    generate_subsequence(0, [])
    # print(f"SUBSEQUENCES: {subsequences = }")

    def is_increasing(nums: list[int]) -> bool:
        if len(nums) <= 1:
            return True
        for idx in range(len(nums) -1):
            if not (nums[idx] < nums[idx+1]):
                return False
        return True


    increasing_subsequences = [ss for ss in subsequences if is_increasing(ss)]

    return max(len(iss) for iss in increasing_subsequences)




"""
Use dynamic programming.

We can get this down to an O(N^2) 1-dimensional dynamic programming problem, if we really try.
A list of length len(nums)
dp[i] = LISS from index i ... end
So dp[len(nums)-1] = 1
dp[i] = Max(dp[i+1], dp[i+2], ... as long as nums[i] < nums[i+1]/[i+2] , etc)

IE, for every index, consider all later indexes in the DP table.
We can extend the ones for which the numbers at the same positions in nums are strictly increasing.
"""
def liss_dp(nums: list[int]) -> int:
    dp = [1] * len(nums) # Every number can at least be its own subsequence

    # For every index (R -> L)
    for idx in range(len(dp)-1, -1, -1):
        # For every following index:
        for comparison_index in range(idx+1, len(dp)):
            # If we can extend (prepend) that LISS starting at comparison index (to be dp[comparison_index]+1, then update our dp[idx] if it needs it.
            if nums[comparison_index] > nums[idx]:
                dp[idx] = max(dp[idx], dp[comparison_index] + 1)

    return max(dp)



def test(fn):
    assert fn([10,9,2,5,3,7,101,18]) == 4
    assert fn([0,1,0,3,2,3]) == 4
    assert fn([7,7,7,7,7,7,7]) == 1

test(liss_naive)
test(liss_dp)

