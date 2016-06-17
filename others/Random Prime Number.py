"""
Write a function to generate a random prime number from 1 to n
"""
from random import randint
def randomPrimeNumber(n):
    lookup = [True for i in range(n)]
    lookup[0] = False
    primes = []
    for i in range(1, n):
        if lookup[i]:
            prime = i + 1
            primes.append(prime)
            cur = prime - 1
            while cur < len(lookup):
                lookup[cur] = False
                cur += prime
    index = randint(0, len(primes) - 1)
    return primes[index]

if __name__ == "__main__":
    n = 100
    print(randomPrimeNumber(n))
