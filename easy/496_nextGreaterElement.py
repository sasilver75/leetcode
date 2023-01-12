"""
The NEXT GREATER ELEMENT of some element x in an array is
the FIRST GREATER element that is TO THE RIGHT of x in the same array!

You are given two 0-index integer arrays nums1 and nums2 where nums1 is
a subset of nums2.

FOR EACH I IN 0 <= i < nums1.length, find the index j such that
nums[i] == nums[j], and determine the NEXT GREATER ELEMENT of nums2[j] in nums2.

If there is no next great element, then the answer for this query is -1.

Constraints:
* All integers in nums1 and nums2 are unique, within their arrays
* All the integer of nums1 also appear in nums2
"""

"""
Thinking:
It looks from the answers that "next greater element"
means the first element following "element" that is greater than element.
"""

"""
This is an O(N^2) Solution, since we might be checking every element in numsB for every element in numsA.
It's pretty much a scan where the interior loop is looking for a number greater than X, but only after a boolean is tripped indicating that we've passed X in nums2

"""
def next_greater_dumb(numsA: list[int], numsB: list[int]) -> list[int]:
    ans = []
    for a in numsA:
        found = False
        appended = False
        for b in numsB:
            if a == b:
                found = True
            if b > a and found:
                ans.append(b)
                appended = True
                break;
        if not appended:
            ans.append(-1)

    return ans


assert next_greater_dumb([4,1,2], [1,3,4,2]) == [-1, 3, -1]
assert next_greater_dumb([2,4], [1,2,3,4]) == [3, -1]


"""
A better solution to the seeking problem in numsB might be to sort numsB... but we can't do that, can we? 
Because we need to preserve in some way the original order of numsB to get the NEXT OCCURRING GREATER NUMBER for a given number.

Instead of doing the search per-item in numsA, is there a way that we could efficiently precompute the answers for all numbers in numsB?
Such that something like
[1, 3, 4, 2]
turns into 
[(1,3), (3,4), (4,-1), (2,-1)], or something, where each element is (val, val of next greater element)

But then when we are looking through elements in numsA [4, 1, 2], we still have to linearly scan for the complement.
A great way to not linearly scan is to use a hashtable...
We're given the constraint that all elements in each list are unique, which might make that a workable solution.

What if we were able to turn the 
[(1,3), (3,4), (4,-1), (2,-1)] into { 1:3, 3:4, 4:-1, 2:-1 } ? Or maybe the -1's wouldn't even be in there.

So how do we process  
[1, 3, 4, 2] into { 1:3, 3:4 } in O(N) time?
"""

def next_greater(numsA: list[int], numsB: list[int]) -> int:
    """
    An interesting property that you'll note about our use of a stack
    is that the numbers in it are always going to be descending from left-to-right
    That is, the lowest number will be on the top.

    That's because we only add a number to the stack when it's LESS THAN the top of the stack
    But before doing that, we pop off (and process) all of the elements from the stack that are LESS than our number

    Any numbers remaining in the stack at the end don't have a nge in nums2.
    """
    nge = {}
    stack = []
    for num in numsB:
        # While the top number of the stack is LESS THAN the current number
        while stack and num > stack[-1]:
            # Mark that stack number's next greatest element as the current element
            nge[stack.pop()] = num
        stack.append(num)

    ans = []
    for num in numsA:
        ans.append(nge.get(num, -1))
    return ans

# assert next_greater([4,1,2], [1,3,4,2]) == [-1, 3, -1]
# assert next_greater([2,4], [1,2,3,4]) == [3, -1]
assert next_greater([4,3,7,5,9,2,1,8,6], [6,4,1,3,5,8,9,7,2]) == [5,5,-1,8,-1,-1,3,9,8]

"""
Here's another way of thinking about this
[1, 3, 2, 4, 2] can be visualized as (turn your head to the right)

X                   1     Before this: Stack is []      After this: Stack is [1]
X   X   X           3     Before this: Stack is [1]     After this: Stack is [3] because 1 was popped off and processed {1:3}
X   X               2     Before this: Stack is [3]     After this: Stack is [3, 2] because we couldn't pop any elements off the stack {1:3}
X   X   X   X       4     Before this: Stack is [3,2]   After this: Stack is [4] because we popped off 2 then 3 and processed them {1:3, 2:4, 3:4}
X   X               2     Before this: Stack is [4]     After this: Stack is [4, 2] because we couldn't pop any elements off the stack {1:3, 2:4, 3:4}

So... Given {1:3, 2:4, 3:4}

We then scan through the complementing nums1 array, and append to a result array either lookup[elt] or -1 for each element elt in nums1
"""

