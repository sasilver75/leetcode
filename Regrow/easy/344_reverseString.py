"""
Write a function that reverses a string.
The input string is give as an array of characters s

You must do this by modifying the input array in-place with O(1) extra memory
"""

def reverse_string(s: list[str]):
    l = 0
    r = len(s) - 1
    while l < r:
        # Swap
        tmp = s[l]
        s[l] = s[r]
        s[r] = tmp

        # Move pointers closer to center
        l += 1
        r -= 1
    return s

assert reverse_string([char for char in "hello"]) == [char for char in "olleh"]
assert reverse_string([char for char in "Hannah"]) == [char for char in "hannaH"]