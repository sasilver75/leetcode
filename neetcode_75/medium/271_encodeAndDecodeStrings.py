"""
Encode and Decode Strings
Category: String

Design an algorithm to encode a list of strings
to a string. The encoded string is then sent over
the network and is decoded back to the origianl list of
strings.
"""
import string

"""
I think the idea here is that you want to have some sort of 
separator/delimiter in the encoding method to join your list element into a string
with.
So maybe
["hi", "there", "buddy"] 
becomes 
"hi%there%buddy"
and then if we decode by splitting on %:
["hi" "there" buddy"]

Except what if the strings were actually
["hi%", "there", "buddy"] and this was valdi?
becomes
"hi%%there%buddy%"
And then if we decode by splitting on %:
["hi", "", "there", "buddy"]
Okay... but what if we just split on ANY number of %s?
Well we what if we had this?:
["hi", "th%re", "buddy"]
That would be encoded into
"hi%th%re%buddy"
Which would then be decoded into
["hi", "th", "re", "buddy"], which isn't right!

Two options, I think:
 1) We can append either prepend and escape character to a user-supplied delimiting character during encoding
Escape: \
["hi", "th%re", "buddy"]
encoded: "hi%th\%re%buddy"
decoded: ["hi", "th%re" "buddy"]
This then pretty much supposes that the user will never enter a "valid" \% sequence,
which may or may not be a good assumption. Eh!

2) We could encode information about each string's length?
["hi", "th%re", "buddy"]
encoded: 2/hi5/th%re5/buddy
decoded: [hi th%re buddy]
This one actually is resilient to the string using {num}/ in the original
string. Let's look at it:
["hi", "th%re", "bu/2dy"]
encoded: 2/hi5/there6/bu/2dy
decoded: hi th%re bu/2dy
This works because the decoding pretty much "ignores" any of the characters 
after length/, with respect to splitting. But we have to process it intelligently.
"""

class Solution:
    def encode(self, strs: list[str]) -> str:
        acc = ""
        for s in strs:
            length = len(s)
            token = str(length) + "/" + s
            acc += token
        print(acc)
        return acc

    def decode(self, s: str) -> list[str]:
        # 2/hi5/th%re5/buddy
        acc = []
        l = 0
        r = 0

        while l < len(s):
            # Assuming this is a "valid" encoding
            while s[r] in string.digits:
                r += 1

            # r is now at /
            next_word_length = int(s[l:r])
            acc.append(s[r+1: r+1+next_word_length])

            l = r+1+next_word_length
            r = r+1+next_word_length

        print(acc)
        return acc







# -- Test --
def test(clazz):
    sol = clazz()
    assert sol.decode(sol.encode(["lint", "code", "love", "you"])) == ["lint", "code", "love", "you"]
    assert sol.decode(sol.encode(["we", "say", ":", "yes"])) == ["we", "say", ":", "yes"]
    assert sol.decode(sol.encode(["hi", "th%re", "bu/2dy"])) == ["hi", "th%re", "bu/2dy"]

test(Solution)