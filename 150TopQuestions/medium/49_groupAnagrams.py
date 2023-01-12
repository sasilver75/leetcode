"""
Group Anagrams

Given an array of strings strs, group the anagrams togheter. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using ALL of the original letters EXACTLY ONCE.
"""
from collections import defaultdict
from typing import Callable

"""
Thinking:
Comparing two anagrams is pretty straightforward -- we collect the 
character counts of each character and compare them to eachother.

Is there a better way of doing this?

What if we turned each word into a tuple of character counts, where 
a word like ABD became (1,1,0,1,0,...)
And then we stuck them in a hashtable?

"""

def group_anagrams_naive(strs: list[str]) -> list[list[str]]:
    # Assuming all strs are lowercase
    anagrams = defaultdict(list)
    for s in strs:
        char_vector = [0] * 26
        for char in s:
            char_vector[ord(char) - 97] += 1
        char_vector = tuple(char_vector)
        anagrams[char_vector].append(s)
    ans = list(anagrams.values())
    print(ans)
    return ans


# - Test Zone -
def test(fn: Callable):
    fn(["eat","tea","tan","ate","nat","bat"]) # [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert fn([""]) == [[""]]
    assert fn(["a"]) == [["a"]]

test(group_anagrams_naive)