"""
Given an integer array `nums` and an integer `k`, return
the `kth` largest element in the array!

Note that it is the `kth` largest element in the sorted order, not the `kth`
distinct element.

*** You must solve it in O(N) time complexity! ***

Note: k=1 is the "highest" number
Note: k will bea  "valid" index.
"""

def find_kth_largest_dumb(nums: list[int], k: int) -> int:
    # in O(NlogN) time and O(N) space complexity using sort-then-select
    def merge(l1: list[int], l2: list[int]) -> list[int]:
        # DESC
        acc = []
        p1, p2 = 0, 0
        while p1 < len(l1) and p2 < len(l2):
            e1, e2 = l1[p1], l2[p2]
            if e1 >= e2:
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
            sort(nums[mid:])
        )

    nums = sort(nums)
    return nums[k-1]


"""
Okay, how could we possibly do this in O(N) time?

I guess we could do this in O(NK) time, if that's okay?
We would just keep track of the "top K" elements as we do one iteration
across the list.
"""
def find_kth_largest(nums: list[int], k: int) -> int:
    top_k = [-float('inf')] * k

    def insert_into_top_k(num: int) -> None:
        # Given a sorted list, insert num into it. The scan for insertion point could be log(N), but I'm just going to linearly scan for it, since it's NK either way
        for idx, val in enumerate(top_k):
            # [5,4,2,1] N = 4, inserting 3   idx=2
            if num > val:
                # Do thing
                for i in range(len(top_k) - 1, idx, -1):
                    top_k[i] = top_k[i-1]
                top_k[idx] = num
                break

    for num in nums:
        insert_into_top_k(num)

    return top_k[k-1]

"""
Is there a better solution than O(NlogK)? We're asked for O(N) specifically.
Neetcode time.

Using a Max Heap will be slightly better because we won't have to sort
the entire input array...
WE can heapify the list and turn it into a heap, in O(N) time.

But we don't necessarily want the largest element in the heap, we want
the K'th largest elment! So we'd have to pop K times to get the kth largest elt.

Every time we pop from the heap, it takes log(n), where n is the size of the heap

So the heap solution would be: O(N + Klog(n))

This is about as good as you can do if you care about worst case time complexity
But there is a solution that could be better if you care about average case 
time complexity 

That's what we'll focus on below
=======
The main part of QuickSort is the Partition step. That's what we'll do first.

We'll take the array and apartition it into two halves:
[3,2,1,5,6,4]
Where every value in the left half is less than or equal to every value in the right half
How can we make sure that it's always going to be half?... We can't, actually...
So the worst-case is actually O(N^2).
How do we pick a pivot?
Let's just randomly pick the rightmost element each time as the pivot value
which will be used to decide what goes in the left/right half.
So we select the last element of [3,2,1,5,6,4] -> 4 as the pivot

Then go through each element in our nums list, and "partition" the list
into two halves by comparing to the pivot value (4)

In-Place:
3 is <= 4, so we'll basically swap it with itself
2 is <= 4, so we'll basically swap it with itself
1 is <= 4, so we'll basically swap it with itself

https://youtu.be/XEmy13g1Qxc

Complicated!

nlogn



"""



def neetcode_quick_select(nums: list[int], k: int) -> int:
    # The target index that we're looking for is going to be len(nums) - k
    k = len(nums) - k  # Let's just say we were looking for the kth element, if the array were sorted

    def quickSelect(l: int, r: int):
        pivot_value = nums[r]
        pointer = l

        for idx in range(l, r): # Will not reach right index (pivot value)
            if nums[idx] <= pivot_value:
                nums[pointer], nums[idx] = nums[idx], nums[pointer]
                pointer += 1

        # Swap the pivot value with the pointer-index-value
        nums[r], nums[pointer] = nums[pointer], nums[r]

        # We may or may not have found a solution at this point
        if k < pointer:
            # Run quickselect on left portion of array
            return quickSelect(l, pointer - 1)
        elif k > pointer:
            # Run quickselect on right portion of array
            return quickSelect(pointer + 1, r)
        else:
            return nums[pointer]

    return quickSelect(0, len(nums) - 1)


def test(fn):
    assert fn([3,2,1,5,6,4], 2) == 5
    assert fn([3,2,3,1,2,4,5,5,6], 4) == 4

test(find_kth_largest_dumb)
test(find_kth_largest) # This could be O(NK), which is still very good if k is small and N is big...
test(neetcode_quick_select) # Wow it works :) In the average, it's O(N), in the worst, O(N^2). Depends on hwo lucky we are with our choice of pivot.