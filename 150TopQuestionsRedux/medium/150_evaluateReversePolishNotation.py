import operator as op
"""
Evaluate Reverse Polish Notation

You're given an array of strings `tokens` that represents an arithmetic
expression in REVERSE POLISH NOTATION!

Evaluate the expression and return the integer that represents the value of
the expression.

Note that:
- The valid operators are +, -, *, /
- Each operand may be an integer or another expression
- The division between two integers always truncates towards zero
- There will not be any division by zero
- The input represent a valid mathematical expression in reverse polish notation
- The answer and all the intermediate calculations can be represented in a 32-bit integer

"""
from numbers import Number

"""
Let's evaluate some of these by hand and see how we might group and execute
operators and operands.

Here's what I'm thinking is true of both of the examples
    assert fn(["2", "1", "+", "3", "*"]) == 9  # ((2 + 1) * 3) = 9
    assert fn(["4", "13", "5", "/", "+"]) == 6  # (4 + (13 / 5)) = 6

I think it's true for each of them that operators are executed with the 
preceding two operands.
In the first example, it's not like we do the multiplication first -- 
we have to evaluate the 2+1 before we have an operand to apply with the * one

Is this always the case, that we execute these operators left to right?



" If there are multiple operations, operators are given immediately after their final operands (often an operator takes two operands, in which case the operator is written after the second operand); so the expression written 3 − 4 + 5 in conventional notation would be written 3 4 − 5 + in reverse Polish notation: 4 is first subtracted from 3, then 5 is added to it."
"The concept of a stack, a last-in/first-out construct, is integral to these actions"

So there's two options that I can think of if this works how I think it works

And they both involve scalling left to right for an operator, and then applying 
it to the two previous operands.

The trick/question is how to performantly find the two previous operands, and then
"replace" those operands with the result of (operator @ operands) -- lists for instance
aren't performant, if we spliced/replaced the result back into the list.

One option is to use a DoublyLinkedList, and the other is to use a Stack
"""

def apply(operator: str, operands: list[int]) -> int:
    lookup = {
        "+": op.add,
        "-": op.sub,
        "/": op.truediv,
        "*": op.mul
    }
    ans = int(lookup[operator](*operands))
    return ans

def evaluate_rpn_stack(tokens: list[str]) -> int:
    operators = set(["+", "-", "/", "*"])
    stack: list[str] = []

    for token in tokens:
        if token in operators:
            operands = [int(stack.pop()), int(stack.pop())][::-1] # Str -> Int and reversing so that 13 5 / is 13/5 not 5/13
            res = apply(token, operands)
            stack.append(str(res)) # Recall that the stack is strings
        else:
            stack.append(token)

    return res


# ------

class Node:
    def __init__(self, value: str):
        self.value = value
        self.prev = None
        self.next = None

    def insert(self, value: str) -> None:
        new_node = Node(value)
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def as_list(self):
        acc = []
        cur = self.head
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc[1:-1]




"""
Now let's do it in a much more cumbersome way!
"""
def evaluate_rpn_dll(tokens: list[str]) -> int:
    if not tokens:
        return 0

    operators = ["+", "-", "/", "*"]

    # Step 1: Generate DLL from Tokens with dummy head/tail
    head = Node(None)
    tail = Node(None)
    head.next = tail
    tail.prev = head
    for i in range(0, len(tokens)):
        token = tokens[i]
        new_node = Node(token)
        new_node.prev = tail.prev
        tail.prev.next = new_node
        tail.prev = new_node
        new_node.next = tail

    # Step 2: Iterate while looking for operators, then combine two previous operands with operator
    cur = head
    while cur:
        if cur.value in operators:
            # Seek back for nearest two operands
            first = cur
            while first.value in operators: # Step back to the first number
                first = first.prev
            second = first.prev
            while second.value in operators: # Step back to the second number
                second = second.prev

            # Evaluate
            ans = apply(cur.value, [second.value, first.value]) # Order matters for division. (5, 13, /) -> 5/13, not 13/5
            cur.value = str(ans)

            # Stitch up DLL
            cur.prev = second.prev
            second.prev.next = cur

            print("Stitched")
        cur = cur.next

    return int(head.next.value)


def test(fn):
    assert fn(["2", "1", "+", "3", "*"]) == 9  # ((2 + 1) * 3) = 9
    assert fn(["4", "13", "5", "/", "+"]) == 6  # (4 + (13 / 5)) = 6

test(evaluate_rpn_stack)
# test(evaluate_rpn_dll)
