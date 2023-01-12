"""
Decode Ways

A message containing letters from A-Z can be encoded into numbers
using the following mapping:

"A" -> "1"
"B" -> "2"
...
"Z": "26"

To decode an encoded message, all the digits MUST be grouped, then mapped
back into letters using the reverse of the mapping above (there may be multiple
ways of doing this).

For example, "11106" can be mapped to:
-> "AAJF" with grouping (1, 1, 10, 6)
-> "KJF" with the grouping (11, 10, 6)

NOTE that the grouping (1, 11, 06) is INVALID because "06" cannot be
mapped into "F", since "6" is different from "06"

Given a string `s` containing only digits, return the NUMBER OF WAYS
to decode it!
"""
import string

"""
Thinking:

So I think the idea is that we have a bunch of recursive braches that attempt 
to get some "current" index to the end of s, or similar.

So at the current index, you could take a BITE of either length 1 or length 2,
assuming you're able to do each.

The trick is about these 0's.
We can never START a bite (either length 1 or 2) with a 0.
Meaning if you have an opportunity to bite UP TO (inclusive) a zero, you 
HAVE to -- and you can ONLY do that (as opposed to taking "both" a 1+2) 
"""

LOOKUP = {k: v for k, v in zip([str(num) for num in range(1, 27)], string.ascii_uppercase)}


def n_ways(s: str) -> int:
    # Assuming s is a valid string .. ex: No 00's
    ways = 0

    def helper(idx: int) -> None:
        """
        Given an index. process at the current index
        (adding characters as appropriate), and recurse into valid futures
        """
        nonlocal ways
        if idx >= len(s):
            ways += 1
            return

        # First: Check if we HAVE to take a 2-bite
        if idx + 1 < len(s) and s[idx + 1] == "0" and s[idx:idx + 2] in LOOKUP:
            return helper(idx + 2)

        # We can take either a 1 bite or a 2 bite (length-permitting, lookup-permitting)
        if s[idx:idx + 1] in LOOKUP:
            helper(idx + 1)
        if idx + 1 < len(s) and s[idx:idx + 2] in LOOKUP:
            helper(idx + 2)

    helper(0)
    return ways


assert n_ways("12") == 2
assert n_ways("226") == 3
assert n_ways("06") == 0
