"""
Merge Intervals

Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals,
and then return an array of the NON-OVERLAPPING INTERVALS that cover all of the intervals in the input.
"""

"""
Thinking
- It seems like we're going to be given nodes sorted by start time ASCending, is that true? > "Sure" (made up answer)
- If two elements have the same start time, will they be ordered then by their ending time? > "Can't assume that" (made up answer)



        ---------a
                        ------------b
                                   ----------------c
                                        ---d
                                        
        [[astart,aend]]                                        
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    merged = [intervals[0]]
    for idx in range(1, len(intervals)):
        last_interval = merged[-1]
        current_interval = intervals[idx]

        def can_be_merged(current_interval, last_interval):
            # really if we know that they're sorted ASC, we can just do current_interval[0] <= last_interval[1]
            return last_interval[0] <= current_interval[0] <= last_interval[1]

        if can_be_merged(current_interval, last_interval):
            last_interval[1] = max(last_interval[1], current_interval[1])
        else:
            merged.append(current_interval)

    print(merged)
    return merged


assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge([[1, 4], [4, 5]]) == [[1, 5]]
