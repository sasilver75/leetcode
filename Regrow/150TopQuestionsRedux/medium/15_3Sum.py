"""
3 Sum

Given an integer array nums, return ALL THE TRIPLETS [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k and nums[i] + nums[k] + nums[k] == 0

Notice that the solution set must NOT contain duplicate triplets!
"""


def threesum_naive(nums: list[int]) -> list[list[int]]:
    # Consider all combinations of 3 numbers
    triplets = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet.sort()
                    triplet = tuple(triplet)
                    triplets.add(triplet)

    print(triplets)
    return [list(tup) for tup in triplets]


"""
Surely there's another way we can do this, perhaps in O(N^2) by using more memory?

Realize that there are four ways to get 3 numbers to add to 0:
Case 1: [+, -, 0]
Case 2: [+, +, -]
Case 3: [+, -, -]
Case 4: [0, 0, 0]

Let's use this! First, break the list of nums into P, N, and Z lists!
"""
def threesum(nums: list[int]) -> list[list[int]]:
    triplets = set()
    P, N, Z = [], [], []
    for num in nums:
        if num > 0:
            P.append(num)
        elif num < 0:
            N.append(num)
        else:
            Z.append(num)
    Pset, Nset, Zset = set(P), set(N), set(Z)

    # Consider Case 1: [+, -, 0]
    # If we don't even have any zeroes, we don't need to consider this
    if Z:
        for pos in P:
            if -pos in Nset:
                    triplets.add((pos, -pos, 0))


    # Consider Case 2: [+, +, -]
    if len(P) >= 2 and len(N) >= 1:
        # For all pairs of positive numbers...
        for a in range(len(P)):
            for b in range(a+1, len(P)):
                # Does their sum's complement exist in Nset?
                pos_sum = P[a] + P[b]
                if -pos_sum in Nset:
                    triplets.add((P[a], P[b], -pos_sum))


    # Consider Case 3: [+, -, -]
    if len(P) >= 2 and len(N) >= 2:
        # For all pairs of negative numbers...
        for a in range(len(N)):
            for b in range(a+1, len(N)):
                # Does their sum's complement exist in Pset?
                neg_sum = N[a] + N[b]
                if -neg_sum in Pset:
                    triplets.add((N[a], N[b], neg_sum))


    # Consider Case 4: [0, 0, 0]
    if len(Z) >= 3:
        triplets.add((0,0,0))


    # In Python this will still be O(N^3) because of this ocnversion to Tuples, unfortuantely. If they'd accept a solution in List[tup[int]], this would be O(N^2)
    print(triplets) # This hast he right numbers, in the "Wrong" order according to the test cases. That's fine!
    return triplets



def test(fn):
    assert fn([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert fn([0, 1, 1]) == []
    assert fn([0, 0, 0]) == [[0, 0, 0]]

# test(threesum_naive) # This works but TBH it's really annoying because of the "must not contain duplicate triplets" bit
test(threesum)