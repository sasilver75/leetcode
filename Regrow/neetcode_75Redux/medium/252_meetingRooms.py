"""
Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1], [s2,e2], ...]
    where all si<ei  (meaning all meeting end times are after start times

Determine if a person could attend all meetings
"""

"""
A person could only attend all meetings if none of the meetings were overlapping
    Where overlapping doesn't just mean that the meetings were abutting (ie one ending at 5 and the next starting at 5.
    
So I think the easiest way to do that is to sort hte meetings by start time 
    TODO: Do I need to sort them by start, end    or is just start enough?
    

[[5,10], [5,7],]

I think it's enough to just sort by the start times.
Once sorted, the current meeting is overlapping with the previous meeting if:
    previous_meeting.start <= current_meeting.start < previous_meeting.end
Note that we're using < on the right boolean expression

"""

def can_attend_all_meetings(meetings: list[list[int]]) -> bool:
    meetings.sort(key=lambda meeting: meeting[0])
    non_overlapping_meetings = [meetings[0]]

    def overlaps(current_meeting, previous_meeting):
        return previous_meeting[0] <= current_meeting[0] < previous_meeting[1]


    for idx in range(1, len(meetings)):
        previous_meeting = non_overlapping_meetings[-1]
        current_meeting = meetings[idx]
        if overlaps(current_meeting, previous_meeting):
            return False
        else:
            non_overlapping_meetings.append(current_meeting)

    return True

assert can_attend_all_meetings([[0,30],[5,10],[15,20]]) == False
assert can_attend_all_meetings([[7,10],[2,4]]) == True