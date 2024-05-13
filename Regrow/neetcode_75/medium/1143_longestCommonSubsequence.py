"""
Longest Common Subsequence
Category: DP

Given two strings `text1` and `text2`, return the LENGTH of their
longest common subsequence! If there is no common subsequence, return 0!

Note: Subsequences preserve order but not necessarily contiguous numbers

"""
from typing import Optional


def longest_common_subsequence_naive(text1: str, text2: str) -> int:
    def populate_subsequences(source_str: str, subsequences: set, idx: int = 0, built: str = "") -> set:
        if subsequences is None:
            subsequences = set()
        if idx >= len(source_str):
            subsequences.add(built)
            return

        # Either include or don't include char @ idx in source_str in the built subsequence string
        populate_subsequences(source_str, subsequences, idx + 1, built + source_str[idx])
        populate_subsequences(source_str, subsequences, idx + 1, built)

    # Generate all subsequences for text1 and store in set
    text1_subsequences = set()
    populate_subsequences(text1, text1_subsequences)

    # Generate all subsequences for text2, seeing if they exist in set and updating max_length
    text2_subsequences = set()
    populate_subsequences(text2, text2_subsequences)

    common_subsequences = text1_subsequences.intersection(text2_subsequences)
    return max(
        [len(cs) for cs in common_subsequences]
    )


"""
Insight: This is a 2-dimesnional dynamic programming problem!

Assume we had "abcd" and "afcegq"
If we just considered the first characters, they're the same, cool!
That is, LCS("abcd", "afcegq") == 1 + LCS("bcd", "fcegq") -- that's a subproblem!

But what about LCS("bcd", "fcegq")?
It could be the case that the first three characters of tex1 match with teh last 3 
characters of text1, or with the odd characters, or... We really don't have any way of 
knowing how to proceed, but we know that: 

Because "b" != "f", LCS("bcd", "fcegq") = MAX( LCS("cd", "fcegq"), LCS("bcd", "cegq") )

If we envision this as a 2D grid:

    f   c   e   g   q
b   _   _   _   _   _
c   _   _   _   _   _
d   _   _   _   _   _

Where [0,0] represents (char@idx0 in text1, char@idx0 in text2)
Let's call that [row, col]
So when text1[row] == text2[col]:
    grid[row][col] = 1 + helper(row+1, col+1)
    
When text1[row] != text2[col]:
    grid[row][col] = Max( helper(row+1, col), helper(row, col+1) )

And whenever we call helper on a row/col that's "out of bounds", meaning 
>= len(text1) or >= len(text2), then we simply return 0, since there isn't 
anything common between "xxx" and "" :)
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    grid = [
        [0 for col in range(len(text2))]
        for row in range(len(text1))
    ]

    maximum_length = 0

    def helper(row: int, col: int) -> int:
        """
        When called on a (possibly invalid) row/col in grid, attempts to populate
        the cell at grid[row][col] using the strategy described above the encolosing
        function's definition.

        Returns the value of the cell that was populated
        """
        nonlocal maximum_length
        if row >= len(text1) or col >= len(text2):
            return 0

        if text1[row] == text2[col]:
            grid[row][col] = 1 + helper(row + 1, col + 1)
            maximum_length = max(maximum_length, grid[row][col])
            return grid[row][col]
        else:
            grid[row][col] = max(
                helper(row, col + 1),
                helper(row + 1, col)
            )
            maximum_length = max(maximum_length, grid[row][col])
            return grid[row][col]

    helper(0, 0)
    return maximum_length  # It seems we can actually just return grid[0][0]


# -- Test --
def test(fn):
    assert fn("abcde", "ace") == 3  # ace
    assert fn("abc", "abc") == 3  # abc
    assert fn("abc", "def") == 0  # none
    assert fn("awrehr", "aefhhgggr") == 4
    assert fn("awefg", "rrrrrrg") == 1


test(longest_common_subsequence_naive)
test(longest_common_subsequence)
