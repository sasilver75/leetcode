from typing import Optional

"""
Design Add and Search Words Data Structure
Category: Tree

Design a data structure that supports adding new words and finding if a string
matches any previously added string.

Implement the WordDictionary class:
    - WordDictionary() initializes the object
    - void addWord(word)
        Adds word to the data structure; it can be matched later
    - bool search(word)
        Returns true if there is any string in data structure that matches
        word or false otherwise. Word may contain dots '.' where dots
        can be matched with any letter!
"""


class Node:
    def __init__(self, value: str, children: Optional[dict] = None):
        if children is None:
            children = dict()

        self.value = value
        self.children = children
        self.is_last = False


class WordDictionary:
    def __init__(self):
        self.root = Node(None)

    def add_word(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                node = Node(char)
                cur.children[char] = node
            cur = cur.children[char]

        cur.is_last = True

    def search(self, word: str) -> bool:

        def search_helper(cur: Node, idx: int) -> bool:
            # Given a current position cur, and the idx of the char we're looking for,
            # attempt to find word[idx] in cur's children, and move to it.
            if idx == len(word):
                return cur.is_last

            char = word[idx]
            if char == ".":
                if not cur.children:
                    return False
                return any(
                    search_helper(cur.children[child], idx + 1)
                    for child in cur.children
                )
            else:
                if char not in cur.children:
                    return False
                return search_helper(cur.children[char], idx + 1)

        search_helper(self.root, 0)


wd = WordDictionary()
wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")
wd.search("pad") == False
wd.search("bad") == True
wd.search(".ad") == True
wd.search("b..") == True
