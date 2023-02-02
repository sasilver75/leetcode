"""
Word Break

Given a string s and a dictionary of strings wordDict, return TRUE if s can be segmented int o space-separated sequence
of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)

    def explore(idx: int) -> bool:
        if idx == len(s):
            return True

        # Determine the chompable words
        chompable_words = [
            word
            for word in words
            if word == s[idx:idx+len(word)]
        ]

        return any(
            explore(idx+len(chompable_word))
            for chompable_word in chompable_words
        ) if chompable_words else False

    return explore(0)

"""
If we assumed that we were going to have a lot of short strings, at every step, instead of looping through all  of the 
words in word dict, we could just expand a window from the current index, starting at width 1, and ending at width max(len(word in word dict))

We know what the maximum chomp size would be,, and we know what our s side of the string comparison will look like, so we'll just
use a hasset of the words in word_dict to see if we even have tha word. 
"""
def word_break_alternative(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    max_length_word = max(len(word) for word in word_dict)

    def helper(idx: int):
        if idx == len(s):
            return True

        # Consider windows in s of width in range [1, max_length_word], checking to see if the resulting word substring is in our words set
        for window_width in range(1, max_length_word + 1):
            substring = s[idx: idx+window_width]
            if substring in words and helper(idx+window_width):
                return True

        return False

    return helper(0)


"""
Could we solve this in a dynamic programming fashion
1-dimensional DP

dp[x] = can s[x:] get broken successfully?
dp of length(n) + 1
Start with all Falses
dp[-1] = True -- ie "" can be broken successfully 

"abc"
[False, False, False, True]

"""
def word_break_dp(s: str, word_dict: list[str]) -> bool:
    dp = [False] * (len(s)+1)
    dp[-1] = True

    for idx in range(len(s)-1, -1, -1):
        for word in word_dict:
            # If the bite is of valid length and the bite "matches" and the bite would get us into a "winning" state
            if s[idx: idx+len(word)] == word and dp[idx+len(word)] == True:
                # Then we can win from here
                dp[idx] = True
                break


    print(dp)
    return dp[0]





def test(fn):
    assert fn("leetcode", ["leet", "code"]) == True
    assert fn("applepenapple", ["apple", "pen"]) == True
    assert fn("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

test(word_break)
test(word_break_alternative)
test(word_break_dp)
