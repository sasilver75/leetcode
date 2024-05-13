"""
Give a string s, find the first NON-REPEATING CHARACTER in it, and
return its index. If it does not exist, return -1.
"""

def first_unique_character(s: str) -> int:
    """
    There's no logical ordering to the characters in the given string
    That is to say, given that we're at char X in s, we don't have
    any way of knowing whether X occurs way later in the string without
    looking at the other characters in the string.
    """
    char_counts = {}
    for char in s:
        if not char in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    # The interesting thing is that dicts in python preserve insertion order
    # So we could either iterate over keys in char_counts or iterate over chars in s
    for idx, char in enumerate(s):
        if char_counts[char] == 1:
            return idx
    return -1


assert first_unique_character("leetcode") == 0
assert first_unique_character("loveleetcode") == 2
assert first_unique_character("aabb") == -1

"""
What if we wanted to use O(1) memory specifically?

We could sort the string, then scan across sequentially in O(nlogn) time!
But we need to be sure to use O(1) memory if we can...

Things like BubbleSort (O(N^2)) or InsertionSort O((N^@)) are O(1) memory
because they're in-place sorts that don't take additional memory.
"""


"""
Now... a string, which is the argument to this function...is immutable
in python. So we can't sort the string in place. WE have to turn it into 
an array, which technically makes this O(N) memory too, on top of O(N^2).
"""
def first_unique_character(s: str) -> str:
    s = [char for char in s] # Turn into array (shh)

    for i in range(1, len(s)):
        key = s[i]
        j = i - 1
        while j >= 0 and s[j] > key:
            s[j+1] = s[j]
            j -= 1

        s[j+1] = key

    s = "".join(s) # Now we have a sorted string! :)
    print(s)

    # What defines a unique character?
    for idx, val in enumerate(s):
        if idx == 0:
            if val != s[idx + 1]:
                return idx
        elif idx == len(s) - 1:
            if val != s[idx - 1]:
                return idx
        else:
            if val != s[idx -1] and val != s[idx + 1]:
                return idx

    return -1

"""
LMAO Oh -- this doesn't actually work. 
Because it's the FIRST unique character that we want.
And while InsertionSort IS a stable sort, it can still change the order
of occurrence of unique characters, assuming there are multiple.
"""

# assert first_unique_character("leetcode") == 0
# assert first_unique_character("loveleetcode") == 2
# assert first_unique_character("aabb") == -1