"""
Insert Interval

Given an array of NON-OVERLAPPING intervals `intervals` where intervals[i] = [start, end] represent the start and end of the ith interval,
and intervals are sorted in ASCENDING ORDER BY START

You're given a new interval newInterval = [start, end]
Insert newInterval to intervals such that:
    - intervals is still sorted in ascending order by start
    - intervals does not have any overlapping intervals (you must merge any overlapping intervals if necessary)

Return intervals after the insertion
"""

"""
Not to overcomplicate things

Given existing intervals
            ---------
                        -----------
                                                ---------------
                                                
and a newInterval ~~~~~~


We need to find: 
- The appropriate insertion point based on the start
    - This If we're inserting [1,3] and there's alerady a [1,6], let's insert [1,3] BEFORE the [1,6]
    - This insertion will be based purely on the start, seeking left while t <= c
- Insert the interval
- perform as many merge operations as needed
    - It's possible that we need to seek backwards to find the the leftmost mergable interval
        - Seek left while merging.. 
        
    - When we start htem erging process, I think we're going to be mutating our "L" interval, and continuing to move "R" right while it's mergable with the "L" interval.
        - This means that all of the intervals in L-R have been merged; we can then refdefine the array of intervals as [*arr[:L+1], *arr[R:]]
        
The search is LogN
The insertoin is O(N)
The merging and redefinition of the array is going to be O(N)

Overall: O(N) 
"""


def search_for_insertion_index(intervals: list[int], interval: list[int]) -> int:
    # Return the index
    l, r = 0, len(intervals)

    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_interval = intervals[mid_idx]

        # Seek for the leftmost index having interval.start
        if interval[0] <= mid_interval[0]:
            r = mid_idx - 1
        else:
            l = mid_idx + 1

    return l


def is_mergable(intervalA: list[int], intervalB: list[int]):
    return (
            (intervalA[0] >= intervalB[0] and intervalA[0] <= intervalB[1]) or
            (intervalB[0] >= intervalA[0] and intervalB[0] <= intervalA[1])
    )


def insert(intervals: list[list[int]], new_interval: list[int]) -> int:
    insertion_index = search_for_insertion_index(intervals, new_interval)
    intervals = [*intervals[:insertion_index], new_interval, *intervals[insertion_index:]]
    # intervals[insertion_index] now contains new_interval

    # Walk l back to the first mergable element
    l = insertion_index
    while l > 0 and is_mergable(intervals[l], intervals[l - 1]):
        l -= 1

    print(f"Leftmost mergable is {l} : {intervals[l]}")

    # walk r to the last mergable element, "merging" with the intervals[l] element
    r = l+1
    while r < len(intervals) and is_mergable(intervals[l], intervals[r]):
        # "Merge" l with r, updating l's end time with the latest r of either of hem
        intervals[l][1] = max(intervals[l][1], intervals[r][1])
        r += 1

    # Return the intervals list with the "merged cells" (merged into intervals[l]) cut out of it
    return [*intervals[:l+1], *intervals[r:]]




def test(fn):
    assert fn([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert fn([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]


test(insert)
