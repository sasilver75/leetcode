from typing import Optional, Callable


# Using two pointers to walk across the array
# For each element, compare with every following element, see if it adds to sum
# O(N^2) time with O(1) memory
def two_sum_attempt_one(nums: list[int], target: int) -> Optional[list[int, int]]:
    i = 0
    while i < len(nums):
        ival = nums[i]
        j = i + 1
        while j < len(nums):
            jval = nums[j]
            if ival + jval == target:
                return [i, j]
            j += 1
        i += 1

# Pass through the array, storing the complement
# O(N) with O(N) memory
def two_sum_attempt_two(nums: list[int], target: int) -> Optional[list[int, int]]:
    complements = {}
    for idx, val in enumerate(nums):
        comp = target - val
        # Check: Is there an existing complement? If so, return
        if comp in complements:
            return [complements[comp], idx]

        # Check: If val not in complements, add it
        if val not in complements:
            complements[val] = idx






def test(fn: Callable):
    cases = [
        ([[2,7,11,15], 9], [0,1]),
        ([[3,2,4], 6], [1,2]),
        ([[3,3], 6], [0,1]),
        ([[2,7,9,11,14], 18],[1,3]),
        ([[2,7,9,11,14], 19],None),
    ]
    for inputs, soln in cases:
        answer = fn(*inputs)
        print(f"""
Inputs: {inputs}
Answer is: {answer}
Soln is: {soln}
Correct?: {answer == soln}
""")

    assert fn([2,7,11,15], 9) == [0,1]
    assert fn([3, 2, 4], 6) == [1, 2]
    assert fn([3, 3], 6) == [0, 1]

test(two_sum_attempt_one)
print("###")
test(two_sum_attempt_two)