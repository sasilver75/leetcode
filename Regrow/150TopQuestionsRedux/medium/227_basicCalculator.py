import operator as op
"""
Basic Calculator

Given a string s which represents an expression, evaluate this expression
and return its value.

The integer division should truncate towards zero

You can assume that the given expression is always going to be valid
All intermediate results will be in range -2^-31, 2^31-1

Note: You're not allowed to use any built-in function which evaluates strings as
mathematical epxressions, like eval.
"""
import string

"""
Thinking:
My idea for how to do this one is very similar to the idea of the 
doubly linked list from ReversePolishNotation (RPN)

Turn 3 + 2 * 2 into

(3) -> (+) -> (2) -> (*) -> (2) -> 

And to do two passes through it, each looking for (*/) and (+-), which each
are sets of equally-precedent operators.

When we find a * operator, we find the nearest operands on the left/right side 
of it, and combine them

So <-> (2) <-> (*) <-> (2) <-> needs to become <-> (4) <->
    - This involves both combining the values of the operators/operands into one node
    - Doing the stitching/removing of nodes
"""

class DLLNode:
    def __init__(self, value: str):
        self.value = value
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = DLLNode(None)
        self.tail = DLLNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node: DLLNode):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node


def evaluate(operator: str, operandA: str, operandB: str):
    operator_lookup = {k:v for k, v in zip("+-*/", [op.add, op.sub, op.mul, op.truediv])}
    return int(operator_lookup[operator](int(operandA), int(operandB)))



def calculate(s: str) -> int:
    s_clean_arr = [char for char in s if char in set(string.digits +'*/+-')]
    dll = DLL()
    for char in s_clean_arr:
        dll.insert(DLLNode(char))

    # Pass for */
    cur = dll.head.next
    while cur != dll.tail:
        if cur.value in ("*", "/"):
            operator = cur.value
            operandA = cur.prev.value
            operandB = cur.next.value
            cur.value = evaluate(operator, operandA, operandB)

            cur.prev.prev.next = cur
            cur.prev = cur.prev.prev
            cur.next.next.prev = cur
            cur.next = cur.next.next

        cur = cur.next

    # Pass for +-
    cur = dll.head.next
    while cur != dll.tail:
        if cur.value in ("+", "-"):
            # Evaluate + Stitch
            operator = cur.value
            operandA = cur.prev.value
            operandB = cur.next.value
            cur.value = evaluate(operator, operandA, operandB)

            cur.prev.prev.next = cur
            cur.prev = cur.prev.prev
            cur.next.next.prev = cur
            cur.next = cur.next.next
        cur = cur.next

    return int(dll.head.next.value)





def test(fn):
    assert fn("3+2*2") == 7
    assert fn("3/2") == 1
    assert fn("3+5/2") == 5

test(calculate)