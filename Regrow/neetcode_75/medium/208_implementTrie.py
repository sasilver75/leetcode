from __future__ import annotations

from typing import Optional

"""
Implement Trie
Category: Tree

A `trie` (pronounced "try") or PREFIX TREE is a tree data structure
used to efficently store and retrieve keys in a dataset of strings!
There are various applications of this data structure, such as autocomplete
and spellchecking.

Implement the Trie class:
    - Trie() initializes a trie object
    - void insert(String word)
        -> Inserts the string `word` into the trie
    - boolean search(String word)
        -> Returns `true` if `word` is in the trie, and `false` otherwise
    - boolean startsWith(String prefix)
        -> Returns `true` if there is a previously inserted string `word` that
        has the prefix `prefix`, and `false` otherwise.
"""

class Node:
    def __init__(self, value: str, is_last: bool = False, children: Optional[dict[str, Node]] = None):
        if children is None:
            children = dict()

        self.value = value
        self.is_last = is_last
        self.children = children

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not char in cur.children:
                new_node = Node(char)
                cur.children[char] = new_node
            cur = cur.children[char]

        cur.is_last = True


    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if not char in cur.children:
                return False
            cur = cur.children[char]
        return cur.is_last

    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if not char in cur.children:
                return False
            cur = cur.children[char]
        return True

# Test
t = Trie()
t.insert("apple")
assert t.search("apple") == True
assert t.search("app") == False
assert t.starts_with("app") == True
t.insert("app")
assert t.search("app") == True