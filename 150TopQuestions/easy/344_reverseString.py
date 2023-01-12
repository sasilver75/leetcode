"""
Reverse String

Write a function that reverses a string. The input string is given as an array of characters s

You must do this by modifying the input array IN PLACE with O(1) extra memory
"""

def reverse(chars: list[str]) -> list[str]:
    """
    Insight: Use two pointers that walk towards eachother, swapping values
    """

    l, r = 0, len(chars) - 1
    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1
    print(chars)
    return chars



assert reverse([char for char in "hello"]) == [char for char in "olleh"]
assert reverse([char for char in "Hannah"]) == [char for char in "hannaH"]

