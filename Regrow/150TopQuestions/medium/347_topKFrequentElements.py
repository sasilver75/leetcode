"""
Top-K Frequent Elements

Given an integer array `nums` and an integer `k`, return the `k` most
frequent elements! You may return the answer in any order :)

"""
import collections
import heapq
import math

"""
Thinking:
The easiest way that I can think of to do this is to 
process the nums list into a list of (num, count).
"""


def topKFrequentNaive(nums: list[int], k: int) -> list[int]:
    num_counts = list(collections.Counter(nums).items())  # [(count, num), ...]

    def merge(l1: list[tuple[int, int]], l2: list[tuple[int, int]]) -> list[tuple[int, int]]:
        # DESC sort of list[tuple(num, count)] by count
        acc = []
        p1, p2 = 0, 0
        while p1 < len(l1) and p2 < len(l2):
            e1, e2 = l1[p1], l2[p2]
            if e1[1] >= e2[1]:
                acc.append(e1)
                p1 += 1
            else:
                acc.append(e2)
                p2 += 1

        acc.extend(l1[p1:])
        acc.extend(l2[p2:])

        return acc

    def sort(nums: list[tuple[int, int]]) -> list[tuple[int, int]]:
        # DESC sort of (num, count) tuples by count
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        return merge(
            sort(nums[:mid]),
            sort(nums[mid:])
        )

    num_counts = sort(num_counts)
    print(num_counts)

    # Return the num part of the (num, counts) tuple for the first k tuples
    return [tup[0] for tup in num_counts[:k]]


"""
Can we do better, or just different?

We could insert all n (num, count) elements into a Min Heap, then pop off the first K
elements into a list and return it.
That would similarly be O(NlogN)/O(N) as the sorting solution.
"""


def topKFrequentNaiveTwo(nums: list[int], k: int) -> list[int]:
    num_counts = collections.Counter(nums).items()

    # Heapify turns a list into a heap. But it can't take an argument for what to use to compare. If you use tuples, it uses the first attribute. We want it to do that with the count!
    # Therefore we have to reverse the (num,count) tuples into (count, num) tuples
    num_counts = [(tup[1], tup[0]) for tup in num_counts]  # "Reverse the tuples"

    # By default, though, heapq only makes a min heap! There isn't an option to create a max heap... in 2022.
    # The standard workaround is to "invert" the value of the keys, and then use the default-min-heap heapq implementation
    num_counts = [(-tup[0], tup[1]) for tup in num_counts]

    heapq.heapify(num_counts)  # Count, Nums

    acc = []
    for _ in range(k):
        acc.append(heapq.heappop(num_counts)[1])

    return acc


""""
Is there a better way that we could do this?
Either using less time than O(NlogN) --> O(N)
or using constant space?

We could do it in O(NK) time by having a "leaderboard" of K places that we
insert each (num, count) tuple into based on where it ranks.

This could be quite good if k were low and n were quite high
"""


def topKFrequent(nums: list[int], k: int) -> list[int]:
    numCounts = collections.Counter(nums)  # {num: count}

    # We could either do this with a maxheap with a limited size, or with a list.
    # The former could possibly be Nlog(k), right? Pretty good
    top_k = [float('-inf')] * k

    def insert_into_top_k(item: tuple[int, int]) -> None:
        # This would be implemented in either O(K) or O(logK)
        pass

    for numCount in numCounts.items(): # (num, count)
        insert_into_top_k(numCount)

    return top_k



# -- Test Zone --
def test(fn):
    assert fn([1, 1, 1, 2, 2, 3], 2) == [1, 2]  # or [2,1]
    assert fn([1], 1) == [1]


# test(topKFrequentNaive)
# test(topKFrequentNaiveTwo)
# test(topKFrequent)