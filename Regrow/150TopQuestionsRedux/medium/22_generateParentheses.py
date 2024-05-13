"""
Generate Parentheses

Given n pairs of parentheses, write af unction to generate all combinations
of WELL-FORMED parentheses.
"""


def generate_parens_naive(n: int) -> list[str]:
    # 1) Generate all possible parentheses strings
    parens_strings = []

    def recursive_helper(opens: int, closes: int, built: str):
        # Base Case/Exit Condition:
        if opens == 0 and closes == 0:
            parens_strings.append(built)
            return

        if opens > 0:
            recursive_helper(opens - 1, closes, built + "(")
        if closes > 0:
            recursive_helper(opens, closes - 1, built + ")")

    recursive_helper(n, n, "")

    # 2) Filter parentheses strings to well-formed parentheses
    def is_well_formed(ps: str) -> int:
        parens_stack = []  # Does this have to be a list?

        for char in ps:
            if char == "(":
                parens_stack.append(char)
            else:
                # Check for inappropriate closing (no matching open)
                if not parens_stack or parens_stack.pop() != "(":
                    return False

        # Check that all opening parens are closed
        return len(parens_stack) == 0

    well_formed_parens_strings = [
        ps for ps in parens_strings
        if is_well_formed(ps)
    ]

    return well_formed_parens_strings

"""
Is there a way that we can be more intelligent?
In the previous example we generated all possible parentheses, and then
filtered them down to the valid ones.
Is there a way that we could just generate the valid parentheses de novo?

Are there rules for when we would append a closing parentheses?
Let's look at some valid ones
(())
()()
((()()))
We definitely only have the option of appending a closing a parentheses when
the number of opening parentheses so far used is greater than the number of 
closed parentheses used so far.
Rephrased: Only when we have more right-parens "remaining" than left-parens.

This makes sense considering our failure conditions that we used in the 
previous naive solution -- when would we "fail", in our assessment of whether
a parens was valid? When there wasn't a matching opening parentheses available --
which in the case of "just ( parentheses", equates to the relation above.
"""
def generate_parens(n: int) -> list[str]:
    accumulator = []
    def recursive_helper(openers_remaining: int, closers_remaining: int, built: str):
        if openers_remaining == 0 and closers_remaining == 0:
            accumulator.append(built)
            return

        # 1) Can we use an opening parens?
        if openers_remaining > 0:
            recursive_helper(openers_remaining-1, closers_remaining, built+"(")

        # 2) Can we use a closing parens?
        if closers_remaining > openers_remaining:
            recursive_helper(openers_remaining, closers_remaining-1, built+")")

    recursive_helper(n, n, "")

    return accumulator

# -- Test --
def test(fn):
    ans1 = fn(3)
    assert all(p in ans1 for p in ["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert fn(1) == ["()"]


test(generate_parens_naive)
test(generate_parens)
