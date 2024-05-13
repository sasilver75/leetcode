"""
Valid Parentheses
Category: String

Given a string `s` containing just the characters
(, ), {, }, [, ]  ... determine if the input string is valid.

An input string is valid if:
    * Open brackets must be closed by the same type of brackets
    * Open brackets must be closed in the correct order
    * Ever close bracket has a corresponding open bracket of the same type

"""

def is_valid(s: str) -> bool:
    parens = [] # Stack

    openers = {"(", "[", "{"}
    # Closer to Opener
    lookup = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for char in s:
        if char in openers:
            # Opener
            parens.append(char)
        else:
            # Closer
            if not parens or lookup[char] != parens[-1]:
                return False
            parens.pop()
    
    return not bool(parens)






def test(fn):
    assert fn("()") == True
    assert fn("()[]{}") == True
    assert fn("(]") == False
    assert fn("({}[{[]}()])") == True
    assert fn("({}[{[]}()]()") == False # One left Open

test(is_valid)