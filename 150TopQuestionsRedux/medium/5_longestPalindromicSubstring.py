"""
Longest Palindromic Substring

Given a string s, return the LONGEST PALINDROMIC SUBSTRING in s
"""


def lps_naive(s: str) -> str:
    # Generate all Substrings
    substrings = []
    for starting_index in range(len(s)):
        for ending_index in range(starting_index, len(s)):
            substrings.append(s[starting_index: ending_index + 1])

    # Filter to Palindromic Substrings
    def is_palindrome(s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    palindromic_substrings = [
        ss for ss in substrings
        if is_palindrome(ss)
    ]
    # Return the longest one
    ans = max(palindromic_substrings, key=len)
    print(ans)
    return ans


"""
Can we do better?
The above one is O(N^2) to generate the substrings, then another O(N) for each substring to check each one for being a palindrome.
I think it's O(N^3)

Can we do it in O(N^2)? I think so! We could start at each character in the substring, and "grow" a window outwards!
Say that we have "babad". Perhaps we start with a window at "b[a]bad", of length 1 (any substring of length 1 is a palindrome)
And then we can expand teh window by just considering the two characters on the outside of the palindrome window.
Because we know a{short}a is itself a {longer palindrome}.

Note that we don't actually need to use any memory to keep a window -- just a pair of pointers -- we can compute the length from teh pointers (r - l + 1)

There's one complication though -- if we start with windows of length 1 and then expand on eitehr side outward from it, we'll only be considering odd-lengthed palindromes.
We needto do another pass through using bases of length TWO!, to capture palindromes like ABBA. We only start expanding when i,i+1 are equal to eachother, though.
"""


def lps(s: str) -> str:
    max_length_palindrome = ""
    # Considering Odd-Length Palindromes
    for starting_index in range(len(s)):
        left = right = starting_index
        # Expand the window while possible based on both the length of the string and on palindrome rules
        while (
                left - 1 >= 0 and
                right + 1 < len(s) and
                s[left - 1] == s[right + 1]  # Would maintain the palindrome rule
        ):
            left -= 1
            right += 1
        max_length_palindrome = max_length_palindrome if len(max_length_palindrome) > right - left + 1 else s[left: right+1]

    # Considering Even-Length Palindromes
    for starting_index in range(len(s) - 1):
        if s[starting_index] == s[starting_index + 1]:
            left = starting_index
            right = starting_index + 1
        while (
                left - 1 >= 0 and
                right + 1 < len(s) and
                s[left - 1] == s[right + 1]  # Would maintain the palindrome rule
        ):
            left -= 1
            right += 1
        max_length_palindrome = max_length_palindrome if len(max_length_palindrome) > right - left + 1 else s[left: right+1]

    print(max_length_palindrome)
    return max_length_palindrome


def test(fn):
    assert fn("babad") in ["bab", "aba"]
    assert fn("cbbd") == "bb"
    assert fn("tacocat") == "tacocat"


# test(lps_naive)
test(lps)
