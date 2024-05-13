"""
Basic Calculator

Given a string `s` representing an expression, evaluate this expression and
return its value!

*** The integer division should truncate towards zero.***

You may assume that the given expression is always valid. All intermediate results
will be in the range of [2^-31, 2^31 - 1]

Note: you can't use any built-in function that evaluates strings as mathematical
expressions, such as eval.
"""
import collections
from typing import Optional


class DLLNode:
    def __init__(self, value: Optional[str]):
        self.value = value
        self.prev = None
        self.next = None

"""
Here's what I'm thinking.

Essentially what we're doing is combining operators with 2 operands.

{operand} {operator} {operand}

If there was no operator precedence, then what we could do is just 
iterate through the list of characters, and whenever we see an operator,
combine it with the operands on either side.

But there are two problems with that:
    * Time Complexity of "removing" (net) two items from a list is O(2N)
    * Operator Precedence (Ordering)

To address the first one, I think a doubly-linked-list would give me 
constant "combining" time, since I can easily remove items from that list.

To address the second one, I think we need to scan through the list 
and have some notion of the operators that I'll be "combining". 
And then I have to order those operators?
Or perhaps given that there are only four operators to work with, I 
can have a dict of {operator: [OperatorNode, ...]}


Ohh... but this is a little complicated, because it isn't just 
* > / > + > - in terms of operator associativity -- it's 
(* and /), (+ and -), where each (..) is evaluated left to right.
So there are really just two levels to our dict
"""

def evaluate(operator: str, operandA: str, operandB: str) -> str:
    res = eval(operandA + operator + operandB)
    if operator == "/":
        res = int(res) # Int casting has effect of rounding div towards zero
    return str(res)

def calculate(s: str) -> int:
    # Stage 1: Generate DLL
    head = DLLNode(None)
    tail = DLLNode(None)
    head.next = tail
    tail.prev = head
    cur = head

    for char in s:
        new_node = DLLNode(char)

        # Splice in Node: (4 operations)
        new_node.next = cur.next
        cur.next.prev = new_node
        cur.next = new_node
        new_node.prev = cur

        # Advance cur
        cur = new_node

    # Stage 2: Traverse DLL and get Operator-Dict
    operators = {
        "md": [], # *, /
        "as": [] # +, -
    }
    cur = head
    while cur:
        if cur.value in ("*", "/"):
            operators["md"].append(cur)
        elif cur.value in ("+", "-"):
            operators["as"].append(cur)
        cur = cur.next

    # Stage 3: Iterate through operators in the two layers
    for layer in ("md", "as"):
        for operator in operators[layer]:
            # Evaluate and set Result of {OperandA Operator OperandB}
            operandA = operator.prev
            operandB = operator.next
            operator.value = evaluate(operator.value, operandA.value, operandB.value)
            # Splice out OperandA, OperandB nodes (4 operations)
            operator.prev.prev.next = operator
            operator.prev = operator.prev.prev
            operator.next.next.prev = operator
            operator.next = operator.next.next

    return head.next.value

def test(fn):
    fn("3+2*2") == 7
    fn("3/2") == 1

test(calculate)
