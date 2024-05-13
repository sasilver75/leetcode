"""
Odd Even Linked List

Given the `head` of a singly-linked list, group all of the nodes
with ODD indices together followed by the nodes with EVEN indices,
and then return the reordered list.

The FIRST node is considered `odd`, and the SECOND node is considered `even`, etc.

Note that the relative order inside both the even and odd groups should remain
as it was in the input.

** You must solve the problem in O(1) extra space complexity and O(N) time complexity.
"""
from __future__ import annotations

from typing import Optional, Callable


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
        print(acc)
        return acc


def oddEvenList(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    # ~~ Stage 1: Establish Pointers
    cur_odd = head  # Starting at "index 1" (first node - first ODD-indexed Node)
    cur_even = head.next  # Starting at "index 2" (second node - first EVEN-indexed Node)
    even_head = cur_even  # Implicitly, "head" would be our oddHead

    # ~~ Stage 2: Sweep pointers across. While look uses `cur_even` since that's the further right of the two
    while cur_even is not None and cur_even.next is not None:
        # /!\ It's important that cur_odd go first in this, so that they don't step on eachother's fingers
        cur_odd.next = cur_odd.next.next  # Connect to next two spaces ahead (Could be None)
        cur_odd = cur_odd.next  # Slide cur to next

        cur_even.next = cur_even.next.next  # Connect to next two spaces ahead (Could be None)
        cur_even = cur_even.next  # Slide cur to next

    # Now we have one list with odd values, and one list with even values.
    # Now that `odd` is at the end of the odd list and `evenHead` is at the beginning of the even list,
    # we just need to connect them!

    if cur_even:
        cur_even.next = None  # So that our "tail" points to None
    cur_odd.next = even_head # Connect the lists

    return head


"""
Let's explain the above code with a visual example


Initialize "curOdd", "curEven", "oddHead", "evenHead", 

    cO      cE
    (1) -> (2) -> (3) -> (4) -> (5) -> None
    oH      eH
    
    
    (1).next = (1).next.next = (2).next = (3)    
    (1) -> (3)
            cO
            
    (2).next = (2).next.next = (3).next = (4)
    (2) -> (4)
            cE
    
    (3).next = (3).next.next = (4).next = (5)
    (3) -> (5)
    
    ...
    
    What we end up with is basically TWO LISTS:
    
    oH             cO 
    (1) -> (3) -> (5) -> ? 
    
    eH      cE
    (2) -> (4) -> ?
    
    We know that we want (1) -> (3) -> (5) -> (2) -> (4) -> None eventually
    
    To do that:
        * Set cO.next = eH
        * Set cE.next = None   (if it isn't already, I'm not sure)
"""


# Test Zone
def test(fn: Callable[[Node], Node]):
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert fn(head).as_list() == [1, 3, 5, 2, 4]

    head = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))
    assert fn(head).as_list() == [2, 3, 6, 7, 1, 5, 4]

    # Even-length test: [6,4,5,7,9,3] --> [6,5,9,4,7,3]
    head = Node(6, Node(4, Node(5, Node(7, Node(9, Node(3))))))
    assert fn(head).as_list() == [6, 5, 9, 4, 7, 3]


test(oddEvenList)
