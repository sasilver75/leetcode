"""
Course Schedule
Category: Medium

There are a total of `numCourses` courses you have to take, labeled from
0 to numCourses - 1.

 You are given an array `prerequisites` where
`prerequisites[i]` = `[a,b]` indicates that you must first take class
`b` before taking `a`.

Return `true` if you can finish all classes. Otherwise, return false.
"""
import collections


def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    I was thinking that this was a topological sort problem, but maybe that's a little
    bit of an extension of what this actually is.

    Given [a,b], if we consider this instead as a directed edge from B to A,
    (meaning after B, you can take A), then this creates a directed graph.

    There cannot be any cycles in the directed prerequisite graph if we want
    it to be completable...
    """
    prereqs = {i: set() for i in range(numCourses)}
    for course, precourse in prerequisites:
        prereqs[course].add(precourse)

    taken = set()
    progress = True
    while progress:
        progress = False
        for course in range(numCourses):
            # If we haven't taken this course but we've taken all of its prereqs
            if course not in taken and (
                    all(precourse in taken for precourse in prereqs[course])
                    or len(prereqs[course]) == 0
            ):
                # Take the course!
                taken.add(course)
                progress = True

    return len(taken) == numCourses


"""
Does NeetCode have a better solution?
https://www.youtube.com/watch?v=EgI5nU9etnU

You can solve this using either DFS or BFS, but we're going to do a DFS solution.

Given Prerequisites:
    [[0,1], [0,2], [1,3], [1,4], [3,4]]
and N = 5

Graphically:

    (0) ->  (1) ->  (3)
     |        |       |
     v        |       v
    (2)       >----->(4)
    
We've drawn the edges as they appear in the `prerequisites` list.
Our goal here... for each of these nodes, can we complete this course or not?

How do we know if a course can be completed?
Looking at this picture, 0 has a prerequisite of 2 (and 2 has no prerequisites)
                        0 also has a prereqs of 1, which has 2 prereqs (3, 4)
                        3 has 1 prereq, of 4
                        4 has no prereqs
                        
In some sense, 2 and 4 are kind of our base cases: We don't have any
prerequisites for these classes.
We can a hashmap to store these relationships regarding prerequisites:

{
    course: [prerequisites]
}

So we'll interpret our list of prerequisites to:

{
    0: [1,2],
    1: [3,4],
    2: [],
    3: [4],
    4: []
}
NOW we're going to run DFS on every single node -- let's just do it in the 
order of 0 - n-1. 
How do we do DFS? We have our prereq map; We do it recursively.

For 0:
    Look at 0's prerequisites, and see that it has [1,2]
    So we run DFS on 1
    We look at 1's prereqs, and see that it has [3,4]
    So we run DFS on 3
    We now want to know if we can complete course 3; It has one prerequisite, 4.
    So we run DFS on 4
    We look at Course 4, and want to know if we can complete its prerequisites.
    We look at 4's prerequisites, and see that it's empty. So we know that Course 4
    CAN be taken. Yay!
    Now we bubble back...
    
So TLDR, a course can be taken if all of its prerequisites can be taken.
We know a course can be taken when it ha

But what about the problem of "cycles" of prerequisites?
How would that manifest itself? Usually, we'd be looking for a connection
to a class that we've already visited... 

Imagine that we have (0) -> (1) -> (2) -> (0)    ... a cycle!
So imagine we initially did DFS(0, set())
and then we called DFS(1, {0}) and then called DFS(2 {0, 1})
then we'd look and see that 0 is a neighbor. Before calling DFS on it, 
we check that 0 isn't in our visited list. If it is, then we have a cycle!
"""

def can_finish_neetcode(n_courses: int, prerequisites: list[list[int]]) -> bool:
    # Make sure all courses are present as keys, even if they don't have prereqs
    prereqs = {i: set() for i in range(n_courses)}
    for course, precourse in prerequisites:
        prereqs[course].add(precourse)

    def dfs(course: int, visited: set):
        """Can we take this course?"""

        # If there are no prerequisites, then yes
        if not prereqs[course]:
            return True

        visited.add(course)

        # Check for cycles :O
        if any(precourse in visited for precourse in prereqs[course]):
            return False

        # Otherwise, if we can take all the prerequisites, then yes
        return all(
            dfs(precourse, visited.copy()) for precourse in prereqs[course]
        )

    # For every course: Can we take this course? If not, return False.
    for course in range(n_courses):
        if not dfs(course, set()):
            return False


    return True




def test(fn):
    assert fn(2, [[1, 0]]) == True
    assert fn(2, [[1, 0], [0, 1]]) == False  # There's a cycle here


test(can_finish)
test(can_finish_neetcode)