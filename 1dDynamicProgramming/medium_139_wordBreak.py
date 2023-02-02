"""
Word Break

Given a string `s` and a dictionary of strings `wordDict`, return `true` if
`s` can be segmented into a space-separated sequence of ONE OR MORE of the
dictionary words!

Note that the same word in the dictionary MAY BE REUSED multiple times in the
segmentation.


Sam Translation: basically, using the words ( >= 0 times ) in `words`, can you
take chomps of `s` using a `word` from `words` such that we completely exhaust the
string s?
"""
from typing import Callable


def word_break(s: str, words: list[str]) -> bool:
    # Base Case: Empty String -- Done! :)
    if s == "":
        return True

    # Recurse for each recursable word in words, given s
    for word in words:
        word_l = len(word)
        if word == s[0: word_l] and word_break(s[word_l:], words):
            return True

    # Unable to recurse to completion; return False
    return False


"""
How can we do this in a DP way? What patterns are available?
Is there repeated work that's being done?

Say we had "leetcode" and ["leet", "code"]

One of the ways is interesting -- Above, we were looping through each WORD
in WORDS and seeing if it matches the appropriate-length-leading-substring
of S. 
Instead we could grow a window from length [1...max(len(word) for word in words)],
recursing. That would save some time, I think? We'd still have to scan through words.
Could put words in a hashset to speed up that lookup time...
"""


def word_break_2(s: str, words: list[str]) -> str:
    wordset = set(words)
    max_word_length = max(len(word) for word in wordset)

    def helper(s: str, idx: int):
        for length in range(1, max_word_length + 1):
            if idx + length <= len(s) and s[idx: idx + length] in wordset:
                # Chomp
                if idx + length == len(s):  # Did we finish?
                    return True
                return helper(s, idx + length)
        return False

    return helper(s, 0)


"""
Neetcode time...
Illustration of Decision Tree --> How to cache that to eliminate repeated work
--> How to do the optimal bottom-up DP solution

neetcode        [neet, leet, code]

starting at i=0, we're going to be keeping track of whatever index we're at...
If we can find a word that matches "neet", for example, then our subproblem would
be the word_break problem starting at index 4. 

So we're only going to be keeping track of one variable (i) in our backtracking solution

                        i=0
            neet(V)        leet(X)        code(X)
            i=4
    neet(X) leet(V) code(X)    
            i=8
            done
            
    Let's say we were somehow at i=5, and none of our branches (words) were able
    to take a chomp. We'd want to return False from that path. But we also want
    to cache that i=5 is False, so that we don't have to redo all that work!
"""


def neetcode_1(s: str, words: list[int]):
    cache = {}

    def helper(idx: int):
        if idx in cache:
            return cache[idx]

        if idx == len(s):
            cache[idx] = True
            return True
        for word in words:
            word_length = len(word)
            if word == s[idx:idx + word_length] and helper(idx + word_length):
                cache[idx] = True
                return True
        cache[idx] = False
        return False

    return helper(0)


"""
Bottom up DP Approach
neetcode FROM [neet, leet, code]
We know that dp[8] is True... (Meaning the point after which we've exhausted the string)
dp[7] = False (After scanning through words)
dp[6] = False (After scanning through words)
dp[5] = False (After scanning through words)
dp[4] = True (Match on "code"), Now "end" is set to 4, and we'll match future strings to the substring ending at 4.
dp[3] = False
dp[2] = False
dp[1] = False
dp[0] = True (Match on "neet"), Now "end" is set to 0, and ...
(done)
return dp[0]
"""

"""
                  i  
i       0 1 2 3 4 5 6 7 8
dp      _ _ _ _ _ _ _ _ T
s       n e e t c o d e         leet code neet

"""
def neetcode_2(s: str, words: list[int]) -> bool:
    # Bottom Up Approach
    dp = [False] * (len(s) + 1)
    dp[-1] = True

    anchor = len(s)

    # From the back of the DP table
    for i in range(len(s) - 1, -1, -1):
        # From here to the beginning of the last chomp...
        ss = s[i:anchor]
        if any(ss == word for word in words):
            # If we have a match, update anchor (beginning of this chomp) and dp[i]
            dp[i] = True
            anchor = i

    # print(dp)
    return dp[0]




# -- Test Zone -- /!
def test(fn: Callable):
    assert fn("leetcode", ["leet", "code"])
    assert fn("applepenapple", ["apple", "pen"])
    assert fn("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert fn("neetcode", ["neet", "leet", "code"])
    assert fn("abc", ["c", "bc", "a"])


# test(word_break)
# test(word_break_2)
# test(neetcode_1)
test(neetcode_2)