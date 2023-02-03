"""
Course Schedule

There are a total of `numCourses` courses that need to be taken,
labeled from [0, ..., numCourses - 1]

Given an array of prerequisites, where prerequisites[i] = [a,b]
indicates that you must take course b before taking course a
in other words, b is a prerequisite of a.

For example, the pair [0,1] indicates that you must take course 1
before taking course 0.

Return true IF YOU CAN FINISH ALL OF THE COURSES
Otherwise, return False
"""


def process_prerequisites(prerequisites: list[list[int]]) -> dict[str, list[str]]:
    """
    From a list of [course, precourse] two-lists,
    genreate a dict of
    {
        courseA: [prerequisiteCourseOfCourseA, ...]
    }
    """
    prereqs = {}

    for course, precourse in prerequisites:
        if course not in prereqs:
            prereqs[course] = []
        if precourse not in prereqs:
            prereqs[precourse] = []

        prereqs[course].append(precourse)

    return prereqs


# Using an intuitive approach
def can_finish_naive(num_course: int, prerequisites: list[list[int]]) -> bool:
    prereqs = process_prerequisites(prerequisites)

    progress = True

    untaken_courses = set(prereqs.keys())
    taken_courses = set()
    while progress:
        # We have to take at least one course per pass to be able to continue the loop
        progress = False

        # For each course, we can take it if we've taken all prereqs
        courses_taken_this_pass = []  # Using this becuase we can't change the size of untaken_courses during iteration. The alternative is to break out whenever we make progress, meaning we can only make progress n one course per while loop.
        for course in untaken_courses:
            if all(precourse in taken_courses for precourse in prereqs[course]):
                # take the course, record progress
                courses_taken_this_pass.append(course)
                taken_courses.add(course)
                progress = True

        for course in courses_taken_this_pass:
            untaken_courses.remove(course)

    # Did we take all of the courses?
    return len(taken_courses) == num_course


# Using a Topological-Sort type algorithm
# The idea is that if you want to take a course, take all of the courses precourses
# When you "take a precourse", we first have to take all of the courses' precourse.
# Because of the order of recursion, we also need to detect cylces.
# We could have a separate cycle detection algorithm, or we could also
class CycleDetectedError(Exception):
    ...

def can_finish(num_course: int, prerequisites: list[list[int]]) -> bool:
    prereqs = process_prerequisites(prerequisites)

    taken_courses = set()

    def take_precourses_and_course(course, seen: set) -> None:
        if course in seen:
            raise CycleDetectedError("Cycle Detected")
        seen.add(course)

        # Is the course already taken? No work to do, then.
        if course in taken_courses:
            return

        # Take the Precourses
        for precourse in prereqs[course]:
            take_precourses_and_course(precourse, seen.copy())

        # Take the Course
        taken_courses.add(course)

    for course in prereqs.keys():
        try:
            take_precourses_and_course(course, set())
        except CycleDetectedError:
            return False

    return len(taken_courses) == num_course


def test(fn):
    assert fn(2, [[1, 0]]) == True
    assert fn(2, [[1, 0], [0, 1]]) == False  # Cycle detected here

    """
                /1\
        0               3
                \2/
    """
    assert fn(4, [[0, 1], [0, 2], [2, 3], [1, 3]]) == True  # Diamond


test(can_finish_naive)
test(can_finish)
