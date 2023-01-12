"""
Count primes

Given an integer n, return the number of prime numbers
that are STRICTLY LESS THAN n.
"""

# HONESTLY I don't care to learn the sieve of eratostehenes


def count_primes(n: int) -> int:
    if n <= 1:
        return 0

    # This is going to be the dumb solution
    def is_prime(candidate: int):
        for i in range(2, candidate):
            if candidate % i == 0:
                return False
        return True

    count = 0
    for candidate in range(2, n):
        if is_prime(candidate):
            count += 1

    print(count)
    return count


# -- Test Zone --
assert count_primes(10) == 4
assert count_primes(0) == 0
assert count_primes(1) == 0