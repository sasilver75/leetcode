"""
Palindrome Partitioning

Given a string `s`, partition `s` such that every SUBSTRING of the
partition is a palindrome.

Return all possible palindrome partitionings of `s`
"""

"""
The naivest thing that I could do would be to figure out every possible
partitioning of `s`, and then filter those to the palindromic ones.

Let's try that out first...
"""


def partition(s: str) -> list[list[str]]:
    partitionings = []

    # I think the idea with the recursion is that you either extend the previous partition or create a new one
    def recursive_partition(idx: int, partitioning: list[str]):
        if idx == len(s):
            partitionings.append(partitioning)
            return

        char = s[idx]

        # Either extend the previous partition with char or create a new one
        # Create new Partition
        new_partitioning = [*partitioning, char]
        recursive_partition(idx + 1, new_partitioning)

        # Extend Partition if one exists
        if partitioning:
            partitioning[-1] = partitioning[-1] + char
            recursive_partition(idx + 1, partitioning)

    recursive_partition(0, [])

    def is_palindrome(s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    palindromic_partitionings = [
        partitioning
        for partitioning in partitionings
        if all(is_palindrome(part) for part in partitioning)
    ]

    return palindromic_partitionings


"""
Here's the neetcode solution - it also runs in 2^N, but is good to see.
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

def test(fn):
    assert fn("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert fn("a") == [["a"]]


test(partition)
