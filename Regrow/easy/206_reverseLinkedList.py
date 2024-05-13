"""
Reverse Linked List

Given the HEAD of a singly linked list,
reverse the list, and return the REVERSED list.
"""
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next


def reversed(head: Node) -> Node:
    # Setup
    prev = None
    cur = head

    while cur:
        # Throw out a grappling hook to the next one
        next = cur.next
        # Flip current node's next pointer to the PREVIOUS node
        cur.next = prev
        # Inchworm your prev/cur pointers forward, from back to front
        prev = cur
        cur = next

    # At the end, prev will be the "last" node, which is actually teh head of our reversed list
    return prev


def values(head: Node):
    vals = []
    cur = head
    while cur:
        vals.append(cur.value)
        cur = cur.next
    return vals

# Ex 1
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(values(head))
print(values(reversed(head))) # [5, 4, 3, 2, 1]

# Ex2
head = Node(1, Node(2))
print(values(head))
print(values(reversed(head))) # [2, 1]

# Ex3
print(reversed(None)) # None