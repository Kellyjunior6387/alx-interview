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
    maria = 0
    ben = 0
    for n in nums:
        primes = sieve_of_erastosthenes(n)
        count = sum(primes[2:n+1])
        if count % 2 == 1:
            maria += 1
        elif count % 2 == 0:
            ben += 1
    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
