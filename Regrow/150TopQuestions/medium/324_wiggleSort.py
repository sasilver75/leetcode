"""
Wiggle Sort

Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] ...`

You may assume that the input array always has a valid answer.
"""

"""
It's interesting to note that that it's not like you're zippering together
the even and odd-indexed values from a sorted array, though you could 
do that as your naive solution.

The only thing that needs to be satisfied is that is that even-indexed indices
have values that are less than their neighbors, and odd-indexed indices
have values that are greater than their neighbors.

It doesn't say anything about idx[1] > or < than idx[2], for instance.
"""


def wiggleSortDumb(nums: list[int]) -> list[int]:
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

        mid = len(nums) // 2

        return merge(
            sort(nums[:mid]),
            sort(nums[mid:])
        )

    sorted_nums = sort(nums)  # [1,2,3,4,5,6,7] -> # [1,7,2,6,3,5,4]
    print("Sorted: ", sorted_nums)
    acc = []
    l, r = 0, len(sorted_nums) // 2
    while r < len(sorted_nums):
        acc.append(sorted_nums[l])
        acc.append(sorted_nums[r])
        l += 1
        r += 1

    if len(sorted_nums) % 2 == 1:
        acc.append(sorted_nums[l])

    print(acc)
    return acc

"""
Is there a way that we can do better than the O(NLogN) solution above,
where we sorted, and then walked through the list, "zipping"
"""

def wiggleSortDumbShort(nums: list[int]) -> list[int]:
    # This is an abbreviated version of the function above - it works! :)
    nums.sort()
    mid = len(nums) // 2
    return [
        el for pair in zip(
            nums[:mid],
            nums[mid:]
        ) for el in pair
    ]

"""
Neetcode! :)

We're given an unsorted integer array, and we want to reorder it such that
our equalities hold:

nums[0] <= nums[1] >= nums[2] <= nums[3] ...

The restriction is that we want to be able to do it IN PLACE
But there's a thought process that can actually make it pretty simple.

Would this have been easier if we had a sorted list?

[1,2,3,4,5,6]

Yes! We can swap [2,3], [4,5]

[1,3,2,5,4,6]   _-_-_-   -> Good!

The downside of this approach is that we had to sort before doing the linear-time
swap, so the actual approach is O(NlogN)

But there IS a way to do this in O(N) time WITHOUT sorting the array!

[3, 5, 2, 1, 6, 4]

Let's look at the first two values: We want to second value to be greater
than the first one.
If that's already the case, like it is here (([3,5]), we don't have to do
anything! 

Now we want to look at the next two values (moving the "window" forward by
one): [5,2]. We want the second value to be LESS THAN the previous one, here.
Again, that already is the case, so we don't have to do anything.

Now let's look at the next pair:
[2,1]
We want the second value to be GREATER than the previous one.
That is NOT the case here! So what should we do? 

I mean... to make THESE TWO values "correct," we could just swap them...
But is it possible that we could have messed something up in the previous 
part of the array?
                                P  V  P    (desired peak valley peak)
Consider just the section [..., 5, 2, 1, ...] of the array above

So we confirmed that [5,2] is correct.
Then we looked at [2,1], and it was NOT correct.
If we swap to [5,1,2], how do we know that we aren't fucking up [5,1] while we "fix" [1,2]?

What did we WANT TO SEE in the original [2, 1] window? We WANTED to see a number
GREATER than 2 in the second place, but we saw a number smaller than two.

So what we have CURRENTLY is [2, {smallerThanTwo}] (we actually want a largerThanTwo)

If we had already validated  [5,2] as [5, {smallerThanFive}], we know that 
if we replace {smallerThanFive} with {smallerThanTwo}, the rule will still be respected!

So we can safely "swap" [2,1] to [1,2] without breaking the rule for the existing [5,2] as it swaps to [5,1]!
"""

def wiggleSort(nums: list[int]) -> list[int]:
    for i in range(0, len(nums) - 1):
        if i % 2 == 0:
            # Should be a Trough; i.e. i+1th number should be GREATER
            if not (nums[i+1] > nums[i]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        else:
            # Should be a Peak; i.e. i+1th number should be LESSER
            if not (nums[i+1] < nums[i]):
                nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums

# -- Test Zone --
def obeys_wigglesort(nums: list[int]):
    for idx, num in enumerate(nums):
        if idx % 2 == 0:
            # Should be Trough (strict)
            left_neighbor = nums[idx - 1] if idx - 1 >= 0 else float('inf')
            right_neighbor = nums[idx + 1] if idx + 1 < len(nums) else float('inf')
            if not (left_neighbor > num < right_neighbor):
                return False

        else:
            # Should be Peak (strict)
            left_neighbor = nums[idx - 1] if idx - 1 >= 0 else float('-inf')
            right_neighbor = nums[idx + 1] if idx + 1 < len(nums) else float('-inf')
            if not (left_neighbor < num > right_neighbor):
                return False

    return True

assert obeys_wigglesort([1,3,2,4,3,4,3,5,2,4]) == True
assert obeys_wigglesort([1,4,2,3,3,5,4,6]) == False
assert obeys_wigglesort([-1,15,14,16,-2,]) == True


def test(fn):
    assert obeys_wigglesort(fn([1, 5, 1, 1, 6, 4])) # == [1, 6, 1, 5, 1, 4]
    assert obeys_wigglesort(fn([1, 3, 2, 2, 3, 1])) # == [2, 3, 1, 3, 1, 2]

test(wiggleSortDumb)
test(wiggleSortDumbShort)
test(wiggleSort) # Works! :)