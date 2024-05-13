"""
Rotate Array

Given an integer array `nums`, rotate the array to the RIGHT by K steps,
where K is non-negative
"""

"""
1) O(N)/O(N) allocate a new array, determining the source index in nums for each index
in rotated nums, creating rotated_nums as a new data structure, setting nums=rotated_nums

2) O(N^2)/O(1) doing N "rotate by one" movements, using a tmp variable

3) O(N)/O(1) doing one "rotate by N" movements, using a tmp variable
"""

"""
Given a rotation of k, which source_index in nums should I look for in order
to populate target_index in nums_rotated?
"""


def rotate_naive_reallocate(nums: list[int], k: int) -> None:
    nums_rotated = [nums[(target_index - k) % len(nums)] for target_index in range(len(nums))]

    # Because of how variable scoping works, we can't just rebind the name nums to nums_rotated,
    # creating a new reference locally for the name nums but not changing the object referred to
    # initially by the name nums. We actually have to directly mutate the object
    for idx in range(len(nums)):
        nums[idx] = nums_rotated[idx]


def rotate_naive_rotation(nums: list[int], k: int) -> None:
    def rotate_right_one(nums: list[int]) -> None:
        """
        In a rotation of [1,2,3] -> [3,1,2]
        The key for these rotations is to be "dragging the change behind you"
        """
        tmp = nums[-1]  # This is the index we're starting from
        for i in range(len(nums)-1, -1, -1): # Traversing through the list backwards
            nums[i] = nums[(i - 1) % len(nums)] # Looking "forward" k=1, to result in a rightward rotation
        nums[0] = tmp  # Setting the incorrectly set (k=1)-1'th index to temp

    for _ in range(k):
        rotate_right_one(nums)


"""

Given [0, 1, 2, 3, 4, 5], k=2
The 5@index5 needs to go to index1  (In our last example, the "first" casualty" was the one
    we saved in the temp variable. In that example, it 


Noticing that the first K elements are fucked up in my answer.
What if I just did my current thing and then patched the first K elements (which should be the last k elements)
using teh last K elements -- but that would only work if k < len(nums)
The patch subarray would be of length k, starting at k%length(N)?


We can't actually esaily generalize the rotate-by-one into rotate-by-k


-------------------

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
"""
def rotate(nums: list[int], k: int) -> None:
    # Goal: [1, 2 ,3 ,4, 5, 6, 7], k=3 -> [5, 6, 7, 1, 2, 3, 4]
    numscopy = nums.copy()

    # ReverseWhole -> [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
    numscopy = numscopy[::-1]

    # Separate -> Into first k elements, last elements
    first_part = numscopy[:k]
    second_part = numscopy[k:]

    # ReverseParts
    first_part = first_part[::-1]
    second_part = second_part[::-1]

    # Combine
    correct = [*first_part, *second_part]

    # Mutate over the existing... We could have done this in-place too I suppose
    for idx in range(len(nums)):
        nums[idx] = correct[idx]







def test(fn):
    nums = [1, 2, 3, 4, 5, 6, 7]
    fn(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    fn(nums, 2)
    assert nums == [3, 99, -1, -100]


# test(rotate_naive_reallocate)
# test(rotate_naive_rotation)
# test(rotate)
