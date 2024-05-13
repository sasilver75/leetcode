"""
Longest Consecutive Sequence

Given an unsorted array of integers nums, return the lenght of hte
longest consecutive elements sequence

** You must write an algorithm that runs in O(N) time. **

"""
import time

"""
A consecutive sequence of elements by the definition of this problem is a
range of present numbers with a start and an end 

How can we take this list of ints and turn it into
"""


def longest_consecutive_naive(nums: list[int]) -> int:
    numset = set(nums)
    max_span_length = 0

    for num in numset:
        span_length = 0
        cur = num
        while cur in numset:
            span_length += 1
            max_span_length = max(max_span_length, span_length)
            cur += 1

    return max_span_length


# Optimized: If we sort nums, then we can avoid N^2 behavior by not considering num in numsets that are already in a span.
def longest_consecutive_naive_optimized(nums: list[int]) -> int:
    nums.sort()
    numset = set(nums)
    processed = set()
    max_span_length = 0

    for num in numset:
        if num in processed:
            continue
        span_length = 0
        cur = num
        while cur in numset:
            span_length += 1
            max_span_length = max(max_span_length, span_length)
            processed.add(cur)
            cur += 1

    return max_span_length


"""
How can we do it in linear time (perhaps in multiple linear passes)

We can't sort the numbers.
Consider the Start, Ends of these ranges.

We could try and create these [Start, End] ranges, or we could create [Starts] and [Ends]. 
Let's try doing that latter one.
    What defines a start? it's a number for which number-1 is not found in nums.  (Implication: a set might be useful)
    What defines an end? It's a number for which number-1 is not found in nums.

Okay, so now that we have starts and ends... Now what? 
The starts/ends are not necesarily ordered. Let's look at an example

nums: [100, 4, 200, 1, 3, 2]

starts: [100, 200, 1]
ends: [100, 4, 200]

The problem is that starts/ends are necessarily ordered in a favorable way, in order to match them up
    And sorting them would put this in O(NLogN) territory
It would be nice if they came sorted like:
starts: [1, 100, 200]
ends: [4, 100, 200]
Then they could be paired up in a linear fashion... But we can't expect them to come out this way, unless the input were sorted.

Instead of generating both starts AND ends, let's just generate the statrs
We can just generate the starts, and then linearly probe for the end of each, keeping track of the longest span
    Because we're only going to be visiting numbers that are in the input, and because we won't visit numbers more than once while probing, we'll
    still be in linear asymptotic time complexity.
"""
def longest_consecutive(nums: list[int]) -> int:
    numset = set(nums)
    starts = [num for num in nums if num - 1 not in numset]
    longest_consecutive_span_length = 0

    for start in starts:
        span_length = 0
        cur = start
        while cur in numset:
            span_length += 1
            longest_consecutive_span_length = max(longest_consecutive_span_length, span_length)
            cur += 1

    return longest_consecutive_span_length





def timed(fn):
    def wrapper(*args, **kwargs):
        start = time.process_time()
        res = fn(*args, **kwargs)
        elapsed = time.process_time() - start
        print(f"{elapsed = }")
        return res

    return wrapper


@timed
def test(fn):
    assert fn([100, 4, 200, 1, 3, 2]) == 4
    assert fn([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


test(longest_consecutive_naive)
test(longest_consecutive_naive_optimized)
test(longest_consecutive)
