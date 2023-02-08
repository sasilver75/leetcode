from __future__ import annotations
from typing import Optional

"""
Remove Nth Node from End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

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

def remove_nth_node(head: Optional[Node], n: int) -> Optional[Node]:
    pass


# -----
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
assert remove_nth_node(head, 2).to_list() == [1,2,3,5]

head = Node(1)
assert remove_nth_node(head, 1) == None

head = Node(1, Node(2))
assert remove_nth_node(1).to_list() == [1]