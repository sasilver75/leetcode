"""
Longest Consecutive Sequence

Given an unsorted array of integers `nums`, return the LENGTH
of the LONGEST CONSECUTIVE ELEMENTS SEQUENCE!

Where consecutive elements are like [1,2,3,4], for example.
But these numbers don't need to be consecutive in the list. See tests.

*** You must write an algorithm that runs in O(N) time.
Sam Note: Makes no note about memory...
"""

"""
The dumb (and wrong, given requirements) way to do this would be to
sort the list, and then do a linear scan. But this runs in O(nlogn), not O(N)
"""

def longest_consecutive_dumb(nums: list[int]) -> int:
    def merge(l1: list[int], l2: list[int]) -> list[int]:
        acc = []
        p1, p2 = 0, 0
        while p1 < len(l1) and p2 < len(l2):
            e1, e2 = l1[p1], l2[p2]
            if e1 <= e2:
                acc.append(e1)
                p1 += 1
            else:
                acc.append(e2)
                p2 += 1

        acc.extend(l1[p1:])
        acc.extend(l2[p2:])
        return acc

    def sort(nums: list[int]) -> int:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2

        return merge(
            sort(nums[0:mid]),
            sort(nums[mid:])
        )

    nums = sort(nums)

    longest_span = 0
    current_span = 0
    for i in range(len(nums)):
        prev = nums[i-1] if i-1 >= 0 else None
        cur = nums[i]

        current_span = current_span + 1 if (prev is not None and prev+1 == cur) else 1
        longest_span = max(longest_span, current_span)

    return longest_span


"""
Okay, but we can't do a sorting solution, because that's O(nlogn).
How can we (perhaps take advantage of more memory?) To do this in a series 
of single passes instead, achieving O(N) time?

We could do something like a counting sort, but that would be bounded by O(max(nums)), not O(N)
"""

def longest_consecutive_counting_sort(nums: list[int]) -> int:
    observed = [False] * (max(nums) + 1)
    for num in nums:
        observed[num] = True

    running = 0
    total = 0
    for idx, obs in enumerate(observed):
        prev =  observed[idx-1] if idx - 1 >= 0 else None

        running = running + 1 if (prev and obs) else 1
        total = max(total, running)

    return total

"""
Longest Consecutive Sequence

How to do it in O(N) time, though?
(Side note: We could also generate all possible subsequences and then go thorough each of them, which would be 2^N or something)

Okay, here's the insight:

If we visualize  [100, 4, 200, 1, 3, 2] on a number line:

        1   2   3   4   ... ... 100 ... ... 200
        _____________           ___         ____
        
So these subsequences are characterized be [start, end] values

What characterizes the `start` of a subsequence? Even if it's a subsequence of length 1?:
--> The `start` is the `num` for which `num-1` is NOT in `nums`

What characterizes the `end` of a subsequence? Even if it's a subsequence of length 1?:
--> The `end` is the `num` for which `num+1` is NOT in nums

SO We can build up a list of starts: [1, 100, 200]
and a list of ends: [4, 100, 200]
and then ZIP them together:  (this works because lengths will be the same and these subsequences will be non-overlapping on a number line)
[(1,4), (100,100), (200,200)], 

We KNOW NECESSARILY that each of the values 1...4 ARE ACTUALLY PRESENT in that subsequence, too!
The length of each one will be (top - bottom + 1)
Take the make of these.


Oh shit. Okay actually the problem with ZIPPING like this is that we might not encounter the starts/ends in the same order
So I have a case for 
[100, 4, 200, 1, 3, 2]            {1-4}  {100-100}  {200-200}
Which ends in 
starts: [100, 200, 1]
ends: [100, 4, 200]

So you can see that our starts and ends would need to be sorted before zipping. That's no good!

The suggestion that Neetcode suggests is to just collect the STARTS:

starts:[100, 200, 1]
Then for each starting index,
walk to the right until we find a number that is NOT in nums, and add the appropriate number to ends

"""

def longest_consecutive_sequence(nums: list[int]) -> int:
    num_set = set(nums)
    starts = []
    ends = []

    for num in nums:
        if num-1 not in num_set:
            starts.append(num)

    for start in starts:
        cur = start
        while cur in num_set:
            cur += 1
        ends.append(cur-1)

    # Now we should have ends that match with starts, in order

    ranges = zip(starts, ends)
    max_length_range = 0

    for start, end in ranges:
        max_length_range = max(max_length_range, end - start + 1)

    return max_length_range



# -- Test --
def test(fn):
    assert fn([100, 4, 200, 1, 3, 2]) == 4  # [1,2,3,4]
    assert fn([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9  #0-8

# test(longest_consecutive_dumb)
# test(longest_consecutive_counting_sort)
test(longest_consecutive_sequence)