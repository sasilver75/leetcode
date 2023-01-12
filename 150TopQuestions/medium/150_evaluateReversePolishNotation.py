from __future__ import annotations
from typing import Optional, Union

"""
Evaluate Reverse Polish Notation

Evaluate the value or an arithmetic expression in REVERSE POLISH NOTATION

Valid operators are +, -, *, and /
Each operand may be an integer or another expression.

NOTE that division between two integers should truncate "towards zero".

It is guaranteed that the given RPN expression is always valid.
This means that the expression will always evaluate to a result, and there
will not be any division by zero operation.
"""

"""
Thinking:
    2   1   +   3   *
    
    Gets grouped into 
    ((2 1 +) 3 *)
    So you group into (operand operand operator) triplets
    
In both the case of 
    2   1   +   3   *       --> ((2 + 1) * 3)
and
    4   13  5   /   +       --> (4 + (13 / 5))

The evaluation order of the operators is "left to right", using the nearest
two operands to the left of the operator.
We could do this recursively or iteratively:

    {2   1   +}   3   *                        4   {13  5   /}   +
     {3   3    *}                               {4   2  +}                        
     9                                          6.6
    
Note on the right side example that we considered 13 / 5 to be 2, rather 
than 2.6. This is because of our rule about dividing "toward zero"

So we could do M passes, where M is the # of operands, for each pass
"combining" the operator and appropriate operands.

A way that we could do this is to do a single pass through the list,
and turn it into a doubly-linked list.
This makes the "combining" operation of 3 elements (operand, operand, operator)
into a constant time operation, instead of an O(N) operation of splicing into a list 

"""
class Node:
    def __init__(self, value: int, next: Optional[Node] = None, prev: Optional[Node] = None):
        self.value = value
        self.next = next
        self.prev = prev

    def print_list(self) -> list[int]:
        cur = self
        acc = []
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc


def evaluate(operator: str, operand1: str, operand2: str):
    # Given a valid operator and two numeric operands, return result
    res = eval(operand1+operator+operand2)
    if operator == "/":
        res = int(res) # This rounds towards zero whether positive or negative
    return res

def rpn(tokens: list[str]) -> int:
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
            ans = evaluate(cur.value, second.value, first.value) # Order matters for division. (5, 13, /) -> 5/13, not 13/5
            cur.value = str(ans)

            # Stitch up DLL
            cur.prev = second.prev
            second.prev.next = cur

            print("Stitched")
        cur = cur.next

    return int(head.next.value)



# -- Test Zone --
def test(fn):
    assert fn(["2", "1", "+", "3", "*"]) == 9  # ((2+1)*3) == 9
    assert fn(["4", "13", "5", "/", "+"]) == 6  # (4 + (13 / 5)) = (4 + 2) = 6
    assert fn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5",
               "+"]) == 22  # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5

test(rpn)