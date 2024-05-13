from __future__ import annotations
from typing import Optional

"""
Odd Even Linked List

Given the `head` of a singly linked list, group all of the
nodes with odd indices together, followed by the
nodes with the even indices, and return the reordered list.

The first node is considered odd, second even, ...

Note that the relative order inside both the even and odd groups should remain
as it was in the input

Must solve in O(1) extra space complexity, and O(N) time complexity


1 -> 2 -> 3 -> 4 -> 5 ->
TO
1 -> 3 -> 5 -> 2 -> 4 ->
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


"""
I think the idea is just having a pointer to the current Odd node and the 
the current Even node, but the trick is in how/when you repoint .nexts and 

"""


def odd_even_linked_list(head: Node) -> Node:
    odd_head = head
    even_head = head.next
    original_even_head = even_head

    while odd_head.next and even_head.next:
        next_odd_head = odd_head.next.next
        next_even_head = even_head.next.next

        odd_head.next = next_odd_head
        even_head.next = next_even_head

        odd_head = next_odd_head
        even_head = next_even_head

    # Stitch the end of the odd one to the start of the even one
    odd_head.next = original_even_head

    return head


def test(fn):
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert fn(head).to_list() == [1, 3, 5, 2, 4]
    head = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))
    assert fn(head).to_list() == [2, 3, 6, 7, 1, 5, 4]

test(odd_even_linked_list)
