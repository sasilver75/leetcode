"""
Jump Game II

Given a zero-indexed array of integers `nums` of length `n`
You are initially positioned at `nums[0]`

Each element `nums[i]` represents the MAXIMUM length of a forward jump
from index i. In other words, if you are at nums[i], you can jump
to any nums[i+j] where:

    * 0 <= j <= nums[i]
    * i + j < n

Return the MINIMUM NUMBER OF JUMPS to reach nums[n-1] (the last index)

Assume that you CAN reach nums[n-1] using the available jumps
"""

def jump_game_naive(nums: list[int]) -> int:
    min_steps = float('inf')
    def dfs(idx: int, steps: int) -> None:
        nonlocal min_steps
        if idx == len(nums) - 1:
            min_steps = min(min_steps, steps)

        # Take only valid steps
        val = nums[idx]
        for step in range(1, val+1):
            # If it would be a valid step
            if idx + step < len(nums):
                dfs(idx+step, steps+1)

    dfs(0,0)
    return min_steps


"""
Okay, can we do any better?
DP
"""
def jump_game(nums: list[int]) -> int:
    dp = [float('inf')] * len(nums)
    dp[-1] = 0
    for idx in range(len(dp) - 2, -1, -1):
        steps = nums[idx]
        for step in range(1, steps+1):
            if idx + step < len(nums):
                dp[idx] = min(dp[idx], 1 + dp[idx+step])

    print(dp)
    return dp[0]



def test(fn):
    assert fn([2, 3, 1, 1, 4]) == 2
    assert fn([2, 3, 0, 1, 4]) == 2

test(jump_game_naive)
test(jump_game)