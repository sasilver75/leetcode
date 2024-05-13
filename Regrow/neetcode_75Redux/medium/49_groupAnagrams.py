"""
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return
the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all of the original letters exactly once.

NOTE: strs[i] consists of only lowercase english letters!
"""
import collections

"""
Okay, so a string is an anagram for anathor string if the characters
can be rearranged to make the same string.
The characters can be arranged to do this if the count of each character is 
the same.

So I think what we could do is turn each str into a vector of character counts
And then use a hashtable to accumulate the strings with the same char counts

This is doable in a reasonable space becasue we're guaranteed that all
of the character sin the strings are lowercase english characteres

We could do this in ~Linear time, I believe? 
"""


def group_anagrams_naive(strs: list[str]) -> list[list[str]]:
    def get_character_count_vector(s: str) -> tuple[int]:
        # ord('a') = 97, so we want to do ord[char]-97 to get index
        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1

        return tuple(counts)

    anagrams = collections.defaultdict(list)
    for s in strs:
        anagrams[get_character_count_vector(s)].append(s)

    ans = list(anagrams.values())
    print(ans)
    return ans


def test(fn):
    assert fn(
        [""]
    ) == [[""]]

    assert fn(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    ) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

test(group_anagrams_naive)  # This is correct, actually! Just the order is a little wrong
