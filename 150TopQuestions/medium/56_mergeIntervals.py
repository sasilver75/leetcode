"""
Merge Intervals

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge
all overlapping intervals, and return an array of the NON-OVERLAPPING
INTERVALS that cover all intervals in the input!

Sam Note: This is "Merge Meetings"
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    # It seems like we can expect that intervals are always going to be sorted by start time
    # What you would want to do is sort by start time. Do we need to sort by end time WITHIN start time? Yes, we actually should.
    # It seems like they're sorted this way in the example data. We can just do merges.

    merged = [intervals[0]]
    for idx in range(1, len(intervals)):
        candidate_start, candidate_end = intervals[idx]
        last_start, last_end = merged[-1]
        if candidate_start <= last_end: # We know they're sorted ASC
            # Mergeable
            merged[-1][1] = max(merged[-1][1], candidate_end)
        else:
            merged.append(intervals[idx])

    print(merged)
    return merged






def test(fn):
    assert fn([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert fn([[1, 4], [4, 5]]) == [[1, 5]]

test(merge_intervals)