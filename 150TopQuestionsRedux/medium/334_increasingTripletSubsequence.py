"""
Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices
(i,j,k) such that (both):
    - i < j < k
    - nums[i] < nums[j] < nums[k]
If no such indices exist, return False

(Is there an increasing triplet subsequence?)
"""


def is_increasing(nums: list[int]) -> bool:
    if len(nums) <= 1:
        return True

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            return False
    return True


assert is_increasing([1, 2, 3, 4, 5])
assert not is_increasing([1, 2, 3, 4, 5, 4])
assert not is_increasing([5, 6, 3, 4])

"""
1. Generate all length-3 subsequences
2. Search for an increasing one

Optimization: Check the the length-3 subsequence if it's increasing once
you've generated it, so that you can early-exit. Doesn't change asmyptotic c
time copmlexity
"""


def increasingTripletNaive(nums: list[int]) -> bool:
    triplets = []

    def generate_triplets(idx: int, built: list[int]) -> None:
        if idx == len(nums) and len(built) != 3:  # If we didn't built a triplet, return
            return
        if len(built) == 3:
            triplets.append(built.copy())
            return

        # Include or don't include
        built.append(nums[idx])
        generate_triplets(idx + 1, built)
        built.pop()
        generate_triplets(idx + 1, built)

    generate_triplets(0, [])
    # print(triplets)

    return any(is_increasing(triplet) for triplet in triplets)


def increasingTripletN2(nums: list[int]) -> bool:
    def update_maxes(biggest_seen: list[int], num: int):
        if num > biggest_seen[0]:
            biggest_seen[1] = biggest_seen[0]
            biggest_seen[0] = num
        elif num > biggest_seen[1]:
            biggest_seen[1] = num

        return biggest_seen

    for starting_index in range(len(nums) - 2):
        biggest_seen = [-float('inf'),
                        -float('inf')]  # Representing the smallest [0] and the second smallest [0] we've seen
        for seek_idx in range(starting_index + 1, len(nums)):
            biggest_seen = update_maxes(biggest_seen, nums[seek_idx])

        if not any(bs == float('inf') for bs in biggest_seen) and nums[starting_index] < biggest_seen[1]:
            return True

    return False


"""
How can we be smarter?

Do a single pass across nums, keeping track of:
    - The smallest we've seen
    - The second smallest we've seen
    
Every number should either be :
    - <= smallest (update smallest)
    - <= secondSmallest (update secondSmallest)
    - > secondSmallest (meaning we have an increasing triplet)

Consider how this works for:
[5, 4, 3, 2, 1]

[4, 5, 3, 2]
"""


"""
WARNING - ERROR
This doesn't work for the case [7,5,3,6], erroneously returning True when the answer should be false

"""
def increasingTriplet(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False  # Can't make a triplet!

    smallest = float('inf')
    secondSmallest = float('inf')

    for i in range(len(nums)):
        num = nums[i]
        if num <= smallest:  # Doesn't seem like we need
            secondSmallest = smallest
            smallest = num
        elif num <= secondSmallest:
            secondSmallest = num
        else:
            return True
        print(f"{i = } {smallest},{secondSmallest}")
    return False


def test(fn):
    # assert fn([4, 5, 3, 2]) == False
    assert fn([7, 5, 3, 6]) == False
    # assert fn([1, 2, 3, 4]) == True
    # assert fn([1, 2, 3, 4, 5]) == True
    # assert fn([5, 4, 3, 2, 1]) == False
    # assert fn([2, 1, 5, 0, 4, 6]) == True


# test(increasingTripletNaive)
# test(increasingTripletN2)
test(increasingTriplet)
