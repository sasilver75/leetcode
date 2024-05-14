"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

"""

def length_of_last_word(s: str) -> int:
    """
    How can we solve this?
    Given that it's just a list of words, there's no ordering to it such that we could do something like a binary search in less than O(N) time.
    If we scan backwards from the end of the list, that's worst-case O(N) time, which I don't think we can beat.
    """
    r = len(s)-1

    while s[r] == " ":
      r -= 1

    # r is at last char of last word
    l = r
    while s[l] != " ":
       l -= 1

    # l is at space before last word

    return r - l

assert length_of_last_word("Hello World") == 5
assert length_of_last_word("   fly me   to   the moon ") == 4
assert length_of_last_word("luffy is still joyboy") == 6