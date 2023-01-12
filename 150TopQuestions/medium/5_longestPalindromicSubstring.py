"""
Longest Palidromic Substring

Given a string s, return the longest palindromic substring in s.

A palindromic substring is a contiguous sub-section of the string that is a palidrome.
"""


"""
Thinking:
* The dumbest possible solution that I can think of is to generate every possible substring, and of all
that are determined to be palindromic, take the max length one.
"""

def longest_palindromic_substring_brute(s: str) -> str:
    def is_palindrome(s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # Recursively generate all possible substrings
    substrings = [] # These brute ones actually don't work wit ha set because they don't preserve the order of the input elements. So example1 may give "aba" instead of "bad"
    max_length_substring = ""


    for i in range(len(s)):
        for j in range(i+1, len(s)):
            substrings.append(s[i:j])

    # For each substring: if it's palindromic, update max_length as appropriate
    for substring in substrings:
        if is_palindrome(substring):
            max_length_substring = substring if len(substring) > len(max_length_substring) else max_length_substring

    print(max_length_substring)
    return max_length_substring




"""
How can we do this in better than O(N^2) time? Is it possible? Sorting isn't useful.
Is there some sort of sliding/expanding window approach that we could use to do it in something closer to O(N) time?


There IS an interesting property about palindromes... If you have a palindrome like ABA... and you glom two C's on the outside of it.... then
you know that you still have a palindrome.
So there's this idea of having some {already-approved-palindrome}, and then "growing" that substring by expanding the window in two directions outward...

I guess the flipside of that would be starting with a very wide window and "shrinking" that window, stopping the shrinking and "moving on" whenever
we get to a window size that's smaller than our largest-so-far-seen?
"""

def longest_palindromic_substring_dynamic_programming(s: str) -> str:
    """
    The problem can be broken down into subproblems that are reused several times.
    Overlapping subproblems lead us to Dynamic Programming.

    Decomposition:
    * State Variables
        - The `start` index and `end` index of a substring can identify a state, which influences our decision
        - So the state variable is state(start, end), indicating whether s[start, end] inclusive is palindromic
    * Goal State
        - max(end - start + 1) for all state(start, end) == True substrings
    * State Transition
        - for start = end (e.g. 'a'), state(start, end) is True
        - for start + 1 = end (e.g. 'aa'), state(start, end) is True IF s[start] = s[end]
        - for start + 2 = end (e.g. 'aba'), state(start,end) is True IF s[start] = s[end]
        - for start + 3 = end (e.g. 'abba'), state(start, end) is True IF s[start] = s[end] AND s[start+1] = s[end-1]

    This approach takes O(N^2) time complexity; O(N^2) space complexity, where n is the length of s.
    """
    n = len(s)
    # It seems this is going to be a 2d table that's start/end indexes (row/column), with a False/True value
    dp = [[False] * n for _ in range(n)]

    # The diagonal (meaning start/end at same point [inclusive -- not meaning indexs of start end])
    for i in range(n):
        dp[i][i] = True
    longest_palindrome_start, longest_palindrome_len = 0, 1

    for end in range(0, n):
        for start in range(end - 1, -1, -1):
            # print(f"Start: {start}, End: {end}")

            if s[start] == s[end]:
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    palindrome_len = end - start + 1
                    if palindrome_len > longest_palindrome_len:
                        longest_palindrome_len = palindrome_len
                        longest_palindrome_start = start

    ans = s[longest_palindrome_start: longest_palindrome_start + longest_palindrome_len]
    print(ans)
    return ans



def longest_palindromic_substring_two_pointers(s: str) -> str:
    """
    This approach also takes O(N^2) time complexity, O(1) space complexity, where n is the length of s.

    For each character s[i], we get the first character to its right which isn't equal to s[i], @ s[right]
    Then, s[i, right - 1] inclusive are KNOWN to be equal characters (e.g. "AAA")
    Then we make left = i - 1, and we increase the size of our window by extending both ends by left -= 1 and right += 1,
    updating the tracked longest palindrome as needed.
    """
    n = len(s)
    longest_palindrome_start, longest_palindrome_len = 0, 1

    for i in range(0, n):
        right = i

        # Expand right while we're in a segment of equal characters ("AAA")
        while right < n and s[i] == s[right]:
            right += 1
        # Now s[o] != s[right], and right may be off the end of the list

        left = i - 1 # This MAY be -1
        # EXPANSION time. While s[left] == s[right], we know that s[left, right] inclusive is a palindrome
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1 # Expand
            right += 1

        # We've expanded as large as we can (actually, one expansion in either direction PAST a "good" state)
        # Let's consider updating our longest_... variables
        # At this point, s[left + 1]...s[right - 1] is palindromic.   Say we're at s[1] and s[5] -- that would mean indexes 2,3,4 are a palindrome.
        # that comes out to {right - left - 1}

        palindrome_len = right - left - 1
        if palindrome_len > longest_palindrome_len:
            longest_palindrome_len = palindrome_len
            longest_palindrome_start = left + 1 # Recall that left is currently at a "violating" position -- so use the "previous" left, left + 1

    ans = s[longest_palindrome_start: longest_palindrome_start + longest_palindrome_len]
    print(ans)
    return ans






assert longest_palindromic_substring_brute("babad") == "bab"
assert longest_palindromic_substring_brute("cbbd") == "bb"
print("---")
assert longest_palindromic_substring_dynamic_programming("babad") == "bab"
assert longest_palindromic_substring_dynamic_programming("cbbd") == "bb"
print("---")
assert longest_palindromic_substring_two_pointers("babad") == "bab"
assert longest_palindromic_substring_two_pointers("cbbd") == "bb"
