from __future__ import annotations
from typing import Optional

"""
Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there's some node that can be reached again by continuously following the next pointer.

 """

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next



def linked_list_cycle_memory(head: Node) -> bool:
    seen = set()
    cur = head
    while cur:
        if cur in seen:
            return True
        seen.add(cur)
        cur = cur.next
    return False

"""Can we do it without using O(N) memory as well?"""
def linked_list_cycle(head: Node) -> bool:
    # Base Case of it being a one-node list
    if head.next is None:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


a = Node(3)
b = Node(2)
c = Node(0)
d = Node(-4)
a.next = b
b.next = c
c.next = d
d.next = b
assert linked_list_cycle_memory(a) == True
assert linked_list_cycle(a) == True

a = Node(1)
b = Node(2)
a.next = b
b.next = a
assert linked_list_cycle_memory(a) == True
assert linked_list_cycle(a) == True

a = Node(1, Node(2, Node(3)))
assert linked_list_cycle_memory(a) == False
assert linked_list_cycle(a) == False

a = Node(1)
assert linked_list_cycle_memory(a) == False
assert linked_list_cycle(a) == False