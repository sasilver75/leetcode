"""
House Robber

You're a professional robber planning to rob houses along a street.
EAch house has a certain amount of money stashed.
The only constraint stopping you from robbing ALL of them is that adjacent houses
have security systems that are connected to eachother, and the police will be contacted
if two adjacent houses are broken into on the same night!

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money that you can rob tonight WITHOUT alerting the police!
"""


def max_robbery_brute(house_values: list[int]) -> int:
    # What's the "dumbest" way to do this?
    # For each house... you either rob it, or you rob the following one.
    def helper(house_values: list[int], idx: int, total: int, can_rob=False):
        print(house_values, idx, total, can_rob)
        # Base Case
        if idx >= len(house_values):
            return total

        # Either you can currently rob (didn't rob the last house), or you can't rob (robbed the last house
        # If you CAN rob, you can either ACTUALLY ROB this house, or NOT ROB this house
        # If you CAN'T rob, you need to skip this house

        if can_rob:
            return max(
                helper(house_values, idx + 2, total + house_values[idx], can_rob=True),
                # You can rob and DO rob this house! Skip the next house and get your robbing back
                helper(house_values, idx + 1, total, can_rob=True)  # Though you can rob, don't rob. Skip this house.
            )
        else:
            return helper(house_values, idx + 1, total, can_rob=True)  # You can't rob. Skip this house.

    ans = helper(house_values, 0, 0, True)
    print(ans)
    return ans


# assert max_robbery_brute([1, 2, 3, 1]) == 4  # Rob house 1 and 3
# assert max_robbery_brute([2, 7, 9, 3, 1]) == 12  # Rob house 1, rob house 3, and rob house 5


"""
Can we do better?


Decision tree time?...

[1  2   3   1]
              
Left: No Rob
Right: Rob

                                        (root)
                    0                                           1
            0               2                           1                    _1    
        0       2       2       _2                   1       4            1          4
     0    1   2   _2   2   3   2     3           1      2        _4     1   2       4       _4
                

We can't do a 1D from teh back, asking whether we should rob there or not...

      loot      1       2       3       1
index
0               _       _       _       _
1               _       _       _       _
2               _       _       _       _
3               _       _       _       _

One of these, maybe? Or do these kind of represent the same thing... this IS a one-dimensional problem :)
But the idea of transitions is probably right in some way. I don't think we need to keep track of the idea of 
index AND loot...

What if the question were, for each index: "If this were the last house, what's the max that we could get by this point?"
And then we populated that array left to right? Would that even guarantee the correct answer?
"""

# def max_robbery(house_values: list[int]) -> int:
#     maxes = [house_values[0], max(house_values[0], house_values[1])] # Assuming there are at least two houses...
#     for val in house_values[2:]:
#         max_val =
#     return maxes[-1]

"""
Insight:
To know the max that we can rob from the entire neighborhood...Either:
    Rob from teh first house, then find the maximum from the remaining houses (3rd:...) (skipping the second house).
        This "remaining houses" is a subproblem
    SKip the first house, then find the maximum from the remaining houses (2nd:..)
    
If we want to find the maximum that we can rob from the entire list, we have two choices:

rob = max(
    array[0] + rob(array[2:]),  # DO Rob this house and then skip the next house, considering the remaining houses
    rob(array[1:])              # DON'T Rob this house and then consider the remaining house 
)

^ This is the RECURRENT RELATIONSHIP. That's the way to break up the Dynamic Progamming problem. The result depends only on these two concepts.
"""


def max_robbery_recursive(house_values: list[int]) -> int:
    if not house_values:
        return 0

    return max(
        house_values[0] + max_robbery_recursive(house_values[2:]),
        max_robbery_recursive(house_values[1:])
    )


assert max_robbery_recursive([1, 2, 3, 1]) == 4  # Rob house 1 and 3
assert max_robbery_recursive([2, 7, 9, 3, 1]) == 12  # Rob house 1, rob house 3, and rob house 5

"""
Moving from right to left...
        nums: [1,  2,  3,  1]
        maxs: [1,  2,  4,  1]

So at every index, moving left to right, the max is:
    
    max(
        current + nums[idx - 2], # Rob after not robbing last time
        nums[idx-1]             # Don't Rob since we can't
    )
    
You might be thinking: Wait, isn't there a danger of robbing twice in a row? Nope! 
It's more like with the rules above, we NEVER "don't rob" twice in a row. If we're going to rob, we assume that we also robbed
two spaces ago.

"""


def max_robbery(nums: list[int]) -> int:
    maxes = nums[0:2]
    for i in range(2, len(nums)):
        maxes.append(
            max(
                nums[i] + maxes[i - 2],  # Rob
                maxes[i - 1]  # Don't Rob
            )
        )
    return maxes[-1]

assert max_robbery([1, 2, 3, 1]) == 4  # Rob house 1 and 3
assert max_robbery([2, 7, 9, 3, 1]) == 12  # Rob house 1, rob house 3, and rob house 5

"""
We only ever actually need to look at the previous two values that were computed.
So we can reduce our memory usage...to just keeping track of two values, instead of generating a "maxes" list of size N!
"""

def max_robbery_best(nums: list[int]) -> int:
    # Assuming at least 3
    n_minus_2 = nums[0]
    n_minus_1 = nums[1]
    for i in range(2, len(nums)):
        best_candidate = max(n_minus_2 + nums[i], n_minus_1)
        n_minus_2 = n_minus_1
        n_minus_1 = best_candidate
    return best_candidate

assert max_robbery_best([1, 2, 3, 1]) == 4  # Rob house 1 and 3
assert max_robbery_best([2, 7, 9, 3, 1]) == 12  # Rob house 1, rob house 3, and rob house 5


def neetcode_solution(nums: list[int]) -> int:
    # Assuming at least 3
    n_minus_2 = 0
    n_minus_1 = 0
    for num in nums:
        best_candidate = max(n_minus_2 + num, n_minus_1)
        n_minus_2 = n_minus_1
        n_minus_1 = best_candidate
    return best_candidate

assert neetcode_solution([1, 2, 3, 1]) == 4  # Rob house 1 and 3
assert neetcode_solution([2, 7, 9, 3, 1]) == 12  # Rob house 1, rob house 3, and rob house 5
