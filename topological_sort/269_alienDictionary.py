"""
Alien Dictionary
Difficulty: Hard

There is a new alien language which uses the latin alphabet!

However the order among letters are unknown to you!

You receive a list of NON-EMPTY words from the dictionary, where words
are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language!

Notes:
    * You may assume that all letters are in lowercase.
    * You may assume that if a is a prefix of b, then a must appear
    before b in the given dictionary.
    * If the order is invalid, return an empty string.
    * There may be multiple valid orderings of the letters; returning any
    one of them is fine.
"""

"""
Knowing that this were a topological sorting... What would the graph look like?
I suppose the graph would include a node for all of the characters...
and a directed edge from (B) --> (A) would mean that B "comes after" A 
[in other words, a is a prerequisite of b, in the parlance of CourseScheduleII]
In that case, a toplogical ordering would result in ABCD... which is what we'd 
want for the Alien Language.

Okay, but how do we populate the edges of this graph, which we could then turn
into an adjacency matrix?

What if we were given two strings from the list... what could we tell from them?
[These strings not NECESSARILY be directly adjacent!]
These are from the first example...

"wrf"
"er"
In this case we know that E comes after W   [E W]

What about 
"wrt"
"wrf"
We know that F comes after B  [B, F]

So we can compare each string to each string following it and try to generate as
many edges as possible. Many of these comparisons will be a No-Op, which is fine.
    --> Optimization: Once we hit our first No-Op, we don't have to continue?
            - edit: I don't think we can actually do this optimization, see below

We turn our edges into an adjacency matrix.
We run a topological sort on the adjacency matrix

We check that the length of the topological sort is the length of the # of characters?...
But what about the example of the invalid topological sort? I guess we detect that
when we're generating the adjacency list...which means we have to check every following
word in the dictionary (True O(N^2))  
"""


def alien_dictionary(words: list[str]) -> str:

    def generate_edges(words: list[str]) -> list[int]:
        edges = set()

        def compare_strings(s1: str, s2: str) -> None:
            """
            :param s1: The earlier string
            :param s2: The later string
            :return:
            """
            p1, p2 = 0, 0
            while p1 < len(s1) and p2 < len(s2) and s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1

            # Nothing to learn here
            if p1 == len(s1) or p2 == len(s2):
                return

            # Otherwise, we can learn something!
            # The character at s2[p2] is necessarily "later" in the alien alphabet than the one at s1[p1]
            edges.add((s2[p2], s1[p1]))  # Meaning c2 first requires c1 in the alien alphabet

        # Try to learn what we can by comparing every alien word with every other alien word
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                compare_strings(words[i], words[j])

        return edges

    # How many characters are there, anyways?
    characters = set()
    for word in words:
        for char in word:
            characters.add(char)
    n_characters = len(characters)

    # Generate Edges
    try:
        edges = generate_edges(words)
    except ValueError:
        # A cycle was detected!
        return ""
    print(edges)

    # Generate adjacency matrix
    prechars = {}
    for char in characters:
        prechars[char] = set()

    for char, prechar in edges:
        prechars[char].add(prechar)

    def contains_cycle(edges: list[tuple]) -> bool:
        """This im leaving unimplemented, but you basically keep track of your starting node and only take unused edges,
        checking to see if you can get back to the starting node."""
        def dfs(char: str, visited: set(tuple[str, str])) -> bool:
            pass

        for char in prechars:
            if dfs(char):
                return True

        return False

    # Check adjacency matrix for cycles
    if contains_cycle(edges):
        return ""

    # Topological Sort
    processed_characters = set()
    topological_ordering = []

    def dfs(char: str) -> None:
        if char in processed_characters:
            return

        for prechar in prechars[char]:
            dfs(prechar)

        processed_characters.add(char)
        topological_ordering.append(char)

    for char in characters:
        dfs(char)

    print(topological_ordering)
    return "".join(topological_ordering) if len(topological_ordering) == n_characters else ""

"""https://www.youtube.com/watch?v=6kTZYvNNyps

I got it right above, but let's look at some optimizations that neet
put in his video!
    * Only need to check n, n+1 word for n word in words at beginning
    * Can directly create the adjacency matrix
    * Cycle detection
"""
def neetcode_solution(words: list[str]) -> str:
    # Cool! This is a better way to guarantee that all characters have an entry
    # Think of this as "prerequisites"
    adjacency_matrix = {
        char: set()
        for word in words
        for char in word
    }

    # Interesting: You only need to compare a word to the one IMMEDIATELY after it
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))

        # Checking for an invalid ordering (abcd coming before abc). If we have ABCD and ABC, then ABC must appear first
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""

        # Now find the first differing character and learn something
        for j in range(minLen):
            w1c, w2c = w1[j], w2[j]
            if w1[j] != w2[j]:
                # We know that w2c "comes after" w1c in the alien alphabet
                adjacency_matrix[w1c].add(w2c) # NOTE! This is actually the opposite of prerequisites, oops! I reverse the list in the end topological sort to fix this
                break;

    # Do Cycle Detection Here (Skipping)

    # False = Visited, True = Visited & In Current Path, NotPresent = Not Visited at all
    processed_characters = set()
    # We're going to be traversing the graph is "reverse order", so we'l populate this list and then reverse/join it.
    topological_ordering = []

    # Now, do a topological sort (Sam's Code)
    def dfs(char: str):
        if char in processed_characters:
            return

        for prechar in adjacency_matrix[char]:
            dfs(prechar)

        processed_characters.add(char)
        topological_ordering.append(char)

    for char in adjacency_matrix:
        dfs(char)

    print(topological_ordering)
    return "".join(topological_ordering[::-1])



def test(fn):
    assert fn([
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]) == "wertf"

    assert fn([
        "z",
        "x"
    ]) == "zx"

    assert fn([
        "z",
        "x",
        "z"
    ]) == ""  # The order is invalid, so return ""


# test(alien_dictionary)
test(neetcode_solution)