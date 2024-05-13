"""
Jump Game
Category: DP

You are given an integer array `nums`.
You're initially positioned at teh array's FIRST INDEX, and each element in
the array represents the MAXIMUM jump length at that position!

Return TRUE if you can reach the last index, or FALSE otherwise.
"""

"""
Note: It seems that "to the end" means to the len(nums) index -- i.e. just "off" the end of the list!
"""
def jump_game_naive(nums: list[int]) -> int:

    def helper(idx: int) -> bool:
        if idx > len(nums):
            return False
        if idx == len(nums):
            return True

        # Of all the jumps you can take, do any result in eventually getting to the end?
        # nums[idx] = 6 means you can just 1,2,3,4,5, or 6 spaces from the current idx
        return any(
            helper(idx + jump_option)
            for jump_option in range(1, nums[idx]+1)
        )


    return helper(0)


"""
How can we do better?

If we're at idx=4, trying to figure out the answer to 
jump_game(nums, idx=4) ... Wouldn't it be helpful to know the answer to 
jump_game(nums, idx=5)? Or jump_game(nums, idx=6)? I think so! 

I think this is a one-dimensional bottom-up Dynamic Programming problem
where dp[i] is whether we can make it to the end (idx len(nums)) from index i
"""
def jump_game(nums: list[int]) -> int:
    dp = [False] * (len(nums)+1)
    dp[-1] = True

    # From the back, starting at the dp[-2] index
    for idx in range(len(dp) - 2, -1, -1):
        # Stick this into a future variable in case it's empty (say num[x] = 0), so we don't do max({empty})
        futures = [
            dp[idx + step_option]
            for step_option in range(1, nums[idx] + 1)  # nums[x] = 3 means you can take any of 1,2,3 steps
            if idx + step_option < len(dp)
        ]
        dp[idx] = any(
            futures
        ) if futures else False

    return dp[0]


# -- Test Zone --
def test(fn):
    assert fn([2, 3, 1, 1, 4]) == True
    assert fn([3, 2, 1, 0, 4]) == False

# test(jump_game_naive)
test(jump_game)