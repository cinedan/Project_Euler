"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import sys
import math


# O(sqrt(n)) time primality check
def __checkPrime(n):
  for i in range(2, math.ceil(n**0.5)):
    if n % i == 0:
      return False
  return True

# # the time complexity of this naive solution should be O(sqrt(n) * sqrt(n))  = O(n)
# # it seems like it should not work if the largest factor is > sqrt(n)
# def naive(n):
#   large = 1
#   for i in range(1, math.ceil(n**0.5)):
#     # if this larger i is prime and it divides n then set large equal to it
#     large = i if __checkPrime(i) and n % i == 0 else large
#   return large

# the time complexity of this naive solution should be O(n * sqrt(n))
def naive(n):
  large = 1
  for i in range(1, n):
    # if this larger i is prime and it divides n then set large equal to it
    large = i if __checkPrime(i) and n % i == 0 else large
  return large

# the time complexity of this solution should be O(m * sqrt(m)), where m is the largest prime factor of n
def better(n):
  return __naive_aux(n, 2)

def __naive_aux(n, start):
  if __checkPrime(n):
    return n
  for i in range(start, math.ceil(n**0.5)):
    # if this larger i is prime and it divides n then divide it from n and continue searching from the smaller value
    if __checkPrime(i) and n % i == 0:
      return max(i, __naive_aux(n // i, i + 1))


# a prime spiral would probably be more efficient here...
if __name__ == '__main__':
  if len(sys.argv) != 2:
    n = 600851475143
  elif sys.argv[1].isdigit():
    n = int(sys.argv[1])
  else:
    n = 600851475143

  print(naive(n))
  print(better(n))
