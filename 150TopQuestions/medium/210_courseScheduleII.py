"""
Course Schedule II

There are a total of `numCourses` courses that you HAVE to take,
labeled from 0...numCourses-1

You are given an array of prereqs where prereqs[i] = [a,b] where you
have to take b before taking a.

ex: [0,1] indicates that you must take class 1 before class 0.

Return the ORDERING of courses that you need to take in order
to finish all courses! If there are many valid answers, return ANY
of them.
If it is impossible to finish all courses, return an empty array.
"""
from collections import defaultdict

"""
Notes:
It seems like there are courses that have multiple prerequisites (see second example)

I probably want to preprocess this prereqs into a different datastructure.

Option 1:
Process Prereqs into

{
    class:  [prereq, ...]
    ...
}
Noting when generating that there may be classes that exist without prereqs that need to be in there.

And then doing multiple iterations where we ask each class:
* Can I take you, given the classes that I've taken?
    - If yes, add the class to 
* Only when we don't take any new classes for a given iteration loop would we stop, or if we hit the max?

"""
def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    courses_taken = []
    courses_to_prereqs = dict() # course: list[prereq]

    # Create courses_to_prereq lookup
    for course, prereq in prerequisites:
        if course not in courses_to_prereqs:
            courses_to_prereqs[course] = []
        if prereq not in courses_to_prereqs:
            courses_to_prereqs[prereq] = []

        courses_to_prereqs[course].append(prereq)

    alive = True
    while alive and len(courses_taken) < numCourses:
        # If we take any courses, re-evaluate again
        alive = False
        for course in courses_to_prereqs:
            # If I haven't taken the course and I CAN take the course, take it!
            if course not in courses_taken and all(req in courses_taken for req in courses_to_prereqs[course]):
                # Take the course!
                courses_taken.append(course)
                alive = True

    # Were we able to take enough courses? If so, return the list!
    return courses_taken if len(courses_taken) >= numCourses else []

"""
How can we do better than above? In the above, we're going N iterations (where N is the number of classes)
in the worst case in the "alive" loop.
That alive loop is what's pushing us into what might be O(N^3) territory.

I want to be able to preprocess this prerequisites list into a GRAPH
that I can somehow traverse, right? It'd be lovely if we could do this in O(N^2) time
instead.

Neetcode: https://youtu.be/Akt3glAwyfY

We're again given N courses labeled from 0 - N-1
These are basically going to be the NODES in our GRAPH.
This is again a GRAPH problem.
Prerequisites = [[a,b], ...]
Where B is a prerequisite of A.

For all of the courses and all of the rerequisites that are given, we want to
return the ORDER of courses that we would take to finish ALL THE COURSES.

Subtlety: It's possible that we CAN'T take all the courses given the prereqs.

So.
* Generate the graph from the prerequisite pairs
* Attempt to fully traverse the graph (keeping order)

[0,1] really means (0) --> (1) in our graph  (i.e. do (1) before (0))

What if we had both [0,1] and [1,0]? 
That would mean a graph looging ike (0) <--> (1)
Is it possible to take these courses? No!
If there are cycles in the graph of any sort, we can't complete all the courses.

We're going to use Topological Sort, but you don't need to KNOW Topological Sort
in order to solve this problem -- this problem will teach you it!

(5)>          >(1)--->(3)
    \ >(O) > /       /
    /       \     /
(4)>          >(2)</

What we're gonna doo.... 
Starting at every single node, we'll run DepthFirstSeafch DFS on the node.

Starting at node 0. Let's run DFS on it
to do that, we would need to build an adjacency list -- for each node, we 
need to know its neighbors:

    adj             prereq
    0               [1,2]
    1               [3]
    2               []
    3               [2]
    4               [0]
    5               [0]
    
This tells us for each node, which are the prerequisites for this node?
They're also OUTGOING edges from each node in the graph (ie 0 has outgoing edges to 1,2)

We're now going to do DFS at every single node, and the output that we're 
trying to build is the order that we can take courses.

We're considering the node 0 first.
Looking at the graph, we know that we have to take 1 and 2 before 0,
so we know the output for this node will start with 1,2,0, ...

But what's the algorithm?

Starting at 0, we don't update our output yet - we want to take the prerequisites first.
Let's go to ONE of our prerequisites, using the adjacency list/prereq map.
So let's look at the first prereq, 1.
Now, we check: Can we take 1? It has a prerequisite, 3!
So we need to take 3 before we can take 1.
So let's look at 3: Can we take 3? Not yet, it has a prereq of 2!
Looking at 2, we have no prerequisiites! So we can take course 2. 

What does it mean for us that we took this path from
0 -> 1 -> 3 -> 2, and found a node with no prerequisites? We're allowed
to take course 2! We can add it our output.

Output: [2,]

Now let's "CROSS OUT" 2 on our graph and adjacency matrix values, since we
never have to visit it again (take the course again)

Now in our DFS, let's go back to where we came from (3).
Look, 3 doesn't have any more prerequisites!
So we can take 3, add it to our output, and "cross it out" of the graph/adj list

Output: [2,3,]

Now in our DFS, let's again go back to where we came from (1)
1 has no REMAINING prerequisites either! We can take it, cross it out, etc

Output: [2,3,1,]

Now in our DFS let's bubble back to 0.
0 had two prerequisites, but we've taken them both!
So we "take" 0, remove it from adjacency matrices

Output: [2,3,1,0,]

Okay... Now what? We still haven't really considered nodes (5) and (4).
Well in our algorithm, remember that we're running DFS over all nodes

So maybe the next node in our iteration loop of nodes is (1) (because
say, we're iterating from nodes 0...numCourses-1). We look at (1),
and see that it's already visited.
We try to run DFS on (2), see it's already visited.
We try to run DFS on (3), see it's already visited
We try to run DFS on (4), and see that it's NOT already visited.

DFS on 4:
 * Can we take 4? Have we taken all of the prerequisites of 4? Yes.
 * Take 4, "cross it off"

Output: [2,3,1,0,4,]

Next Node iteration loop is for DFS on (5), and we see that it's NOT already
visited.
DFS on 5:
 * Can we take 5? Have we taken all of hte prerequisites of 5? Yes.
 * take 45, "cross it off"
 
Output: [2,3,1,0,4,5] 
 
Node Iteration completes! Yay!
"""


def find_order_smarter(numCourses: int, prerequisite_list: list[list[int]]) -> list[int]:
    # Populate `prerequisites`, an adjacency list of { course : [prerequisites] }
    prerequisites = dict()
    for course, prereq in prerequisite_list:
        if course not in prerequisites:
            prerequisites[course] = []
        if prereq not in prerequisites:
            prerequisites[prereq] = []

        prerequisites[course].append(prereq)

    taken_courses = set()
    course_order = []

    def explore_course(course: int) -> None:
        """
        If you haven't taken this course, take all prereqiusites, then take the current course.
        """
        if course in taken_courses:
            return

        # Q: Is this like a... "post-order DFS" traversal?
        for precourse in prerequisites[course]:
            explore_course(precourse)

        # Take this course if appropriate
        taken_courses.add(course)
        course_order.append(course)

    for c in range(0, numCourses):
        explore_course(c)

    print(taken_courses)
    return course_order if len(taken_courses) == numCourses else []




# -- Test --
def test(fn):
    assert fn(2, [[1,0]]) == [0,1]
    assert fn(4, [[1,0], [2,0], [3,1], [3,2]])

test(find_order)
test(find_order_smarter)
