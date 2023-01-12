from __future__ import annotations

"""
Add Two Numbers

You are given two NON-EMPTY linked lists representing two NON-NEGATIVE integers.
The digits are stored in REVERSE ORDER, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a (new) linked list.

You may assume that the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def get_list(self):
        acc = []
        cur = self
        while cur:
            acc.append(cur.value)
            cur = cur.next

        print(acc)
        return acc


def add_two_numbers(l1: Node, l2: Node) -> Node:
    head = Node(0)
    cur = head

    carry = 0

    # Note: These three while statements could be combined into a single while statement, just with some more annoying ternaries
    while l1 and l2:
        sum = l1.value + l2.value + carry
        val = sum % 10
        carry = sum // 10

        cur.next = Node(val)

        cur = cur.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        sum = l1.value + carry
        val = sum % 10
        carry = sum // 10

        cur.next = Node(val)

        cur = cur.next
        l1 = l1.next

    while l2:
        sum = l2.value + carry
        val = sum % 10
        carry = sum // 10

        cur.next = Node(val)

        cur = cur.next
        l2 = l2.next


    # Take care of any remaining carry
    if carry:
        cur.next = Node(carry)
        # cur = cur.next  # Not needed

    return head.next  # "Remove" the leading dummy element


# Scenario 1
l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(4)))
assert add_two_numbers(l1, l2).get_list() == [7, 0, 8]

# Scenario 2
l1 = Node(0)
l2 = Node(0)
assert add_two_numbers(l1, l2).get_list() == [0]

# Scenario 3
l1 = Node(9, Node(9, Node(9, Node(9, Node(9, Node(9, Node(9)))))))
l2 = Node(9, Node(9, Node(9, Node(9))))
assert add_two_numbers(l1, l2).get_list() == [8, 9, 9, 9, 0, 0, 0, 1]
