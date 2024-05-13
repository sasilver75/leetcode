"""
Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an INTERLEAVING
of s1 and s2.

An INTERLEAVING of two strings `s` and `t` is a configuration where `s` and
`t` are divided into `n` and `m` substrings, respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1

The interleaving would then be:
s1+ t1+ s2 + t2 + s3+ t3 + ...
or
t1+ s1 + t2+ s2 + t3 + s3 + ...

Note: a+b is the concatenation strings a and b
SEE PICTURES HERE: https://leetcode.com/problems/interleaving-string/
"""

"""
The actual question:
Can we form the string s3 by interleaving the strings s1 and s2?

s1:    a a b c c
s2:    D B B C A

s3:    a a d b b c b c a c   ?

Yes!
       a a D B B C b c A c

Trying to illustrate me taking from s1 vs s2 via capitals. 
The important thing is that this isn't just a charcounts thing -- the ORDER
of the strings actually matters! Once we add a character @ index[2] 


Quetsion: Do we have to use every character is s1/s2?
"""

# def is_interleave_naive(s1: str, s2: str, s3: str) -> bool:
#     # Imagining we had a pointer moving left to right on each...
#
#     def helper(s1p: int, s2p: int, s3p: int) -> bool:
#         # Are we done?
#         if s3p == len(s3):
#             return True
#         # Have we exhausted our s1 and s2?
#         if s1p == len(s1) and s2p == len(s2):
#             return False
#
#         s1c, s2c, s3c = s1[s1p] if s1p < len(s1) else None, s2[s2p] if s2p < len(s2) else None, s3[s3p] if s3p < len(
#             s3) else None
#
#         if s1c == s3c:
#             # Match on s1c... Eitehr use it or don't use it
#             if helper(s1p + 1, s2p, s3p + 1) or helper(s1p + 1, s2p, s3p):
#                 return True
#
#
#         elif s2c == s3c:
#             # Match on s2c... Either use it or don't use it
#             if helper(s1p, s2p + 1, s3p + 1) or helper(s1p, s2p + 1, s3p):
#                 return True
#
#
#         # Advance a pointers without using either s1c/s2c
#         else:
#             # No match on either
#             if helper(s1p + 1, s2p, s3p) or helper(s1p, s2p + 1, s3p):
#                 return True
#
#         return False
#
#     return helper(0, 0, 0)


"""
Is there a 2D dynamic programming solution to this? What would characterize 
our position in the tree?

Is it just s1p and s2p (the indices that we're at in each?)? 

Imagine we had the following example:
s1 = aabcc
s2 = dbbca
s3 = aadbbcbcac
        
            d   b   b   c   a   ""
        _____________________________
    a   |   _   _   _   _   _   _
    a   |   _   _   _   _   _   _
    b   |   _   _   _   _   _   _
    c   |   _   _   _   _   _   _
    c   |   _   _   _   _   _   _
    ""  |   _   _   _   _   _   T
    
If we're able to fully exhaust both "" and "", I suppose that means... we're good?
If we use i, j to refer to the pointers in s1, s2
Then we can infer s3's k pointer as k = i + j

***INSIGHT***
The idea that I was missing before is twofold, I think:
    1) We'll never "skip" a character in either s1 or s2; an "interleaving" implies 
    that all characters are going to be used
    2) Assume that there will never be characters remaining in s3 after we've exhausted s1 and s2.
    That is, I believe that the length of s3 = len(s1) + len(s2)
    
These weren't clear to me as a reader of the question, but it clarifies the problem
dramatically, I think. 
"""


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    dp = {}  # (i,j): boolean of "can we interleave"

    def dfs(i, j):
        # Base Case 1: We've exhausted s1 and s2
        if i == len(s1) and j == len(s2):
            return True

        # Base Case 2: This case is in DP cache already
        current_key = (i, j)
        if current_key in dp:
            return dp[current_key]

        # Consider options: we have to either use s1[i] or s2[j] to match s3[i+j]
        if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
            # If we can use s1's next char and using it puts us down a successful path:
            return True
        if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
            # If we can use s2's next char and using it puts us down a successful path
            return True

        # Otherwise, we either couldn't use s1/s2's next character, or doign so didn't
        # put us down a successful path. Therefore, False. Mark this in DP so that we
        # don't have to go down this path again.
        dp[(i, j)] = False
        return False

    return dfs(0, 0)


# -- Test --
def test(fn):
    assert fn("aabcc", "dbbca", "aadbbcbcac") == True
    assert fn("aabcc", "dbbca", "aadbbbaccc") == False


# test(is_interleave_naive) # This doesn't quite work, but the idea's there. It's pretty finnicky.
test(is_interleave)
