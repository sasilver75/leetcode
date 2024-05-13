from __future__ import annotations
from typing import Optional

"""
Given the ROOT of a binary tree, return the length of the diameter of the tree.
The DIAMETER of the binary tree is the length of the longest path between any two nodes of the tree.
The path may or may not pass through the root.

                        1
            2                       3
        4       5

    Ans: 3, which is the length of the path [4,2,1,3] or [5,2,1,3]
"""

"""
Thinking:
Is the answer not just the length of the max left subtree depth plus the length of the max right subtree depth?
Not quite -- Consider a thing like this:

                            1
                2                       9
            3      6
         4           7
       5
In this case it's the path that's running through [5,4,3,2,6,7,8], which isn'it through the root. 
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


""""
                        1
            2                       3
        4       5

ans = 3 -> [4, 2, 1, 3]
Max depth of left = 2 [1,2,4]
Mad depth of right = 1 [1,3]
"""

"""
It's important to note that the diameter of the BST
can be defined at some point by the max depth of left subtree
plus the max depth of the right subtree, BUT it's not 
true that the diameter need go through the root!

So we need to calculate the diameter at each node
and find the maximum diameter.
https://leetcode.com/problems/diameter-of-binary-tree/discuss/1515564/Python-Easy-to-understand-solution-w-Explanation
"""

class Solution:
    def __init__(self):
        self.diameter = 0 # Stores max diameter calculated

    def depth(self, node: Optional[Node]) -> int:
        """
        1) Calulates the maximum depth of the left and right sides of the given node
        2) Determines the diameter @ current node + update self.diameter if necessary
        """
        left_depth = self.depth(node.left) if node.left else 0
        right_depth = self.depth(node.right) if node.right else 0

        current_diameter = left_depth + right_depth

        if current_diameter > self.diameter:
            self.diameter = current_diameter

        return 1 + max(left_depth, right_depth)


    def diameter_of_tree(self, root: Optional[Node]) -> int:
        self.depth(root)
        return self.diameter

# Case 1
root = Node(1, Node(2, Node(4), Node(5)), Node(3))
print(Solution().diameter_of_tree(root)) # 3


# Case 2
root = Node(1, None, Node(2))
print(Solution().diameter_of_tree(root)) # 1

print(Solution().diameter_of_tree(Node(1))) # 0