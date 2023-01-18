"""
Decode Ways

A message containing hte letters from A-Z can be ENCODED
into numbers using the following strategy:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To DECODE a message, all the digits must be groujped and then
mapped back into letters using the reverse of hte mapping above

For example, "11106" can be mapped into:
    - "AAJF" with the grouping (1 1 10 6)
    - "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid, because "06" can't be mapped into "F",
since "6" is different from "06"

Given a string `s` containing only digits, return the NUMBER of ways to DECODE it
"""
import string

LOOKUP = {k:v for k, v in zip([str(i) for i in range(1, 27)], string.ascii_uppercase)}


"""
What are the rules here?
If the next character is a 0, then we can only take a two-biter.
Else, we can take a one-biter and a two-biter (assuming there are two characters remaining to takea two biter with)
"""
def n_ways_decode(s: str) -> bool:

    def recursive_explorer(idx: int) -> int:
        """
        A DFS Exploration function
        Given a current position in the string `s`, we may have [0,2] options of bites
        that we could take, depending on the characters at s[idx] and s[idx+1]

        Rules:
        If s[idx+1] is a 0, then we HAVE to ONLY take a "two-biter,"
        """
        if idx >= len(s):
            return 1

        options = set()
        options.add(s[idx:idx+2])
        if idx+1 < len(s) and s[idx+1] != "0":
            options.add(s[idx])

        options = {option for option in options if option in LOOKUP}
        if not options:
            return 0

        return sum(
            recursive_explorer(idx+len(option))
            for option in options
        )

    ans = recursive_explorer(0)
    print(ans)
    return ans


assert n_ways_decode("12") == 2
assert n_ways_decode("226") == 3
assert n_ways_decode("06") == 0