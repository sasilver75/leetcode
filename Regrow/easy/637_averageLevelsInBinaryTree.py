from __future__ import annotations
from typing import Optional
"""
Given the ROOT of a binary there, return the AVERAGE VALUE OF THE NODES
ON EACH LEVEL in the form of an array!



                    3
            9               20
                        15      7

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]



                    3
            9               20
        15      7

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
"""

def average_levels(root: Node):
    levels = {}
    if root:
        explore(root, 0, levels)

    # The below comprehension assumes that keys are inserted into levels in level-order, which is true for us
    # There are also no "holes" in levels. If key "4" is in levels, "3...0" are as well
    level_averages = [sum(levels[k])/len(levels[k]) for k in levels]
    return level_averages

def explore(node: Node, level: int, levels: dict) -> None:
    if not level in levels:
        levels[level] = []
    levels[level].append(node.value)

    if node.left:
        explore(node.left, level + 1, levels)
    if node.right:
        explore(node.right, level + 1, levels)



class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


# Case 1
root = Node(3, Node(9), Node(20, Node(15), Node(7)))
assert average_levels(root) == [3, 14.5, 11]

# Case 2
root = Node(3, Node(9, Node(15), Node(7)), Node(20))
assert average_levels(root) == [3, 14.5, 11]



