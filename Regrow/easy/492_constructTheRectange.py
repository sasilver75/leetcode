"""
Construct the Rectangle

A web developer needs to know how to design a web page's size.
So... given a specific rectangular web page's area, your job is to
now design a rectangular web page whose length L and width W satisfy
the following requirements:

1) The area of the rectangular web page you designed must equal
the given target area.
2) The width W should not be larger than the length L, which means L >= W
3) The difference between L and W should be as small as possible.

Return an array [L, W] where L and W are the length and width of the web
page you designed in sequence
"""

"""
Thinking:

Dumb Soln:
For the given A, generate all pairs of [L, W] that equal A
and then loop through those pairs and select 
the one that is (valid) and (optimal)
"""

def rectangle(area: int) -> list[int]:
    pairs = []
    # Because of the L >= W constraint, we just need to walk W up to the
    # halfway point, and L down to W a few times

    width = 1
    length = area
    while width <= length:
        while length >= width:
            if length * width == area:
                pairs.append((length, width))
            length -= 1

        length = area
        width += 1

    pairs_with_distance = [(length - width, (length, width)) for length, width in pairs]
    min_pair = min(pairs_with_distance, key=lambda tup: tup[0])[1]
    return list(min_pair)


# assert rectangle(4) == [2, 2]
# assert rectangle(37) == [37, 1]
# assert rectangle(122122) == [427, 286] # This highlights than an O(N^2) will not work well


"""THIS IS THE SOLUTION TO THIN ABOUT!"""
def construct_rectangle(area: int) -> list[int]:
    """
    Since L >= W, the closest we can get is L = W, L*W == L*L == L**2
    And if, at L's largest, L**2 is supposed to equal A, we can say that
    L at its largest is going to be L = floor(sqrt(A))

    On the other end, L is never going to be zero, since X * 0 = 0 for all X
    and X isn't an area :)

    When looking for a common multiplicand W in W * L = A
    We can rearrange to W = A / L
    Since W can only be a natural number (pos int), we have a
    candidate L only when A % L == 0 (when you can "cleanly" divide it)


    """
    for w in range(int(area ** .5), 0, -1):
        if area % w == 0:
            return [int(area / w), int(w)]


assert construct_rectangle(4) == [2, 2]
assert construct_rectangle(16) == [4,4]
assert construct_rectangle(18) == [6, 3]
assert construct_rectangle(37) == [37, 1]
assert construct_rectangle(122122) == [427, 286]