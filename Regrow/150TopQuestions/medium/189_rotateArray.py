"""
Given an ARRAY, rotate the array to the RIGHT by `k` steps,
where k is non-negative.
"""

"""
Okay, I think the idea might be that you start at some place in the 
array (maybe at the start, maybe at some other point), and then look
backwards K steps -- that's the value that should be at your current location!
Alternatively, you could look forward N-k steps, where N is the length
of the `nums` list.

Either way, you're going to be modulus-wrapping around the list.

I'm guessing there's going to be a little snag where you're "overwriting"
data that you'll later need?

For example, in:
nums = [1,2,3,4,5,6,7], k = 3
Which becomes
[5,6,7,1,2,3,4]

Say we're starting at index=0.
We might look forward to nums[0+(7-3)] -> N[4] and see 5, which needs
to them overwrite our current value from 1 -> 5

But when we get to index=3, we'll be looking forward to index 0... where
we'll see 5, rather than the 1 that we neeed.

Is there any index that we could start at that would solve this, or no?
What if we started at the N-k'th index?

[1,2,3,4,5,6,7]
         ^
[1,2,3,4,1,6,7]
[1,2,3,4,1,2,7]
Nope, this clearly isn't working.

It's a ROTATION... Can we just keep track of one 


 
"""


def rotate_dumb(nums: list[int], k: int) -> list[int]:
    # Given that we have to look forward len(nums)-k spaces to find the value that we should be
    # O(N) time and O(N) space
    return [nums[(idx + len(nums) - k) % len(nums)] for idx in range(0, len(nums))]


"""
Can we do it in O(1) space, though?

I'm thinking about the "Rotate Matrix" example
Where imagine we were rotating four values that were each in the corner 
of a matrix

    1     >     2               4       1
    ^           V       -->    
    4      <    3               3       2
    
The "easy" way to imagine doing this was to use a single temp variable
temp = 2
2 = 1
1 = 4
4 = 3
3 = temp

In that example, I could just enumerate the "transition" logic, since there 
were only four examples. I need to find the generic way of doing that in
a list of length n

tmp = nums[0]
cur_idx = 0
for _ in range:
    # overwrite the value at the current index with the value that needs to be here
    # move cur_idx to the "source_value's index"
    
# Overwrite nums[cur_idx] with tmp

Let's try something like that!

I think just like in the square example, every index has exactly one index
that is "pointing to it."
So we take a snapshot of the "first" (randomly chosen, really) value,
and then overwrite it with its source.
And then overwrite the source with ITS source
and then overwrite the sourcesource with ITS source ...

And then we use that snapshot to overwrite the value 

"""

"""
nums = [1,2,3,4,5,6,7], k = 3
Which becomes
[5,6,7,1,2,3,4]


There's a problem that I'm noticing with this function where it
breaks down when N is divisible by k... Annoying!
"""


def rotate(nums: list[int], k: int) -> list[int]:
    # This is intended to be an O(N) time complexity, regardless of k
    N = len(nums)
    tmp = nums[0]
    cur_idx = 0
    # Do N rotations!
    """
    You can do N rotations and then correct the last one
    """
    for _ in range(N):
        # At the current target index, overwrite it with the value from the
        # appropriate source index! Then move to consider that source index
        source_index = (cur_idx - k) % N
        nums[cur_idx] = nums[source_index]
        cur_idx = source_index

    # We have tmp, which was the original value at 0. That number was supposed
    # to be correctly rotated to the right by k, but it neve was (correctly). Use tmp now!
    print("Before: ", nums)
    nums[k] = tmp

    print("After: ", nums)
    return nums


"""
SourceValueOfIndexI = 

N=7
K=3

0 -> 4    (0 + 7 - 3) % 7 = 4
1 -> 5    (1 + 7 - 3) % 7 = 5
2 -> 6    (2 + 7 - 3) % 7 = 6
3 -> 0    (3 + 7 - 3) % 7 = 0
4 -> 1     ... 1
5 -> 2     ... 2
6 -> 3
"""


def rotate_right(nums: list[int]):
    # What if we had a function that could rotate a list by one?
    # This would be a kN time complexity, and would be quite slow for large k
    tmp = nums[-1]
    for i in range(len(nums) - 1, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = tmp
    return nums


def rotate_array_simple(nums: list[int], k: int) -> list[int]:
    for _ in range(k):
        nums = rotate_right(nums)
        # print(nums)
    return nums



"""
Neetcode: 

There are three solutions:
1) O(N), O(N) where we do a list comprehension, basically
2) O(N^2), O(1) where do we do N single-rotations
3) O(N), O(1) where we do a single smart pass through the list

It's very tricky to come up with the O(N), O(1) solution.


(i+k) % N is the index destination of the current value at index i

[1,2,3,4,5], k=2        -->   [4,5,1,2,3]

Hint:
* Notice that when we rotate the array, we really have two "portions" of
the resulting array.
    - We have the [1,2,3] portion that will be moved to the end of the array
    - We have the [4,5] portion, the last k elements, that will be moved to the beginning of the array
    
[1,2,3,  4,5]
    
What would happen if we took the entire input array and reversed it?

[5,4,  3,2,1]

And then reversed the two "segments" we talked about earlier?
Meaning the first K elements, and then the remaining elements

[4,5  1,2,3]   -->  [4,5,1,2,3]

Is this what we were looking for? yes!

Interesting! Why does this work!


Catch: What if we were rotating a large amount, such that k > N?
We'd have to do some modulus work :)
We could actually just immediately mod K by he length of an input,
since [1,2],k=3 and [1,2],k=1 produce the same result!
"""
def neetcode_rotate(nums: list[int], k: int) -> list[int]:
    N = len(nums)
    def reverse_inplace(l: int, r: int) -> None:
        l, r = l % N, r % N
        # Inclusive of [l,r]
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    # Reverse the whole list
    reverse_inplace(0, N - 1)

    # Reverse the first K elements (inclusive) of nums, and then the remainder
    reverse_inplace(0, k-1)
    reverse_inplace(k, N-1)

    print(nums)
    return nums


def test(fn):
    assert fn([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert fn([1, 2, 3, 4, 5, 6, 7], 2) == [6, 7, 1, 2, 3, 4, 5]
    assert fn([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [7, 8, 9, 1, 2, 3, 4, 5, 6]
    assert fn([-1, -100, 3, 99], 3) == [-100, 3, 99, -1]
    assert fn([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert fn([2,5], 3) == [5,2]


# test(rotate_dumb)
# test(rotate_array_simple)
# test(rotate)
test(neetcode_rotate)