"""
Word Break

Given a string `s` and a dictionary of strings `wordDict`, return
`true` if `s` can be segmented into a space-separated sequence of
ONE OR MORE dictionary words.

NOTE that the same word in the diction MAY BE REUSED multiple times in
the segmentation.
"""

def word_break(s: str, wordList: dict):
    def helper(idx: int, remaining:str):
        if not remaining:
            return True

        return any(
            helper(idx + len(word), remaining[len(word):]) for word in wordList if remaining[0:len(word)] == word
        )
    return helper(0, s)


# -- Test Zone --
def test(fn):
    assert fn("leetcode", ["leet", "code"]) == True
    assert fn("applepenapple", ["apple", "pen"]) == True
    assert fn("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

test(word_break)