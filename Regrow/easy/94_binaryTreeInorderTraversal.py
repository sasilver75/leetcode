"""
Given the root of a binary tree, return the
INORDER TRAVERSAL of its nodes values!

Recall: Preorder, Inorder, Postorder

Inorder:
1. Traverse the left subtree
2. Visit the root
3. Traverse the right subtree
Uses: In the case of a BinarySearchTree BST, inorder traversal gives
nodes in a NON-DECREASING order (asc).
If you wanted to get the nodes of BST in a NON-INCREASING order, a reverse of
inorder traversal can be used.

Preorder:
1. Visit the root
2. Traverse the left subtree
3. Traverse the right subtree
Uses: Can be used to create a copy of the tree. Also to get prefix expressions on an expression tree.

Postorder:
1. Traverse the left subtree
2. Traverse the right subtree
3. Visit the root
Uses: Used to delete trees. Also useful to get the postfix expression of an expression tree.
"""


class BSTNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder_traversal(root: BSTNode) -> list[int]:
    acc = []
    helper(root, acc)
    return acc

def helper(node: BSTNode, acc: list):
    if not node:
        return

    if node.left:
        helper(node.left, acc)
    acc.append(node.value)
    if node.right:
        helper(node.right, acc)


# Case One
root1 = BSTNode(1)
root1.right = BSTNode(2)
root1.right.left = BSTNode(3)
print(inorder_traversal(root1)) # Should be [1,3,2]

# Case Two
root2 = None
print(inorder_traversal(root2)) # Should be []

# Case Three
root3 = BSTNode(1)
print(inorder_traversal(root3)) # Should be [1]
