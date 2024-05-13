"""
Meeting Rooms II
Category: Intervals

Given an array of meeting time intervals consisting of start and end times
[[s1,e2], [s2,e2], ...] where si<ei for all i, find the MINIMUM NUMBER
of conference rooms required!
"""


def n_rooms_naive(intervals: list[list[int]]) -> int:
    """
    We could just try MeetingRoomsI with 1 room... then try it with 2 rooms...
    then try it with 3 rooms... and see the earliest one that we could do it for.
    """
    intervals.sort(
        key=lambda meeting: meeting[0])  # Do we need to sort by start or start,end? ASC end or DESC end if so?

    def can_fit(n_rooms: int) -> int:
        rooms = [[] for _ in range(n_rooms)]
        for meeting in intervals:
            # Try to slot the meeting into a room
            scheduled = False
            for room_meeting_list in rooms:
                # If there are no scheduled meetings or if the last-scheduled meeting in the room permits this meeting being scheduled, schedule it
                if not room_meeting_list or meeting[0] >= room_meeting_list[-1][1]:
                    room_meeting_list.append(meeting)
                    scheduled = True
                    break  # meeting scheduled, no need to check other rooms
            if not scheduled:
                return False

        # All meetings were successfully scheduled in n_rooms rooms! :)
        print(f"Scheduled meetings using {len(rooms)} rooms: {rooms}")
        return True

    n_rooms = 1
    while True:
        # Scary While True!
        if can_fit(n_rooms):
            return n_rooms

        n_rooms += 1


"""
How can we do better?

What if we started with 1 room and dynamically added a room when we needed it?
Would that give us the optimal answer? Unsure!
"""


def n_rooms(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda meeting: meeting[0])  # Sort by Start, ASC
    rooms = []  # Starting with zero rooms

    for meeting in intervals:
        # Try to schedule the meeting in a room. If you can't, create a new room.
        scheduled = False
        for room_schedule in rooms:
            if not room_schedule or meeting[0] >= room_schedule[-1][1]:
                room_schedule.append(meeting)
                scheduled = True
                break;

        # If we weren't able to schedule it, create a new room for the meeting
        if not scheduled:
            rooms.append(
                [meeting]
            )

    print(rooms)
    return len(rooms)


def test(fn):
    assert fn([[0, 30], [5, 10], [15, 20]]) == 2
    assert fn([[7, 10], [2, 4]]) == 1
    assert fn([[1, 4], [3, 4], [1, 3]]) == 2


# test(n_rooms_naive) # Works :)
test(n_rooms) # Works! :)
