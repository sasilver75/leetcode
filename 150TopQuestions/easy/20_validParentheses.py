"""
Valid Parentheses

Given a string s containing just the characters
( ) { } [ ]
determine whether the input string is valid

A valid input string in this context is one where:
1) Open Brackets must be closed by the same type of brackets
2) Open Brackets must be closed in the correct order
3) Every close bracket has a corresponding open bracket of the same type
"""

def is_valid_parens(s: str) -> bool:
    stack = []
    lookup = { # "char in lookup" == "char is a closer"
        "}": "{",
        "]": "[",
        ")": "("
    }
    for char in s:
        if char in lookup: # Is a closer
            if not stack or lookup[char] != stack[-1]: # If no matching opener on top of stack
                return False
            stack.pop()
        else:
            stack.append(char)

    return False if stack else True


assert is_valid_parens("()")
assert is_valid_parens("()[]{}")
assert not is_valid_parens("(]")