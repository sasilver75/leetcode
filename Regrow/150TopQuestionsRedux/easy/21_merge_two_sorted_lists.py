from __future__ import annotations
from typing import Optional
"""
21. Merge Two Sorted Lists

"""

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def to_list(self) -> list[int]:
        cur = self
        acc = []
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc

    @classmethod
    def from_list(cls, nums: list[int]) -> Optional[Node]:
        dummy = Node(None)
        cur = dummy
        for num in nums:
            cur.next = Node(num)
            cur = cur.next
        return dummy.next


assert Node.from_list([1,2,3]).to_list() == [1,2,3]

"""
Given that two lists are sorted, this is very similar to the "merge" operation from merge sort
"""
def merge_lists(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    dummy = Node(None)
    cur = dummy
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            cur.next = l1
            cur = cur.next

            l1 = l1.next
        else:
            cur.next = l2
            cur = cur.next

            l2 = l2.next

    # You don't need to do a while loop here; we can just attach the end of our merged list to the remaining l1
    if l1 is not None:
        cur.next = l1

    if l2 is not None:
        cur.next = l2

    return dummy.next




l1 = Node.from_list([1,2,4])
l2 = Node.from_list([1,3,4])
assert merge_lists(l1,l2).to_list() == [1,1,2,3,4,4]

assert merge_lists(None, None) is None

assert merge_lists(None, Node(0)).to_list() == [0]