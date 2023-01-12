"""
Implement Trie (Prefix Trie)

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings.

There are various applications of this structure, like autocomplete
and spellchecking.

Implement the Trie Class

* Trie() initializes trie object
* void insert(String word) inserts the string word into the trie
* boolean search(String word) returns true if the string word is in the trie
(was inserted before), and false otherwise
* boolean startsWith(string prefix) returns true if there is a previously
inserted string `word` that has the prefix `prefix` and `false` otherwise.


Note: One tricky thing to look out for in the example is the insertion
of both APPLE and APP

This results in
                Dummy
                    A
                        P
                            P
                                L
                                    E

which could look like just APPLE if we didn't know that APP was also in there
So our nodes probably also need to have a boolean flag indicating if this node
is the end character in an inserted word.
"""

class TrieNode:
    def __init__(self, char: str, is_last=False):
        self.char = char
        self.children = dict()
        self.isLast = is_last

    def set_last(self):
        self.isLast = True


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        curNode = self.root
        for idx, char in enumerate(word):
            if char not in curNode.children:
                newNode = TrieNode(char)
                curNode.children[char] = newNode
                curNode = newNode
            else:
                curNode = curNode.children[char]

            if idx == len(word) - 1:
                curNode.set_last()


    def search(self, word: str) -> bool:
        curNode = self.root
        for char in word:
            try:
                curNode = curNode.children[char]
            except KeyError:
                return False
        return curNode.isLast

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for char in prefix:
            try:
                curNode = curNode.children[char]
            except KeyError:
                return False
        return True


trie = Trie()
trie.insert("apple")
assert trie.search("apple") == True
assert trie.search("app") == False
assert trie.startsWith("app") == True
trie.insert("app")
assert trie.search("app") == True
