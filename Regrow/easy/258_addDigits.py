"""
Given an integer num, repeatedly add all its digits until the result
has only one digit, and return it.
"""

def add_digits(num: int) -> int:
    str_num = str(num)
    if len(str_num) == 1:
        return num

    sum = 0
    for num_char in str_num:
        sum += int(num_char)

    return add_digits(sum)



# Case 1
assert add_digits(38) == 2

# Case 2
assert add_digits(0) == 0