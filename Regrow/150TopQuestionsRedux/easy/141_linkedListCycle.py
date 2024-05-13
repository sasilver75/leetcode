from __future__ import annotations
from typing import Optional

"""
141 Linked List Cyclec

Given the head of a linked list, determine if the linked list has a cycle in it.

There's a cycle in a LL i there's a node in thelist that can be reached again by continuously
following the NEXT pointer. Internally, pos is used to denote the index
of a node that tail's next pointer is connected to.

REturn TRUE if there is a cycle in the linked list, otherwise return FALSE.
"""

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

def has_cycle(head: Optional[Node]) -> bool:
    slow, fast = head, head

    while fast is not None:
        # Move them
        fast = fast.next.next if fast.next else fast.next  # Take 2 if you can, 1 if you can't
        slow = slow.next

        # Check: Did they line up on a Node?
        if fast == slow and fast is not None:
            return True

    return False


a = Node(3)
b = Node(2)
c = Node(0)
d = Node(4)
a.next = b
b.next = c
c.next = d
d.next = b

assert has_cycle(a) == True

a = Node(1)
b = Node(2)
a.next = b
b.next = a
assert has_cycle(a) == True

assert has_cycle(Node(1)) == False