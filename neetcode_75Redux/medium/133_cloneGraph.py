"""
Clone graph

Given a reference of a node in a fully-connected, undirected graph

Return a DEEP COPY (clone) of the graph.

Each node in the graph contains a value (int) and a list (list[Node]) of its
neighbors.
"""
from typing import Optional


class Node:
    def __init__(self, value: int, neighbors: Optional[list] = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node) -> Node:
    if node is None:
        return None

    # A dict of real:clone
    cloned_nodes = {}

    def clone(n: Node) -> Node:
        """
        Given a real node, return the cloned version of it
        """
        # Have we already cloned this node? Return it!
        if node in cloned_nodes:
            return cloned_nodes[node]

        # Create the clone and stick it into our cloned_nodes dict
        clone_node = Node(n.value)
        cloned_nodes[node] = clone_node

        # Populate each of the clone's clone neighbors, using recursion
        for neighbor in n.neighbors:
            clone_node.neighbors.append(clone(neighbor))

        return clone_node




    return clone(node)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

ans = clone_graph(n1)
print(ans)
