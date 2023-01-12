"""
FizzBuzz

Given an integer n, return a STRING ARRAY answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5
answer[i] == "Fizz" if i is divisible by 3
answer[i] == "Buzz" if i s divisible by 5
answer[i] == i (as a stirng) if none of the above conditions are true
"""


def fizzbuzz(n: int) -> list[str]:
    acc = []

    for i in range(1, n + 1):
        element = ""     # You could do this string-building pattern or you could just have if/elif/elif/else blocks
        if i % 3 == 0:
            element += "Fizz"
        if i % 5 == 0:
            element += "Buzz"
        acc.append(element or str(i))

    print(acc)
    return acc


assert fizzbuzz(3) == ["1", "2", "Fizz"]
assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizzbuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
assert fizzbuzz(1) == ["1"]
assert fizzbuzz(0) == []
assert fizzbuzz(-1) == []