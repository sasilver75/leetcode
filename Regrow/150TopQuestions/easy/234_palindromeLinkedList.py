from __future__ import annotations
from typing import Optional, Tuple

"""
Palindrome Linked List

Given the head of a singly linked list, return true if it
is a palindrome or false otherwise.
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def print(self) -> None:
        cur = self
        while cur:
            print(cur.value)
            cur = cur.next
        print()


def is_palindrome(head: Node) -> bool:
    """
    If this were a list, we'd just have a pointer at each end, and walk them towards eachother
    But in this situation, we've got a singly linked list with no backwards-references

    Can we correct this by temporarily making it a doubly-linked list?
    And then clean up afterwards?
    That'd be O(N) in the same way as copying the list into an actual array, though.
    (Though probably less actual memory overhead)

    ---

    It turns out that the ONLY way that we can avoid using O(N) extra space is by
    modifying the input-inplace.... by REVERSING the second half of hte linked list
    in-place, modifying the structure, and then putting it back in-order afterwards.
    """
    slow = head
    fast = head.next
    slow.prev = None  # Technically don't need to do this...
    while fast:
        fast.prev = slow
        # Slide pointers forward
        slow = fast
        fast = fast.next

    # Slow is the tail node

    l = head
    r = slow
    while l != r:
        if l.value != r.value:
            return False
        l = l.next
        r = r.prev

    return True


# Example 1
head = Node(1, Node(2, Node(2, Node(1))))
assert is_palindrome(head) == True
assert is_palindrome(head) == True

# Example 2
head = Node(1, Node(2))
assert is_palindrome(head) == False


