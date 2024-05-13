"""
Gas Station

There are `n` gas stations along a CIRCULAR ROUTE, hwere the
amount of gas at the ith station is gas[i]

You have a car with an unlimited-capacity gas tank, and
it costs cost[i] to travel FROM the ith station to the
next i+1'th station.

You begin the journey with an empty tank at
one of the gas stations.

Given two integer arrays `gas` and `cost`, return the
starting gas station's index if you cna travel around the circuit
once in the clockwise direction, otherwise return -1.

If there exists a solution, it's guarantee to be unique
"""


def can_complete_circuit_naive(gas: list[int], cost: list[int]) -> int:
    def can_complete_from(starting_idx: int, current_idx: int, remaining_gas: int, at_trip_outset: bool = False):
        # Are we at our goal?
        if not at_trip_outset and current_idx == starting_idx:
            return True

        # Fill up at current gas station
        remaining_gas += gas[current_idx]

        # Consider move to next position: Could we make it?
        gas_at_next = remaining_gas - cost[current_idx]
        if gas_at_next < 0:
            return False

        # Move to the next position (wrapping if necessary)
        return can_complete_from(starting_idx, (current_idx + 1) % len(gas), gas_at_next)

    for starting_idx in range(len(gas)):
        if can_complete_from(starting_idx, starting_idx, 0, True):
            return starting_idx
    return -1


"""
Can we do better than O(N^2)?
    - DP?
    - Way of combining gas and cost, does that help?
    
How could we do this in O(N) time?
Given the GAS and COST array, it might be useful to generate a NET array

GAS = [1, 2, 3, 4, 5]
COST= [3, 4, 5, 1, 2]       (Answer is Index 3)
________________________
NET = [-2, -2, -2, 3, 3]

From these, we know that anything with a negative number isn't going 
to work as a starting index. 

The KEY is that we KNOW that EXACTLY ONE ANSWER EXISTS!

So start with i=0: 0 + (-2) = -2 [We fail! Try again at next index with gas=0]
              i=1: 0 + (-2) = -2 [We fail! Try again at the next index with gas=0]
              i=2: 0 + (-2) = -2 [We fail! Try again at the next index with gas=0]
              i=3: 0 + (3) = 3 [Interesting, we haven't failed yet. Roll this gas into the next gas station
              i=4: 3 + (3) = 6 [Interesting, we haven't failed yet.]
              
Given that we KNOW that EXACTLY ONE of these starting indexes is going to
result in a successful circumnavigation, which one do YOU think it should be?

We only got to 6 gas in the tank by starting at i=3, so the answer is i=3
"""


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(cost) > sum(gas):
        return -1

    net = [gas[i] - cost[i] for i in range(len(gas))]

    total = 0
    starting_index = 0  # The starting position that we'll return

    for i in range(len(net)):
        total += net[i]

        if total < 0:
            # We've ran out of gas at the current starting index.
            total = 0
            starting_index = i + 1  # <-- Think about why this is this, rather than start + 1

    return starting_index



def test(fn):
    assert fn(
        gas=[1, 2, 3, 4, 5],
        cost=[3, 4, 5, 1, 2]
    ) == 3

    assert fn(
        gas=[2, 3, 4],
        cost=[3, 4, 3]
    ) == -1


test(can_complete_circuit_naive)
test(can_complete_circuit)