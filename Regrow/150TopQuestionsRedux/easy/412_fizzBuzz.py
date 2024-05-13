"""
Fizz Buzz! The Classic

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""


def fizz_buzz(n: int) -> list[str]:
    acc = []
    for i in range(1, n+1):
        """
        TBH this += isn't as good as just if/elifs, since strings are immutable and += involves doing a linear-time recreation of a string
        """
        v = ""
        if i % 3 == 0:
            v += "Fizz"
        if i % 5 == 0:
            v += "Buzz"

        if len(v) == 0:
            v = str(i)

        acc.append(v)
    print(acc)
    return acc


assert fizz_buzz(3) == ["1", "2", "Fizz"]
assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizz_buzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                         "FizzBuzz"]
