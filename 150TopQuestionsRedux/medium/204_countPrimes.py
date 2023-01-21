"""
Count Primes

Given an integer `n`, return the number of prime numbers that are strictly
less than `n`
"""

"""
This is just the sieve of eratosthenes. I'm not interested in learning it.

It finds all prime numbers up to a given limit.

It does so by iteratively marking as COMPOSITE the multiples of each prime, starting with
the first prime number, 2. The multiples of a given prime are generated as a sequence of numbers
starting from that prime.
"""
def count_primes(n: int) -> int:
    if n < 2:
        return 0

    # Numbers are assumed to be prime until disproven
    primes = [True] * (n+1) # 0 .. n   [technically primes[0],primes[1] should be set to false, doesn't matter
    idx = 2

    prime_count = 0
    while idx < len(primes):
        if primes[idx]:
            prime_count += 1

            # Mark all multiples of current prime number as composite
            for multiple_index in range(idx+idx, len(primes), idx):
                primes[multiple_index] = False

        idx += 1

    print(primes, prime_count)
    return prime_count



assert count_primes(10) == 4 # 2, 3, 5, 7
assert count_primes(0) == 0