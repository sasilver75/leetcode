"""
You are given a large integer represented as an integer array DIGITS
where each digits[i] is the ith digit of the integer
The integers are ordered from most significant to least significant,
in left to right order.
The larger integer does not contain any leading 0s.

Increment the large integer by one and then return the resulting array of digits.

[1,2,3] -> [1,2,4]
[4,3,2,1] -> [4,3,2,2]
[9] -> [1,0]  ***
"""



def plus_one(arr: list) -> list:
    arr[-1] += 1
    return correct_int_array(arr)


def correct_int_array(arr: list) -> list:
    # Given an int array, scan for an offending digit (>= 10)
    offending_index = -1
    for idx, val in enumerate(arr):
        if val >= 10:
            offending_index = idx

    # No offending digits found
    if offending_index < 0:
        return arr
    # Leftmost digit is offending. Append the digit list onto a new leftmost digit @ 1
    elif offending_index == 0:
        arr[offending_index] = 0
        return [1, *arr]
    # Some other digit is offending. "exchange up" the
    else:
        arr[offending_index - 1] += 1
        arr[offending_index] = arr[offending_index] - 10
        return correct_int_array(arr)




assert plus_one([1,2,3]) == [1,2,4]
assert plus_one([4,3,2,1]) == [4,3,2,2]
assert plus_one([9]) == [1,0]
assert plus_one([8,9,9,9]) == [9,0,0,0]
assert plus_one([9,0,9,9]) == [9,1,0,0]
assert plus_one([9,9,9]) == [1,0,0,0]