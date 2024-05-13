"""
Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:

"A"   ->  "1"
"B"   ->  "2"
...
"Z"   ->  "26"

To decode an encoded messsage, all of the digits must be grouped then mapped back
into letters using the reverse of the mapping above. There may be multiple ways.

For instance, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

Note that the grouping 1 11 06 is invalid, because "06" cannot be mapped into "F", since
"6" is different from "06"

Given a string s containing only digits, return the NUMBER OF WAYS to decode it
"""
import string

LOOKUP = {k:v for k,v in zip([str(num) for num in range(1, 27)], string.ascii_uppercase)} # {"1": "A", "2": "B", ... "Z": "26"}

"""
Insight:
We can either take a one-bite or a two-bite at any time, assuming that we have the ability to.
"""
def num_decodings(s: str) -> int:
    n_decodings = 0
    def dfs(idx: int) -> bool:
        """
        At the current index, there may be up to two options depending on what the bit would look like
        """
        nonlocal n_decodings
        if idx == len(s):
            n_decodings += 1
            return

        one_bite = s[idx]
        two_bite = s[idx:idx+2]
        if one_bite in LOOKUP:
            dfs(idx+1)
        if len(two_bite) == 2 and two_bite in LOOKUP:
            dfs(idx + 2)

    dfs(0)

    return n_decodings




def num_decodings_with_caching(s: str) -> int:
    n_decodings = 0
    cache = set() # Set of indexes from which we know we can decoe
    def dfs(idx: int) -> bool:
        """
        At the current index, there may be up to two options depending on what the bit would look like
        """
        nonlocal n_decodings
        if idx == len(s) or idx in cache:
            if idx in cache:
                print("Using cached at ", idx)
            return True

        one_bite = s[idx]
        two_bite = s[idx:idx+2]
        options = []
        if one_bite in LOOKUP:
            options.append(one_bite)
        if len(two_bite) == 2 and two_bite in LOOKUP:
            options.append(two_bite)

        for op in options:
            if dfs(idx+len(op)):
                cache.add(idx)
                n_decodings += 1

    dfs(0)

    return n_decodings

"""
Is there a DP solution?

What if we had a dp table of length len(s) where dp[idx] was "How many ways can we decode s[idx:]"
    - Trick is to ahve "" on the end too
"""
def n_decodings_dp(s: str) -> int:
    dp = [0] * len(s) # TODO: Should we start with zeros? Does it even matter?
    dp.append(1) # So that when we are at the last index of "s" and looking to take a bite of 1 (s), we can inc 1 to our count. There's 1 way to decode ""
    for idx in range(len(dp) - 2, -1, -1):
        # We can take a maximum of two chomps at the current index
        one_bite = s[idx]
        two_bite = s[idx:idx+2]
        valid_bites = []
        if one_bite in LOOKUP:
            valid_bites.append(one_bite)
        if len(two_bite) == 2 and two_bite in LOOKUP:
            valid_bites.append(two_bite)

        for bite in valid_bites:
            dp[idx] += dp[idx + len(bite)]

    return dp[0]

def test(fn):
    assert fn("12") == 2
    assert fn("226") == 3
    assert fn("06") == 0



test(num_decodings)
test(num_decodings_with_caching)
test(n_decodings_dp)