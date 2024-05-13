"""
Word Break

Given a string `s` and a dictionary of strings `wordDict`, return `true` if
`s` can be segmented into a space-separated sequence of one or more dictionary
words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.
"""

"""
I think the idea here is just to do a DFS on any matching choice in wordDict

In the worst case, s="aaa" and wordDict=["a", "a", "a", "a"] or something,
which would be 4^3 different options... so that's len(s)^len(wordDict)?
That's not great.
"""
def word_break_naive(s: str, wordDict: list[str]) -> bool:
    def dfs_explorer(idx: int) -> bool:
        if idx > len(s): # This should never happen
            return False
        if idx == len(s):
            return True

        options = [word for word in wordDict if word == s[idx:idx+len(word)]]
        return any(
            dfs_explorer(idx+len(option))
            for option in options
        ) if options else False

    return dfs_explorer(0)

"""
How can we do better?
We can formulate this as a bottom-up dynamic programming problem!

dp = [False] * (len(s)+1)

"leetcode", ["leet", "code"]

[False, False, False, False, False, False, False, False, True]

From back to front: dp[7] indicates that s[7:] can be wordbroken using words
d[i] = True if any of the dp[i+wordLength]=True for word in words
"""
def word_break_smart(s: str, wordDict: list[str]) -> bool:
    wds = set(wordDict)
    dp = [False] * (len(s)+1)
    dp[-1] = True

    for idx in range(len(dp)-1, -1, -1):
        for word in wds:
            if (
                    idx + len(word) < len(dp) and
                    dp[idx+len(word)] == True and
                    s[idx:idx+len(word)] == word
            ):
                dp[idx] = True
                break # Don't need to do the remaining words in wds once we set to True


    print(dp)
    return dp[0]

def test(fn):
    assert fn("leetcode", ["leet", "code"]) == True
    assert fn("applepenapple", ["apple", "pen"]) == True
    assert fn("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

test(word_break_naive)
test(word_break_smart)