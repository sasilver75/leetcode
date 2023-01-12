class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postorder(node: BSTNode) -> None:
    if not node:
        return

    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.value)



h1 = BSTNode(1)
n2 = BSTNode(2)
n3 = BSTNode(3)
h1.right = n2
n2.left = n3

postorder(h1) # 3, 2, 1
print("--")
postorder(None)
print("--")
postorder(BSTNode(1)) # 1