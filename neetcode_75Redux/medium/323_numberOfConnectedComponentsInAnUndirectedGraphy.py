"""
Number of Connected Components in an Undirected Graph

You have a graph of n nodes.

You are given an integer n and an array edges, where edges[i] = [a,b] indicates that there is an undirected edge betweeen
a and b in the graph.

Return the number of connected components in the graph.

NOTE: You can assume that no duplicate edges will appear in edges.
NOTE Since all edges are undirected, [0,1] == [1,0], both will not appear together in edges.
"""

"""
This problem (number of connected components in a graph) should be solved by the Union Find algorithm

The Union Find data structure supports two operations:
    1) Union(x, y) : unions two groups containing objects x and y
            [0, 2], [1,3] --> union(0,1) --> [0,1,2,3]
    
    2) Find(x) : find the group that x belongs to
            (Specifically, given a node x, return the representative element from the group x is a part of)
    

So how do we implement UnionFind?
- Each group has a representative element, which represents the entire group it belongs to, in the sense that when we
invoke the Find function on any element within the group, the representative element of the group is returned.
    * Note that two elements belong to the same group IFF they have the same representative

-

"""


def number_of_connected_components(n: int, edges: list[int]):
    # Create a dict (or array, if you wanted), mapping       node: representativeNodeOfNodesGroup
    parents = {
        node: node
        for node in range(n)
    }

    # Create an adjacency matrix
    # TODO: Can I use a defaultdict instead? Is it a problem that unconnected nodes wouldn't be in the adjacency list?
    adjacents = {}
    for a, b in edges:
        if a not in adjacents:
            adjacents[a] = []
        if b not in adjacents:
            adjacents[b] = []
        adjacents[a].append(b)
        adjacents[b].append(a)

    def find(n: int) -> int:
        """Return the representative element of the group containing n"""
        current = n
        while parents[current] != current:
            current = parents[current]
        return current

    def union(x: int, y: int):
        parents[y] = x

    for node in adjacents:
        for neighboring_node in adjacents[node]:
            # Consider adjacent nodes;
            node_leader = find(node)
            neighboring_node_leader = find(neighboring_node)
            if node_leader != neighboring_node_leader:
                union(node_leader, neighboring_node_leader)

    # count the number of nodes in parents that are their own parent, meaning
    # of which there is one per group
    groups = 0
    for node in parents:
        if parents[node] == node:
            groups += 1

    return groups


"""
An alternative way is to build the adjacency matrix, and do a DFS through the graph
for each node, recursing through unvisited nodes, marking them as visited, and counting
the number of DFSs that we do.
"""


def number_of_connected_components_dfs(n: int, edges: list[int]):
    # Create our adjacency matrix
    neighbors = {node: [] for node in range(n)}
    for a, b in edges:
        # Populate the bidirectional edge
        neighbors[a].append(b)
        neighbors[b].append(a)

    visited_nodes = set()

    def dfs(node: int) -> None:
        if node in visited_nodes:
            return

        visited_nodes.add(node)
        for neighboring_node in neighbors[node]:
            dfs(neighboring_node)

    group_count = 0

    # Apply DFS across all unvisited nodes, at the top level, inc group_count
    for node in range(n):
        if node not in visited_nodes:
            group_count += 1
            dfs(node)

    return group_count



def test(fn):
    assert fn(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert fn(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1


test(number_of_connected_components)
test(number_of_connected_components_dfs)
