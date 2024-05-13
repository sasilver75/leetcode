"""
https://www.youtube.com/watch?v=utDu3Q7Flrw

Top 5 Most Common Graph Algorithms for Coding Interviews
"""


"""
1. Depth First Search (DFS) ***************************************

Time: O(N), where N is the number of nodes in the graph.
Data Structures: Hash Set (+)
If you're doing this recursively, you won't need a stack, because the recursion
handles that for you -- but if you're doing this iteratively, you may use a 
also use a stack to keep track of the order of exploration of nodes.

            A
        B       E
    C     D

Output: ABCDE  (Using Prefix DFS)
    
This looks like a tree -- and it is! Trees are just special cases of graphs (DAGs) with
ever node having maximum one parent.

"""

"""
2. Breadth First (BFS) ***************************************
Time: O(N)
Data Structures: Queue (Double-Ended)

Usually not implemented recursively, but iteratively using a Queue.
There could be a cycle in the graph, so if we don't want to be stuck in a loop,
we need to avoid that by using a HashSet to detect duplicate nodes.

            A
        B       E
    C     D

Output: ABECD
Traverses the graph "layer by layer" (A, BE, CD)
"""


"""
3. Union Find ***************************************

Used to "Union Together" disjoint sets in a graph and combine them efficiently
(think finding the number of islands/"connected components" in a graph)

        B       G       F
        |               |           N: connected components == 3
        C ---- D        E           

Time: O(NlogN)
Data Structures: a "Forest of Trees"
    - Usually have to implement it yourself! :)

See: #323 Number of Connected Components in Undirected Graph
"""

"""
4. Topological Sort ***************************************

One of the more difficult ones, and more obscure.
Built on top of Depth-First-Search!

Given a Directed, acyclical graph, the topological sort of a graph would be
reading every single node in the graph, and printing those values out in
such an order that (when we print "D", every node that "comes before it" in 
the dag has already been printed.

    />  B  >  \
A               >   D >   E
    \>  C  >  /
    
Topological sorts aren't necessarily unique; there are actually TWO in the 
graph above:
A -> B -> C -> D -> E
A -> C -> B -> D -> E
    
Time: O(N)
Data Structures: Hash Set (since we're doing DFS)
If we're doing it recursively, the HashSet would be the only data structure needed,
else you might want to use a stack.

See: #269 Alien Dictionary
"""


"""
5. Djikstra's Shortest Path Algorithm ***************************************

Rarely asked about in interviews
We want to find teh shortest path from some starting node A to every 
other node in the graph (B, C, D, E)

    1/>  B  >  \5
A               >   D  1>   E
    2\>  C  >  /2

Unlike other graphs in the previous examples, the edges in graphs that we'd
use Djikstra's algorithm for may be weighted, indicating the cost of travel
between nodes

Time: Elog(V)  where E=#Edges, V=#Vertices
Data Structures: Heap/PriorityQueue is usually used to find the shortest path,
since we're curious about looking at the minimum edge, etc. We also don't want
to get stuck in a cylce, so a HashSet is also often used.

The algorithm involves greedily "exploring" the cheapest edge that's available
to us, from the nodes that we've gotten to, and marking down the cost to get
to nodes as we arrive at them.

See: #743 Network Delay Time
"""