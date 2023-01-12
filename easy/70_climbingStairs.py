"""
You are climbing a staircase
It takes n steps to reach the top
Each time, you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?
"""

def count_steps(remaining_steps: int):
    # Base Cases: If you're there, or 1 step away, there's only one thing you can do (either nothing or 1 step)
    if remaining_steps <= 1:
        return 1

    # Otherwise, you can either take 1 or 2 steps. Each have their own unique recursion trees below -- add the results!
    return count_steps(remaining_steps-2) + count_steps(remaining_steps-1)



assert count_steps(2) == 2
assert count_steps(3) == 3
