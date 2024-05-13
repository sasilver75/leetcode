"""
Word Pattern

Given a PATTERN and a string S, find if S follows
that same pattern.

Here "follows" means a full match -- such that
there is a bijection between a letter in PATTERN
and a non-empty word in S.
"""

"""
Thinking... Okay, so each word needs to get mapped to a letter 
in the pattern. And a word can't be mapped to more than one letter.

If we had a mapping from word: letter...

And then we iterated over the words...
If the current word was not in the mapping 

Constraints:
* A word cannot be mapped to more than one pattern letter
* A pattern letter can only be mapped to a single word
* 
"""

"""
Thinking
        For word in 
        1) Current Pattern Letter IS Free (is not in mapping)
            * ...and the current Word is already used elsewhere
                - return False
            * ... and the current Word is NOT already used elsewhere
                - assign the Pattern Letter: Word and mark Word as used
                - inc PatternLetterIndex
        2) Current Pattern Letter IS NOT Free (is in mapping)
            * ... and is mapped to the current Word
                - inc PatternLetterIndex
            * ... and is mapped to another Word
                - return False

        At any point during iteration, if patternLetterIndex >= len(pattern),
        then you're "out of pattern letters" before you're "out of words," so
        you should probably return False.
        """
def matches(pattern: str, s: str) -> bool:
    claimed_words = set() # Claimed words. Words shouldn't
    mapping = {} # Map of "pattern letter" to word
    pattern_index = 0
    words = s.split()

    # Every word needs to have a corresponding pattern letter
    if len(words) != len(pattern):
        return False
    # Every unique word needs to have a unique pattern letter
    if len(set(words)) != len(set(pattern)):
        return False

    for word in words:
        pattern_letter = pattern[pattern_index]

        # See explanation above
        if pattern_letter not in mapping:
            if word in claimed_words:
                return False
            mapping[pattern_letter] = word
            claimed_words.add(word)
            pattern_index += 1
        else:
            if mapping[pattern_letter] != word:
                return False
            pattern_index += 1


    # If we didn't use up all of the pattern characters, return False
    if pattern_index != len(pattern):
        return False
    return True


"""
Here's another solution from LC:
I've modified it to make more sense
"""
def pattern_matches(p: str, s: str) -> bool:
    words = s.split(' ')
    w_to_p = {}

    # Precondition Checks
    if len(p) != len(words):
        return False # for the case p = 'ab' and w = ['dog'] or w = ['dog', 'cat', 'fish']
    if len(set(p)) != len(set(words)):
        return False # for the case p = 'aa' and w = ['dog', 'cat']

    # By making sure that len(p) == len(words), we don't have to manage two independent pointers.
    # We should be able to just move a single incrementing index across both w/p in lockstep
    # For the given word, if it's claimed, it should be claimed for the current pattern_letter
    for idx, word in enumerate(words):
        pattern_letter = p[idx]
        if word not in w_to_p:
            w_to_p[word] = pattern_letter
        elif w_to_p[word] != pattern_letter:
            return False

    # above: You might have been worried about the same pattern_letter being mapped to in two entries/items
    # of the mapping. That's impossible because of our check that len(set(p)) == len(set(words))

    return True

# Case 1
assert matches("abba", "dog cat cat dog") == True
assert pattern_matches("abba", "dog cat cat dog") == True

# Case 2
assert matches("abba", "dog cat cat fish") == False
assert pattern_matches("abba", "dog cat cat fish") == False

# Case 3
assert matches("aaaa", "dog cat cat dog") == False
assert pattern_matches("aaaa", "dog cat cat dog") == False