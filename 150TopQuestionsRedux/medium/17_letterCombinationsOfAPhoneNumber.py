"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent
Return the answer in any order.

A mapping of digits to letters will be provided
"""

"""
Okay, so you'd just use any tree-traversal method here, where at any recursive step you're keeping track of a built string and an index in the digits list.
"""
def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

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
    combinations = []

    def recursive_helper(idx: int, built: str):
        if idx == len(digits):
            combinations.append(built)
            return

        digit = digits[idx]
        characters = LOOKUP[digit]
        for char in characters:
            # DFS into character
            recursive_helper(idx+1, built+char)

    recursive_helper(0, "")
    print(f"{combinations = }")
    return combinations


def test(fn):
    ans1 = fn("23")
    assert all(ans in ans1 for ans in ["ad","ae","af","bd","be","bf","cd","ce","cf"])

    assert fn("") == []

    ans3 = fn("2")
    assert all(ans in ans3 for ans in ["a", "b", "c"])

test(letter_combinations)
