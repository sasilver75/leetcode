from __future__ import annotations
from typing import Optional
"""
Given the heads of two singly linked lists headA and headB, return the NODE
at which the two lists intersect. If the two linked lists have NO intersection
at all, return Null.

For example, the following two linked lists
begin to intersect at node c1:

        a1  a2
              \
                c1  c2  c3
              /
    b1  b2  b3

Note that the linked list must retain their original structure after the
function returns.
"""

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

"""
Okay, what if we just walked one of the lists and kept a hashset of all
of the nodes in the list? Assuming the nodes are hashable, would this work?
"""
def intersection_of_two_linked_lists_naive(head1: Optional[Node] = None, head2: Optional[Node] = None):
    cur = head2
    seen_in_2 = set()
    while cur:
        seen_in_2.add(cur)
        cur = cur.next

    cur = head1
    while cur:
        if cur in seen_in_2:
            print(cur)
            return cur
        cur = cur.next

    print(None)
    return None


"""
Is there a way to do this using just constant extra space?
We need to find another way to align the two linked lists
https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/1092898/js-python-java-c-easy-o-1-extra-space-solution-w-visual-explanation/

This needs a visual explanation.
If in the pictures we assume that the "top" route is A
and the "bottom" route is B,  then we can turn the top route into A+B and the bottom route into B+A, and
just walk in lockstep until the values equal eachother.

We don't do this by actually modifying the structure of the list, just through the 
logic of how we iterate the "a" pointer, and how we iterate the "b" pointer.

Think about for this solution what's actually happening if there ISN'T a 
cycle in the linked list.
"""
def intersection_of_two_linked_lists(head1: Optional[Node] = None, head2: Optional[Node] = None):
    cur1, cur2 = head1, head2
    while cur1 != cur2:
        cur1 = cur1.next if cur1 else head2
        cur2 = cur2.next if cur2 else head1
    return cur1


def test(fn):
    a1 = Node(4)
    a2 = Node(1)
    c1 = Node(5)
    c2 = Node(6)
    c3 = Node(1)
    b1 = Node(8)
    b2 = Node(4)
    b3 = Node(5)
    a1.next = a2
    a2.next = b1
    c1.next = c2
    c2.next = c3
    c3.next = b1
    b1.next = b2
    b2.next = b3
    assert fn(a1, c1) == b1

    a1 = Node(1)
    a2 = Node(9)
    a3 = Node(1)
    c1 = Node(3)
    b1 = Node(2)
    b2 = Node(4)
    a1.next = a2
    a2.next = a3
    a3.next = b1
    c1.next = b1
    b1.next = b2
    assert fn(a1, c1) == b1

    a = Node(2, Node(6, Node(4)))
    b = Node(1, Node(5))
    assert fn(a,b) == None

test(intersection_of_two_linked_lists_naive)
test(intersection_of_two_linked_lists)