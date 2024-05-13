"""
Given a string s consisting of words and spaces, return the length
of the LAST word in the string
A WORD is a maximal substring consisting of non-space characters only
"""
import string


def length_of_last_word_easy(s: str):
    words = [w for w in s.split(" ") if len(w) > 0]
    return len(words[-1]) if words else 0

def length_of_last_word(s: str):
    # Phase 1: Scan from rear until first letter
    # Phase 2: Scan left, counting length of word until you hit a space.
    s = s.lower()
    count = 0
    i = len(s) - 1
    while s[i] not in string.ascii_lowercase and i >= 0:
        i -= 1
    while s[i] != " " and i >= 0:
        count += 1
        i -= 1
    return count





assert length_of_last_word("Hello World") == 5
assert length_of_last_word("   fly me   to   the moon  ") == 4
assert length_of_last_word("luffy is still joyboy") == 6
assert length_of_last_word("         ") == 0