"""
Course Schedule II

There are a total of `numCourses` courses that you have to take, labeled from 0
to numCourses - 1.

You're given an array `prerequisites`, where preqreuisites[i] = [a,b] indicates
that you need to take b before taking a. IE "a's prerequisite is b"

Return the _ORDERING OF COURSES_ you should take to finish all courses.
If there are many valid answers, return any of them. If it's imposslbe
to finish all courses, return an empty array.
"""


def get_prereqs(prerequisites: list[list[int]]) -> dict[int, list[int]]:
    """
    Generate an adjacency list of courses and their precourses
    :param prerequisites: A list of [a,b] elements where b is a preerq of a
    :return: A dict of course: [precourse, ...] for all courses in prerequisites
    """
    prereqs = {}
    for course, precourse in prerequisites:
        if course not in prereqs:
            prereqs[course] = []
        if precourse not in prereqs:
            prereqs[precourse] = []

        prereqs[course].append(precourse)

    return prereqs


def find_order_naive(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    prereqs = get_prereqs(prerequisites)

    course_order = []
    taken_courses = set()

    should_continue = True  # is there a better name for this?
    while should_continue:
        """
        For every course that we haven't taken, take the ones that we can take (all prereqs satisfied)
        """
        should_continue = False
        for course in prereqs.keys():
            if course not in taken_courses and all(precourse in taken_courses for precourse in prereqs[course]):
                taken_courses.add(course)
                course_order.append(course)
                should_continue = True

    print(course_order)
    return course_order if len(course_order) == numCourses else []


"""
Okay, now let's do it using topological sorting. In this case,
for every class in prereqs, we first take all of the prereqs, then take the course.

One thing we have to do is look out for cycle, though.
Let's add that afterwards.
"""
class CycleDetectedError(Exception):
    pass

def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    prereqs = get_prereqs(prerequisites)
    course_order = []
    taken_courses = set()

    def take_course(course: int, seen: set) -> None:
        # Cycle Detection bolted on at the end :)
        if course in seen:
            raise CycleDetectedError(f"Cycle detected at {course}, {seen}")
        seen.add(course)

        # Have we already taken the course? Then we're good!
        if course in taken_courses:
            return

        # Take da untaken Prereqs
        for precourse in prereqs[course]:
            if precourse not in taken_courses:
                take_course(precourse, seen)

        # Take da course
        taken_courses.add(course)
        course_order.append(course)

    for course in prereqs:
        try:
            take_course(course, set())
        except CycleDetectedError:
            return []

    print(course_order)
    return course_order if len(course_order) == numCourses else []


# -----

def test(fn):
    assert fn(2, [[1, 0]]) == [0, 1]
    assert fn(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in [[0, 1, 2, 3], [0, 2, 1, 3]]
    assert (fn(4, [[0, 1], [1, 2], [2, 3], [3, 0]])) == [] # Cycle


# test(find_order_naive)
test(find_order)
