"""
Target Sum
Difficulty: Medium

You're given an integer array `nums` and an integer `target`.

You want to build an `expression` out of nums by adding one of the
symbols "+" or "-" before eachi nteger in nums, and then concatenate
all of the integers!

For example, if nums = [2,1], you can add a '+' before 2, and a '-' before
1, and concatenate them to build the express "+2-1", which equals target!

Return the number of different expressions that you can build, which evaluate
to `target`
"""

"""
Note that each number can only be used one time, but it appears
that each number needs to be used exactly once.

Let's look at a decision tree

nums = [1,1,1,1,1] ,  target = 3

Using (index, total)
                            (0, 0)
                        +1          -1
            (1,1)                       (1, -1)
        +1        -1                ...         ...
    (2,2)          (2,0)
                +1      -1
            (3,1)           ...
            +1
        (4,2)
        +
    (5,3)
    Success!
        
            
"""


def find_target_sum_ways_naive(nums: list[int], target: int) -> int:
    # Since every item needs to be used, it's just 2^N options, where each option is either + or -. Then we see
    n_ways = 0

    # Instead of keeping track of built, here, we could instead just keep track of "total",
    # and we would save ourselves some work instead of evaluating it at the end.
    def helper(idx: int, built: str) -> None:
        nonlocal n_ways
        if idx == len(nums):
            if eval(built) == target:
                n_ways += 1
            return

        helper(idx + 1, built + f"+{nums[idx]}")
        helper(idx + 1, built + f"-{nums[idx]}")

    helper(0, "")
    return n_ways

"""
How can we do better?
Can we formulate this as a dynamic programming problem?
What characterizes our status/progress?

The index that we're currently at, and the running sum where we're current at,
right?
So maybe that can't be formatted as a DP table...since the size of the
 running sum space could be quite hard to determine when determining the 
 dimensions of the table..
 
 Maybe we could just do a DP hashtable where the key is a composite of 
 (index, runningSum) : True/False ?
 
 Hm... Let's poke around and see if that makes any sense to do...
"""
def find_target_sum_ways(nums: list[int], target: int) -> int:
    dp = {} # (index, sum): number of ways

    # We want the NUMBER OF WAYS, not just whether it can be done!
    def dfs(index: int, running_sum: int) -> int:
        if index == len(nums):
            return 1 if running_sum == target else 0

        current_key = (index, running_sum) # Key describing our current position in tree
        if current_key in dp:
            return dp[current_key]

        num = nums[index]
        dp[current_key] = dfs(index+1, running_sum+num) + dfs(index+1, running_sum-num)

        return dp[current_key]

    dfs(0, 0)
    print(dp)
    return dp[(0,0)]


# --- Test ---
def test(fn):
    assert fn([1, 1, 1, 1, 1], 3) == 5  # (-1 +1 +1 +1), (+1 -1 +1 +1 +1), (+1 +1 -1 +1 +1), (+1 +1 +1 -1 +1 ), (+1 +1 +1 +1 -1)
    assert fn([1], 1) == 1 # (1)


test(find_target_sum_ways_naive)
test(find_target_sum_ways)