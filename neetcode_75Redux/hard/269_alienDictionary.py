"""
Alien Dictionary
Difficulty: Hard

There is a new alien language which uses the latin alphabet!

However the order among letters are unknown to you!

You receive a list of NON-EMPTY words from the dictionary, where words
are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language!

Notes:
    * You may assume that all letters are in lowercase.
    * You may assume that if a is a prefix of b, then a must appear
    before b in the given dictionary.
    * If the order is invalid, return an empty string.
    * There may be multiple valid orderings of the letters; returning any
    one of them is fine.
"""

"""
This is a problem where there are directed relationships between numbers 

We could either do 
    - A -> B  meaning "A comes before B"
    - A -> B meaning "B comes before A"
        - If we do this, and then traversed the list... I think we'd have to reverse at the end.
        
If we had:

acc = []
learned = {
    letter: [allOfTheLettersThatComeBeforeIt],
    ...
}
for letter in learned:
    # Add all the letters that come before it (recursively for each)
    # Add the letter 
    
So let's process the list of words sorted in lexicographical order into an adjacency list, as far as we're able to.

- Note: We need to eventually look out for cycles, and I'm guessing that if there are any disconnected components of the graph we won't be able to do this.


So we need to create this dict of adjacency lists by procesing the given `words` list
When comparing two words, what can we learn?

"wrt"
"wrf"

We know that wrf is "greater than" (later than) "wrt" because it appears later than "wrt" in the words list.

So in this case we start with pointesr on each

w   r   t               w   r   f
^                       ^

While they're pointing at the same letter, and while someone hasn't walked off their word (it's possible that they aren't the same length):
    move the pointers forward on each
    

w   r   t               w   r   f
        ^                       ^
        
Now that they're different, we know that t is "less than" f, meaning t comes before f, meaning we should do:
    prechars[f].append(t)

Assume that we instead had wrtd and wrfc

w   r   t   d           w   r   f   c
        ^                       ^

In this case, after "learning" about  t vs f, we can't continue to learn about d/c -- they aren't comparable, because their prefixes aren't identical.
So we can only learn a maximum of one thing by comparing two strings.


"""


def alien_dictionary(words: list[str]) -> str:
    """
    Process the words in a dict of adjacency lists, where for each word key, the value is a list of characters that we know come before
    the target character.
    With this adjacency list, produce a topological sort of the keys such that for every ith characters in the sorting, all characters that we know
    come before it must necessarily be in the [0:i] span.

    Note: I don't need to do cycle checking on this one, I don't think, because a lexicographical ordering of characters is like... guaranteed
    to not have any cycles in it.

    :param words: A list of lexicographically sorted words in the alien tongue
    :return: A string of alien characters sorted in one of perhaps multiple lexicographic orderings
    """
    # Prepare prechars dict
    prechars = {}
    for word in words:
        for char in word:
            if char not in prechars:
                prechars[char] = set()

    # Process each word, comparing it to successive words and learning what we can ( O(N^2) )
    for idx in range(len(words)):
        word = words[idx]
        for comparison_idx in range(idx+1, len(words)):
            comp = words[comparison_idx]

            # What can we learn by comparing word and comparison word?

            word_pointer, comp_pointer = 0, 0

            while word[word_pointer] == comp[comp_pointer] and word_pointer < len(word) and comp_pointer < len(comp):
                word_pointer += 1
                comp_pointer += 1

            if word_pointer == len(word) or comp_pointer == len(word):
                continue # Nothing to learn between two strings

            # We know that comp_char comes after word_char in the lexicographical ordering, because the word and comp have common prefixes
            word_char = word[word_pointer]
            comp_char = comp[comp_pointer]

            prechars[comp_char].add(word_char)

    print(prechars)

    acc = []
    processed_chars = set()

    def explore_character(char: str) -> None:
        if char in processed_chars:
            return

        processed_chars.add(char)

        # Add all of the characters that come before char
        for prior_character in prechars[char]:
            explore_character(prior_character)

        acc.append(char)

    for char in prechars.keys():
        explore_character(char)

    return "".join(acc)




def test(fn):
    assert fn(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert fn(["z", "x"]) == "zx"

test(alien_dictionary)