"""
Number of Connected Components in an Undirected Graph
Category: Graph

Given n nodes labeled from 0 to n-1, and a list of UNDIRECTED edges (where
each edge is a pair of nodes), write a function to find the number of
(generally) CONNECTED components in an undirected graph.

Sam Note: It seems like "connected" here means like... how many "islands"
are there in a graph of nodes, where there might be connections between
nodes in this adjacency list.
"""
import collections

"""
Thinking:

# Process edges into an adjacency_dict of { sourceNode: [neighborNode, ...]] }
# Process edges into a remaining_edges set of tuples (for easy removals)

while edge_set:
    # Pop an edge off and fully exploit the island, recursively using the adjacency matrix
    # Remove edges from remaining_edges as they are used. Don't need to modify the adjacency dict
    n_islands += 1
    edge = edge_set.pop()
    
    explore(edge) # Given an edge, recursively DFS explores its island, removing edges from remaining_edges as they're used and adding unseen nodes to seen_nodes

We now have an n_islands, but it's possibel that there were unconnected "floaters" that weren't 
even present in the adjacency list... so we should probably keep track of the encountered nodes as well,
and add to n_islands += len(seen_nodes) - n_nodes

OH, one complication! These are UNDIRECTED edges, so when we process them into
the adjacency matrix, we want to add both a -> b and b -> a.
We don't need to include the mirrors in the edge_set, though -- it won't matter, since
we'll be recursively explorign the entire island anyways.
"""


def number_of_connected_components(n: int, edges: list[list[int]]) -> int:
    neighbors = collections.defaultdict(list)
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)

    """Later, we seem to be using edges as a proxy for "nodes in the graph", so it could also just be a set of all nodes observed in the graph"""
    edges = set(tuple(edge) for edge in edges)
    n_islands = 0
    seen = set()  # Seen Nodes. We can assume that seen nodes have had their edges fully explored.

    def explore(node: int) -> None:
        seen.add(node)

        # Using neighbors, explore all unexplored neighbors of both a and b
        for neighbor in neighbors[node]:
            if neighbor not in seen:
                # One of (node, neighbor) / (neighbor, node) are in edges; remove it
                if (node, neighbor) in edges:
                    edges.remove((node, neighbor))
                if (neighbor, node) in edges:
                    edges.remove((neighbor, node))

                explore(neighbor)

    while edges:
        a, b = edges.pop()
        n_islands += 1  # Since A,B are connected, they're part of the same island
        explore(a)
        explore(b)

    # There may be "floater" islands that didn't have connections. Each of these is an island.
    n_islands += len(seen) - n

    return n_islands


"""
The "number of connected components" is a perfect example of a problem where
the "UNION FIND" algorithm should be employed.  (Also called merge-find sets or disjoint set union)

The Union Find data structure supports two operations (as the name suggests
    - 1) Union(x,y) , unions two groups containing objects x and y
        [0, 2], [1,3] --> union(0,1) --> [0,1,2,3]
        
    - 2) find(x) ,  finds the group that x belongs to.
    
So how do we implement UnionFind?
* Each group has a representative element, which represents the entire group it belongs to,
in the sense that the find function on group members will always return the representative.
* Notice that two elements belong to the same group if and only if they have the same representative.
* Now we need to implement the other function, allowing the union of two groups.
...
We initialize an array called Parent, where Parent[i] gives the parent of object i
Next we implement a function find(x), which finds the root of the tree containing
x.  

def find(x)
    if Parent[x] != x:
        return find(Parent[x])
    return x

def union(x, y):
    Parent[find(y)] = find(x)
    
Let's now discuss the complexity of the algorithm. If a data structure contains
N elements, the height of the tree is Log(N). Since both find and union involve doing
this, the find/union complexities are both log(N). 

Neetcode Explanation:
We're given the edges as a list of edges, but we could make an adjacent matrix and do
a depthfirstsearch through the graph, marking nodes as visited when we visit them, and
counting the number of unique DFSs that we do. This is pretty much waht I did above.

The overall time complexity is basically goin to be O(e+v), since we will have to go
through every edge building teh adjacency matrix, and go through every vertice
doing the DFS.

But there's actually a more natural way of finding this answer using UnionFind. 
This algorithm was literally made to count the number of connected components, and
identifying teh number of disjoint sets, and all that stuff.

We're going to mainly be maintaiing two arrays, one called the Parent array,
where we'll have a value for each node given in the input. The value in 
each index will be initialized to itself. Parent[i] = i means that i is i's parent.

(0)     (1)             (3)

        (2)             (4)
        
Edges: [[0,1], [1,2], [3,4]]
        
Parents = [0,1,2,3,4]

The way union finds work is basically a forest of trees -- we'll have multiple
trees (starting with N trees - 1 for every node in the input), and as we go through
the edges, we're going to glomb/connect trees. Every time we perform one of these
merges, we're taking the number of connected components that we have, and decreasing it by one.

Optimization: We're going to maintain the "rank" of every single component with a 
Rank array. For every component, we'll maintain the SIZE of it. Initially, it's
going to be 1 for all components. 
Since we just made a merge, we'll leave the rank of 1 as it is.... But for the 
parent of the two, that will then be set to 2. So it's kind of the size of the subtree
at that node.

Imagine we had a component

    (0) <- (1)   where 0 is the "leader" of its component (parent of itself)
    
    and we were merging in a (2) node into that component. 
    Would we prefer that the (0) <- (1) subtree be merged into/under the (2)
    node, or vice versa? Here are the options:
    
            (0)                         
         /       \          or      (1) <- (0) <- (2)
       (1)       (2)        
       
    We can see that our options are essentially a tree or a linked list. 
    We'd of course like the tree, since that's shorter to traverse top to bottom
    (LogN instead of N)
    That is to say, it seems like we should choose the one with a higher "Rank"
    as the leader, when considering merging two leaders.
    
    That's the main algorithm :) 
    
    So, Given:
    
    (0)     (1)             (3)

            (2)             (4)
        
Edges: [[0,1], [1,2], [3,4]]
        
Parents = [0,1,2,3,4]
Rank    = [1,1,1,1,1]
N_Components = 5

We pick out the first edge, [0,1] and consider which one we'd like to merge
into the other one. Let's say that 0 is going to be the parent (they have the same
rank).
So 1's parent is going to be set to 0, and 0's rank is going to be increased.

    (0) <-- (1)             (3)

            (2)             (4)
        
 Edges: [____, [1,2], [3,4]]
        
Parents = [0,0,2,3,4]
Rank    = [2,1,1,1,1]
N_Components = 4

Now let's process the second edge, [1,2]

1 is part of 0's component/subtree, so we'll consider the ranks of 0 vs that
of 2.
Specifically, when we do a merge(a,b), we first compare the rank of find(a) vs
the rank of find(b), where find(x) returns the ultimate leader of x's component.
In our case, this is rank[find(1)] vs rank[find(2)]. The former is the larger one,
so (2) will be "merged under" (1)'s component, which is led by (0). 

    (0) <-- (1)             (3)
        <\
           \ (2)             (4)
    This is me attempting to point an arrow from 2 to 1

Edges: [____, ____, [3,4]]
Parents = [0,0,0,3,4]
Rank =    [3,1,1,1,1]
N_Components = 3

Now let's process the remaining edge.

    (0) <-- (1)             (3)
        <\                    ^
           \ (2)             (4)

( Doesn't matter whether 3 or 4 are chosen as parent )
Edges = [___, ___, ___]
Parents = [0,0,0,3,3]
Rank =    [3,1,1,2,1]
N_Components = 2

We're done! :)
"""


def number_components(n: int, edges: list[list[int]]) -> int:
    parents = [i for i in range(n)]
    rank = [1] * n

    def find(n1):
        cur = n1
        while cur != parents[cur]:
            cur = parents[cur]
        return cur

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        # Nodes may already be unioned. If they are, no-op
        if p1 == p2:
            return False  # Union "Not Successful"

        if rank[p1] >= rank[p2]:
            # Merge p2 "under" p1
            parents[p2] = p1  # Set P1
            rank[p1] += rank[p2]  # Absorb P2's rank
        else:
            parents[p1] = p2
            rank[p2] += rank[p1]

        return True  # "Union Successful"

    for edge in edges:
        n1, n2 = edge
        if union(n1, n2):
            n -= 1

    return n


def number_components_reimplementation(n: int, edges: list[list[int]]) -> int:
    """This is just be coming back after going to the movies and drinking a bit, seeing if I can
    reimplement the same logic from above without looking at it. I think I can."""
    # We begin in a state where every node is conceptually in its own tree/component
    parents = [i for i in range(n)]
    rank = [1] * n

    def find(node: int) -> int:
        """Given a node, return the leader of that node's component"""
        cur = node
        while parents[cur] != cur:
            cur = parents[cur]
        return cur

    def union(n1: int, n2: int) -> bool:
        """
        Attempt to union the components of n1 and n2
        Return True if the components were unioned, else False.
        """
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False

        if rank[p1] >= rank[p2]:
            parents[p2] = p1
            rank[p1] += rank[p2]
        else:
            parents[p1] = p2
            rank[p2] += rank[p1]

        return True

    for a, b in edges:
        if union(a, b):
            n -= 1

    return n


def test(fn):
    """
            0           3
            |           |
            1 - 2       4
    """
    assert fn(5, [[0, 1], [1, 2], [3, 4]]) == 2

    """
            0               4
            |               |
            1   -- 2    --  3
    """
    assert fn(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1


test(number_of_connected_components)
test(number_components)
test(number_components_reimplementation)
