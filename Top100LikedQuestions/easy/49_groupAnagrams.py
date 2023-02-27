"""
Group Anagrams

Given an array of strings strs, group the ANAGRAMS together

You can return the answer in any given order

An anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all of the original letters at least once


Note: strs[i] consists only of lowercase lettters
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    ...


def test(fn):
    ans = fn(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert all(ls in ans for ls in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert fn([""]) == [[""]]
    assert fn(["a"]) == [["a"]]

