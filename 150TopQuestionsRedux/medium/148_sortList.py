from __future__ import annotations
from typing import Optional

"""
Sort List

Given the head of a linked list, return the list after sorting
it in ASCENDING order

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
    def from_list(cls, nums: list[int]) -> Optional[Node]:
        if not nums:
            return None

        head = Node(nums[0])
        cur = head
        for i in range(1, len(nums)):
            next_node = Node(nums[i])
            cur.next = next_node
            cur = cur.next
        return head


def merge_lists(h1: Node, h2: Node):
    dummy = Node(None)
    cur = dummy
    n1, n2 = h1, h2
    while n1 and n2:
        if n1.value <= n2.value:
            next_cur = Node(n1.value)
            n1 = n1.next
        else:
            next_cur = Node(n2.value)
            n2 = n2.next

        cur.next = next_cur
        cur = cur.next

    while n1:
        next_cur = Node(n1.value)
        n1 = n1.next
        cur.next = next_cur
        cur = cur.next

    while n2:
        next_cur = Node(n2.value)
        n2 = n2.next
        cur.next = next_cur
        cur = cur.next

    return dummy.next


def split_list(head: Node) -> Node:
    # 1 -> 2 -> 3 -> -> 4
    # becomes 1 -> 2  3 -> 4  , 3 is returned
    slow = head
    fast = head

    slow_slow = slow
    while fast and fast.next:
        fast = fast.next.next
        slow_slow = slow
        slow = slow.next

    slow_slow.next = None
    return slow


h1 = Node(1, Node(2, Node(3)))
h2 = split_list(h1)
assert h1.as_list() == [1]
assert h2.as_list() == [2, 3]

h1 = Node(1, Node(2, Node(3, Node(4))))
h2 = split_list(h1)
assert h1.as_list() == [1, 2]
assert h2.as_list() == [3, 4]


def sort_list(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    head2 = split_list(head)

    sorted_left = sort_list(head)
    sorted_right = sort_list(head2)

    merged = merge_lists(sorted_left, sorted_right)
    return merged


# -- Test --
head = Node.from_list([4, 2, 1, 3])
assert sort_list(head).as_list() == [1, 2, 3, 4]

head = Node.from_list([-1, 5, 3, 4, 0])
assert sort_list(head).as_list() == [-1, 0, 3, 4, 5]
