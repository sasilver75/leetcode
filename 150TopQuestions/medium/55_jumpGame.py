"""
Jump Game

You're given an integer array `nums` -- You're initially positioned at
the array's FIRST INDEX, and each element in the array represents your MAX
jump length at that position.

Return `true` if you can reach the LAST INDEX, or `false` otherwise.
"""

def jump_game_brute(nums: list[int]) -> bool:

    def jump_helper(idx: int) -> bool:
        """Given a current idx location, jump into all possible futures if appropriate"""
        # Are we at the end?
        if idx == len(nums) - 1:
            return True

        # Jump to all valid futures in range [1...Max]
        return any(
            jump_helper(idx + jump) for jump in range(1, nums[idx] + 1) if idx+jump < len(nums)
        )

    return jump_helper(0)



"""
Instantly I was thinking that this could be a "bottom-up 1-dimensional dynamic programming problem"
"""
def jump_game_dp(nums: list[int]) -> bool:
    dp = [False] * len(nums)
    dp[-1] = True

    # Bottom Up: Walking Backwards
    for idx in range(len(nums) - 2, -1, -1):
        # Can we Jump to a True from here?
        dp[idx] = any(
            dp[idx + jump] for jump in range(1, nums[idx]+1) if idx + jump < len(nums)
        )

    return dp[0]



# ---
def test(fn):
    assert fn([2,3,1,1,4]) == True
    assert fn([3,2,1,0,4]) == False

test(jump_game_brute)
test(jump_game_dp) # Nice! <3