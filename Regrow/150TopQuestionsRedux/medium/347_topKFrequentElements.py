"""
347 Top K Frequent Elements

Given an integer array nums and an integer k,
return the k MOST FREQUENT ELEMENTS! You may return the answer in any order.

You algorithm must be better in complexity than O(NlogN), where N
is hte array's sizes
"""
import collections


def topKFrequentNaive(nums: list[int], k: int) -> list[int]:
    """
    This would be the most straightforward way of doing it

    Turn the given list [1, 2, 1, 2, 1, 3]

    Into Counts
    {
    1:  3,
    2: 2,
    3: 1
    }

    Then sort these (num, count) items descending by count
    [(1,3), (2,2), (3,1)]

    And select the first k=2 items
    [(1,3), (2,2)]
    And return the numbers from those tuples
    [1, 2]


    This happens in O(NLogN) time, and O(N) space
    """
    counts = collections.Counter(nums)
    num_counts = list(counts.items()) # Iterable of (number, countNumber)
    num_counts.sort(key=lambda numCount: numCount[1], reverse=True)
    return [nc[0] for nc in num_counts[:k]]



"""
Can we be smarter?
Can we be BETTER than O(NLogN), ie O(N)?

We could maybe do it in NK time by keeping a "leaderboard" of the top K 
elements
    - This could be maybe NLogK if we had a maxHeap of size K that we kept
    
Given that K is in the range [1, # unique elements in the array], it's at least
going to be O(NLogN)
"""
def topKFrequent(nums: list[int], k: int) -> list[int]:
    pass


def test(fn):
    assert fn([1, 1, 1, 2, 2, 3], k=2) == [1, 2]
    assert fn([1], k=2) == [1]

test(topKFrequentNaive)
# test(topKFrequent)