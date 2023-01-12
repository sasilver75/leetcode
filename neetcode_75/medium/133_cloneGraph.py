from __future__ import annotations

from typing import Optional

"""
Clone Graph
Category: Medium

Given a reference to a node in a connected UNDIRECTED graph

Return a DEEP COPY (clone) of the graph

Each node in the graph contains a value (int) and a list (List[Node])
of its neighbors
"""


class Node:
    def __init__(self, value: int, neighbors: Optional[list[Node]] = None):
        self.value = value
        self.neighbors = neighbors or []

"""
        1  ---  2
        |       |
        3  ---  4

        Process the Node 1
            - Map the Old Node to the New Node
            - Look at neighbors...say Node2
            - Recurse on Node 2
                - Map Node2 to CloneNode2
                - Look at neighbors... say Node1
                    - We TRY to clone Node1, but we see in oru hashmap
                    that we already ended up cloning Node1, so we update
                    our Node2 analogue to point at Node1 analogue via neighbors
                - Next neighbor... say Node 4
                    - We add Node4:Node4Clone to analogues

        """
def clone_graph(node: Node) -> Node:
    if node is None:
        return None

    # These are nodes that we've processed
    analogues = {} # Node: Analogue  (ie Old: New)

    def clone(n: Node):
        print("Called")
        if n in analogues:
            return analogues[n]

        analogue = Node(n.value)
        analogues[n] = analogue

        for neighbor in n.neighbors:
            analogue.neighbors.append(clone(neighbor))

        return analogue

    return clone(node)


# -- Test Zone --
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.neighbors = [b, c]
b.neighbors = [a, d]
c.neighbors = [a, d]
d.neighbors = [b, c]
copy = clone_graph(a)

a = Node(1)
copy = clone_graph(a)

assert clone_graph(None) == None
