from __future__ import annotations
from typing import Optional
"""
Copy List with Random Pointer

A linked list of length `n` is given such that each
node contains an additional RANDOM pointer, which could point to any node
in the list, OR null!

Construct a DEEP COPY of the list -- the depe copy should
consist of exactly n BRAND NEW nodes, where each new node has its value set to the
value of its corresponding original node.
Both the NEXT and RANDOM pointer of the new nodes should point to new
nodes in the copied list, such that the pointers in the original list
and copied list represent the same list state.

None of the pointers in the new list should point to nodes in the original
list!

For example, if there are two nodes X and Y in the original list,
where X.random ---> Y, then for the corresponding two nodes x and y in the
copied list, x.random --> y

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.
EAch node is representing as a pair of [val, random_index] where:

* val: an integer representing node.val
* random_index: the index of the node (range from 0 to n-1) that the `random`
pointer points to, or `null` if it does not point to any node.

Your code will only be given the head of the original linked list.
"""

class Node:
    def __init__(self, value: int, next: Optional[Node] = None, random: Optional[Node] = None):
        self.value = value
        self.next = next
        self.random = random

def copy_random_list(head: Node):
    pass

# -- Test Zone --
head = Node()