"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def valid_parens(parens: str) -> bool:
    """
    The way that we do this is use a stack
    """
    stack = [] # append and pop
    closers = {")", "}", "]"}
    matchers = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    for paren in parens:
        if paren in closers:
            # We have a closer, it must close a valid parens
            try:
                if stack[-1] != matchers[paren]:
                    return False
            except IndexError:
                return False
            stack.pop()
        else:
            # We have an opener, append it
            stack.append(paren)
    
    # After iteration, any parens left in the stack? Then the parens were unbalanced!
    if stack:
        return False








