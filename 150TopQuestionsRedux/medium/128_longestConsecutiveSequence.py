"""
Longest Consecutive Sequence

Given an unsorted array of integers `nums`, return the length of the
longest consecutive elements sequence.

You must write an algorithm that runs in O(N) time

IE fn([100, 4, 200 , 1, 3, 2]) = 4, since [1,2,3,4] is the longest consecutive element sequence

Recall that a SUBSEQUENCE is ordered, but not necessarily contiguous
"""

"""
An O(NlogN) solution
"""


def longest_consecutive_sequence_naive(nums: list[int]) -> int:
    def merge(l1: list[int], l2: list[int]) -> list[int]:
        acc = []
        p1, p2 = 0, 0
        while p1 < len(l1) and p2 < len(l2):
            e1, e2 = l1[p1], l2[p2]
            if e1 <= e2:
                acc.append(e1)
                p1 += 1
            else:
                acc.append(e2)
                p2 += 1

        acc.extend(l1[p1:])
        acc.extend(l2[p2:])

        return acc

    def merge_sort(nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid_idx = len(nums) // 2

        return merge(
            merge_sort(nums[0:mid_idx]),
            merge_sort(nums[mid_idx:])
        )

    sorted_nums = merge_sort(nums)

    lcs = 0
    running = 0
    for idx, num in enumerate(sorted_nums):
        previous_num = sorted_nums[idx - 1] if idx - 1 >= 0 else num - 1
        if previous_num + 1 == num:
            running += 1
        else:
            lcs = max(lcs, running)
            running = 1

    lcs = max(lcs, running)

    return lcs


"""
One way we could do it is by a sort of counting sort, but the numbers are
in the range of -10^9 and 10^9, which means that the array allocated would be quite big.
"""


def longest_consecutive_sequence_counting_sort(nums: list[int]) -> int:
    nums_max = max(nums)
    presence = [False] * (nums_max + 1)

    for num in nums:
        presence[num] = True

    lcs = 0
    running = 0
    for idx, present in enumerate(presence):
        if not present:
            running = 0
        if present:
            running += 1
            lcs = max(lcs, running)

    print(lcs)
    return lcs


"""
How can we do this in O(N) time?
This implies that we won't be sorting the input.
Perhaps we'll be using more memory as a result, in order to be able to do this
in linear time.

Insight:

Given [100, 4, 200, 1, 3, 2]

Visualize it on a number line:

    ___________             __          __
    1         4           100 100     200 200 
    
Each of these sequences of consecutive numbers has a [start, end] range.

What characterizes the start of a range?
    - A number N for which N-1 is NOT in nums
What characterizes the end of a range?
    - A number N for which N-1 is NOT in nums
    
So we can build up a list of starts: [1, 100, 200]
                and a list of ends: [4, 100, 200]
                
But what about the ranges between these?
For each start/end range, we know that all numbers between the start/end ARE
going to necessarily be in nums too! Just given by the rules above! Cool!

Given [100, 4, 200, 1, 3, 2]
we would build up start,end as 

start: [100, 200, 1]
end: [100, 4, 200]

As you can see, we unfortunately would have to sort theses lists (Which in
 the worst case would make this O(NLogN)
 
 A better solution is to JUST generate the starts:
 
 start: [100, 200, 1]
 And then for each, linearly probe until we find the "end" of that range (a
 number that is NOT in nums, when we would update the length as r-l+1.

"""


def longest_consecutive_sequence(nums: list[int]) -> int:
    nums_set = set(nums)
    starts = []
    for num in nums:
        if num - 1 not in nums_set:
            starts.append(num)

    lcs = 0
    for start in starts:
        end = start
        while end in nums:
            end += 1
        # For the included range [1,4], now start,end is at [1,5]
        lcs = max(lcs, end - start)

    return lcs


def test(fn):
    assert fn([100, 4, 200, 1, 3, 2]) == 4
    assert fn([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


test(longest_consecutive_sequence_naive)
test(longest_consecutive_sequence_counting_sort)
test(longest_consecutive_sequence)
