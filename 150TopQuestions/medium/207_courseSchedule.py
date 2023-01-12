"""
Course Schedule

There are a total of `numCourses` courses you have to take,
labeled from 0 to numCourses - 1.

You are given an array of `prerequisites` where `prereq[i] = [ai,bi]`, indicating
that you must take course bi first if you want to take course ai.

For example, the pair [0,1] indicates that to take course 0, you have to take
course 1.

Return true if you can finish all courses. Otherwise, return false!
"""


"""
These examples are kind of pathetic -- Can I generate a better one?
Are there courses without prerequisites? I suppose I wouldn't know about them.

What if a class has two prerequisites? How would that be expressed?

I think I want to preprocess the prerequisites into a dict where the keys
"""

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    # Assuming courses and prereqs are 1:U(0,1)
    course_set = set([num for lst in prerequisites for num in lst])
    pre_requisited = {p[0] for p in prerequisites}
    takeable = course_set - pre_requisited


    course_lookup = {k:v for v,k in prerequisites} # If you take K, you can take V


    finishable = 0
    while takeable:
        next_takeable = set()
        for course in takeable:
            finishable += 1
            next_course = course_lookup.get(course, None)
            if next_course:
                next_takeable.add(next_course)

        takeable = next_takeable

    return finishable >= num_courses


# -- Test Zone --
def test(fn):
    assert fn(2, [[1, 0]]) == True
    assert fn(2, [[1, 0],[0, 1]]) == False

test(can_finish)