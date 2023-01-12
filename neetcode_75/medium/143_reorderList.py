from __future__ import annotations
from typing import Optional

"""
Reorder List
Category: Linked List

You're given the `head` of a singly linked list.

The list can be repesented as

(0) -> (1) -> .. -> (n-1) -> (n) ->

REORDER the list to be on the following form:

(0) -> (n) -> (1) -> (n-1) -> (2) -> (n-2) -> ... -> 
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def to_list(self):
        acc = []
        cur = self
        while cur:
            print(cur.value)
            acc.append(cur.value)
            cur = cur.next
        print(acc)
        return acc

    @classmethod
    def from_list(cls, values: list[int]) -> Optional[Node]:
        if not values:
            return None

        head = Node(values[0])
        cur = head
        for idx in range(1, len(values)):
            new = Node(values[idx])
            cur.next = new
            cur = new

        return head


# -- Work Zone --

"""
Thinking:

1 -> 2 -> 3 -> 4 -> 5 -> 
to
1 -> 5 -> 2 -> 4 -> 3 ->

Can we just load them into memory and in an array, and use two pointers?

[1, 2, 3, 4, 5]
l            r


arr = [1,2,3,4,5] # Populate this
if len(arr) <= 2:
    return head

cur = arr[0]
l = 1
r = len(arr) - 1
while l <= r:
    leftNode = arr[l]
    rightNode = arr[r] if arr[r] is not leftNode else None
    
    if l == 0:
        cur = leftNode
    
    cur.next = rightNode
    cur = rightNode
"""


def reorder_list(head: Optional[Node]) -> Optional[Node]:
    # O(N) time and O(N) space
    if head is None:
        return None

    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next

    reordered = []
    l = 0
    r = len(nodes) - 1
    while l <= r:
        leftNode, rightNode = nodes[l], nodes[r]
        reordered.append(leftNode)
        if rightNode is not leftNode:
            reordered.append(rightNode)
        l += 1
        r -= 1

    for idx, node in enumerate(reordered):
        node.next = reordered[idx + 1] if idx < len(reordered) - 1 else None

    return head


"""
Is there a way that we could do it in O(N) time and O(1) space?

1 -> 2 -> 3 -> 4 -> 5 -> 
to
1 -> 5 -> 2 -> 4 -> 3 ->

1) Find the mid-point node using fast/slow pointers
    1 -> 2 -> 3 -> 4 -> 5 -> 
              ^
              
2) Reverse the second half of the list in-place
    1 -> 2 -> 5 -> 4 -> 3 -> 
              ^

3) "Merge"/Interleave the first and second halves of the list into a "new" list
    1 -> 5 -> 2 -> 4 -> 3 -> 
    This is our answer that we wanted! 
"""


def reorder_list_good(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    def get_list_length(head: Node) -> int:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        return length

    def find_midpoint(head: Node) -> Node:
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
        return slow

    def reverse_list(head: Node) -> Node:
        prev, cur = None, head
        while cur:
            # Get a reference to actual next node
            next = cur.next

            # Flip the .next pointer
            cur.next = prev

            # Slide pointers forward
            prev = cur
            cur = next
        return prev

    """
        4
1   2   3
            None        1   4   2   3

    """

    def merge_lists(h1: Node, h2: Node, length: int):
        dummy = Node(None)
        cur = dummy

        while h1 and h2:
            print("Bomp: ", h1.value, h2.value)
            if h1 is cur:  # This is for the case of an even-lengthed list
                break

            next_h1 = h1.next
            next_h2 = h2.next

            cur.next = h1
            cur = cur.next
            cur.next = h2
            cur = cur.next

            h1 = next_h1
            h2 = next_h2

        # For an even-lengthed list... would his work? Odd lengthed?
        if length % 2 == 1:
            cur.next = h1
            h1.next = None

        return dummy.next

    """
    1   2 ->  3 ->   4 ->   5 ->
              ^
    1 -> 2->  3 <-  4  <-  5
            (3 points to None as .next because of reversing)
    15243
    """
    length = get_list_length(head)
    mid_node = find_midpoint(head)
    tail = reverse_list(mid_node)
    ans = merge_lists(head, tail, length)
    return ans


"""
1 -> 2 -> 3 -> 4 -> None

Find midpoint:
1 -> 2 -> 3 -> 4 -> None 
          ^

Reversed:
1 -> 2 -> 3 -> None       4 -> 3 -> None


        4
1   2   3
            None        1   4   2   3

"""


# -- Test Zone --
def test(fn):
    head = Node.from_list([1, 2, 3, 4])
    assert fn(head).to_list() == [1, 4, 2, 3]

    head = Node.from_list([1, 2, 3, 4, 5])
    assert fn(head).to_list() == [1, 5, 2, 4, 3]


# test(reorder_list)
test(reorder_list_good)
