"""Finds Primes and if two primes make a target sum."""
import math

# Prime samples: 2, 3, 5, 7, 11, 13, 17, 19

def is_it_prime(num):
    """
    Is our number prime?
    """
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def two_primes(num):
    """
    Do two primes add up to our num?
    """
    for i in range(2, num):
        if is_it_prime(i):
            compliment = num - i
            if is_it_prime(compliment) and i + compliment == num:
                return i, compliment

################################################################################

N = 23

RESULT = two_primes(N)
if RESULT:
    print(RESULT)
else:
    print("There are no two primes that add up to", N)

# Prompt:
#   Every even integer greater than 2 can be expressed as the sum of two primes.
#   Write a method that tests this conjecture given an integer.
