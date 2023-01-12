"""
Generate Parentheses

Given n pairs of parentheses, write af unction to generate all combinations
of well-formed parentheses.
"""
from typing import Optional

"""
The decision to make is whether to (at the current point)
EITHER use an opening parens (if available) or use a closing parens

But we can't have more closing parens than open parens
"""


def parens(n: int) -> str:
    parens = set()

    def helper(openers: int, closers: int, built: str = ""):
        if built is None:
            built = []

        # Base Case: No more openers or closers left to use
        if not openers and not closers:
            parens.append(built)
            return

        # Recurse if you've got 'em
        if openers:
            helper(openers - 1, closers, built + "(")
        if closers:
            helper(openers, closers - 1, built + ")")

    helper(n)
    return parens


# -- Test Zone --
def test(fn):
    assert fn(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert fn(1) == ["()"]
