from __future__ import annotations
from typing import Optional
"""
You are given the heads of two sorted linked lists
list1 and list2.
Merge the two lists into one sorted list!
The list should be made by splicing together the nodes
of the first two lists. 
Return the head of the merged linked list.
"""

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next


def merge_lists(n1: Node, n2: Node) -> Node:
    dummy = Node(None)
    cur = dummy
    while n1 is not None and n2 is not None:
        if n1.value <= n2.value:
            cur.next = Node(n1.value)
            cur = cur.next
            n1 = n1.next
        else:
            cur.next = Node(n2.value)
            cur = cur.next
            n2 = n2.next

    while n1 is not None:
        cur.next = Node(n1.value)
        cur = cur.next
        n1 = n1.next

    while n2 is not None:
        cur.next = Node(n2.value)
        cur = cur.next
        n2 = n2.next

    return dummy.next

def ll_to_list(head: Node) -> list[int]:
    """
    Just a helper for testing
    """
    acc = []
    while head:
        acc.append(head.value)
        head = head.next

    return acc

n1 = Node(1, Node(2, Node(4)))
n2 = Node(1, Node(3, Node(4)))
assert ll_to_list(merge_lists(n1, n2)) == [1,1,2,3,4,4]
assert merge_lists(None, None) == None
n2 = Node(0)
assert ll_to_list(merge_lists(None, n2)) == [0]
