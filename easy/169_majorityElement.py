"""
Given an array nums of size n, return THE MAJORITY ELEMENT

The majority element is the element that appears more than floor(n/2) times.
You may assume that some majority element ALWAYS exists in the array.
"""

"""
Thinking

* I could sort the array, then scan across it, keeping track of the max length
continuous span of the array (and its number). O(nlogn) time and O(1) space.
* I could just scan across the array and use a hash table to keep of the counts,
and another register to keep track of the one with the max value (and its count).
That would be O(N) time and O(N) space.

Is there a way that I could do O(N) time and O(1) space?
"""


def merge_sort_solution(nums: list[int]) -> int:
    """O(nlogn), O(1)
    This works because there is GUARANTEED to be some majority element

    Note there's actually an insight here that I didn't take advantage of
    This is that a majority of a list of nums of length n is going to be
    floor(n/2) + 1 long, at the minimum. That is, 3/4, or 3/5.
    Imagine a line segment of length 5, and then a line segment of length 3
    floating above it. No matter where you slide that 3-length line, left or right,
    (the position of the majority span), the value at index floor(n/2) is always
    going to be the majority element -- so you can skip all this! :)
    """
    sorted = merge_sort(nums)

    if not nums:
        return None

    i = 1
    current_majority_number = nums[i]
    current_majority_count = 1
    span_count = 1
    while i < len(sorted):
        # If the current number is the same as the previous, we're in the same span
        current_number = sorted[i]
        previous_number = sorted[i-1]
        if current_number == previous_number:
            span_count += 1
            # Are we not the current majority number and should we be?
            if (current_number != current_majority_number) and span_count > current_majority_count:
                # Now majority number!
                current_majority_number = current_number
                current_majority_count = span_count
            # Otherwise, are we the current majority already? update majcount to span_count
            elif (current_number == current_majority_number):
                current_majority_count = span_count

        i += 1

    return current_majority_number



def merge_sort(nums: list[int]) -> list:
    """
    Given an unsorted list, sort it
    The intuition of merge sort has two parts:
    1) It's easy to merge two sorted lists into a sorted list
    2) Lists of length 1 or 0 are inherently sorted

    Therefore we recurse, splitting the list in half, until we get to base cases
    of length 0 or 1. Then we merge those lists, bubbling back up.
    """
    if len(nums) <= 1:
        return nums.copy() # Maybe return a NEW array. That's probably nicer.

    mid = len(nums) // 2

    left = merge_sort(nums[:mid]) # YO... this doesn't actually work -- this isn't recursing at all, you fool!
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge(l1: list, l2: list) -> list:
    """Given two sorted lists (even if empty), return a merged, sorted list"""
    merged = []
    p1 = 0
    p2 = 0

    # Both have items left
    while p1 < len(l1) and p2 < len(l2):
        e1 = l1[p1]
        e2 = l2[p2]
        if e1 <= e2:
            merged.append(e1)
            p1 += 1
        else:
            merged.append(e2)
            p2 += 1

    # One is Exhausted -- Append the remaining one (whichever it is)
    merged.extend(l1[p1:])  # It's safe to slice like this, even if p1 is "out of bounds" -- it's just a []
    merged.extend(l2[p2:])

    return merged

def hash_table_soln(nums: list[int]) -> int:
    """O(n), O(n)"""
    counts = {}
    max_count = 0
    max_count_number = None

    for num in nums:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
        if counts[num] > max_count:
            max_count = counts[num]
            max_count_number = num

    return max_count_number

# The "Best" solution
def majority_element(nums: list[int]) -> int:
    """
    Is there a way that we can be O(n) time and O(1) space?
    It really seems like we can't, can we?
    That feeling should make you think: "Is there some weird ass bit-wise
    solution that I'm not thinking of?" -- The answer is Yes :)

    Intuition:
    If an element "majority_element" occurs more than floor(n/2) times,
    then there are at least floor(n/2) elements in num with identical values at
    each bit.
        -> Sure. This is saying if [1,5,3,5,5], then there are going to be
        at LEAST 3 elements with ...101 bit representation.
    Therefore, we can reconstruct the majority_element by "combining" the
    most frequent value at each bit!

    Starting at the least significant bit, we enumerate each bit to determine which
    value is the majority at this bit; 0 or 1. We put this value to the corresponding
    bit of the result. Finally, we end up with the bit result, and convert it.

    Because all of the numbers are in the range -10^9 to 10^9... This can be
    represented in 32-bit, so we only need to enumerate 32 bits for each element.
    """
    pass


print(merge_sort_solution([3, 2, 3])) # == 3
print(merge_sort_solution([2, 2, 1, 1, 1, 2, 2])) # == 2

print(hash_table_soln([3, 2, 3])) # == 3
print(hash_table_soln([2, 2, 1, 1, 1, 2, 2])) # == 2

# print(majority_element([3, 2, 3])) # == 3
# print(majority_element([2, 2, 1, 1, 1, 2, 2])) # == 2

