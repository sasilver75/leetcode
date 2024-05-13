"""
Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on
a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.


SAM NOTE: It seems like the "top floor" is the len(n) index -- the one just out of bounds.
"""


"""
Thinking: I think an idea is that you can 
"""

def min_cost_brute(costs: list[int]) -> int:
    ans = min(helper(costs, 0, 0), helper(costs, 1, 0))
    # print(ans)
    return ans


def helper(costs: list[int], position: int, total: int) -> int:
    if position == len(costs):
        return total

    new_total = total + costs[position]

    return min(
        helper(costs, min(position + 1, len(costs)), new_total),
        helper(costs, min(position + 2, len(costs)), new_total)
    )

assert min_cost_brute([10, 15, 20]) == 15 # Cheapest: Start of cost[1], pay the cost, go to teh top
assert min_cost_brute([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6 # Cheapest: Start on cost[0], only step on 1s, also skipping cost[3]


def min_cost_1d(costs: list[int]) -> int:
    # This is O(N) and O(N) too :)
    # Let's pretend that we're actually trying to walk down to zero, for my brain's sake
    costs = costs[::-1]
    min_costs = []
    for idx, cost in enumerate(costs):
        two_step = min_costs[idx-2] if idx-2 >= 0 else 0
        one_step = min_costs[idx-1] if idx-1 >= 0 else 0
        min_costs.append(cost + min(two_step, one_step))
        # print(f"At idx {idx}, cost is {cost}, min_costs is {min_costs}")

    print(min_costs)
    return min(min_costs[-1], min_costs[-2])

"""
We can actually get better than O(N) memory complexity too!
Sort of like climbing stairs, we only need to keep track of two numbers.
"""

assert min_cost_1d([10, 15, 20]) == 15 # Cheapest: Start of cost[1], pay the cost, go to teh top
assert min_cost_1d([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6 # Cheapest: Start on cost[0], only step on 1s, also skipping cost[3]


"""
    Can we do this in a top-down dynamic option?

    Notice: From every spot, we have two decisions -- take one, or take two steps.
    We like to do decision tree to think about the problem
    
idxs:    0      1       2         3
        [10,    15,     20,     _Top_]
        
                        
index                  0
cost            $10         $10
            1                       2
        $15   $15                   $20
        2       3[$25]               3[$30]
        $20
        3[$45]
Okay, so we reached the end... what was the minimum cost to reach the position?
The cheapest was 0->1->3 @ $25

But wait, we saw in the example solution that the actual answer was $15!
that's because we have the option to either start at index 0 or index 1, and we just did 
a decision tree for index 1. Do we have to draw another decision tree starting at index 1?

Well... Look at our picture above. that second tree is actually the subtree starting 
at 1, in the left subtree.

        1
    $15     $15
    2       3 [$15]
    $20
    3[$35]
    
If we take the decision tree approach... the max height of the tree would be O(N)
if we always take length-1 steps. We can have two branches for every single node,
so it comes to 2^N.

But we can actually get this down to O(N)!

To solve the original problem... if we cache the repeated work with a hashmap,
we don't need to repeat the same problem multiple times :) 
If we cache "How much does it cost to get to TOP from 2 (example)", then we don't have
to re-solve the problem!

The solution is O(N) because we have N subproblems (from index 0, how much does it take... from index 1, how much does it take..., etc)
It will also be O(N) memory complexity. 
We can either do this recursively or iteratively.
"""


"""
We can actually get better than O(N) memory complexity too!
Sort of like climbing stairs, we only need to keep track of two numbers.
"""



"""
                    
    10      15      20      0

"""
def min_cost(costs: list[int]) -> int:
    # Moving from right to left... we only have to
    if not costs:
        return 0
    if len(costs) == 1:
        return costs[0]

    two_ago = 0
    one_ago = costs[-1]
    for i in range(len(costs) - 2, -1, -1):
        min_cost_candidate = costs[i] + min(two_ago, one_ago)
        two_ago = one_ago
        one_ago = min_cost_candidate

    return min(one_ago, two_ago)





assert min_cost([10, 15, 20]) == 15 # Cheapest: Start of cost[1], pay the cost, go to teh top
assert min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6 # Cheapest: Start on cost[0], only step on 1s, also skipping cost[3]


def neetcode_solution(costs: list[int]) -> int:
    # Apparently we're guaranteed that we're going to have at least two values in the costs array.
    costs.append(0)
    for i in range(len(costs)-3, -1, -1):
        costs[i] += min(costs[i + 1], costs[i+ 2])
    return min(costs[0], costs[1])