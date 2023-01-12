"""
Course Schedule
Difficulty: Medium

There are a total of n courses that you have
to take, labelled from 0 to n-1.

Some course have PREREQUISITES; for example, if prerequites[i] = [a,b],
this means you must take course b[i] before the course a[i].

Given the total number of courses numCourses and a list of the prerequisite
pairs, return the ORDERING of the courses you should take to finish all courses.

If there are many valid answers, return ANY of them.
If it's impossible to finish all courses, return an EMPTY array.
"""
import collections


def course_path_naive(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    taken = []

    # Generate adjacency list
    prereqs = {}
    for courseNum in range(numCourses):
        prereqs[courseNum] = list()

    for course, precourse in prerequisites:
        prereqs[course].append(precourse)

    progress = True
    while progress:
        progress = False
        for course in prereqs:
            # If we can take a course (all prereqs taken) and we haven't yet, take it!
            if all(precourse in taken for precourse in prereqs[course]) and course not in taken:
                taken.append(course)
                progress = True

    return taken if len(taken) == numCourses else []


"""
Now, let's use topological sort!
A topological sort algorithm takes a DIRECTED GRAPH and returns an ARRAY
of the nodes where each node appears before all of the nodes it points to!
 ** Note that there may be multiple valid toplogical orderings 
 ** Note that CYCLIC graphs don't have valid topological orderings!
 
How does topological sort work, again?

Find a node with an in-degree of zero (meaning no prerequisites) and add
it to the topological order.
Once a node is added to the topological ordering, we can take the node, and its outgoing
edges, out of the graph.
Then we can repeat our earlier approach: look for any node with an indegree of zero
and add it to the topological ordering.

This is a common algorithm design pattern:
    1) Figure out how to get the first thing
    2) Remove the first thing from the problem
    3) Repeat


Again:
1) Determine the indegree for each node 
    - An iteration through node-edges
    - O(M) time, where M is the # of edges
2) Find nodes with no incoming edges.
    - A simple loop through the nodes
    - O(N) time, where N is the # of nodes
3) Add nodes to our accumulator (our topological sort) until we run out
of nodes with no incoming edges.
    - This loop could run once for every node -- O(N) times. In the body, we:
        * Do two constant-time operations on an array to add a node to the acc
        * Decrement the indegree for each neighbor of the node we added

4) Check if we included all nodes or found a cycle (O(1) fast comparison)

Altogether, this should be O(M+N) time
This is the fastest time we can expect, since we'll have to look at all
of the nodes and edges at least once.

What about space complexity?
    - indegrees: this one has an entry to each node - O(N) space
    - nodesWithNoIncomingEdges:  In the worst case, in a graph with no edges, starts
    out containing every node, so it's O(N) space
    - topologicalOrdering:  In a cycle-less graph, this will eventually
    have every node. O(N) space.
    
So the overall space complexity is O(N)
The most common nuse for topological sort is ordering steps of a process where
some of the steps depend on eachother!

As an example, the steps of making a chocolate bundt cake, which may have
concurrently-doable steps gated by other steps.



We can take a class if all of its prerequisites can be taken.
"""
def course_path(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # Generate Adjancency list
    prereqs = {}

    # Make sure every course has an entry
    for i in range(numCourses):
        prereqs[i] = set()
    # Populate all prerequisites in adjacency list
    for course, precourse in prerequisites:
        prereqs[course].add(precourse)

    taken_courses = set()
    topological_ordering = []

    def dfs(course: int) -> None:
        """
        Can we take this course and haven't? If so, add it to the topological ordering.
        We can take this course if we HAVE (or CAN) taken/took all of its prerequisites
        """
        if course in taken_courses:
            return

        # Take all prerequisite courses for the current course
        for precourse in prereqs[course]:
            dfs(precourse)

        # Take the current course
        taken_courses.add(course)
        topological_ordering.append(course)

    # Run this process on every course.
    """
    Imagine a directed graph of prerequisites. Imagine the nodes that are touched
    when you invoke DFS -- it's sosrt of a flood-filly series of nodes that are touched.
    We hope that all nodes get touched when we invoke the floody-filly function on all nodes.
    """
    for course in range(0, numCourses):
        dfs(course)

    """Think: How does this function turn out if there are cycles (even not length-1 cycles) or un-takeable classes"""
    print(topological_ordering)
    return topological_ordering if len(topological_ordering) == numCourses else []









def test(fn):
    assert fn(2, [[1,0]]) == [0,1]
    assert fn(4, [[1,0], [2,0], [3,1], [3,2]]) in ([0,2,1,3], [0,1,2,3])  # I got [0, 1, 2, 3]
    assert fn(1, []) == [0]

test(course_path_naive)
test(course_path)