from __future__ import annotations
from typing import Optional, Callable

"""
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the
end of the list and return its head.

NOTE: n=1 means the "last" one
"""

class Node:
    def __init__(self, value: Optional[int], next: Optional[Node] = None):
        self.value = value
        self.next = next


def remove_nth_node(head: Node, n: int) -> Node:
    if n < 1:
        raise ValueError("n must be >= 1")

    dummy = Node(None)
    dummy.next = head

    # Get the length of the list
    length = 0
    cur = dummy.next
    while cur:
        length += 1
        cur = cur.next

    if n > length:
        raise ValueError("n is out of bounds")

    # Determine how many steps we have to take from DUMMY to get to
    # the node immediately BEFORE the one we need to cut
    """
    (D)->(4)->(1)->(7)->(19)
                    ^
    length = 4 (without dummy)
    
    n=1 --> 3 steps
    n=2 --> 2 steps
    n=3 --> 1 steps 
    n=4 --> 0 steps
    
    Seems to be (length - n) steps to the "before cut" node
    """
    steps = length - n
    cur = dummy
    while steps:
        steps -= 1
        cur = cur.next

    # Make Incision
    cur.next = cur.next.next

    return dummy.next









# -- Test Zone --

# Scenario 1
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
ans_1 = remove_nth_node(head, 2) # Should be 1235 - Yep!
ans_2 = remove_nth_node(Node(1), 1) # Should be [] - Yep!
ans_3 = remove_nth_node(Node(1, Node(2)), 1) # Should be 1 - Yep!
print("Done!")