"""
Wiggle Sort II (The Return of WiggleSort)

Given an integer array `nums`, reorder it such that
nums[0] < nums[1] > nums[2] < nums[3] ...

In other words:
        second          fourth
first           third           fifth

For example:
[1,4,1,5,1,6]
[1,6,1,5,1,4]
[2,3,1,3,1,2]

It seems like we sort of want to have some idea of "the high numbers"
and then some idea of "the low numbers", and then somehow stitch/zip them
together in some way that satisfies the wigglemaster.

Example:
    Given:      [1, 5, 1, 1, 6, 4]
        Sorted: [1, 1, 1, 4, 5, 6]
    Produce:    [1, 4, 1, 5, 1, 6] or [1, 6, 1, 5, 1, 4]

    Given:      [1, 3, 2, 2, 3, 1]
        Sorted: [1, 1, 2, 2, 3, 3]
    Produce:    [2, 3, 1, 3, 1, 2]

Would a good start be to sort the list? Let's insert what the sorted results
look like into the above examples...

So let's look at the second example.
We can split the sorted list into two halves, giving us the "upper" and "lower"
halves. Let's just assume that we have an even-lenghted list for now...

    Given:      [1, 3, 2, 2, 3, 1]
        Sorted: [1, 1, 2, 2, 3, 3]
            Lows: [1, 1, 2]
            Highs: [2, 3, 3]

How should we stitch these together to make [2,3,1,3,1,2]?
It seems like we have a pointer at the back of each of these two lists
and do low[p], high[p] low[p], high[p], low[p] ...

Does this work for the first example?
    Given:      [1, 5, 1, 1, 6, 4]
        Sorted: [1, 1, 1, 4, 5, 6]
            Lows: [1, 1, 1]
            Highs: [4, 5, 6]

    Without looking at the answer, this would yield:
    [1, 6, 1, 5, 1, 4]
    (One of) the answer(s) was:
    [1, 6, 1, 5, 1, 4]
    Great.

    Fortuantely all of the examples are even-lengthed
    I think if they were odd-lengthed, the real decision is more "how do
    we categorize that odd one into the "lows" or "highs"?
    I think if we make the right choice there, it will just naturally work.
    That comes down to using // or not, I think...
"""


def wiggle_sort_naive(nums: list[int]) -> list[int]:
    def merge(n1: list[int], n2: list[int]) -> list[int]:
        acc = []
        p1, p2 = 0, 0
        while p1 < len(n1) and p2 < len(n2):
            e1, e2 = n1[p1], n2[p2]
            if e1 <= e2:
                acc.append(e1)
                p1 += 1
            else:
                acc.append(e2)
                p2 += 1

        acc.extend(n1[p1:])
        acc.extend(n2[p2:])

        return acc

    def sort(nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid_idx = len(nums) // 2

        return merge(
            sort(nums[:mid_idx]),
            sort(nums[mid_idx:]),
        )

    sorted_nums = sort(nums)  # [1,2,3,4,5,6,7,8]
    mid_idx = len(sorted_nums) // 2
    lows = sorted_nums[:mid_idx]
    highs = sorted_nums[mid_idx:]
    low_pointer = len(lows) - 1
    high_pointer = len(highs) - 1

    acc = []
    # This assumes even lengthed `nums`
    while low_pointer >= 0 and high_pointer >= 0:
        acc.append(lows[low_pointer])
        low_pointer -= 1

        acc.append(highs[high_pointer])
        high_pointer -= 1

    return acc


def test(fn):
    assert fn([1, 5, 1, 1, 6, 4]) in [[1, 4, 1, 5, 1, 6], [1, 6, 1, 5, 1, 4]]
    assert fn([1, 3, 2, 2, 3, 1]) == [2, 3, 1, 3, 1, 2]


test(wiggle_sort_naive)
