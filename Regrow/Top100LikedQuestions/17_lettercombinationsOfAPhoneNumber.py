"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return
 ALL POSSIBLE LETTER COMBINATIONS that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone button is given below)
Note that one does not map to any letters
"""
from typing import Optional

LOOKUP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


def letter_combinations(digits: str) -> list[str]:
    ways = []

    def dfs(idx: int, built: Optional[list[str]] = None) -> None:
        if built is None:
            built = []

        # No digits remaining; append our built option
        if idx == len(digits):
            ways.append("".join(built))
            return

        chars = LOOKUP[digits[idx]]

        for char in chars:
            # new_built = [*built, char]
            # dfs(idx + 1, new_built)
            """
            We can do the above, but with less memory, we can just append/pop
            like this, and because we're specifically doing DEPTH FIRST SEARCH, 
            """
            built.append(char)
            dfs(idx + 1, built)
            built.pop()

    if digits:
        dfs(0, None)

    ways.sort()  # Just to make it conform to answers
    print(ways)
    return ways


def test(fn):
    assert fn("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert fn("") == []
    assert fn("2") == ["a", "b", "c"]


test(letter_combinations)
