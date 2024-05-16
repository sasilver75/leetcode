"""
Given the `root` of a binary tree, return the INORDER TRAVERSAL of its nodes values
"""


from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        self.value = value
        self.right = right
        self.left = left


"""
This asks for the INORDER traversal of a binary tree.

Recall the definitions of preorder, inorder, and postorder traversal.
They're all about "when you visit the 'current' node"

Preorder: Visit the current node, then the left subtree, then the right subtree
Inorder: Visit the left subtree, then the current node, then the right subtree
Postorder: Visit the left subtree, then the right subtree, then the current node

"""

def inorder_traversal(root: Optional[Node]) -> list[int]:
    acc = []

    def _inorder_traversal(node: Optional[Node]) -> None:
        """
        Does an inorder traversal starting at node `node`, and appends the values to `acc`
        """
        print(f"Processing Node {node.value if node else 'None'}")
        # Base Case: We were called on a "None" node; there's no additional exploring that needs to happen
        if node is None:
            return
        
        # Inorder Traversal: Left, then current, then Right; We don't need to check if left or right exists, because of our baes case
        _inorder_traversal(node.left) # Recurse left
        acc.append(node.value) # Process current
        _inorder_traversal(node.right) # Recurse right

    # Kick off the recursive process, populating our acc
    _inorder_traversal(root)

    return acc



assert inorder_traversal(Node(1, None, Node(2, Node(3)))) == [1, 3, 2]
assert inorder_traversal(None) == []
assert inorder_traversal(Node(1)) == [1]
