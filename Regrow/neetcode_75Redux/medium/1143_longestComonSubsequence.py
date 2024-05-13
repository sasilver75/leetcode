"""
Longest Common Subsequence

Given two strings text1 and text2, return the LENGTH of their LONGEST COMMON SUBSEQUENCE!
If there is no common subsequence, return 0

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted, without changing
the relative order of the remaining characters
    eg "ace" is a subsequence of "abcde"

A common subsequence of two strings is a subsequence that is common to both strings
"""

def generate_unique_subsequences(s: str) -> set[str]:
    subsequences = set()

    def build_subsequence(idx: int, built: list[int]) -> None:
        if idx == len(s):
            subsequences.add("".join(built))
            return

        # Either include or don't include the character @ index idx in the current subsequence
        # Include
        new_built = [*built, s[idx]]
        build_subsequence(idx+1, new_built)

        # Don't include
        build_subsequence(idx+1, built)

    build_subsequence(0, [])
    return subsequences



def longest_common_subsequence_naive(text1: str, text2:str) -> int:
    text1_subsequences = generate_unique_subsequences(text1)
    text2_subsequences = generate_unique_subsequences(text2)

    intersection = text1_subsequences.intersection(text2_subsequences)
    return max(len(ss) for ss in intersection) if intersection else 0

"""
How can we be smarter about this?
I sort of assume that there's going to be a 2-D DP solution to this.

IE if we know (bcde,ace), does that subproblem help us with (abcde, ace)? Maybe.

Neetcode hint: 
recursive: if first chars are equal find lcs of remaining of each, else max of: 
    lcs of first and remain of 2nd and lcs of 2nd remain of first,
     cache result; nested forloop to compute the cache without recursion;
     
Let's look at an example

("abcde", "ace")

1 + "bcde", "ce"
    "cde", "ce"                             vs                          "bcde", "e"
                                                                        "cde", "e"        vs    "bcde"   ""
                                                                                                    0

"""
def longest_common_subsequence(text1: str, text2: str) -> int:

    def explore(idx1: int, idx2: int):
        if idx1 == len(text1) or idx2 == len(text2):
            return 0

        if text1[idx1] == text2[idx2]:
            return 1 + explore(idx1+1, idx2+1)

        return max(
            explore(idx1+1, idx2),
            explore(idx1, idx2+1)
        )

    return explore(0, 0)


"""
TWO Dimensional DP!
Using the exact same logic as above:

LCS(ace, abcde) = 3
    
    a   b   c   d   e
a   0   0   0   0   0
b   0   0   0   0   0
c   0   0   0   0   0

Think about the graph above where being at the "a"th row means that you only have "a" to work with, while being at the "c"th row means you still
have "abc" to work with.

We can populate this from the top-left to the bottom-right using:

dp[row][col] = 1 + dp[row-1][col-1] if text1[row] == text2[col] else max(dp[row-1][col], dp[row][col-1])
Applying this each row (top to bottom), left to right

    a   b   c   d   e
a   1   1   1   1   1
b   1   2   2   2   2
c   1   2   3   3   3

dp[-1][-1] = 3


Above, we were like.
______________
| match| cand|
|_____|______|
|cand | curr |
|_____|______|      For the current cell, if ther was a match, we did 1 + match; else, max of cand(idates).
And we sort of dragged this idea of looking "up to the left" behind us, moving from top left to bottom right

If the characetrs "match", imagine that we're pairing them together and taking them out of the equation entirely; in that case, both strings are -1 in 
length, putting us back at [row-1][col-1]....

If the characters DON'T match, then we have to "discard" one of them; ideally, we discard the one that leaves us with two strings that still give the
best LISS, which is why we use max(d[row-1][col], d[row][col-1]) 

"""
def longest_common_subsequence_dp(text1: int, text2: int):
    pass

def test(fn):
    assert fn("abcde", "ace") == 3
    assert fn("abc", "abc") == 3
    assert fn("abc", "def") == 0

test(longest_common_subsequence_naive)
test(longest_common_subsequence)