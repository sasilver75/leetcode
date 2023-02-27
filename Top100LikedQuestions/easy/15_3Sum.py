"""
Three Sum

Given an integer array nums, return ALL the trips [nums[i], nums[j], nums[k]]
Such that:
 * i != j, i != k, and j != k
 * nums[i] + nums[j] + nums[k] == 0

(In other words, pick three different indices such that the values add to 0)
(And find all such triplets, returning a list of their indices)

**NOTE** the solution set must not contain duplicates!
So [1,2,3] and [3,2,1] and [2,1,3] area all the same.
"""
import collections


def three_sum_naive(nums: list[int]) -> list[list[int]]:
    ways = []
    ways_set = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                v_i, v_j, v_k = nums[i], nums[j], nums[k]
                if v_i + v_j + v_k == 0:
                    values = [v_i, v_j, v_k]
                    values.sort()  # This sort is only going to be on length 3
                    values_tup = tuple(values)
                    if values_tup not in ways_set:
                        ways.append(values)
                        ways_set.add(values_tup)

    return ways


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Can we do better than O(N^3)? Can we do O(N^2) by preprocessing
    into pairs?
    What would that dict look like?
    {
        sum: [{indexA, indexB}, ...]
        ...
    }
    And then we can do another pass?

    But there's a note that there can be multiple A,B pairs that sum to a
    given sum, so it should be [{indexA, indexB}, ...]

    This runs in O(N^2)/O(N)
    """
    ways = []
    ways_set = set()
    lookup = collections.defaultdict(list)

    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            ab_sum = nums[a] + nums[b]
            lookup[ab_sum].append(([a, b]))

    for idx in range(len(nums)):
        complement = 0 - nums[idx]
        for s in lookup[complement]:
            if idx not in s:
                vals = [nums[idx], nums[s[0]], nums[s[1]]]
                vals.sort()
                vals_tup = tuple(vals)
                if vals_tup not in ways_set:
                    ways.append(vals)
                    ways_set.add(vals_tup)

    return ways


def three_sum_smart(nums: list[int]) -> list[list[int]]:
    """
    I don't know if this is going to necessarily be better than O(N) but there's
    an idea that there are only a certain number of ways to get to 0, using 3 numbers

    1) 0 0 0
    2) + - 0
    3) + + -
    4) + - -

    So if we segregate into pos/neg/zero, we could do this

    I think it's still going to be O(N^2), because we'll have to consider
    every combination of ++, --, for instance. In the worst case, they'll all
    be positive/negatives
    """
    ways = []
    ways_set = set()

    positives = []
    negatives = []
    zeroes = []

    ways = []

    for num in nums:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)
        else:
            zeroes.append(num)

    positives_set = set(positives)
    negatives_set = set(negatives)

    # Case 1: 0 0 0
    if len(zeroes) >= 3:
        ways.append([0, 0, 0])

    # Case 2: + - 0
    if zeroes:
        for pos in positives:
            if -pos in negatives_set:
                values = [-pos, 0, pos]
                values_tup = tuple(values)

                if values_tup not in ways_set:
                    ways.append(values)
                    ways_set.add(values_tup)





    # Case 3: + + -
    for first in range(len(positives)):
        for second in range(first+1, len(positives)):
            positive_sum = positives[first] + positives[second]
            if -positive_sum in negatives_set:
                values = [positives[first], positives[second], -positive_sum]
                values.sort()
                values_tup = tuple(values)

                if values_tup not in ways_set:
                    ways.append(values)
                    ways_set.add(values_tup)



    # Case 4: + - -
    for first in range(len(negatives)):
        for second in range(first + 1, len(negatives)):
            negative_sum = negatives[first] + negatives[second]
            if -negative_sum in positives_set:
                values = [negatives[first], negatives[second], -negative_sum]
                values.sort()
                values_tup = tuple(values)

                if values_tup not in ways_set:
                    ways.append(values)
                    ways_set.add(values_tup)

    return ways


def test(fn):
    assert all(l in fn([-1, 0, 1, 2, -1, -4]) for l in [[-1, -1, 2], [-1, 0, 1]])
    assert fn([0, 1, 1]) == []
    assert fn([0, 0, 0]) == [[0, 0, 0]]

# test(three_sum_naive)
test(three_sum)
test(three_sum_smart)
