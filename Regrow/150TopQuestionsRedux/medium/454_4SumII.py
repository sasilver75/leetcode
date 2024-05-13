"""
4Sum II

Given four integerarrays nums1, nums2, nums3, and nums4, all of length n, return the NUMBER OF TUPLES
(i, j, k, l) such that:

0 <= i, j, k, l < n  (They're...all valid indices)
nums1[i] + nums2[j] + nums3[k] + nums[l] == 0
"""
import collections


def fourSumCountNaive(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    count = 0
    for i in nums1:
        for j in nums2:
            for k in nums3:
                for l in nums4:
                    if sum([i,j,k,l]) == 0:
                        count += 1
    return count

"""
3Sum uses the idea of "combining" two of the three lists into a SET of sums...
"""
def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    # Get the number of ways to make each possible sum in each (n1/n2) and (n3/n4)
    n1n2 = collections.defaultdict(int)
    for n1 in nums1:
        for n2 in nums2:
            n1n2[n1+n2] += 1

    n3n4 = collections.defaultdict(int)
    for n3 in nums3:
        for n4 in nums4:
            n3n4[n3+n4] += 1

    # Now we have two O(N^2) lists of numbers...
    # Traverse one of them, looking for the complement in the other in constant time.
    n_ways = 0
    for num in n1n2:
        complement = -num
        # If we had 3 ways to make 10 in n1n2, and there were 2 ways to make -10 in n3n34, then +=2 ways
        # If there wasn't even a way to make -10 in n3n34, then += 0 ways
        n_ways += min(n1n2[num], n3n4[complement])

    return n_ways




def test(fn):
    assert fn(
        [1,2],
        [-2,-1],
        [-1,2],
        [0,2]
    ) == 2 # 0001 1100

    assert fn(
        [0],
        [0],
        [0],
        [0]
    ) == 1

test(fourSumCountNaive)
test(fourSumCount)
