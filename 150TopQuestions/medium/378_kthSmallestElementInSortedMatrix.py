"""
Kth Smallest Element in a Sorted Matrix

Given an `n*n` (SQUARE) `matrix` where each of the rows AND columns
is sorted in ASCENDING order,  return the `kth` smallest element in the matrix!

Note that it is the `kth` smallest element in the sorted order, not
the kth smallest distinct element.

You must find a solution with memory complexity better than O(n^2).
(ie better than searching linearly through the n*n matrix.)
"""
from bisect import bisect_right

"""
Questions to ask:
Are we guaranteed that "k" will be valid?
Are we guaranteed that matrix will be not-None? That it will have multiple rows?
"""

"""
Thinking:
This reminds me of searching in a sorted matrix from an earlier question. 
I suppose it's a little harder because we aren't just searching for a 
specific number, we're searching for the KTH SMALLEST element in a sorted matrix...

So we have to not just find the correct element, but also know (as we're searching)
how many numbers occur AFTER our element in the sorted matrix :(

        1   5   9
        10  11  13
        12  13  15      k=8
        
Explaination: The elements in the matrix are [1, 5, 9, 10, 11, 12, 13, (13), 15]
And the 8 smallest number is 13!

I think this kind of lays out a possible solution in an interesting way...
Or does it?
I was thinking that we could just turn the lovely grid into a sorted list
and then select the k-1'th element frmo the list, but that would take some time
to construct, wouldn't it?
It's sort of like merge sort but we've already got our sorted subarrays -- n
of them, depending on whether you'd like rows or columns (n*n).

We could then merge these in O(n*n) time into a sorted list and select the 
smallest element.
Is there a way that we could do better that that, perhaps without actually merging the lists?

I can't think of one that would be better than O(N) (meaning n*n in this case)

    1   5   9
    10  11  13
    12  13  15          k=8, answer is 13

I'm not sure whether the idea of having three points (one per either row or col)
and comparing them and moving the appropriate pointer will get us better than O(n*n), which we would usually
call an O(N) solution (which we have to beat).
I think we have to do some sort of O(NLogN) solution if we can.

Okay, so some sort of binary type search, right? 
But we aren't binary searching for a VALUE, we're binary-searching for 
the kth-smallest value -- for a position in the sorted list, basically.
"""


def kth_smallest_dumb(matrix: list[list[int]], k: int) -> int:
    # 1) Flatten the Matrix into an "unsorted" array
    flattened = [el for row in matrix for el in row]

    # 1a) Validate that the input k is in range [1...len(flattened)]
    if 0 >= k > len(flattened):
        raise ValueError(f"K outside of allowed ranges of [{0}, {k}]")

    # 2) Sort the array ASC
    def merge(l1: list[int], l2: list[int]) -> list[int]:
        # ASC
        p1, p2 = 0, 0
        acc = []
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

    def sort(nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        return merge(
            sort(nums[:mid]),
            sort(nums[mid:]),
        )

    sorted_flat = sort(flattened)

    # 3) Return the k-1'th element from the array
    return sorted_flat[k - 1]


def kth_smallest_dumb_concise(matrix: list[list[int]], k: int) -> int:
    flattened = [el for row in matrix for el in row]
    flattened.sort()
    return flattened[k - 1]


"""
https://www.youtube.com/watch?v=0d6WF79hQME
How can we do better than this O(n**2) solution?

Because it's sorted on row/column fashion, there has to be something that we can 
take advantage of here, right?

One way that we could do that is to do a binary search, but instead
of looking at the elements themselves, we look at the GAP between the minimum
and the maximum in each list. That's going to be our RANGE when we do our B-Search.

And we'll do another bsearch through each row to find how many elements are LESS
than we're searching for.

And as soon as we have that information, we can return our answer.

** One important piece of information that we DO know from the row-ASC and col-ASC
sorting that we've gotten is that the top-left element in the matrix WILL be the minimum,
and the top-right element in the matrix WILL be the maximum.


"""

"""
Explanation:

    1   5   9
    10  11  13
    12  13  15          k=8, answer is 13
    
The idea is that we know that the values in the matrix are encompassed 
in the range [1, 15], since matrix[0][0] is the minimum and matrix[2][2] (above)
is the maximum, based on the rules of row/col sorting described in the problem.

So what we want to do is do a binary search on the range from
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Where what we're looking for is the number whose {something} == k
And that something is the number of numbers in the matrix that are 
less than or equal to it.

Say we calculate mid above as (1 + (15-1)/2) = 8
We look at 8, and ask: "How many numbers are there <= 8 in the matrix?"

To most efficiently calculate that, we could look at each row and ask:
"How many items in this list are <= 8?" And then do a row-wise sum.
This could be extracted into a helper function. It would ask:
"Where would we insert 8 in this list?"
[0, 5, 6], 8 == 3
[0 ,2, 8, 8, 9], 8 == 4
You can see that we want to binary search for the LATEST 8 (or target value)

Okay so again we're binary-searching on the RANGE(min, max) 
    So we look at mid=8 in the example matrix above, and 
determine that there are only 2 elements <= mid.
    Since we're looking for some mid that has k elements <= mid, we know
that we have to look for a larger mid number. So we recurse right.

"""


def kth_smallest_element(matrix: list[list[int]], k: int) -> int:
    def n_lte(nums: list[int], target: int):
        # Given a list nums, how many elements are <= the candidate number?
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] <= target:
                l = mid + 1  # Even if there were only one element in nums == target and we wre at it, l (serving as count) would be index + 1, since 0-based indexing
            else:
                r = mid - 1

        return l

    def get_num_elements_lte_mid(candidate: int):
        # How many elements in matrix are <= the candidate number?
        cnt = 0
        for row in matrix:
            # Do a binary search here to find how many elements are <= k
            x = n_lte(row, candidate)
            cnt += x
        return cnt

    # The actual algo: B-searching the range of [min(matrix), max(matrix)]
    l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

    """
    Warning: 
    Since we're b-searching over the whole range of numbers from [min, max], 
    it's possible that there are multiple correct answers -- and correct answers 
    aren't even in nums too, right?
    [0,3,5,6,6,9], k=2 --> 4 would be a valid answer, but 3 would also be a valid answer
    and would be what we would want to return.
    """
    while l <= r:
        mid = l + (r - l) // 2
        if get_num_elements_lte_mid(mid) >= k:
            # Look Left
            r = mid - 1
        else:
            # Look right
            l = mid + 1

    return l


# -- Tests --
def test(fn):
    assert fn(
        [[1, 5, 9],
         [10, 11, 13],
         [12, 13, 15]], k=8
    ) == 13

    assert fn(
        [
            [2, 7, 12, 14],
            [3, 6, 9, 11],
            [4, 7, 8, 13]
        ], k=5
    ) == 7

    assert fn(
        [[-5]], k=1
    ) == -5

    assert fn(
        [[0,505, 1024],
        [7, 606, 1154],
        [15, 900, 1300]], k=7
    ) == 1024

    assert fn(
        [[0,505, 1024],
        [7, 606, 1154],
        [15, 900, 1300]], k=8
    ) == 1154


# test(kth_smallest_dumb)
# test(kth_smallest_dumb_concise)
test(kth_smallest_element)

# def n_lte(nums: list[int], target: int):
#     print(f"Searching {nums} for {target}")
#     # Given a list nums, how many elements are <= the candidate number?
#     l, r = 0, len(nums) - 1
#
#     while l <= r:
#         mid = l + (r - l) // 2
#
#         if nums[mid] <= target:
#             # look right
#             l = mid + 1
#         else:
#             r = mid - 1
#
#     return l


# assert n_lte([1,2,3,3,3,4,5,6,8], 0) == 0
# assert n_lte([1,2,3,3,3,4,5,6,8], 1) == 1
# assert n_lte([1,2,3,3,3,4,5,6,8], 2) == 2
# assert n_lte([1,2,3,3,3,4,5,6,8], 3) == 5
# assert n_lte([1,2,3,3,3,4,5,6,8], 4) == 6
# assert n_lte([1,2,3,3,3,4,5,6,8], 8) == 9
