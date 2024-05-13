"""
Course Schedule

There are a total of `numCourses` courses that you have to take,
labeled from 0 to numCourses - 11.

You're given an array `prerequisites` where `prerequisites[i] = [a,b]` indicates
that you need to take b before taking a.

For example, the pair [0,1] indicates that to take course 0, you have
to take course 1 first.

Return true if you can finish all courses. Otherwise, return false.
"""

def generate_prereqs(prerequisites: list[list[int]]):
    """
    Generates an adjacency list of prerequisite courses, where the keys are courses, and the values are lists of courses
    :param prerequisites: [[a,b],...] where [a,b] means b is a prerqeuisite of a, ie "a requires b"
    :return: dict{course: [prereq, ...]}
    """
    prereqs = {}
    # In order to make sure every course is in prereqs, we're not going to use a defaultdict
    for course, precourse in prerequisites:
        if course not in prereqs:
            prereqs[course] = []
        if precourse not in prereqs:
            prereqs[precourse] = []

        prereqs[course].append(precourse)

    return prereqs



def can_finish_naive(num_courses: int, prerequisites: list[list[int]]) -> bool:
    prereqs = generate_prereqs(prerequisites)

    courses_taken = set()
    progress = True
    while progress:
        progress = False
        for course in prereqs:
            # If we haven't taken a course, and we CAN take it (all prereqs taken)
            if course not in courses_taken and all(precourse in courses_taken for precourse in prereqs[course]):
                courses_taken.add(course)
                progress = True

    return len(courses_taken) == num_courses

""""
What's the actual way we do this one?
I think this is an example of a Topological Sort, which is a possible
route through a directed graph.

The way it works is just that you iterate through all of the keys in prereqs..
And for each course, you do:
    - For each of the course's prerequisites, if we haven't taken the prerequisite,
    take the prerequisite (recursive call to take all of that course/s prerequisites)
    
One thing to look out for though is cycles in the course requirements!
We can run a separate cycle detection step before the course_taking step if need be.
"""
class CycleDetectedError(Exception):
    pass

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    prereqs = generate_prereqs(prerequisites)
    courses_taken = set()

    # Take the course. Before taking a course, make sure that we've taken all of
    # the precourses of the course. Integrated into this is the idea of keeping track of
    # all of the courses that we've seen, and detecting any cycles.
    def take_course(course: int, visited: set):
        if course in visited:
            raise CycleDetectedError("Cycle Detected")
        visited.add(course)
        for precourse in prereqs[course]:
            if precourse not in courses_taken:
                take_course(precourse, visited.copy())
        courses_taken.add(course)

    for course in prereqs:
        try:
            take_course(course, set())
        except CycleDetectedError:
            return False

    return len(courses_taken) == num_courses




def test(fn):
    assert fn(2, [[1, 0]]) == True
    assert fn(2, [[1, 0], [0, 1]]) == False  # Cycle, can't
    assert fn(6, [[1, 0], [2, 1], [3, 1], [4, 2], [5, 3], [5, 4]]) == True  # Sam Example

test(can_finish_naive)
test(can_finish)
