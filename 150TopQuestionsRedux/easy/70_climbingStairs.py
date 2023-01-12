"""
Climbing Stairs

You're climbing a staircase that takes n steps to reach the top

Each time, you can either climb 1 or 2 steps. IN HOW MANY DISTINCT WAYS can you climb to the top?
"""

def climb_stairs(n: int) -> int:

    def climb_stairs_helper(step: int):
        """
        Given that we're on a step, how many ways are there to get to the n'th step?
        If we're at teh n'th step, there's only one way to get to the n'th step, in the sense that we're already there
        If we're already past the nth step, there aren't any ways to get to the nth step.

        Otherwise, we can take either 1 or 2 steps from our current step'th step.

        :param step: The current step that we're on
        :return: The number of ways to get to the n'th step from the step'th step
        """
        if step == n:
            return 1
        if step > n:
            return 0

        return climb_stairs_helper(step+1) + climb_stairs_helper(step+2)

    return climb_stairs_helper(0)


assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
assert climb_stairs(4) == 5 #1111, 112, 121, 211, 22


