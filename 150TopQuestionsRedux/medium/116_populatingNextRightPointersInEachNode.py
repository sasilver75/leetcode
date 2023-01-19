from __future__ import annotations

import collections
from typing import Optional

"""
Populating Next Right Pointers in EAch Node

Given a perfect binary tree where all leaves are on the same level,
and every parent has two children.

Populate each next pointer to point to its next right node.
If there's no next right node, it should be set to None.

(This is more like a left-to-right sequence for each layer)
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.value = value
        self.next = None


"""
Possible optimization. 
We don't actually need to build level_nodes to full capacity before
processing each level. We could instead just use a variable that is an 
list collecting the nodes of the latest layer. When we encounter a node from
a new layer, we first process the previous list before creating a new list
and inserting the newset node.
"""


def connect_levels(root: Optional[Node]) -> Optional[Node]:
    if root is None:
        return None
    level_nodes = collections.defaultdict(list)

    # BFS through Tree, putting nodes on their level
    bfs_queue = collections.deque()
    bfs_queue.appendleft((root, 0))

    while bfs_queue:
        node, level = bfs_queue.pop()

        level_nodes[level].append(node)

        if node.left:
            bfs_queue.apppend(node.left)
        if node.right:
            bfs_queue.append(node.right)

    for nodes in level_nodes.values:
        for i in range(0, len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

    return root


def connect_levels_optimized(root: Optional[Node]) -> Optional[Node]:
    if root is None:
        return None

    nodes = []
    nodes_level = -1

    bfs_queue = collections.deque()
    bfs_queue.appendleft((root, 0))

    while bfs_queue:
        node, level = bfs_queue.pop()

        if level > nodes_level:
            # Process Nodes
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]
            # Reset Nodes
            nodes = [node]
            # Set Nodes_Level
            nodes_level = level
        else:
            nodes.append(node)

        if node.left:
            bfs_queue.appendleft(node.left)
        if node.right:
            bfs_queue.appendleft(node.right)

    # Process remaining Nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    return root
