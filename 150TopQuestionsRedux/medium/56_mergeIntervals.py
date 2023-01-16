"""
Merge Intervals

Given an array intervals where intervals[i] = [start, end], merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all of the intervals in the input.
"""

"""
It's easier to imagine merging these intervals if you consider them as a gant chart

---------
   -------------
          ----
                     -------------
                                     
Above, are 1 and 2 mergable? Yes, because 2start >= 1start and <= 1end. We take the later of the two end times
Are (12) and 3 mergable? Yes, because 3start >= (12)start and <= (12) end. We take the later of teh two end times.
Are (123) and 4 mergable? No, becuase of rules above. 

Steps:
1) Sort by start time ascending
2) Merge possible intervals
3) Return list of post-merge intervals
"""
def merge(intervals: list[list[int]]) -> int:
    intervals.sort(key= lambda interval: interval[0])

    merged = [intervals[0]]
    for idx in range(1, len(intervals)):
        current_interval = intervals[idx]
        last_interval = merged[-1]
        if current_interval[0] <= last_interval[1]:
            last_interval[1] = max(last_interval[1], current_interval[1])
        else:
            merged.append(current_interval)
    return merged

def test(fn):
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4], [4,5]]) == [[1,5]]

test(merge)