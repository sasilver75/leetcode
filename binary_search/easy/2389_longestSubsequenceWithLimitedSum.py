"""
Longest Subsequence With Limited Sum

Given an integer array `nums` of length `n`, and an integer array `queries` of
length `m`.

Return an array `answer` of length `m` where `answer[i]` is the maximum size
of a subsequence that you can take from `nums`, such that the sum of its
elements is less than or equal to (<=) `queries[i]`
"""
import collections

"""
For every `number` in `queries`, what's the length of hte maximum-length
 subsequence in `nums` that sums to <= `number`? Produce a list of such values.
"""


def answer_queries_naive(nums: list[int], queries: list[int]) -> list[int]:
    # Generate all possible subsequences in nums
    subsequences = []

    def helper(idx: int, built: list[int]) -> None:
        if idx == len(nums):
            subsequences.append(built)
            return

        # Include or don't include the character at idx
        helper(idx + 1, [*built, nums[idx]])
        helper(idx + 1, built)

    helper(0, [])

    # Process subsequences into dict of {sum: maximumLengthSubsequence}
    lookup = collections.defaultdict(lambda: 0)
    for ss in subsequences:
        ss_sum = sum(ss)
        ss_len = len(ss)
        lookup[ss_sum] = max(lookup[ss_sum], ss_len)  # Maximum Length Subsequence is the one we want

    acc = []
    for sum_target in queries:
        max_length = 0
        for sum_key in range(sum_target, -1, -1):
            max_length = max(max_length, lookup[sum_key])
        acc.append(max_length)

    # print(acc)
    return acc


"""
INSIGHT:
Okay, so while subsequences usually mean preserving order but not contiguity,
you might think that we can't sort nums. Except adding is commutative, so
the ordering doesn't actually matter -- and we aren't returning the actual
subsequence itself, just a length.

So we can sort the nums

[4, 5, 2, 1] --> [1, 2, 4, 5]

And then we can generate a prefix sum list
where prefix_sum[i] is the sum of all numbers <= i in the sorted nums list

[1,2,4,5] --> [0, 1, 3, 7, 12]

Now, for each q in queries, we can find the greatest sum that's <= q,
and return the INDEX of that one.
Recall that in our prefix_sum list, the index is pretty much encoding the LENGTH
of the list that was being used

prefix_sum[i] = x
    - Means: "Using i elements without repeat, the SMALLEST sum I can make is x"
So conversely if I was looking at prefix_sum[3] = 5
I know that if I were LOOKING for 5, the GREATEST NUMBER of elements that could be
combined to make 5 is 3!

That's pretty much what we want here! 
This is NOT an easy question, when solved performantly, in my book!
"""
def answer_queries(nums: list[int], queries: list[int]) -> list[int]:
    nums.sort()
    prefix_sums = [0] # Because of sort asc... index: # of elements, val: minimum sum using idx elements
    for num in nums:
        prefix_sums.append(prefix_sums[-1]+num)

    print(prefix_sums)

    acc = []
    for q in queries:
        """
        Binary search for the appropriate number in prefix_sums
        We want the rightmost element <= target(q)
        """
        left, right = 0, len(prefix_sums) - 1
        last_seen_greatest_lte = -1

        while left <= right:
            mid_idx = left + (right - left) // 2
            mid_val = prefix_sums[mid_idx]

            if mid_val > q:
                right = mid_idx - 1
            elif mid_val < q:
                last_seen_greatest_lte = mid_idx
                left = mid_idx + 1
            else:
                last_seen_greatest_lte = mid_idx
                break

        # If it stayed at -1, we still want to return 0
        acc.append(max(last_seen_greatest_lte, 0))
    return acc

# --- Test ---
def test(fn):
    assert fn([4, 5, 2, 1], [3, 10, 21]) == [2, 3, 4]
    assert fn([2, 3, 4, 5], [1]) == [0]


test(answer_queries_naive)
test(answer_queries)