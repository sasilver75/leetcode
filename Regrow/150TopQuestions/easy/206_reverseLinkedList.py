from __future__ import annotations
from typing import Optional

"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the
reversed list!
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def print_list(self) -> None:
        cur = self
        while cur:
            print(cur.value)
            cur = cur.next
        print()


"""
    i         n
        1 ->  2 ->  3 ->  4 ->  5 ->
        j
"""


def reverse_linked_list(head: Node):
    slow = None
    fast = head

    while fast:
        # Shoot out an anchor to "Save" our next "fast"
        next = fast.next
        # Reverse from our lead pointer
        fast.next = slow
        # Slide both pointers forward
        slow = fast
        fast = next

    return slow


# Case 1
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
reverse_linked_list(head).print_list()

# Case 2
head = Node(1, Node(2))
reverse_linked_list(head).print_list()
