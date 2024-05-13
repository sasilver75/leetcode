"""
Gas Station

There are `n` gas stations along a CIRCULAR ROUTE, where
the amount of gas at the ith station is `gas[i]`.

You have a car with an UNLIMITED GAS TANK, and it costs
`cost[i]` of gas to travel from the `ith` station to the next
`i+1`th station. You begin the journey with an empty tank
at ONE of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's
index if you can travel around the circuit once in the clockwise direction,
otherwise return -1.

If there exists a solution, it is guaranteed to be unique.
"""

"""
Thinking:

I think this should be pretty straightforward to do in O(N^2) time.
"""

def can_complete_circuit(gas: list[int], cost:list[int]) -> int:
    for starting_idx in range(0, len(gas)):
        tank = 0
        current_idx = starting_idx
        # While we aren't at the destination and we still have gas in the tank
        while current_idx - len(gas) != starting_idx and tank >= 0:
            # Fill Up at current_idx
            tank += gas[current_idx % len(gas)]
            # Spend the gas to get to current_idx+1
            tank -= cost[current_idx % len(gas)]

            current_idx += 1

        if current_idx - len(gas) == starting_idx and tank >= 0:
            return starting_idx

    return -1

"""
How can we do better than O(N^2)?

Neetcode:
We want to return the index that we can start at... such that we can travel around the entire circuit...
in the clockwise direction... without running out of gas.

If that's not possible for any starting index... then we return -1.
If there DOES exist a solution, we're guaranteed that it's unique.

Given the GAS and COSTS arrays:
GAS:    [1, 2,  3,  4,  5]
COSTS:  [3, 4,  5,  1,  2]
It might be useful to generate a NET array:
NET:    [-2, -2, -2, 3, 3]

We know off the bat that starting positions with negative number aren't
going to work.
"""

def can_complete_circuit_smarter(gas: list[int], costs: list[int]) -> int:
    net = [g - c for g, c in zip(gas, costs)]

    # For each starting index
    for starting_idx in range(len(net)):
        tank = 0
        current_idx = starting_idx
        # While we haven't reached our destination and while we still have gas: Drive
        while current_idx != starting_idx + len(net) and tank >= 0:
            # Consume current (Gas - Cost)
            tank += net[current_idx % len(net)]
            current_idx += 1
        # Did we reach our goal with at least 0 gas?
        if current_idx == starting_idx + len(net) and tank >= 0:
            return starting_idx

    # We didn't reach our goal :(
    return -1

"""
One interesting thing to note is that the SUM(gas) >= SUM(cost) array
to be able to complete a loop from somewhere. "How can we complete a loop 
if we don't have enough gas to cover the total cost?"

We're going to keep track of a total and a start position.

diff = [-2, -2, -2, 3, 3]

Let's consider starting at the 0th index
Total = Total + (diff[i]) = -2
If the total ever becomes negative, meaning less than zero, we ran
out of gas. That means this start position didn't work.
Let's move our starting index forward and reset our total to 0.

(the same thing will happen for indices 1 and 2)
For index 3.
Our total is 0+3 = 3!
Moving forward, our index is now 4.
Total += 3 = 6
Notice that we hve no more elements left if our input array.
What does that tell us? Do we need to go back to the start and 
restart our loop from the beginning? No!
Why?
We verified that the sum of gas is greater than or equal to the sum of cost.
So we guaranteed that there exists a solution... and we know that index=4 was
the one that allowed us to reach the end... And since we know that we have
enough gas to complete a loop starting SOMEWHERE, it HAS to be this position.
Because there's only one unique solution, and we know that starting at index 3
will give us more gas in the tank (going into the negative section) than starting
at index 4.

So this takes O(N) time.
"""

def can_complete_circuit_smartest(gas: list[int], costs: list[int]) -> int:
    if sum(costs) > sum(gas):
        return -1

    # We now know that a (exactly 1) solution exists
    total = 0
    start = 0 # Starting position that we'll return

    for i in range(0, len(gas)):
        net = gas[i] - costs[i]
        total += net

        if total < 0:
            # This position doesn't work. Start the next position.
            total = 0
            start = i + 1

    # Return the starting position for which the total never dipped below zero after we got to that starting position
    # the main thing about this problem is identifying that it's greedy.
    return start




# -- Test Zone --
def test(fn):
    assert fn([1,2,3,4,5], [3,4,5,1,2]) == 3
    """
    Starting at station 3 (index 3), you can fill up with 4 units 
    of gas. 
    You then travel to station 4, which costs cost[3] = 4. You fill up 5
    at station 4, tank is now 4 - 1 + 5 = 8
    You then travel to station 0. tank = 8 - 2 + 1 = 7
    You travel to station 1. tank = 7 - 3 + 2 = 6
    You travel to station 2. tank = 6 - 4 + 3 = 5
    You travel to station 3. The cost was 5. Your gas is just enough 
    to travel back to station 3!
    """
    assert fn([2,3,4], [3,4,3]) == -1
    """
    You can't start at station 0 or 1, as there isn't enough gas to travel to
    the next station.
    Starting at station 2, we fill up with 4 gas. Tank = 4
    Travel to station 0, tank = 4 - 3 + 2 = 3
    Travel to station 1, tank = 3 - 3 + 3 = 3
    You cannot travel back to station 2, as it requires 4 units of gas, and 
    we only have 3.
    Therefore, you can't travel around the circuit once no matter WHERE you start!
    """

test(can_complete_circuit)
test(can_complete_circuit_smarter)
test(can_complete_circuit_smartest)