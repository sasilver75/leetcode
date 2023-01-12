from __future__ import annotations
from typing import Optional

"""
Sort List

Given the `head` of a linked list, return the list AFTER SORTING IT
in ASCENDING ORDER!
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def to_list(self) -> list[int]:
        acc = []
        cur = self
        while cur:
            acc.append(cur.value)
            cur = cur.next

        print(acc)
        return acc

"""
I can sort of think of two ways of doing this, maybe?

I'm planning on doing something like merge sort on a linked list.
You can either be constructing a new list, or you can be swapping the values 
and/or pointers on the existing linked list.

For the first case, the "easiest" think to do would be to "cast" the linked list
to a list, sort the list, and generate and return a new linked list.
"""

def merge(l1: list[int], l2: list[int]) -> list[int]:
    # ASCENDING SORT
    acc = []
    p1, p2 = 0, 0
    while p1 < len(l1) and p2 < len(l2):
        e1, e2 = l1[p1], l2[p2]
        if e1 <= e2:
            acc.append(e1)
            p1 += 1
        else:
            acc.append(e2)
            p2 += 1

    acc.extend(l1[p1:])
    acc.extend(l2[p2:])

    return acc

def sort(nums: list[int]) -> int:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    return merge(
        sort(nums[0: mid]),
        sort(nums[mid:])
    )



def sort_list_dumb(head: Optional[Node]) -> Node:
    if not head:
        return None

    lst = []
    cur = head
    while cur:
        lst.append(cur.value)
        cur = cur.next

    lst = sort(lst)

    head = Node(lst[0])
    cur = head
    for i in range(1, len(lst)):
        val = lst[i]
        val_node = Node(val)
        cur.next = val_node
        cur = val_node

    return head


"""
How can we do better?
Can we actually merge sort using the nodes themselves?
"""

def merge_nodes(l: Optional[Node], r: Optional[Node]):
    """
    Given two sorted lists, produce one sorted list
    Checked: This works.
    """
    dummy = Node(0)
    cur = dummy

    while l and r:
        if l.value <= r.value:
            cur.next = l
            cur = cur.next

            l = l.next
        else:
            cur.next = r
            cur = cur.next

            r = r.next

    # One of the two sorted lists is exhausted
    cur.next = l if r is None else r

    return dummy.next

def sort_nodes(head: Optional[Node] = None):
    """
    Given an unsorted list of nodes, break it into pieces until it's of
    length
    """
    if head is None: # Length 0 BaseCase
        return None

    if head.next is None: # Length 1 BaseCase
        return head

    # Walk to middle (using fast/slow pointer strategy)
    """
    We want to turn 0 -> 6 -> 4 -> 3 -> 2 -> (None)
    into            0 -> 6 -> (None) and 4 -> 3 -> 2 -> (None)
    So simply walking a pointer to the middle isn't QUITE what we want
    Because we need the mid.prev.next to point to None, rather than Mid.
    So by starting fast "one ahead" of slow, we end with slow at mid-1
    
    Observe:
                     f    
    [0, 6, 4, 3, 2]          -> [0,6,4] + [3, 2]   
           s    
    or
                    f
    [0, 6, 4, 3, 2, 1]  -> [0,6,4] + [3,2,1]
           s
    """


    slow, fast = head, head.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # slow is now at mid-1 --> "Split" the list into two halves!
    head_2 = slow.next
    slow.next = None

    return merge_nodes(
        sort_nodes(head),
        sort_nodes(head_2)
    )



# -- Test --
def test(fn):
    head = Node(4, Node(2, Node(1, Node(3))))
    assert fn(head).to_list() == [1, 2, 3, 4]
    
    head = Node(-1, Node(5, Node(3, Node(4, Node(0)))))
    assert fn(head).to_list() == [-1, 0, 3, 4, 5]
    
    head = None
    assert fn(head) == None

# test(sort_list_dumb)
test(sort_nodes) # Good one :)