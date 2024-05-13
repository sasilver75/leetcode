"""
Palindrome Partitioning

Given a string `s`, PARTITION `s` such that every substring
of that partition is a palindrome!

Return all possible palindrome partitionings of s.
"""

"""
Sam Translation:
Partitioning = breaking s into N pieces

Return all possible partitionings for which each sub-partition is a palindrome
"""

def partition_brute(s: str) -> list[list[str]]:
    # Generate all partitions
    all_partitions = []
    def helper(idx: int, partitions: list[str] = None) -> None:
        if partitions is None:
            partitions = []

        if idx >= len(s):
            all_partitions.append(partitions)
            return

        """
        At current index, either:
         1) extend the current partition by setting partitions[-1] = partitions[-1] + char
         2) create a new partition via partitions.append(char)
        """
        char = s[idx]
        # Extend Current Partition (if there is one)
        if partitions:
            extended_p = [*partitions]
            extended_p[-1] = extended_p[-1] + char
            helper(idx+1, extended_p)

        # New Partition
        new_p = [*partitions, char]
        helper(idx+1, new_p)

    helper(0)

    # Filter to Partitions containing elements that are all palindromes
    def is_palindrome(s: str) -> int:
        l , r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    palindromic_partitionings = [
        partitioning for partitioning in all_partitions if all(is_palindrome(partition) for partition in partitioning)
    ]

    print(palindromic_partitionings)
    return palindromic_partitionings

"""
Okay, is there a way that we can do this in better than 2^N time?

Neetcode:

We want to partition the string s such that every substring of the partition
is a palindrome.

The Brute Force was to solve this problem also happens to be the main way 
to solve this problem, which is "backtracking"
-> We'll create every single possible way to partition this, and then 
determine if each way is a palindrome, and if they are, add them to a result
list.


                 aab
    a           aa          aab[NO]
a   ab[NO]       b
b

This is one possible way to partition the string AAB
This is how you solve it with backtracking, in 2^N
"""

def partition_brute_neetcode(s: str) -> list[list[str]]:
    res = []
    partition = []

    def is_palindrome(i: int, j: int):
        # Is s[i:j+1] a palindrome?
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def dfs(i: int):
        if i >= len(s):
            res.append(partition.copy())
            return

        # Generate every possible substring from i to j. Checking if it's a palindrome, recursively continuing if it is
        for j in range(i, len(s)):
            if is_palindrome(i, j):
                partition.append(s[i:j+1])
                dfs(j+1)
                partition.pop()

    dfs(0)
    return res



# Test Zone
def test(fn):
    ans1 = fn("aab")
    assert all(lst in ans1 for lst in [["a", "a", "b"], ["aa", "b"]])
    ans2 = fn("a")
    assert all(lst in ans2 for lst in [["a"]])

test(partition_brute) # Yay! :)
test(partition_brute_neetcode) # Yay! :)