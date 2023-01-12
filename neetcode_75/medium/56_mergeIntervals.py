"""
Merge Intervals
Category: Intervals

Given an array of intervals where intervals[i] = [start,end],
mergea ll overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals
in the input.

Note: Abutting intervals like [1,4] and [4,5] are considered overlapping.
"""


def merge_meetings(meetings: list[list[int]]) -> list[list[int]]:
    meetings.sort(key=lambda meeting: meeting[0])  # Sort ASC by StartTime

    merged = [meetings[0]]
    for meeting in meetings:
        last_meeting = merged[-1]

        # Mergable when this meeting starts at or before the ending of last meeting
        if meeting[0] <= last_meeting[1]:
            # Mergable
            # We know that last_meeting has a start <= current_meeting, since we sorted them.
            # The end time will be the largest of the two
            last_meeting[1] = max(
                (meeting[1], last_meeting[1])
            )
        else:
            # Not Mergable
            merged.append(meeting)

    return merged


def test(fn):
    assert fn(
        [[1, 3], [2, 6], [8, 10], [15, 18]]
    ) == [[1, 6], [8, 10], [15, 18]]

    assert fn(
        [[1, 4], [4, 5]]
    ) == [[1, 5]]


test(merge_meetings)
