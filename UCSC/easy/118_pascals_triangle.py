"""
Given an integer NUMROWS, return the first NUMROWS of Pascal's Triangle


                1
            1       1
        1       2       1
    1       3       3       1
1       4       6       4       1

"""

def generate(numRows: int) -> list[list[int]]:
    acc = [[1]]

    def _generate_pair_sums(nums: list[int]) -> list[int]:
        """
        Given a list of integers, generate a new list of integers where the elements are the pascal's triangle sum
        of the previous layer
        """
        # The second row has no "inner" elements
        if len(nums) == 1:
            return []
        
        acc = []
        for idx in range(1, len(nums)):
            acc.append(nums[idx] + nums[idx-1])
        return acc

    for rowNumber in range(1, numRows):
        inner = _generate_pair_sums(acc[rowNumber-1])
        acc.append([1, *inner, 1])
    
    print(acc)
    return acc



assert generate(5) == [
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1],
]

assert generate(1) == [[1]]