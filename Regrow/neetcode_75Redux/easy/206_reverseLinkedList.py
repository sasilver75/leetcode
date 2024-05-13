from __future__ import annotations
from typing import Optional

"""
Reverse LInked List

Given the head of a singly linked list, reverse the list and return the head of the reversed list.
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def as_list(self):
        acc = []
        cur = self
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc


def reverseList(head: Node) -> Node:
    prev = None
    cur = head
    while cur:
        next_cur = cur.next
        cur.next = prev
        prev = cur
        cur = next_cur

    return prev




head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
assert reverseList(head).as_list() == [5, 4, 3, 2, 1]

head = Node(1, Node(2))
assert reverseList(head).as_list() == [2,1]
