"""
Group Anagrams
Category: String

Given an array of strings `strs`, group the ANAGRAMS together!
You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the lettesr
of a different word or phrase, typically using all of the original
letters exactly once.
"""
import collections

"""
Assuming 
"""
def group_anagrams_naive(strs: list[str]) -> list[list[str]]:
    """
    Here's an O(N), O(N) solution off the dome.
    Turn the strs into character vectors of length 26.
    Then make them into a immutable, hashable tuple, and insert/append them
    into a defauldict(list).
    Then take the values of that dict as a list.
    """
    def generate_count_vector(s: str) -> tuple[int]:
        # Assuming all-lowercase A-Z
        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1
        return s, tuple(counts)


    groups = collections.defaultdict(list)
    s_and_vector = [generate_count_vector(s) for s in strs]

    print(s_and_vector)
    for s, vector in s_and_vector:
        groups[vector].append(s)

    ans = list(groups.values())
    print(ans)
    return ans

"""
Can we do better than O(N)/O(N)? Can we do it with less memory? I don't think so, without 
increasing the time it would take...
Doesn't seem like there are better solutions if you want to keep O(N) time?
"""



def test(fn):
    assert all(l in fn(["eat","tea","tan","ate","nat","bat"]) for l in [["bat"],["nat","tan"],["ate","eat","tea"]]) # This does work
    assert fn([""]) == [[""]]
    assert fn(["a"]) == [["a"]]

test(group_anagrams_naive)