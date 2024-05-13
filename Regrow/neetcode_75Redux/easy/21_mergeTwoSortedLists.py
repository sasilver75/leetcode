from __future__ import annotations
from typing import Optional
"""
Merge Two Sorted Lists

You are given the heads of two SORTED linked lists list1 and list2

Merge the two lists into one SORTED list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    @classmethod
    def from_list(cls, lst: list[int]):
        dummy = Node(None)
        cur = dummy
        for i in lst:
            cur.next = Node(i)
            cur = cur.next
        return dummy.next

    def to_list(self):
        acc = []
        cur = self
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc

def merge_two_lists(list1: Optional[Node], list2: Optional[Node]):
    dummy = Node(None)
    cur = dummy
    l1n = list1
    l2n = list2

    while l1n and l2n:
        if l1n.value <= l2n.value:
            cur.next = l1n
            cur = cur.next
            l1n = l1n.next
        else:
            cur.next = l2n
            cur = cur.next
            l2n = l2n.next

    if l1n:
        cur.next = l1n

    if l2n:
        cur.next = l2n

    return dummy.next


l1 = Node.from_list([1,2,4])
l2 = Node.from_list([1,3,4])
assert merge_two_lists(l1, l2).to_list() == [1,1,2,3,4,4]

l1 = None
l2 = None
assert merge_two_lists(l1, l2) == None

l1 = None
l2 = Node.from_list([0])
assert merge_two_lists(l1, l2).to_list() == [0]