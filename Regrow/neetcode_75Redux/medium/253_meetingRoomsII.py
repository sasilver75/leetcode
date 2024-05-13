"""
Meeting Rooms 2

Given an array of meeting time intervals consisting of start and end times [[s1,e1], [s2,e2], ...] where for any meeting, (si < ei)

Find the MINIMUM NUMBER OF CONFERENCE ROOMS REQUIRED!

For exmaple, given [[0,30], [5,10], [15,20]]    return 2

"""

"""
Thinking:
- I notice that the given inputs aren't sorted by start time. One of the first things that we should do is sort them by start, end
- Then, it's just merge intervals, except the "merged" meeting is isn't slotted into the next meeting room. If no meeting rooms are available, then
we have to create a new meeting room.
"""


def can_insert(meeting: list[int], room: list[list[int]]) -> bool:
    """Given a meeting and a populated room, can the meeting be inserted?"""
    last_meeting = room[-1]
    # Making the executive assumption that [5,10] and [10,15] can go in the same room
    return meeting[0] >= last_meeting[1]

def number_meeting_rooms(meetings: list[list[int]]) -> int:
    # Sort by (START, END) ASC
    meetings.sort(key=lambda meeting: (meeting[0], meeting[1]))

    rooms = []

    for meeting in meetings:
        inserted=False
        for room in rooms:
            if can_insert(meeting, room):
                room.append(meeting)
                inserted=True
                break
        if not inserted:
            rooms.append([meeting])

    print(rooms)
    return len(rooms)


assert number_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
assert number_meeting_rooms([[7, 10], [2, 4]]) == 1
