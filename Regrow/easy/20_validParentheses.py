"""
Given a string s containing just the characters (){}[], determine if the
input string is valid.

Input strings are valid if:
1) Open brackets are always closed by the SAME type of brackets
2) Open brackets must be closed in the correct order
3) Every close bracket has a corresponding open bracket of the same type
"""
import math


def is_balanced_parens(parens: str) -> bool:
    # "[([{}{}])]"
    complement = {
        '{': '}',
        '(': ')',
        '[': ']',
    }
    stack = []
    if len(parens) % 2 != 0: # Balanced parens strings are always even length
        return False
    for char in parens:
        if char in complement:
            # Opening parens -- add em!
            stack.append(char)
        else:
            # Closing parens -- does the top of the stack match?
            if stack and complement.get(stack[-1]) == char:
                stack.pop()
    return not bool(stack)



def test(fn):
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", True),
        ("[([{}{}])]", True),
        ("[{()]}", False),
    ]

    for inp, soln in cases:
        ans = fn(inp)
        print(f"Input: {inp}")
        print(f"ans: {ans}")
        print(f"correct: {ans == soln} \n")

test(is_balanced_parens)