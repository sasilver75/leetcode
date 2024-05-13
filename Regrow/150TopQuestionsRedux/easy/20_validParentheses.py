"""
20. Valid Parentheses
"""

"""
The idea is that you maintain a stack datastructure
When you encounter an opening parens, you add it to the stack
When you encounter a closing parens, it needs to "match" the opening parens on the top of the stack
    - If it doesn't, or if there isn't ANY element on the top of the stack, return false.
At the end, return False if there are still elements remaining in the stack, representing unlcosed parentheses.
    
"""
def is_valid(s: str) -> bool:
    # Assuming a string containing only "{[(" and "}])"
    p_stack = []
    matcher = { # Given a closing character, what's the matching open character?
        "}": "{",
        ")": "(",
        "]": "["
    }

    for char in s:
        if char in "([{":
            p_stack.append(char)
        else:
            # Assuming that any non-opening characters are closing characters
            if not p_stack or matcher[char] != p_stack.pop():
                return False
            # p_stack matched and has been popped; continue

    return len(p_stack) == 0


assert is_valid("()") == True
assert is_valid("()[]{}") == True
assert is_valid("(]") == False