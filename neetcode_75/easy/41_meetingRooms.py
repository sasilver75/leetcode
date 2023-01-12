"""
Meeting Rooms
Category: Interval

Given an array of meeting room time intervals
consisting of a start and end time [[s1, e1], [s2, e2], ...],
determine if a person could attend all meetings!
"""


def could_attend_all(times: list[list[int]]) -> bool:
    # Sort meetings by Beginning time (I don't think we need ending time for this one)
    times.sort(key=lambda meeting: meeting[0])
    print(times)

    # Process meetings, looking for violations
    for i in range(1, len(times)):
        last_meeting_end = times[i-1][1]
        current_meeting_start = times[i][0]
        # If there's any intersection with the previous meeting, fail!
        # Intersection if current meeting's start time is < last meeting end, given that we know that the meetings are sorted by start time ASC
        if current_meeting_start <= last_meeting_end: # assuming end/start at same time == Nope!
            return False

    return True


def test(fn):
    assert fn([[0, 30], [5, 10], [15, 20]]) == False
    assert fn([[7,10], [2,4]]) == True

test(could_attend_all)