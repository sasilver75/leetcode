"""
Given an integer array "nums", move all the "0"s to the end of it, while
MAINTAINING the relative order of the non-zero elements

Note: Do this IN-PLACE ... WITHOUT making a copy of the array
"""

""" 
             s      f
       1  3  12  0  0     

"""

"""
Thinking:
Here's an O(N^2) Option that works...
For every element... While it's a 0, scan forward and swap it with the first non-zero element you find
"""

def move_zeroes(nums: list[int]) -> list[int]:
    # O(N^2)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp # Could break after this if you wanted
    return nums


"""
Is there any way to do it faster than O(N^2)?
What information would we have to keep track of to do it in O(N)?
"""
def move_zeroes_linear_but_not_in_place(nums: list[int]) -> list[int]:
    zeroes = [num for num in nums if num == 0]
    non_zeroes = [num for num in nums if num != 0]
    return [*non_zeroes, *zeroes]

"""
Recall: We must "do this in-place without making a copy of the array"

We need to preserve the order of the array.

        0   1   0   2   0   3   0


                s
        1   2   3   0   0   0   0
                                f
                                
The idea is that f moves with every tick of the clock
And everything behind s shouldn't have any zeroes

Fast moves forward every Tick
Slow moves forward once only when nums[s] != 0
    * Slow COULD move forward until the next zero, I think, using a while loop
    * But then you'd have to check whether SLOW moved off the edge of the array at the beginning
    of each for loop, and return nums if true
    -> By having slow only increment by at most 1 each tick, we guarantee that slow <= fast,
    so we don't have to worry about any runoff.
"""
def move_zeroes_linear(nums: list[int]) -> list[int]:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            temp = nums[slow]
            nums[slow] = nums[fast]
            nums[fast] = temp

        if nums[slow] != 0:
            slow += 1

    return nums


assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
assert move_zeroes_linear([0,1,0,3,12]) == [1,3,12,0,0]
assert move_zeroes_linear([8,0,0,1,4,3,0,6,1]) == [8,1,4,3,6,1,0,0,0]
assert move_zeroes_linear([0,0,0,0,0,1,0,0,0]) == [1,0,0,0,0,0,0,0,0]
assert move_zeroes_linear([3,1,0,0,3,2,0,0,1]) == [3,1,3,2,1,0,0,0,0]

# assert move_zeroes([0]) == [0]
assert move_zeroes_linear([0]) == [0]