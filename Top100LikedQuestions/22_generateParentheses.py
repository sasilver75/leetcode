"""
Generate Parentheses

Given n pairs of parentheses, write a fn to generate ALL COMBINATIONS
of WELL-FORMED PARENTHESES


"""

""""
Okay, so how do we think about this?
Do we think about that there's a number of remaining openers and closers?
Do we just think about a single number?
What does it mean for there to be a valid parentheses?
    - I think a parens string of a single parens is valid if there aren 

"""

def generate_parentheses(n: int) -> list[str]:
    ways = []

    def explore(openers: int, closers: int, built: str) -> None:
        if openers == 0 and closers == 0:
            ways.append(built)
            return

        # Can we use an opener?
        # We can if we have openers_remaining
        if openers:
            explore(openers - 1, closers, built+"(")


        # Can we use a closer?
        # We can if closers_remaining > openers_remaining
        if closers > openers:
            explore(openers, closers - 1, built+")")

    explore(n, n, "")

    print(ways)
    return ways



def test(fn):
    a1 = fn(3)
    assert all(p in a1 for p in ["((()))","(()())","(())()","()(())","()()()"])

    a2 = fn(1)
    assert a2 == ["()"]

test(generate_parentheses)
