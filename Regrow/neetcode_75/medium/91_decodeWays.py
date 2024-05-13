"""
91 Decode Ways
Category: DP

A message containing letters from A-Z can be ENCODED into
nubmers using the following mapping:

"A": 1,
"B": 2,
...
Z": 26

To DECODE an encoded message, all of the digits must be grouped
and then mapped back into letters using teh reverse of the mapping
above (there may be multiple ways).
For example, "11106" can be mapped into:

* "AAJF" with the grouping (1, 1, 10, 6)
* "KJF" with the grouping (11, 10, 6)

Note that grouping (1, 11, 06) is INVALID because "06" cannot be mapped into
F, since "6" is different from "06".


-> Given a string `s` containing only digits, return the NUMBER of ways to
decode it!
The test cases are generated so that the answer fits in a 32-bit integer.

"""
import string

LOOKUP = {
    str(num): char for num, char in zip(
        range(1, 27),
        string.ascii_uppercase
    )
}

"""
This is sort of a counting steps type problem, but it's complicated by 
the fact that 06 != 6, and 0 is not in LOOKUP.

So given that we're at the ^ index:
2052
^

What can we do? We can eitehr take 2 or 20, right? Wrong!
If we were to take 2, then we'd next have
052
^
Which is unworkable, since neither 0 nor 05 are in lookup!

-> Should we intelligently avoid such situations, or just let those recursive 
paths fizzle out as being unable to progress? Works either way.
"""

def num_decodings_brute(s: str) -> int:
    n_ways = 0

    def helper(idx: int):
        nonlocal n_ways

        if idx == len(s):
            n_ways += 1
            return

        # Can we take a 1-length bite? Take if possible
        if s[idx:idx+1] in LOOKUP:
            helper(idx+1)

        # Take a 2-length bite if possible
        if len(s[idx: idx+2]) ==2 and s[idx: idx+2] in LOOKUP:
            helper(idx+2)


    helper(0)
    return n_ways

"""
How can we be smarter?

Think:

NUM_DECODINGS("21432")
What would help us figure this out?

If we knew NUM_DECODINGS("1432") = 5, would that help? Yeah!
Because then we'd know it was NUM_DECODINGS("21432") = NUM_DECODINGS("1432")!
That is, for each of the 5 ways to decode NUM_DECODINGS("1432"), that way could
also then decode the "remaining" "2" character, so it's still 5 ways.

But we could either (from the left) decode 2 OR 21!

So NUM_DECODINGS("21432") = NUM_DECODINGS("1432") + NUM_DECODINGS("432")
Assuming that we can actually take a two-biter (or a one-biter)

We can easily translate that to a 1-D DP table
"""
def num_decodings(s: str) -> int:
    dp = [0] * (len(s)+1)
    dp[-1] = 1

    for i in range(len(dp)-2, -1, -1):
        # For each 1/2 bites... If we have room to take that bite, and the bite is in LOOKUP
        one_bite = dp[i+1] if i+1 < len(dp) and s[i] in LOOKUP else 0
        two_bite = dp[i+2] if i+2 < len(dp) and s[i:i+2] in LOOKUP else 0
        dp[i] = one_bite + two_bite

    return dp[0]




def test(fn):
    assert fn("12") == 2  # AB (1 2) or L (12)
    assert fn("226") == 3  # BZ (2 26) or VF (22 6) or BBF(2 2 6)
    assert fn("06") == 0  # 06 cannot be mapped to anything because of the leading 0

test(num_decodings_brute)
test(num_decodings)