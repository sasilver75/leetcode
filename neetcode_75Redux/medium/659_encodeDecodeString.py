"""
Encode Decode String

Design an algorithm to encode a list of strings to a string; the encoded string is then
sent over the network, and is decoded by to the original list of strings.

Please implement both Encode and Decode
"""
import string

"""
Okay, so what's the simplest thing that we might think of doing?
We might think of some delimiting character to use, like an & sign.

Okay, so let's join our input string using this separator...
But what if our original string naturally had this separator in it?
We'd have to first replace these natural separators with something like using
an scape character. So we would do something like:

On encode:
1. Replace all natural occurrences of your delimiter with en escaped delimiter
2. Join your list of strings with our delimiter

On decode: 
1. Split on all occurrences of the delimiter
2. For each resulting list element, replace the escape delimiter with the natural occurrence of the delimiter

This guards against natural occurrences of the delimiter, but not against natural
occurrences of the escaped delimiter. We could make our escape character(s) more
complicated, but this would never be a guarantee, as is.

----

A better idea could be to have a smarter delimiter than just a single character?
Our delimiter could possibly be something that encodes each element's length? It could look like anything. For instance we could do something like:
turn ["i", "love", "leetcode"] into (1)i(4)love(8)leetcode
                            or into 1:i4:love8:leetcode 
What's actually important is that we have {number}{thing indicating the end of the number}, which together act as the delimiter.
Once we know the length of the next actual token, we can consider that token individually.
Note that we aren't using delimiters -- why is that? What would happen if there was a natural occurrence of (eg) :26 in our string?
    -> It would be ignored! Because once we encounter a leading length-delimiter, we consider the next {length} characters as dumb characters; we don't even actually consider
    them during the decoding.

On encode:
1. For each token, determine the length of the token
2. Add into the accumulator the {tokenLength}{lengthEndingCharacter}{token}

On decode:
1. While-loop iterating across the encoded string
2. Extract the {tokenLength}, and use it to determine the {token}. Add it to your accumulator, and move the cursor to the beginning of the next tokenLength
"""


def encodeNaive(tokens: list[str]) -> str:
    delimiter = "+"
    escape = "/"

    def clean_token(s: str) -> str:
        return "".join([
            c if c != delimiter else escape+delimiter
            for c in s
        ])

    tokens = [
        clean_token(token)
        for token in tokens
    ]
    encoded = delimiter.join(tokens)
    # print("Encoded: ", encoded)
    return encoded



def decodeNaive(s: str) -> list[str]:
    natural_delimiter = "/+"
    delimiter = "+"
    acc = []
    start = 0
    for end in range(1, len(s)):
        # If it's areal delimiter, and not a natural delimiter
        if s[end] == delimiter and s[end-1:end+1] != natural_delimiter:
            # Everything up to the delimiter is a token
            acc.append(s[start:end])
            start = end+1

    # Remaining token
    acc.append(s[start:end+1])

    def restore(s: str) -> str:
        encoded_delimiter = "/+"
        delimiter = "+"
        acc = []
        i = 0
        while i < len(s):
            if s[i:i+2] == encoded_delimiter:
                acc.append(delimiter)
                i += 2
            else:
                acc.append(s[i])
                i += 1

        return "".join(acc)

    acc = [restore(token) for token in acc]
    # print("Decoded: ", acc)
    return acc



def encodeSmart(tokens: list[str]) -> str:
    acc = []
    for token in tokens:
        token_length = len(token)
        encoded_token = f"{token_length}:{token}"
        acc.append(encoded_token)
    encoded = "".join(acc)
    # print(encoded)
    return encoded


def decodeSmart(s: str) -> list[str]:
    acc = []
    start = 0
    end = 0
    while end < len(s):
        # Seek end forward to the length-ending character
        while s[end] in string.digits:
            end += 1
        token_length = int(s[start:end])
        # print(" Token length: ", token_length)
        token = s[end+1: end+1+token_length]
        # print(" Token: ", token)
        acc.append(token)
        start = end+1+token_length
        end = start

    print(f"{acc = }")
    return acc




for encode, decode in [
    [encodeNaive, decodeNaive],
    [encodeSmart, decodeSmart]
]:
    inpA = ["lint", "code", "love", "you"]
    assert decode(encode(inpA)) == inpA

    inpB = ["we", "say", ":", "yes"]
    assert decode(encode(inpB)) == inpB

