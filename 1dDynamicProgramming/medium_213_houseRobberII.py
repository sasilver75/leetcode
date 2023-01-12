"""
House Robber II

You are a professional robber planning to rob house along a street.
Each house has a certain amount of money stashed.

All houses in this neighborhood are arranged IN A CIRCLE,
meaning the first house is the neighbor of the last house!

Meanwhile, adjacent houses have a security system connected -- the police will automatically
be alerted if two adjacent houses were broken into on the same night!

Given a list of non-negative integers nums representing the amount of money of each
house, return the maximum amount of money you can rob tonight without alerting the cops.
"""

"""

nums:    1   2   3   1
max:     1   2   4   4

Ans: 4


nums:   2   3   2  
max:    2   3   4       <-- Wrong ,can't rob

max:    0   3   2 
"""


def max_loot(nums: list[int]) -> int:
    """
    Insight: Run the "house robber" loop TWICE on different subarrays of our input array, since we aren't allowed to rob the first and the last
    house together.
    Pretty much running it on [0: len-1] and [1: len]

    This is still O(N)
    We don't actually need to keep track of the whole maxes list -- that can be O(1) by just keeping track of the "last two" values.
    """
    # First loop through: Steal the first house. If there are an odd number of houses, this means you won't be able to steal the last house.
    maxes = nums[0:2]
    for i in range(2, len(nums) - 1):
        maxes.append(max(nums[i] + maxes[i - 2], maxes[i - 1]))
    max_candidate_1 = maxes[-1]

    # Second loop through: DOn't steal the first house. This means you can steal the last house.
    maxes = nums[0:2]
    maxes[0] = 0  # Simulate not being able to rob the first house?
    for i in range(2, len(nums)):
        maxes.append(max(nums[i] + maxes[i - 2], maxes[i - 1]))
    max_candidate_2 = maxes[-1]

    ans = max(max_candidate_1, max_candidate_2)
    print(max_candidate_1, max_candidate_2)
    return ans


assert max_loot([2, 3, 2]) == 3  # You can't rob houses 1 and 3, since they're adjacent houses
assert max_loot([1, 2, 3, 1]) == 4  # rob house 1 and house 3
assert max_loot([1, 2, 3]) == 3  # Rob house 3


"""
Neetcode

Basically the premise is the same as houseRobberI -- trying to maximize the amount that we can rob, and we still can't rob houses that 
are adjacent to eachother. 

There's one more catch though -- the houses are arranged in a circle, so we have [2,3,2], but we REALLY have something like 2 -> 3 -> 2 -> 2 -> 3 -> ...

The insight is that we have to run the "house robber" helper function from House robber I TWICE on different subarrays of the problem.
"""

def neetcode_solution(nums: list[int]) -> int:

    def helper(nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[1]


        n_minus_1, n_minus_2 = 0, 0
        for n in nums:
            newRob = max(
                n + n_minus_2,
                n_minus_1
            )
            n_minus_2 = n_minus_1
            n_minus_1 = newRob

        return newRob

    first_rob_soln = helper(nums[0: len(nums) - 1])
    first_no_rob_soln = helper(nums[1:])

    return max(first_rob_soln, first_no_rob_soln)


assert neetcode_solution([2, 3, 2]) == 3  # You can't rob houses 1 and 3, since they're adjacent houses
assert neetcode_solution([1, 2, 3, 1]) == 4  # rob house 1 and house 3
assert neetcode_solution([1, 2, 3]) == 3  # Rob house 3


