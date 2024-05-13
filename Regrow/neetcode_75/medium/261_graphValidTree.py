"""
Graph Valid Tree
Category: Graph

Given n nodes labeled from 0 to n-1 and a list of UNDIRECTED edges (each
edge is a pair of nodes), write a function to check whether these edges
make up a valid TREE.
"""
import collections

"""
Thinking:
What's needed in order for a graph to be a valid tree?
All edges need to be connected (ie # of connected components == 1) AND
there need to be no cycles in the graph.

"""


def number_connected_components(n: int, edges: list[list[int]]) -> bool:
    # Use UnionFind to confirm that there is only one connected component
    parents = [i for i in range(n)]
    ranks = [1] * n

    def find(n: int) -> int:
        """Who's the leader of node n's component?"""
        cur = n
        while parents[cur] != cur:
            cur = parents[cur]
        return cur

    def union(n1: int, n2: int) -> bool:
        """Attempt to union n1 and n2's components;
        return true if you needed to"""
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False

        if ranks[p1] >= ranks[p2]:
            parents[p2] = p1
            ranks[p1] += ranks[p2]
        else:
            parents[p1] = p2
            ranks[p2] += ranks[p1]

        return True

    for a, b in edges:
        if union(a, b):
            n -= 1

    return n


def contains_cycle(edges: list[list[int]]) -> bool:
    # Use DFS + Hashset to detect a cycle. This graph is undirected though...
    adjacency_matrix = collections.defaultdict(list)
    for a, b in edges:
        adjacency_matrix[a].append(b)
        adjacency_matrix[b].append(a)

    def contains_cycle_helper(node: int, used: set[tuple[int, int]], starting_node: int) -> bool:
        # TODO: Maybe instead of keeping track of the nodes we've visited, we keep track of the edges that we've used...
        # And if we're able to get back to our starting node without reusing edges, we have a cycle?
        if used and node == starting_node:
            return True

        for neighbor in adjacency_matrix[node]:
            if (node, neighbor) not in used and (neighbor, node) not in used:
                new_used = used.copy()
                new_used.add((node, neighbor))
                new_used.add((neighbor, node))

                if contains_cycle_helper(neighbor, new_used, starting_node):
                    return True

        return False

    for node in adjacency_matrix:
        if contains_cycle_helper(node, set(), node):
            return True

    return False


def is_valid_tree(n: int, edges: list[list[int]]) -> bool:
    n_components = number_connected_components(n, edges) == 1
    has_cycle = contains_cycle(edges)

    return n_components == 1 and not has_cycle


def test(fn):
    assert fn(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
    assert fn(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False  # Cycle in 1 -> 2 -> 3 -> 1


test(is_valid_tree)
