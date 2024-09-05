#!/usr/bin/python3
"""Module to implement the prime game number"""


def sieve_of_erastosthenes(n: int):
    """Function to find all find prime numbers up to  n """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes


def isWinner(x, nums):
    """Function to simulate prime geam winner"""
    if x == 0 or not nums:  # No rounds to play
        return None
    max_n = max(nums) if nums else 0
    primes = sieve_of_erastosthenes(max_n)
    prime_count_up_to = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count_up_to[i] = prime_count_up_to[i - 1] + (1 if primes[i] else 0)

    maria = 0
    ben = 0

    for n in nums:
        if n == 1:  # Special case: if n is 1, Ben automatically wins
            ben += 1
            continue

        count = prime_count_up_to[n]  # Get number of primes up to n
        if count % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
