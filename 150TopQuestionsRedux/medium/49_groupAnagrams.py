"""
Group Anagrams

Give an array of strings strs, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all of the original letters exactly once.

NOTE: strs[i] consists only of lowercase english letters
"""
import collections

"""
An anagram just means that it has the same character counts as another character.
Given that it's only lowercase english letters (a character set of only 26), we can convert each str into a tuple of character counts, and insert them into a defaultdict(list) structure. 
"""
def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)

    for s in strs:
        acc = [0]*26
        for char in s:
            idx = ord(char)-97 # So 'a' is 0
            acc[idx] += 1
        acc_tup = tuple(acc)
        anagrams[acc_tup].append(s)

    print(anagrams)
    return list(anagrams.values())


# ans1 = group_anagrams(["eat","tea","tan","ate","nat","bat"])
# print(ans1) # This works, just the assertion is tricky tyo get ordered correctly.
# assert all(group in ans1 for group in [["bat"],["nat","tan"],["ate","eat","tea"]])

assert group_anagrams([""]) == [[""]]
assert group_anagrams(["a"]) == [["a"]]