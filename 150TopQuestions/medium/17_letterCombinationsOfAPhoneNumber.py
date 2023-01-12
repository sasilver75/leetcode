"""
Letter Combinations of a Phone Number

Given a string containing digits from [2, 9] inclusive, return all
possible letter combinations that the number could represent!
Return the answer in any order.

A Mapping of digits to letters is provided.
"""
from typing import Callable

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
    # This runs in 4^N time
    acc = []
    def helper(idx: int, built: str) -> None:
        # Base Case: We've exhausted `digits` -- Save the built string
        if idx == len(digits):
            acc.append(built)
            return

        # Recursive: Recurse into digit options
        for char in LOOKUP[digits[idx]]:
            helper(idx+1, built+char)

    helper(0, "")
    return acc

"""
Can we do any better than the 4^N Option above? Eh!
"""

# -- Test Zone --
def test(fn: Callable):
    assert fn("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert fn("") == []
    assert fn("2") == ["a", "b", "c"]
