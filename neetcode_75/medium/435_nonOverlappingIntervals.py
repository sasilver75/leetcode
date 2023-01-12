"""
Non-Overlapping Intervals
Category: Intervals

Given an array of intervals `intervals` where `intervals[i] = [start, end]`
return the MINIMUM NUMBER of intervals you need to remove to make the
rest of the intervals non-overlapping.
"""


def merge(l1: list[list[int]], l2: list[list[int]]) -> list[list[int]]:
    pass

def sort(intervals: list[list[int]]) -> list[list[int]]:
    pass


"""
I sort of suspect that this is going to be similar to a merge intervals problem, but instead
of merging, we'll just "evict" the one that was going to be merged. Let's look at an example:

Intervals: [[1,2], [2,3], [3,4], [1,3]]
Sorted by Start, End ASC: [[1,2], [1,3], [2,3], [3,4]]    (Question: Do we need to sort by BOTH? Or just by start?)

non_overlapping = []
Add [1,2] to Non-Overlapping Accumulator
Considering [1,3] --> Overlap detected with previous [1,2], evict [1,3]
Considering [2,3] --> No Overlap detected with previous [1,2], add to accumulator  (contiguous, but non overlapping)
Considering [3,4] --> No Overlap detected with previous [2,3], add to accumulator
End: [[1,2], [2,3], [3,4]]

Q: Would this have worked if we ONLY sorted by start? --> NO! We'd perhaps have started
with [[1,3]] in the accumulator, evicted [1,2], evicted [2,3], and accumulated [3,4].

"""

def merge_intervals(intervals_a: list[list[int]], intervals_b: list[list[int]]) -> int:
    # Sort intervals ASC by start, end
    merged = []
    pointer_a, pointer_b = 0, 0
    while pointer_a < len(intervals_a) and pointer_b < len(intervals_b):
        interval_a, interval_b = intervals_a[pointer_a], intervals_b[pointer_b]

        if interval_a[0] < interval_b[0] or (
            interval_a[0] == interval_b[0] and interval_a[1] <= interval_b[1]
        ):
            merged.append(interval_a)
            pointer_a += 1
        else:
            merged.append(interval_b)
            pointer_b += 1

    merged.extend(intervals_a[pointer_a:])
    merged.extend(intervals_b[pointer_b:])

    return merged



def sort_intervals(intervals: list[list[int]]) -> int:
    if len(intervals) <= 1:
        return intervals

    mid = len(intervals) // 2

    return merge_intervals(
        sort_intervals(intervals[:mid]),
        sort_intervals(intervals[mid:])
    )


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals = sort_intervals(intervals)

    n_erased = 0
    non_overlapping = [intervals[0]]
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_interval = non_overlapping[-1]

        if current_interval[0] < last_interval[1]:
            # "Evict" the current interval
            n_erased += 1
            continue
        non_overlapping.append(current_interval)

    return n_erased



def test(fn):
    """Note: It seems like contiguous [1,2], [2,3] intervals are not considered to be overlapping"""
    assert fn([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1  # [1,3] can be removed, and the rest of the intervals are non-overlapping
    assert fn([[1, 2], [1, 2], [1, 2]]) == 2 # Need to remove both [1,2]s
    assert fn([[1, 2], [2, 3]]) == 0 # Don't need to remove any of the intervals

test(erase_overlap_intervals)