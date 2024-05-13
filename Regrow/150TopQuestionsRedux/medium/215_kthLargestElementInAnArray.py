"""
Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the kth largest element in the
array.

Note that it's the kth largest element in the sorted order, not the kth distinct element.

** YOU MUST SOLVE IT IN O(N) TIME COMPLEXITY!
"""
import heapq

"""
Thinking:
Okay, so the straightforward way to do this would be to do sort the list DESC
and then select the kth element, but this would be NLogN time

Another way would be to process the elements into a Max Heap, and then return
the fifth popped element, but this would also be NLogN time

How can we possibly solve this in O(N) time?
Are there any characteristics of the problem (constraints) that make this possible?

Given constraints are:
1 <= k <= nums.length  # Okay, so it's just going to be a realistic K
-10^4 <= nums[i] <= 10^4 # Nums[i] are in [-10,000, 10,000] interval

Is the answer that we're pretty much going to maintain a list/heap of size K,
and iterate through the list that way?
"""

"""
Python has a heapq module as part of the standard library
    - An implementation of the heapqueue algorithm also known as the priority queue algorithm
Heaps are binary trees fro which every parent node has a value less than or equal
to any of its children. 
    - Uses arrays for which heap[k] <= heap[2*k+1], heap[2*k+2] for all k
    - The smallest element of the heap is always the root, heap[0]

Annoyingly, heapq only has an implementation for a min-heap; for a max-heap,
you have to get tricky with it by inverting the values of the keys, and then
using heapq as usual. (ie turn 1000.0 into -1000.0)
"""


def find_kth_largest_naive(nums: list[int], k: int) -> int:
    # Min Heap of size K
    heap = []

    # We just push/pop elements onto the heap, so the smallest element keeps getting removed
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    # print(f"After iteration: {heap = }")
    heap.sort(reverse=True)  # Sort the heap DESC
    # print(f"After sort: {heap = }")
    return heap[k - 1]


def test(fn):
    assert fn([3, 2, 1, 5, 6, 4], k=2) == 5
    assert fn([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4


test(find_kth_largest_naive)
