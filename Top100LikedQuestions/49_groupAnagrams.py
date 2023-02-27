import collections

"""
Group Anagrams

Given an array of strings strs, group the ANAGRAMS together

You can return the answer in any given order

An anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all of the original letters at least once


Note: strs[i] consists only of lowercase lettters
    - This is exploitable
"""

"""
Anagrams only care about character counts
What is a representation of character counts in a word that we can use to collect like-valued items?
Collecting like-valued items in O(1) time makes you think of a hashtable
So a hashtable that's a list of words that have the same character counts
How do we encode character counts? On a 26-tuple, which is immutable and hashable.
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = collections.defaultdict(list)

    def get_char_vect(s: str) -> tuple[int]:
        acc = [0] * 26
        for char in s:
            idx = ord(char) - 97  # a = 0, z = 25
            acc[idx] += 1
        return tuple(acc)

    for s in strs:
        char_vect = get_char_vect(s)
        groups[char_vect].append(s)

    ans = list(groups.values())
    print(ans)
    return ans


def test(fn):
    ans = fn(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert all(ls in ans for ls in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert fn([""]) == [[""]]
    assert fn(["a"]) == [["a"]]

test(group_anagrams) # This works, just the testing is a little finnicky