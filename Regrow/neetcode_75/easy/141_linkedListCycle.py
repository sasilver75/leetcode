from __future__ import annotations
from typing import Optional
"""
Linked List Cycle

Given `head`, the head of a linked list, determine
if the linked list has a cycle in it or not!

There's a cycle in the linked list if there is some node
in the list that can be reached again by continuously following
the `next` pointer.

Internally, `pos` is used to denote the index of
the node that tail's .next pointer is connected to. Note
that pos is not possed as a parameter.
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


def linked_list_cycle(head: Optional[Node]) -> bool:
    if not head or not head.next:
        return False

    slow = fast = head

    while fast:
        # Advance Slow
        slow = slow.next

        # Advance Fast
        if fast.next:
            fast = fast.next.next
        else:
            fast = fast.next

        # Check: Are we at the same node?
        if slow is fast:
            return True

    return False

# -- Test Zone --
a = Node(3)
b = Node(2)
c = Node(0)
d = Node(-4)
a.next = b
b.next = c
c.next = d
d.next = b
assert linked_list_cycle(a) == True

a = Node(1)
b = Node(2)
a.next = b
b.next = a
assert linked_list_cycle(a) == True

a = Node(1)
assert linked_list_cycle(a) == False
