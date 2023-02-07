"""
435. Non Overlapping Intervals

Given an array of intervals intervals where intervals[i] = [start, end]

Return the MINIMUM NUMBER OF INTERVALS THAT YOU NEED TO REMOVE to make the rest of the intervals non-overlapping

"""

"""
Thinking:
I'm going to assume that the intervals are sorted ASC by start time AND end time, since that's what I see in the example problems. 
OOPS, that is NOT the case!
In our first example, [[1,2],[2,3],[3,4],[1,3]], that is not the case!
Let's make it the case by sorting.
    (The other option that I can think of is a brute force one that essentially is generating all possible subsequences of intervalA, and then filtering those to
    ones without overlaps, and determining the longest of these subsequences (which implicitly means the fewest had to be removed?)

** According to this problem, [1,2] and [2,3] are NOT overlapping 

Note: Could I do the usual "merge intervals" thing, but instead of merging... just increment the count of erased intervals?
Note that I don't even need to maintain the "merged" interval list liek I would usually, since we don't care about returning the list; we just need
to keep track of the last non-overlapping interval. 
"""


# TODO: Is there every a time where I would want to preference erasing the existing interval, instead of the candidate one that I'm considering?

def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda interval: (interval[0], interval[1]))

    def overlaps(intervalA: list[int], intervalB: list[int]) -> bool:
        return (
                (intervalB[0] < intervalA[0] < intervalB[1]) or
                (intervalA[0] < intervalB[0] < intervalA[1]) or
                (intervalA[0] == intervalB[0] and intervalA[1] == intervalB[1])
        )

    non_overlapping = [intervals[0]]
    intervals_removed = 0
    for idx in range(1, len(intervals)):
        current_interval = intervals[idx]
        last_non_overlapping_interval = non_overlapping[-1]

        if not overlaps(last_non_overlapping_interval, current_interval):
            non_overlapping.append(current_interval)
        else:
            intervals_removed += 1

    print(non_overlapping, intervals_removed)
    return intervals_removed


assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0
