from __future__ import annotations
from typing import Optional

"""
Reverse Linked List
Category: Linked List

Given the `head` of a singly linked list, reverse
the list, and return the reverse list!
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

    @classmethod
    def from_list(cls, values: list[int]) -> Optional[Node]:
        if not values:
            return None

        head = Node(values[0])
        cur = head
        for i in range(1, len(values)):
            next = Node(values[i])
            cur.next = next
            cur = cur.next
        return head


"""
(1) -> (2) -> (3) -> None

prev = None
while cur:
    next = cur.next
    cur.next = prev
    prev = cur
"""
def reverse_list(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    prev = None
    cur = head
    while cur:
        """
        (1) -> (2) -> (3) -> None
        
        Given cur @ (1) and prev is None
        1) Prepare
            * Throw out a "grappling hook" to the next node we'll be processing
        2) Process the Current Node
            * Flip around the next pointer at the previous node to point at prev
        
        3)Move Forward
            * prev = cur
            * cur = next
        """
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    # At the end, prev should be pointing at the new head
    return prev


# Test Zone
assert reverse_list(Node.from_list([1, 2, 3, 4, 5])).as_list() == [5, 4, 3, 2, 1]

assert reverse_list(Node.from_list([1, 2])).as_list() == [2, 1]
