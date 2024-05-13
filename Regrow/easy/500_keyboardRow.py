"""
Given an array of strings WORDS, return the words in that list that can
be typed using letters of the alphabet on only one row of American keyboard...

In the American keyboard:
    First row: "qwertyuiop"
    Second row: "asdfghjkl"
    Third row: "zxcvbnm"
"""

"""
So the general idea is, given a word, can it be constructed using the characters
from one of the three ROWS above.

word = "abc"
for row in ROWS:
    if all(char in row for char in word):
        YAY
NAY

But that's a linear scan for each character in each word. It'd be 
"""

# O(N) time, O(1) memory
def row_filter(words: list[str]) -> list[str]:
    first_row = set("qwertyuiop")
    second_row = set("asdfghjkl")
    third_row = set("zxcvbnm")

    rows = [first_row, second_row, third_row]

    ans = []
    for word in words: # N
        for row in rows: # 3
            if all(char.lower() in row for char in word):
                ans.append(word)
    print(ans)
    return ans



# Note Cap/Lower usage
assert row_filter(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
assert row_filter(["omk"]) == []
assert row_filter(["asdf", "sfd"]) == ["asdf", "sfd"]
