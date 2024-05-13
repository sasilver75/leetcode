from __future__ import annotations
from typing import Optional

"""
Remove Nth Node from End of List
Category: Linked List

Given the `head` of a linked list, remove the nth node from
the end of the list and return its head.
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


# ---- Work Zone ----

"""
Note that 1'st frmo the end of list is going to be the 
"""
def removeNthFromEnd(head: Optional[Node], n: int) -> Optional[Node]:
    if not head or (not head.next and n == 1):
        return None


    # Count number of nodes
    node_count = 0
    cur = head
    while cur:
        node_count += 1
        cur = cur.next

    print(node_count)

    # Given number of nodes, how many steps to get to the nth-from-end node?
    if n > node_count:
        raise ValueError("Nope!")

    steps_to_take = node_count - n

    # Walk to the to-cut node
    prev = None
    cur = head
    for _ in range(steps_to_take):
        prev = cur
        cur = cur.next

    # Cut it out
    prev.next = cur.next

    return head




# -- Test Zone --
head = Node.from_list([1, 2, 3, 4, 5])
assert removeNthFromEnd(head, 2).as_list() == [1, 2, 3, 5]

head = Node.from_list([1])
assert removeNthFromEnd(head, 1) == None

head = Node.from_list([1, 2])
assert removeNthFromEnd(head, 1).as_list() == [1]
