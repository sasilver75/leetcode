from __future__ import annotations
from typing import Optional
"""
Add Two Numbers
Given two NON-EMPTY linked lists representing two non-negative integers
The digits are stored in REVERSE ORDER, and each of their nodes contains a single digit. Add the two numbers and return
the sum as a linked list.
You may assume that the two numbers don't contain any leading zero, except the number 0 itself.
"""

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def to_int(self):
        acc = []
        cur = self
        while cur:
            acc.append(str(cur.value))
            cur = cur.next

        if not acc:
            return 0

        ans = int("".join(acc))
        print(ans)
        return ans




def add_two_numbers(l1: Node, l2: Node) -> Node:
    dummy = Node(None)
    cur = dummy

    # Pointers for traversing l1/l2
    n1 = l1
    n2 = l2

    carry = 0
    while n1 and n2:
        # Calculate Sum and Carry
        sum_with_carry = n1.value + n2.value + carry
        new_val = sum_with_carry % 10
        carry = sum_with_carry // 10

        # Create Next Node
        cur.next = Node(new_val)

        # Advance Pointers
        cur = cur.next
        n1 = n1.next
        n2 = n2.next

    while n1:
        # Calculate Sum and Carry
        sum_with_carry = n1.value + carry
        new_val = sum_with_carry % 10
        carry = sum_with_carry // 10

        # Create Next Node
        cur.next = Node(new_val)

        # Advance Pointers
        cur = cur.next
        n1 = n1.next

    while n2:
        # Calculate Sum and Carry
        sum_with_carry = n2.value + carry
        new_val = sum_with_carry % 10
        carry = sum_with_carry // 10

        # Create Next Node
        cur.next = Node(new_val)

        # Advance Pointers
        cur = cur.next
        n2 = n2.next

    # There may be some remaining carry that should be in a new node on the end
    if carry:
        cur.next = Node(carry)

    return dummy.next

l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(4)))
assert add_two_numbers(l1, l2).to_int() == 708

l1 = Node(0)
l2 = Node(0)
assert add_two_numbers(l1, l2).to_int() == 0

l1 = Node(9, Node(9, Node(9, Node(9, Node(9, Node(9, Node(9)))))))
l2 = Node(9, Node(9, Node(9, Node(9))))
assert add_two_numbers(l1, l2).to_int() == 89990001
