from __future__ import annotations
from typing import Optional

"""
Reverse Linked List

Given the HEAD of as ingly linekd list, reverse the list and return the
reversed list.
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def to_list(self):
        acc = []
        cur = self
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc


# Reverse Linked List
def reverse_list(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev


def test(fn):
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert fn(head).to_list() == [5, 4, 3, 2, 1]

    head = Node(1, Node(2))
    assert fn(head).to_list() == [2, 1]

    assert fn(None) == None

test(reverse_list)