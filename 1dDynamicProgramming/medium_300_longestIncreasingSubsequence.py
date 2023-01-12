from typing import Callable, Optional

"""
Longest Incerasing Subsequence

Given an integer array `nums`, return the LENGTH of the LONGEST strictly increasing SUBSEQUENCE.

A SUBSEQUENCE is a sequence that can be derived from an array by deleting some or no elements without
changing the order of the remaining elements! For example, given an array [0, 3, 1, 6, 2, 2, 7],
something like [3, 6, 2, 7] would be a valid subsequence.
"""


def longest_increasing_subsequence_brute(nums: list[int]) -> int:
    # Generate all possible subsequences
    subsequences = []

    def generate_subsequences(idx: int = 0, built: Optional[list[int]] = None):
        if built is None:
            built = []

        if idx >= len(nums):
            subsequences.append(built)
            return

        generate_subsequences(idx + 1, [*built, nums[idx]])  # With current number (copy by value)
        generate_subsequences(idx + 1, [*built])  # Without current number (copy by value)

    generate_subsequences()

    def is_ascending(seq: list[int]):
        for i in range(1, len(seq)):
            if seq[i] < seq[i-1]:
                return False
        return True

    # print(subsequences)

    max_length_increasing_substring = max(filter(lambda seq: is_ascending(seq), subsequences), key=len)
    # print(max_length_increasing_substring)
    return len(max_length_increasing_substring)

"""
Now... How can we do this in a way that's smarter than 2^N?

3   0   1   0   2   3   4

What's a subproblem?
The smallest one is one of length 1... 

3

Therefore at i=0, longest is 1

This clearly has a longestIncreasingSubsequence of length 1

3   0

What about this?
It's less than the preceding number...
So at i=2, the longest is max(1, {previousSubsequence}) ... But oh, it's not going to be just substrings...
it's about subSEQUENCES, so there can be gaps in the sequence. How are we going to handle that in a cache-able/reusable way?

Remember though that we don't actually care about the longest increasing subsequence -- we just care
about the LENGTH of the longest increasing subsequence. Does that help us?

How can we modify the 2^N brute force DFS solution above to do better... Maybe something like N^2?
We can do DFS with Caching! :) 

Say we have 
[1, 2, 4, 3]  --> Ans: 1,2,3 = 3

Let's start with the brute force approach, starting all subsequences from index 0...
then repeat that starting frmo index 1, index 2, and index 3.

We take one decision to START at index 0, one to START at index 1, ...
                
                                    [root]
                    0           1           2           3
                [1]             [2]         [4]         [3]
                
Let's go along the first branch on the left

                                    [root]
                    0           1           2           3
                [1]             [2]         [4]         [3]
        1       2       3
    [1,2]      [1,4],   [1,3]           We were able to go into each of these branches because the value
                                at that index was greater than oru last index. Let's continue our decisions
                                
                                
                                [root]
                    0           1           2           3
                [1]             [2]         [4]         [3]
        1       2       3
    [1,2]      [1,4],   [1,3] 
    2      3
[1,2,4]    [1,2,3]          We can't recurse from the [1,2,4] because 3 is lower than [4]
                            and we can't recurse from the [1,2,3] because we've exhausted our indices
                            
Well let's focus on our caching part -- what kind of repeated work have we eliminated?
Well... let's look at the rightmost branch.
Once we have a [3] after choosing a LISS starting at index 3... we can't do anything else.
 We know that LISS[index=3] = 1. 
And we sort of saw that when we were in the left branch, adding index=3 to create [1,2,3] (Which was all
we were able to do, in the end).

Sam Note: I guess this is sort of an insight. If we were going from "right to left", we know that the longest
increasing subsequence STARTING AT index 3 is 1 --> LISS[3] = 1. Is that useful when considering combining 
LISSes? Say LISS[3] were 4. If we were at LISS[2] or something and considering whether we could continue a subsequence
into 3... If we determine that we could, we could just add the LISS[3] to our current LISS[2]?

Yes, I think so! Let's use that and do a solution! :) 
"""

def longest_increasing_subsequence(nums: list[int]) -> int:
    dp = [0] * len(nums)
    dp[-1] = 1
    for i in range(len(nums) -1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]: # We can tack the current number as a first-element of any later subsequence as long as the next number is >= the current one
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


"""
Now let's continue listening to neetcode :) , now that we've solved it...
"""

def neetcode_solution(nums: list[int]) -> int:
    LISS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LISS[i] = max(LISS[i], 1 + LISS[j])

    return max(LISS)


# ---  /!\ Test Zone /!\ ---

def test(fn: Callable):
    assert fn([10, 9, 2, 5, 3, 7, 101, 10]) == 4  # 2, 3, 7, 101
    assert fn([0, 1, 0, 3, 2, 3]) == 4  # 0, 1, 2, 3


# test(longest_increasing_subsequence_brute)
test(longest_increasing_subsequence_test)