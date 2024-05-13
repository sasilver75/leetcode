"""
3 Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j != k, and that sum([nums[i], nums[j], nums[k]]) == 0

Notice that the solution set must not contain duplicate triplets!
"""
import collections

"""
Thinking: I can think of a few ways to do this:
1. Generate all possible combinations of indices - filter to those summing to 0. The problem with this is that we consider [1, 0, -1] and [-1, 0, 1] to be
the same thing. So we have to like... accumulate the encoded versions of these combinations, where the encoded version of the combination just retains
the count of occurrences of elements in the three-list, not the ordering. The problem with this is that it's not like the numbers are only positive -- they're
in the range from [-10^5, 10^5]... So one option is that we have a tuple vector of length 2*10^5, where it counts the ocurrences... and then we accumulate
those to a set. Then we need to retranslate them back from tuples of numbers into lists of numbers. You can see that this is pretty annoying. 
2. the better option is to realize that there are three types of numbers that there can be in nums (negatives, zeroes, and positives), and there are 
4 ways of creating 0 from 3 numbers (order invariant):
    1. Zero Zero Zero
    2. Neg Zero Pos
    3. Neg Neg Pos
    4. Neg Pos Pos

"""


def three_sum_naive(nums: list[int]) -> list[list[int]]:
    ...
    # acc = set()
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         for k in range(j+1, len(nums)):
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 acc.append([nums[i], nums[j], nums[k]])
    # return acc


def three_sum(nums: list[int]) -> list[list[int]]:
    ways = []

    # Proces the nums into buckets
    zeroes = []
    negatives = []
    positives = []
    for num in nums:
        if num == 0:
            zeroes.append(num)
        elif num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    negatives_set = collections.Counter(negatives)
    positives_set = collections.Counter(positives)

    # Consider each of the four cases separately

    # 1: (Zero, Zero, Zero) Case
    if len(zeroes) >= 3:
        ways.append([0, 0, 0])

    # 2: Neg, Zero, Pos
    # For this one, we should use pos_set and neg_set only
    if zeroes:
        for p in positives_set:
            complement = 0 - p
            if complement in negatives_set:
                ways.append([complement, 0, p])

    # 3: Neg, Pos, Pos
    # For this one, we have to do an O(N^2) search on the positives
    for i1 in range(len(positives)):
        for i2 in range(i1 + 1, len(positives)):
            p_sum = positives[i1] + positives[i2]
            complement = 0 - p_sum
            if complement in negatives_set:
                # Have our sublists in ASC order
                ways.append([complement, positives[i1], positives[i2]])

    # 4: Neg, Neg, Pos
    # For this one, we have to do an O(N^2) search on the negatives
    for i1 in range(len(negatives)):
        for i2 in range(i1 + 1, len(negatives)):
            n_sum = negatives[i1] + negatives[i2]
            complement = 0 - n_sum
            if complement in positives:
                # Have our sublists in ASC order
                ways.append([negatives[i1], negatives[i2], complement])

    return ways


def test(fn):
    ans1 = fn([-1, 0, 1, 2, -1, 4])
    assert all(ans in ans1 for ans in [[-1, -1, 2], [-1, 0, 1]])

    ans2 = fn([0, 1, 1])
    assert ans2 == []

    ans3 = fn([0, 0, 0])
    assert ans3 == [[0, 0, 0]]


# test(three_sum_naive)
test(three_sum)
