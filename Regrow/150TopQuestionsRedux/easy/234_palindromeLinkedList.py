from __future__ import annotations
from typing import Optional

"""
Palindrome Linked List

Given the head of a singly linked list, return TRUE if it is a PALINDROME,
or FALSE otherwise.
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next


def is_palindrome_naive(head: Optional[Node]) -> bool:
    acc = []
    cur = head
    while cur:
        acc.append(cur.value)
        cur = cur.next
    l, r = 0, len(acc) - 1
    while l < r:
        if acc[l] != acc[r]:
            return False
        l += 1
        r -= 1
    return True


"""
The idea is to REVERSE the second half of the linked list!
We do a fast/slow pointer trick to walk a pointer to the middle of the list, then reverse the list.
Now we have two linked list heads pointing inwards to a common middle element. 
Then you need to clean up afterwards
"""


def is_palindrome(head: Optional[Node]) -> bool:
    prev = None
    slow, fast = head, head

    """
    1 ->  2 ->  2 ->  1 ->
    """

    # Walk slow to the middle of the linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    """
              s         f
    1 -> 2 -> 2 -> 1 ->
    """

    # Reverse the second half of the linked list
    prev = slow
    slow = slow.next
    prev.next = None # Is this even required? This is for the terminating condition on line 65, but that could be a while True too

    """
              p    s      f
    1 -> 2 -> 2 -> 1 -> 
              v
    """

    while slow:
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next

    """             
    1 -> 2 -> 2 <- 1 
              v
    """

    # Now we can walk two head/tail pointers in towards eachother from each end
    # If their values are not equal, we can return False
    left, right = head, prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True




def test(fn):
    root = Node(1, Node(2, Node(2, Node(1))))
    assert fn(root) == True

    root = Node(1, Node(2))
    assert fn(root) == False


# test(is_palindrome_naive)
test(is_palindrome)
