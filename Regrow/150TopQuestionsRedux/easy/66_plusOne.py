"""
Plus One

Given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integr.

The digits are ordered from MOST significant to LEAST significant in left-to-right order.

** The large integer doesn't contain any leading 0s. **
"""

"""
I think the idea here is to process the list from right to left, keeping track of a carry as you do so
If you have a carry at the end, then you have to prepend a 1 to your list
"""
def plus_one(digits: list[int]) -> list[int]:
    # Process the list while there's any carry to be done
    carry = 1 # Starting with a carry of 1 in the 1's digit is a way of adding one

    # For each digit, from right to left, add the carry to the digit and determine the new value of the digit and the new carry
    # Note that we could early-exit from here if we ever notice that carry is 0 on ln26 but that won't change the runtime complexity
    for idx in range(len(digits) - 1, -1, -1):
        digit_sum = digits[idx] + carry

        carry = digit_sum // 10
        digits[idx] = digit_sum % 10


    return digits if not carry else [1, *digits]





assert plus_one([1,2,3]) == [1,2,4]
assert plus_one([4,3,2,1]) == [4,3,2,2]
assert plus_one([9]) == [1,0]
