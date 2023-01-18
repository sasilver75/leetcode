from __future__ import annotations

import collections
from typing import Optional
"""
Binary Tree Level Order Traversal

Given the `root` of a binary tree, return the LEVEL ORDER TRAVERSAL of its
nodes' values (i.e. from left to right, level by level).
"""

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

"""
I think this is pretty much just a breadth-first search of the tree?
But we need to return it as a list of the nodes at each level, so
on our BFS queue we'll have to encode both the node and the height.
As long as we enqueue left then right, we'll process nodes in level order,
left to right.

Because we need to be able to accumulate node values on the same level into a
list, we should probably have a hashtable keyed by height that will accumulate a 
list of node values at that level.
"""
def level_order_traversal(root: Optional[Node]) -> list[list[int]]:
    level_values = collections.defaultdict(list)
    if not root:
        return []

    bfs_queue = collections.deque()
    bfs_queue.appendleft((root, 0))

    while bfs_queue:
        node, height = bfs_queue.pop()

        # Process Node
        level_values[height].append(node.value)

        # Enqueue Available Children
        if node.left:
            bfs_queue.appendleft((node.left, height+1))
        if node.right:
            bfs_queue.appendleft((node.right, height + 1))

    ans = list(level_values.values())
    print(ans)
    return ans

def test(fn):
    root = Node(3, Node(9), Node(20, Node(15), Node(7)))
    assert fn(root) == [[3],[9,20],[15,7]]
    root = Node(1)
    assert fn(root) == [[1]]


test(level_order_traversal)
