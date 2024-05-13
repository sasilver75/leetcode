"""
Impelment Trie

A Trie (prenounced try) or Prefix Tree is a tree datas tructure used
to efficiently store and retrievec keys in a dataset of strings.

There are various applications to this tdata structure, like autocomplete
and spellchecking.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

"""

class Node:
    def __init__(self, value: str):
        self.value = value
        self.is_end_of_word = False
        self.children = []

    def get_child_by_value(self, value: str):
        for child in self.children:
            if child.value == value:
                return child
        return None



class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie
        :param word: The word to be inserted into the Trie
        :return: None
        """
        cur = self.root

        for char in word:
            child = cur.get_child_by_value(char)
            if child:
                cur = child
            else:
                new_node = Node(char)
                cur.children.append(new_node)
                cur = new_node

        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
        :param word: A search word
        :return: Whether the search word is in the trie
        """
        cur = self.root
        for char in word:
            cur = cur.get_child_by_value(char)
            if cur is None:
                return False
        return cur.is_end_of_word


    def startsWith(self, word: str) -> bool:
        """
        Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
        :param word: The search word
        :return: Whether the search word is a prefix of a previously inserted word
        """
        cur = self.root
        for char in word:
            cur = cur.get_child_by_value(char)
            if cur is None:
                return False
        return True


trie = Trie()
trie.insert("apple")
trie.search("apple") == True
trie.search("app") == False
trie.startsWith("app") == True
trie.insert("app")
trie.search("app") == True