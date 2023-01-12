"""
Decode Ways

A message containing the letters from A-Z can be ENCODED into numbers using the following mapping:

A -> 1
B -> 2
...
Z -> 26

To DECODE the encoded message, all of the digits must be grouped, then mapped back into letters using the reverse
of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)

*** Note that the grouping (1, 11, 06) is invalid because "06" cannot be mapped into "F", since "6" is different from "06"
    -> My takeaway is that the keys should be strings instead of ints

Given a string s containing only digits, return the NUMBER OF WAYS TO DECODE IT!
"""
import string
from typing import Callable
from string import ascii_uppercase

LOOKUP = dict(zip([str(n) for n in range(1, 27)], string.ascii_uppercase))

"""
I think this is going to be a situation where we're iterating from left to right, and at each element beginning a process of growing a "window" while
we have usable characters...

It might be interesting that we only need the NUMBER of the ways, not the actual ways themselves :) 
"""

"""

2   2   6
^

                                    0
                        2                       22
                  2          26                    6
                6
"""


class Solution:
    def __init__(self):
        self.n_ways = 0

    def decode_ways(self, s: str) -> int:
        print(LOOKUP)

        def helper(s: str, idx: int):
            print(f"Helper called for {s} at idx {idx}")
            if idx >= len(s):
                print("Reached end")
                self.n_ways += 1
                return

            for i in range(idx, len(s)):
                print(f"At base index {i}")
                l, r = idx, idx
                print(f"Initial slice: {s[l:r + 1]} in lookup? {s[l:r + 1] in LOOKUP}")
                while r + 1 < len(s) and s[l:r + 1] in LOOKUP:
                    print(f"Considering substring {s[l:r + 1]}")
                    # If the substring is in lookup, take a bite! (Choose that substring, move index forward by the length of the substring)
                    helper(s, idx + (r - l + 1))
                    r += 1

        helper(s, 0)
        print(f"N Ways: {self.n_ways}")
        return self.n_ways


"""

l   r
1   2





"""


class Sol:
    def __init__(self):
        self.way_count = 0

    def n_ways(self, s: str) -> int:

        def helper(s: str, idx: int):
            print(f"Helper called at {idx}")
            l, r = idx, idx
            while r < len(s) and s[l:r + 1] in LOOKUP:
                print(f"Chomping: {s[l:r + 1]}, moving to _{s[r + 1:]}_ remaining substring")
                # Chomp at current window, moving i rightward by chomp size
                helper(s, r + 1)

                # If we just ate up to the end, inc n_ways
                if r >= len(s) - 1:
                    print("~ INC")
                    self.way_count += 1

                # Increase window size by one
                r += 1

        for idx in range(len(s)):
            helper(s, idx)

        print("WAY COUNT: ", self.way_count)
        return self.way_count


"""
--- Two Day Break

There's an interesting thing

As we slide acorss, we'll either be "taking" a length-1 or length-2 slice
of the string to decode.
Note that we can't decode things like a "06" into 6.
Note actually that we also can't decode "0" into 0 -- that isn't a number in our lookup table.
We can actually only "take" double digit values IF the first digit starts with a 1 or 2 (and even then, only sometimes)

121
            start
        1       12
    2    [21]       [1]
  [1]               
        
        
I also suppose if we're at 12013 and we're at index 0, we really 
HAVE to take ONLY 1 (and not 12), since if we took (12), that would leave
us with idx 2 at 0, which is a non-starter...
So the only option is 
(1, 20, ...)

But then that opens the door to the question of what to do if there were
TWO ZEROES in a row, i.e. 120013. I suppose this would be UNDECODABLE by
the rules that we've been given, since we'll either have a 0 or a leading 0
on some take of the string?
"""


def n_ways_brute(s: str, idx: int = 0) -> int:
    # If we're at the end of the string (even the last character), return 1. This stops us from double-counting on the second recursive case if we were at the last character
    if idx >= len(s) - 1:
        return 1

    current_char = s[idx]
    next_char = s[idx + 1] if idx + 1 < len(s) else None
    next_next_char = s[idx + 2] if idx + 2 < len(s) else None
    # CombinedChar will only be non-None if it's in the interval [10, 26]
    combined_char = current_char + next_char if next_char and 10 <= int(current_char + next_char) <= 26 else None

    # print(f"Iteration. Current is {current_char} and Combined is {combined_char}")

    # If nextnext char is a 0, we CAN'T do a two-take, since that would lead us with a leading zero for the next
    if next_next_char == 0:
        return n_ways_brute(s, idx + 1)
    # If next_char is a 0, we HAVE to take the combined_char ONLY -- 0 can't stand as a "take one", or a lead char in a "take two"
    elif next_char == 0:
        # But there's the thought that the combined char might not be valid too. What then? I think instead of throwing an error, we'd likely just return a 0 for this recursive branch, and do no further recursion.
        # But I'll leave that out... I realize that we're somewhere between "assume the input is valid, ie no 00s, and check for all invalids and return 0
        return n_ways_brute(s, idx + 2)
    else:
        # Take One and Take Two if available
        return n_ways_brute(s, idx + 1) + (n_ways_brute(s, idx + 2) if combined_char else 0)


"""
How can we do this a little smarter?

Say we have 121

When we take just (1) by itself
Then we're asking... how many ways can we decode the remaining string (21)
When we take the first TWO characters (12), we're asking how many ways can
we decode the remaining string (1)? There are actually times where we're 
repeatedly asking the same question, and memoization could help, right?

But whenever you're populating some memoization table, you have to be sure that
you're populating it in a way that it's useful for the other subproblems... it's 
sometimes possible to populate a memoization table nad not take advantage of it once, 
since we did top-down instead of bottom-up, for example.

To be able to solve 
"How Many Ways Can We Decode 121"
We need to first know "How many ways can we decode _21"?
For which we need ot know "How many ways can we decode __1"?

So we're gonna have some i that designates an index that represents....
starting from i (inclusive), how many ways can we decode the remaining string?

Basically... the dimension of our cache is going to be N. The runtime complexity is also 
going to be O(N) and our memory usage too.
Because any time we get to a position i, at MOST we have two different decisions
to make, which is an O(1) operation.
"""


def n_ways(s: str) -> int:
    # Bottom Up Recursive Solution
    memo = [1, 2]
    for i in range(len(s) - 3, -1, -1):
        memo.append(memo[-1] + memo[-2])

    return memo[-1]


def n_ways_constant_memory(s: str) -> int:
    n_2 = 1
    n_1 = 2
    for i in range(len(s) - 3, -1, -1):
        ways = n_2 + n_1
        n_2 = n_1
        n_1 = ways

    return n_1


# Neetcode Solution
class Solution:
    def numDecocdings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i: int):
            # How many ways can we decode a string starting at index i?
            if i in dp:  # Base Case: In Cache
                return dp[i]
            if s[i] == "0":  # Base Case: No way to decode a 0
                return 0

            # Recursive: Can take single or double digit?
            res = dfs(i + 1)
            if (i + 1 < len(s)) and 10 <= int(s[i:i + 2]) <= 26:  # Checking for double digit-ability
                res += dfs(i + 2)
            dp[i] = res

            return res

        return dfs(0)


# Neetcode actual dynamic programmign solution
def num_decodings(s: str) -> int:
    # Tbh I think this might have an edge case or two... like actually doing "05"
    dp = {len(s): 1}
    for i in range(len(s) - 1, -1, -1):

        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
            dp[i] += dp[i + 2]

    return dp[0]


# ------- TEST ZONE -------

def test(fn: Callable) -> None:
    assert fn("12") == 2  # "12" -> "AB" (1,2) or "L" (12)
    assert fn("226") == 3  # "226" -> "BZ" (2, 26), "VF" (22, 6), or "BBF" (2, 2, 6)


# print(n_ways_brute("12"))
# print(n_ways_brute("121"))
# print(n_ways_brute("1201"))  # (1,20,1), (
# test(n_ways_brute)
# test(n_ways)
# test(n_ways_constant_memory)

test(Solution().numDecocdings)
