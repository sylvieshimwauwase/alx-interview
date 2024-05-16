#!/usr/bin/python3
"""performing prime numbers game"""


def isWinner(x, nums):
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Function to get primes up to n
    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    # Function to simulate the game
    def play_game(n):
        primes = get_primes(n)
        if len(primes) % 2 == 0:
            return "Ben"  # If there are even number of primes, Ben wins
        else:
            return "Maria"  # If there are odd number of primes, Maria wins

    # Play each round and keep track of the winners
    wins = {"Maria": 0, "Ben": 0}
    for i in range(x):
        winner = play_game(nums[i])
        wins[winner] += 1

    # Determine the player with the most wins
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
