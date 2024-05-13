"""
Given HEAD, the head of a linked list, determine if the linked list
has a cycle in it.

There is a cycle in a LinkedList if there is some node in the list that
can be reached again by continnuously following the .next pointer.

Return whether there is a cycle in the LL
"""
from __future__ import annotations # This lets me use LLN as a type ann in the same class -- cooll!

from typing import Optional


class LinkedListNode:
    def __init__(self, val: int, next: Optional[LinkedListNode] = None):
        self.val = val
        self.next = next

def has_cycle(head: LinkedListNode) -> bool:
    # Simple: Keep track of the ones you've visited! This uses O(1)
    seen = set()
    cur = head
    while cur:
        if cur not in seen:
            seen.add(cur)
            cur = cur.next
        else:
            return True
    return False

def has_cycle_constant_memory(head: LinkedListNode) -> bool:
    # Smarter: O(1) memory: Have a slow and fast pointer -- if they ever touch, cycle!
    slow = head
    fast = head
    # Until Fast has left the LL
    while fast:
        # Advance
        slow = slow.next # One Step for slow
        fast = fast.next # Two Steps for fast
        fast = fast.next if hasattr(fast, "next") else None
        # Look: Cycle? Confirm that they're both not None also by checking first condition :)
        if slow and slow == fast:
            return True

    return False



# Case 1
a_1 = LinkedListNode(3)
a_2 = LinkedListNode(2)
a_3 = LinkedListNode(0)
a_4 = LinkedListNode(4)
a_1.next = a_2
a_2.next = a_3
a_3.next = a_4
a_4.next = a_2
print(has_cycle_constant_memory(a_1)) # true

# Case 2
b_1 = LinkedListNode(1)
b_2 = LinkedListNode(2)
b_1.next = b_2
b_2.next = b_1
print(has_cycle_constant_memory(b_1)) # true

# Case 3
c_1 = LinkedListNode(1)
print(has_cycle_constant_memory(c_1)) # false


